# Benchmark study of the two-dimensional Hubbard model with auxiliary-field quantum Monte Carlo method

Mingpu Qin, Hao Shi, and Shiwei Zhang
Department of Physics, College of William and Mary, Williamsburg, Virginia 23187, USA
(Received 3 June 2016; revised manuscript received 9 July 2016; published 4 August 2016)

Ground-state properties of the Hubbard model on a two-dimensional square lattice are studied by the auxiliary-field quantum Monte Carlo method. Accurate results for energy, double occupancy, effective hopping, magnetization, and momentum distribution are calculated for interaction strengths of $U/t$ from 2 to 8, for a range of densities including half-filling and $n = 0.3,0.5,0.6,0.75$, and 0.875. At half-filling, the results are numerically exact. Away from half-filling, the constrained path Monte Carlo method is employed to control the sign problem. Our results are obtained with several advances in the computational algorithm, which are described in detail. We discuss the advantages of generalized Hartree-Fock trial wave functions and its connection to pairing wave functions, as well as the interplay with different forms of Hubbard-Stratonovich decompositions. We study the use of different twist angle sets when applying the twist averaged boundary conditions. We propose the use of quasirandom sequences, which improves the convergence to the thermodynamic limit over pseudorandom and other sequences. With it and a careful finite size scaling analysis, we are able to obtain accurate values of ground-state properties in the thermodynamic limit. Detailed results for finite-sized systems up to $16 \times 16$ are also provided for benchmark purposes.

DOI: 10.1103/PhysRevB.94.085103

## I. INTRODUCTION

The two-dimensional (2D) Hubbard model [1] is one of the simplest models that are relevant to many correlated electron phenomena including interaction-driven metal-insulator transitions [2], spin and charge density waves [3], magnetism [4], and superconductivity [5]. The ability to predict the properties of the 2D Hubbard model is crucial to our understanding of the related exotic quantum states and the transition between them. Though the one-dimensional Hubbard model is exactly solvable [6], no exact solution for the Hubbard model exists in two or higher dimensions except for a few special parameter values.

The ground-state property of the 2D Hubbard model has been investigated by a variety of methods that have both strengths and weaknesses in different regions of the parameter space. In a recent work [7], the 2D Hubbard model was studied by state-of-the-art numerical methods [8-15]. In the present paper, we provide a detailed account of the auxiliary-field quantum Monte Carlo (AFQMC) study in Ref. [7], introduce two methodological advances that improve the accuracy and efficiency of AFQMC calculations, and present systematic results for finite-size supercells and detailed analysis of the scaling to the thermodynamic limit. Because of the high accuracy of AFQMC, the results in this paper will be able to serve as benchmarks for future calculations and method development. Such benchmarks will be very valuable given the fundamental nature of the Hubbard model.

In addition to the detailed and systematic data, we propose here the use of a quasirandom sequence that reduces the fluctuations and accelerates convergence when implementing twist averaged boundary conditions (TABC). We test this approach and study the convergence of different boundary conditions. The quasirandom twist is applicable to all many-body calculations of extended systems, including realistic electronic structure calculations in correlated materials.

We also describe the use of generalized Hartree-Fock (GHF) trial wave functions over the more standard unrestricted Hartree-Fock (UHF) form, and discuss how and when improvement in accuracy and efficiency results, both at half-filling and in the doped regime. The connection between the GHF form for magnetic correlations (repulsive model, half-filling) and the BCS form for superconducting order (attractive, spin-balanced model) is discussed, as well as their relation to the form of the many-body propagators and their symmetry properties. Such wave functions can be readily generalized to other quantum Monte Carlo calculations in many-electron systems.

At half-filling in the repulsive Hubbard model, the result from AFQMC is numerically exact and the method is computationally very efficient. Away from half-filling, AFQMC methods suffer from the minus sign problem [16,17] associated with Fermi statistics which leads to exponentially growing statistical errors with system size and inverse temperature. We employ the constrained path formalism under AFQMC, commonly referred to as constrained path Monte Carlo (CPMC), to control the sign problem by introducing a trial wave function to guide the walk in the Slater determinant space. This restores the algebraic computational scaling as in the half-filled case, but introduces a possible systematic error. The goal of considering different forms of the trial wave function is to minimize this error, and to improve the prefactor in the algebraic scaling.

The rest of the paper is organized as follows. In Sec. II, we first define the Hubbard model and give a brief summary of the method used in this work. We also introduce the use of twist boundary conditions in computations of finite supercells. In Sec. III, we describe the computational algorithmic advances. The use of a quasirandom sequence in the twist averaged boundary conditions is discussed, with test results presented. We also study the use of GHF trial wave functions and analyze their connection to BCS wave functions. The interplay between the form of the trial wave function and symmetry properties

of the Hubbard-Stratonovich transformation is examined. In Sec. IV, we present detailed, exact numerical finite-size results at half-filling for a range of supercell sizes and boundary conditions, from weak to strong-coupling regimes. A careful finite-size scaling analysis is carried out to extrapolate the computed quantities to the thermodynamic limit. In Sec. V, the results for a system away from half-filling are presented. A short summary in Sec. VI will conclude this paper. The Appendix contains the finite size numerical data including the ground-state energy, double occupancy, and kinetic energy.

## II. MODEL AND METHOD

### A. Hubbard model

The Hubbard model is defined as
$$
H=K+V=-\sum_{i, j, s} t_{i j}\left(c_{i, s}^{\dagger} c_{j, s}+\text { H.c. }\right)+U \sum_{i} n_{i \uparrow} n_{i \downarrow},
\tag{1}
$$
where $K$ and $V$ are the kinetic and interaction terms, respectively. The creation (annihilation) operator on site $i$ is $c_{i, s}^{\dagger}$ ($c_{i,s}$), with $s=\uparrow, \downarrow$ the spin of the electron, and $n_{i,s}$ is the corresponding number operator. We denote the total number of electrons with up and down spin by $N_{\uparrow}$ and $N_{\downarrow}$. In this work, we only consider the spin-balanced ($N_{\uparrow}=N_{\downarrow}$) systems. The filling factor is defined as $n=(N_{\uparrow}+N_{\downarrow})/N$, where $N$ is the total number of lattice sites in the supercell. Half-filling is $n=1$, and away from it the hole density is given by $h=1-n$. We deal with only nearest neighboring and uniform hopping, $t_{i j}=t$ for each near-neighbor pair $\langle i j\rangle$, and set $t$ as the energy unit. The strength of the repulsive interaction is given by $U/t$. With the exception of the $h=1/8$ doping case where a rectangular lattice is studied to accommodate the underlying spin density wave structure, we consider supercells of square lattice with size $N=L \times L$.

In order to better extrapolate to the thermodynamic limit (TDL), we use TABC [18]. As shown in Sec. IV, the standard periodic boundary conditions (PBC) turns out to give nonmonotonic convergence with supercell size. Under twist boundary conditions (TBC), an electron gains a phase when hopping across the boundaries:
$$
\Psi\left(\ldots, \mathbf{r}_{j}+\mathbf{L}, \ldots\right)=e^{i \hat{\mathbf{L}} \cdot \boldsymbol{\Theta}} \Psi\left(\ldots, \mathbf{r}_{j}, \ldots\right),
\tag{2}
$$
where $\hat{\mathbf{L}}$ is the unit vector along $\mathbf{L}$, and the twist angle $\boldsymbol{\Theta}=(\theta_{x},\theta_{y})$ is a parameter, with $\theta_{x}$ ($\theta_{y}$) $\in [0,2\pi)$. This is equivalent to placing the lattice on a torus topology and applying a magnetic field, which induces a flux of $\theta_{x}$ along the $x$ direction (and a flux of $\theta_{y}$ along the $y$ direction). In Eq. (2), the translational symmetry is explicitly broken, but we can also choose another gauge with which the translational symmetry is preserved, i.e., adjust $t$ to $t \times e^{i\theta_{x}/L}$ along $x$ and $t \times e^{i\theta_{y}/L}$ along $y$. By imposing a random TBC, the possible degeneracy of the noninteracting energy levels is lifted by breaking the rotational symmetry of the lattice. This eliminates the so-called open-shell effects.

