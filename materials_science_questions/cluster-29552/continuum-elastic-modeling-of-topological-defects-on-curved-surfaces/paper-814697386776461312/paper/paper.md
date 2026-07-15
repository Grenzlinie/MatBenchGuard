# Specific Heat in Two-Dimensional Melting
Sven Deutschländer, $^{1}$ Antonio M. Puertas, $^{2}$ Georg Maret, $^{1}$ and Peter Keim $^{1}$
$^{1}$ Physics Department, University of Konstanz, 78464 Konstanz, Germany
$^{2}$ Department of Applied Physics, University of Almeria, 04120 Almeria, Spain
(Received 19 December 2013; published 18 September 2014)

We report the specific heat $c_N$ around the melting transition(s) of micrometer-sized superparamagnetic particles confined in two dimensions, calculated from fluctuations of positions and internal energy, and corresponding Monte Carlo simulations. Since colloidal systems provide single particle resolution, they offer the unique possibility to compare the experimental temperatures of the peak position of $c_N(T)$ and symmetry breaking, respectively. While order parameter correlation functions confirm the Kosterlitz-Thouless-Halperin-Nelson-Young melting scenario where translational and orientational order symmetries are broken at different temperatures with an intermediate so called hexatic phase, we observe a single peak of the specific heat within the hexatic phase, with excellent agreement between experiment and simulation. Thus, the peak is not associated with broken symmetries but can be explained with the total defect density, which correlates with the maximum increase of isolated dislocations. The absence of a latent heat strongly supports the continuous character of both transitions.

DOI: 10.1103/PhysRevLett.113.127801

PACS numbers: 61.20.Ja, 64.70.D-, 64.70.pv, 65.40.Ba

KTHNY theory, a microscopic melting scenario for two-dimensional solids developed by Kosterlitz, Thouless, Halperin, Nelson, and Young [1-3], motivated extended analytic theories [4-8], numerous experimental studies [9-24], and simulations [25-44] to clarify the detailed melting mechanism and the order of phase transitions in two dimensions. The KTHNY melting is mediated by the dissociation of two kinds of topological defects, dislocations and disclinations. This scenario predicts two continuous phase transitions, where translational and orientational order is broken at different temperatures by the unbinding of pairs of dislocations and disclinations. In a triangular lattice, a disclination is a five- or sevenfold oriented site and a dislocation consists of oppositely charged disclinations, namely, a pair of bound five- and sevenfold sites. Both types of topological defects can be treated as a Coulomb gas obeying a logarithmic interaction potential in two dimensions [45]. For the dislocation unbinding, a vector charge description becomes necessary due to the directional character of the defects. The self-screening of the vector gas is taken into account by a renormalization group analysis. A scalar gas of charged defects describes the disclination unbinding in a second step. The intermediate thermodynamic phase is named hexatic. Several experiments [12-15,18-22] and simulations [25-33] clearly show the existence of the hexatic phase, but some studies additionally report first-order characteristics [16,35-40] versus continuous order [18,19,22]. Continuous solid-hexatic and first-order hexatic-isotropic characteristics have been observed for hard discs [41]. Alternatively the two-step melting can be preempted by a single first-order transition when the pair potential contains two length scales [42,43]. It has been suggested that the nature and number of transitions in two dimensions either depends on the dislocation core energy [6,34] (which might implicitly depend on the particle pair interaction being short or long range) or the angular stiffness of the crystal being lower than a critical value [8].

While first-order phase transitions are known to show a discontinuity in the free energy and a $\delta$-like divergence in the specific heat at the transition temperature, the defect free energy and specific heat of the two-dimensional Coulomb gas have only discontinuities and no divergence for both transitions [2,46,47]. Thus, the behavior of the specific heat can be used to identify the order of the transition. On the experimental side, there have been only calorimetric measurements so far, e.g., on atomic monolayers on graphite which show different results concerning the number of peaks in the specific heat, their position and magnitude [48-52]. These experiments lack a precise determination of symmetry switching points, leaving the correlation to occurring phase transitions still elusive. Simulations of interacting dislocations show that for small dislocation core energies, the specific heat has a large discontinuity consistent with a first-order transition while for large core energies, a single moderate peak was observed, pointing to a continuous character [34]. Laplacian roughening models [26] (which are dual to 2D melting) and Lennard-Jones systems [33] display one nondivergent peak along the two-step KTHNY scenario whereas a nonideal Yukawa system shows two singularities associated with two transitions [53]. However, in contrast to the atomic or molecular systems mentioned above, microscopy of individual particles in colloidal systems allows a direct comparison between specific heat and symmetry switching points.


