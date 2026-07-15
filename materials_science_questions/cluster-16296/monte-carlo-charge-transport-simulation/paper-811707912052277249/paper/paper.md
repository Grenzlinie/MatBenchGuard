![](./images/811707912052277249_1.jpg)

# Monte Carlo simulation of carrier dynamics in terahertz quantum cascade lasers

Y. J. Han and J. C. Cao

Citation: *J. Appl. Phys.* **108**, 093111 (2010); doi: 10.1063/1.3505675
View online: http://dx.doi.org/10.1063/1.3505675
View Table of Contents: http://jap.aip.org/resource/1/JAPIAU/v108/i9
Published by the AIP Publishing LLC.

---

Additional information on *J. Appl. Phys.*
Journal Homepage: http://jap.aip.org/
Journal Information: http://jap.aip.org/about/about_the_journal
Top downloads: http://jap.aip.org/features/most_downloaded
Information for Authors: http://jap.aip.org/authors

![](./images/811707912052277249_2.jpg)

# Monte Carlo simulation of carrier dynamics in terahertz quantum cascade lasers
Y. J. Han and J. C. Cao${}^{\mathrm{a)}}$
Laboratory of Terahertz Solid-State Technology, Shanghai Institute of Microsystem and Information Technology, Chinese Academy of Sciences, 865 Changning Road, Shanghai 200050, China

(Received 29 March 2010; accepted 13 September 2010; published online 8 November 2010)

We employ a Monte Carlo method to investigate the carrier dynamics in the terahertz quantum cascade lasers with vertical and diagonal radiative transition designs. Electron-electron and electron-phonon scattering are included in the calculations and their effects on the temperature dependence of electron transport are evaluated. The simulation shows that the degradation of temperature performance is mainly due to the rapid electron relaxation from upper to lower laser levels, in which the electron-phonon interaction is the dominant scattering mechanism. The parasitic coupling between laser levels is weakened in the diagonal design, resulting in better device performance such as lower current density, higher operating temperature, and less hot electron effects. The calculations are in good agreement with experimental results. © 2010 American Institute of Physics. [doi:10.1063/1.3505675]

## I. INTRODUCTION

Terahertz (THz) technology has attracted lots of interests due to its wide potential applications.${}^{1,2}$ As one of important sources, THz quantum cascade lasers (QCLs) were successfully demonstrated with the active region of chirped superlattice,${}^{3}$ bound to continue,${}^{4}$ and resonant phonon${}^{5}$ designs, respectively. Because the lasing levels in a THz QCL have a small energy separation, strong nonradiative transitions lead to a large decrease in population inversion at elevated temperatures. Up to now, THz QCLs are still need to be cryogenically cooled, and the operation up to 178 K and 186 K have been demonstrated with vertical${}^{6}$ and diagonal${}^{7}$ radiative transition designs, respectively. When an external magnetic field is applied, the operating temperature is increased to 225 K.${}^{8}$

Theoretical analyses of THz QCLs have been performed in order to explain physical processes and improve existing designs. As an important issue, temperature performance was simulated in different designs, and the reason of device performance degradation was respectively attributed to larger parasitic injection, shorter upper-state lifetime and less efficiency of extraction process.${}^{9–11}$ Recently, temperature performance of THz QCL has been improved by replacing a vertical radiative transition design with a diagonal design.${}^{7}$ With a goal to achieve higher temperature operation, better understanding of carrier dynamics is necessary to identify the dominant mechanism of temperature performance degradation in such designs.

In this paper, Monte Carlo (MC) simulation${}^{12–20}$ is carried out to study the electron transport in the above-mentioned THz QCLs which are based on vertical${}^{6}$ and diagonal${}^{7}$ radiative transition design, respectively. After a short description of simulation model, the influences of the active region modification on current density, electron distribution, lifetime, and optical gain are comparatively investigated. At the bias for the largest optical gain, the importance of different scattering mechanisms and different transport channels are analyzed, and the dominant temperature degradation mechanism is clarified.

