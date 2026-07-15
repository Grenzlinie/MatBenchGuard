# Model for modulated electronic configurations in selectively doped multilayered $La_2CuO_4$ nanostructures

V. M. Loktev $^{1}$ and Yu. G. Pogorelov $^{2}$

$^{1}$N. N. Bogolyubov Institute for Theoretical Physics, Metrologichna 14b, Kiev 03134, Ukraine
$^{2}$IFIMUP and IN/Institute of Nanoscience and Nanotechnology, Departamento de Física da Faculdade de Ciências da Universidade do Porto, R. Campo Alegre, 687, Porto 4169-007, Portugal

(Received 19 August 2008; published 5 November 2008)

A simple theoretical model is proposed to describe the recent experimental results on formation of induced superconducting state and anomalous tunneling characteristics in selectively doped multilayered nanostructures based on $La_2CuO_4$ perovskite. In particular, it is shown that the structure composed from the nominally nonsuperconducting (undoped and overdoped) layers turns to be superconducting with superconductivity confined to narrow regions near the interfaces, in agreement with the experimental observations.

DOI: 10.1103/PhysRevB.78.180501
PACS number(s): 74.78.Fk, 74.72.–h, 74.25.Jb, 74.45.+c

Recent experiments by Božović et al. $^{1}$ provided an intriguing insight on the electronic properties of nanostructured perovskite systems. Using thorough epitaxy techniques available in Brookhaven National Laboratory, $^{2–4}$ they were able to selectively introduce a well-controlled level (including zero) of Sr dopants into each particular $La_2CuO_4$ layer (along the $c$ axis) and then observed unusual electronic characteristics of the composite structures. For instance, a stack of 15 alternating $(La_{2−x}Sr_xCuO_4)_4(La_2CuO_4)_2$ blocks with $x=0.45$, which is alternating overdoped $^{5}$ and undoped (both separately nonsuperconducting) layers, revealed superconductivity with the critical temperature $T_c=30$ K. $^{1}$ The authors interpreted this behavior as an evidence for carrier delocalization beyond the nominally doped region of the multilayered system. Below we propose a very simple theoretical model permitting a qualitative and semiquantitative explanation of such delocalization effect.

The heuristic basis for the model is the assumption that the collective electronic states in the multilayered system are superpositions of almost uncoupled (because of a very slow $c$-axis hopping $t_c$) planar states in each $j$th $La_2CuO_4$ layer, formed by the fast $ab$-hopping $t_{ab} \gg t_c$ in the energy band of width $W=8t_{ab}$ around the relevant atomic level and shifted by a certain local electric potential $\varphi_j$. The latter is related to the local charge densities $\rho_j=e(p_j−x_j)$ by mobile holes with density $p_j$ and ionized dopants with density $x_j$ (where $e$ is the elementary charge), according to the discrete version of the common Poisson equation:

$$
\varphi_{j+1}+\varphi_{j-1}-2 \varphi_{j}=-\frac{4 \pi c}{\varepsilon_{\mathrm{eff}} a^{2}} \rho_{j}. \tag{1}
$$

Here $a$ and $c$ are the in-plane and $c$-axis lattice parameters and $\varepsilon_{\text{eff}}$ is the (static) dielectric constant that effectively reduces the Coulomb field in the $c$ direction. This equation would be exact for potentials in a stack of mathematical planes, with uniform charge densities $\rho_j$ and separation $c$, and should model real $La_{2−x}Sr_xCuO_4$ (LSCO) layers where $p_j$ delocalized holes and $x_j$ localized dopants are distributed in different atomic planes within the period $c$ of $j$th layer. The adopted form of purely dielectric screening is justified in neglect of $c$-hopping processes, according to their abovementioned weakness. We note that the charge densities $\rho_j$ naturally vanish both in uniformly doped $(p_j=x_j)$ and undoped $(p_j=x_j=0)$ systems.

Otherwise, the hole carrier density $p_j$ is defined by the respective density of states (DOS) $g_j(\varepsilon)$:

$$
p_{j}=2 \int_{\varepsilon_{F}}^{W / 2-e \varphi_{j}} g_{j}(\varepsilon) d \varepsilon, \tag{2}
$$

including the spin factor 2 (this zero-temperature formula is justified for all the considered temperatures $T \lesssim T_c$). Thus the role of $c$ hopping in this model is reduced to establishing the common Fermi level $\varepsilon_F$ for all the layers. Using the simplest approximation of rectangular DOS, $g_j(\varepsilon)=1/W$ within the bandwidth $W$, we arrive at the linear relation between $p_j$ and $\varphi_j$:

