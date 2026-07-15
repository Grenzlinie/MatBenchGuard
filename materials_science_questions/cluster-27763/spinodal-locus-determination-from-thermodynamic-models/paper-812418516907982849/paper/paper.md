![](./images/812418516907982849_1.jpg)

A study of spatially nonuniform solutions of the first BBGKY equation

Laura Feijoo and Aneesur Rahman

Citation: *The Journal of Chemical Physics* **77**, 5687 (1982); doi: 10.1063/1.443775

View online: http://dx.doi.org/10.1063/1.443775

View Table of Contents: http://scitation.aip.org/content/aip/journal/jcp/77/11?ver=pdfcov

Published by the AIP Publishing

---

Articles you may be interested in

Lattice Boltzmann study of kinetic equation derived from BBGKY hierarchy and non-equilibrium work distributions
AIP Conf. Proc. **1591**, 228 (2014); 10.1063/1.4872553

Nonuniform depth grids in parabolic equation solutions
J. Acoust. Soc. Am. **133**, 1953 (2013); 10.1121/1.4792489

On the solution of the nonuniform Percus–Yevick equation
J. Chem. Phys. **73**, 3507 (1980); 10.1063/1.440507

Towards a molecular theory of freezing: The equation of state and free energy from the first BBGKY equation
J. Chem. Phys. **68**, 3632 (1978); 10.1063/1.436222

On the Solution of the BBGKY Equations for a Dense Classical Gas
J. Math. Phys. **6**, 1496 (1965); 10.1063/1.1704686

---

![](./images/812418516907982849_2.jpg)

# A study of spatially nonuniform solutions of the first BBGKY equation

Laura Feijoo and Aneesur Rahman

Argonne National Laboratory, Argonne, Illinois 60439
(Received 14 May 1982; accepted 23 June 1982)

We investigate the existence of periodic nonuniform solutions of the first BBGKY equation under the assumption, first introduced by Kirkwood and Monroe, that the pair correlations in the solid can be described by the radial distribution function of a disordered metastable phase at the same temperature and density. The calculated one-particle distribution function is used to obtain the equation of state of three systems, namely, hard spheres, rubidium, and Lennard-Jones. The consequences of the central approximation are discussed in the light of our results.

## I. INTRODUCTION

We have reexamined the question $^{1-8}$ of whether it is possible to predict the existence of crystalline order, i.e., a nonuniform periodically repeating one-particle distribution in space, from the pair potential and a suitable approximation for the distribution of pairs of particles. Translational invariance of the Hamiltonian is ordinarily assumed to imply that the one-particle distribution function has a uniform value. This question is related to the fundamentals of statistical mechanics as has been discussed by Kirkwood and Boggs. $^{2}$ In this paper we shall adopt the point of view taken by other authors which is to investigate symmetry broken solutions of the equations which relate the relevant distribution functions.

In the work of Kirkwood and Monroe, $^{1}$ the assumption was made that the pair correlations in the solid can be approximated by the radial isotropic distribution function of a disordered metastable phase, at the same temperature and density.

After Kirkwood and Monroe, other authors $^{3,5-8}$ have proposed theories of freezing based on solving the first equation of the BBGKY hierarchy under the assumption just mentioned concerning the pair function.

Using this approach Raveche and Kayser $^{5}$ found, for the hard-sphere system, solutions which give states with a crystalline one-particle density function; these solutions branch out from the fluid solution at a "bifurcation" point. Their calculation showed that the theory predicts a first order fluid-to-solid phase transition.

The integral equation $^{5,6}$ for the one-particle density of the solid involves the pair potential and a radial distribution function. It can be adapted and solved for systems described by simple continuous pair interactions. Our objective in this paper is to use this possibility.

In Sec. II we explain how we have solved the integral equation for the one-particle density. In Sec. III we summarize our results for the hard-sphere system and compare with those of Raveche and Kayser, $^{5}$ as a check on the method used here. We then apply the same procedure to study two model systems: one, described by the Lennard-Jones (6-12) potential, and the other, by a potential suitable for the study of rubidium metal. $^{9}$
We discuss the central approximation, namely that of Kirkwood and Monroe, $^{1}$ in the light of our results.

