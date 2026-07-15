International Journal of Modern Physics B, Vol. 14, No. 5 (2000) 457-473
© World Scientific Publishing Company

# σ-MODEL ANALYSIS OF QUANTUM SPIN LADDERS

OLAV F. SYLJUÅSEN*

Department of Physics, Massachusetts Institute of Technology,
77 Massachusetts Avenue Cambridge, MA 02139, USA

Received 27 December 1999

The $\sigma$-model approach to quantum spin ladders, described here, allows one to analytically calculate correlation lengths and gaps for both even- and odd-legged ladders, at any temperature. Comparison with high precision quantum Monte Carlo simulations show that these analytic results are surprisingly accurate. A self-contained account of these analytic methods is presented.

## 1. Introduction

The undoped phase of the high temperature superconductors is a two-dimensional spin-1/2 antiferromagnetic insulator. This has led to renewed interest in quantum antiferromagnets in two dimensions. Because the spin and the spatial dimension is low, quantum fluctuations are important. The path-integral method offers many advantages for dealing with these. In the path-integral method, an extra imaginary-time dimension whose extent is the inverse temperature is introduced. The extent of the imaginary time dimension will strongly affect the quantum fluctuations of the spins. When the extent of this dimension is large, the variations of the spin configurations in the imaginary time direction can be allowed without a large cost in the action; the multiplicity of such configurations then overwhelms whatever cost in the action that such variations entail. In contrast, when this extent becomes smaller, such variations will be prohibitively costly, and only the spatial fluctuations of the spin will be allowed. Of course, the number of spatial dimensions will also dictate the fluctuations of the spin. Thus, we can expect a strong dependence on the size and the inverse temperature of the system. We will show how this dependence can be found analytically for a finite-sized system, the quantum spin ladder, as both its size and temperature are varied.

The quantum spin ladders are systems in which chains of interacting spins (legs) are coupled by interactions along the rungs of the ladders. They are intrinsically interesting systems from the perspective of fluctuations in low-dimensional quantum systems. In addition, it has been hypothesized that they may shed light on

*Present address: NORDITA, Blegdamsvej 17, DK-2100 Copenhagen, Denmark.

the mechanism of superconductivity in the cuprate superconductors. A number of experimental realizations are known,¹ and, indeed, superconductivity has been observed when these spin ladders were doped and subjected to high pressures.² Moreover, their normal state transport properties bear intriguing resemblance to the cuprate superconductors.³

In the present paper, we limit ourselves to the undoped systems represented by the antiferromagnetic spin-$S$ Heisenberg model, the lattice being infinite in the $x$-direction, but finite in the $y$-direction. The Hamiltonian of the $n$-legged spin ladder, with the coupling $J$ along the chains and the coupling $J_\perp$ across the chains, is

$$
H = \sum_{x=-\infty}^{\infty} \sum_{y=1}^{n} (J\mathbf{S}_{x,y} \cdot \mathbf{S}_{x+1,y} + J_\perp \mathbf{S}_{x,y} \cdot \mathbf{S}_{x,y+1}). \tag{1}
$$

Instead of the strong or the weak coupling limit of the ratio $J/J_\perp$,⁴ we first consider the limit $J/J_\perp = 1$ and study the behavior as a function of the width of the ladder.⁵,⁶ In fact, we begin with the infinite two-dimensional system and ask how its properties are changed as the width is made finite. We shall see that the results are remarkably accurate and can be controlled even for ladders of just a few legs. The efficacy of approaching finite width ladders from the infinite two-dimensional system is that many of the results can be obtained from the proverbial back-of-the-envelope calculations, requiring no extensive numerical computations. In addition, in this approach, we are able to elucidate the subtle nature of the crossover between the one (the single chain limit) and the two-dimensional systems. Because of the simplicity of our approach, it is not unreasonable to hope that this method will also find applications to the more complex doped systems. We then extend our analysis to anisotropic ladders.

## 2. The Nonlinear $\sigma$-Model

The simplest continuum model that describes correctly the long wavelength low energy properties of the two-dimensional spin-$S$ Heisenberg model is the nonlinear $\sigma$-model. The generalization of this model to ladders is simple; all we need to do is to make the width of the system finite. The quantum mechanical action is

$$
\frac{S}{\hbar} = \frac{\rho_{\mathrm{s}}^{0}}{2\hbar} \int_{0}^{\beta\hbar} d\tau \int_{-\infty}^{\infty} dx \int_{0}^{L_{y}} dy \left\{ \frac{1}{c_{0}^{2}} \left( \frac{\partial\hat{\Omega}}{\partial\tau} \right)^{2} + \left( \frac{\partial\hat{\Omega}}{\partial x} \right)^{2} + \left( \frac{\partial\hat{\Omega}}{\partial y} \right)^{2} \right\}, \tag{2}
$$

where $\hat{\Omega}$ is a unit vector, $\beta$ is the inverse temperature, and $L_y$ is the width of the ladder, which is equal to the number of chains times the lattice spacing. We have restricted ourselves to the case $J = J_\perp$; spatial anisotropy will be discussed in Sec. 6. Implicit in the definition of the action is also a short distance cutoff necessary to define the model.

The quantities $c_0$ and $\rho_{\mathrm{s}}^{0}$ are the microscopic spin-wave velocity and the spin-stiffness constant respectively. These are the input parameters of the model and

can be found in two possible ways. The $\sigma$-model can be derived from the microscopic Heisenberg model and the input parameters can be obtained in a large-$S$ expansion. $^{7}$ Unfortunately, such a method has not been pursued to the extent that is necessary. Here, we shall take a different route. $^{8}$ We shall express the macroscopic physical quantities in terms of the input parameters of the $\sigma$-model. These macroscopic quantities can then be obtained in other ways from the microscopic Heisenberg model by suitable methods, such as the spin-wave expansion or quantum Monte Carlo simulations. One can then work back to find the input parameters. Of course, this last step is not necessary if the final calculated quantities are entirely functions of the macroscopic physical quantities, which is the case in this paper.

