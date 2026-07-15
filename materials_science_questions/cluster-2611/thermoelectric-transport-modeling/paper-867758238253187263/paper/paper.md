# Thermoelectric performance of classical topological insulator nanowires

Johannes Gooth$^{1,*}$, Jan Göran Gluschke$^{2,3}$, Robert Zierold$^{1}$, Martin Leijnse$^{2}$, Heiner Linke$^{2}$, Kornelius Nielsch$^{1\#}$

$^{1}$ Institute of Applied Physics, Universität Hamburg, Jungiusstrasse 11, 20355 Hamburg, Germany

$^{2}$ Solid State Physics and Nanometer Structure Consortium (nmC@LU),
Lund University, Box 118, S – 22100 Lund, Sweden

$^{3}$ School of Physics, The University of New South Wales, Sydney NSW 2052, Australia

Electronic address:
$^{*}$jgooth@physnet.uni-hamburg.de
$^{\#}$ knielsch@physnet.uni-hamburg.de

**ABSTRACT**

There is currently substantial effort being invested into creating efficient thermoelectric nanowires based on topological insulator chalcogenide-type materials. A key premise of these efforts is the assumption that the generally good thermoelectric properties that these materials exhibit in bulk form will translate into similarly good or even better thermoelectric performance of the same materials in nanowire form. Here, we calculate thermoelectric performance of topological insulator nanowires based on $Bi_2Te_3$, $Sb_2Te_3$ and $Bi_2Se_3$ as a function of diameter and Fermi level. We show that the thermoelectric performance of topological insulator nanowires does not derive from the properties of the bulk material in a straightforward way. For all investigated systems the competition between surface states and bulk channel causes a significant modification of the thermoelectric transport coefficients if the diameter is reduced into the sub-10 $\mu$m range. Key aspects are that the surface and bulk states are optimized at different Fermi levels or have different polarity as well as the high surface to volume ratio of the nanowires. This limits the maximum thermoelectric performance of topological insulator nanowires and thus their application in efficient thermoelectric devices.

### I. INTRODUCTION

Semiconductor nanowires have been predicted to significantly improve upon the corresponding bulk-material's efficiency of thermoelectric (TE) energy conversion,¹⁻³ quantified by the TE figure of merit $ZT = S^2\sigma T/(\kappa_{\rm el}+\kappa_{\rm ph})$ , where $T$ is the temperature, $S$ denotes the Seebeck coefficient, $\sigma$ the electrical conductivity, $\kappa_{el}$ the electron thermal conductivity and $\kappa_{ph}$ the phonon thermal conductivity. While a power factor $(S^2\sigma)$ enhancement in nanowires due to quantum dot like states has only been achieved at low temperatures,⁴ and the predicted $S^2\sigma$ enhancement due to 1D quantization has yet to be observed,⁵⁻⁷ it has been shown that utilizing the large surface to volume ratio $s/v$ of nanowires enhancing phonon surface scattering can be used to decreases $\kappa_{ph}$.⁸⁻¹¹ A common approach intended to create high performance TE devices for room temperature operation is therefore to downscale materials with already high bulk $ZT$ to improve the TE performance by taking advantage of the expected reduction of $\kappa_{ph}$ while–this is the rationale of this approach–maintaining the high electronic figure of merit $ZT_{\rm el} = S^2\sigma T/\kappa_{\rm el}$ of the bulk material. In particular chalcogenide nanowires based on ${\rm Bi_2Te_3, Sb_2Te_3}$ and ${\rm Bi_2Se_3}$ have attracted special interest and inspired extensive research efforts because these compounds are associated with the highest room-temperature bulk TE efficiencies to date, of up to $ZT \approx 1$ for ${\rm Bi_2Te_3}$.¹² Since $ZT$ strongly depends on the position of the Fermi level of the investigated system, a specific strategy to achieve maximal performance in nano-scaled TE devices is therefore to synthesize nanowires with carrier concentrations optimized for maximum bulk $ZT$.¹³⁻¹⁵ However, while the expected reduction in $\kappa_{ph}$ was observed in various thermoelectric transport experiments on such nanowires,¹⁶⁻¹⁹ the observed $S$ was reduced significantly,¹⁹⁻²³ resulting in a substantial decline of $ZT (\approx 0.1)$

compared to bulk values. Actually, for intrinsic $Bi_2Te_3$ nanowires (p-type in bulk) $S$ was found to be negative (corresponding to n-type transport).$^{21,24}$ Here, we demonstrate that these experimental observations are an expected consequence of the recently discovered topological insulator (TI) nature of such chalcogenide materials.$^{24-39}$ Three dimensional TIs are a phase of matter with insulating bulk and with two-dimensional topological surface states that form a single Dirac cone, protected by time reversal symmetry which results in unique transport properties. While topological surface states play no role in TE transport in bulk materials, they may contribute substantially to the transport in nanostructures$^{40}$ due to their large surface to volume ratio. In fact, electrical transport experiments on $Bi_2Te_3^{24,28,35}$ and $Bi_2Se_2Te^{41}$ nanowires in the 200 - 30 nm diameter range revealed that the two-dimensional TI surface channels contribute up to 30-70 % of the total electrical conduction at surface to volume ratios of $s/v=2-5\cdot 10^{-2}\ nm^{-1}$.

Previous theoretical studies on TE properties of TIs have shown that surface or edge states can in principle enhance the TE performance, for example on two-dimensional TIs with one dimensional edge states,$^{42,43}$ on three-dimensional TIs with line dislocations$^{44}$ as well as on $Bi_2Te_3$ and $Bi_2Se_3$ thin films.$^{45,46}$ These calculations focus on length scales below 10 nm, where hybridization of the topological states, resulting in a gap opening at the Dirac point, is expected to enhance the TE efficiency. Such sub-10 nm TE devices have to date not been realized, in part because of limitations in the template size or disturbances of the delicate equilibrium required in self-organized growth processes.$^{47}$

Recently, it has been found that in two-dimensional TIs $ZT$ is no longer an intrinsic material property but strongly depends on system size just below $10\ \mathrm{\mu m}.^{48}$ Due to its relevance for the material science community and the ongoing development of Bi-Sb-Te-

Se based TE nanostructures we here consider three-dimensional nanowires with diameters above 10 nm at room-temperature. The thermoelectric performance in topological insulators strongly depends on the effective masses, carrier concentrations, bulk band gap and position of the Dirac point. The Fermi level $E_\text{F}$ position is therefore an essential parameter in determining the TE performance of investigated material systems.

Our calculations reveal that with decreasing diameter the thermoelectric transport in chalcogenide TI wires is increasingly dominated by the surface states. Because the TE performances of the bulk and of the surface states are optimized at different Fermi level positions, the maximal achievable $S^2\sigma$ and $ZT$ of TI wires with bulk-optimized carrier concentrations can be significantly reduced at diameters in the sub-10 $\mu$m range, compared to bulk values. Additionally, the model explains the recently found negative Seebeck coefficient in intrinsic $Bi_2Te_3$ nanowires (p-type in bulk).$^{21}$ But even by readjusting the Fermi level for each diameter at the position of maximum TE performance, a significant degradation of the maximum thermoelectric performance in $Bi_2Te_3$ wires for $d < 10$ $\mu$m is observed. In contrast, for $Sb_2Te_3$ and $Bi_2Se_3$ nanowires in this diameter range we find a significantly enhanced $ZT$ compared to bulk, mainly because the total thermal conductivity of the wire $\kappa = \kappa_\text{el} + \kappa_\text{ph}$ converges to the solely electronic thermal conductivity of the surface states $\kappa_\text{s} = \kappa_\text{el,s}$ with decreasing diameter. Moreover, we show that regardless of precise shape or bulk material, the total thermoelectric efficiency of a topological insulator nanostructure with gapless states will eventually converge to the thermoelectric efficiency of the surface with decreasing system size.

## II. MODEL

We have calculated the room temperature thermoelectric transport coefficients $S$, $\sigma$, $\kappa_{el}$ and $ZT = S^2\sigma T/\kappa$ along the longitudinal axis of a single, cylindrical topological insulator nanowire in the diffusive limit as a function of $E_{\text{F}}$ measured relative to the valence band edge. Standard semi-classical Boltzmann equations under constant relaxation time approximation are used, considering two parallel, non-interacting channels as schematically shown in Fig. 1 (a): A three-dimensional semiconducting bulk channel with two parabolic bands (valence and conduction band) separated by a band gap $\Delta E_{\text{b}}$ and a two-dimensional surface channel with electron and hole cones. The investigated nanowire diameters $d$ lie well above the size range, in which confinement effects in the nanowire bulk¹ or hybridization of the surface states⁴⁵,⁴⁹ might entail deviations from our calculation for $\text{Bi}_2\text{Te}_3$, $\text{Sb}_2\text{Te}_3$ as well as for $\text{Bi}_2\text{Se}_3$ at 300 K. The detailed methods for calculating $S$, $\sigma$, $\kappa$ and hence $ZT$ as well as all model parameters—obtained from the literature—of the individual transport channels can be found in the supplementary material.⁶³ For an anisotropic bulk crystal the thermoelectric efficiency $ZT_{\text{b}}$ varies with transport direction, generally determined by the nanowire growth direction, which is expressed in a highly anisotropic effective mass tensor.⁶³ Here, we choose to perform all calculations along the crystal orientation of highest mobility—parallel to the $\text{a}_0$-axis—and therefore along the direction of highest $ZT_{\text{b}}$ to gain maximal bulk contribution in the total thermoelectric transport. Note, that the carrier mobility in nanostructures is generally suppressed compared to bulk values, due to enhanced surface scattering,⁵⁰ which could lead to an overestimation of the bulk contribution to the total electrical transport in our calculations. Bulk $\text{Bi}_2\text{Te}_3$, $\text{Sb}_2\text{Te}_3$, and $\text{Bi}_2\text{Se}_3$ are narrow-band-gap semiconductors with


band gaps of 105 meV, 90 meV, and 300 meV, respectively. The phonon contributions to the thermal conductivity $\kappa_{\text{ph}}$ of the bulk channel were taken from literature and correspond to bulk materials. They do not account for a possible reduction of $\kappa_{\text{ph}}$ in the nanowire e.g. due to enhanced surface scattering or impurities. We have chosen to provide both, the electronic part of the thermoelectric figure of merit $ZT_{\text{el}} = S^2\sigma T/\kappa_{\text{el}}$ as well as $ZT= S^2\sigma T/(\kappa_{\text{el}} + \kappa_{\text{ph}})$ in order to give an upper and lower limit for the actual TE performance of the nanowire bulk channel.

To capture the transport in the surface states of the nanowire, we consider an energy dispersion $E(k)$ that deviates from an ideal linear dispersion $E(k) = \hbar k v_F$ as observed in angle-resolved photoemission spectroscopy (ARPES).$^{32, 33}$ In cylindrical nanowires the energy dispersion relation of the surface states is given by

$$
E(k)=\sqrt{\left(\Delta E_{D P}+\hbar k v_{F}+\frac{\hbar^{2} k^{2}}{2 m^{*}}\right)^{2}+\Delta E_{s}^{2}} \tag{1}
$$

(Fig. 1 (a)), where $\Delta E_{\mathrm{s}}=4 v_{\mathrm{F}} \hbar d^{-1}$ denotes the energy gap around the Dirac point caused by the periodic boundary conditions around the nanowire with diameter $d.^{51} v_{\mathrm{F}}$ is the Fermi velocity of the Dirac particles at the Dirac point and $m^*$ is an effective mass term that accounts for the curvature of $E(k),^{52,53}$ leading to an electron-hole asymmetry of the Dirac cone at higher energies. $^{53} v_{\mathrm{F}}$ and $m^{*}$ have been obtained by fitting $^{61}$ ARPES measurement data $^{32,53}$ for $\Delta E_{\mathrm{s}}=0$. Note that for $E_{\mathrm{F}}-\Delta E_{\mathrm{DP}}>250 \mathrm{meV}$ the local curvature of the surface bands $v(k)=\frac{\partial E}{\partial k} / \hbar$ in $\mathrm{Bi}_{2} \mathrm{Te}_{3}$ becomes anisotropic due to hexagonal warping of the Fermi surface, $^{40}$ which can cause a asymmetry ratio of 0.4 between the transport directions. For all our calculations we fix $v(k)=v_{a_{0}}(k)$ and thus $v_{a_{0}}(0)=v_{F}$.

The position of the Dirac point relative to the bulk valence band edge $\Delta E_{\mathrm{DP}}$ has been

experimentally determined by ARPES as -265 meV for $Bi_2Te_3$, -38 meV for $Sb_2Te_3$ and
145 meV for $Bi_2Se_3$, $^{33}$ exemplary representing materials with the Dirac point deeply
buried in a bulk band ($Bi_2Te_3$), at the band edge ($Sb_2Te_3$) and the center of the band gap
($Bi_2Se_3$).

When calculating the total thermoelectric properties of a topological insulator, care must
be taken in the qualitative comparison of the surface and bulk contributions because of
the different dimensionality of the channels. The total electrical conductivity of a
topological insulator is given by

$$
\sigma=\left(G_{\mathrm{b}}+G_{\mathrm{s}}\right) \cdot \frac{L}{A}=\sigma_{\mathrm{b}}+\sigma_{\mathrm{s}} \frac{s}{v}. \tag{2}
$$

$G_{\mathrm{b}}$ and $G_{\mathrm{s}}$ are the electrical conductances of the bulk and the surface channel,
respectively; $L$ denotes the length of the nanowire; $A$ its cross-sectional area and $s/v$ its
surface-to-volume ratio. Of a (cylindrical) nanowire with diameter $d$ the surface-to-
volume ratio accounts to $\frac{s}{v}=\frac{4}{d}$. The total Seebeck coefficient $S$ of a topological insulator
nanowire can straightforwardly be calculated within the two-channel model $^{12}$ as

$$
S=\frac{S_{b} \sigma_{\mathrm{b}}+S_{\mathrm{s}} \sigma_{\mathrm{s}} \frac{s}{v}}{\sigma_{\mathrm{b}}+\sigma_{\mathrm{s}} \frac{s}{v}} \tag{3}
$$

$S_{\mathrm{b}}$ and $S_{\mathrm{s}}$ are the thermopowers of the bulk and the surface channel, respectively. The
total electronic part of the thermal conductivity $^{12}$ is calculated using

$$
\kappa_{\mathrm{el}}=\kappa_{\mathrm{el}, \mathrm{b}}+\kappa_{\mathrm{el}, \mathrm{s}} \frac{s}{v}+\frac{\sigma_{\mathrm{b}} \cdot \sigma_{\mathrm{s}} \frac{s}{v}}{\sigma_{\mathrm{b}}+\sigma_{\mathrm{s}} \frac{s}{v}}\left(S_{\mathrm{s}}-S_{\mathrm{b}}\right)^{2} T. \tag{4}
$$

$\kappa_{\mathrm{el}}$ consists of the individual electronic thermal conductivity of the bulk $\kappa_{\mathrm{el}, \mathrm{b}}$ and of the
surface channel $\kappa_{\mathrm{el}, \mathrm{s}}$ as well as of an additional diffusion term that is enabled by the two
different Seebeck coefficients of the surface states and of the bulk. $^{12}$ Note that the total
Seebeck coefficient as well as the ratio of the electrical and thermal conductivity of a two

8

channel system will never be larger than the maximum value of the individual channels.⁶³

The TE efficiency of the bulk or surface states will therefore pose the limit of the TE efficiency of the total nanostructure.

## III. RESULTS
The TE transport coefficients of the single bulk channels behave as expected from literature. Their thermoelectric figures of merit $ZT_\text{b}(E_\text{F})$ (Fig. 1(b)) as a function of Fermi level reveal the characteristic double-peak structure of a two-band material, resulting from the line shape of the Seebeck coefficient $S_b(E_\text{F})$ (Fig. 1(c)) weighted by the $\sigma/\kappa$-ratios (Fig. 1(d),(e)). The asymmetry in $ZT_\text{b}(E_\text{F})$ is caused by the different effective masses of the bulk valence and conductance bands. We obtain maximum bulk thermoelectric figures of merit of $ZT_\text{b}(E_\text{F,opt,b} = 155\ \text{meV}) = 0.84$ for n-type $\text{Bi}_2\text{Te}_3$, $ZT_\text{b}(E_\text{F,opt,b} = \text{-54 meV}) = 0.17$ for p-type $\text{Sb}_2\text{Te}_3$, and $ZT_\text{b}(E_\text{F,opt,b} = 361\ \text{meV}) = 0.06$ for n-type $\text{Bi}_2\text{Se}_3$ at 300 K for optimal Fermi level positions $E_\text{F,opt,b}$, corresponding to bulk carrier concentrations of $n_\text{e} = 1.11 \cdot 10^{20}\ \text{cm}^{-3}$, $n_\text{p} = 1.28 \cdot 10^{19}\ \text{cm}^{-3}$ and $n_\text{e} = 4.36 \cdot 10^{18}\ \text{cm}^{-3}$, respectively. These values are in good agreement with literature.¹² Small deviations might occur due to slightly varying bulk parameters in literature. At the surface of thick wires ($\text{d} > 1\ \mu\text{m}$) the Dirac cone is quasi-gapless ($\Delta E_\text{s} < 1\ \text{meV}$) and generates two $ZT$ peaks that are shaped by the asymmetric Dirac cones. We obtain maximum surface TE efficiencies of $ZT_\text{s}(E_\text{F,opt,s} = \text{-257 meV}) = 0.49$ in $\text{Bi}_2\text{Te}_3$, $ZT_\text{s}(E_\text{F,opt,s} = \text{-42 meV}) = 0.25$ in $\text{Sb}_2\text{Te}_3$ and $ZT_\text{s}(E_\text{F,opt,s} = 132\ \text{meV}) = 0.47$ in $\text{Bi}_2\text{Se}_3$, corresponding to carrier concentrations of about about $n_\text{e/p} = 2 \cdot 10^{12}\ \text{cm}^{-2}$. This situation covers TIs with gapless surface states in general. For diameters below $1\ \mu\text{m}$ $\Delta E_\text{s}$ becomes noticeable in our

transport calculations. The maximum $ZT_{\text{s}}$ increases with decreasing nanowire diameter up to $ZT_{\text{s}}(E_{\text{F,opt,s}} = \text{-286 meV}) = 0.91$ in $\text{Bi}_2\text{Te}_3$, $ZT_{\text{s}}(E_{\text{F,opt,s}} = \text{-57 meV}) = 0.58$ for the hole cone in $\text{Sb}_2\text{Te}_3$ and $ZT_{\text{s}}(E_{\text{F,opt,s}} = 132\text{ meV}) = 0.87$ for the electron cone in $\text{Bi}_2\text{Se}_3$ at $d = 10$ nm. We note that the distance between the Fermi level position of the maximum $ZT_{\text{s}}$ and the Dirac point is smaller than $k_{\text{B}}T$. This is a consequence of the asymmetry of the Dirac cone. For an ideal, linear and symmetric cone the optimum $E_{\text{F}}$ would be around $k_{\text{B}}T$ off the Dirac point.

Combining surface and bulk channels, we find that the total thermoelectric properties of topological insulator $\text{Bi}_2\text{Te}_3$, $\text{Sb}_2\text{Te}_3$ and $\text{Bi}_2\text{Se}_3$ wires are increasingly dominated by the surface states with decreasing diameter, as a simple consequence of enhancing surface to volume ratio. If the wire diameter is reduced below the $10$ $\mu\text{m}$ range, the competition between surface states and bulk channel causes a significant reshaping of the whole energy dependence of each individual transport coefficient as shown in Fig. 2. While the total electric (Fig. 2 (b),(g),(i)) and thermal conductivity (Fig. 2 (c),(h),(m)) continuously increase as the system-size is decreased, due to the increasing influence of the surface states, the change of the thermopower (Fig. 2 (a),(f),(k)) depends on the Fermi level, increasing or decreasing with declining nanowire diameter. A reduction of the total Seebeck coefficient has been observed in various experiments on Bi-Sb-Te-Se based nanostructures such as nanowires$^{19-23}$ and thin films.$^{54-56}$ For $\text{Bi}_2\text{Te}_3$ the transformation of the energy landscape has an additional crucial impact: Below a nanowire diameter of about 200 nm, the thermopower becomes of negative sign for Fermi levels within the bulk valence band, because the Dirac point on the surface of $\text{Bi}_2\text{Te}_3$ is located in the bulk valence band leading to a bipolar competition between electrons on the surface (negative

Seebeck coeffcicient) and holes in the bulk (positive Seebeck coefficient). This finding possibly explains recent thermal $^{21}$ and magnetotransport measurements $^{24}$ on $Bi_2Te_3$ nanowires, wherein a negative thermopower has been determined at Fermi levels deeply buried in the bulk valence band. The relative contribution of the surface states to the total electrical conductivity ($Bi_2Te_3$: 15% for $d = 100$ nm at $E_F = -205$ meV) are in reasonably good agreement with experimental data. $^{24, 28, 35}$ The herein presented calculations are done for single-crystalline nanostructures with perfect surfaces and there are several possible reasons for why the relative contributions of the electronic thermal and electric conductivity could deviate in experiments: On the one hand, imperfections at the surface of the nanowire could lead to a lower mean free path than assumed in our model or different dominating scattering mechanisms might entail longer relaxation times in the surface channel. $^{48}$ On the other hand, additional scattering mechanisms in the bulk channel due to grain boundaries or surface roughness are known to decrease its electrical and thermal conductivity. $^{8-11}$ Because all listed effects would result in an overall reduction of the total electrical and thermal conductivity of the topological insulator nanowire, an increasing electrical and thermal conductivity with decreasing nanowire diameter seems to be a strong indication for topological surface states.

We now discuss the common experimental strategy to obtain the predicted high thermoelectric performances in nanowires by downscaling bulk material with carrier concentrations optimized for highest bulk $ZT_b^{13-15}$ in order to retain the high $ZT_{el}$ and benefit from the suppression of $k_{ph}$. In our calculation this experimental strategy is similar to a reduction of the nanowire diameter, fixing the Fermi level at the value that yields the highest bulk $ZT\ E_{F,opt.b.}^{63}$ At 10 nm nanowire diameter we obtain $ZT_{el}(E_{F,opt.b} = -155$ meV)

$= 0.01$ for a n-type $Bi_2Te_3$, $ZT_{\text{el}}(E_{\text{F,opt,b}} = -54$ meV$) = 0.42$ for a p-type $Sb_2Te_3$ and $ZT_{\text{el}}(E_{\text{F,opt,b}} = 361$ meV$) = 0.04$ for a n-type $Bi_2Se_3$. Analogous system-size dependencies are observed in the case of full phonon contribution. $ZT(E_{\text{F,opt,b}})$ converges to similar values as $ZT_{\text{el}}(E_{\text{F,opt,b}})$ at 10 nm diameter. Because the increasing electrical conductivity is compensated by the likewise increase of the thermal conductivity, the thermoelectric efficiency is dominated by $S$. The results reflect the overall experimental observations very well. A more detailed comparison of theory and experiment requires diameter dependent thermoelectric transport studies on nanowires at fixed Fermi levels. Such a study is available for $S$ and $\sigma$ of $Sb_2Te_3$ nanowires, $^{57}$ where an increase in $S$ from $S < 90$ $\mu$V/K at $d = 100$ nm to $S \approx 110$ $\mu$V/K at $d = 20$ nm was observed, which compares well with our findings (see Fig. 3 in the supplementary material$^{63}$). Our results show that such an increase can be caused by the increasing influence of the surface states, even when size quantization remains irrelevant. While $ZT_{\text{el}}(E_{\text{F,opt,b}})$ and $ZT(E_{\text{F,opt,b}})$ for $Bi_2Te_3$ and $Bi_2Se_3$ nanowires are supressed, because the TE performance of the nanowire bulk and surface are optimized at different Fermi levels, $ZT_{\text{el}}(E_{\text{F,opt,b}})$ and $ZT(E_{\text{F,opt,b}})$ of $Sb_2Te_3$ is slightly enhanced compared to $ZT_{\text{b}}(E_{\text{F,opt,b}})$. However, in comparison to their electronic bulk counterparts, $ZT_{\text{el}}(E_{\text{F,opt,b}})$ of wires with diameters in the nanometer range is strongly suppressed for all materials investigated.

The question thus arises whether topological insulator nanowires can reach bulk $ZT_{\text{el}}$ at all to benefit from the $\kappa_{ph}$ suppression for improving the total TE performance? The remarkable suppression of the electronic thermoelectric efficiency in nanometer-scaled optimized bulk materials can be attributed to two main features: first, to a narrowing of the $ZT$-peaks as the system size is reduced; and second, to a Fermi level-shift of the

efficiency maximum. Both effects warrant a very accurate repositioning of the Fermi level at each nanowire diameter to maximize the thermoelectric performance at the specific system size. Tuning the Fermi level (i.e. the carrier concentration) via field effect or doping has recently turned out to provide a powerful experimental tool to achieve maximum thermoelectric performance in semiconducting nanostructures. $^{4,58,59}$ Following this route, we extract the maximum $ZT$ and $ZT_{\text{el}}$ at the optimized Fermi level positions $E_{\text{F,opt}}$ for each nanowire diameter as shown in Fig. 3 (a) and (b). For all materials investigated, a non-monotonic relation between TE efficiency and system size is obtained. A minimum splits the $ZT$ and $ZT_{\text{el}}$ curves into two distinct size ranges marking the crossover between surface state dominated transport in smaller systems and bulk dominated transport in larger systems. The $ZT_{\text{el}}$ curves are shaped by the thermopower at $E_{\text{F,opt}}$ evolving from competing $S_{\text{S}}$ and $S_{\text{b}}$. The dependence of $ZT$ on the system size follows the same arguments as $ZT_{\text{el}}$, but the bulk channel is additionally weighted by $\kappa_{\text{ph}}$. $\kappa_{\text{ph}}$ results in a suppression of $ZT_{\text{b}}$ as well as in an overall suppression of the total nanowire efficiencies $ZT$ compared to $ZT_{\text{el}}$. This demonstrates that phonons still play a noticeable role in thermoelectric transport, even if topological surface states dominate the electronic transport properties of the nanowire.

We find that nanoscaling $\text{Bi}_2\text{Te}_3$ wires leads to a decrease of the maximum $ZT$ compared to bulk (by a factor three at $d=10$ nm). In contrast, the maximum $ZT$ for $\text{Sb}_2\text{Te}_3$ and $\text{Bi}_2\text{Se}_3$ is increased (by a factor of ten [three] for $\text{Sb}_2\text{Te}_3$ [$\text{Bi}_2\text{Se}_3$] at $d=10$ nm). In all nanowire systems investigated the maximum $ZT_{\text{el}}$ is at least one order of magnitude suppressed compared to their bulk counterparts (at $d=10$ nm), because the total maximum TE performances of the topological insulator nanowires converge towards the

maximum TE performance of the surface states with decreasing diameter (the increase in
$ZT$ for $Sb_2Te_3$ and $Bi_2Se_3$ at small diameters occurs mainly because the contribution of
phonon thermal conductivity in the nanowire bulk becomes small compared to the solely
electronic thermal conductivity contribution of the surface states, not because the surface
states have a very high $ZT_{el}$). Similar findings are obtained for topological insulators with
gapless surface states. Exemplary calculations for gapless Dirac cone systems on thin
films are shown in Fig. 3 (d) and (e).

## IV. DISCUSSION

Summing up, in the presence of surface states, the total thermoelectric efficiency of a
topological insulator nanostructure will eventually converge to the thermoelectric
efficiency of the surface states with decreasing system size, regardless of precise shape or
bulk material. However, the details of this process depend on the surface to volume ratio
of the nanostructure, on $ZT_b$, on the relaxation time of the surface states as well as on the
relative position of the Dirac point to the bulk band structure. Topological insulator
nanostructures could therefore, on one hand be a chance to enhance the thermoelectric
performance of materials with $ZT_b < ZT_s$ and on the other hand pose a limit to the
thermoelectric performance of materials with $ZT_b > ZT_s$. Nevertheless, the maximum TE
surface efficiencies $ZT_s \approx 0.5$ ($Bi_2Te_3$) of gapless surface states and $ZT_s \approx 0.9$ ($Bi_2Te_3$)
on the surface of cylindrical nanowires (at 10 nm diameter) do not exceed the highest
room-temperature bulk TE efficiencies to date and are far below the electronic room-
temperature bulk TE efficiencies. A reduction of $\kappa_{ph}$ does not lead to an enhancement of
the TE efficiency of topological insulator nanostructures beyond best bulk efficiencies

($ZT \approx 1$) to date. Important for future room temperature TE applications will therefore be the suppression of the topological surface states. The implementation of magnetic impurities on the surface of a topological insulator is known to break time reversal symmetry and thus to introduce a backscattering channel accompanied with a gap opening at the Dirac point. $^{60, 61}$ In addition, recent calculations predict that the hybridization gap formed in ultrathin topological insulators with system sizes below 10 nm may provide a chance to improve their thermoelectric properties far beyond $ZT=1.^{42-}$

$^{46}$ Topological insulator nanowires with diameters below 10 nm could hence be of high interest because hybridization of the surface states as well as quantum confinement in the bulk is proposed to significantly enhance the thermoelectric performance of each individual transport channel. However, in the diameter range experimentally achievable to date ($d > 10$ nm), the presence of surface states limits the thermoelectric efficiency of topological insulator nanowires and thus their application in efficient thermoelectric devices. In this size range, alternative concepts utilizing confinement effects in nanometer-scaled non-conventional good bulk thermoelectric materials, such as in InAs, $^{4}$ ZnO and $GaN^{62}$ nanowires as well as in Ge-Si core-shell nanowires $^{58}$ might pave the way to future TE application.

# ACKNOLEDGEMENTS

We thank Ulrich Merkt and Toru Matsuyama for useful discussions. This work was supported by the Deutsche Forschungsgemeinschaft (DFG) via Graduiertenkolleg 1286 "Functional Metal-Semiconductor Hybrid Systems", Project NI-616/18-1 and SPP 1666 "Topological insulators: Materials – Fundamental Properties – Devices", by the Swedish Energy Agency (project 38331-19) as well as by the Swedish Foundation for Strategic Research.

# REFERENCES

[1] L. D. Hicks and M. S. Dresselhaus, *Phys. Rev. B* **47**, 16631 (1993).

[2] N. Mingo, *Appl. Phys.Lett.* **84**, 2652 (2004).

[3] J. E. Cornett and O. Rabin, *Appl. Phys.Lett.* **98**, 182104 (2011).

[4] P. M. Wu *et al.*, *Nano Lett.* **13**, 4080 (2013).

[5] N. Neophytou and H. Kosina, *Phys. Rev. B* **83**, 245305 (2011).

[6] N. Nakpathomkun, H. Q. Xu, and H. Linke, *Phys. Rev. B* **82**, 235428 (2010).

[7] J. E. Cornett and O. Rabin, *Phys. Rev. B* **84**, 205410 (2011).

[8] A. I. Hochbaum *et al.*, *Nature* **451**, 163 (2008).

[9] A. I. Boukai *et al.*, *Nature* **451**, 168 (2008).

[10] F. Zhou *et al.*, *Phys. Rev. B* **83**, 205416 (2011).

[11] K. Nielsch, J. Bachmann, J. Kimling, and H. Boettner, *Adv. Energ. Mat.* **1**, 713 (2011).

[12] G. S. Nolas, J. Sharp, and H. J. Goldsmid, *Thermoeletries* (Springer-Verlag: Berlin Heidelberg, Germany, 2001).

[13] G. Chen, M. S. Dresselhaus, G. Dresselhaus, J. P. Fleurial, and T. Caillat, Intern. Mat. Rev. 48, 45 (2003).

[14] M. S. Dresselhaus et al., Adv. Mat. 19, 1043 (2007).

[15] E. Pop, Nano Res. 3, 147 (2010).

[16] M. Munoz Rojo et al., J. of Appl. Phys. 113, 054308 (2013).

[17] G. D. Li, D. Liang, R. L. J. Qiu, and X. P. A. Gao, Appl. Phys. Lett. 102, 043104 (2013).

[18] D. Bessas et al., Nanoscale 5 10629 (2013).

[19] J. H. Zhou, C. G. Jin, J. H. Seol, X. G. Li and L. Shi, Appl. Phys. Lett. 87, 133109 (2005).

[20] A. Mavrokefalos et al., J.of Appl. Phys. 105, 104318 (2009).

[21] B. Hamdou et al., Adv. Mat. 25, 239 (2013).

[22] A. Purkayastha, F. Lupo, S. Kim, T. Borca-Tasciuc and G. Ramanath, Adv.Mat. 18, 496 (2006).

[23] S. Baessler et al., Nanotechn. 24, 495402 (2013).

[24] B. Hamdou, J. Gooth, A. Dorn, E. Pippel, and K. Nielsch, Appl. Phys. Lett. 103, 193107 (2013).

[25] S. Matsuo et al., Phys. Rev. B 85, 075440 (2012).

[26] J. J. Cha et al., Nano Lett. 12, 1107 (2012).

[27] F. Xiu et al., Nature Nanotechn. 6, 216 (2012).

[28] M. Tian et al., Sci. Rep. 3, 1212 (2013).

[29] B. Hamdou, J. Gooth, A. Dorn, E. Pippel, and K. Nielsch, Appl. Phys. Lett. 102, 223110 (2013).

[30] H. Peng, *et al.*, *Nature Mat.* **9**, 225 (2010).

[31] Y. L. Chen *et al.*, *Science* **325**, 178 (2009).

[32] D. Hsieh *et al.*, *Phys. Rev. Lett.* **103**, 146401 (2009).

[33] H. Zhang *et al.*, *Nature Phys.* **5**, 438 (2009).

[34] G. Q. Zhang, Q. X. Yu, W. Wang, and X. G. Li, *Adv. Mat.* **22**, 1959 (2010).

[35] Y. Xia *et al.*, *Nature Phys.* **5**, 398 (2009).

[36] H. Steinberg, D. R. Gardner, Y. S. Lee and P. Jarillo-Herrero, *Nano Lett.* **10**, 5032 (2010).

[37] S. S. Hong, J. J. Cha, D. Kong and Y. Cui, *Nature Comm.* **3**, 757 (2010).

[38] D. Kong *et al.*, *Nano Lett.* **10**, 329 (2010).

[39] J. Gooth, B. Hamdou, A. Dorn, R. Zierold, and K. Nielsch, *Appl. Phys. Lett.* **104**, 43115 (2014)

[40] F. Rittweger, N. F. Hinsche, P. Zahn and I. Mertig, *Phys. Rev. B* **89**, 035439 (2014).

[41] L. Bao *et al.*, *Sci. Rep.* **2**, 726 (2012).

[42] R. Takahashi and S. Murakami, *Phys. Rev. B* **81**, 161302 (2010).

[43] R. Takahashi and S. Murakami, *Sem. Sci. and Techn.* **27**, 124005 (2012).

[44] O. A. Tretiakov, A. Abanov, S. Murakami, and J. Sinova, *Appl. Phys. Lett.* **97**, 073108 (2010).

[45] P. Ghaemi, R. S. K. Mong, and J. E. Moore, *Phys. Rev. Lett.* **105**, 166603 (2010).

[46] Y.S. Hor *et al.*, *Phys.Rev. B* **79**, 195208 (2009).

[47] L. Cademartiri and G. A. Ozin, *Adv. Mat.* **21**, 1013 (2009).

[48] Y. Xu, Z. Gan, and S.-C. Zhang, S.-C. *Physical Review Letters* **112**, 226801 (2014).

[49] Y. Jiang *et al.*, *Phys. Rev. Lett.* **108**, 016401 (2012).

[50] E. H Sondheimer, *Adv. in Phys.* **1**, 1 (1952).

[51] A. Cook, and M. Franz, *M. Phys. Rev. B* **84**, 201105 (2011).

[52] A. A. Taskin, and Y. Ando, *Phys. Rev. B* **84**, 035301 (2011).

[53] A. A. Taskin, Z. Ren, S. Sasaki, K. Segawa, and Y. Ando, *Phys. Rev. Lett.***107**, 016801 (2011).

[54] N. Peranio, O. Eibl, and J. Nurnus, *J. of Appl. Phys.* **100**, 114306 (2006).

[55] S. Zastrow *et al.*, *Semicon. Sci. and Techn.* **28**, 035010 (2013).

[56] A. Boulouz *et al.*, *J. of Appl. Phys.* **89**, 5009 (2001).

[57] Zuev, Y. M.; Lee, J. S.; Galloy, C.; Park, H.; Kim, P. *Nano Letters* **2010**, 10, 3037–3040.

[58] J. Moon, J.-H. Kim, Z. C. Y. Chen, J. Xiang, and R. Chen, *Nano Lett.* **13**, 1196 (2013).

[59] S. Roddaro *et al.*, *Nano Lett.* **13**, 3638 (2013).

[60] H. T. He *et al.*, *Phys. Rev. Lett.* **106**, 166805 (2011).

[61] Q. Liu, C.-X. Liu, C. Xu, X.-L. Qi and S.-C.Zhang, *Phys. Rev. Lett.* **102**, 156603 (2009).

[62] C.-H. Lee, G.-C. Yi, Y. M. Zuev and P. Kim, *Appl. Phys. Lett.* **94**, 022106 (2009).

[63] See supplementary material for calculation details and parameters.

![](./images/867758238253187263_1.jpg)

FIG 1. Thermoelectric transport coefficients of the bulk (left) and of the surface (right) channel of cylindrical topological insulator $Bi_2Te_3$ (blue), $Sb_2Te_3$ (red) and $Bi_2Se_3$ (green). Bulk and surface channel correspond to the subscripts b and s respectively. (a) The three-dimensional bulk channel is a two-band semiconductor with parabolic dispersion relation, where the two bands (valence (VB) and conduction band (CB)) are

separated by a bandgap $\Delta E_{\rm b}$. The transport parameters of the bulk are independent of the nanowire diameter $d$. The two-dimensional surface channel is characterized by a Dirac cone with electron states (e⁻) on one side of the Dirac point and hole states (p⁺) on the other. Angular momentum states around the nanowire perimeter cause a gap $\Delta E_{\rm s} \approx 4v_{\rm F}\hbar d^{-1}$ around the Dirac point. $\Delta E_{\rm DP}$ is the distance between the Dirac point and the bulk valence band edge. (b), (f) The thermoelectric figure of merit $ZT$, (c), (g) the thermopower $S$ as well as the (d), (h) electrical $\sigma$ and (e), (i) thermal conductivity $\kappa$ of both channels are calculated as a function of the Fermi level $E_{\rm F}$, measured relative to the bulk valence band edge.

![](./images/867758238253187263_2.jpg)

FIG 2. Diameter-dependent thermoelectric transport coefficients of topological insulator
$Bi_2Te_3$, $Sb_2Te_3$ and $Bi_2Se_3$ nanowires (from left to right column). (a), (g), (m)
thermopower $S$; (b),(h),(n) electrical conductivity $\sigma$; (c), (i), (o) thermal conductivity $\kappa$;
(d), (j), (p) electronic figure of merit $ZT_{el}$ and (e), (k), (q) thermoelectric figure of merit
with full phonon contribution $ZT$ at 300 K are plotted as a function of Fermi level,
relative to the bulk valence band edge ($E_F = 0$ eV). (f), (l), (r) $ZT$ is plotted as function of

diameter and Fermi level $E_{\text{F}}$ in a two-dimensional color plot. When the wire diameter is reduced the competition between surface states and bulk channel causes a significant reshaping of the whole energy dependence of each individual transport coefficient, because nanowire bulk and surface have different Fermi level dependencies and with decreasing wire diameter the thermoelectric transport is increasingly dominated by the surface states as a simple consequence of increasing surface to volume ratio.

![](./images/867758238253187263_3.jpg)

FIG 3. Maximum electronic thermoelectric figure of merit $ZT_{\rm el}(E_{\rm F,opt}) = S^2\sigma/\kappa_{\rm el}$ and maximum thermoelectric figure of merit $ZT(E_{\rm F,opt}) = S^2\sigma/(\kappa_{\rm el+}\kappa_{\rm ph})$ at optimized Fermi level position $E_{\rm F,opt}$ of a topological insulator $Bi_2Te_3$ (blue), $Sb_2Te_3$ (red) and $Bi_2Se_3$ (green) nanowire (left) and thin film (right) as a function of diameter and thickness, respectively. The dotted lines show the maximum $ZT$ of the single surface states. Regardless of precise shape or bulk material, the total thermoelectric efficiency of a topological insulator nanostructure with gapless surface states will eventually converge to the thermoelectric efficiency of the surface with decreasing system size.