## II. THEORY AND METHOD OF CALCULATION

### A. Calculation of $\rho_{1}(r)$

We consider a system of $N$ particles in a volume $\Omega$ interacting via a potential function $v(r_{i j})$ and define the $n$-particle distribution function in the usual way $^{10}$ by

$$
\begin{aligned}
\rho_{n}\left(\mathbf{r}_{1}, \ldots, \mathbf{r}_{n}\right)= & \frac{N!}{(N-n)!} \\
& × \frac{1}{Z} \int_{\Omega} d \mathbf{r}_{n+1} \cdots d \mathbf{r}_{N} \exp \left[-\beta \sum_{i<j} v\left(r_{i j}\right)\right].
\end{aligned}
$$

In particular the pair correlation function is defined by

$$
g_{2}\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right)=\frac{\rho_{2}\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right)}{\rho_{1}\left(\mathbf{r}_{1}\right) \rho_{1}\left(\mathbf{r}_{2}\right)}.
$$

In this case $\rho_{1}$ and $\rho_{2}$ provide enough information to calculate all thermodynamic properties.

Taking the gradient with respect to $\mathbf{r}_{1}$ of the defining expression for $\rho_{1}$ [Eq. (1) with $n=1$ ] we get $^{10}$

$$
\nabla_{1} \ln \rho_{1}\left(\mathbf{r}_{1}\right)=-\beta \int_{\Omega} d \mathbf{r}_{2} \rho_{1}\left(\mathbf{r}_{2}\right) g_{2}\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right) \nabla_{1} v\left(r_{12}\right),
$$

which is the first equation of the BBGKY hierarchy.

We shall assume that the correlation function $g_{2}(\mathbf{r}_{1}, \mathbf{r}_{2})$ of the solid can be approximated $^{1}$ by the radial distribution function $g_{2}^{\text {flud }}(r_{12})$ of a hypothetical fluid at the same temperature and density. Replacing $g_{2}(\mathbf{r}_{1}, \mathbf{r}_{2})$ by $g_{2}^{\text {flud }}(r_{12})$ we obtain the approximate equation for $\rho_{1}$,

$$
\nabla_{\mathbf{r}} \ln \rho_{1}(\mathbf{r})=-\beta \int_{\Omega} d \mathbf{s} \rho_{1}(\mathbf{r}+\mathbf{s}) g_{2}^{\text {flud }}(s) v^{\prime}(s)(\mathbf{s} / s),
$$

where $v'(s)=dv(s)/ds$. Writing $g_{1}(\mathbf{r})=\rho_{1}(\mathbf{r})/\rho$, where $\rho=N/\Omega$, we get

$$
\nabla_{\mathbf{r}} \ln g_{1}(\mathbf{r})=-\beta \rho \int_{\Omega} d \mathbf{s} g_{1}(\mathbf{r}+\mathbf{s}) g_{2}^{\text {flud }}(s) v^{\prime}(s)(\mathbf{s} / s).
$$

We are interested in solutions of Eq. (5) which have the periodicity of a specified lattice. The periodic $g_{1}$ and its logarithm may be expanded in the Fourier series

![](./images/812418516907982849_3.jpg)

FIG. 1. $\|h_{1}\|$ as a function of $\rho$ for a hard-sphere solid with fcc symmetry.

$$
g_{1}(\boldsymbol{r})=\sum_{\{\mathbf{k}\}} \hat{g}_{1}(\mathbf{k}) \exp (i \mathbf{k} \cdot \boldsymbol{r}), \tag{6a}
$$

$$
\ln g_{1}(\boldsymbol{r})=\sum_{\{\mathbf{k}\}} \hat{G}_{1}(\mathbf{k}) \exp (i \mathbf{k} \cdot \boldsymbol{r}), \tag{6b}
$$

where the elements of $\{\mathbf{k}\}$ are the vectors of the recip- rocal lattice of the assumed space structure, which has lattice sites $\{\mathbf{R}_{L}\}$. Substitution of Eq. (6) into Eq. (5) yields

$$
\hat{G}_{1}(\mathbf{k})=\alpha(k) \hat{g}_{1}(\mathbf{k}), \tag{7a}
$$