### 3. One-Loop Reduction of the Effective Action
The $\sigma$-model can be simplified in the following regimes: a) $\beta\hbar c/L_y \gg 1$, b) $\beta\hbar c/L_y \approx 1$, and c) $\beta\hbar c/L_y \ll 1$. The boxes in Fig. 1 illustrate the three regimes. The system is visualized as a three-dimensional box. One of the dimensions of the box, corresponding to the length of the ladder, is infinite in extent; the remaining two have extents $\beta\hbar c$ and $L_y$ respectively. The finiteness of these dimensions restrict the longest allowed wavelength of the variation of $\hat{\Omega}$. We now derive an effective $\sigma$-model by integrating out the "fast" components (in either spatial or in temporal sense) of the field $\hat{\Omega}$. The slow components are chosen such that they are constant along the shortest direction(s), which is of course an assumption that must be checked at the end. For example, for the low-temperature regime (a), this means that the correlation length should be bigger than $L_y$.

![](./images/814585980399910913_1.jpg)

Fig. 1. The size of the quantum system visualized in the three regimes.

Integrating out the fast components to one-loop order we find the following effective $\sigma$-models in the three distinct regimes listed above:

$$
S_{a}=\frac{1}{2 t_{a}} \int_{0}^{\beta \hbar c} d \tau \int d x\left\{\left(\partial_{\tau} \hat{\Omega}\right)^{2}+\left(\partial_{x} \hat{\Omega}\right)^{2}\right\}, \tag{3}
$$

$$
S_{b}=\frac{1}{2 t_{b}} \int d x\left(\partial_{x} \hat{\Omega}\right)^{2},
\tag{4}
$$

$$
S_{c}=\frac{1}{2 t_{c}} \int d x \int_{0}^{L_{y}} d y\left\{\left(\partial_{x} \hat{\Omega}\right)^{2}+\left(\partial_{y} \hat{\Omega}\right)^{2}\right\},
\tag{5}
$$

where

$$
\frac{1}{t_{a}}=\frac{L_{y}}{g_{0}}\left(1-\frac{g_{0}}{L_{y} \beta \hbar c} \sum_{p \neq 0, \omega} \int \frac{d k}{2 \pi} \frac{1}{\omega^{2}+p^{2}+k^{2}}\right),
\tag{6}
$$

$$
\frac{1}{t_{b}}=\frac{L_{y} \beta \hbar c}{g_{0}}\left(1-\frac{g_{0}}{L_{y} \beta \hbar c} \sum_{p \neq 0, \omega \neq 0} \int \frac{d k}{2 \pi} \frac{1}{\omega^{2}+p^{2}+k^{2}}\right),
\tag{7}
$$

$$
\frac{1}{t_{c}}=\frac{\beta \hbar c}{g_{0}}\left(1-\frac{g_{0}}{L_{y} \beta \hbar c} \sum_{p, \omega \neq 0} \int \frac{d k}{2 \pi} \frac{1}{\omega^{2}+p^{2}+k^{2}}\right),
\tag{8}
$$

and $g_{0}=\hbar c / \rho_{\mathrm{s}}^{0}$. Here $\omega=2 \pi n / \beta \hbar c$ and $p=2 \pi m / L_{y}$.

For mathematical convenience, we have assumed periodic boundary conditions along the width of the ladder. This is not the most realistic choice as the experimental systems are better desribed by open boundary conditions along the width. However, it has been demonstrated from extensive Monte Carlo calculations⁹ that the difference between the two boundary conditions is small and is of significance only at low temperatures for narrow ladders.

### 4. When are Topological Terms Important?

In viewing the 2D Heisenberg antiferromagnet as pieced together by spin chains Haldane has argued¹⁰ that an extra topological term for each chain $j$

$$
2 \pi i S \sum_{j=1}^{n} Q_{j},
\tag{9}
$$

where

$$
Q_{j}=\frac{1}{4 \pi} \int d x \int d \tau \hat{\Omega}_{j} \cdot\left(\partial_{x} \hat{\Omega}_{j} \times \partial_{\tau} \hat{\Omega}_{j}\right),
\tag{10}
$$

which is an integer, should be added to the nonlinear $\sigma$-model. We must find out what this implies for the reduced effective actions obtained in the previous section. It is clear that the topological term can only be present in the low-temperature regime a) as $\hat{\Omega}$ is constant in $\tau$ in the other regimes, something which makes $Q_{j}$ identically zero. Requiring a smooth configuration Haldane argued that $Q_{j}=-Q_{j+1}$ which makes the topological term vanish when the number of chains is even. For the odd-legged ladders the topological term remains,¹¹ thus the topological term is only present in the low-temperature regime for odd-legged ladders.

The 2D antiferromagnet is very well described by a $\sigma$-model *without* the topological term.⁸ This might sound strange as there is no reason that a 2D antiferromagnet cannot have a huge *odd* number of chains, which would imply the presence of a topological term. The answer is that in the 2D limit the topological term only influences the physics at unobservably low temperatures. This can be seen by noticing that the action cost in the low-temperature regime increases with $|Q|$ and is proportional to the stiffness. Therefore, when the stiffness is huge, as it is for many chains (it is proportional to $L_y$), only the $Q=0$ sector will have significant weight in the action. This is just as if the topological term was absent. Renormalizing to lower energies, it is well known that the stiffness decreases, and eventually at low enough energies other topological sectors will become important. But if the initial spin stiffness is huge this crossover will occur at an unobservably low temperature. This is what happens in the 2D limit.

To make a crude estimate for when the topological term becomes important one can use the following arguments. Coming from the high temperature side the fields are roughly constant on a scale of order $\xi$, the correlation length, which can be estimated using the result for the correlation length obtained *without* the topological term $\xi_0$, Eq. (17). For temperatures such that $\beta\hbar c \sim \xi_0$ the fields will effectively be constant in the temperature-direction and the topological term is identically zero. So only for temperatures such that $\beta\hbar c \gg \xi_0$ will the topological term be important. For 3-, 5- and 7-legged ladders these arguments give the following estimates for when the topological term is important