In this work, we present a melting study of superparamagnetic colloidal spheres confined in two dimensions and corresponding Monte Carlo simulations. The precise knowledge of the particle pair potential together with high precision single particle resolution and long term stability of the sample allows us to measure an anomaly in the specific heat and compare it with simulations. Using order parameter correlation functions, we confirm in the experiments and simulations the two-step KTHNY melting scenario from a solid phase through a hexatic fluid to an isotropic fluid, yet we find a single peak in the specific heat. Remarkably, this peak does not coincide with either transition temperature but lies within the hexatic phase. We show that it is connected to a sharp increase of the number of topological defects associated with a progressive unbinding of dislocation pairs on heating above the solid-hexatic transition temperature. Further, we do not find an additional peak correlated to the disclination unbinding which might not be resolvable due to the very small concentration of single disclinations $<5‰$ in the background of a large overall defect density at the hexatic-isotropic transition.

The experimental system consists of an ensemble of spherical superparamagnetic polystyrene beads, with diameter $d = 4.5\ \mu\text{m}$ and mass density $1.7\ \text{kg/dm}^3$, dissolved and sterically stabilized with sodium dodecyl sulfate in water. The colloidal suspension is sealed in a millimeter sized glass cell where sedimentation leads to the formation of a monolayer $(> 10^5$ particles) on the bottom glass plate. The whole sample is under steady control and stable for more than 20 months which allows sufficient equilibration times and provides ideal sample conditions, e.g., vanishing density gradients or drifts. The ensemble is kept at room temperature and a highly homogeneous, finely tunable external magnetic field $H$ perpendicular to the colloidal layer induces a repulsive dipole-dipole interaction between the particles. This is quantified by the inverse system temperature that is defined as the ratio of the mean magnetic energy between two neighboring particles $E_{\text{mag}}$ and the thermal energy,

$$
\Gamma = \frac{E_{\text{mag}}}{k_B T} = \frac{\mu_0 (\pi n)^{3/2} (\chi H)^2}{4\pi k_B T}, \tag{1}
$$

where $n = 1/a_0^2$ is the 2D particle density with the mean particle distance $a_0$ and $\chi$ the magnetic susceptibility of the beads. We assume an error of $\Gamma \pm 0.5$ due to density and room temperature fluctuations during the measurements. After changing the interaction strength, the system is equilibrated for at least 24 hours before $\approx 3000$ particles are monitored and tracked by video microscopy. Previous studies of this system have shown excellent agreement with the KTHNY melting scenario [13–15,18,22,23].

In addition, standard Monte Carlo simulations are run in an ensemble with constant particle number, volume, and temperature (NVT ensemble), with $N = 2500$ particles interacting with a dipolar potential: $\beta V(r) = \Gamma / r^3$, with distances measured in units of $(\pi n)^{-1/2}$. The interactions are cut off at $R_{\text{cut}} = 9a_0$, which is large enough to avoid effects from the truncation [29]. The system is simulated in a rectangular box with a size ratio $2:\sqrt{3}$ and a (hard disc) 2D area fraction $\phi = 0.07$ to mimic the experimental conditions. Cycles of increasing $\Gamma$ from the fluid to the crystal, and subsequent decrease to the fluid again were used to confirm that there is no hysteresis within our $\Gamma$ resolution.