$$
\alpha(k)=4 \pi \rho \beta k^{-1} \int_{0}^{\infty} d s s^{2} g_{2}^{\text {fluid }}(s) v^{\prime}(s) j_{1}(k s). \tag{7b}
$$

The iterative scheme we have followed is described below. It is to be remarked that it is applicable to hard spheres as well as continuous interactions.

As input we need the pair potential $v(r)$ and $g_{2}^{\text {fluid }}(r)$ at the appropriate values of $\rho$ and $T$. $\alpha(k)$ is then evaluated using Eq. (7b) for all values of $|\mathbf{k}|$ that may be required. The zeroth-order values of $\hat{g}_{1}(\mathbf{k})$, denoted by $\hat{g}_{1}^{0}(\mathbf{k})$, are obtained by Fourier transforming the function

$$
g_{1}^{0}(\boldsymbol{r})=A \sum_{L} \exp \left[-\omega^{-2}\left(\mathbf{r}-\mathbf{R}_{L}\right)^{2}\right]. \tag{8}
$$

The constant $A$ gives the normalization

$$
\Omega_{0}^{-1} \int d \boldsymbol{r} g_{1}^{0}(\boldsymbol{r})=1, \tag{9}
$$

where the integration is over the unit cell of volume $\Omega_{0}$.

From Eq. (8) we see that $\omega$ determines the initial degree of localization around $\mathbf{R}_{L}$ that we give to the one particle density in space. We shall treat the consequences of this in detail below. Substituting $\hat{g}_{1}^{0}(\mathbf{k})$ into Eq. (7a) one obtains $G_{1}^{1}(\mathbf{k})$. Using these values in Eq. (6b) one finds the first iterate $g_{1}^{1}(\boldsymbol{r})$ to replace $g_{1}^{0}(\boldsymbol{r})$. The process is repeated until a suitable criterion for convergence is met:

$$
g_{1}^{t}(\boldsymbol{r}) \rightarrow \hat{g}_{1}^{t}(\mathbf{k}) \rightarrow \hat{G}_{1}^{t+1}(\mathbf{k}) \rightarrow \ln g_{1}^{t+1}(\boldsymbol{r}) \rightarrow g_{1}^{t+1}(\boldsymbol{r}). \tag{10}
$$

We shall describe the characteristic features of the solutions to Eq. (5) by using $\left\|h_{1}\right\|$, the norm of $h_{1}(\boldsymbol{r})$ $=g_{1}(\boldsymbol{r})-1$,

$$
\left\|h_{1}\right\|^{2}=\Omega_{0}^{-1} \int d \boldsymbol{r} h_{1}^{2}(\boldsymbol{r}). \tag{11}
$$

$h_{1}$ is everywhere zero for a uniform fluid. $\left\|h_{1}\right\|$, the order parameter, is zero for the fluid and a nonzero value measures the degree of nonuniformity in the system.

For the purpose of discussing two special values of the density $\rho^{*}$ and $\rho_{b}$ which arise in these calculations we refer to the behavior of $\left\|h_{1}\right\|$ as a function of $\rho$ for a hard-sphere system; this is shown in Fig. 1.

We see from the figure that for: (1) $\rho<\rho_{b}$ there is a fluid solution. (2) $\rho_{b} \leqslant \rho<\rho^{*}$ there are two nonuniform solutions and a fluid solution. (3) $\rho^{*} \leqslant \rho$ there is a nonuniform solution and a fluid solution.

The role of $\omega$ [Eq. (8)] in the way the iterative scheme proceeds is as follows:

When $\rho<\rho_{b}$, i.e., for low densities, even a highly localized initial guess for $g_{1}^{0}(\boldsymbol{r})$ does not sustain itself as the iteration proceeds: for any $\omega$ one obtains the fluid solution.

When $\rho>\rho^{*}$, i.e., for high densities, even a not so localized $g_{1}^{0}(\boldsymbol{r})$ gathers its wings up as the iteration proceeds: the solution converges to the solid branch unless very large values of $\omega$ are chosen, in which case $g_{1}^{0}(\boldsymbol{r}) \simeq 1$ in the whole cell and the solution falls to the fluid solution.

