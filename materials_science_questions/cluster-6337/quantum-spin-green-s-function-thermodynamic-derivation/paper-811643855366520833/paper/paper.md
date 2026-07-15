# Correlation energy of the spin-polarized uniform electron gas at high density

Pierre-François Loos* and Peter M. W. Gill†

Research School of Chemistry, Australian National University, Canberra ACT 0200, Australia

(Received 17 May 2011; published 21 July 2011)

The correlation energy per electron in the high-density uniform electron gas can be written as $E_{\rm c}(r_s,\zeta) = \lambda_0(\zeta)\ln r_s + \varepsilon_0(\zeta) + \lambda_1(\zeta)r_s\ln r_s + O(r_s)$, where $r_s$ is the Seitz radius and $\zeta$ is the relative spin polarization. We derive an expression for $\lambda_1(\zeta)$ that is exact for any $\zeta$, including the paramagnetic and ferromagnetic limits, $\lambda_1(0)$ and $\lambda_1(1)$, and discover that the previously published $\lambda_1(1)$ value is incorrect. We trace this error to an integration and limit that do not commute. The spin resolution of $\lambda_1(\zeta)$ into contributions of electron pairs is also derived.

DOI: 10.1103/PhysRevB.84.033103

PACS number(s): 71.10.Ca, 71.15.Mb

The final decades of the 20th century witnessed a major revolution in solid-state and molecular physics, as the introduction of sophisticated exchange-correlation models¹ propelled density-functional theory (DFT) from qualitative to quantitative usefulness. In principle, the foundation of DFT is the Hohenberg-Kohn theorem² but, in practice, it is usually the supposed similarity between the electron density in a real system and the electron density in the hypothetical uniform electron gas (UEG).³

The three-dimensional UEG is characterized by a density $\rho = \rho_\uparrow + \rho_\downarrow$, where $\rho_\uparrow$ and $\rho_\downarrow$ is the (uniform) density of the spin-up and spin-down electrons, respectively. In order to guarantee its stability, the electrons are assumed to be embedded in a uniform background of positive charge.

In 1965, Kohn and Sham⁴ showed that the knowledge of an analytical parametrization of the UEG correlation energy allows one to perform approximate calculations for atoms, molecules, and solids. This led to the development of various spin-density correlation functionals (VWN,⁵ PZ,⁶ PW92,⁷ etc.), all of which require information on the high- and low-density regimes of the spin-polarized UEG, and are parametrized using results from near-exact quantum Monte Carlo (QMC) calculations.⁸⁻¹⁵

However, inspired by Wigner’s seminal work,¹⁶ Sun, Perdew, and Seidl have recently shown that the correlation energy of the UEG can be estimated accurately without any QMC input.¹⁷ They used a density-parameter interpolation (DPI) between the (near-) exact high- and low-density regimes, which precisely reproduces the first few coefficients of the high- and low-density energy expansions.¹⁸ Knowledge of these coefficients, of course, is essential for such interpolations, and is the motivation for the present work. We use atomic units throughout.

The high-density expansion of the correlation energy per electron (or reduced energy) of the UEG is¹⁶,¹⁷,¹⁹⁻²⁸

$$
E_{\rm c}(r_s,\zeta) = \lambda_0(\zeta)\ln r_s + \varepsilon_0(\zeta) + \lambda_1(\zeta)r_s\ln r_s + O(r_s), \tag{1}
$$

where $r_s = (4\pi\rho/3)^{-1/3}$ is the so-called Seitz radius and $\zeta = (\rho_\uparrow - \rho_\downarrow)/\rho$ is the relative spin polarization. It is clear that $\lambda_0(\zeta), \varepsilon_0(\zeta), \lambda_1(\zeta), \dots$ must be even functions.

The coefficient $\lambda_0(\zeta)$ can be obtained by the Gell-Mann–Brueckner resummation technique,²² which sums the most divergent terms of the series (1) to obtain

$$
\lambda_0(\zeta) = \frac{3}{32\pi^3}\int_{-\infty}^{\infty} [R_0(u,\zeta)]^2 du, \tag{2}
$$

where

$$
R_0(u,\zeta) = k_\downarrow R_0\left(\frac{u}{k_\downarrow}\right) + k_\uparrow R_0\left(\frac{u}{k_\uparrow}\right), \tag{3}
$$