To implement TABC, we choose a set of $N_{\theta}$ twist angles and carry out the calculation for each separately. The constrained path condition can be generalized straightforwardly to the case of TBC [19]. The computational cost is thus nominally $N_{\theta}$ times that of a single calculation for, say, the PBC. However, by averaging the same physical quantities from all the calculations, the statistical error bar of the TABC value of the given quantity is reduced. As will be discussed later, the associated statistical uncertainty can be estimated from the distribution among the twist angles. For noninteracting systems, the TABC energy at half-filling approaches the exact TDL value as $N_{\theta}$ is increased. However, if the canonical ensemble is used with fixed particle number $N$, the TABC result with $N_{\theta} \to \infty$ is in general not equal to the TDL value [18,20]. This is the case away from half-filling in the 2D Hubbard model. (Of course, the discrepancy goes to zero as the system size $N$ is increased.)

The use of TABC and the treatment of finite-size effects, including the effect from electron correlations, have been discussed earlier [19,21,22]. The quasirandom sequence we discuss below can be directly applied in this framework. Recently, another method has been proposed to reduce the one-body finite-size effect in the Hubbard model by modifying the energy levels of the free electron part of the Hamiltonian in a way consistent with the corresponding one-particle density of states in the TDL [23]. In this work, we have chosen to treat the original Hubbard Hamiltonian, since part of our goal is to produce benchmark data for finite-size supercells.

### B. Auxiliary-field Monte Carlo method

In this section, we will briefly introduce the AFQMC [24] method. (For a comprehensive discussion of this method, see Ref. [25].) By repeatedly applying the projection operator to a state $|\psi_{0}\rangle$ whose overlap with the ground state $|\psi_{g}\rangle$ of the Hamiltonian $H$ in Eq. (1) is nonzero, we can obtain $|\psi_{g}\rangle$
$$
|\psi_{g}\rangle \propto \lim_{\beta \to \infty} e^{-\beta H}|\psi_{0}\rangle
\tag{3}
$$
and the expectation value of an operator $O$ can be calculated as
$$
\langle O\rangle=\frac{\langle\psi_{0}|e^{-\beta H} O e^{-\beta H}|\psi_{0}\rangle}{\langle\psi_{0}|e^{-2 \beta H}|\psi_{0}\rangle}.
\tag{4}
$$

Through the Trotter-Suzuki decomposition, we can decouple the kinetic and interaction part in the projection operator:
$$
e^{-\beta H}=(e^{-\tau H})^{n}=(e^{-\frac{1}{2} \tau K} e^{-\tau V} e^{-\frac{1}{2} \tau K})^{n}+O(\tau^{2}),
\tag{5}
$$
where $\beta=\tau n$. The Trotter error can be eliminated by an extrapolation of $\tau$ to 0. We typically choose $\tau=0.01$ in this work, with which we have verified that the Trotter error is below the targeted statistical errors.

We usually choose $|\psi_{0}\rangle$ as a Slater determinant in AFQMC. The one-body term $e^{-\frac{1}{2} \tau K}$ can be directly applied to it and the result is another Slater determinant. This does not hold for the two-body term $e^{-\tau V}$. However, we can decompose the two-body term into an integral of one-body terms through the so-called Hubbard-Stratonovich (HS) transformation. There exist different types of HS transformations for $e^{-\tau V}$. The two commonly used types in the literature are the so-called spin decomposition
$$
e^{-\tau U n_{\uparrow} n_{\downarrow}}=e^{-\tau U(n_{\uparrow}+n_{\downarrow})/2} \sum_{x=\pm 1} \frac{1}{2} e^{\gamma_{s} x(n_{\uparrow}-n_{\downarrow})},
\tag{6}
$$

with the constant $\gamma_{s}$ is determined by $\cosh(\gamma_{s}) \equiv \exp(\tau U/2)$, and the charge decomposition
$$e^{-\tau U n_{\uparrow} n_{\downarrow}}=e^{-\tau U\left(n_{\uparrow}+n_{\downarrow}-1\right) / 2} \sum_{x= \pm 1} \frac{1}{2} e^{\gamma_{c} x\left(n_{\uparrow}+n_{\downarrow}-1\right)},\qquad(7)$$
with $\cosh(\gamma_{c}) \equiv \exp(-\tau U/2)$ [26]. Here, $x$ is an Ising-spin-like auxiliary field. Different choices of the HS can lead to different accuracies or efficiencies, because of symmetry considerations [27,28] or other factors [29]. We will further comment on the decompositions later.

After the HS transformation, Eq. (4) turns into
$$\langle O\rangle=\frac{\sum_{\left\{X_{i}, X_{j}\right\}}\left\langle\psi_{0}\left|\prod_{i=1}^{n} P_{i}\left(X_{i}\right) O \prod_{j=1}^{n} P_{j}\left(X_{j}\right)\right| \psi_{0}\right\rangle}{\sum_{\left\{X_{i}, X_{j}\right\}}\left\langle\psi_{0}\left|\prod_{i=1}^{n} P_{i}\left(X_{i}\right) \prod_{j=1}^{n} P_{j}\left(X_{j}\right)\right| \psi_{0}\right\rangle},\qquad(8)$$
where $X_{i}$ is the collection of the $N$ auxiliary fields introduced by the HS transformation, and $P_{i}$ is the product of the kinetic term $e^{-\frac{1}{2} \tau K}$ and the one-body terms from the HS transformation at time slice $i$. The multi-dimensional integrals can then be computed by Monte Carlo methods, e.g., with the Metropolis algorithm.

At half-filling, the denominator of Eq. (8) is always non-negative because of particle-hole symmetry [4]. Away from half-filling, the denominator of Eq. (8) will, in general, become negative for some auxiliary fields. In this situation the direct evaluation of Eq. (8) by Monte Carlo will suffer from the sign problem [16,17]. The sign problem can be eliminated by the constrained path approximation. The framework within which this has been implemented in a Hubbard-like model has been referred to as the constrained path Monte Carlo (CPMC) method [30]. To ensure the denominator in Eq. (9) is positive, we constrain the paths of auxiliary fields so that the overlap with $|\psi_{T}\rangle$, computed at each time slice, remains non-negative. A description of the CPMC method for Hubbard-like models can be found in Ref. [32].

In CPMC, the wave function is represented as a linear combination of a set of slater determinants, which are called walkers. The evolution of the wave function in the imaginary time is represented as random walks in the Slater determinant space by sampling the auxiliary field. Physical quantities can be calculated using the mixed estimator as
$$\langle O\rangle_{\text {mixed }}=\frac{\sum_{k} w_{k}\left\langle\psi_{T}|O| \psi_{k}\right\rangle}{\sum_{k} w_{k}\left\langle\psi_{T}| \psi_{k}\right\rangle},\qquad(9)$$
where $|\psi_{k}\rangle$ is the $k$ th walker, $w_{k}$ is the corresponding weight, and $|\psi_{T}\rangle$ is the trial wave-function we introduced. The mixed estimator is used to compute the energy (and other observables that commute with the Hamiltonian). For observables that do not commute with the Hamiltonian, the mixed estimate is biased, and back propagation is applied to correct for this [30,31].

In order to remove the sign problem, the constrained path approximation in CPMC introduces a systematic error, which depends on the trail wave function $|\psi_{T}\rangle$. With the TBC, a simple generalization of constraint can be made [19]. Previous studies have shown the systematic error is small even with a free-electron or Hartree-Fork trial wave function [19]. We will further discuss the accuracy of CPMC and the role of the trial wave function below in Secs. III B and V.

## III. METHODOLOGICAL DEVELOPMENTS

### A. Quasirandom twist angles
To implement TABC, a set of twist angles need to be chosen. If we only consider how to minimize the one-body finite-size effect [21,22], the problem is related to the calculation of a two-dimensional quadrature. In this section, we compare three choices of random twist angles, i.e., the pseudorandom (PR) sequence, quasirandom (QR) sequence, and uniform grid.

A quasirandom sequence is also known as low-discrepancy sequence, which is a sequence with the property that for all values of $N$, its subsequence $x_{1}, \ldots, x_{N}$ has a low discrepancy. Low discrepancy means that the proportion of points in the sequence falling into an arbitrary set $B$ is close to being proportional to the measure of $B$. Different from a pseudorandom sequence, it fills the sampling space more uniformly at the price of losing some randomness. In this sense, a quasirandom sequence is correlated. We choose the Halton sequences [33] to generate our twist angles in this work. In the uniform grid method, the $N_{\theta x} \times N_{\theta y}$ twist angles are set as
$$\theta_{i j}=\left(\frac{2 \pi}{N_{\theta x}} i, \frac{2 \pi}{N_{\theta y}} j\right),\qquad(10)$$
where the integers $i=0, \ldots, N_{x}-1$ and $j=0, \ldots, N_{y}-1$. For pseudorandom twists, we generate the twist $\boldsymbol{\Theta}$ by a pseudorandom number sequence.