$$
e \varphi_{j}=\frac{1-p_{j}}{2} W-\varepsilon_{F}. \tag{3}
$$

Then inserting Eq. (3) into Eq. (1) leads to a nonuniform linear system for the densities $p_j$:

$$
p_{j+1}+p_{j-1}-(2+\alpha) p_{j}=-\alpha x_{j}, \tag{4}
$$

where the dimensionless value

$$
\alpha=\frac{8 \pi c e^{2}}{W \varepsilon_{\mathrm{eff}} a^{2}} \tag{5}
$$

is a single material parameter of the model, describing the localization degree of charge-density fluctuations in the nanostructured system (less delocalization for bigger $\alpha$). The advantage of Eq. (4) against an analogous system for potentials $\varphi_j$ is in eliminating the Fermi level (doping dependent) and, notably, this system assures the total electroneutrality condition $\sum_i \rho_j=0$. The present approach can be seen as a more detailed alternative to the phenomenological Thomas-Fermi treatment. $^{6}$

It is elementary to resolve Eq. (4) for the densities through the doping levels: $p_j=\sum_{j'} f_{jj'}(\alpha)x_{j'}$. The problem is reasonably simplified considering it periodic, then the period of $n$ layers at given $\alpha$ fully defines the coefficients $f_{jj'}(\alpha)$ for $1 \leq j,j' \leq n$. For the sake of definiteness, let us consider a

![](./images/811894386341183488_1.jpg)

FIG. 1. Schematic of nanostructured system with periodically introduced dopants (light gray circles) into consecutive layers of La₂CuO₄ along the c axis. There are only three independent values of electronic density over six layers in a period.

sample system such as that in the experiment, Ref. 1, with $n=6$ and $x_1$=$x_2$=$x_5$=$x_6$≡$x$, $x_3$=$x_4$=0 (Fig. 1). The explicit solution of Eq. (4) in this case reads as
$$
p_1 = p_6 = \left( 1 - \frac{1}{(\alpha+1)(\alpha+3)} \right) x,
$$
$$
p_2 = p_5 = \frac{\alpha+2}{\alpha+3} x,
$$
$$
p_3 = p_4 = \frac{\alpha+2}{(\alpha+1)(\alpha+3)} x, \tag{6}
$$
satisfying the evident electroneutrality condition $p_1$+$p_2$+$p_3$=2$x$.

Using the soft x-ray resonant scattering techniques⁴ for direct measurement of carrier densities in the experiment, Ref. 6 yielded $p_1^{\exp}$≈0.33, $p_2^{\exp}$≈0.24, $p_3^{\exp}$≈0.15. A reasonable fit to this set can be achieved from Eq. (6) with the choice of $\alpha$=1: $p_1^{\text{theor}}$≈0.315, $p_2^{\text{theor}}$≈0.27, $p_3^{\text{theor}}$≈0.135, which is within the experimental error of ±0.03 from the measured values.

In order to relate these carrier densities with the experimentally defined critical temperatures, we can employ the phenomenological bell-like dependence:
$$
T_{\text{ph}}(p) = (p_{\text{max}} - p)(p - p_{\text{min}})T^{*}, \tag{7}
$$
with $p_{\text{min}}$=0.07, $p_{\text{max}}$=0.2, and $T^{*}$=9000 K [this curve being slightly below the commonly reported $T_c(p)$ in bulk LSCO (Ref. 5)]. Using $p$=$p_3^{\text{theor}}$ in Eq. (7) yields the value of $T_c$≈38 K, just like that observed in Ref. 6. This confirms the conclusion that the superconducting (SC) state in this system is limited to the nominally undoped layers 3 and 4 as represented schematically in Fig. 2.

One can compare the fitted value of $\alpha$=1 with the theoretical expression, Eq. (5), using the standard values $a$≈0.38 nm, $c$=1.3 nm, and $W$≈2 eV. This suggests a high value of $\varepsilon_{\text{eff}}$ as ~150, however, it does not seem unrealistic if the static $c$-axis polarizability for La₂CuO₄ (Refs. 7 and 8) is enhanced by a contribution from doped mobile carriers.