To determine the respective symmetry breaking temperatures, we analyze the spatial correlation function $g_6(r) = \langle \psi_6^*(r) \psi_6(0) \rangle$ of the orientational order parameter $\psi_6 = \frac{1}{n_j} \sum_k \exp(i6\theta_{jk})$, where the sum runs over all $n_j$ nearest neighbors of particle $j$, and $\theta_{jk}$ is the angle of the $k$th bond with respect to a certain reference axis. According to the KTHNY theory, $g_6(r)$ approaches a constant value in the solid phase (long-range order), decays algebraically $\sim r^{-\eta_6}$ in the hexatic fluid (quasi-long-range), and exponentially $\sim e^{-r/\xi_6}$ in the isotropic fluid (short-range), with an orientational correlation length $\xi_6$. The orientational exponent $\eta_6$ is inversely proportional to the orientational stiffness of the system: infinite in the solid, zero in the isotropic fluid, and finite in the hexatic phase, approaching a value of $\eta_6 \sim 1/4$ at the hexatic-isotropic transition [2,18]. This behavior of $g_6(r)$ has successfully been probed and verified in experiments [13,18–21] and simulations [27,29–32]. The results for our system are shown in Fig. 1: for both experiment and simulation, we clearly observe the characteristic behavior of $g_6(r)$ for the different phases, verifying the stability of the orientational quasi-long-range ordered hexatic fluid. For the solid-hexatic transition, we find the (inverse) transition temperatures $\Gamma_m^{\text{exp}} \approx 70.3$ and $\Gamma_m^{\text{sim}} = 69.25$ and for the hexatic-isotropic transition $\Gamma_i^{\text{exp}} \approx 67.3$ and $\Gamma_i^{\text{sim}} = 68.25$ [54]. These values are extracted from Fig. 1. Since the solid-hexatic transition is more difficult to locate by means of $g_6(r)$, we present a finite-size analysis of the translational order parameter and the 2D Lindemann parameter in the Supplemental Material confirming these values [55]. It is well known that the width of the hexatic phase is affected by the system size which might explain the small differences in the melting temperatures in experiment and simulation.

Within KTHNY theory, the specific heat is inversely proportional to diverging correlation lengths (with well-defined critical exponents) and shows no divergence but only an essential singularity at both transitions [2,47]. In the context of simulations, it has been discussed whether these singularities might appear as a more or less pronounced "bump" whose location and shape is strongly model dependent or not detectable at all [46]. In what follows we prove that the characteristics of the specific heat as a function of temperature can indeed be explained with the defect density, as suggested by Katherine Strandburg

![](./images/814697386776461312_1.jpg)

FIG. 1 (color online). Spatial orientational correlation $g_6(r) = \langle \psi_6^{*}(r)\psi_6(0) \rangle$ at different system temperatures $\Gamma$ for experiment (a) and simulation (b). The data are plotted on a log-log scale in reduced coordinates, where $a_0=(n)^{-1/2}$ is the mean particle distance in the respective system. The decay behavior of $g_6(r)$ has distinct characteristics in the solid (constant), the hexatic fluid (algebraic decay), and in the isotropic fluid (exponential decay). An algebraic exponent of $-1/4$ marks the hexatic-isotropic transition [2].

[46]. The energy of both dislocations and disclinations is described with an elastic (logarithmic) part above a cutoff radius $a_{\rm core}$. Below $a_{\rm core} \approx a_0$ the continuum elastic description fails and the energy is given by a discrete value $E_{\rm core}$ [2,3,64]. During melting, at least this core energy has to be provided for the dissociation of dislocations and disclinations.

From the data, the specific heat $c_N$ per particle and at constant volume can be calculated via the derivative of the internal energy with respect to temperature (inverse $\Gamma$) or from energy fluctuations (see the Supplemental Material [55]),

$$
c_N = \frac{1}{N} \frac{\partial \langle E \rangle}{\partial T} = -k_B \Gamma^2 \frac{\partial (\tilde{E}/\Gamma)}{\partial \Gamma} = \frac{\langle E^2 \rangle - \langle E \rangle^2}{N k_B T^2}, \tag{2}
$$

where $E$ is the total internal energy of the $N$-particle system, the brackets denote a time average, and $\tilde{E} = \langle E \rangle / N k_B T$ [65]. The results are shown in Fig. 2: summing up the energy, the cutoff is set to $15a_0$ for the experiment

![](./images/814697386776461312_2.jpg)