$$
R_0(u) = 1 - u \arctan(1/u), \tag{4}
$$

and $k_{\uparrow,\downarrow} = (1 \pm \zeta)^{1/3}$ is the Fermi momentum of the spin-up or spin-down electrons. The paramagnetic¹⁹ ($\zeta = 0$) and ferromagnetic²⁵ ($\zeta = 1$) limits are given in Table I and the spin-scaling function

$$
\begin{aligned}
\Lambda_0(\zeta) = \frac{\lambda_0(\zeta)}{\lambda_0(0)} &= \frac{1}{2} + \frac{1}{4(1 - \ln 2)}\bigg[ k_\downarrow k_\uparrow(k_\downarrow + k_\uparrow) \\
&\quad - k_\downarrow^3 \ln\left(1 + \frac{k_\uparrow}{k_\downarrow}\right) - k_\uparrow^3 \ln\left(1 + \frac{k_\downarrow}{k_\uparrow}\right) \bigg]
\end{aligned} \tag{5}
$$

was obtained by Wang and Perdew.²⁷

The coefficient $\varepsilon_0(\zeta)$ is usually written as the sum

$$
\varepsilon_0(\zeta) = \varepsilon_0^a(\zeta) + \varepsilon_0^b \tag{6}
$$

of a RPA (random-phase approximation) term $\varepsilon_0^a(\zeta)$ and a first-order exchange term $\varepsilon_0^b$. The RPA term $\varepsilon_0^a(\zeta)$ is not known in closed form, but it can be computed numerically with high precision.²⁸ Its paramagnetic and ferromagnetic limits are given in Table I and the spin-scaling function $\Upsilon_0^a(\zeta) = \varepsilon_0^a(\zeta)/\varepsilon_0^a(0)$ can be found using Eq. (20) in Ref. 28. The first-order exchange term²⁶ is given in Table I and, because it is independent of the spin polarization, the spin-scaling function $\Upsilon_0^b(\zeta) = \varepsilon_0^b(\zeta)/\varepsilon_0^b(0) = 1$ is trivial.

The coefficient $\lambda_1(\zeta)$ can be written similarly²⁴ as

$$
\lambda_1(\zeta) = \lambda_1^a(\zeta) + \lambda_1^b(\zeta), \tag{7}
$$

where

$$
\lambda_1^a(\zeta) = -\frac{3\alpha}{8\pi^5}\int_{-\infty}^{\infty} \mathcal{R}_1^a(u,\zeta) du, \tag{8}
$$

$$
\lambda_1^b(\zeta) = \frac{3\alpha}{16\pi^4}\int_{-\infty}^{\infty} \mathcal{R}_1^b(u,\zeta) du \tag{9}
$$

are the RPA and second-order exchange contributions and $\alpha = (9\pi/4)^{-1/3}$. The integrand functions are⁷,¹⁷

$$
\mathcal{R}_1^a(u,\zeta) = R_0(u,\zeta)^2 R_1(u,\zeta), \tag{10}
$$

$$
\mathcal{R}_1^b(u,\zeta) = R_0(u,\zeta) R_2(iu,\zeta), \tag{11}
$$

$$
R_1(u,\zeta) = k_\downarrow^{-1} R_1\left(\frac{u}{k_\downarrow}\right) + k_\uparrow^{-1} R_1\left(\frac{u}{k_\uparrow}\right), \tag{12}
$$


