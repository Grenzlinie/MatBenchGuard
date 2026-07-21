# THE COULOMB EXPLOSION OF CHARGED DROPS

I.T. Iakubov, A.G. Khrapak, L.I. Podlubny* and V.V. Pogosov

Institute of High Temperatures of the Academy of Sciences of the USSR, Moscow 127412, USSR

(Received 13 August 1984 by L. Hedin)

In the framework of the density functional theory using a simple variational model we have calculated the first-order size corrections to electrophysical characteristics of small metal particles. We have discovered that the curvature correction to the surface energy is of positive sign. We have shown that it is possible to use macroscopic electrodynamics in calculations of the ionization potential and the electron affinity. We have determined the maximum charge which can be retained by a particle of a given size.

## 1. INTRODUCTION
THE PHENOMENA in systems with large specific surface are different from those in massive samples. The surface properties of metal particles determine the features of physical processes in different fine-dispersed media (evaporation and condensation, nucleation, thermo- and auto-electronic emission, the interaction with light and electron beams, etc.). One of the interesting effects here is the so called Coulomb explosion, a process in which an overcharged particle emits the surplus part of its charge. The consequences of the Coulomb explosion of small positively charged particles were observed by Sattler *et al.* [1] They were not able to detect a double-charged particle that would have a size smaller than some value.

In order to build a theory we must determine the energy characteristics of small particles. The most consistent approach is offered by the density functional theory (Hohenberg, Kohn, Sham [2, 3]), which was successfully used in calculations of the surface energy and the work function of planar metal surface [4, 5].

The size dependence of the work function and the electron affinity was studied in [6-10]. The authors mostly present the results of numerical calculations only, so these results are difficult to analyse and to interpret. In [7] and [10] the attention was focused on consideration of the size effect, which plays an important role only in the case of very small particles (containing 10-100 atoms). We will consider larger particles for which the size effects are connected with the curvature of the surface layer which leads to changes in the electrostatic potential and the electron distribution. By using the direct variational method with a simple trial function we were able to obtain the first-order size corrections to different electrophysical quantities in the analytical form.

The main qualitative results of this paper are the following. (i) We have found a positive curvature correction to the surface energy. (ii) We have shown that it is possible to use macroscopic electrodynamics in calculations of the work function. (iii) We have determined the maximum charge which can be retained by a metal particle of a given size; the particles with larger charges are unstable against the Coulomb explosion, i.e. the emission of the "surplus" electrons and ions. This result is in good agreement with experiment [1].

## 2. THE SURFACE ENERGY OF A NEUTRAL PARTICLE
In the following calculations we use the jellium model for describing the ion subsystem; as for electrons, we employ the local density approximation [4, 5]. So the energy of electrons can be presented as a functional of the electron density

$$
E\{n(\mathbf{r})\}=E_{k}+E_{x c}+E_{q}, \tag{1}
$$

where $E_{k}$ is the kinetic energy (with the first gradient correction), $E_{xc}$ is the exchange-correlation energy, and $E_{q}$ is the Coulomb energy:

$$
\begin{aligned}
E_{k}=E_{t}+E_{g} & =\frac{3}{10}\left(3 \pi^{2}\right)^{2 / 3} \int n^{5 / 3}(\mathbf{r}) d^{3} r \\
& +\frac{1}{72} \int \frac{|\nabla n(\mathbf{r})|^{2}}{n(\mathbf{r})} d^{3} r, \tag{2}
\end{aligned}
$$

$$
\begin{aligned}
E_{x c}= & -\int n(\mathbf{r})\left[\frac{3}{4}\left(\frac{3}{\pi}\right)^{1 / 3} n^{1 / 3}(\mathbf{r})+0.0474\right. \\
& \left.+0.0155 \ln \left(3 \pi^{2} n(\mathbf{r})\right)^{1 / 3}\right] d^{3} r \tag{3}
\end{aligned}
$$

* Moscow Power Institute, Moscow 111250, USSR

---

$$
E_{q}=\frac{1}{2} \int\left[n(\mathbf{r})-n_{+}(\mathbf{r})\right] \varphi(\mathbf{r}) d^{3} r,
$$

where
$$
\varphi(\mathbf{r})=\int \frac{n\left(\mathbf{r}^{\prime}\right)-n_{+}\left(\mathbf{r}^{\prime}\right)}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|} d^{3} r^{\prime}
$$

is the electrostatic potential; $n_{+}(\mathbf{r})$ is the ion density.