FIG. 2 (color online). Filled symbols correspond to experiment, open symbols to simulation. (a) Specific heat $c_N/k_B$ as a function of $\Gamma$ calculated via the derivative approach. The inset shows the energy per particle. (b) $c_N/k_B$ for experiment (right side of the right scale) and simulation (left side of the right scale) from energy fluctuations and the total defect number density (left scale), counting all defects ($\rho$) and isolated disclinations ($\rho_{\rm disc}$). (c) and (d) The behavior of isolated dislocations and disclinations analyzed with tanh fit to show the steepest increase. The background color of (b),(c),(d) is organized as follows: the solid and isotropic fluid found by the experiment are colored blue and red (dark gray), respectively. The hexatic phase is colored green (light gray). The color gradient shows the estimated error in determining the transition temperatures.

and $9a_0$ for the simulation (further discussion of the cutoff dependency can be found in the Supplemental Material [55]). Within the simulations, the calculation of $c_N$ from the derivative of the energy [Fig. 2(a)] and its fluctuations [Fig. 2(b)] agree almost quantitatively and show a single peak at $\Gamma_{c_N}^{\text{sim}}=68.5$ due to a single change of slope in the energy (inset). In the solid phase we observe a value of $c_N$ in agreement with the Dulong-Petit law $c_N=\frac{4}{2}Nk_B$, predicting the heat capacity of a two-dimensional monatomic crystal [horizontal line in Fig. 2(a)]. For the experiments, the calculation from the derivative of the energy is too noisy (see the Supplemental Material [55]), and a reliable value can be obtained only from the energy fluctuations [Fig. 2(b)]. We find again a single marginal peak at $\Gamma_{c_N}^{\text{exp}}\approx68.4$, very close to the value of the simulations. (Note, however, the different scale for experiment and simulation of $c_N$. As discussed in the Supplemental Material [55], an increased peak height and baseline can be attributed to additional density fluctuations picked up in the experiment. Nevertheless, those "mechanical" fluctuations do not affect the peak position.) The (inverse) temperature $\Gamma_{c_N}$ of the specific heat peak lies within the hexatic phase below the melting temperature $\Gamma_m$ from solid to hexatic ($\Gamma_{c_N}<\Gamma_m$ or $T_{c_N}>T_m$), both in the experiments and simulations. A second peak is not detectable. This is unexpected, given the picture of the KTHNY theory which predicts two specific heat discontinuities (eventually marginal) located at the transition temperatures [2]. Already in the 1950s, a shift of the specific heat peak in 2D systems has been reported for quantum fluids like $^4$He films, whose position is found at higher temperatures with respect to the onset of superfluidity [66,67]. The authors put this on the increasing importance of surface excitations with reduced film thickness. de Gennes (comment in [67]) pointed out that the temperature onset of superfluidity might be caused by short-range-order effects which become important in one- and two-dimensional salts [68,69]. Later, Kosterlitz and Thouless [1] considered this effect for the neutral superfluid in 2D. Berker and Nelson [70] gave analytic evidence for a specific heat shift for superfluid films of $^3$He-$^4$He mixtures, and explained this with the gradual unbinding of vortex pairs with increasing temperature while the maximum in the specific heat occurs when the mean separation of vortex pairs is comparable with the vortex core size. A shift of the peak to higher temperatures has also been reported in simulations of planar models [71-73] and 2D solids [26,33,34].