<table><caption>TABLE I. Energy coefficients and spin-scaling functions of the paramagnetic ($\zeta=0$) and ferromagnetic ($\zeta=1$) states of the high-density UEG. Note that $\alpha=(9\pi/4)^{-1/3}$ and $z(n)$ is the Riemann $\zeta$ function (Ref. 29).</caption>
<thead>
  <tr>
    <th>Term</th>
    <th>Coefficient</th>
    <th>Paramagnetic Limit $\varepsilon(0)$, $\lambda(0)$</th>
    <th>Ferromagnetic Limit $\varepsilon(1)$, $\lambda(1)$</th>
    <th>Spin-Scaling Function $\Upsilon(\zeta)$, $\Lambda(\zeta)$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$\ln r_s$</td>
    <td>$\lambda_0(\zeta)$</td>
    <td>$\dfrac{1 - \ln 2}{\pi^2}$</td>
    <td>$\dfrac{1 - \ln 2}{2\pi^2}$</td>
    <td>Eq. (5)</td>
  </tr>
  <tr>
    <td>$r_s^0$</td>
    <td>$\varepsilon_0^a(\zeta)$</td>
    <td>$-0.0710995$</td>
    <td>$-0.0499167$</td>
    <td>Ref. 28</td>
  </tr>
  <tr>
    <td></td>
    <td>$\varepsilon_0^b(\zeta)$</td>
    <td>$\dfrac{\ln 2}{6} - \dfrac{3}{4\pi^2} z(3)$</td>
    <td>$\dfrac{\ln 2}{6} - \dfrac{3}{4\pi^2} z(3)$</td>
    <td>1</td>
  </tr>
  <tr>
    <td>$r_s \ln r_s$</td>
    <td>$\lambda_1^a(\zeta)$</td>
    <td>$\dfrac{\alpha}{24\pi^3} (\pi^2 - 6)$</td>
    <td>$\dfrac{1}{27^{/3}} \dfrac{\alpha}{24\pi^3} (\pi^2 + 6)$</td>
    <td>Eq. (16)</td>
  </tr>
  <tr>
    <td></td>
    <td>$\lambda_1^b(\zeta)$</td>
    <td>$\dfrac{\alpha}{4\pi^3} (\pi^2 - 12 \ln 2)$</td>
    <td>$\dfrac{1}{2^{4/3}} \dfrac{\alpha}{4\pi^3} (\pi^2 - 12 \ln 2)$</td>
    <td>Eq. (17)</td>
  </tr>
</tbody>
</table>

$$
R_{2}(i u, \zeta)=R_{2}\left(i \frac{u}{k_{\downarrow}}\right)+R_{2}\left(i \frac{u}{k_{\uparrow}}\right),\qquad(13)
$$

$$
R_{1}(u)=-\frac{\pi}{3\left(1+u^{2}\right)^{2}},\qquad(14)
$$

$$
R_{2}(i u)=4 \frac{\left(1+3 u^{2}\right)-u\left(2+3 u^{2}\right) \arctan u}{1+u^{2}}.\qquad(15)
$$

Carr and Maradudin gave an estimate $^{24}$ of $\lambda_1(0)$, and this was later refined by Perdew and coworkers. $^{7,17}$

However, we have found that the integrals in Eqs. (8) and (9) can be evaluated exactly by computer software, $^{30}$ giving the paramagnetic and ferromagnetic values in Table I and the spin-scaling functions

$$
\begin{aligned}
\Lambda_{1}^{a}(\zeta)= & \frac{3}{\pi^{2}-6}\left\{\left(\frac{\pi^{2}}{6}+\frac{1}{4}\right)\left(k_{\downarrow}^{2}+k_{\uparrow}^{2}\right)-\frac{3}{2} k_{\downarrow} k_{\uparrow}\right. \\
& -\frac{k_{\downarrow}^{2}+k_{\uparrow}^{2}}{k_{\downarrow}^{2}-k_{\uparrow}^{2}} k_{\downarrow} k_{\uparrow} \ln \left(\frac{k_{\downarrow}}{k_{\uparrow}}\right)-\frac{k_{\downarrow}^{2}-k_{\uparrow}^{2}}{2} \\
& \left.\times\left[\operatorname{Li}_{2}\left(\frac{k_{\downarrow}-k_{\uparrow}}{k_{\downarrow}+k_{\uparrow}}\right)-\operatorname{Li}_{2}\left(\frac{k_{\uparrow}-k_{\downarrow}}{k_{\downarrow}+k_{\uparrow}}\right)\right]\right\},
\end{aligned}\qquad(16)
$$