The electron density can be found by minimizing the functional $E\{n(\mathbf{r})\}$. We use the following trial function
$$
n(\mathbf{r})=n_{+}\{1+\exp [b(r-R')]\}^{-1}.
$$

Here $n_{+}$is the density of electrons and ions in a homogeneous system, and $b^{-1}$ determines the thickness of the surface layer. The effective radius of the electron cloud $R^{\prime}$ does not coincide with the particle's radius $R$. These two radii are related by the neutrality condition
$$
\int\left[n(\mathbf{r})-n_{+}(\mathbf{r})\right] d^{3} r=0, \quad n_{+}(r)=n_{+} \theta(R-r).(7)
$$

The functional $E\{n(\mathbf{r})\}$ can be presented in the form
$$
E\{n(\mathbf{r})\}=\frac{4}{3} \pi R^{3} \epsilon\left\{n_{+}\right\}+\int\left[\epsilon\{n(\mathbf{r})\}-\epsilon\left\{n_{+}(\mathbf{r})\right\}\right] d^{3} r, \quad(8)
$$

where $\epsilon\{n\}$ is the volume energy density. The first term in (8) describes a homogeneous system, while the second term accounts for the inhomogeneity of the boundary surface and is equal to $4 \pi R^{2} \sigma(R)$, where $\sigma$ is the surface energy density. Using (6) we have
$$
\begin{aligned}
4 \pi R^{2} \sigma(R)= & \frac{4 \pi R^{\prime 2}}{b} \int_{-a^{\prime}}^{+\infty}\left(1+\frac{x}{a^{\prime}}\right)^{2} \\
& \times\left[\epsilon\{n(x)\}-\epsilon\left\{n_{+}(x)\right\}\right] \mathrm{d} x,
\end{aligned}
$$

where $a^{\prime}=b R^{\prime}$ and $x=b\left(r-R^{\prime}\right)$. Parameter $b$ is determined by the condition $d \sigma / d b=0$. Since the macroscopic approach is valid only for large particles, we must have $a^{\prime} \gg 1$. The case $a=\infty$ was studied by Smith [4]. The curvature corrections can be obtained from (9) by expanding the integrand into a series in powers of $1/a'$
$$
\begin{aligned}
\sigma(R) & =\sigma^{0}\left[1+\sum_{k=1}^{\infty} \frac{C^{k}}{R^{\prime k}}\right], \\
\sigma^{0} & =\frac{1}{b} \int_{-\infty}^{+\infty}\left[\epsilon\{n(\mathbf{r})\}-\epsilon\left\{n_{+}(\mathbf{r})\right\}\right] \mathrm{d} x.
\end{aligned}
$$

In order to transform the expansion in powers of $R^{\prime-1}$ into an expansion in powers of $R^{-1}$ we use (7), which gives
$$
a^{\prime}=a\left(1-\frac{\pi^{2}}{3 a^{2}}+O\left(\frac{1}{a^{4}}\right)\right).
$$

Substituting (6) into (7) and using (10) and (11), we get
$$
\sigma(R)=\sigma^{0}+\sigma^{1}/R b
$$

where
$$
\begin{aligned}
\sigma^{j}= & C_{g}^{j} n_{+} b^{-3}-C_{t}^{j} n_{+}^{5/3} b^{-1}+C_{\mathrm{ex}}^{j} n_{+}^{4/3} b^{-1} \\
& +C_{\mathrm{c}}^{j} n_{+} b^{-1}+C_{g}^{j} n_{+} b, \quad j=0,1.
\end{aligned}
$$

<table>
<caption>Table 1. The valuer of coefficient in (13).</caption>
<thead>
<tr>
<th>$j$</th>
<th>$C_{q}^{j}$</th>
<th>$C_{t}^{j}$</th>
<th>$C_{\mathrm{ex}}^{j}$</th>
<th>$C_{\mathrm{c}}^{j}\cdot 10^{3}$</th>
<th>$C_{g}^{j}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>3.768</td>
<td>2.184</td>
<td>0.329</td>
<td>8.556</td>
<td>6.94</td>
</tr>
<tr>
<td>1</td>
<td>0</td>
<td>0.824</td>
<td>0.275</td>
<td>16.210</td>
<td>14.1</td>
</tr>
</tbody>
</table>

The values of coefficients $C^{j}$ are presented in Table 1. The condition $d \sigma / d b=0$ permits us to determine the value of $b$ which minimizes the surface energy
$$
b \cong b^{0}+R^{1}/R b^{0}.
$$

As one can see from (13), $b^{0}$ is a real root of a biquadratic equation, while $b^{1}$ is easily found by successive approximations. The values of $b^{j}$ and $\sigma^{j}$ are presented in Table 2. The values of $\sigma^{0}$ are in satisfactory agreement with experimental data (Spilrain *et al* [11]).

In the adopted approach the surface energy results from the spreading of the electron gas beyond the limits of the ion frame of the particle. In a sense one can speak of an effective increase of the particle's radius which corresponds to greater expenditures of energy necessary to create the particle surface. Because of this $\sigma^{1}>0$.

### 3. THE IONIZATION ENERGY AND THE ELECTRON AFFINITY

Let $E_{N+Z}\{n(\mathbf{r})\}$ be the energy of a particle with $\mathrm{N}$ ions and $N+Z$ electrons. The electron distribution $n_{Z}(\mathbf{r})$ differs from $n(\mathbf{r})$ by a quantity $\delta n(\mathbf{r})$,
$$
\int n(\mathbf{r}) d^{3} r=N, \quad \int \delta n(\mathbf{r}) d^{3} r=Z.
$$

When the $N+Z$-th electron is removed the energy changes by
$$
\Delta E(Z)=E_{N+Z-1}-E_{N+Z}.
$$

In particular, $\Delta E(0)$ determines the first ionization potential $I$, while $\Delta E(1)$ determines the electron affinity $A$
$$
\begin{aligned}
& I=\Delta E(0)=E_{N-1}-E_{N}, \\
& A=\Delta E(1)=E_{N}-E_{N+1}.
\end{aligned}
$$

**Table 2. The calculated valuer of $b^0, b^1, \sigma^0, \sigma^1, \mu^1$, $e=m=\hbar=1$.**

<table>
  <thead>
    <tr>
      <th></th>
      <th>$n_+\cdot10^3$</th>
      <th>$b^0$</th>
      <th>$b^1$</th>
      <th>$\sigma^0\cdot10^5$</th>
      <th>$\sigma^1\cdot10^5$</th>
      <th>$\mu^1\cdot10^2$</th>
      <th>$\sigma^0_{\text{exp}}\cdot10^5$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cs</td>
      <td>1.33</td>
      <td>1.82</td>
      <td>2.16</td>
      <td>3.13</td>
      <td>4.01</td>
      <td>$-5.39$</td>
      <td>4.59</td>
    </tr>
    <tr>
      <td>Rb</td>
      <td>1.67</td>
      <td>1.81</td>
      <td>2.12</td>
      <td>3.84</td>
      <td>5.05</td>
      <td>$-5.54$</td>
      <td>5.95</td>
    </tr>
    <tr>
      <td>K</td>
      <td>1.95</td>
      <td>1.80</td>
      <td>2.08</td>
      <td>4.38</td>
      <td>5.89</td>
      <td>$-5.65$</td>
      <td>7.32</td>
    </tr>
    <tr>
      <td>Na</td>
      <td>3.77</td>
      <td>1.74</td>
      <td>1.75</td>
      <td>7.07</td>
      <td>11.1</td>
      <td>$-6.19$</td>
      <td>12.5</td>
    </tr>
    <tr>
      <td>Li</td>
      <td>6.92</td>
      <td>1.68</td>
      <td>1.24</td>
      <td>8.6</td>
      <td>18.7</td>
      <td>$-6.48$</td>
      <td>25.6</td>
    </tr>
  </tbody>
</table>

For a planar surface $T = A = W = -\mathrm{d}E/\mathrm{d}N$ where $W$ is the electron work function, and $\mu$ is the electron chemical potential. In a finite sample both $I$ and $A$ depend on the radius $R$. This dependence is basically determined by a strong electrostatic "self-interaction" of the uncompensated charge $Z$.

As well known, the averaging of Maxwell equations over a sufficiently large volume and the use of macroscopic electrodynamics lead to an abrupt disappearance of the external field inside the metal and to localization of the uncompensated charge on the metal surface. In this approach the electrostatic energy of a charged sphere equals $Z^2/2R$,
$$
I\ =\ W+Z^2/2R,\qquad A\ =\ W-Z^2/2R. \tag{18}
$$

We will show that the result of microscopic calculations using the density functional theory is approximately the same.

We use the expansion of $\Delta E(Z)$ into a functional series in $\delta n(\mathbf{r})$
$$
\begin{align}
E_{N+Z}\{n(\mathbf{r})+\delta n(\mathbf{r})\} &= E_N\{n(\mathbf{r})\} + \int \frac{\delta E_{N+Z}}{\delta n} \\
&\quad \times \bigg|_{Z=0} \delta n(\mathbf{r})d^3r + \frac{1}{2!} \int \frac{\delta^2 E_{N+Z}}{\delta n(\mathbf{r})\delta n(\mathbf{r}')} \bigg|_{Z=0} \\
&\quad \times \delta n(\mathbf{r})\delta n(\mathbf{r}')d^3rd^3r' + \dots \tag{19}
\end{align}
$$

Let the density of the uncompensated charge concentrated inside the surface layer be small in comparison with the ambient electron density
$$
|Z| \ll 4\pi R^2b^{-1}n_+. \tag{20}
$$

In this case we can confine ourselves to the terms given in (19), neglect the dependence of $b$ on $Z$ and choose $\delta n(r)$ in a convenient form
$$
\delta n(r)\ =\ -c\frac{\mathrm{d}n(r)}{\mathrm{d}r},\qquad c\ =\ Z/4\pi R^2n_+. \tag{21}
$$

Now (19) can be approximately rewritten as
$$
E_{N+Z}-E_N\ \cong\ \mu_N Z+Z^2/2R, \tag{22}
$$
where $\mu_N=\delta E_N/\delta n(r)$ is the chemical potential of an electron in a neutral particle. In analogy with $\sigma(R)$ in (12) $\mu_N$ can be presented by the form
$$
\mu_N\ =\ \mu(R)\ =\ \mu^0+\mu^1/Rb^0 \tag{23}
$$

In a halfinfinite metal $\mu^0$ equals [4, 5]
$$
\begin{align}
\mu^0\ &=\ -W\ =\ \frac{\mathrm{d}\epsilon\{n_+\}}{\mathrm{d}n_+}-\Delta\varphi, \\
\Delta\varphi\ &=\ -\varphi(-\infty)\ =\ \frac{2\pi^3n_+}{3(b^0)^3}, \tag{24}
\end{align}
$$
where the potential is chosen to be zero at large distances from the metal ($\varphi(+\infty)=0$).

When $Z=\pm1$ (23) specifies the classical formula (18):
$$
\begin{align}
E_N-E_{N+1}\ &=\ \int\left[\epsilon\{n(\mathbf{r})+\delta n(\mathbf{r})\}-\epsilon\{n(\mathbf{r})\}\right]d^3r \\
&=\ \mp\mu_N-\frac{1}{2R}\ =\ \pm W-\frac{1}{2R}\pm\frac{\mu^1}{Rb^0}. \tag{25}
\end{align}
$$

In the integrand of (25) we have retained only the terms $\sim\delta n$ and $(\delta n)^2$. A straightforward integration gives
$$
\mu^1\ =\ -\Delta\varphi\left(\frac{1}{2}+\frac{b^1}{b^0}\right)-\frac{2o^0b^0}{n_+}+\frac{(b^0)^2}{72}. \tag{26}
$$

The numerical $\mu^1$ are presented in Table 2. As one can see, the correction term $\mu^1/Rb^0$ in (25) is no greater than a few per cent of the term $1/2R$, so by accounting this term we actually exceed the precision of our method. The size effect is basically determined by the self-interaction of the uncompensated charge.

## 4. THE CRITICAL CHARGE OF A PARTICLE

A negatively charged particle can retain $Z$ "surplus" electrons only when the energy of this state is smaller than the energy of the state with $Z-1$ electrons, i.e. $\Delta E(Z)>0$. Let us call the number of electrons $Z^*$ for which $\Delta E(Z^*)=0$ a critical number. From (16) and (22) it follows that
$$
Z^*\ =\ -\mu_NR+\frac{1}{2}. \tag{27}
$$

When $Z\rightarrow Z^*$ the electron affinity $A(Z)\ =\ -\mu_N+(1-2Z)/2R$ tends to zero.

The calculated $Z^*$ are presented in Fig. 1. Let us

![](./images/812446795928961025_1.jpg)

Fig. 1. The calculated dependence of $Z^{*}$ on $R$: (1) Li;
(2) Na; (3) Cs.

note an interesting fact: even for particles containing
more than a thousand ions the critical charge does
not exceed a few units. This fact is due to the strong
Coulomb repulsion of the surplus charge spread near
the surface of the particle. The situation is different for
atomic and molecular ions, where the electrons are not
collectivized. The extrapolation of the sodium electron
affinities calculated by Cini [6] results in $Z^{*}=1$ for
$R \cong 6 a_{0}$. Our calculations give $R(Z^{*}=1) \cong 7 a_{0}$.

When $Z>Z^{*}$ the particle is overcharged. There is
a potential barrier between the free and bounded states,
so the particle with $Z>Z^{*}$ can exist for some time.
The lifetime is determined by specific conditions in
non-equilibrium system. According to (20) we can
describe the charges that do not exceed $Z=4 \pi R^{2} b^{-1} n_{+}$.

## 5. THE COULOMB EXPLOSION OF POSITIVELY CHARGED PARTICLES

Let us consider now a positively charged drop of a
conductive fluid, which contains $N$ electrons and $N+Z$
ions. Its energy $E^{N+Z}$ is related to the energy of a
neutral drop $E^{N}$ in the following way

$$
E^{N+Z}=E^{N}-Z W_{+}+Z^{2} / 2 R,
\tag{28}
$$

where $W_{+}$is the ion work function for a plane surface.
As in (25) we will assume that the most essential
dependence on $R$ is given by the self-interaction of the
surplus charge $Z$. A rigorous derivation of (28) involves
additional calculations which are not presented in this
paper. Let us consider the question of the maximum
possible value of $Z$ for a particle with the radius $R$.

The change in the energy due to the detachment
of one of the ions is

$$
\Delta E(Z)=E^{N+Z-1}-E^{N+Z}=-W_{+}+(2 Z-1) / 2 R.
\tag{29}
$$

A particle with the charge $Z$ can exist in equilibrium
only if $\Delta E(Z)>0$. For the critical charge we have

$$
Z^{*}=W_{+} R+\frac{1}{2}
\tag{30}
$$

If $Z>Z^{*}$ the particle emits a surplus ion.

Using the Born cycle (e.g., [12]) we can express
the ion work function in terms of the ionization
potential of the atom $I_{a}$, the evaporation heat per
atom $q$ and the electron work function $W$:

$$
W_{+}=q+I_{a}-W.
\tag{31}
$$

For $Pb$ Kikoin's Handbook [14] gives $q=1.5$,
$W=4.0, I_{a}=7.4, W_{+}=5.3$. For $R=12 a_{0}$ the critical
charge is equal to 2.8. This result is in good agreement
with recent measurements [1] and with the results
of more complicated calculations [13]. In the case of
$Na$ ($q=0.9, I_{a}=2.3, W=5.1, W_{+}=3.7$) for the same
radius we have $Z^{*}=2.1$.

## REFERENCES

1. Sattler,K., J. Muhlbach, O. Echt & E. Recknagel,
*Phys. Rev. Lett.* **47**, 160 (1981).
2. P. Hohenberg & W. Kohn, *Phys. Rev.* **136**, B864 (1964).
3. W. Kohn & L. Sham, *Phys. Rev.* **140**, A 1133 (1965).
4. J.R. Smith, *Phys. Rev.* **181**, 532 (1969).
5. N.D. Lang, *Solid State Physics* **28**, 225 (1973).
6. M. Cini, *J. Catalysis* **37**, 187 (1975).
7. J.L. Martins, R. Car & J. Buttet, *Surf. Sci.* **106**, 265 (1981).
8. L.I. Podlubny, I.V. Avilova & L.Y. Chuchukina,
*Trudy MEI* (Proceedings of Moscow Power Institute) **512**, 15 (1981); **602**, 42 (1983).
9. D.R. Snider & R.S. Sorbello, *Solid State Commun.* **47**, 845 (1983).
10. W. Ekardt, *Phys. Rev.* **B29**, 1558 (1984).
11. E.E. Shpilrain, K.A. Yakimovich, E.E. Totsky,
D.L. Timrot & V.A. Fomin. *Termofisicheskie svoistva schelochnykh metallov* (Termophysical Properties of Alkali Metals), Izdatel'stvo Standartov, Moscow, p. 370 (1970).
12. A.G. Khrapak & I.T. Iakubov, *Electrony v plotnykh gasakh i plasme* (Electrons in Dense Gases and Plasma), p. 202, p. 250, Nauka, Moscow, (1981).
13. D. Tomanek, S. Mukherjee & K.H. Bennemann,
*Phys. Rev.* **B28**, 665 (1983).
14. I.K. Kikoin, (ed), *Tablitsy fisicheskikh velichin* (Tables of Physical Values), Atomizdat, Moscow, p. 420, p. 444, (1976).