The interesting region is that between $\rho_{b}$ and $\rho^{*}$. We find that there exists an $\omega_{0}$ such that,

(i) $\omega \ll \omega_{0}$: $g_{1}^{0}$ is quite narrow and in a few iterations one converges, with any prescribed tolerance, on the

nonuniform solution with the high value of $\|h_1\|$ (see Fig. 1).

(ii) $\omega \gg \omega_0$: the uniform solution is obtained without any hesitation during the iterations.

(ii) $\omega \lesssim \omega_0$: $\omega$ slightly less than $\omega_0$, the iterations give persistent functions $g_1^i(\mathbf{r})$ for several cycles around a tolerance $^{11}$ of say $\epsilon=10^{-3}$ before falling rapidly towards the high values of $\|h_1\|$.

(iv) $\omega \gtrsim \omega_0$: $\omega$ slightly larger than $\omega_0$, the same per sistence is found except that the iterations finally fall towards the fluid solution.

The search for $\omega_0$ is quite a simple matter to under take. In Figs. 1 and 3 the low nonzero value of $\|h_1\|$, for $\rho$ between $\rho_b$ and $\rho^*$, is the value at which the deli cately balanced unstable solution persists for several $(\sim 5)$ iterations with $\epsilon<10^{-3}$.

Solutions to Eq. (5) as those in Fig. 1 were obtained by Raveche and Kayser $^{5}$ for a system of hard spheres. They found the higher solid branch by an iterative tech- nique that does not require numerical integration; but they used a parametrization method to handle the lower branch.

### B. Calculation of the bifurcation point

As done by Raveche and Kayser, $^{5}$ Eq. (5) can be linearized for $\rho \to \rho^*$ to get
$$
\nabla_{\mathbf{r}} h_{1}(\mathbf{r})=-\beta \rho \int_{\Omega} d \mathbf{s} h_{1}(\mathbf{r}-\mathbf{s}) g_{2}^{\text {fluid }}(s) v^{\prime}(s)(\mathbf{s} / s), \quad(12)
$$
which in $\mathbf{k}$ space becomes
$$
\hat{g}_{1}(\mathbf{k})=\alpha(k) \hat{g}_{1}(\mathbf{k}). \quad(13)
$$

Hence we look for the value of $\rho^*$ which, for the first reciprocal lattice vector of the assumed structure $\mathbf{k}_{0}$ makes $\alpha[\mathbf{k}_{0}, T, \rho^{*}(T)]=1$.

### C. Equation of state and thermodynamic potentials

Having solved for $g_1(\mathbf{r})$, with $v(r)$ and $g_2^{\text {fluid }}(r)$ as input functions, we get
$$
\begin{aligned}
\frac{p V}{N k_{B} T}= & 1-\frac{\rho}{6 k_{B} T} \frac{1}{\Omega} \\
& \times \int_{\Omega} d \mathbf{r} d \mathbf{s} v^{\prime}(s) g_{2}^{\text {fluid }} g_{1}\left[\frac{\mathbf{r}-\mathbf{s}}{2}\right] g_{1}\left[\frac{\mathbf{r}+\mathbf{s}}{2}\right] \quad(14) \\
= & 1-\frac{2 \pi \rho}{3 k_{B} T} \int_{0}^{\infty} d s s^{3} v^{\prime}(s) g_{2}^{\text {eff }}(s).
\end{aligned}
$$