The situation can be further traced at varying the doping level $x$ (with $\alpha$ supposedly constant). Thus, for $x$=0.45 we obtain respectively: $p_1^{\text{theor}}$≈0.395, $p_2^{\text{theor}}$≈0.34, $p_3^{\text{theor}}$≈0.165, and then using this $p_3^{\text{theor}}$ in Eq. (7) results in $T_c$≈30 K, again in agreement with the measured value.¹

![](./images/811894386341183488_2.jpg)

FIG. 2. Modulated electronic configuration by the shifted energy bands (solid rectangles) in the nanostructured system by Fig. 1, calculated for $x$=0.45 and localization parameter $\alpha$=1. The dashed rectangles indicate the initial energy bands for isolated doped and undoped layers, and the hatched stripe marks the interval of carrier densities where superconductivity should exist.

At least, for the nominally optimum doping level $x$=0.15, we have $p_1$=0.132, $p_2$=0.113, and $p_3$=0.055, and the SC state with almost maximum $T_c$ should persist only in the doped 1, 2, 5, and 6 layers separated by the insulating 3 and 4 layers. This agrees with the observation of blocked tunneling through the undoped La₂CuO₄ layer sandwiched between optimally doped La₂₋ₓSrₓCuO₄ electrodes.¹

Furthermore, combining the results, Eq. (6), and the phenomenological dependence, Eq. (7), one can easily build a model dependence for critical temperature of SC transition in the given La₂₋ₓSrₓCuO₄-La₂CuO₄ system vs the doping level $x$. As seen from Fig. 3, this dependence chosen as the maximum value from three bell-like curves, $T_c(p)$=$\max_j$ $T_{\text{ph}}[p_j(x)]$, has generally a nonmonotonous behavior with the broadest region contributed by the 3 and 4 layers. It should be noted that the SC state realized in this region may be of special interest since much longer lifetimes of charge carriers in the nominally undoped layers, in similarity with the well explored physics of two-dimensional electron gas (2DEG) inverse layers in semiconducting heterojunctions.⁹

![](./images/811894386341183488_3.jpg)

FIG. 3. Critical temperature $T_c$ vs doping level $x$ (solid line) for the (La₂₋ₓSrₓCuO₄)₄(La₂CuO₄)₂ system as the maximum among three curves related by the respective numbers to the layers in Fig. 2. The arrows indicate the particular doping levels of 0.15, 0.36, and 0.45 as in the experimental systems (Refs. 1 and 6).

MODEL FOR MODULATED ELECTRONIC CONFIGURATIONS...
PHYSICAL REVIEW B 78, 180501(R) (2008)

This can be an important property for envisaged superconducting devices in nanotailored heterosystems¹⁰ or excitonic superconductors.¹¹

The model, Eqs. (1)-(5), can be easily extended to other characteristic nanostructures. Thus, inclusion into an infinite stack of layers with some uniform doping level $x$ of a single layer with different level $x+\Delta x$ will produce a symmetric distribution of carrier densities $p_j=p_{-j}$ that obviously tend to the asymptotic value: $p_{j\to\infty}\to x$. Then, considering the reduced densities $\delta_j=p_j-x$, we obtain from Eq. (4) an infinite set of linear equations:
$$(2+\alpha)\delta_0-2\delta_1=\alpha\Delta x,$$

$$(2+\alpha)\delta_j=\delta_{j+1}+\delta_{j-1},\quad j\geq1,\tag{8}$$
with the electroneutrality condition $\delta_0+2\sum_{j\geq1}\delta_j=\Delta x$. It can be easily checked that the system, Eq. (8), is solved with $\delta_j=\delta_0\exp(-\kappa j)$ where $\kappa=\text{arccosh}(1+\alpha/2)$ and with the most interesting central value given by $\delta_0=\Delta x\tanh\kappa/2=\Delta x\sqrt{\alpha/(\alpha+4)}$. From this function, it follows that the greatest part of added charge density remains at the central layer, $\delta_0>\Delta x/2$, when the localization parameter $\alpha$ surpasses $4/3$. Though being somewhat higher of that used in the previous analysis of periodically doped system, such value can be supposed to describe a stronger localization for the single layer doping. Then it can support the experimental observation of persisting SC state in a single optimally doped layer sandwiched between undoped semispaces $(x=0,\ \Delta x=x_{\text{opt}}),^{12}$ if $p_0$ falls within the range $[p_{\text{min}},p_{\text{max}}]$ (Fig. 4). Contrariwise, a single undoped layer $(x_0=0)$ between optimally doped semispaces $(x=x_{\text{opt}}=-\Delta x)$ should possess a lower local density $p_0=x_{\text{opt}}-\delta_0$, which more probably goes out of $[p_{\text{min}},p_{\text{max}}]$ so that this layer would pertain insulating.