The PR and QR twists both have residual errors that are statistical, while the grid will have a systematic residual error. The errors vanish in the limit of a large number of twists, $N_{\theta}$. From two-dimensional quadrature considerations, one would expect the convergence rate, i.e., the residual error as a function of $N_{\theta}$, should be $\frac{1}{\sqrt{N_{\theta}}}, \frac{\ln N_{\theta}}{N_{\theta}}, \frac{1}{N_{\theta}}$ for PR, QR, and the uniform grid, respectively. In Fig. 1, we show the convergence rates of the ground-state energy of the noninteracting Hubbard model ($U=0$) for the $4 \times 4$ lattice at half-filling. The results are

![](./images/811169758815715333_1.jpg)

FIG. 1. The convergence rate of the ground-state energy of the noninteracting Hubbard model computed using TABC with twist angles from QR sequence, PR sequence, and uniform grid. The system is $4 \times 4$ at half-filling. The vertical axis shows the absolute value of the relative error with respect to the exact value, which is $-16/\pi^{2}$.

![](./images/811169758815715333_2.jpg)

FIG. 2. (a) The error bar of the ground-state energy computed from TABC vs the number of twist angles used with twists generated by QR sequence, PR sequence, and the uniform grid. The system is $4\times4$ with 2 up and 2 down electrons, and $U=8$. The ground-state energies are obtained by the ED method. Note the log-log scale of the plot. (b) Similar results for an $8\times8$ lattice at $n=0.5$, with $U=4$, for QR and PR twist angles. The energies are computed by the CPMC method.

consistent with the expectation above. The convergence rate with QR TABC is almost the same as that of the uniform grid, both much faster than with the PR sequence.

In Fig. 2(a), we study an interacting case, with $U=8$ and a filling factor of $n=0.25$ ($N_\uparrow=N_\downarrow=2$), again in a $4\times4$ lattice. We use exact diagonalization (ED) to calculate the ground-state energy for each twist angle. A total of $\bar{N}_\theta=3600$ twist angles are used in each method. To estimate the statistical error bar of the TABC energy for $N_\theta$ ($<3600$) twist angles for QR and PR sequences, we partition all the data into blocks with size $N_\theta$. The standard derivation of the average energies from the $[\bar{N}_\theta/N_\theta]$ blocks then provides an estimate of the desired statistical error. For the uniform grid, we calculate the relative error for each grid size as the difference between its average and that of the entire 3600 twist angles. As in the noninteracting case shown in Fig. 1, the TABC energy using QR sequence converges at a similar rate to that using uniform grid, with both showing faster convergence rate than the PR sequence. Linear fits of the logarithm of the "error bar" versus the logarithm of $N_\theta$ are performed, and are shown in the figure. The slopes of the fit are 0.94(3), 0.508(7), and 0.96(2), respectively, for QR sequence, PR sequence, and the uniform grid. These are consistent with the expected rate mentioned above.

In Fig. 2(b), we plot the result of an $8\times8$ system at $n=0.5$. We use the CPMC method to compute the ground-state energy for each twist in this system, which is well beyond the reach of ED. In the CPMC calculation, the corresponding noninteracting (i.e., free electron) wave function is used as a trial wave function. For many high-symmetry points on a uniform grid of twist angles, the ground state of a noninteracting system is degenerate. In such situations, the trial wave function (of a single Slater determinant) is not unique, and an arbitrary choice without consideration of symmetry properties can affect the accuracy of the CPMC result. (This issue is further discussed below.) To keep the analysis simple here, we only test the PR and QR sequences. A total of 360 twist angles are used for both methods. The same error analysis procedure is employed as in Fig. 2(a). The fitted convergence rate for PR and QR twist angles is 0.54(3) and 1.0(1), respectively, again consistent with the theoretical values.

These examples show that, with QR twist angles, the computed total energy from TABC converges essentially as quickly as with a uniform grid, and is much faster than with PR twists. The use of QR twists allows the advantage of the uniform grid, while overcoming two of the drawbacks of the latter in QMC calculations. The first drawback of a uniform grid is the degeneracy, which often exists with a high symmetry grid point. As mentioned above, the degeneracy can affect the noninteracting wave function, and correspondingly the quality of the CPMC calculation. (Multideterminant trial wave functions can improve the quality but they require extra handling computationally.) The second disadvantage of the uniform grid is that one needs to determine the size of the grid prior to the calculations. We often cannot reuse the results from a small grid size if a larger grid turns out to be necessary for convergence. On the other hand, QR sequences are cumulative. Given that in QMC one has both statistical and convergence errors present, it is desirable to be able to add additional twist angles "on the fly" as we accumulate better indications of the magnitude of the associated errors. The QR TABC makes this possible: one can add QR twists one by one until a desired accuracy is reached.

### B. GHF trial wave functions in AFQMC and their connections to BCS wave functions

When the sign problem is present, we use a trial wave function (TWF) to constrain the random walk paths in AFQMC. The sign or phase of the overlap of the sampled Slater determinants with the TWF is evaluated in each step, and this is used as a gauge condition which determines or modifies the acceptance of the move [25,30]. The constraint eliminates the sign or phase instability and restores the low-power (third power of system size here) computational scaling, at the cost of introducing, in most cases, a systematic bias. The quality of the TWF can affect the accuracy of the results. In this work, we employ only single Slater determinant TWFs, which have been shown to provide accurate results in many systems. In Hubbard-like models, the most common choices have been the free-electron wave function or the unrestricted Hartree-Fock (UHF) solution. The two choices each have advantages and disadvantages. The UHF is the best single Slater determinant variationally, however, it breaks the spin and translational

<table>
<caption>Table I. The effect of the trial wave function on the (artificial) constraint and its interplay with the form of the HS transformation. Ground-state energies are shown for $4 \times 4$ with PBC ($U = 4$) at half-filling. The exact ground-state energy is $-13.62192$. The UHF and GHF trial wave functions are also with $U = 4$.</caption>
<tbody>
<tr>
  <th>Trial WF</th>
  <td>HS spin</td>
  <td>HS charge</td>
</tr>
<tr>
  <th>UHF</th>
  <td>$-13.478(2)$</td>
  <td>$-13.6222(2)$</td>
</tr>
<tr>
  <th>GHF</th>
  <td>$-13.623(1)$</td>
  <td>$-13.6223(2)$</td>
</tr>
</tbody>
</table>

symmetry of the system. Both symmetries, on the other hand, are preserved in the free-electron TWF.

In this work, we use a special form of the generalized Hartree-Fock (GHF) [34] wave function as TWF in the AFQMC calculations. This will increase the computation time by a factor of 2 to 4 in different portions of algorithm, because now the Slater determinant of up and down spin are coupled. However, the usage of the GHF trial wave function will reduce the bias as shown in the discussion below. This is implemented as a UHF with spin order in the $x$-$y$ plane. As we illustrate next, this form combines the advantages of the UHF and free-electron TWFs and performs better than both, even though it is related to the $z$-direction UHF by a spin rotation and is variationally the same.

In Table I, we compare the effects of different TWFs and different HS decompositions. The system is a $4 \times 4$ with PBC and $U = 4$. The spin and charge decompositions are defined in Eqs. (6) and (7), respectively. The AFQMC results have been extrapolated to the $\tau = 0$ limit. The system is at half-filling, where there is no sign problem. The CP calculations can be easily made exact by redefining the importance sampling to have a nonzero minimum [27]. However, we deliberately apply the constraint as usual, which can prevent the walkers from tunneling from one region of the determinant space to another with an artificial boundary where $\langle \psi_T | \psi_k \rangle = 0$, even though both sides are positive. As can be seen, with the spin decomposition, the calculations using the UHF as a TWF leads to a bias.

When the GHF trial wave function is used instead of the UHF, the bias of the spin-decomposition calculation is removed. Below, we further discuss the symmetry properties of the GHF to explain why it is a better TWF. With the charge decomposition, the energies agree well with the exact energy regardless of which trial wave function is used. This is because the auxiliary fields are complex in this case. The sign problem would become a phase problem [35]. However, since we are at half-filling, the overlap $\langle \psi_T | \psi_k \rangle$ turns out to be real and non-negative for all configurations of auxiliary fields. This "two-dimensional" nature of the random walks [29,35] allows ergodicity, and there is no constraint error.