We observe that
$$
\begin{aligned}
g_{2}^{\mathrm{eff}}(s) & =\frac{1}{4 \pi s^{2}} \frac{1}{\Omega} \int_{\Omega} d \mathbf{r} \int d \hat{\Omega}_{s} g_{2}^{\text {fluid }}(s) g_{1}\left[\frac{\mathbf{r}-\mathbf{s}}{2}\right] g_{1}\left[\frac{\mathbf{r}+\mathbf{s}}{2}\right] \\
& =g_{2}^{\text {fluid }}(s) \sum_{\{\mathbf{k}\}}\left|\hat{g}_{1}(\mathbf{k})\right|^{2} \frac{\sin (k s)}{(k s)}, \quad(15)
\end{aligned}
$$
is an effective radial distribution function. $g_{2}^{\text {eff }}=g_{2}^{\text {fluid }}$ for a fluid, but for the solid $g_{2}^{\text {eff }}$ is an approximation to the angle-averaged pair correlation function $g_{2}^{s}(r)$ given by
$$
g_{2}^{s}(s)=\frac{1}{4 \pi s^{2} \rho} \frac{1}{N} \int_{\Omega} d \mathbf{r} \int d \Omega_{s} \rho_{2}(\mathbf{r}, \mathbf{r}+\mathbf{s}). \quad(16)
$$

This approximation results from assuming
$$
\rho_{2}\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right)=\rho^{2} g_{1}\left(\mathbf{r}_{1}\right) g_{1}\left(\mathbf{r}_{2}\right) g_{2}^{\text {fluid }}\left(r_{12}\right).
$$

Using $p=-(\partial F / \partial v)_{T}$, the Helmholtz free energy per particle $f=F / N$ can be obtained from
$$
f(V)=-\int_{V_{\text {ref }}}^{V} \frac{p V^{\prime}}{N} \frac{d V^{\prime}}{V^{\prime}}, \quad(17)
$$

<table><caption>TABLE I. On the left is shown $\|h_1\|$ as a function of $\rho$ for a hard-sphere system with fcc symmetry; and on the right, the equation of state and chemical potential as a function of $(V/V_0)$ ($V_0=\sigma^3/\sqrt{2}$). Symbols HI and LO denote the nonuniform solution with the high and low value of $\|h_1\|$, respectively (see Fig. 1); symbol FL denotes the fluid solution.</caption>
<thead>
  <tr>
    <th>$\rho$</th>
    <th>$\|h_1\|^{HI}$</th>
    <th>$\|h_1\|^{LO}$</th>
    <th>$\frac{V}{V_0}$</th>
    <th>$\left[\frac{pV_0}{Nk_BT}\right]^{HI}$</th>
    <th>$\left[\frac{pV_0}{k_BT}\right]^{HI}$</th>
    <th>$\left[\frac{pV_0}{Nk_BT}\right]^{FL}$</th>
    <th>$\left[\frac{\mu}{k_BT}\right]^{FL}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>0.809</td>
    <td>6.61</td>
    <td>0.00</td>
    <td>1.748</td>
    <td>3.60</td>
    <td>6.16</td>
    <td>4.55</td>
    <td>7.95</td>
  </tr>
  <tr>
    <td>0.800</td>
    <td>6.28</td>
    <td>0.25</td>
    <td>1.768</td>
    <td>3.51</td>
    <td>6.00</td>
    <td>4.37</td>
    <td>7.65</td>
  </tr>
  <tr>
    <td>0.790</td>
    <td>5.91</td>
    <td>0.38</td>
    <td>1.790</td>
    <td>3.42</td>
    <td>5.84</td>
    <td>4.19</td>
    <td>7.31</td>
  </tr>
  <tr>
    <td>0.780</td>
    <td>5.55</td>
    <td>0.49</td>
    <td>1.813</td>
    <td>3.33</td>
    <td>5.68</td>
    <td>4.00</td>
    <td>6.99</td>
  </tr>
  <tr>
    <td>0.775</td>
    <td>5.37</td>
    <td>0.55</td>
    <td>1.825</td>
    <td>3.28</td>
    <td>5.60</td>
    <td>3.92</td>
    <td>6.83</td>
  </tr>
  <tr>
    <td>0.770</td>
    <td>5.19</td>
    <td>0.60</td>
    <td>1.837</td>
    <td>3.24</td>
    <td>5.52</td>
    <td>3.84</td>
    <td>6.68</td>
  </tr>
  <tr>
    <td>0.760</td>
    <td>4.84</td>
    <td>0.71</td>
    <td>1.861</td>
    <td>3.16</td>
    <td>5.37</td>
    <td>3.67</td>
    <td>6.38</td>
  </tr>
  <tr>
    <td>0.750</td>
    <td>4.47</td>
    <td>0.82</td>
    <td>1.886</td>
    <td>3.08</td>
    <td>5.22</td>
    <td>3.52</td>
    <td>6.08</td>
  </tr>
  <tr>
    <td>0.740</td>
    <td>4.10</td>
    <td>0.95</td>
    <td>1.911</td>
    <td>3.00</td>
    <td>5.08</td>
    <td>3.37</td>
    <td>5.80</td>
  </tr>
  <tr>
    <td>0.730</td>
    <td>3.71</td>
    <td>1.11</td>
    <td>1.937</td>
    <td>2.93</td>
    <td>4.94</td>
    <td>3.22</td>
    <td>5.52</td>
  </tr>
  <tr>
    <td>0.725</td>
    <td>3.50</td>
    <td>1.20</td>
    <td>1.951</td>
    <td>2.90</td>
    <td>4.87</td>
    <td>3.15</td>
    <td>5.39</td>
  </tr>
  <tr>
    <td>0.720</td>
    <td>3.28</td>
    <td>1.31</td>
    <td>1.964</td>
    <td>2.87</td>
    <td>4.81</td>
    <td>3.09</td>
    <td>5.25</td>
  </tr>
  <tr>
    <td>0.710</td>
    <td>2.73</td>
    <td>1.64</td>
    <td>1.992</td>
    <td>2.81</td>
    <td>4.71</td>
    <td>2.95</td>
    <td>4.99</td>
  </tr>
  <tr>
    <td>0.706</td>
    <td>2.35</td>
    <td>1.93</td>
    <td>2.003</td>
    <td>2.81</td>
    <td>4.70</td>
    <td>2.90</td>
    <td>4.89</td>
  </tr>
  <tr>
    <td>0.705</td>
    <td>2.12</td>
    <td>2.12</td>
    <td>2.006</td>
    <td>2.82</td>
    <td>4.73</td>
    <td>2.89</td>
    <td>4.87</td>
  </tr>
  <tr>
    <td>0.704</td>
    <td></td>
    <td></td>
    <td>2.009</td>
    <td></td>
    <td></td>
    <td>2.88</td>
    <td>4.84</td>
  </tr>
  <tr>
    <td>0.703</td>
    <td></td>
    <td></td>
    <td>2.012</td>
    <td></td>
    <td></td>
    <td>2.87</td>
    <td>4.82</td>
  </tr>
  <tr>
    <td>0.700</td>
    <td></td>
    <td>2.020</td>
    <td></td>
    <td></td>
    <td></td>
    <td>2.82</td>
    <td>4.74</td>
  </tr>
