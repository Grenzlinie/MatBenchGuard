**PHYSICAL REVIEW E 100, 061301(R) (2019)**

Rapid Communications | Editors' Suggestion

# From early nucleation past the percolation threshold: Status of the Kolmogorov-Avrami theory on a cold Ising lattice

Vitaly A. Shneidman
Department of Physics, New Jersey Institute of Technology, Newark, New Jersey 07102, USA

![](./images/812704374693298176_1.jpg)
(Received 1 July 2019; published 6 December 2019)

A high-precision test of the Kolmogorov-Avrami (KA) model of "geometric" interactions between growing nuclei is performed for an Ising ferromagnet driven by Metropolis dynamics. As long as the interface boundaries of interacting nuclei are rough, the KA model is adequate for arbitrary large densities of the new phase, well beyond the percolation transition, as in the case of homogeneous nucleation. For a prenucleated system the KA description breaks down at sufficiently low temperature, when the length of a kinetically smooth interface exceeds the distance between seeds.

DOI: 10.1103/PhysRevE.100.061301

About 80 years ago, Kolmogorov, Johnson, Mehl, and Avrami [1] (KA for brevity) proposed a theory of crystallization kinetics in a strongly undercooled melt. The remarkable feature of the theory is that it is not restricted to small volume fractions $X$ occupied by the new phase and at least formally is valid even when interactions between growing nuclei become dominant, i.e., for any $X < 1$. Not surprisingly, the KA formalism found an enormous amount of applications, not only in the crystallization of melts [2,3], but also for polymers [4], electrodeposition [5], DNA replication [6], to mention just a few. Similarly, the KA approach became a valuable tool to analyze large-scale simulations for phase field models [7], Lennard-Jones systems [8], or the dynamic Ising-type models, introduced later below.

At the heart of KA model lies the idea of "geometric interaction." If two or more nuclei happen to be close to each other, they nevertheless are assumed to be growing independently, even if this leads to their overlap. One then has the famous KA relation expressing the transformed volume [area in the two-dimensional (2D) case] $X$ in terms of the "extended volume" $X_{\text{ext}}$ which would be occupied by nuclei in neglect of overlap,

$$
X(t) = 1 - \exp\left\{-X_{\text{ext}}(t)\right\}. \tag{1}
$$

With the assumption that the nucleation and growth of independent nuclei are described adequately, so that the above equation is accurate when the volume fraction is small, one is faced with the dilemma whether to accept Eq. (1) for $X_{\text{ext}} \gtrsim 1$. The most stringent test could come from volume fractions which are large enough to allow a percolation transition, when the new phase is no longer an independent collection of nuclei. The geometric interaction model can appear counterintuitive due to inevitable *physical* interactions between nuclei. Yet, due to the outstanding success of the KA approach in experimental applications, there must exist situations where the model is justified (and other situations where the model breaks down).

The Ising system of interacting spins was the first "microscopic" model to challenge the intuitive descriptions and classifications of phase transformations due its exact solvability in equilibrium for square [9] and triangular or hexagonal [10] lattices. Out of equilibrium and with added spin-flip dynamics the model cannot be described exactly, but low-temperature analytical approaches and efficient Monte Carlo (MC) methods are available for both nucleation [11-14] and growth [15-17]. Yet, even for the Ising model there is no clarity with respect to the validity of the KA description. Due to limited computational power, early first-principles studies on triangular and square Ising lattices [18,19] were mostly restricted to assessments of the KA approach at intermediate and high temperatures where it is hard to follow the interactions of individual nuclei due to fluctuations caused by weak interfacial tension. The traditional KA assumptions of time- and size-independent nucleation and growth rates (which require a strong separation of scales, unavailable in most simulations) were used sometimes, which blurred the validity of the geometric interaction *per se*. At high temperatures $T = 0.8T_c$, the critical temperature, conclusions were made that "the [KA] theory breaks down for late times, when the remaining metastable volume fraction becomes less than one half" [19], which, if confirmed at lower $T$, would imply a serious limitation of the entire approach. The intent of this Rapid Communication is thus to clarify the status of the KA model by analyzing direct collisions between nuclei at low temperatures and testing the implications for large transformed areas during nucleation and growth, including areas beyond the percolation threshold. No strong *a priori* assumptions regarding the structure of nucleation and growth rates will be made, but rather those rates will be approximated based on independent MC simulations (or, when available [14], based on symbolic analytical data). The approximations, which make the adjusted KA theory accurate for small area fractions, will be further used to evaluate large $X_{\text{ext}}$, allowing one to specifically address the validity of Eq. (1). We discuss both the homogeneous nucleation where the KA approach appears appropriate at small $T$ without restrictions, and the prenucleated system where it can break down in a spectacular explosive fashion for a sufficiently large density of seeds.