$$
T/J <
\begin{cases}
0.58 & n=3, \\
0.13 & n=5, \\
0.03 & n=7.
\end{cases} \tag{11}
$$

## 5. Zero Temperature

In this and the remaining sections we will discuss the reduced effective actions quantitatively to obtain results for spin gaps and correlation lengths. In the $T=0$ limit the reduced action Eq. (3) is the two-dimensional $\sigma$-model for which the correlation length is known in the weak coupling limit. So all we need to do is calculate the coupling $t_{a0}$ which translates into calculating the integral

$$
I_a^0 = \frac{1}{L_y} \sum_{p\neq 0} \int \frac{dk}{2\pi} \int \frac{d\omega}{2\pi} \frac{1}{\omega^2 + k^2 + p^2}, \tag{12}
$$

where $p=2\pi m/L_y$. Performing the summation over $m$, changing to polar coordinates and doing the angular integration first we get

$$
I_a^0 = \frac{\Lambda}{4\pi} - \frac{1}{2\pi L_y} \ln\left( \frac{L_y \Lambda}{1 - e^{-L_y \Lambda}} \right). \tag{13}
$$

where we have introduced an ultra-violet cutoff $\Lambda$. We will drop the denominator in the logarithm as it is exponentially small. However we should note that for small

$L_y\Lambda$ the denominator becomes important and tends to cancel the logarithm and
the constant term. This indicates the crossover to a purely one-dimensional regime.

With the above expression for the integral the inverse coupling constant takes
the form

$$
\frac{1}{t_{a 0}}=\frac{L_{y} \rho_{\mathrm{s}}}{\hbar c}+\frac{1}{2 \pi} \ln \left(L_{y} \Lambda\right),\qquad(14)
$$

where we have identified the $T=0$ macroscopic spin stiffness constant for the
two-dimensional antiferromagnet, $\rho_{\mathrm{s}}$, as

$$
\rho_{\mathrm{s}}=\rho_{\mathrm{s}}^{0}\left(1-\frac{g_{0} \Lambda}{4 \pi}\right).\qquad(15)
$$

This follows from considering Eq. (13) in the two-dimensional limit $(L_{y} \to \infty)$.
From Monte Carlo studies done by Beard et al. $^{12}$ on the Heisenberg model the
macroscopic spin-stiffness constant and spin-wave velocity is measured to be

$$
\rho_{\mathrm{s}}=0.1800 J,
$$

$$
\hbar c=1.657 J a.\qquad(16)
$$

Using the known expression for the correlation length of the 2D $\sigma$-model, $^{13}$ we
find

$$
\xi=\frac{e}{8}\left(\frac{\xi_{J}}{2 \pi}\right) e^{2 \pi L_{y} / \xi_{J}}\left[1-\frac{\xi_{J}}{4 \pi L_{y}}\right],\qquad(17)
$$

where we have introduced the Josephson length $\xi_{J}=\hbar c / \rho_{\mathrm{s}}$. We have ignored higher
order logarithms as they have been shown to vanish. $^{14}$ This is the expression first
obtained in Ref. 5.

Because of the "Lorentz" invariance of the original action the gap $\Delta$ is simply
related to the correlation length by

$$
\Delta \xi=\hbar c,\qquad(18)
$$

which immediately gives us the gap values. Table 1 shows correlation lengths and
energy gaps for four- and six-legged ladders obtained from Eqs. (17) and (18) com-
pared with results obtained in Monte Carlo simulations.

Let us make some remarks regarding the range of applicability of Eq. (17). As
the form of Eq. (17) is partially dictated by the weak coupling expression for the
correlation length for the classical $\sigma$-model it is clear that the effective coupling
must be smaller than unity. For big $L_{y}$ this translates into $\xi_{J} / 2 \pi L_{y}<1$. In fact
Eq. (17) is asymptotically exact for $L_{y} \to \infty$. For spin ladders with higher spin $S$ we
should note that $\xi_{J} \sim 1 / S$, thus for fixed $L_{y}$, Eq. (17) gets more and more accurate
as $S$ increases. However, if we compare Eq. (17) at fixed values of $\xi_{J} / L_{y}$ to the
correlation lengths for different values of $S$ we expect the opposite; the agreement
should grow worse as $S$ increases. This is because in the dimensional reduction
process we assumed $L_{y} \Lambda \gg 1$, see the discussion following Eq. (13). For fixed
$\xi_{J} / L_{y}$, $L_{y}$ will effectively get smaller as $S$ increases and increasingly violating this

Table 1. Comparison between analytic results and Monte Carlo simulations for the gaps and correlation lengths at zero temperature for spin-1/2 4- and 6-legged ladders. As the analytic results depends on the input parameters $\rho_{\mathrm{s}}$ and $c$ we give the results both for the parameters calculated by Beard et al. $^{12}$ and from the $1 / S$ spin-wave calculation to order $1 / S$ ($\rho_{\mathrm{s}}=0.191 J, \hbar c=1.638 J a$). The Monte Carlo results which are done for both periodic and open boundary conditions are from Greven et al. $^{6,9}$

<table>
  <thead>
    <tr>
      <th colspan="2">$T=0$</th>
      <th colspan="2">$\xi[a]$</th>
      <th colspan="2">$\Delta[J]$</th>
    </tr>
    <tr>
      <th>Method</th>
      <th></th>
      <th>4 legs</th>
      <th>6 legs</th>
      <th>4 legs</th>
      <th>6 legs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Analytic</td>
      <td>Beard et al.</td>
      <td>6.2</td>
      <td>26.2</td>
      <td>0.266</td>
      <td>0.063</td>
    </tr>
    <tr>
      <td></td>
      <td>Spin waves ($1/S$)</td>
      <td>7.2</td>
      <td>33.5</td>
      <td>0.227</td>
      <td>0.049</td>
    </tr>
    <tr>
      <td>Monte Carlo</td>
      <td>p.b.c.$^{6}$</td>
      <td>7.1</td>
      <td>30.5</td>
      <td>0.234</td>
      <td>0.055</td>
    </tr>
    <tr>
      <td></td>
      <td>o.b.c.$^{9}$</td>
      <td>10.3</td>
      <td>32.0</td>
      <td>0.160</td>
      <td>0.053</td>
    </tr>
  </tbody>