</tbody>
</table>
J. Chem. Phys., Vol. 77, No. 11, 1 December 1982

![](./images/812418516907982849_4.jpg)

FIG. 2. Variation of $pV_{0}/Nk_{B}T$ with $V/V_{0}$ for a hard-sphere system with fcc symmetry $(V_{0}=\sigma^{3}/\sqrt{2})$. ---: from the nonuniform solutions; —: from the fluid solution.

where $V_{ref}$ is the volume of a conveniently chosen reference state. Then the chemical potential is given by $\mu=f+(pV)/N$. The pressure at which $\mu^{solid}(p)=\mu^{fluid}(p)$ is the solid-liquid equilibrium pressure. The bifurcation point provides a natural way to choose the reference state to calculate the free energy $^{5}$ since $f^{solid}(\rho^{*})$ $=f^{fluid}(\rho^{*})$.

### III. RESULTS AND DISCUSSION

To calculate $g_{1}(\mathbf{r})$ and the pressure for a system of hard spheres of diameter $\sigma$ we need as input only $g_{2}^{fluid}(\sigma)$ [see Eqs. (7b), (14), and (15)]. From Ree and Hoover$^{12}$ this function, for density $\rho$, is
$$
g_{2}^{\text{fluid}}(\sigma)=\frac{1.0+0.133089\rho+0.076014\rho^{2}}{1.0-1.175988\rho+0.356679\rho^{2}}. \tag{18}
$$