To explain the shift in the specific heat peak, we investigate the defect distributions on single particle level. We analyze the total number density $\rho$ of defects [all *not* sixfold coordinated sites, Fig. 2(b)] as well as the density of isolated dislocations and disclinations for both, experiment [Fig. 2(c)] and simulation [Fig. 2(d)]. (Note, that one dislocation consist of two defects.) In the region of the peak, the overall defect density $\rho$ undergoes a significant increase from $\approx$5% to $\approx$20%. Energy costs which become apparent in the specific heat should directly be connected to the core energy due to the creation and dissociation of defects. $c_N$ should peak where the increase of defects is largest (which is not at $\Gamma_m$). This can clearly be seen from the simulations where the sharpest increase of $\rho$ is exactly at the peak position $\Gamma_{c_N}^{\text{sim}}=68.5(\Delta\rho\approx0.1)$. With the total defect increase $\Delta N_{\text{def}}\approx220$ at this interaction strength, we can make a rough estimate for the simulation peak height via the the dislocation core energy in the hexatic phase $E_c\approx5.5k_BT$ [64] yielding $c_N\approx30k_B$ (see the Supplemental Material [55]). The defect density in the experiment, on the other hand, shows a rather broad increase. It must be noted that our analysis includes all kinds of defects, even cluster conformations which earliest occur in the hexatic phase. KTHNY theory does not account for such cluster but assumes a dilute gas of defects. But clustering at finite defect densities is quite natural due to the attractive interaction of the defects. Counting all (including clustered) dislocations, the peak height is already overestimated compared to the measurements. Implicitly, this means that such clustered dislocations seem to have a significantly reduced core energy $E_c<5.5k_BT$. We checked that such a cluster consists only of an equal amount of five- and seven-folded particles in the hexatic phase: clusters are dislocation cluster (with small core energy) but not a dislocation-disclination cluster. The latter, with an unequal number of five- and seven-folded particles, are only observable quite deep in the isotropic phase. Thus, we focus on the isolated topological defects that drive the transitions within KTHNY theory: isolated dislocations show their sharpest increase in density below $\Gamma_m$ but very close to the peak position ($\Gamma_{\text{disl}}^{\text{exp}}\approx68.2$ for the experiment and $\Gamma_{\text{disl}}^{\text{sim}}\approx68.4$ for the simulation). On the other hand, the steepest but small increase of isolated disclinations is shifted with respect to the hexatic-isotropic transition as well, but only marginally. We do not observe an indication of a second peak in specific heat corresponding to disclination unbinding presumably because the number of disclinations is less than 5$\text{\textperthousand}$ of the overall defect density [see Fig. 2(b)]. A rough estimate of the peak height due to disclination unbinding ($E_{\text{core}}^{\text{discl}}\approx5k_BT$) gives only $\approx1k_B$ [64].

In summary, we have measured the specific heat via fluctuations of the internal energy using a colloidal model system and Monte Carlo simulations. We observe a single peak in the specific heat above the solid-hexatic transition ($T_{c_N}>T_m$), although melting in two dimensions shows two phase transitions at distinct temperatures. The peak in $c_N$ arises when the change in the defect density is largest, which appears within the hexatic phase and not directly at $T_m$. Whereas only a few defects are needed to destroy the given order at $T_m$ (and $T_i$), their cost in energy is small. A second peak in $c_N$ associated to disclination unbinding from dislocations is not detectable since their number density stays small compared to the overall defect density

even deep in the isotropic fluid phase. We can further conclude that the absence of a latent heat strongly supports the continuous character of both transitions.

A. M. P. acknowledges financial support from the Consejera de Economía, Innovación y Ciencia (Junta de Andalucía), and from the Ministerio de Ciencia e Innovación, and FEDER funds, under Projects No. P09- FQM-4938 and No. MAT2011-28385, respectively. P. K. acknowledges support from the German Research Foundation (DFG), Project No. KE 1168/8-1.