</table>

condition. This is entirely analogous to what has been pointed out in the context of the finite temperature 2D antiferromagnet. $^{15}$

## 6. Anisotropy

Spatially anisotropic couplings can easily be implemented in the $\sigma$-model approach. The natural starting point is to include a coupling constant $1/\lambda^{2}$ in front of the $(\partial_{y}\hat{\Omega})^{2}$ term. $\lambda$ plays the role of an anisotropy parameter and is of the order $\sqrt{J/J_{\perp}}$. By rescaling $y$ and $\tau$ the anisotropic action can be brought into the isotropic form with the replacements $\rho_{\mathrm{s}} \to \rho_{\mathrm{s}}/\lambda$ and $L_{y} \to L_{y}\lambda$. This rescaling of the $y$-direction is not totally innocuous as it also changes the microscopic cutoff from $\Lambda$ to $\Lambda/\lambda$. However, this cutoff only plays a role as the upper cutoff in the sum over wavenumbers $p=2\pi m/L_{y}\lambda$ in Eq. (12). This summation was carried out by extending the sum to infinity which can be justified for large enough $\Lambda$, and so as long as $\lambda$ is not to big a rescaling of the cutoff is unimportant. So, provided $\lambda$ is not to big, we only need to replace $\rho_{\mathrm{s}} \to \rho_{\mathrm{s}}/\lambda$ and $L_{y} \to L_{y}\lambda$ in the expression for the correlation length Eq. (17). This gives

$$
\xi=\frac{e}{8}\left(\frac{\xi_{J}\lambda}{2\pi}\right) e^{2\pi L_{y}/\xi_{J}}\left[1-\frac{\xi_{J}}{4\pi L_{y}}\right], \tag{19}
$$

where $\xi_{J}=\hbar c/\rho_{\mathrm{s}}$ is now a function of $J_{\perp}/J$. An estimate for this dependence can be found by calculating $\rho_{\mathrm{s}}$, $c$ and $\lambda$ to first order in the spin-wave expansion (Holstein–Primakoff) for the 2D system at $T=0$. To first order in the $1/S$-expansion we get

$$
\hbar c=2SJa\sqrt{1+\frac{J_{\perp}}{J}}\left(1+\frac{A(J_{\perp}/J)}{2S}+\frac{(J_{\perp}/J)}{2(1+J_{\perp}/J)}\frac{B(J_{\perp}/J)}{2S}\right), \tag{20}
$$

and

$$
\lambda=\sqrt{\frac{J}{J_{\perp}}}\left(1+\frac{1}{2} \frac{B\left(J_{\perp} / J\right)}{2 S}\right),\tag{21}
$$

where

$$
A\left(\frac{J_{\perp}}{J}\right)=\frac{2}{N} \sum_{k}\left[1-\sqrt{1-\left(\frac{\cos k_{x} a+J_{\perp} / J\right) \cos k_{y} a}{1+\left(J_{\perp} / J\right)}}\right]^{2},\tag{22}
$$

$$
\begin{aligned}
B\left(\frac{J_{\perp}}{J}\right)= & \frac{2}{N} \sum_{k}\left(\cos k_{x} a-\cos k_{y} a\right) \frac{\cos k_{x} a+\left(J_{\perp} / J\right) \cos k_{y} a}{1+\left(J_{\perp} / J\right)} / \\
& \times\left(1-\left(\frac{\cos k_{x} a+\left(J_{\perp} / J\right) \cos k_{y} a}{1+\left(J_{\perp} / J\right)}\right)^{2}\right]^{-1 / 2}.\tag{23}
\end{aligned}
$$

To find the spin stiffness constant $\rho_{\mathrm{s}}$ we will use the hydrodynamic relation

$$
c=\left(\frac{\rho_{\mathrm{s}}}{\chi_{\perp}}\right)^{1 / 2}\tag{24}
$$

which is also true in the anisotropic case. This can be seen by extending the treatment in Ref. 16 to anisotropic couplings. The uniform perpendicular susceptibility $\chi_{\perp}$ is to order $1 / S$

$$
\chi_{\perp}=\frac{1}{4 J\left(1+J_{\perp} / J\right)}\left[1-\frac{A\left(J_{\perp} / J\right)}{2 S}-\frac{2 \Delta S\left(J_{\perp} / J\right)}{2 S}\right],\tag{25}
$$

where

$$
\Delta S\left(J_{\perp} / J\right)=\frac{1}{N} \sum_{k}\left\{1 /\left[1-\left(\frac{\cos k_{x} a+\left(J_{\perp} / J\right) \cos k_{y} a}{1+\left(J_{\perp} / J\right)}\right)^{2}\right]^{-1 / 2}-1\right\}.\tag{26}
$$

To order $1 / S$ we find

$$
\rho_{\mathrm{s}}=J S^{2}\left[1+\frac{A\left(J_{\perp} / J\right)}{2 S}-\frac{2 \Delta S\left(J_{\perp} / J\right)}{2 S}+\frac{J_{\perp} / J}{1+J_{\perp} / J} \frac{B\left(J_{\perp} / J\right)}{2 S}\right].\tag{27}
$$

Of course, the $1/S$-expansion cannot be very accurate for $S=1/2$, especially not when the anisotropy is significant, and so it would be desirable to have some better estimates from other methods. Nevertheless, the spin-wave expansion should at least give qualitative correct results in the vicinity of $J_{\perp}/J=1$. The $T=0$ gap as a function of anisotropy is shown in Fig. 2 for 4- and 6-legged ladders.

![](./images/814585980399910913_2.jpg)

Fig. 2. $T=0$ Gap as a function of anisotropy.

## 7. Even-Legged Ladders at Low Temperatures