For an fcc structure in space we have calcuated $\|h_{1}\|$ as a function of $\rho$ for the high $(g_{1}^{\text{HI}})$ and the low $(g_{1}^{\text{LO}})$ branches of the periodic solution. Our results are shown in Table I and Fig. 1. We found $\rho_{b}=0.705$ and $\rho^{*}=0.809$. These results agree with those of Raveche and Kayser, shown in Fig. 3 of Ref. 5. Note that they could obtain $g_{1}^{\text{LO}}(\mathbf{r})$ from $\rho^{*}$ to $\rho=0.705$ only while we found this function for densitites as low as $\rho_{b}$, by the procedure discussed in Sec. II.

Figure 2 shows the equation of state fitted to a cubic spline; $V_{0}$ in the figure is the volume per particle at close packing, i. e., $V_{0}/\sigma^{3}=1/\sqrt{2}$.

Our results for the pressure and the chemical potential as a function of volume are shown in Table I for $g_{1}^{\text{HI}}$ and the fluid solution. By inspection of this table we conclude that a first order phase transition occurs at $pV_{0}/Nk_{B}T=2.8$, $V_{solid}=2.006V_{0}$, $V_{fluid}=2.020V_{0}$. Raveche and Kayser$^{5}$ give $pV_{0}/Nk_{B}T=2.808$, $V_{solid}$ $=1.997V_{0}$, $V_{fluid}=2.025V_{0}$. Monte Carlo calculations reported by Wood$^{13}$ yield $pV_{0}/Nk_{B}T=8.0$, $V_{solid}=1.35V_{0}$, $V_{fluid}=1.50V_{0}$. Thus, agreement between the theory and computer simulation is not quantitative. $^{5}$

We have used the methods described above to study the alkali metal rubidium. We chose this system because extensive studies on the nucleation of a solid (into a bcc structure) from a supercooled liquid have been recently done. $^{9}$ The calculations reported here were done at the reduced temperature $T=0.8$ (= 322 K). The required $g_{2}^{fluid}(r)$ was obtained using the hypernetted chain (HNC) approximation. Figure 3 shows $\|h_{1}\|$ vs $\rho$ for both fcc and bcc structures in space. We find $(\rho_{b}=0.568$, $\rho^{*}=0.670)$ for the bcc system, and $(\rho_{b}=0.567$, $\rho^{*}=0.665)$ for the fcc crystal. We remark that bifurcation occurs almost at the same density for both crystals. The values of $\rho_{b}$ are also very close to each other.

The densities at which the double-valued periodic solution exists are very low compared to the density near the melting point, $^{9}\simeq 0.9$. This has an unsatisfactory consequence in that the pressure for the non-

![](./images/812418516907982849_5.jpg)

FIG. 3. Dependence of $\|b_{1}\|$ on $\rho$ for rubidium at $T=0.80$. ---: bcc symmetry; —: fcc symmetry.

![](./images/812418516907982849_6.jpg)

FIG. 4. As in Fig. 2 but for the rubidium system with bcc symmetry.

uniform state has negative values, as shown in Fig. 4. Therefore, it is not possible to perform the "equal area" construction explained in Fig. 12 of Ref. 5, which means that no phase transition can occur. The results in Fig. 4 are for the existance of the bcc phase; similar results were obtained for the fcc structure.

The fact that solid solution are obtained at abnormally low densities in the hard-sphere system as well as in rubidium, implies that the approximation $^{1} g_{2}(r_{1}, r_{2})$ $=g_{2}^{fluid}(r_{12})$ favors the ordered structure even at very low densities, irrespective of the interaction potential.

To gain further insight into the consequences of the above mentioned approximation we inspected the angle-averaged pair distribution function $g_{2}^{s}$ and the pressure of a Lennard-Jones solid with fcc symmetry, at $\rho=0.9$ and $T=0.80$ in reduced units. We recall that studies of crystal nucleation $^{9}$ of this system have shown that it leads to an fcc structure. The values of $\rho$ and $T$ were chosen based on the phase diagram of the (12-6) potential calculated by Hansen and Verlet $^{14}$ using molecular dynamics (MD) simulations.