The statistical error bars are also much smaller with the charge than with the spin decomposition for the same amount of computing, as seen in Table I. This is because the former preserves SU(2) symmetry of spin degree of freedom [27]: when we choose as an initial state for the projection the noninteracting wave function [36], all the random walkers will stay in the singlet space throughout the random walks, reducing fluctuations. (When $|\psi_T \rangle$ is used as the initial state as opposed to the noninteracting wave function, the equilibration time becomes much longer [37], and the fluctuations are larger. The final converged results are consistent with each other between the two different initial states, as we would expect.)

<table>
<caption>Table II. Effect of the GHF trial wave function on the constraint. Mean absolute relative errors of the CP ground-state energy are shown from TABC with free, UHF, and GHF trial wave functions. All UHF and GHF trial wave functions are generated with effective $U$ of 4. The system is a $4 \times 4$ lattice with $N_\uparrow = 7$ and $N_\downarrow = 7$. A total of 60 twist angles are used. The TABC results from ED are $-16.3964$ and $-12.1510$ for $U = 4$ and 8, respectively.</caption>
<tbody>
<tr>
  <th>TWF</th>
  <td>$U = 4$</td>
  <td>$U = 8$</td>
</tr>
<tr>
  <th>free</th>
  <td>$0.51(2)\%$</td>
  <td>$1.8\ (1)\%$</td>
</tr>
<tr>
  <th>UHF</th>
  <td>$0.16(2)\%$</td>
  <td>$1.1\ (1)\%$</td>
</tr>
<tr>
  <th>GHF</th>
  <td>$0.21(1)\%$</td>
  <td>$0.51\ (4)\%$</td>
</tr>
</tbody>
</table>

In Table II, we illustrate the effects away from half-filling. We compare the TABC energy of $4 \times 4$, $U = 4,8$ systems at $n = 0.875$ using noninteracting (free), UHF, and GHF trial wave functions. Spin decompositions are used in this case. For simplicity, we use a uniform parameter in the $z$ ($x$) direction for the UHF (GHF) calculation. In principle, we can implement a full UHF (GHF) calculation, which will improve the quality of the trial wave functions. For $U = 4$, the result from GHF is similar to that from UHF. Improvement with the GHF can be seen for the $U = 8$ case, with a CPMC energy closer to the exact value.

Next, we further discuss the nature of the GHF wave function, its connection to Bardeen-Cooper-Schrieffer (BCS) wave functions [38], and correspondingly, the connection between the repulsive Hubbard model we have studied, and the attractive model. Let us consider a partial particle-hole transformation $\hat{P}$, which only involves spin-$\uparrow$ electrons:
$$
\hat{P}^{\dagger} c_{i \uparrow}^{\dagger} \hat{P}=(-1)^{i} c_{i \uparrow} \quad(11)
$$
and
$$
\hat{P}^{\dagger} c_{i \uparrow} \hat{P}=(-1)^{i} c_{i \uparrow}^{\dagger}. \quad(12)
$$

This operator $\hat{P}$ transforms the interaction term in the Hubbard model from repulsive to attractive (from $U$ to $-U$) but leaves the hopping term unchanged.

For the attractive Hubbard model, the best mean-field description is given by the BCS theory,
$$
\begin{array}{r}
\hat{H}_{\mathrm{BCS}}=-t \sum_{\langle i j\rangle, s}\left(c_{i, s}^{\dagger} c_{j, s}+\text { H.c. }\right)+\sum_{i}\left(\Delta_{i} c_{i \uparrow}^{\dagger} c_{i \downarrow}^{\dagger}+\text { H.c. }\right), \\
(13)
\end{array}
$$
where $\Delta_{i}$ is the order parameter. This Hamiltonian can be transformed back to the repulsive case [4,39]
$$
\begin{array}{r}
\hat{H}_{\mathrm{GHF}}=-t \sum_{\langle i j\rangle, s}\left(c_{i, s}^{\dagger} c_{j, s}+\text { H.c. }\right)+\sum_{i}\left(M_{i} c_{i \uparrow}^{\dagger} c_{i \downarrow}+\text { H.c. }\right) \\
(14)
\end{array}
$$
with $M_{i}=(-1)^{i} \Delta_{i}$. The ground state of $\hat{H}_{\mathrm{GHF}}$ is a GHF wave function, with antiferromagnetic order along the $x$-$y$ plane. In other words, the GHF wave function for the repulsive model corresponds to the BCS for the attractive Hubbard model. (The UHF wave function corresponds to a charge-density

wave restricted Hartree-Fock single Slater determinant for the attractive model.)

The symmetry properties of an AFQMC calculation directly affect its accuracy and efficiency [27,28]. The BCS wave function conserves translational symmetry as shown in Eq. (13), while breaking the conservation of particle numbers. In AFQMC calculations of an attractive Hubbard model (with $N_\uparrow = N_\downarrow$ at any density), the walkers will break translational symmetry because of the fluctuating auxiliary fields, which are site-dependent if the charge decomposition is used. However, the walkers remain single determinant with fixed particle numbers. Thus the AFQMC calculation using a BCS trial wave function [38,40] will have all symmetries conserved.

With particle-hole transformation, similar arguments apply to the GHF wave function in the repulsive case. Particle-number symmetry translates to spin symmetry along the $x$-$y$ plane. The GHF preserves all the other symmetries except magnetic order in the plane. When combined with UHF-type walkers, which always preserve magnetic order in the plane, all symmetries are conserved during the AFQMC calculation.

We can also think of BCS or GHF wave functions as linear combinations of single Slater determinants. A BCS wave function can be written as the UHF wave function plus all possible double excitations $(c_{i\uparrow}^\dagger c_{j\downarrow}^\dagger)$, which is a large multideterminant wave function. Similarly, the GHF wave function is the UHF wave function with all possible spin-orbit excitations $(c_{i\uparrow}^\dagger c_{j\downarrow})$, again a multideterminant wave function. It is thus reasonable to expect the GHF wave function to perform better than the UHF.

Incidentally, since the charge decomposition is transformed to the spin decomposition under the particle-hole transformation, results in Table I would indicate that spin decomposition would always give correct results for the attractive Hubbard model. Further, the BCS trial wave functions would have no constraint bias. The latter is consistent with observations from calculations in Fermi gas systems in three [38] and two dimensions [40].

## IV. RESULTS AT HALF-FILLING

In this section, we present results at half-filling. As mentioned, the AFQMC results are numerically exact, as the sign problem is absent because of the particle-hole symmetry. We use a combination of the path-integral approach [40] and the random walk approach [25]. With the former, an infinite variance problem exists, which makes the Monte Carlo error bars unreliable and thus could render results from standard AFQMC calculations incorrect [29]. The infinite variance problem was removed [29] in our calculations, to obtain reliable results and error estimates on the observables. Results are presented for the ground-state energy, double occupancy, effective hopping, and staggered magnetization for $U=2$, 4, 6, and 8. Detailed finite-size data are given, up to $16\times16$, to provide benchmarks for future theoretical and computational studies. Careful extrapolation and analysis are then performed to obtain results at the thermodynamic limit from the finite-size data.

### A. Energy, double occupancy, and effective hopping

We consider three types of boundary conditions here, i.e., PBC, PBC-APBC, and TABC. Here, PBC-APBC means periodic along the $x$ direction and antiperiodic along the $y$ direction, which gives a closed-shell at half-filling. In Fig. 3,

![](./images/811169758815715333_3.jpg)

FIG. 3. Ground-state energy at half-filling calculated using different boundary conditions. PBC, PBC-APBC and TABC data are represented by black triangular, blue star, and red dot, respectively. A fit of the TABC data is also shown, with solid red line. (a), (b), (c), and (d) correspond to results for $U=2,4,6,8$. In the insets of each panel, a zoom of the TABC results and the fit are shown for large supercell sizes. The cyan dot in each inset represents the TDL value and combined statistical and twist error bars and the uncertainty from the fit.

we plot the ground-state energies versus supercell size for all three boundary conditions. Detailed data are given in Appendix. As seen in the table there, our PBC and PBC-APBC data typically range from $4 \times 4$ to $16 \times 16$. Our TABC data contain about 200 twists for the smaller supercells to about 6 twists for $20 \times 20$. The statistical error bars contain joint QMC and twist uncertainties. The fits to reach the TDL are also shown in Fig. 3, with the insets displaying the asymptotic regime with the TABC, from which the TDL values are obtained.

Our fit for the ground-state energy has the following form:
$$
E_{0} / L^{2}=e_{0}+a / L^{3}+b / L^{4}, \tag{15}
$$
where $e_0$ is the energy per site at the TDL. In the large $U$ limit at half-filling, the Hubbard model reduces to the spin-1/2 Heisenberg model with coupling constant $J=4t^2/U$ [41]. From spin density wave theory, the leading order of finite size correction of ground-state energy per site for the latter is $1/L^3$ on a square lattice [42]. This scaling relationship was also confirmed by quantum Monte Carlo calculations [43]. Our scaling choice in Eq. (15), based on these considerations, is seen to fit the data in the Hubbard model with excellent accuracy.