For low, but nonzero temperatures the reduced action Eq. (3) is no longer the action for the classical two-dimensional $\sigma$-model, but that of a quantum spin-chain. The correlation length for this is not known to the same degree of accuracy as for the classical model. One can however obtain an estimate of the gap for this model using a self-consistent spin-wave approach. Relaxing the constraint on the magnitude of $\boldsymbol{\Omega}$ and inserting a mass term $(\Delta/\hbar c)^2\boldsymbol{\Omega}^2$ one has the action for $N=3$ free massive bosons. Then one can account for the constraint in an average way by requiring $\langle\boldsymbol{\Omega}^2\rangle=1$. Writing out this self-consistency equation we get in the isotropic limit $\lambda=1$,

$$
Nt_{a}\int\frac{dk}{2\pi}\frac{\coth\left(\sqrt{k^{2}+(\Delta/\hbar c)^{2}}\beta\hbar c/2\right)}{2\sqrt{k^{2}+(\Delta/\hbar c)^{2}}}=1.\tag{28}
$$

This gap equation gives us the temperature dependence of the gap. Solving this equation at $T=0$ and using the relation between the gap and the correlation length Eq. (18) we get

$$
\xi=\frac{1}{2\Lambda}e^{2\pi/Nt_{a0}}(1-e^{-4\pi/Nt_{a0}}),\tag{29}
$$

where $\Lambda$ is a momentum cutoff. Comparing this with the above expression for the $T=0$ correlation length we see that this expression has the correct leading order dependence on $t_{a0}$ for $t_{a0}$ small, except that $N$ should be replaced by $N-2$. Thus this gap equation is to crude to quantitatively give the $T=0$ correlation length.

However, we already know the $T=0$ correlation length from Eq. (17), and we wish only to get the correct temperature dependence. Therefore we split the coupling in Eq. (6) into a $T=0$ and a finite-$T$ contribution

$$
\frac{1}{t_{a}}=\frac{1}{t_{a 0}}-\sum_{p \neq 0} \int \frac{d k}{2 \pi} \frac{\left(k^{2}+p^{2}\right)^{-1 / 2}}{\exp \left(\beta \hbar c \sqrt{k^{2}+p^{2}}\right)-1}.\qquad(30)
$$

Instead of using the deduced expression for $t_{a 0}$ from Eq. (14) we regard it as a parameter and adjust it such that the gap equation gives the correct $T=0$ correlation length. To get the temperature dependence of the gap we solve the gap equation numerically. The gap equation depends on the cutoff $\Lambda$, but this dependence is very weak. We used $\Lambda a=\sqrt{2} \pi$ in our calculations, but $\Lambda a=[0.5 \pi-8 \pi]$ gives no visual changes in our curves.

The gap equation can also be solved analytically for very small $T$ and gives

$$
\Delta(T)=\Delta(0)+2 \pi \sqrt{\Delta(0) T} e^{-\Delta(0) / T}+\cdots.\qquad(31)
$$

However, when $T$ becomes of the order $\Delta$ this expansion breaks down and is of limited usefulness here.

At finite temperatures the relation Eq. (18) between the gap and the correlation length is not on as solid footing as at $T=0$, as it requires $c$ to be unrenormalized. However, $c$ is not renormalized within the one-loop approximation at finite temperatures, and so this relation can still be used consistently within our one-loop approximation.

### 8. Odd-Legged Ladders at Low Temperatures
The nonlinear $\sigma$-model with the topological term Eq. (9) is very difficult to treat directly when the coupling becomes big. However, Affleck and Haldane $^{17}$ have argued that the stable infrared fixed point $(T=0)$ of this theory is the $k=1$ Wess-Zumino-Witten (WZW) model. Therefore the low-temperature properties of the odd-legged ladders can presumably be analyzed by studying the $k=1$ WZW model. The WZW model has a chiral SU(2)×SU(2) symmetry and not just the single O(3)≃SU(2) symmetry of the nonlinear $\sigma$-model. It is therefore clear that in order to explain the behavior of the nonlinear $\sigma$-model with a topological term close to the infrared fixed point one must perturb the WZW model with terms that break the chiral invariance down to a single SU(2) symmetry. There are many such terms, but the ones most important near the fixed point are terms marginal with respect to the WZW-action. There is only one marginal term $^{17}$

$$
S_{\text {pert. }}=\frac{\gamma_{n}\left(T_{0}\right)}{2} \int d z d \bar{z} J^{a}(z) \cdot \bar{J}^{a}(\bar{z})\qquad(32)
$$

where $J^{a}$ and $\bar{J}^{a}$ are the currents in the WZW model, and $\gamma_{n}$ is a coupling constant. We have indicated with the subscript $n$ that $\gamma_{n}$ depends on the number of legs. It also depend on the scale of definition $T_{0}$. As we move away to higher temperatures

other perturbation terms than the one shown becomes important. One could hope that adjusting the coupling constants for these terms one would achieve a smooth crossover to the behavior of the nonlinear $\sigma$-model without a topological term. This is clearly complicated, but there exists promising results which can make this possible. $^{18}$ Here we will just consider the behavior close to $T=0$ where it is justified to only keep the above perturbation term.

As shown in Ref. 19 the correlation length for the WZW model with the perturbation (32) is

$$
\xi / a=\frac{J}{2 T}\left\{1-\frac{\pi \gamma_{n}\left(T_{0}\right)}{2\left[1+\pi \gamma_{n}\left(T_{0}\right) \ln T_{0} / T\right]}\right\}^{-1}.\qquad(33)
$$

Close to $T=0, \gamma_{n}$ drops out. Thus near $T=0$ the behavior should be the same for all odd-legged ladders and is

$$
\frac{\xi}{a}=\frac{J}{2 T}\left(1+\frac{1}{2 \ln \left(T / T_{0}\right)}\right)^{-1}.\qquad(34)
$$

### 9. Intermediate Temperatures

In the intermediate temperature regime we need to calculate the integral