## II. MC SIMULATION MODEL

In our model, 5000 electrons are engaged in three modules of THz QCL structures. We assume that the modules are ideally periodic and an electron scattered out of a module is reinjected with identical in-plane wave vector. The electronic states of the structure are determined by self-consistently solving Schrödinger and Poisson equations, and the lowest four subbands in each module are selected to set up a scattering table${}^{21}$ in which electron-LO phonon ($e$-LO) and electron–electron ($e$-$e$) interactions are included. The maximum $e$-$e$ scattering probability is calculated as${}^{20}$

$$
\Gamma_{im,max}^{ee}(k_{1})=\frac{m^{*}N_{sub}}{2\hbar^{3}A}M_{im,max}^{2}\sum_{j,\mathbf{k}_{2}}f_{j}(\mathbf{k}_{2}), \tag{1}
$$

where $m^{*}$ is the effective mass, $N_{sub}$ is the total number of subband, $\hbar$ is the reduced Planck constant, $M_{im,max}^{2}$ is the maximum of transition matrix element $|M_{ijmm}(q)|^{2}$. Note that $M_{im,max}^{2}$ is not related with partner electrons and $\Gamma_{im,max}^{ee}(k_{1})$ depends only on the electron distribution $f_{j}(\mathbf{k}_{2})$, which can avoid introducing artificial errors by random selection of the partner electron.

The electrons in each subband are assumed to obey Fermi-Dirac distribution with respective quasi-Fermi level and effective temperature. The effective temperature $T_{i}^{*}$ and quasi-Fermi level $E_{F,i}^{*}$ of subband $i$ can be calculated as

$$
\beta_{i}=k_{B}T_{i}^{*}\left[1-\exp\left(-\frac{n_{i}}{\rho_{i}k_{B}T_{i}^{*}}\right)\right], \tag{2}
$$

${}^{\mathrm{a)}}$Electronic mail: jccao@mail.sim.ac.cn.

![](./images/811707912052277249_3.jpg)

FIG. 1. (Color online) Calculated potential profiles and squared wave functions of the THz QCLs with vertical (a) and diagonal (b) radiative transition designs. The external applied bias is 60 mV/module for the vertical design and 64 mV/module for the diagonal design.

$$
E_{F, i}^{*}=E_{i}-k_{B} T_{i}^{*} \ln \left(\frac{k_{B} T_{i}^{*}}{\beta_{i}}-1\right), \tag{3}
$$

where $\beta_{i}$ can be obtained as $^{16}$

$$
\beta_{i}=\int_{0}^{\infty} f_{i}(\varepsilon)\left[1-f_{i}(\varepsilon)\right] d \varepsilon, \tag{4}
$$

and $k_{B}$ is the Bolzmann constant, $n_{i}$ is the electron sheet density, $\rho_{i}$ is two-dimensional density of states, $f_{i}(\epsilon)$ is the electrons' distribution.

During the simulation, Pauli exclusion principle is applied to deal with the degeneracy effect. The carrier distribution, scattering rates, and current density are obtained after an equilibrium condition is achieved.

## III. SIMULATION RESULTS

The simulated devices are resonant-phonon assisted THz QCLs with the vertical $^{6}$ and diagonal $^{7}$ radiative transition designs, respectively. The conduction band diagrams and squared wave functions are shown in Fig. 1. Starting from the injection barrier, the layer sequences are **48/96/20/74/42/161 Å** for the vertical design and **48/85/28/85/42/164 Å** for the diagonal design, where the $\mathrm{Al}_{0.15} \mathrm{Ga}_{0.85} \mathrm{As}$ barriers are shown in bold and GaAs wells in plain text. Because electron-impurity scattering is neglected in our simulation, the doping density of $3.0 \times 10^{10} \mathrm{~cm}^{-2}$ per module in the depopulation well is used for both designs in order to reduce the influences of doping difference on the simulation results. Radiative transition takes place from subband 4 to subband 3 with the dipole matrix element of 4.6 nm and 3.0 nm in the vertical and diagonal designs, respectively. The electrons in subband 3 are efficiently extracted by resonant tunneling and $e$-LO phonon scattering, resulting in large population inversion. The devices are fabricated with metal-metal waveguide structure $^{22,23}$ and the optical loss is calculated in a $100 \mu \mathrm{m}$ $\times 1$ mm laser ridge.