From Fig. 3, we see that the TABC energies tend to lie between the PBC and PBC-APBC results. With PBC and PBC-APBC, the curves are less smooth. In fact the PBC energies are nonmonotonic for $U=4$ and $U=6$. To enter the scaling region of Eq. (15), large system size is needed, which makes extrapolation to the TDL challenging. The finite size effect is reduced with TABC, as expected from our discussion in the previous section. Even at small system sizes, the scaling relationship in Eq. (15) holds well, making the fit more robust comparing to that using PBC and PBC-APBC data. With a least squares fit of the TABC data, a reliable estimate of the ground-state energy in TDL is obtained. For $U=2,4,6$, and 8, the final ground-state energies per site are $-1.1760(2)$, $-0.8603(2)$, $-0.6567(3)$, and $-0.5243(2)$, respectively. (The ground-state energy for $U=4$ is consistent with a previous QMC result $-0.85996(5)$ obtained with a $45^\circ$ tilted supercell [44].)

The magnitude of the finite size effect is seen to decrease with $U$. (Note the vertical scales are different in the different panels.) This is the result of a balance of one-body and two-body finite-size effects. The one-body effects are especially pronounced at low $U$ because of shell effects. The two-body finite-size effects are weakened in the Hubbard model because of the very short-range nature of the interaction. That the TABC results fit the ansatz in Eq. (15) so well across the entire range of lattice sizes for all interactions is an indication of the separation (or additive nature) of the one- and two-body finite-size effects. The relative improvement of TABC over other boundary conditions is the largest at low $U$. At large $U$, the effect of boundary condition is suppressed, and the finite-size effect is dominated by the interaction and the antiferromagnetic correlation. All three boundary conditions give results that fall on the same finite-size curve of Eq. (15) for lattice sizes beyond $L\sim8$.

In Fig. 4, we plot the double occupancy, $D=\langle\sum_i n_{i\uparrow}n_{i\downarrow}\rangle/N$. Similar to the situation with the ground-state energy, the data with TABC lie between the PBC and PBC-APBC data and the finite size effect is reduced by using TABC. We carry out a least squares fit of the TABC data using the scaling relationship given in Eq. (15), although the variation with $L$ is not large compared to the statistical error bars, and the extrapolation is insensitive to the precise form used here. The TDL value obtained by the fits are 0.1923(3), 0.1262(2), 0.0810(1), and 0.0540(1) for $U=2,4,6$, and 8, respectively. The double occupancy decreases rapidly with $U$ as expected.

![](./images/811169758815715333_4.jpg)

FIG. 4. Double occupancy at half-filling calculated using different boundary conditions. Symbols and setup are similar to Fig. 3.

![](./images/811169758815715333_5.jpg)

FIG. 5. The dependence of the effective hopping, $t_{\rm eff}/t$, on the interaction strength $U$ at half-filling. The inset shows the corresponding potential energy in units of the noninteracting kinetic energy.

To help quantify the effect of $U$ on the bandwidth, we calculate the effective hopping $t_{\rm eff}/t$ [45], defined as the ratio of kinetic energy in the presence of $U$ to its noninteracting ($U=0$) value,
$$
\frac{t_{\rm eff}}{t} = \frac{\langle K \rangle_U}{\langle K \rangle_{U=0}}. \tag{16}
$$

The kinetic energy can be obtained straightforwardly by subtracting the potential energy, given by $U$ times the double occupancy discussed above, from the total energy. The effective hopping at the TDL is shown in Fig. 5 as a function of interaction. The decrease of effective hopping with the increase of $U$ is consistent with the increasing of locality, as the system develops stronger antiferromagnetic order, which we characterize next.

We list the data of total energy, double occupancy, and kinetic energy with finite system size from $4 \times 4$ to $16 \times 16$ for PBC and PBC-APBC in Appendix.

### B. Spin correlations and magnetization

To quantify the magnetic properties in the ground state, we compute the spin correlation function,
$$
C(x,y) = \langle \psi_0 | {\bf S}(0,0) \cdot {\bf S}(x,y) | \psi_0 \rangle. \tag{17}
$$

${\bf S}(x,y)$ is the spin operator at site $i$ with coordinate $(x,y)$, which is given by
$$
{\bf S}(x,y) = \frac{1}{2} \sum_{ss'} c_{is}^\dagger \vec{\sigma} c_{is'}, \tag{18}
$$
where $\vec{\sigma}$ denotes the Pauli matrices. In our calculation, translational symmetry is preserved statistically, so the reference point (0,0) can be averaged over the whole lattice to reduce the statistical error. In Fig. 6, we plot the ground-state spin correlation function for system sizes ranging from $4 \times 4$ to $16 \times 16$ under PBC for $U=4$. Long-range order is clearly seen. However, the strength of the correlation decreases substantially from its short-distance values and also as system size is increased, saturating to the asymptotic value very slowly with distance and with system size.

![](./images/811169758815715333_6.jpg)

FIG. 6. Spin correlation function in the ground state at half-filling. System sizes ranging from $4 \times 4$ to $16 \times 16$ are shown, under PBC, with $U=4$. The horizontal axis is the relative distance, $\sqrt{x^2+y^2}$. The top panel shows the spin correlation function, while the bottom panel shows the staggered correlation. The dashed horizontal line in (b) shows the final TDL value obtained from the fit.

We also compute the staggered magnetization. Two definitions are usually used in the literature [43]. One uses the spin-spin correlation function at the greatest distance which, for a square lattice, is $M_1^2 = C(L/2,L/2)$. The other relies on the spin structure factor,
$$
M_2^2 = S(\pi,\pi) = \frac{1}{N} \sum_{i=1}^N (-1)^{x_i+y_i} C(x_i,y_i). \tag{19}
$$

Both definitions have significant finite-size effects, as can be deduced from the results in Fig. 6. We use a modified definition [47]
$$
M(d)^2 = \frac{1}{N-n} \sum_{x_i^2+y_i^2>d^2}^N (-1)^{x_i+y_i} C(x_i,y_i), \tag{20}
$$
where $n$ is the number of sites that fall within a sphere (circle) of radius $d$ centered at the reference point. All three definitions of the magnetization will converge to the same TDL value as $L \to \infty$. However, Eq. (20) gives a compromise which removes the large local effects near the reference point while averaging over multiple distances of the long-range correlation to reduce fluctuations.

The computed magnetizations are plotted in Fig. 7 for $U=4$ and 8. In each case, we show results for a sequence of

![](./images/811169758815715333_7.jpg)

FIG. 7. Magnetization computed with TABC at half-filling for (a) $U=4$ and (b) $U=8$. For each choice of $d$, the result of a fit using the form in Eq. (21) is also plotted. The cyan dot represents the final TDL value and the estimated error bar.

choices of $d$. We fit the computed magnetization as a function of supercell size, for each choice of $d$, with the following scaling form:
$$
M^{2}=M_{0}^{2}+\frac{a}{L}+O\left(\frac{1}{L^{2}}\right),\qquad(21)
$$
where $M_0$ is the staggered magnetization at the TDL. Similar to scaling forms used above, the form in Eq. (21) is motivated by spin-wave theory [46]. The evolution of the fitting with $d$ is illustrated in the figure. The TDL results of magnetizations are $0.119(4),0.236(1),0.280(5)$, and $0.26(3)$ for $U=2,4,6$, and 8, respectively. Note that the $U=2$ result is different from that listed in Ref. [7] which contained an error in the extrapolation to the TDL. An upper bound for the magnetization is given by the value of $0.3070(3)$, from the spin-1/2 Heisenberg model on a square lattice [43]. Our results are consistent with the scenario that the long-range AFM order persists to small $U$ values, with no Mott transition at finite $U$ in the two-dimensional Hubbard model at half-filling.

## V. RESULTS AWAY FROM HALF-FILLING

We next study the ground state when the system is doped. The constrained-path approximation is applied to control the sign problem, as mentioned. Previous studies have shown that the systematic error from the constraint in the CPMC calculation is small in the Hubbard model [19]. We carried out additional benchmarks to further quantify the systematic errors [7]. At low and intermediate densities, the CP errors are small, using free-electron TWFs. At higher densities where magnetic correlation is enhanced, the GHF trial wave function improves the CP result and brings them to a level roughly comparable to that at intermediate densities, as discussed in Sec. III B.