$$
I_{b}=\frac{1}{\beta \hbar c L_{y}} \sum_{\omega, p}^{\prime} \int \frac{d k}{2 \pi} \frac{1}{\omega^{2}+k^{2}+p^{2}}\qquad(35)
$$

to find the effective coupling constant $t_{b}$. The prime on the sum means that the term $\omega=p=0$ is excluded. By using a combination of Euler and Poisson summation formulas $^{20}$ the integral can be split into

$$
\begin{aligned}
I_{b}= & \int \frac{d \omega}{2 \pi} \frac{d k}{2 \pi} \frac{d p}{2 \pi} \frac{1}{\omega^{2}+k^{2}+p^{2}} \\
& +\frac{1}{2 \pi \sqrt{\beta \hbar c L_{y}}}\left\{\int_{1}^{\infty} \frac{d y}{\sqrt{y}}\left[X\left(\frac{L_{y}}{\beta \hbar c} \pi y\right) X\left(\frac{\beta \hbar c}{L_{y}} \pi y\right)-1\right]-2\right\},
\end{aligned}\qquad(36)
$$

where

$$
X(y)=\sum_{n=-\infty}^{\infty} e^{-y n^{2}}.\qquad(37)
$$

The explicit calculation is shown in Appendix. The first term in the above is just the term expected in the 2D $T=0$ case. It will therefore contribute to the renormalization of $\rho_{\mathrm{s}}^{0}$ and we get

$$
t_{b}^{-1}=\frac{L_{y} \beta \hbar c}{\xi_{J}}+L_{y} A\left(\frac{\beta \hbar c}{L_{y}}\right),\qquad(38)
$$

where

$$
A(x)=\frac{\sqrt{x}}{2 \pi}\left\{\int_{1}^{\infty} \frac{d y}{\sqrt{y}}\left[X\left(\frac{\pi y}{x}\right) X(\pi y x)-1\right]-2\right\},\qquad(39)
$$

and $\xi_J = \hbar c/\rho_{\rm s}$. The reduced action (4) describes the continuum limit of the classical Heisenberg spin chain. As the low temperature effective action is that of a quantum spin chain this result is just as expected.

To obtain the correlation length we consider the reduced action (4) as the limit of the lattice action

$$
\frac{S}{\hbar}=-K \sum_{i} \hat{\Omega}_{i} \cdot \hat{\Omega}_{i+1}
\tag{40}
$$

when the lattice spacing $a$ goes to zero. The naive continuum limit of this lattice action is

$$
\frac{S}{\hbar}=\frac{K a}{2} \int d x\left(\partial_{x} \hat{\Omega}\right)^{2}+\text { const }.
\tag{41}
$$

where $K a$ is kept fixed as $a \rightarrow 0$. By identifying

$$
t_{b}^{-1}=K a,
\tag{42}
$$

we obtain the desired correspondence. The correlation length for the lattice model was calculated long ago by Fisher$^{21}$ and is

$$
\frac{\xi}{a}=-\frac{1}{\ln (\operatorname{coth} K-1 / K)}.
\tag{43}
$$

To keep $K a$ fixed when taking $a \rightarrow 0$ we need to take $K \rightarrow \infty$. Doing so for the correlation length we find

$$
\xi=K a,
\tag{44}
$$

and so the correlation length in the intermediate temperature regime is simply given by

$$
\xi=t_{b}^{-1},
\tag{45}
$$

where $t_{b}^{-1}$ is as in Eq. (38). This result contains no adjustable parameters.

## 10. High Temperatures

For high temperatures $\beta \hbar c \ll L_{y}$ the reduced action is equivalent to the reduced action in the low temperature regime except that $\beta \hbar c$ is interchanged by $L_{y}$. To get the temperature dependence of the gap in the high temperature limit we proceed as in the low temperature limit by solving the self-consistent gap equation

$$
N t_{c} \int \frac{d k}{2 \pi} \frac{\operatorname{coth}\left(\sqrt{k^{2}+(\Delta / \hbar c)^{2}} L_{y} / 2\right)}{\sqrt{k^{2}+(\Delta / \hbar c)^{2}}}=1,
\tag{46}
$$

where $\beta \hbar c$ has been interchanged with $L_{y}$. For $L_{y} \rightarrow \infty$ the gap is known as it is the gap for the 2D antiferromagnet which was found in Ref. 8.

$$
\Delta=\frac{\hbar c}{a}\left[\frac{e}{8}\left(\frac{\xi_{J}}{2 \pi}\right) e^{2 \pi \rho_{\mathrm{s}} / T}\left(1-\frac{T}{4 \pi \rho_{\mathrm{s}}}\right)\right]^{-1}.
\tag{47}
$$

As in the low temperature regime the above gap equation is to crude to give the $L_y \to \infty$ gap to this accuracy. So we proceed in analogy with what we did in the low temperature regime. We separate out the $L_y \to \infty$ term $t_{c\infty}$ in the expression for the coupling constant

$$
\frac{1}{t_{c}}=\frac{1}{t_{c \infty}}-\sum_{\omega \neq 0} \int \frac{d k}{2 \pi} \frac{\left[k^{2}+\omega^{2}\right]^{-1 / 2}}{\exp \left[L_{y} \Lambda \sqrt{k^{2}+\omega^{2}}\right]-1},
\tag{48}
$$

and adjust it such that we obtain Eq. (47) in the limit $L_y \to \infty$. The gap equation is then solved numerically for finite $L_y$.

### 11. Comparisons with Numerical Results
The results for the three regimes a), b) and c) in the isotropic case $\lambda=1$ are plotted in Fig. (3) together with Monte Carlo results on 4- and 6-legged ladders with periodic boundary conditions. We have used the parameters specified in Eq. (16). The Monte Carlo results shown here are taken from Ref. 5. In the same figure we also show a comparison for the two-legged ladder. Here the Monte Carlo data are taken from Ref. 9 and are in this case for a two-legged ladder with open boundary conditions. Our analytic results are for a two-legged ladder with periodic boundary conditions and $(J_{\perp}/J)=1/2$. This anisotropic ladder with periodic boundary conditions should be equivalent to the isotropic two-legged ladder with open boundary conditions. For this anisotropic case, the input parameters $\rho_{\mathrm{s}}$, $\hbar c$ and $\lambda$ are calculated