We used as input the $g_{2}^{fluid}(r)$ obtained from MD and calculated $g_{1}^{HI}, g_{2}^{eff}$ [Eq. (15)], and the corresponding pressure [Eq. (14)]. Using MD calculations on the solid, the angle-averaged pair correlation function $g_{2}^{s}$ was used in Eq. (14) to calculate the pressure. The purpose therefore is to compare $g_{2}^{s}$ and $g_{2}^{eff}$ , and the values of the pressure corresponding to these functions. The functions $g_{2}^{s}$ and $g_{2}^{eff}$ are shown in Fig. 5, together with the input $g_{2}^{fluid}$ . The results for the equation of state are: $p V / N k_{B} T=2.02$ using $g_{2}^{s}$ , and 4.35 using $g_{2}^{eff}$ ; these values are in complete disagreement with each other.

For the hard-sphere system near $\rho=\rho^{*}$ , i.e., $V / V_{0}$ $=1.75$ the values of $p V / N k_{b} T$ for a Monte Carlo simulated solid (see Fig. 9, Ref. 5) is $4.60 V / V_{0}$ , whereas the value calculation from the theory is $3.60 V / V_{0}$ (see Table I), which again shows the inadequate nature of this approach.

Apart from the calculations just mentioned we determined the bifurcation density of the Lennard-Jones system at three different temperatures. We found $(T$ $=0.79, \rho^{*}=0.80),(T=0.84, \rho^{*}=0.85)$ , and $(T=2.20$ , $\rho^{*}=0.90)$ . These points lie to the left of the freezing curve in the phase diagram of Hansen and Verlet $^{14}$ and, consequently, we believe that $\rho^{*}$ cannot be identified with the limit of stability of the disordered phase. $^{5,6}$ This is consistent with the theoretical work of Lovettand Buff. $^{15}$

![](./images/812418516907982849_7.jpg)

FIG. 5. Comparison of theoretical and MD results for a Lennard-Jones crystal at $T=0.80, \rho=0.90$ with fcc symmetry. (i) - is $g_{2}^{eff}$ from Eq. (16). (ii) - - is $g_{2}^{s}$ from MD simulations of the solid. (iii) - - - is $g_{2}^{fluid}$ also from MD.

$^{1}$ J. G. Kirkwood and E. Monroe, J. Chem. Phys. 9, 514 (1941).
$^{2}$ J. G. Kirkwood and E. M. Boggs, J. Chem. Phys. 10, 307(1942).
$^{3}$ R. Brout, Physica 29, 1041 (1963); 30, 459 (1964); see also R. Brout, Phase Transitions (Benjamin, New York, 1965).

⁴J. D. Weeks, S. A. Rice, and J. J. Kozak, J. Chem. Phys. 52, 2416 (1970).

⁵H. J. Raveche and R. F. Kayser, Jr., J. Chem. Phys. 68, 3632 (1978).

⁶H. J. Raveche and C. A. Stuart, J. Chem. Phys. 63, 1099 (1975).

⁷D. N. Lowy and C.-W. Woo, Phys. Rev. B 13, 3790 (1976); Phys. Lett. A 56, 402 (1976); Phys. Rev. D 13, 3201 (1976); M. A. Lee, D. N. Lowy, and C.-W. Woo, Phys. Rev. B 14, 4874 (1976).

⁸M. D. Miller, W. J. Mullin, and R. A. Guyer, Phys. Rev. B 18, 3189 (1978).

⁹C.-S. Hsu and A. Rahman, J. Chem. Phys. 71, 4974 (1974).

¹⁰T. L. Hill, *Statistical Mechanics* (McGraw-Hill, New York, 1956).

¹¹$\epsilon = \max_{\mathbf{r}} |g_{1}^{m+1}(\mathbf{r}) - g_{1}^{m}(\mathbf{r})|$.

¹²F. H. Ree and W. G. Hoover, J. Chem. Phys. 40, 939 (1964).

¹³W. W. Wood, *Fundamental Problems in Statistical Mechanics III*, edited by E. G. D. Cohen (North-Holland, Amsterdam, 1975).

¹⁴J.-P. Hansen and L. Verlet, Phys. Rev. 184, 151 (1969).

¹⁵R. Lovett and F. P. Buff, J. Chem. Phys. 72, 2425 (1980).