![](./images/811707912052277249_4.jpg)

FIG. 2. (Color online) Bias dependence of the current density $J$ (a), the lifetime of upper laser level $\tau_{4}$ (b), population inversion $\Delta n_{s, 43}$ (c), and optical mode gain (d) in the vertical and diagonal designs (VD and DD). The overestimated regions of the current density around 40 mV/module [in figure (a)] are neglected in the guide lines for eyes.

When the vertical transition is replaced by the diagonal one, electron transport through both radiative and nonradiative transitions will be affected. At the lattice temperature of 25 K, the devices' performance including current density $(J)$, lifetime $(\tau_{4})$, population inversion $(\Delta n_{s,43})$, and optical gain as a function of applied bias are compared in Fig. 2. A clear reduction in current density is observed in the diagonal design, which can be attributed to the weakened coupling between subbands 4 and 3. The threshold and maximum current densities are 218 and $500 \mathrm{~A} / \mathrm{cm}^{2}$ in the diagonal design, lower than 487 and $886 \mathrm{~A} / \mathrm{cm}^{2}$ in the vertical design with a factor of about 2. This trend is in a good agreement with experimental results although the simulated values are smaller than the measured ones as discussed elsewhere. $^{24}$ The population inversion, $\Delta n_{s,43} \propto J_{4} \tau_{4}(1-\tau_{3}/\tau_{43})$, is a key factor for lasing. In the present designs, the scattering time $\tau_{43}$ is much longer than $\tau_{3}$ at the lasing zone. Thus, the population inversion depends mainly on the lifetime $\tau_{4}$ and the injection current density $J_{4}$. Although the lifetime $\tau_{4}$ is in-

![](./images/811707912052277249_5.jpg)

FIG. 3. (Color online) Comparison of different electron transport channels for the vertical (a) and diagonal (b) designs at the lattice temperature of 25 K.

creased largely in the diagonal design, the population inver- sion is only enhanced a little. It indicates that the diagonal design leads to a reduction in $J_{4}$. During the calculation of optical gain, homogeneous broadening of spontaneous emis- sion linewidth $(\Delta \nu)$ is considered via the relation $^{25}$

$$
\Delta \nu=\frac{1}{\pi}\left(\frac{1}{2 \tau_{4}}+\frac{1}{2 \tau_{3}}+\frac{1}{\tau^{*}}\right), \tag{5}
$$

where $\tau^{*}$, the pure dephasing time, is a fit parameter with 0.10 ps and 0.14 ps for the vertical and diagonal designs, respectively. The optical gain of the diagonal design is much lower than that of the vertical design due to a smaller dipole matrix element. With Cu-Cu waveguide layers, lasing opera- tion can be observed at a wide bias range for both designs which has been experimentally demonstrated. The following discussion will be performed at the bias for the largest opti- cal gain.

To better understand the device performance, we inves- tigate the effects of different transport channels and scatter- ing mechanisms in Fig. 3. The electrons in subband $1'$ are mainly scattered to subbands 4, 3, and 2, while those in subband 4 are relaxed to subbands 3 and 2. The transport channel $1'-4$ is designed for the injection process in which the $e-e$ interaction is the dominant scattering mechanism. The other channels are due to parasitic coupling of subbands and the electron transport in those channels will lower the device quantum efficiency. The subbands 3 and 2 behave as important mediated states and the $e$-LO phonon scattering is more important than the $e-e$ scattering. In the diagonal de- sign, the parasitic coupling between subbands $1',4$ and sub- bands 3, 2 are weakened, which is the reason for the decrease in the current density $J$ and the increase in the lifetime $\tau_{4}$. Note that the scattering rate from $1'$ to 4 is also reduced. It leads to the decrease in injection current density $J_{4}$ and has a detrimental effect on the population inversion. A further op- timization of the injection process in the diagonal design possibly results in a better device performance. The contri- bution of LO phonon scattering through the absorption of phonons $(\propto n_{phonon})$ can be neglected in both designs because the phonon number $n_{phonon}$ is much smaller than 1.0 at 25 K.