$$
\begin{aligned}
\Lambda_{1}^{b}(\zeta)= & \frac{3}{\pi^{2}-12 \ln 2}\left\{\frac{\pi^{2}}{6}\left(k_{\downarrow}^{2}+k_{\uparrow}^{2}\right)+(1-\ln 2)\left(k_{\downarrow}-k_{\uparrow}\right)^{2}\right. \\
& -\frac{k_{\downarrow}^{2}}{2} \operatorname{Li}_{2}\left(\frac{k_{\downarrow}-k_{\uparrow}}{k_{\downarrow}+k_{\uparrow}}\right)-\frac{k_{\uparrow}^{2}}{2} \operatorname{Li}_{2}\left(\frac{k_{\uparrow}-k_{\downarrow}}{k_{\downarrow}+k_{\uparrow}}\right) \\
& +\frac{1}{k_{\downarrow} k_{\uparrow}}\left[k_{\downarrow}^{4} \ln \left(\frac{k_{\downarrow}}{k_{\downarrow}+k_{\uparrow}}\right)+k_{\downarrow}^{2} k_{\uparrow}^{2} \ln \left(\frac{k_{\downarrow} k_{\uparrow}}{\left(k_{\downarrow}+k_{\uparrow}\right)^{2}}\right)\right. \\
& \left.\left.+k_{\uparrow}^{4} \ln \left(\frac{k_{\uparrow}}{k_{\downarrow}+k_{\uparrow}}\right)\right]\right\},
\end{aligned}\qquad(17)
$$

where $\operatorname{Li}_2$ is the dilogarithm function. $^{29}$

The spin scalings $\Lambda_0(\zeta)$, $\Upsilon_0^a(\zeta)$, $\Upsilon_0^b(\zeta)$, $\Lambda_1^a(\zeta)$, and $\Lambda_1^b(\zeta)$ are shown in Fig. 1, highlighting the Hoffmann minimum $^{28}$ in $\Upsilon_0^a(\zeta)$ near $\zeta=0.9956$ and revealing a similar minimum in $\Lambda_1^a(\zeta)$ near $\zeta=0.9960$. Such minima seem to be ubiquitous in RPA coefficients.

The data in Table I yield the exact values

$$
\lambda_{1}(0)=\frac{\alpha}{4 \pi^{3}}\left(\frac{7 \pi^{2}}{6}-12 \ln 2-1\right)=0.00922921 \ldots, \text { (18) }
$$

$$
\lambda_{1}(1)=2^{-4 / 3} \frac{\alpha}{4 \pi^{3}}\left(\frac{13 \pi^{2}}{12}-12 \ln 2+\frac{1}{2}\right)=0.00479225 \ldots,\qquad(19)
$$

and it is revealing to compare these with recent numerical calculations. The estimate $\lambda_1(0) \approx 0.0092292$ by Sun $et$ $al.^{17}$ agrees perfectly with Eq. (18) but their estimate $\lambda_1(1) \approx$ 0.003125 is strikingly different from Eq. (19). How can this discrepancy be explained?

Following Gell-Mann and Brueckner $^{22}$ and Ueda, $^{31}$ Mi sawa argued $^{25}$ that the $\zeta=0$ and $\zeta=1$ limits of the RPA and exchange contributions to the correlation energy are related by

$$
E_{\mathrm{c}}^{a}\left(r_{s}, 1\right)=\frac{1}{2} E_{\mathrm{c}}^{a}\left(2^{-4 / 3} r_{s}, 0\right),\qquad(20)
$$

$$
E_{\mathrm{c}}^{b}\left(r_{s}, 1\right)=E_{\mathrm{c}}^{b}\left(2^{-4 / 3} r_{s}, 0\right),\qquad(21)
$$

and, from these relations, Perdew and Wang inferred $^{7}$

$$
\lambda_{1}^{a}(1)=2^{-7 / 3} \lambda_{1}^{a}(0),\qquad(22)
$$

$$
\lambda_{1}^{b}(1)=2^{-4 / 3} \lambda_{1}^{b}(0).\qquad(23)
$$

These are also obtained if the $\zeta \to 1$ limit of the integrands in Eqs. (8) and (9) is taken before integrating over $u$.

Numerical evaluations of Eq. (9) and analytical results from Eq. (17) confirm that Eq. (23) is correct. However, numerical

![](./images/811643855366520833_1.jpg)

FIG. 1. The five spin scalings as functions of $\zeta$.