All results reported in this work have thus used single-determinant TWFs. Recent progress has resulted in further improvement in the accuracy of CPMC, by use of symmetry properties [27,28], by constraint release [27], or by improving the trial wave function within CPMC via a self-consistent iteration [48]. We have used multideterminant trial wave functions and constraint release to verify the accuracy in a few systems of larger $L$. The results are consistent with the benchmark discussed above.

### A. Low to medium density

In this section, we present numerical results for densities of $n=0.3,0.5,0.6$, and $0.75$ in the TDL. We first illustrate the finite-size effects and the extrapolation to the TDL with $n=0.5$, which can be precisely realized for any even $L$. In Figs. 8(a) and 8(c), we plot the ground-state energy for $U=4$ and 8, using TABC. The corresponding double occupancy is presented in Figs. 8(b) and 8(d). We have also relaxed the targeted statistical accuracy somewhat compared to half-filling, because of CP systematic errors. Given this and given the large system sizes we compute, the residual finite-size effects are modest. For example, the results from $16\times16$ lattices with TABC are indistinguishable from the extrapolated TDL value within statistical errors. Both quantities are seen to

![](./images/811169758815715333_8.jpg)

FIG. 8. Ground-state energy and double occupancy vs supercell size at $n=0.5$ for $U=4$ and 8. TABC is used. (a) and (b) correspond to $U=4$. (c) and (d) correspond to $U=8$. The solid lines are from a fit using $E_0/L^2(D)\sim e_0(D_0)+a/L^3$.

<table>
<caption>TABLE III. Ground-state energy and kinetic energy per site, and double occupancy for low to intermediate densities at $U = 4$ and 8.</caption>
<tbody><tr>
<td>
</td>
<td>
$n$
</td>
<td>
0.3
</td>
<td>
0.5
</td>
<td>
0.6
</td>
<td>
0.75
</td>
</tr>
<tr>
<td>
$U = 4$
</td>
<td>
$e_0$
</td>
<td>
$-$0.8793(2)
</td>
<td>
$-$1.141(2)
</td>
<td>
$-$1.1845(5)
</td>
<td>
$-$1.1491(2)
</td>
</tr>
<tr>
<td>
</td>
<td>
$D$
</td>
<td>
0.00932(1)
</td>
<td>
0.02740(4)
</td>
<td>
0.0404(1)
</td>
<td>
0.06606(6)
</td>
</tr>
<tr>
<td>
</td>
<td>
$k$
</td>
<td>
$-$0.9166(2)
</td>
<td>
$-$1.251(2)
</td>
<td>
$-$1.3461(6)
</td>
<td>
$-$1.4133(3)
</td>
</tr>
<tr>
<td>
$U = 8$
</td>
<td>
$e_0$
</td>
<td>
$-$0.8534(1)
</td>
<td>
$-$1.066(2)
</td>
<td>
$-$1.0729(1)
</td>
<td>
$-$0.9666(4)
</td>
</tr>
<tr>
<td>
</td>
<td>
$D$
</td>
<td>
0.00442(1)
</td>
<td>
0.01232(2)
</td>
<td>
0.01776(3)
</td>
<td>
0.02847(4)
</td>
</tr>
<tr>
<td>
</td>
<td>
$k$
</td>
<td>
$-$0.8888(1)
</td>
<td>
$-$1.165(2)
</td>
<td>
$-$1.2150(3)
</td>
<td>
$-$1.1944(5)
</td>
</tr>
</tbody></table>

continue to fit well the general form in Eq. (15), being linear in $1/L^3$ for large $L$. With double occupancy, the TABC reduces the finite-size effects substantially. The residual two-body finite-size effects are seen to have opposite slopes for $U = 4$ and 8. Similar behavior is seen in the results at half-filling presented in Fig. 4.

Similar calculations and analysis were carried out for the other densities. For $n = 0.3$ and 0.6, integer fillings are not possible in certain finite systems. In these cases, we interpolate from the results for the nearest two integer fillings. A prior study [19] had computed the equation of state for $U = 4$. Our results in this density range are consistent with theirs. In Table III, we list the ground-state energies, double occupancies, and kinetic energies for all densities studied in this regime for both $U = 4$ and 8.

We also computed the momentum distribution at $n = 0.5$, which is shown in Fig. 9. For each $U$, we plot the results for several twist angles. The $x$ axis is the noninteracting energy for the given momentum normalized by the noninteracting Fermi energy of the corresponding twist. For $U = 4$, we can find a a obvious discontinuity, which is a indicator of the Fermi liquid behavior in this system and agree with an early QMC calculation [49]. For $U = 8$, there is no obvious jump.

### B. $n = 0.875$

The nature of the ground state at $n = 0.875$ is still not completely known. Many competing tendencies are present including spin density wave, charge density wave, and possibly superconducting order [50]. We did not measure the superconducting correlation function in this work. (Prior calculations with CPMC using free-electron trial wave functions did not find long-range pairing correlation in the ground state with the resolution possible then [51].) In a previous study [52], a spin density wave (SDW) ground state with wave length $\lambda = 16$ ($2/h$) was found at $n = 0.875$ and $U = 4$. The computed energies with supercells which are commensurate with the SDW wavelength are seen to be slightly lower than those which are not. Our new GHF trial wave functions gave results consistent with this.

To accommodate the SDW structure, we studied a range of systems with sizes $4 \times 16$, $8 \times 16$, $16 \times 16$, $8 \times 32$, and $8 \times 48$. The energy per site under TABC for these were $-0.7674(7)$, $-0.7658(3)$, $-0.7657(2)$, $-0.7657(4)$, and $-0.7660(3)$, respectively, at $U = 8$. The energies are consistent with each other except for the one with the smallest width of 4. A conservative estimate the ground-state energy in the TDL is $-0.766(1)$. Similarly, the TDL value for $U = 4$ is estimated to be $-1.026(1)$. [The corresponding energy results using free-electron trial wave functions are $-0.773(1)$ and $-1.032(1)$, respectively. Based on the analysis and benchmark discussed earlier, these are expected to be less accurate than the GHF results.] The corresponding double occupancy values are 0.0403(2) for $U = 8$ and 0.0940(3) for $U = 4$.

![](./images/811169758815715333_9.jpg)

## VI. CONCLUSION

The Hubbard model is one of the most fundamental models in many-body physics. It is often used as a test ground as new approaches are developed in the quest to reliably treat interacting fermion systems or correlated materials. In this work, we have presented detailed benchmark results for the ground state of the two-dimensional Hubbard model. The total energy, double occupancy, effective hopping, spin correlation function, and magnetization are computed with the AFQMC method.

At half-filling, the results are numerically exact. By a finite size scaling of the TABC data, the most accurate values to date of these quantities are obtained. We also provide the finite size data for system sizes ranging from $4 \times 4$ to $16 \times 16$ so as to facilitate benchmark of future analytical and computational studies.

Away from half-filling, we employ the constrained path CPMC method, which removes the sign problem and allows

us to systematically reach large system size in the same manner as at half-filling. Prior results and a new set of benchmark calculations here show that the systematic error from the constraint is small. Results are presented from low to intermediate densities for $U/t=4$ and 8. We also study the case of $n=0.875$ with a new form of single Slater determinant trial wave function, obtaining energetics and determining the spin correlations for both values of $U/t$.

In addition to the generalized Hartree-Fock trial wave functions, which we have shown to improve the accuracy of the constraint, we have also introduced the use of quasirandom twist sequences when implementing twist boundary conditions. The quasirandom twists allow convergence with the number of twists, which is as fast as a uniform grid, while eliminating any shell effects from degeneracies in the single-particle levels. The connection between GHF and BCS trial wave functions, and their interplay with the form of Hubbard-Stratonovich transformations will have broader impacts beyond Hubbard models.

## ACKNOWLEDGMENTS

We acknowledge the Simons Foundation for funding. SZ and HS acknowledge support from NSF (DMR-1409510) for AFQMC method development. MQ was also supported by DOE (DE-SC0008627). We thank G. Chan and B.X. Zheng for valuable exchanges and C.-C. Chang for a careful reading of the manuscript. Earlier calculations were carried out at the Oak Ridge Leadership Computing Facility at the Oak Ridge National Laboratory. Most of the calculations were carried out at the Extreme Science and Engineering Discovery Environment (XSEDE), which is supported by National Science Foundation Grant No. ACI-1053575, and the computational facilities at the College of William and Mary.

## APPENDIX: FINITE-SIZE DATA AT HALF-FILLING