![](./images/811707912052277249_6.jpg)

FIG. 4. (Color online) Temperature dependence of the injection levels' life- time and the key intersubband scattering rates in the vertical (a) and diago- nal (b) designs.

In the following, we evaluate the relative strength of carrier transport channels and scattering mechanisms at dif- ferent temperatures. For the injection subband $1'$, the scat- tering rates related with the two most important channels are plotted in Fig. 4. With the increase in temperature, the elec- tron transport from subband $1'$ to subbands 4 and 3 are en- hanced as indicated by the scattering rates $(\tau_{1'4})^{-1}$ and $(\tau_{1'3})^{-1}$. The relative concentration of both channels show a small variation. Therefore, the injection efficiencies $J_{4}/J$ only change a little around $64\%$ and $69\%$ for the vertical and diagonal designs, respectively. The injection process is gov- erned by $e-e$ scattering but the increase in the injection probability is due to the $e$-LO phonon scattering. The elec- tron relaxation through the channels 4-3 and 4-2 are shown in Fig. 5. The scattering rates, $(\tau_{43})^{-1}$ and $(\tau_{42})^{-1}$, increase with the temperature, which results from the thermal acti- vated $e$-LO phonon interaction. At the same time, the relative strength of the channel 4-3 becomes larger than that of 4-2 at elevated temperatures. Therefore, the rapid decrease in the upper laser levels' lifetime $\tau_{4}$ can be mainly ascribed to the electron relaxation from subband 4 to subband 3. The de- population ability can be reflected by the lower laser levels' lifetime $\tau_{3}$. As shown in Fig. 5, $\tau_{3}$ keeps stable from 25 to 200 K, which means that the lattice temperature has small influences on the depopulation process. From the above analysis, it is quite evident that the main reason for the tem- perature performance degradation is the sharp decrease in the upper laser level's lifetime, in which the $e$-LO phonon scat- tering between the laser subbands has a major effect.

In comparison, the diagonal design does not basically change the limiting factors for high temperature operation but it lowers the detrimental effects of the parasitic coupling between laser subbands. The influences on the subband oc-

![](./images/811707912052277249_7.jpg)

FIG. 5. (Color online) Temperature dependence of the laser levels' lifetime and the key intersubband scattering rates in the vertical (a) and diagonal (b) designs.

cupation and the optical mode gain are investigated in the following. With the increase in temperature, the evolutions of the carrier density in laser levels are shown in Fig. 6. The rapid decrease in the population in the subband 4 is mainly due to the increasing electron relaxation from the subband 4 to 3. At the same time, more electrons are injected to sub- band 3, and thus the population in the subband 3 increases accordingly because the extraction efficiency has a small temperature dependence. The diagonal design leads to the larger population inversion thanks to the longer lifetime of the upper laser level. The optical gain versus the lattice tem- perature is shown in Fig. 7. The decrease in the optical gain of both designs are attributed to the reduction in population inversion and the broadening of linewidth. With a slower decreasing rate, the optical gain of the diagonal design ex- ceeds that of the vertical design when the temperature is higher than 150 K. Note that the laser frequency of the two designs are different. With an attempt to clarify the influ- ences of the frequency difference, we calculate the optical gain in a modified diagonal design, which has the same laser frequency as the vertical design. It can be seen that the peak gain is lowered due mainly to the decrease in lasing fre- quency $(g_{peak } \propto h v)$ . However, the lower thermal quenching rate of the gain is still observed in the modified structure and its peak gain exceeds that of the vertical design at the tem- perature of 166 K. For the devices with $Cu-Cu$ waveguide, the maximum lasing temperature of the selected and modi- fied diagonal designs are 189 and 179 K, about 20 and 10 K higher than that of the vertical design. For those with Au-Au waveguide, the improvement is not demonstrated. The re- sults indicate that the temperature performance is improved by the diagonal design and the $Cu-Cu$ waveguide, which are in good agreement with experimental findings. The inset of Fig. 7 shows the gain profiles at the lattice temperature of 25 K. Since the gain can mainly be ascribed to a single transi- tion between laser levels, $^{26}$ the other transitions are ignored during the calculation of gain spectra. $^{25}$ The full width at halfmaximum of the gain spectra are 3.4 THz (vertical design) and 2.4 THz (diagonal design), a little larger than other pub- lished values. $^{25,26}$ It indicates that the pure dephasing time used in the calculation may be too short.