[1] J. M. Kosterlitz and D. J. Thouless, J. Phys. C **5**, L124 (1972); **6**, 1181 (1973).
[2] B. I. Halperin and D. R. Nelson, Phys. Rev. Lett. **41**, 121 (1978); D. R. Nelson and B. I. Halperin, Phys. Rev. B **19**, 2457 (1979).
[3] A. P. Young, Phys. Rev. B **19**, 1855 (1979).
[4] D. S. Fisher, B. I. Halperin, and R. Morf, Phys. Rev. B **20**, 4692 (1979).
[5] T. V. Ramakrishnan, Phys. Rev. Lett. **48**, 541 (1982).
[6] S. T. Chui, Phys. Rev. Lett. **48**, 933 (1982).
[7] H. Kleinert, Phys. Lett. **95A**, 381 (1983).
[8] H. Kleinert, Phys. Lett. A **130**, 443 (1988); **136**, 468 (1989).
[9] A. Widom, J. R. Owers-Bradley, and M. G. Richards, Phys. Rev. Lett. **43**, 1340 (1979).
[10] W. F. Brinkmann, D. S. Fisher, and D. E. Moncton, Science **217**, 693 (1982).
[11] T. F. Rosenbaum, S. E. Nagler, P. M. Horn, and R. Clarke, Phys. Rev. Lett. **50**, 1791 (1983).
[12] R. E. Kusner, J. A. Mann, J. Kerins, and A. J. Dahm, Phys. Rev. Lett. **73**, 3113 (1994).
[13] K. Zahn, R. Lenke, and G. Maret, Phys. Rev. Lett. **82**, 2721 (1999).
[14] K. Zahn and G. Maret, Phys. Rev. Lett. **85**, 3656 (2000).
[15] H. H. von Grünberg, P. Keim, K. Zahn, and G. Maret, Phys. Rev. Lett. **93**, 255703 (2004).
[16] D. E. Angelescu, C. K. Harrison, M. L. Trawick, R. A. Register, and P. M. Chaikin, Phys. Rev. Lett. **95**, 025702 (2005).
[17] A. V. Petukhov, D. van der Beek, R. P. A. Dullens, I. P. Dolbnya, G. J. Vroege, and H. N. W. Lekkerkerker, Phys. Rev. Lett. **95**, 077801 (2005).
[18] P. Keim, G. Maret, and H. H. von Grünberg, Phys. Rev. E **75**, 031402 (2007).
[19] Y. Han, N. Y. Ha, A. M. Alsayed, and A. G. Yodh, Phys. Rev. E **77**, 041406 (2008).
[20] Y. Peng, Z. Wang, A. M. Alsayed, A. G. Yodh, and Y. Han, Phys. Rev. Lett. **104**, 205703 (2010).
[21] A. Brodin, A. Nych, U. Ognysta, B. Lev, V. Nazarenko, M. Skarabot, and I. Musevic, Condens. Matter Phys. **13**, 33601 (2010).
[22] S. Deutschländer, T. Horn, H. Löwen, G. Maret, and P. Keim, Phys. Rev. Lett. **111**, 098301 (2013).
[23] T. Horn, S. Deutschländer, H. Löwen, G. Maret, and P. Keim, Phys. Rev. E **88**, 062305 (2013).
[24] J. Schockmel, E. Mersch, N. Vandewalle, and G. Lumay, Phys. Rev. E **87**, 062201 (2013).

[25] D. Frenkel and J. P. McTague, Phys. Rev. Lett. **42**, 1632 (1979).
[26] K. J. Strandburg, S. A. Solla, and G. V. Chester, Phys. Rev. B **28**, 2717 (1983).
[27] C. Udink and J. van der Elsken, Phys. Rev. B **35**, 279 (1987).
[28] K. Chen, T. Kaplan, and M. Mostoller, Phys. Rev. Lett. **74**, 4019 (1995).
[29] S. Z. Lin, B. Zheng, and S. Trimper, Phys. Rev. E **73**, 066106 (2006).
[30] H. Shiba, A. Onuki, and T. Araki, Europhys. Lett. **86**, 66004 (2009).
[31] N. Gribova, A. Arnold, T. Schilling, and C. Holm, J. Chem. Phys. **135**, 054514 (2011).
[32] S. Prestipino, F. Saija, and P. V. Giaquinta, Phys. Rev. Lett. **106**, 235701 (2011).
[33] K. Wierschem and E. Manousakis, Phys. Rev. B **83**, 214108 (2011).
[34] Y. Saito, Phys. Rev. Lett. **48**, 1114 (1982).
[35] S. Toxvaerd, Phys. Rev. Lett. **44**, 1002 (1980).
[36] F. F. Abraham, Phys. Rev. Lett. **44**, 463 (1980).
[37] J. Tobochnik and G. V. Chester, Phys. Rev. B **25**, 6778 (1982).
[38] K. J. Strandburg, J. A. Zollweg, and G. V. Chester, Phys. Rev. B **30**, 2755 (1984).
[39] H. Weber, D. Marx, and K. Binder, Phys. Rev. B **51**, 14636 (1995).
[40] A. H. Marcus and S. A. Rice, Phys. Rev. Lett. **77**, 2577 (1996).
[41] E. P. Bernard and W. Krauth, Phys. Rev. Lett. **107**, 155704 (2011).
[42] S. Prestipino, F. Saija, and P. V. Giaquinta, J. Chem. Phys. **137**, 104503 (2012).
[43] D. E. Dudalov, Yu. D. Fomin, E. N. Tsiok, and V. N. Ryzhov, Phys. Rev. Lett. **112**, 157803 (2014)
[44] H. Löwen, Phys. Rev. E **53**, R29 (1996).
[45] P. Minnhagen, Rev. Mod. Phys. **59**, 1001 (1987).
[46] K. J. Strandburg, Rev. Mod. Phys. **60**, 161 (1988).
[47] J. M. Kosterlitz, J. Phys. C **7**, 1046 (1974).
[48] T. T. Chung, Surf. Sci. **87**, 348 (1979).
[49] A. D. Migone, Z. R. Li, and M. H. W. Chan, Phys. Rev. Lett. **53**, 810 (1984).
[50] H. K. Kim, Q. M. Zhang, and M. H. W. Chan, Phys. Rev. Lett. **56**, 1579 (1986).
[51] R. Marx and B. Christoffer, Phys. Rev. B **37**, 9518 (1988).
[52] A. Warken, M. Enderle, and K. Knorr, Phys. Rev. B **61**, 3028 (2000).
[53] O. S. Vaulina, Yu. V. Khrustalyov, O. F. Petrov, and V. E. Fortov, Europhys. Lett. **89**, 35001 (2010).
[54] These values differ from the transition points found in earlier works (Refs. [13–15,18]) by a constant factor (see the Supplemental Material [55]).
[55] See the Supplemental Material http://link.aps.org/ supplemental/10.1103/PhysRevLett.113.127801, which in- cludes Refs. [56–63], for further information.
[56] K. Bagchi, H. C. Andersen, and W. Swope, Phys. Rev. Lett. **76**, 255 (1996).
[57] V. M. Bedanov and G. V. Gadiyak, Phys. Lett. **109A**, 289 (1985); X. H. Zheng and J. C. Earnshaw, Europhys. Lett. **41**, 635 (1998).