Consider a ferromagnetic 2D square lattice with neighboring spins interacting with energies $\pm 1$, while each spin also interacts with an external field $h$ with energies $\pm h$. If $h = 0$,

2470-0045/2019/100(6)/061301(5)
061301-1
©2019 American Physical Society

![](./images/812704374693298176_2.jpg)

FIG. 1. Coalescence of growing squares with rough (upper insets, $T=0.8$) and smooth (lower insets, $T=0.4$) interfaces. In each case the arrows indicate the instant the corresponding snapshot was taken; $n$ is the total number of up spins and the scaled time is $t/\exp[(2-h)/T]$. The higher $T$ case is consistent with the KA model, while the lower $T$ case is not (see text).

there is a critical temperature $T_c \simeq 2.26$, and we are going to discuss temperatures which are much lower. The system is originally prepared in a metastable state with all spins pointing in one direction ("down") while the field $h$ favors the "up" direction. Both cases of $h<2$ and $2<h<4$ corresponding, respectively, to a stable and unstable interface of a single nucleus [15,17] will be discussed. For $h<2$, a nucleus—a compact group of $n$ up spins—is close in shape to an $m \times m$ square, which will serve as a definition of the side $m$ if the square is not ideal or, in the case $h>2$, when the nucleus is close to circular with radius $m/\sqrt{\pi}$. For a large $m$ the growth rate of a nucleus $\dot{m}$ is expected to be $m$ independent, as in the original KA theory. The anisotropy of growth reflects the structure of the lattice and is not an issue as long as it is identical for all nuclei [20]. One then has $X_{\text{ext}}=\frac{1}{3}J_{st}\dot{m}^2t^3$ for homogeneous nucleation, $J_{st}$ being the steady state nucleation rate (per spin). More generally, the extended area fraction occupied by the squares with sides $m(t)$ is given by