<table>
<caption>TABLE II. Reduced correlation energy $-E_{\text{c}}(r_{s},1)$ for the ferromagnetic state of the UEG for various $r_{s}$.</caption>
<thead>
<tr>
<th>$r_{s}$</th>
<th>QMCª</th>
<th>DPIᵇ</th>
<th>Modified DPIᶜ</th>
</tr>
</thead>
<tbody>
<tr>
<td>2</td>
<td>0.0240(3)</td>
<td>0.0236</td>
<td>0.0238</td>
</tr>
<tr>
<td>5</td>
<td>0.0154(1)</td>
<td>0.0151</td>
<td>0.0152</td>
</tr>
<tr>
<td>10</td>
<td>0.0105(1)</td>
<td>0.0102</td>
<td>0.0103</td>
</tr>
<tr>
<td>20</td>
<td>0.006 78(2)</td>
<td>0.006 63</td>
<td>0.006 64</td>
</tr>
<tr>
<td>50</td>
<td>0.003 55(1)</td>
<td>0.003 50</td>
<td>0.003 50</td>
</tr>
<tr>
<td>100</td>
<td>0.002 073(3)</td>
<td>0.002 055</td>
<td>0.002 055</td>
</tr>
</tbody>
</table>
ªBenchmark QMC results taken from Ref. 8. The digits in parentheses represent the error bar in the last decimal place.
ᵇResults taken from Ref. 17 using the DPI (density-parameter interpolation) formula with $\lambda_{1}(1) = 0.003125$.
ᶜResults from the present work using the DPI formula with $\lambda_{1}(1) = 0.004792$.

evaluations of Eq. (8) and analytical results from Eq. (16) agree that Eq. (22) is wrong and that, in fact,
$$
\lambda_{1}^{a}(1)=2^{-7 / 3} \lambda_{1}^{a}(0) \times \frac{\pi^{2}+6}{\pi^{2}-6}.\qquad(24)
$$

The error in Eq. (22) arises from the noncommutivity of the $\zeta \to 1$ limit and the $u$ integration, which is due to the nonuniform convergence of $\mathcal{R}_{1}^{a}(u, \zeta)$.

To show this particular point, let us define
$$
\Delta \lambda_{1}^{a}(\zeta)=-\frac{3 \alpha}{8 \pi^{5}} \int_{-\infty}^{\infty} \Delta \mathcal{R}_{1}^{a}(u, \zeta) d u,\qquad(25)
$$

$$
\Delta \mathcal{R}_{1}^{a}(u, \zeta)=\frac{k_{\uparrow}^{2}}{k_{\downarrow}} R_{0}\left(\frac{u}{k_{\uparrow}}\right)^{2} R_{1}\left(\frac{u}{k_{\downarrow}}\right).\qquad(26)
$$

It can be easily shown that it is not possible to find a function $D(u)$, which is integrable with respect to $u$ and dominates $\Delta \mathcal{R}_{1}^{a}(u, \zeta)$, i.e., $\forall(u, \zeta),|\Delta \mathcal{R}_{1}^{a}(u, \zeta)| \leqslant D(u)$. Thus, according to the dominated convergence theorem, one cannot show that limit and integration can be interchanged, and
$$
\lim _{\zeta \rightarrow 1} \Delta \mathcal{R}_{1}^{a}(u, \zeta)=0, \quad \Delta \lambda_{1}^{a}(1)=0.\qquad(27)
$$

However, substituting $t=u / k_{\downarrow}$ in Eqs. (25) and (26), one immediately finds a function $D(t)$, which is integrable with respect to $t$ and dominates $\Delta \mathcal{R}_{1}^{a}(t, \zeta)$. This ensures the possibility of interchanging limit and integration. It yields
$$
\lim _{\zeta \rightarrow 1} \Delta \mathcal{R}_{1}^{a}(t, \zeta)=-\frac{2^{2 / 3} \pi}{3\left(1+t^{2}\right)^{2}},\qquad(28)
$$

$$
\begin{aligned}
\Delta \lambda_{1}^{a}(1) & =\frac{3 \alpha}{8 \pi^{5}} \int_{-\infty}^{\infty} \frac{2^{2 / 3} \pi}{3\left(1+t^{2}\right)^{2}} d t=2^{-1 / 3} \frac{\alpha}{8 \pi^{3}} \\
& =0.00166727,
\end{aligned}\qquad(29)
$$
which is exactly the difference between the two values of $\lambda_{1}^{a}(1)$.