In Table IV, we list the total ground-state energy, potential energy, and kinetic energy with PBC and PBC-APBC.

TABLE IV. Total ground-state energy ($E$), potential energy ($P$), and kinetic energy ($K$) in the Hubbard model at half-filling, for $U=2$, 4, 6, and 8. Supercell cell sizes ranging from $4\times 4$ to $16\times 16$ are studied. Results are listed for both PBC and PBC-APBC. Statistical errors are on the last digit and are indicated in parenthesis.

<table>
<thead>
<tr>
<th>
</th>
<th>
</th>
<th colspan="2">$U=2$</th>
<th colspan="2">$U=4$</th>
<th colspan="2">$U=6$</th>
<th colspan="2">$U=8$</th>
</tr>
<tr>
<th>
</th>
<th>
</th>
<th>PBC</th>
<th>PBC-APBC</th>
<th>PBC</th>
<th>PBC-APBC</th>
<th>PBC</th>
<th>PBC-APBC</th>
<th>PBC</th>
<th>PBC-APBC</th>
</tr>
</thead>
<tbody>
<tr>
<td>$4\times 4$</td>
<td>$E$</td>
<td>$-18.024(6)$</td>
<td>$-20.114(2)$</td>
<td>$-13.616(6)$</td>
<td>$-14.594(3)$</td>
<td>$-10.541(4)$</td>
<td>$-10.902(7)$</td>
<td>$-8.476(9)$</td>
<td>$-8.646(8)$</td>
</tr>
<tr>
<td>
</td>
<td>$P$</td>
<td>$5.135(9)$</td>
<td>$6.389(1)$</td>
<td>$7.370(8)$</td>
<td>$9.227(7)$</td>
<td>$7.559(4)$</td>
<td>$8.56(1)$</td>
<td>$6.864(8)$</td>
<td>$7.26(1)$</td>
</tr>
<tr>
<td>
</td>
<td>$K$</td>
<td>$-23.164(3)$</td>
<td>$-26.503(3)$</td>
<td>$-20.989(4)$</td>
<td>$-23.823(8)$</td>
<td>$-18.097(7)$</td>
<td>$-19.46(1)$</td>
<td>$-15.34(2)$</td>
<td>$-15.90(2)$</td>
</tr>
<tr>
<td>$6\times 6$</td>
<td>$E$</td>
<td>$-41.457(5)$</td>
<td>$-43.499(2)$</td>
<td>$-30.865(9)$</td>
<td>$-31.43(2)$</td>
<td>$-23.74(1)$</td>
<td>$-23.84(1)$</td>
<td>$-19.00(2)$</td>
<td>$-19.01(1)$</td>
</tr>
<tr>
<td>
</td>
<td>$P$</td>
<td>$12.522(7)$</td>
<td>$14.357(1)$</td>
<td>$17.43(1)$</td>
<td>$19.21(2)$</td>
<td>$17.276(7)$</td>
<td>$17.78(1)$</td>
<td>$15.51(2)$</td>
<td>$15.67(1)$</td>
</tr>
<tr>
<td>
</td>
<td>$K$</td>
<td>$-53.982(4)$</td>
<td>$-57.857(4)$</td>
<td>$-48.230(8)$</td>
<td>$-50.63(1)$</td>
<td>$-41.012(9)$</td>
<td>$-41.62(1)$</td>
<td>$-34.51(2)$</td>
<td>$-34.69(2)$</td>
</tr>
<tr>
<td>$8\times 8$</td>
<td>$E$</td>
<td>$-74.470(5)$</td>
<td>$-76.308(3)$</td>
<td>$-55.05(1)$</td>
<td>$-55.31(1)$</td>
<td>$-42.16(2)$</td>
<td>$-42.17(2)$</td>
<td>$-33.68(3)$</td>
<td>$-33.66(2)$</td>
</tr>
<tr>
<td>
</td>
<td>$P$</td>
<td>$23.098(5)$</td>
<td>$25.407(6)$</td>
<td>$31.747(8)$</td>
<td>$33.006(9)$</td>
<td>$31.08(2)$</td>
<td>$31.21(1)$</td>
<td>$27.67(2)$</td>
<td>$27.70(2)$</td>
</tr>
<tr>
<td>
</td>
<td>$K$</td>
<td>$-97.565(5)$</td>
<td>$-101.710(8)$</td>
<td>$-86.793(8)$</td>
<td>$-88.314(8)$</td>
<td>$-73.24(2)$</td>
<td>$-73.37(1)$</td>
<td>$-61.30(3)$</td>
<td>$-61.33(3)$</td>
</tr>
<tr>
<td>$10\times 10$</td>
<td>$E$</td>
<td>$-116.908(4)$</td>
<td>$-118.505(4)$</td>
<td>$-86.12(4)$</td>
<td>$-86.20(2)$</td>
<td>$-65.80(2)$</td>
<td>$-65.76(2)$</td>
<td>$-52.54(3)$</td>
<td>$-52.49(2)$</td>
</tr>
<tr>
<td>
</td>
<td>$P$</td>
<td>$36.793(5)$</td>
<td>$39.521(7)$</td>
<td>$50.14(2)$</td>
<td>$50.89(3)$</td>
<td>$48.56(3)$</td>
<td>$48.64(3)$</td>
<td>$43.18(4)$</td>
<td>$43.22(2)$</td>
</tr>
<tr>
<td>
</td>
<td>$K$</td>
<td>$-153.699(5)$</td>
<td>$-158.024(9)$</td>
<td>$-136.23(1)$</td>
<td>$-137.10(2)$</td>
<td>$-114.37(2)$</td>
<td>$-114.41(2)$</td>
<td>$-95.73(3)$</td>
<td>$-95.69(3)$</td>
</tr>
<tr>
<td>$12\times 12$</td>
<td>$E$</td>
<td>$-168.749(7)$</td>
<td>$-170.112(3)$</td>
<td>$-123.95(2)$</td>
<td>$-123.99(3)$</td>
<td>$-94.66(2)$</td>
<td>$-94.67(2)$</td>
<td>$-75.54(2)$</td>
<td>$-75.58(3)$</td>
</tr>
<tr>
<td>
</td>
<td>$P$</td>
<td>$53.616(7)$</td>
<td>$56.629(9)$</td>
<td>$72.52(3)$</td>
<td>$72.96(2)$</td>
<td>$69.96(2)$</td>
<td>$69.96(3)$</td>
<td>$62.23(2)$</td>
<td>$62.20(2)$</td>
</tr>
<tr>
<td>
</td>
<td>$K$</td>
<td>$-222.364(8)$</td>
<td>$-226.741(9)$</td>
<td>$-196.48(1)$</td>
<td>$-196.95(2)$</td>
<td>$-164.64(2)$</td>
<td>$-164.64(2)$</td>
<td>$-137.77(4)$</td>
<td>$-137.74(4)$</td>
</tr>
<tr>
<td>$14\times 14$</td>
<td>$E$</td>
<td>$-229.981(6)$</td>
<td>$-231.134(4)$</td>
<td>$-168.67(2)$</td>
<td>$-168.69(3)$</td>
<td>$-128.76(2)$</td>
<td>$-128.78(3)$</td>
<td>$-102.85(3)$</td>
<td>$-102.83(4)$</td>
</tr>
<tr>
<td>
</td>
<td>$P$</td>
<td>$73.545(8)$</td>
<td>$76.661(8)$</td>
<td>$98.93(3)$</td>
<td>$99.12(3)$</td>
<td>$95.24(2)$</td>
<td>$95.24(2)$</td>
<td>$84.65(3)$</td>
<td>$84.60(4)$</td>
</tr>
<tr>
<td>
</td>
<td>$K$</td>
<td>$-303.530(6)$</td>
<td>$-307.795(8)$</td>
<td>$-267.59(2)$</td>
<td>$-267.82(2)$</td>
<td>$-224.01(2)$</td>
<td>$-224.02(3)$</td>
<td>$-187.49(4)$</td>
<td>$-187.47(4)$</td>
</tr>
<tr>
<td>$16\times 16$</td>
<td>$E$</td>
<td>$-300.596(6)$</td>
<td>$-301.562(5)$</td>
<td>$-220.29(4)$</td>
<td>$-220.30(4)$</td>
<td>$-168.19(3)$</td>
<td>$-168.21(5)$</td>
<td>$-134.23(3)$</td>
<td>$-134.25(3)$</td>
</tr>
<tr>
<td>
</td>
<td>$P$</td>
<td>$96.585(8)$</td>
<td>$99.694(7)$</td>
<td>$129.16(4)$</td>
<td>$129.36(5)$</td>
<td>$124.36(3)$</td>
<td>$124.33(6)$</td>
<td>$110.53(3)$</td>
<td>$110.57(3)$</td>
</tr>
<tr>
<td>
</td>
<td>$K$</td>
<td>$-397.184(8)$</td>
<td>$-401.259(8)$</td>
<td>$-349.52(2)$</td>
<td>$-349.68(2)$</td>
<td>$-292.54(3)$</td>
<td>$-292.57(3)$</td>
<td>$-244.72(5)$</td>
<td>$-244.82(5)$</td>
</tr>
</tbody>
</table>