![](./images/811707912052277249_8.jpg)

FIG. 6. (Color online) The occupation of laser levels as a function of lattice temperature. VD $i$ and DD $i$ indicate the subband $i$ in the vertical and diagonal designs, respectively.

![](./images/811707912052277249_9.jpg)

FIG. 7. (Color online) The evolution of peak gain as a function of lattice temperature. DD-M indicates the modified diagonal design, which has the same laser frequency as the vertical design. The inset shows the gain spectra at 25 K.

The electron transport between laser levels is mainly me- diated by $e$ -LO phonon scattering because the electrons in the upper laser level are warmed up and get enough kinetic energy. With the assumption described in Sec. II, the electron distribution can be characterized by an effective temperature. Figure 8(a) shows the effective temperature of the upper la- ser level $(T_{4})$ as a function of lattice temperature. Hot elec tron regimes are demonstrated in both designs. With the lat- tice temperature increasing from 25 to 200 K, the effective temperature increases from 123 to 222 K in the vertical de- sign, and from 108 to 200 K in the diagonal design. The hot electron effects are efficiently lowered by the diagonal de- sign, which benefits to high temperature operation. The reli- ability of the description of hot electrons with an effective temperature is also investigated. In the MC simulation, elec- trons are scattered randomly and form a distribution after an equilibrium situation is obtained. Such a MC-distribution is similar to the real situation and can be used to examine whether the effective temperature description is sufficiently good or not. As shown in Figs. 8(b) and 8(c), the MC- distribution in subband 4 is compared with the theoretical Fermi-Dirac distribution at the lattice temperature of 25 and200 K. The electrons approximately obey the Fermi-Dirac

![](./images/811707912052277249_10.jpg)

FIG. 8. (Color online) The effective temperature of the upper laser levels $(T_{4})$ vs lattice temperatures $(T_{lattice})$ (a), and the electron distribution in the upper laser levels at the lattice temperature of 25 and 200 K [(b) and (c)]. The lines in the figures (b) and (c) indicate the quasi-Fermi-Dirac distribution functions.

distribution except for a little deflection at the kinetic energy of 10 meV. It indicates that the effective temperature is a reasonable parameter to describe the hot electrons' distribution in the simulated THz QCLs. In the diagonal design, a better consistency is observed between the MC-distribution and the theoretical principle. It is presumably related with the longer lifetime $\tau_{4}$ which leaves electrons enough time for relaxation.

## IV. CONCLUSION
Using the MC simulation, we have investigated the electron dynamics in the THz QCLs. The carrier transport between laser levels is dominated by the electron-phonon scattering. With the increase in temperature, it leads to strongly decreased lifetime and occupation of the upper laser level. The results indicate that the temperature performance is mainly limited by the large leakage from the upper laser level. The diagonal radiative transition design weakens such parasitic transport and higher operating temperature is therefore achieved.

## ACKNOWLEDGMENTS
One of the authors, Y. J. Han, would like to thank Dr. H. Li for valuable discussions. This work was supported by the National Basic Research Program of China (Project No. 2007CB310402), the National Natural Science Foundation of China (Project No. 60721004), the Major Projects (Project Nos. KGCX1-YW-24 and KGCX2-YW-231) and the Hundred Talent Program of the Chinese Academy of Sciences, and the Shanghai Municipal Commission of Science and Technology (Project No. 10JC1417000).