$$
X_{\text{ext}}(t)=\int_{0}^{t}dt'J(t')m^2(t-t'), \tag{2}
$$

where the time dependence of the nucleation rate can be due to internal transient effects or due to external control.

Thus, detailed studies of nucleation and growth of noninteracting nuclei allow an accurate prediction of the extended area. The observed dependences $J(t)$ and $m(t)$ may or may not correspond to those traditionally assumed in conjunction with the KA model, but this does not support or disprove the model itself. To assess the key feature of the KA model, namely, the validity of geometric interaction picture, we first consider "collisions" of two growing nuclei, as in Fig. 1 (computational details will be described below later). The inner corner points appearing due to an overlap stimulate the flipping of neighboring spins and two extreme scenarios can be identified. In the first scenario, approximately corresponding to the higher-temperature case in the figure, the overall rate of adding spins elsewhere on the interface is much larger than at the corners. Here, in compliance with the KA model, the squares grow over each other without significant changes of individual growth rates. At lower temperatures, on the other hand, the interface is kinetically smooth and the corners are the only places where new spins are added. Once coming in contact with each other, almost immediately the two squares will transform into a single larger square (or rectangle), in effect implying a strong direct interaction which is beyond the KA assumption.

Crossover is expected for squares with side $m$ about $m_c \sim \exp[(4-2h)/T]$. Larger squares have more than one kink (are "rough") and grow at a rate $\dot{m} \sim m_c^{-1/2}$ [17]. In order to validate the KA model one needs $m_c \ll \bar{l}$, the average distance between nuclei. For 2D homogeneous nucleation the latter can be estimated as $(Jt)^{-1/2}$, where $t$ is the characteristic nucleation time with $J\dot{m}^2t^3 \sim 1$, so that $\bar{l} \sim (J/\dot{m})^{-1/3}$. For the Metropolis driven Ising model on a square lattice at $T \to 0$, the exponential asymptote $J \sim \exp\{-(8-2h+2(4-h)[\frac{2}{h}]-2h[\frac{2}{h}]^2)/T\}$, with $[x]$ denoting the integer part, the "floor" of $x$, follows from Ref. [11] (and Ref. [13] also has the preexponential). One can see that the ratio $\bar{l}/m_c$ is large for any field, diverging at least as fast as $\exp(1/T)$, so that there are no low-temperature restrictions on the applicability of the KA interaction model. While initially the nucleated clusters can grow as kinetically smooth, they are so sparse that they do not interact with each other, and when they grow enough to start overlapping they are already rough. On the other hand, a prenucleated system can have an arbitrary value of the above ratio and if the input density of seeds $\rho_{\text{seed}} \sim 1/\bar{l}^2$ is sufficiently large to ensure $\bar{l} \ll m_c$, after initial independent growth the population of the interacting cluster will evolve in a self-accelerating fashion, much faster than in the KA expectation.

To verify and illustrate the above conclusions a $1000 \times 1000$ system of spins was considered with MC simulations carried out with *Mathematica 11* and *12*. In homogeneous nucleation studies all spins were originally oriented "down," against the up-field $h$ and magnetization $M(t)=2X(t)-1$ was typically followed until $M(t) \geqslant 0.99$. The time $t$ was identified with the number of updates of the full lattice. Percolation was associated with the instant the largest cluster spanned the lattice in either direction. When studying the growth and interactions of individual nuclei, as in Fig. 1, $m_0 \times m_0$ squares on smaller lattices were originally created. Then, truncated Metropolis dynamics which forbids the flip of a spin which is surrounded by four down spins (thus preventing homogeneous nucleation) was applied [21]. Due to a significant stochastic contribution to growth during the initial "smooth" stage, there was an appreciable scatter of data for $m(t)$. In each case several runs were performed and a two-parametric nonlinear fit was obtained, to be further used when finding the extended area fraction $X$ for the KA model. Specifically, the growth times were approximated as $t=a(m-m_0)+b\ln\{(m-1)/(m_0-1)\}$ so that

$$
m(t)=1+\frac{b}{a}W\left[\frac{a(m_0-1)}{b}\exp\left(\frac{1}{b}[t+a(m_0-1)]\right)\right], \tag{3}
$$

where $W[z]$ is the Lambert $W$ function and parameters $a$, $b$ are listed in Table I. The value of $m_0=5$ was fixed by initial conditions for most simulations.

Within the KA model contributions to $X_{\text{ext}}$ of homogeneous nucleation and of growing preexisting nuclei can be

<table>
<caption>Table I. Parameters used to approximate nucleation and growth for the temperatures, fields, and densities of seeds considered. $m_c$ is the estimated crossover length to a kinetically rough interface. $X_{\text{perc}}$ are the observed percolation densities.</caption>
<thead>
<tr>
<th>$T$</th>
<th>$h$</th>
<th>$\rho_{\text{seed}}$</th>
<th>$a$</th>
<th>$b$</th>
<th>$J_{st} \times 10^6$</th>
<th>$t_0$</th>
<th>$m_c$</th>
<th>$X_{\text{perc}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.8</td>
<td>0.88</td>
<td>0</td>
<td>1.957</td>
<td>10.75</td>
<td>1.75</td>
<td>19.96</td>
<td>16</td>
<td>$0.61 \pm 0.05$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$10^{-4}$</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>$0.64 \pm 0.03$</td>
</tr>
<tr>
<td>0.25</td>
<td>2.5</td>
<td>0</td>
<td>0.272</td>
<td>1.035</td>
<td>4.78</td>
<td>0</td>
<td>$<1$</td>
<td>$0.62 \pm 0.05$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$1.1 \times 10^{-3}$</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>$0.55 \pm 0.03$</td>
</tr>
<tr>
<td>0.4</td>
<td>0.6</td>
<td>$1.1 \times 10^{-3}$</td>
<td>0</td>
<td>693.5</td>
<td>$\lesssim 10^{-12}$</td>
<td></td>
<td>$10^3$</td>
<td>$0.67 \pm 0.06$</td>
</tr>
</tbody>
</table>

considered independently. The transient rate of homogeneous nucleation in the conventional Becker-Döring approach is given by [22] $J(t) = J_{st} \exp\left\{-\exp\left[(t_0 - t)/\tau - \gamma\right]\right\}$, where $t_0$ is the induction time (or time lag) which depends on the size $m_0$ at which the rate is evaluated, while $\tau$ is a size-independent relaxation time and $\gamma = 0.5772\ldots$ is the Euler constant. A similar transient shape also provides an accurate approximation in the case of the Ising ferromagnet [14]. The situation is further simplified for $t_0 \gg \tau$ when the double exponential is reduced to a theta function, $J(t) \approx J_{st} \Theta(t - t_0)$, and one can write the total extended area fraction as

$$
X_{\text{ext}}(t) \approx J_{st} \Theta(t - t_0) \int_0^{t - t_0} dt' m^2(t') + \rho_{\text{seed}} m^2(t). \tag{4}
$$

The somewhat cumbersome integration can be performed in terms of the same Lambert $W$ function as in Eq. (3). The above equation extends those traditionally used in conjunction with the KA model towards size-dependent growth rates and transient nucleation effects (see also Ref. [23]). This is especially important for computational systems where it is harder to achieve a distinct separation of scales. Regardless of the approximations employed, we expect that the initial stage of the phase transformation with $X_{\text{ext}}(t) \ll 1$ and $X(t) \approx X_{\text{ext}}(t)$ is described accurately. The core of the KA model, Eq. (1) with $X_{\text{ext}} \gtrsim 1$, can then be verified.

In Fig. 2 homogeneous nucleation is considered for stable (left) and for unstable (right) interfaces of growing nuclei. The shapes of the nuclei are close to squares and circles, respectively. Strictly speaking, for the unstable interface a minor anisotropy (deviations from a circle) is expected from the nonequilibrium Wulff construction [15] but this should have no effect on the applicability of the KA theory—see the remark [20]. In the stable case the interface is smooth for the smaller nuclei but roughens when they become large enough to interact with each other; in the unstable case the interface is rough from the start. In both situations the KA model adjusted for time- and size-dependent nucleation and growth and given by Eqs. (1) and (4) with $\rho_{\text{seed}} = 0$ appears valid for the entire transformation. In particular, the magnetization $M(t)$ can extend well above the percolation threshold with $M_{\text{perc}} = 2X_{\text{perc}} - 1 \sim 0.1$–0.35 (see Table I).

![](./images/812704374693298176_3.jpg)

FIG. 2. Homogeneous nucleation at $T = 0.8$, $h = 0.88$ (left, nonscaled time $t$) and $T = 0.25$, $h = 2.5$ (right, time scaled as in Fig. 1). In each case the insets show snapshots of a fraction ($500 \times 500$) of the lattice when time and scaled time are close to 150. In both cases the KA model (lines) is in good agreement with MC data (symbols), including magnetizations beyond the percolation threshold—see text.

The case of a prenucleated system is presented in Fig. 3. For the smaller field $h = 0.88$ preexisting nuclei (“seeds”) were randomly placed with a low density so that when the size of a nucleus becomes comparable with the average distance $\bar{l} \sim 1/\sqrt{\rho_{\text{seed}}} \gg m_c$ (see Table I), its interface is already rough; for a larger field $h = 2.5$ the interface becomes rough almost immediately. According to the above analysis, for such situations the KA model should be adequate, which is confirmed by the figure.

Conversely, in the case of Fig. 4, seeds were created at smaller temperature and field, with a much larger $m_c$ so that the interfaces of an interacting nuclei are expected to remain kinetically smooth, resulting in a strong deviation from the KA regime. To quantify this deviation a single-parameter fit to growth data was used—Eq. (3) with $a = 0$—reflecting the near-exponential growth of a smooth square [17]. In the full multiseed study, an additional run with larger seeds ($m_0 = 11$, the same $\rho_{\text{seed}}$) was performed. The shift in time which was required to match the observed data for the transformed area $X(t)$ with those obtained with $m_0 = 5$ was used for a more accurate determination of the growth parameter $b$ (which could not be reliably determined from individual growth studies at a single $m_0$ due to a significant stochastic component).

![](./images/812704374693298176_4.jpg)

FIG. 3. Same as in Fig. 2 but for prenucleated systems (all times are scaled as in Fig. 1). The KA model (lines) is in good agreement with MC data for both stable (left) and unstable (right) interfaces of growing nuclei.

![](./images/812704374693298176_5.jpg)

FIG. 4. Breakdown of the KA model at small $T$ and $h$ and high seed density. Symbols: MC data for initial seed size $m_0=5$ (circles) and $m_0=11$ (squares, time shifted to match the $m_0=5$ data-see text). Inset: Snapshot of the full lattice ($1000\times1000$) at $t=1000$, shortly before percolation. The KA prediction (line) based on Eq. (1) underestimates the rate of transformation due to the neglect of direct interactions between nuclei which lead to an avalanchelike completion of the phase transformation.

Unlike the situations described in the earlier figures, there is a noticeable scatter in the transformed volume fractions $X(t)$ indicated by the spread of data for individual runs (circles) in Fig. 4. This results from instabilities leading to the formation of a small number of large "aggressive" squares and rectangles which dominate the statistics. The reason for their formation is the following.

In the non-KA regime, two nuclei which get into contact immediately form a larger rectangular island which envelopes both. In turn, the new island has a bigger chance to contact the neighboring one, etc., leading to an avalanchelike transformation. The presence of such anomalously large islands is seen in the inset of Fig. 4. Since those islands mostly grow by scavenging smaller clusters, they are typically separated from each other. The latter is in contrast with the KA case when the largest clusters acquire a more complicated fractal-looking shape once percolation is approached, with a lower value of the observed percolation area $X_{\text{perc}}$ as in Table I.

Even though nucleation and growth take place on a lattice, by the time interactions become important a typical nucleus can contain thousands of spins, so that the percolation problem can be treated as continuous. A few available rigorous estimations of the percolation density $X_{\text{perc}}$ could be relevant in the standard KA approach. For example, $X_{\text{perc}}=0.686\ldots$ for a uniform distribution of disks [24], approximately as for homogeneous nucleation for $h>2$, though the fractal interface increases the effective radius of a nucleus, thus reducing the density. Or, $X_{\text{perc}}=0.666\ldots$ for aligned squares of delta-distributed size [25,26], as in the case of nucleation starting from identical seeds if one neglects the stochastic component of subsequent growth. A reasonably close range of values for $X_{\text{perc}}$ is observed in Table I although there are strong fluctuations between runs and statistics is very limited. Nevertheless, one can certainly conclude that when justified, the KA approach works well above the aforementioned range, practically for the entire phase transformation. On the other hand, in situations when the interfaces of interacting nuclei are kinetically smooth, the KA description breaks down at relatively small transformed areas, below the percolation threshold. The problem requires further analysis in 3D with a thermodynamic transition to a smooth interface at sufficiently low $T$. With respect to 2D nucleation at elevated temperatures, strong fluctuations of the interface-as in Fig. 1 of Ref. [19]-do not appear to comply with the KA geometric interaction of nuclei, which supports the general conclusions of that paper. More studies, however, could be required due to a somewhat different (Glauber) dynamics considered.

In summary, verification of the Kolmogorov-Avrami (KA) model of geometric interaction generally requires kinetic adjustments of the approach for time- and size-dependent nucleation and growth. After that, the KA approach has no low-temperature restrictions for homogeneous nucleation since interacting nuclei are typically large enough to have a rough interface. Remarkably, the approach works accurately not only for small transformed area fractions but also for later stages of a phase transformation, including the percolation transition and beyond. Similarly, the adjusted KA description is accurate for a prenucleated system if the density of seeds is sufficiently small to ensure rough interfaces of interacting nuclei. Otherwise, if the typical interface is kinetically smooth, the KA model breaks down and the phase transformation proceeds in an avalanchelike explosive fashion.

[1] A. N. Kolmogorov, Bull. Acad. Sci. USSR (Sci. Mater. Nat.) 3, 3551 (1937); W. A. Johnson and R. F. Mehl, Trans. AIME 135, 416 (1939); M. Avrami, J. Chem. Phys. 7, 1103 (1939); 8, 212 (1940); 9, 177 (1941).

[2] J. W. Christian, The Theory of Transformations in Metals and Alloys (Pergamon, Oxford, UK, 2002).

[3] R. W. Balluffi, S. M. Allen, and W. C. Carter, Kinetics of Materials (Wiley, Hoboken, NJ, 2005).

[4] R.-Y. Wang, S.-F. Zou, B.-Y. Jiang, B. Fan, M.-F. Hou, B. Zuo, X.-P. Wang, J.-T. Xu, and Z.-Q. Fan, Cryst. Growth Des. 17, 5908 (2017).

[5] S. Frank and P. A. Rikvold, Surf. Sci. 600, 2470 (2006).

[6] S. Jun and J. Bechhoefer, Phys. Rev. E 71, 011909 (2005).

[7] L. Gránásy, G. I. Tóth, J. A. Warren, F. Podmaniczky, G. Tegze, L. Rátkai, and T. Pusztai, Prog. Mater. Sci. 106, 100569 (2019).

[8] M. Li, Y. Liu, and R. Bansil, J. Chem. Phys. 133, 084905 (2010).

[9] L. Onsager, Phys. Rev. 65, 117 (1944).

[10] G. H. Wannier, Phys. Rev. 79, 357 (1950).

[11] E. J. Neves and R. H. Schonmann, Commun. Math. Phys. 137, 209 (1991).

[12] M. A. Novotny, in Computer Simulation Studies in Condensed-Matter Physics IX, edited by D. P. Landau, K. K. Mon, and H.-B. Schüttler, Springer Proceedings in Physics Vol. 82 (Springer, Berlin, 1997), p. 182; D. P. Landau, S. P. Lewis, and

H.-B. Schüttler, *Computer Simulation Studies in Condensed-
Matter Physics XV*, Springer Proceedings in Physics Vol. 90
(Springer, Berlin, 2003), p. 7.

[13] V. A. Shneidman, *J. Stat. Phys.* **112**, 293 (2003).

[14] V. A. Shneidman and G. M. Nita, *Phys. Rev. Lett.* **97**, 065703 (2006).

[15] P. Devillard and H. Spohn, *Europhys. Lett.* **17**, 113 (1992).

[16] P. A. Rikvold and M. Kolesik, *J. Stat. Phys.* **100**, 377 (2000).

[17] V. A. Shneidman, K. A. Jackson, and K. M. Beatty, *J. Cryst. Growth* **212**, 564 (2000).

[18] V. A. Shneidman, K. A. Jackson, and K. M. Beatty, *Phys. Rev. B* **59**, 3579 (1999); *J. Chem. Phys.* **111**, 6932 (1999).

[19] R. A. Ramos, P. A. Rikvold, and M. A. Novotny, *Phys. Rev. B* **59**, 9053 (1999).

[20] This type of anisotropy was already discussed by Kolmogorov [1]; for anisotropic growth of nonaligned nuclei, see, e.g., B. J. Kooi, *Phys. Rev. B* **73**, 054103 (2006), and references therein.

[21] In the spirit of the KA model, the "bare" growth rate $\dot{m}$, unaltered by scavenging of freshly nucleated clusters, is assumed when calculating $X_{\text{ext}}$.

[22] V. A. Shneidman, *Sov. Phys. - Tech. Phys.* **32**, 76 (1987); **33**, 1338 (1988).

[23] V. A. Shneidman and M. C. Weinberg, *J. Non-Cryst. Solids* **160**, 89 (1993).

[24] J. Quintanilla, *Phys. Rev. E* **63**, 061108 (2001).

[25] D. R. Baker, G. Paul, S. Sreenivasan, and H. E. Stanley, *Phys. Rev. E* **66**, 046136 (2002).

[26] S. Mertens and C. Moore, *Phys. Rev. E* **86**, 061109 (2012).