[1] J. Hubbard, Proc. R. Soc. London, Ser. A 276, 238 (1963).

[2] M. Imada, A. Fujimori, and Y. Tokura, Rev. Mod. Phys. 70, 1039 (1998).

[3] J. Xu, C.-C. Chang, E. J. Walter, and S. Zhang, J. Phys.: Condens. Matter 23, 505601 (2011); R. Peters and N. Kawakami, Phys. Rev. B 89, 155134 (2014).

[4] J. E. Hirsch, Phys. Rev. B 31, 4403 (1985).

[5] P. W. Anderson, Science 235, 1196 (1987); E. Dagotto, Rev. Mod. Phys. 66, 763 (1994).

[6] E. H. Lieb and F. Y. Wu, Phys. Rev. Lett. 20, 1445 (1968).

[7] J. P. F. LeBlanc, A. E. Antipov, F. Becca, I. W. Bulik, Garnet Kin-Lic Chan, C. M. Chung, Y. Deng, M. Ferrero, T. M. Henderson,


C. A. Jiménez-Hoyos, E. Kozik, X. W. Liu, A. J. Millis, N. V. Prokof'v, M. Qin, G. E. Scuseria, H. Shi, B. V. Svistunov, L. F. Tocchio, I. S. Tupitsyn, S. R. White, S. Zhang, B. X. Zheng, Z. Zhu, and E. Gull, *Phys. Rev.* **X 5**, 041041 (2015).

[8] L. F. Tocchio, F. Becca, A. Parola, and S. Sorella, *Phys. Rev.* **B 78**, 041101(R) (2008); L. F. Tocchio, F. Becca, and C. Gros, ibid. **83**, 195138 (2011); N. Trivedi and D. M. Ceperley, ibid. **41**, 4552 (1990).

[9] R. Rodriguez-Guzman, C. A. Jimenez-Hoyos, R. Schutski, and G. E. Scuseria, *Phys. Rev.* **B 87**, 235129 (2013)

[10] R. J. Bartlett and M. Musial, *Rev. Mod. Phys.* **79**, 291 (2007).

[11] S. R. White, *Phys. Rev. Lett.* **69**, 2863 (1992).

[12] G. Knizia and G. K.-L. Chan, *Phys. Rev. Lett.* **109**, 186404 (2012).

[13] T. Maier, M. Jarrell, T. Pruschke, and M. H. Hettler, *Rev. Mod. Phys.* **77**, 1027 (2005).

[14] A. N. Rubtsov, M. I. Katsnelson, and A. I. Lichtenstein, *Phys. Rev.* **B 77**, 033101 (2008).

[15] N. Prokofev and B. Svistunov, *Phys. Rev. Lett.* **99**, 250201 (2007).

[16] E. Y. Loh, Jr., J. E. Gubernatis, R. T. Scalettar, S. R. White, D. J. Scalapino, and R. L. Sugar, *Phys. Rev.* **B 41**, 9301 (1990).

[17] M. Troyer and U.-J. Wiese, *Phys. Rev. Lett.* **94**, 170201 (2005).

[18] C. Lin, F. H. Zong, and D. M. Ceperley, *Phys. Rev.* **E 64**, 016702 (2001).

[19] C.-C. Chang and S. Zhang, *Phys. Rev.* **B 78**, 165101 (2008).

[20] S. A. Cheong, Ph.D. Dissertation, Cornell University, 2006.

[21] S. Chiesa, D. M. Ceperley, R. M. Martin, and M. Holzmann, *Phys. Rev. Lett.* **97**, 076404 (2006).

[22] H. Kwee, S. Zhang, and H. Krakauer, *Phys. Rev. Lett.* **100**, 126404 (2008).

[23] S. Sorella, *Phys. Rev.* **B 91**, 241116 (2015).

[24] R. Blankenbecler, D. J. Scalapino, and R. L. Sugar, *Phys. Rev.* **D 24**, 2278 (1981); G. Sugiyama and S. E. Koonin, *Ann. Phys.* (N. Y.) **168**, 1 (1986).

[25] S. Zhang, *Auxiliary-Field Quantum Monte Carlo for Correlated Electron Systems*, edited by E. Pavarini, E. Koch, and U. Schollwock, Emergent Phenomena in Correlated Matter: Modeling and Simulation Vol. 3 (Verlag des Forschungszentrum Julich, 2013).

[26] J. E. Hirsch, *Phys. Rev.* **B 28**, 4059 (1983).

[27] H. Shi and S. Zhang, *Phys. Rev.* **B 88**, 125132 (2013).

[28] H. Shi, C. A. Jimenez-Hoyos, R. Rodriguez-Guzman, G. E. Scuseria, and S. Zhang, *Phys. Rev.* **B 89**, 125129 (2014).

[29] H. Shi and S. Zhang, *Phys. Rev.* **E 93**, 033303 (2016).

[30] S. Zhang, J. Carlson, and J. E. Gubernatis, *Phys. Rev.* **B 55**, 7464 (1997).

[31] W. Purwanto and S. Zhang, *Phys. Rev.* **E 70**, 056702 (2004).

[32] H. Nguyen, H. Shi, J. Xu, and S. Zhang, *Comput. Phys. Commun* **185**, 3344 (2014).

[33] J. H. Halton, *Commun. ACM* **7**, 701 (1964).

[34] S. H. Schiffer and H. C. Andersen, *J. Chem. Phys.* **99**, 1901 (1993).

[35] S. Zhang and H. Krakauer, *Phys. Rev. Lett.* **90**, 136401 (2003).

[36] For open shell system, we can use TBC with a small twist to break the degeneracy.

[37] W. Purwanto, W. A. Al-Saidi, H. Krakauer, and S. Zhang, *J. Chem. Phys.* **128**, 114309 (2008).

[38] J. Carlson, S. Gandolfi, K. E. Schmidt, and S. Zhang, *Phys. Rev.* **A 84**, 061602 (2011).

[39] R. T. Scalettar, E. Y. Loh, J. E. Gubernatis, A. Moreo, S. R. White, D. J. Scalapino, R. L. Sugar, and E. Dagotto, *Phys. Rev. Lett.* **62**, 1407 (1989).

[40] H. Shi, S. Chiesa, and S. Zhang, *Phys. Rev.* **A 92**, 033603 (2015).

[41] A. H. MacDonald, S. M. Girvin, and D. Yoshioka, *Phys. Rev.* **B 37**, 9753 (1988).

[42] H. Neuberger and T. Ziman, *Phys. Rev.* **B 39**, 2608 (1989); D. S. Fisher, ibid. **39**, 11783 (1989).

[43] A. W. Sandvik, *Phys. Rev.* **B 56**, 11678 (1997).

[44] S. Sorella, *Phys. Rev.* **B 84**, 241110 (2011).

[45] S. R. White, D. J. Scalapino, R. L. Sugar, E. Y. Loh, J. E. Gubernatis, and R. T. Scalettar, *Phys. Rev.* **B 40**, 506 (1989).

[46] D. A. Huse, *Phys. Rev.* **B 37**, 2380 (1988).

[47] C. N. Varney, C. R Lee, Z. J. Bai, S. Chiesa, M. Jarrell, and R. T. Scalettar, *Phys. Rev.* **B 80**, 075116 (2009).

[48] M. Qin, H. Shi, and S. Zhang (unpublished).

[49] A. Moreo, D. J. Scalapino, R. L. Sugar, S. R. White, and N. E. Bickers, *Phys. Rev.* **B 41**, 2313 (1990).

[50] E. Fradkin, S. A. Kivelson, and J. M. Tranquada, *Rev. Mod. Phys.* **87**, 457 (2015).

[51] S. Zhang, J. Carlson, and J. E. Gubernatis, *Phys. Rev. Lett.* **78**, 4486 (1997).

[52] C.-C. Chang and S. Zhang, *Phys. Rev. Lett.* **104**, 116402 (2010).