$^{1}$P. H. Siegel, IEEE Trans. Microwave Theory Tech. 50, 910 (2002).
$^{2}$M. Tonouchi, Nat. Photonics 1, 97 (2007).
$^{3}$R. Köhler, A. Tredicucci, F. Beltram, H. E. Beere, E. H. Linfield, A. G. Davies, D. A. Ritchie, R. C. Iotti, and F. Rossi, Nature (London) 417, 156 (2002).
$^{4}$G. Scalari, L. Ajili, J. Faist, H. Beere, E. Linfield, D. Ritchie, and G. Davies, Appl. Phys. Lett. 82, 3165 (2003).
$^{5}$B. S. Williams, H. Callebaut, S. Kumar, Q. Hu, and J. L. Reno, Appl. Phys. Lett. 82, 1015 (2003).
$^{6}$M. A. Belkin, J. A. Fan, S. Hormoz, F. Capasso, S. P. Khanna, M. Lachab, A. G. Davies, and E. H. Linfield, Opt. Express 16, 3242 (2008).
$^{7}$S. Kumar, Q. Hu, and J. L. Reno, Appl. Phys. Lett. 94, 131105 (2009).
$^{8}$A. Wade, G. Fedorov, D. Smirnov, S. Kumar, B. S. Williams, Q. Hu, and J. L. Reno, Nat. Photonics 3, 41 (2009).
$^{9}$D. Indjin, P. Harrison, R. W. Kelsall, and Z. Ikonić, Appl. Phys. Lett. 82, 1347 (2003).
$^{10}$C. Jirauschek and P. Lugli, Phys. Status Solidi C 5, 221 (2008).
$^{11}$J. C. Cao, J. T. Lü, and H. Li, Physica E (Amsterdam) 41, 282 (2008).
$^{12}$C. Jacoboni and L. Reggiani, Rev. Mod. Phys. 55, 645 (1983).
$^{13}$R. C. Iotti and F. Rossi, Appl. Phys. Lett. 76, 2265 (2000).
$^{14}$F. Compagnone, C. A. Di, and P. Lugli, Appl. Phys. Lett. 80, 920 (2002).
$^{15}$H. Callebaut, S. Kumar, B. S. Williams, Q. Hu, and J. L. Reno, Appl. Phys. Lett. 83, 207 (2003).
$^{16}$O. Bonno, J. L. Thobel, and F. Dessenne, J. Appl. Phys. 97, 043702 (2005).
$^{17}$J. T. Lü and J. C. Cao, Appl. Phys. Lett. 88, 061119 (2006).
$^{18}$C. Jirauschek, G. Scarpa, P. Lugli, M. S. Vitiello, and G. Scamarcio, J. Appl. Phys. 101, 086109 (2007).
$^{19}$H. Li, J. C. Cao, J. T. Lü, and Y. J. Han, Appl. Phys. Lett. 92, 221105 (2008).
$^{20}$Y. J. Han and J. C. Cao, Semicond. Sci. Technol. 24, 095026 (2009).
$^{21}$S. M. Goodnick and P. Lugli, Phys. Rev. B 37, 2578 (1988).
$^{22}$B. S. Williams, S. Kumar, H. Callebaut, Q. Hu, and J. L. Reno, Appl. Phys. Lett. 83, 2124 (2003).
$^{23}$B. S. Williams, S. Kumar, Q. Hu, and J. L. Reno, Opt. Express 13, 3331 (2005).
$^{24}$H. Callebaut, S. Kumar, B. S. Williams, Q. Hu, and J. L. Reno, Appl. Phys. Lett. 84, 645 (2004).
$^{25}$B. S. Williams, Ph.D. thesis, MIT, 2003.
$^{26}$C. Jirauschek and P. Lugli, J. Appl. Phys. 105, 123102 (2009).