The effect of the coefficient $\lambda_{1}(1)$ on the reduced correlation energy of the ferromagnetic state has been studied by varying its value in the DPI formula proposed by Sun et al. in Ref. 17. The results have been compared with the benchmark QMC calculations of Ceperley and Alder.⁸ As shown in Table II, the new value of $\lambda_{1}(1)$ derived in the present study systematically improves the accuracy of the DPI correlation energy, especially for small $r_{s}$.

In some cases,²⁷,³² it is of interest to resolve $\lambda_{1}(\zeta)$ into contributions due to $\uparrow \uparrow, \downarrow \downarrow$, and $\uparrow \downarrow$ electron pairs, such as
$$
\lambda_{1}^{i}(\zeta)=\lambda_{1}^{i, \uparrow \uparrow}(\zeta)+\lambda_{1}^{i, \downarrow \downarrow}(\zeta)+\lambda_{1}^{i, \uparrow \downarrow}(\zeta),\qquad(30)
$$

$$
\Lambda_{1}^{i, \sigma \sigma^{\prime}}(\zeta)=\frac{\lambda_{1}^{i, \sigma \sigma^{\prime}}(\zeta)}{\lambda_{1}^{i}(\zeta)},\qquad(31)
$$
where $i=a$ or $b$, and $\sigma \sigma^{\prime}=\uparrow \uparrow, \downarrow \downarrow$,or $\uparrow \downarrow$. Using (16) and (17), we find
$$
\Lambda_{1}^{a, \uparrow \uparrow}(\zeta)=\frac{1}{8} \frac{\pi^{2}+6}{\pi^{2}-6} \frac{(1+\zeta)^{2 / 3}}{\Lambda_{1}^{a}(\zeta)},\qquad(32)
$$

$$
\Lambda_{1}^{b, \uparrow \uparrow}(\zeta)=\frac{1}{4} \frac{(1+\zeta)^{2 / 3}}{\Lambda_{1}^{b}(\zeta)}.\qquad(33)
$$

The remaining contributions can be obtained using the relations
$$
\Lambda_{1}^{i, \downarrow \downarrow}(\zeta)=\Lambda_{1}^{i, \uparrow \uparrow}(-\zeta),\qquad(34)
$$

$$
\Lambda_{1}^{i, \uparrow \downarrow}(\zeta)=1-\Lambda_{1}^{i, \uparrow \uparrow}(\zeta)-\Lambda_{1}^{i, \downarrow \downarrow}(\zeta),\qquad(35)
$$
and are represented in Fig. 2.

In conclusion, we have found a closed-form expression for the coefficient $\lambda_{1}(\zeta)$ of the $r_{s} \ln r_{s}$ term in Eq. (1). It is valid for any value of $\zeta$ and, in particular, for the paramagnetic $(\zeta=0)$ and ferromagnetic $(\zeta=1)$ limits. This reveals that an earlier derivation of the ferromagnetic limit $\lambda_{1}(1)$ was incorrect because of an inadmissible interchange of a limit and an integral. The present result has no direct impact on the quantum phase diagram of the UEG, because the effect of the coefficient $\lambda_{1}(\zeta)$ is more pronounced in the high-density limit $(0<r_{s} \lesssim 2)$, where the paramagnetic fluid is significantly

![](./images/811643855366520833_2.jpg)

FIG. 2. Spin resolution of $\Lambda_{1}^{a, \sigma \sigma^{\prime}}(\zeta), \Lambda_{1}^{b, \sigma \sigma^{\prime}}(\zeta)$, and $\lambda_{1}^{\sigma \sigma^{\prime}}(\zeta)$ as functions of $\zeta$.

more stable than the ferromagnetic one. $^{8}$ Preliminary results on higher-order coefficients reveal that they behave similarly, and special care has to be taken in future studies. We believe that these new results will be useful in the future development of exchange-correlation functionals within DFT.

The authors thank an anonymous referee for providing help- ful comments leading to Eqs. (25)-(29). P.M.W.G. thanks the NCI National Facility for a generous grant of supercomputer time and the Australian Research Council (Grants DP0984806 and DP1094170) for funding.

*loos@rsc.anu.edu.au
†Corresponding author: peter.gill@anu.edu.au