![](./images/814585980399910913_3.jpg)

Fig. 3. Correlation lengths for 2-, 4- and 6-legged ladders as functions of temperature.

![](./images/814585980399910913_4.jpg)

Fig. 4. Correlation lengths for 3- and 5-legged ladders as functions of temperature.

from the spin-wave expansion to order $1/S$. The low temperature curves are all adjusted such that they match the Monte Carlo data at $T=0$. Other than this there are no adjustable parameters.

Figure 4 show results for 3- and 5-legged ladders. The parameters are also here as in Eq. (16). We have used the expression Eq. (34) for low temperatures with $T_0=2.679J.^{22}$ The Monte Carlo data here are taken from Ref. 9 and are for ladders with open boundary conditions.

### 12. Conclusion
We have shown how spin ladders can be treated quantitatively using a $\sigma$-model embedded in a space where the imaginary-time dimension and one of the space dimensions are finite. The most encouraging and perhaps surprising result is that this view of spin ladders as finite-sized 2D antiferromagnets gives good agreements with Monte Carlo simulations all the way down to ladders with as few as three to four legs. It would be interesting in a future study to understand dynamic properties of spin ladders using similar techniques.

### Acknowledgments
The author thanks Sudip Chakravarty for lots of help with making this paper more readable, and Lan Yin for many stimulating discussions and for helpful comments on the manuscript.

### Appendix. Scaling Function

In this appendix we will show how to separate out the $T=0, L_y=\infty$ contribution from the integral $I_{b}$. The procedure is along the lines of Rudnick et al.${}^{20}$

$$
I_{b}=\frac{1}{\beta \hbar c L_{y}} \sum_{\omega, p}^{\prime} \int \frac{d k}{2 \pi} \frac{1}{\omega^{2}+k^{2}+p^{2}+h}. \tag{A.1}
$$

Here $\omega=2 \pi n / \beta \hbar c$ and $p=2 \pi m / L_{y}$. The prime on the sum means that the term $m=n=0$ is excluded. We have included a constant $h$ which we will let go to zero eventually. To ease the notation in this appendix we will shorten $\beta \hbar c$ as $\beta$ and $L_{y} \lambda$ as $L$. Consider first the double sum

$$
S=\sum_{\omega, p}^{\prime} \frac{1}{\omega^{2}+p^{2}+r}, \tag{A.2}
$$

where we have set $r=k^{2}+h$ for convenience. The summand can be written as an integral which again can be split up into two pieces

$$
S=\sum_{\omega, p}^{\prime} \int_{0}^{B} d s e^{-\left(\omega^{2}+p^{2}+r\right) s}+\sum_{\omega, p}^{\prime} \int_{B}^{\infty} d s e^{-\left(\omega^{2}+p^{2}+r\right) s}, \tag{A.3}
$$

$B$ is arbitrary, and should be chosen so as to give good convergence. The first term in (A.3) can be rewritten using Poisson's summation formula

$$
\sum_{\omega, p} f(\omega, p)=\beta L \sum_{u=-\infty}^{\infty} \sum_{v=-\infty}^{\infty} \int \frac{d \omega}{2 \pi} \frac{d p}{2 \pi} e^{i(u \omega \beta+v p L)} f(\omega, p) \tag{A.4}
$$

where $\omega$ and $p$ on the right hand side are continuous variables. Separating out the $u=v=0$ term we get

$$
\begin{aligned}
\sum_{\omega, p}^{\prime} \int_{0}^{B} d s e^{-\left(\omega^{2}+p^{2}+r\right) s}=& \beta L \sum_{u, v}^{\prime} \int_{0}^{B} d s \int \frac{d \omega}{2 \pi} \frac{d p}{2 \pi} e^{\left(i u \omega \beta+i v p L-\omega^{2} s-p^{2} s-r s\right)} \\
&+\beta L \int_{0}^{B} d s \int \frac{d \omega}{2 \pi} \frac{d p}{2 \pi} e^{-\left(\omega^{2}+p^{2}+r\right) s}-\frac{1}{r}\left(1-e^{-B r}\right).
\end{aligned} \tag{A.5}
$$

Completing the squares and performing the gaussian integrals in the first term and performing the integral over $s$ in the second we obtain

$$
\begin{aligned}
\sum_{\omega, p}^{\prime} \int_{0}^{B} d s e^{-\left(\omega^{2}+p^{2}+r\right) s}=& \frac{\beta L}{4 \pi} \int_{1}^{\infty} \frac{d y}{y} e^{-r B / y}\left[X\left(\frac{L^{2} y}{4 B}\right) X\left(\frac{\beta^{2} y}{4 B}\right)-1\right] \\
&+\beta L \int \frac{d \omega}{2 \pi} \frac{d p}{2 \pi} \frac{1-e^{-B\left(\omega^{2}+p^{2}+r\right)}}{\omega^{2}+p^{2}+r} \\
&-\frac{1}{r}\left(1-e^{-B r}\right),
\end{aligned} \tag{A.6}
$$

where we have changed the integration variable $s$ in the first term to $y = B/s$ and defined

$$
X(y) = \sum_{n=-\infty}^{\infty} e^{-n y^{2}}. \tag{A.7}
$$

The $-1$ in the first term is the result of the prime on the $u, v$ sum. The second term in (A.3) can be written as follows when we change the integration variable $s$ to $y = s/B$

$$
\sum_{\omega, p}^{\prime} \int_{B}^{\infty} d s e^{-\left(\omega^{2}+p^{2}+r\right) s}=B \int_{1}^{\infty} d y\left[X\left(\frac{4 \pi^{2} B y}{L^{2}}\right) X\left(\frac{4 \pi^{2} B y}{\beta^{2}}\right)-1\right] e^{-B r y}. \tag{A.8}
$$