127801-5

[58] P. M. Chaikin and T. C. Lubensky, *Principles of Condensed Matter Physics* (Cambridge University Press, Cambridge, England, 1995), Chap. 3, p. 120.

[59] David Polster, Ph.D. thesis, University of Konstanz, 2014, http://nbn-resolving.de/urn:nbn:de:bsz:352-268915.

[60] K. Zahn, J. M. Méndez-Alcaraz, and G. Maret, *Phys. Rev. Lett.* **79**, 175 (1997).

[61] P. Keim, G. Maret, U. Herz, and H. H. von Grünberg, *Phys. Rev. Lett.* **92**, 215504 (2004).

[62] D. Hajnal, J. M. Brader, and R. Schilling, *Phys. Rev. E*, **80**, 021503 (2009).

[63] D. Hajnal, M. Oettel, and R. Schilling, *J. Non-Cryst. Solids* **357**, 302 (2011).

[64] C. Eisenmann, U. Gasser, P. Keim, G. Maret, and H. H. von Grünberg, *Phys. Rev. Lett.* **95**, 185502 (2005).

[65] Since we have a purely repulsive system with an algebraic distance dependence, we have only a single control parameter which is $\Gamma$. For a given particle number, pressure ($\sim \chi^2 H^2$) and volume cannot be changed independently.

Therefore, we denote the specific heat of this particular system with the subscript $N$.

[66] D. F. Brewer, A. J. Symonds, and A. L. Thomson, *Phys. Rev. Lett.* **15**, 182 (1965).

[67] A. J. Symonds, D. F. Brewer, and A. L. Thomson, *Quantum Fluids*, edited by D. F. Brewer (North Holland, Amsterdam, 1966), p. 267.

[68] L. C. van der Marel, J. van den Broek, J. D. Wasscher, and C. J. Gorter, *Physica (Amsterdam)* **21**, 685 (1955).

[69] H. M. Gijsman, N. J. Poulis, and J. van den Handel, *Physica (Amsterdam)* **25**, 954 (1959).

[70] A. N. Berker and D. R. Nelson, *Phys. Rev. B* **19**, 2488 (1979).

[71] J. Tobochnik and G. V. Chester, *Phys. Rev. B* **20**, 3761 (1979).

[72] J. E. Van Himbergen and S. Chakravarty, *Phys. Rev. B* **23**, 359 (1981).

[73] S. A. Solla and E. K. Riedel, *Phys. Rev. B* **23**, 6008 (1981).