$^{1}$R. G. Parr and W. Yang, *Density Functional Theory for Atoms and Molecules* (Oxford University Press, Oxford, UK, 1989).
$^{2}$P. Hohenberg and W. Kohn, *Phys. Rev.* **136**, B864 (1964).
$^{3}$G. F. Giuliani and G. Vignale, *Quantum Theory of Electron Liquid* (Cambridge University Press, Cambridge, UK, 2005).
$^{4}$W. Kohn and L. J. Sham, *Phys. Rev.* **140**, A1133 (1965).
$^{5}$S. H. Vosko, L. Wilk, and M. Nusair, *Can. J. Phys.* **58**, 1200 (1980).
$^{6}$J. P. Perdew, E. R. McMullen, and A. Zunger, *Phys. Rev. A* **23**, 2785 (1981).
$^{7}$J. P. Perdew and Y. Wang, *Phys. Rev. B* **45**, 13244 (1992).
$^{8}$D. M. Ceperley and B. J. Alder, *Phys. Rev. Lett.* **45**, 566 (1980).
$^{9}$P. Ballone, C. J. Umrigar, and P. Delaly, *Phys. Rev. B* **45**, 6293 (1992).
$^{10}$G. Ortiz and P. Ballone, *Phys. Rev. B* **50**, 1391 (1994).
$^{11}$G. Ortiz and P. Ballone, *Phys. Rev. B* **56**, 9970 (1997).
$^{12}$Y. Kwon, D. M. Ceperley, and R. M. Martin, *Phys. Rev. B* **58**, 6800 (1998).
$^{13}$G. Ortiz, M. Harris, and P. Ballone, *Phys. Rev. Lett.* **82**, 5317 (1999).
$^{14}$F. H. Zong, C. Lin, and D. M. Ceperley, *Phys. Rev. E* **66**, 036703 (2002).
$^{15}$S. Zhang and D. M. Ceperley, *Phys. Rev. Lett.* **100**, 236404 (2008).
$^{16}$E. Wigner, *Phys. Rev.* **46**, 1002 (1934).

$^{17}$J. Sun, J. P. Perdew, and M. Seidl, *Phys. Rev. B* **81**, 085123 (2010).
$^{18}$The approximate expression of the correlation energy in Ref. 17 is not an interpolation formula which uses QMC data, unlike the well-known $PZ^{6}$ and PW92$^{7}$ functionals. This interpolation formula uses the exact or near-exact coefficients of the high- and low-density limits embedded in a Padé-like approximant. The only QMC information used in Ref. 17 is the value of the correlation energy at the ferromagnetic transition, $^{8}$ which is required to build an approximate expression of the fourth-order coefficient ($r_{s}$ term).
$^{19}$V. W. Macke, *Z. Naturforsch.* **a5**, 192 (1950).
$^{20}$D. Bohm and D. Pines, *Phys. Rev.* **92**, 609 (1953).
$^{21}$D. Pines, *Phys. Rev.* **92**, 626 (1953).
$^{22}$M. Gell-Mann and K. A. Brueckner, *Phys. Rev.* **106**, 364 (1957).
$^{23}$D. F. DuBois, *Ann. Phys.* **7**, 174 (1959).
$^{24}$W. J. Carr and A. A. Maradudin, *Phys. Rev.* **133**, A371 (1964).
$^{25}$S. Misawa, *Phys. Rev.* **140**, A1645 (1965).
$^{26}$L. Onsager, L. Mittag, and M. J. Stephen, *Ann. Phys.* **18**, 71 (1966).
$^{27}$Y. Wang and J. P. Perdew, *Phys. Rev. B* **43**, 8911 (1991).
$^{28}$G. G. Hoffman, *Phys. Rev. B* **45**, 8730 (1992).
$^{29}$*NIST Handbook of Mathematical Functions*, edited by F. W. J. Olver, D. W. Lozier, R. F. Boisvert, and C. W. Clark (Cambridge University Press, New York, 2010).
$^{30}$Wolfram Research, Inc., *Mathematica* 7, (2008).
$^{31}$S. Ueda, *Prog. Theor. Phys.* **26**, 45 (1961).
$^{32}$P. Gori-Giorgi and J. P. Perdew, *Phys. Rev. B* **69**, 041103 (2004).