To calculate $I_{\text {Int }}$ we will write $r=k^{2}+h$ and integrate over $k$. It is clear that the first part of the second term in (A.6) corresponds to the $T=0, L \rightarrow \infty$ contribution. Writing this term separately, integrating over $k$ and setting $B=\kappa \beta L / 4 \pi^{2}$ we get

$$
\begin{aligned}
I_{b}= & \int \frac{d \omega}{2 \pi} \frac{d k}{2 \pi} \frac{d p}{2 \pi} \frac{1}{\omega^{2}+k^{2}+p^{2}+h} \\
& +\frac{1}{4 \sqrt{\pi \kappa \beta L}} \int_{1}^{\infty} \frac{d y}{\sqrt{y}}\left[X\left(\frac{\pi^{2} L y}{\beta \kappa}\right) X\left(\frac{\pi^{2} \beta y}{L \kappa}\right)-1\right] e^{-\kappa \beta L h / 4 \pi^{2} y} \\
& +\frac{\sqrt{\kappa}}{4 \sqrt{\pi^{3} \beta L}} \int_{1}^{\infty} \frac{d y}{\sqrt{y}}\left[X\left(\frac{\beta \kappa y}{L}\right) X\left(\frac{L \kappa y}{\beta}\right)-1\right] e^{-\kappa \beta L h y / 4 \pi^{2}} \\
& -\int \frac{d \omega}{2 \pi} \frac{d k}{2 \pi} \frac{d p}{2 \pi} \frac{e^{-B\left(\omega^{2}+k^{2}+p^{2}+h\right)}}{\omega^{2}+k^{2}+p^{2}+h} \\
& -\frac{1}{\beta L} \int \frac{d k}{2 \pi} \frac{1-e^{-B\left(k^{2}+h\right)}}{k^{2}+h}. \tag{A.9}
\end{aligned}
$$

It is clear that the above expression is finite as $h \rightarrow 0$. Taking this limit and setting $\kappa=\pi$ we get finally

$$
\begin{aligned}
I_{b}= & \int \frac{d \omega}{2 \pi} \frac{d k}{2 \pi} \frac{d p}{2 \pi} \frac{1}{\omega^{2}+k^{2}+p^{2}} \\
& +\frac{1}{2 \pi \sqrt{\beta L}}\left\{\int_{1}^{\infty} \frac{d y}{\sqrt{y}}\left[X\left(\frac{L \pi y}{\beta}\right) X\left(\frac{\beta \pi y}{L}\right)-1\right]-2\right\}. \tag{A.10}
\end{aligned}
$$

Where we have used

$$
\int \frac{d \omega}{2 \pi} \frac{d k}{2 \pi} \frac{d p}{2 \pi} \frac{e^{-B\left(\omega^{2}+k^{2}+p^{2}\right)}}{\omega^{2}+k^{2}+p^{2}}=\frac{1}{\beta L} \frac{1}{4 \pi^{2}} \sqrt{\frac{\pi}{B}}, \tag{A.11}
$$

$$
\int \frac{d k}{2 \pi} \frac{1-e^{-B k^{2}}}{k^{2}}=\frac{1}{\beta L} \sqrt{\frac{B}{\pi}}. \tag{A.12}
$$

## References

1. Z. Hiroi *et al.*, J. Solid. State. Chem. **95**, 230 (1991).
2. M. Uehara *et al.*, Jour. Phys. Soc. Jpn. **65**, 2764 (1996).
3. F. F. Balakirev *et al.*, "Unconventional Transition from Metallic to Insulating Resis- tivity in the Spin-ladder Compound (Sr, Ca)₁₄Cu₂4O₄1", cond-mat/9808284.
4. For a review, see E. Dagotto and T. M. Rice, Science **271**, 618 (1996) and references therein.
5. S. Chakravarty, Phys. Rev. Lett. **77**, 4450 (1996).
6. O. F. Syljuåsen, S. Chakravarty and M. Greven, Phys. Rev. Lett. **78**, 4115 (1997).
7. F. D. M. Haldane, Phys. Lett. **93A**, 464 (1983); and Phys. Rev. Lett. **50**, 1153 (1983).
8. S. Chakravarty, B. I. Halperin and D. R. Nelson, Phys. Rev. **B39**, 2344 (1989).
9. M. Greven, R. J. Birgeneau and U.-J. Wiese, Phys. Rev. Lett. **77**, 1865 (1996).
10. F. D. M. Haldane, Phys. Rev. Lett. **61**, 1029 (1988).
11. D. V. Khveshchenko, Phys. Rev. **B50**, 380 (1994).
12. B. B. Beard *et al.*, Phys. Rev. Lett. **80**, 1742 (1998).
13. P. B. Wiegmann, Phys. Lett. **B152**, 209 (1985); JETP Lett. **41**, 95 (1985); P. Hasenfratz, M. Maggiore and F. Niedermayer, Phys. Lett. **B245**, 522 (1990).
14. P. Hasenfratz and F. Niedermayer, Phys. Lett. **B268**, 231 (1991).
15. N. Elstner, A. Sokol, R. R. P. Singh, M. Greven and R. J. Birgeneau, Phys. Rev. Lett. **75**, 938 (1995).
16. B. I. Halperin and P. C. Hohenberg, Phys. Rev. **188**, 898 (1969); S. Chakravarty, B. I. Halperin and D. R. Nelson, op. cit. section IIc.
17. I. Affleck and F. D. M. Haldane, Phys. Rev. **B36**, 5291 (1987).
18. P. Fendley, Phys. Rev. Lett. **93**, 4468 (1999).
19. I. Affleck, D. Gepner, H. J. Schultz and T. Ziman, J. Phys. A, **22**, 511 (1989).
20. J. Rudnick, H. Guo and D. Jasnow, J. Stat. Phys. **41**, 353 (1985).
21. M. Fisher, Am. Jour. Phys. **32**, 343 (1964).
22. K. Nomura and M. Yamada, Phys. Rev. **B43**, 8217 (1991).