Another exemplary case is the interface between two semi-infinite stacks of layers with different uniform doping levels $x_j=x$ at $j\leq-1$ and $x_j=x-\Delta x$ at $j\geq1$, where the reduced densities can be defined, respectively, as $\delta_j=x_1-p_j$ at $j\leq-1$ and $\delta_j=p_j-x_2$ at $j\geq1$ with evident symmetry $\delta_j=\delta_{-j}$. Then Eq. (8) is reformulated as
$$(3+\alpha)\delta_1-\delta_2=\Delta x=x_1-x_2,$$

![](./images/811894386341183488_4.jpg)

FIG. 4. Modulated electronic configurations for (a) single doped layer between undoped semispaces and (b) interface between two semispaces with different doping levels.

$$(2+\alpha)\delta_j=\delta_{j+1}+\delta_{j-1},\quad j\geq2,\tag{9}$$
and its solution is $\delta_j=\delta_1\exp[(1-j)\kappa]$ with the same $\kappa$ as above and with $\delta_1=\Delta x/[2-\alpha/2+\sqrt{\alpha(\alpha+4)}]$.

At least, combining the previous cases can serve to explain the "giant proximity effect" observed in a thick underdoped layer sandwiched between optimally doped electrodes.¹³

In conclusion, a simple electrostatic model combined with 2D electronic band spectrum is used to semiquantitatively explain the recent experimental findings in $\text{La}_{2-x}\text{Sr}_x\text{CuO}_4$ multilayered systems, selectively doped with precision to single atomic layer. Exact solutions are found for local charge densities $p$ in conducting $\text{CuO}_2$ planes, for a number of periodic and nonperiodic doping configurations, permitting agreement with the experimentally defined $p$'s and SC transition critical temperature $T_c$. The model can be used for effective designing of SC (including Josephson tunnel) systems; otherwise, it can be also applied to the description of charge and spin accumulation in the multilayered devices of modern spintronics.¹⁴

V.M.L. acknowledges the support from Natl. Acad. of Sci. of Ukraine under the Special Program for Fundamental Research of the Division of Physics and Astronomy.

---

¹I. Božović, Phys. Usp. 51, 170 (2008).
²I. Bozovic, J. N. Eckstein, and G. F. Virshup, Physica C 235-240, 178 (1994).
³I. Bozovic, IEEE Trans. Appl. Supercond. 11, 2686 (2001).
⁴A. Gozar, G. Logvenov, V. Y. Butko, and I. Bozovic, Phys. Rev. B 75, 201402(R) (2007).
⁵M. A. Kastner, R. J. Birgeneau, G. Shirane, and Y. Endoh, Rev. Mod. Phys. 70, 897 (1998).
⁶S. Smadici, J. C. T. Lee, S. Wang, P. Abbamonte, A. Gozar, G. Logvenov, C. D. Cavellin, and I. Bozovic, arXiv:0805.3189 (unpublished).
⁷C. Y. Chen, N. W. Preyer, P. J. Picone, M. A. Kastner, H. P. Jenssen, D. R. Gabbe, A. Cassanho, and R. J. Birgeneau, Phys. Rev. Lett. 63, 2307 (1989).
⁸D. Reagor, E. Ahrens, S.-W. Cheong, A. Migliori, and Z. Fisk, Phys. Rev. Lett. 62, 2048 (1989).
⁹C. Weisbuch and B. Vinter, *Quantum Semiconductor Structures: Fundamentals and Applications* (Academic, London, 1991).
¹⁰C. B. Eom, R. J. Cava, J. M. Phillips, and D. J. Werder, J. Appl. Phys. 77, 5449 (1995).
¹¹V. L. Ginzburg, Phys. Lett. 13, 101 (1964).
¹²I. Bozovic, G. Logvenov, M. A. J. Verhoeven, P. Caputo, E. Goldobin, and T. H. Geballe, Nature (London) 422, 873 (2003).
¹³I. Bozovic, G. Logvenov, M. A. J. Verhoeven, P. Caputo, E. Goldobin, and M. R. Beasley, Phys. Rev. Lett. 93, 157002 (2004).
¹⁴T. Valet and A. Fert, Phys. Rev. B 48, 7099 (1993).

180501-3