# Dielectric control of ultrafast carrier dynamics and transport in graphene

Hai I. Wang, $^{1,2, *}$ Xiaoyu Jia, $^{1}$ Anand Nivedan, $^{3}$ Mischa Bonn, $^{1}$ Aron W. Cummings, $^{3}$ Alessandro Principi, $^{4}$ and Klaas-Jan Tielrooij$^{5,3,*}$

$^{1}$Max Planck Institute for Polymer Research,
Ackermannweg 10, Mainz, 55128, Germany

$^{2}$Debye Institute for Nanomaterials Science, Utrecht University,
Princetonplein 1, Utrecht, 3584, The Netherlands

$^{3}$Catalan Institute of Nanoscience and Nanotechnology (ICN2),
CSIC and BIST, Campus UAB, Bellaterra, 08193, Barcelona, Spain

$^{4}$School of Physics and Astronomy, University of Manchester, UK

$^{5}$Department of Applied Physics, TU Eindhoven,
Den Dolech 2, Eindhoven, 5612 AZ, Netherlands

## Abstract

Understanding the ultrafast dynamics of photoexcited charges in graphene is essential, as the microscopic mechanisms underlying these dynamics determine many of graphene's optical, optothermal, and optoelectronic properties. These are crucial properties for many functionalities and devices enabled by graphene, such as high-speed photodectors. Therefore, beyond scientific understanding, it is highly desirable to control ultrafast carrier dynamics for practical applications. Here, we establish this control by engineering the dielectric environment of graphene, thereby regulating both heating and cooling dynamics without altering the Fermi energy, optical power, or ambient temperature. By combining optical pump – terahertz probe experiments with theoretical calculations, we show that dielectric screening suppresses carrier-carrier interactions and slows the dynamics. In particular, reduced carrier-carrier scattering delays the formation of a quasi-equilibrium hot electron distribution, thus slowing carrier heating. It also slows carrier cooling because re-thermalization after optical-phonon emission depends on the same interactions. The enhanced screening further reduces the energy of electron-hole puddles, thereby increasing charge mobility and the Seebeck coefficient. This ability to externally control internal graphene dynamics and transport properties enables the optimization of device performance, such as the sensitivity of photodetectors for data communication and wireless communication applications.

---
$^*$Electronic address: k.j.tielrooij@tue.nl, h.wang5@uu.nl

### Introduction

The optoelectronic properties of graphene enable many exciting functionalities and devices, such as ultrafast photodetectors and receivers that operate from the visible through the telecom up to the (sub)terahertz regime [1–11], nonlinear optical converters [12–14], saturable absorbers for lasers [15–17], and light emitters [18–20]. The ultrafast dynamics of photoexcited carriers in graphene have therefore been studied in depth, and are relatively well understood [21]. First, the initially photoexcited carriers undergo thermalization via electron-electron interactions, which leads to a hot electron distribution with an electron temperature that is larger than the lattice temperature. The second step is electron cooling via electron-phonon thermalization. The first step – electron heating – takes a few tens of femtoseconds [22–24], depending on the excitation wavelength, excitation power density, and Fermi energy [25, 26]. The second step – electron cooling – occurs on a picosecond timescale at room temperature. Electron-phonon cooling can involve strongly coupled optical phonons [27, 28] optical-to-acoustic phonon cooling [29, 30], disorder-assisted coupling to acoustic phonons [31, 32], or direct coupling between hot electrons and substrate phonons, for example to hyperbolic phonon polaritons in hBN [33, 34] or to molecular modes in water [35]. In the absence of a substrate that acts as an efficient heat sink for hot electrons, and in the case of relatively high charge mobility, cooling is ultimately dominated by a continuous process of optical phonon emission and electron re-thermalization that leads to secondary hot electrons with enough energy to emit optical phonons [36].

Several cooling mechanisms have some degree of tunability, because they depend – to some extent – on the Fermi energy, which can be controlled electrically [34, 37, 38]. Moreover, the cooling dynamics can be influenced by the incident optical power due to an optical-to-acoustic phonon bottleneck that leads to reheating of the electron system by phonons [29, 36]. Finally, the cooling dynamics depend on the ambient temperature: at cryogenic temperatures, diffusive cooling, where electronic heat diffuses out of the heated region, can become dominant, in particular for micrometer-scale heated areas, because electron-phonon cooling channels become less efficient at reduced temperatures [39, 40]. For many applications, it would be beneficial to have a way to control both the cooling and heating dynamics without changing the Fermi energy, optical power, and ambient temperature. It would be particularly useful to increase the hot-carrier cooling time, as this would lead to a larger photoresponse and therefore a higher sensitivity of photo-thermoelectric devices. However, such a mechanism for controlling carrier dynamics is currently unavailable, as the only strategy appears to be modifying the intrinsic optical and acoustic phonon properties of graphene.

Here, we demonstrate the controllability of the photoexcited carrier dynamics of monolayer graphene using dielectric engineering, without modifying any phonon properties. The mechanism we identified acts on the thermalization process for heating dynamics and the re-thermalization process for cooling dynamics. Specifically, by engineering the dielectric environment, we control the screening of electron-electron interactions [41], which in turn governs the (re-)thermalization dynamics. Employing optical pump – terahertz (THz) probe measurements, we experimentally demonstrate slower heating and cooling dynamics due to increased screening, as induced by liquid superstrates with varying dielectric constants (see Fig. 1a). We developed a theoretical model that describes the effect

![](./images/1246410946033745939_1.jpg)

FIG. 1: Experimental observation of slower photoexcited carrier dynamics controlled by the dielectric environment. a, Illustration of the experimental approach, where graphene inside a modified silica flow cell is surrounded by different dielectric environments with static dielectric constant $\epsilon$ (in green), in particular nitrogen gas, toluene, 1-hexanol, acetophenone, and isopropanol (IPA), see chemical structures on the top left. Time-resolved optical pump - THz probe measurements provide access to the ultrafast carrier dynamics, as shown on the right. b, The pump-induced change in THz transmission $\Delta T/T_0$ as a function of pump-probe delay time $\Delta t$ for nitrogen ($\epsilon = 1$) and IPA ($\epsilon = 19.7$) environments, showing a markedly slower rise and slower decay for the IPA case. c, The photoexcited carrier dynamics for the different environments, with the dashed line indicating the delay time where the peak signal occurs. The results show a gradual slowing of the photoexcited carrier dynamics – both heating and cooling – as the dielectric constant of the environment increases. d, Peak THz transmission as a function of pump fluence for the different dielectric environments, showing a lower signal and faster saturation for larger dielectric constants.

of screening on photoexcitation dynamics and confirms the experimentally observed trends. We also calculated the effect of screening on the electronic and thermoelectric properties of graphene, finding that the charge mobility and Seebeck coefficient increase with stronger screening. Finally, we demonstrate that these effects predict an increase in sensitivity for photo-thermoelectric photodetectors.

### Results

#### Experimental signatures of dielectric control of ultrafast carrier dynamics

We studied ultrafast photoexcited carrier dynamics of large-area graphene, which was grown by chemical vapour deposition (CVD) and transferred onto a $\mathrm{SiO}_2$ substrate. This substrate served as a detachable window for a liquid flow cell, through which we could flow different liquids that served as a dielectrically controllable superstrate for graphene (see Fig. 1a). This enabled us to conduct time-resolved THz measurements on the same sample location while tuning the liquid dielectric environment. The specific liquids that we used were toluene, 1-hexanol, acetophenone, and isopropanol (IPA), with dielectric constants $\epsilon$ of 2.4, 13.1, 17.4, and 19.7, respectively [42]. We characterized the graphene sample under different dielectric environments using Raman microscopy (see Supp. Figs. S1-S2). Before each measurement, we first measured the dynamics in the absence of solvent under a purged atmosphere of dry nitrogen, corresponding to a dielectric constant of $\sim$1. To monitor the dynamics of photoexcited carriers, we excited graphene using laser pulses with a pulse duration of $\approx$35 fs and a wavelength of 800 nm (photon energy $\hbar\omega=1.55$ eV), and probed the electron system using quasi-single-cycle terahertz (THz) pulses with a photon energy of 1-10 meV. These THz pulses are directly sensitive to the photoexcited charge carriers via their Drude conductivity. Specifically, photo-induced electron heating for graphene with the Fermi energy away from the Dirac point leads to a reduced Drude conductivity, *i.e.* negative photoconductivity, and therefore increased THz transmission [24, 43-45]. Scanning the temporal delay between the optical pump and THz probe pulses using an optical delay line provides access to the ultrafast photoexcited electron dynamics. For more experimental details, see Methods:Experimental details.

Figure 1b shows two exemplary measurements of the pump-induced change in THz transmission as a function of pump-probe delay time $\Delta t$, for the case of a nitrogen environment ($\epsilon=1$) and an IPA environment ($\epsilon=19.7$). The increase in transmission directly after $\Delta t=0$, where the pump and probe pulses overlap, typically corresponds to carrier heating, while the subsequent decay corresponds to carrier cooling. Clearly, both the heating and cooling dynamics are significantly slower for the IPA case. If we systematically increase the dielectric constant using different liquids, we observe a gradual slowing of the heating and cooling dynamics, as shown in Fig. 1c. In addition, the pump-probe signal amplitude decreases for larger dielectric constants, as shown in Fig. 1d (see Supp. Fig. S3 for an overview of the experimental data). Our Raman measurements show that the different environments do not lead to drastic changes in carrier density (see Supp. Figs. S1-S2). Moreover, slower dynamics would imply a larger Fermi energy [38], which would, in turn, lead to a larger pump-probe signal. In contrast, we observed a reduced pump-probe signal combined with slower dynamics. Therefore, we conclude that the observed changes in the photoexcited carrier dynamics and the pump-probe signal are not due to a shift in the Fermi energy.


# Tuning ultrafast carrier dynamics through dielectric screening

We hypothesize that dielectric environments affect carrier dynamics by screening electron-electron interactions. The idea is that environments with a higher dielectric constant lead to increased screening of electron-electron scattering [41], which in turn affects the photoexcited carrier dynamics. We test this hypothesis using an analytical model that considers the cooling dynamics described in Ref. [36], occurring through a combination of optical phonon emission and carrier re-thermalization via electron-electron scattering. We extended this model to include different dielectric environments (see Supplementary Note 1), focusing on two cases: $\epsilon = 1$ and $\epsilon = 20$. The results shown in Fig. 2a-b demonstrate that a larger dielectric constant indeed gives rise to a slower rise in electron temperature and a slower decay as well, in agreement with the experimental observations. The simulations predict a more pronounced slowing than what we observed in the experiment. One reason is that in the experiment, only the dielectric environment above the graphene changes, whereas the simulation assumes that the entire dielectric environment changes. Furthermore, since the experiment used CVD-grown graphene, cooling can occur via an additional channel: disorder-assisted acoustic phonon emission [31], which sets an upper limit on the cooling time.

In order to understand the pump-induced carrier dynamics in different dielectric environments in more detail, we examine the processes that occur after the absorption of pump light creates initially excited charge carriers, which are additional electrons in the conduction band and additional holes in the valence band at energies $\pm\frac{1}{2}\hbar\omega$, see Fig. 2c. This situation corresponds to a non-thermal distribution at $\Delta t = 0$. In this simulation, we assume that the Fermi energy is located below the Dirac point, meaning that holes are the majority charge carriers. The behaviour would be identical for a Fermi energy above the Dirac point with electrons as majority carriers. Figure 2d shows the evolution of the carrier distribution as a function of time after photoexcitation for the case $\epsilon = 1$. Within several tens of femtoseconds, a thermalized Fermi-Dirac distribution is established, with an elevated carrier temperature. This occurs through a cascade of carrier-carrier interactions starting from the initially photoexcited carriers, which leads to the creation of additional hot carriers (see Fig. 2), [24, 46]. Within several picoseconds, the system relaxes back to equilibrium with an electron temperature equal to the lattice temperature. By describing the carrier distribution with a Fermi-Dirac distribution characterized by a temperature and a chemical potential, we obtain the time-dependent carrier temperature $T$ shown in Fig. 2a. We also obtain the net photo-induced carrier density $\Delta n$ as a function of time, and observe that within a picosecond, there are no net photo-induced charge carriers left in the system, which means that the system is purely characterized by an increased carrier temperature. The photoexcitation dynamics for graphene in an environment with $\epsilon = 1$ are therefore similar to the dynamics of a typical metal, giving a negative photoconductivity and dynamics that reflect the heating-cooling dynamics of the electronic system.

The evolution of the carrier distribution is very different for $\epsilon = 20$. In this case, the carrier distributions are much more non-thermal, as shown in Fig. 2e. Rather than a continuous cascade of carrier-carrier interactions leading to a thermal distribution, there is a significant contribution of optical phonon emission to the relaxation of the initially photoexcited carriers, as illustrated in Fig. 2f. This leads to slower and less efficient

![](./images/1246410946033745939_2.jpg)

FIG. 2: Calculated dielectric tuning of photoexcited carrier dynamics by controlling carrier-carrier interactions. a-b, Calculated photoexcited carrier dynamics in an environment with $\epsilon = 1$ (a) and $\epsilon = 20$ (b), showing the dynamics of the density of photoexcited carriers $\Delta n$ and of the carrier temperature $T$. The latter is obtained by describing the corresponding carrier distributions with Fermi-Dirac statistics.
c, Illustration of the carrier dynamics that occur after optical excitation creates an additional electron in the conduction band and an additional hole in the valence band, for $p$-doped graphene with $\epsilon = 1$. The initially excited carriers relax through carrier-carrier scattering, which creates additional hot carriers, in this case, hot holes with an energy above the Fermi energy. d-e, Snapshots of calculated carrier distributions at several delay times after photoexcitation for $\epsilon = 1$ (d) and $\epsilon = 20$ (e). In the former case, all distributions after $\approx$10 fs are thermalized due to efficient carrier-carrier interactions, whereas in the latter case, they are non-thermal. f, Illustration of the carrier dynamics after photoexcitation for $\epsilon = 20$. In this case, the relaxation of initially excited carriers by the emission of optical phonons plays an important role, since carrier-carrier interactions are screened.

carrier heating. Using a Fermi-Dirac distribution with an "effective" carrier temperature, we obtain the carrier temperature dynamics in Fig. 2b. We observe slower dynamics and a lower temperature for $\epsilon=20$ than for the case of $\epsilon=1$. The lower temperature explains the experimentally observed decrease in pump-probe signal, which scales with the carrier temperature. We also find that the net photo-induced carrier density $\Delta n$ lives significantly longer for $\epsilon=20$. This likely explains the smaller signal magnitude observed in Fig. 1d, because an increased carrier density gives rise to a positive photoconductivity, i.e. a decrease in transient transmission. The photoexcitation dynamics for graphene in an environment with $\epsilon=20$ are therefore more similar to the dynamics of a typical semiconductor. Importantly, the combination of these simulations and our experimental results demonstrate the ability to externally control the cooling dynamics driven by intrinsic electron-phonon interactions in graphene.

## Dielectric tuning of transport properties

Next, we use numerical simulations to examine how altering the dielectric environment can tune the electronic transport properties of graphene. To quantify this, we assume that in graphene on $SiO_2$, charge transport is limited by electron-hole puddles. These arise from charges trapped in the oxide, inducing a spatially varying electrostatic potential in the graphene layer that can dominate charge transport [47, 48]. Scanning tunneling spec- troscopy (STS) measurements have revealed that this potential has a Gaussian distribution with a standard deviation of 50 meV and a length scale of $\sim$10 nm [49, 50].

To simulate charge transport in graphene with disorder on such a length scale, we employ a linear-scaling real-space quantum transport method capable of handling systems with many millions of atoms (see Methods for details) [51]. With this we calculate the Fermi-energy- dependent electrical conductivity, $\sigma(E)$, from which we extract the carrier mobility,

$$
\mu=\frac{1}{e} \frac{\mathrm{d} \sigma}{\mathrm{d} n}, \tag{1}
$$

where $n$ is the carrier density obtained by integrating the density of states. In our simu- lations, we employ a standard nearest-neighbour tight-binding Hamiltonian for graphene, with the puddles modelled as a set of Gaussian electrostatic potentials. To reproduce prior STS measurements of graphene on $SiO_2$, we set the width of each puddle to 10 nm, the height of each puddle is randomly chosen within $[-W,W]$ with $W=50$ meV, and the puddle density is 0.04%.

The puddle height scales inversely with the average dielectric environment, $W=W_0/\epsilon_{\text{avg}}$, where $\epsilon_{\text{avg}}=(\epsilon_{\text{top}}+\epsilon_{\text{bot}})/2$ is the average permittivity of the media above and below the graphene layer [52, 53]. Here, the value of $W_0$ is chosen to correspond to STS measurements of graphene on $SiO_2$ [50]. In our simulations, we consider puddle heights of $W=50,25$, and 10 meV, corresponding to $\epsilon_{\text{top}}=1,5.9$, and 20.6. We also consider larger puddle heights of $W=100,200$, and 400 meV. These latter values correspond to $\epsilon_{\text{top}}=1$, but with the graphene much dirtier.

Figure 3a shows the density-dependent mobility for each puddle height. Reducing the puddle height has a clear impact on charge transport; reducing $W$ from 50 to 10 meV

![](./images/1246410946033745939_3.jpg)
![](./images/1246410946033745939_4.jpg)

FIG. 3: Tuning electronic transport in graphene by modulating the electron-hole puddle height via dielectric screening. a, Carrier mobility as a function of carrier density. b, Seebeck coefficient as a function of Fermi energy, for different puddle heights. Upper right inset: scaling of the mobility with puddle height at $n=10^{12}\ \text{cm}^{-2}$. The dashed line indicates the scaling $\mu\propto1/W^{2}$. Lower left inset: scaling of the maximal value of $S$ with puddle height.

$(\epsilon_{\text{top}}=1\rightarrow20.6)$ increases the mobility by a factor of approximately 25 at high densities, from 10 000 to more than 200 000 $\text{cm}^{2}$/V-s. The upper right inset of Fig. 3b shows how the mobility scales with puddle height at a carrier density of $n=10^{12}\ \text{cm}^{-2}$. The open symbols are numerical data, and the dashed line indicates quadratic scaling, $\mu\propto1/W^{2}$. In a recent experimental work, Domaretskiy and coworkers demonstrated that close proximity $(\approx1\ \text{nm})$ to a graphite gate could reduce electrostatic potential fluctuations in graphene down to below $1\ \text{meV}$, allowing them to measure mobilities reaching above $10^{7}\ \text{cm}^{2}$/V-s [54]. Following the scaling trend we see in the inset, reducing the puddle height down to less than $1\ \text{meV}$ also yields $\mu>10^{7}\ \text{cm}^{2}$/V-s, consistent with their measurements.

Next we examine how the Seebeck coefficient of graphene is altered by dielectric screening. This is calculated from the conductivity as [55]

$$
S(E)=-\frac{1}{eT}\frac{K_{1}(E)}{K_{0}(E)},\tag{2}
$$

where $K_{j}(E)=\int(E-\epsilon)^{j}\sigma(\epsilon)(-\partial f/\partial\epsilon)d\epsilon$, $T=300\ \text{K}$ is the ambient temperature, and $f$ is the Fermi-Dirac distribution. The main panel of Fig. 3b shows the Seebeck coefficient of graphene for each puddle height. As expected, $S$ increases with decreasing puddle height, suggesting that dielectric engineering may be an efficient means of tailoring graphene devices using this effect, such as photodetectors based on the photo-thermoelectric effect [1–11].

The lower left inset shows how the maximum value of $S$ scales with puddle height. Increasing the top dielectric from $\epsilon_{\text{top}}=1\rightarrow20.6$ enhances $S$ by 70%, from 113 to 192 $\mu\text{V}/\text{K}$. Another interesting feature is that $S$ appears to saturate with decreasing puddle height, approaching approximately $200\ \mu\text{V}/\text{K}$. This value is similar to measurements of

graphene on hBN ($S \approx 180\ \mu\text{V/K}$) [56], suggesting an upper achievable value of $S$ in uniform single-layer graphene at room temperature, i.e., in the absence of engineered junctions [57] or hydrodynamic effects at lower temperatures [58].

## Discussion

Using pump-probe measurements of graphene in different liquid environments, we observed systematically slower rise and decay dynamics of photoexcited carriers as the dielectric constant of the liquid increased. We ascribe these observations to the screening effect of the liquids on carrier-carrier interactions in graphene. This screening leads to less efficient carrier heating, as a larger fraction of initially excited carriers relax through phonon emission rather than through carrier-carrier interactions. This means that less energy stays within the electron system. Since carrier-carrier interactions are also crucial for re-thermalization during cooling, increased screening also slows cooling. Moreover, increased screening results in a longer persistence of net photoexcited charge carriers in graphene. In addition to controlling carrier dynamics, screening also affects electronic and thermoelectric properties, as we showed through linear-scaling quantum transport simulations. In particular, increased screening leads to charge mobilities above $10^7\ \text{cm}^2/\text{V-s}$ and Seebeck coefficients up to $200\ \mu\text{V/K}$.

These results are of fundamental interest because they offer an external mechanism for control of intrinsic graphene dynamics and transport, which govern its optoelectronic, elec- tronic, and thermoelectric properties. The ability to control these properties is also promis- ing for applications such as photo-thermoelectric photodetectors. Considering a simple pho- todetector with a rectangular geometry containing a graphene channel and two contacts on either side of the channel, where a $pn$-junction is created, the photocurrent is given by [9, 21, 34]

$$
I_{\mathrm{PTE}} = \frac{(S_1 - S_2)\Delta T}{R}, \tag{3}
$$

$$
\Delta T = \frac{P_{\mathrm{abs}} \tau_{\mathrm{cool}}}{A_{\mathrm{active}} C_{\mathrm{el}}}. \tag{4}
$$

Here, $S_1$ and $S_2$ are the Seebeck coefficients in the $p$- and $n$-doped regions, $R$ is the electrical resistance across the channel, $P_{\mathrm{abs}}$ is the absorbed optical power, $\tau_{\mathrm{cool}}$ is the carrier cooling time, $A_{\mathrm{active}}$ is the active area where the carrier temperature is higher than the ambient temperature, and $C_{\mathrm{el}}$ is the electronic heat capacity. By embedding graphene in an environment with a higher dielectric constant, the Seebeck coefficients will increase, leading to a larger factor $(S_1 - S_2)$. The charge mobility is also increased, leading to a reduced device resistance $R$. The carrier cooling time $\tau_{\mathrm{cool}}$ increases due to slower cooling caused by screened carrier-carrier interactions. Furthermore, the reduced puddle energy allows tuning the Fermi energy very close to the Dirac point, where the electronic heat capacity is very small, thereby increasing the electron temperature. These factors all contribute to an increased photoresponse. However, there is a trade-off: the heating efficiency can be reduced as a result of screened electron-electron interactions, meaning that some initial energy is lost to phonons before the electronic system thermalizes. Moreover, slower cooling

also leads to a longer cooling length and therefore a larger active area $A_{\text{active}}$, which is not necessarily advantageous for photo-thermoelectric photodetectors. Since $A_{\text{active}} \propto \sqrt{\tau_{\text{cool}}}$, the net effect is still an increased photoresponse.

Future work can explore these trade-offs for photodetectors and other applications, such as nonlinear photonic devices based on graphene. It will also be important to explore alternative approaches to tune the dielectric environment, as liquids are not easily compatible with current device processing. Nearby metallic gates or high-permittivity dielectric materials could be good options, provided they do not host phonon modes that act as efficient heat sinks for hot electrons in graphene. Another interesting observation is that photoexcited carriers remain in the conduction band longer than in the screened case. This "semiconductor-like" behaviour opens avenues to exploiting alternative photoresponse mechanisms and functionalities that were not possible with the usual "metal-like" behaviour of graphene.

## Methods

### Experimental details
To perform optical pump – THz probe measurements on graphene with different liquid environments, we adapted a silica flow cell, such that one of the windows can be removed in order transfer graphene onto it. For this transfer, we used wet transfer of CVD graphene on copper foil, transferred using cellulose acetate butyrate (CAB) dissolved in ethyl acetate, which we spin-coated on top of graphene. We first etched the copper in an aqueous solution of 3g/100 ml ammonium persulfate, which was filtered by a 0.2-$\mu$m Nylon membrane filter. After the transferred CAB/graphene on SiO$_2$ had completely dried, we removed the CAB in an acetone bath for 12 hours. We carried out all steps in dust-free environments. The flow cell was prepared in such a way that the thickness of the solvent superstrate was 50 $\mu$m, as defined by the thickness of two sides of the window. This thickness ensured sufficient THz transmission. During the studies of the effect of the dielectric environment, we injected a solvent of interest into the silica flow cell using a syringe. To exclude the effect of inhomogeneity of graphene and ensure a reliable comparison, we conducted all the THz measurements at a single spot of the graphene sample, while varying only the solvent that was injected into the silica flow cell. While the dielec- tric environment above the graphene varied depending on the injected gas or solvent, the dielectric constant below the graphene was fixed to $\epsilon=3.9$, due to the fixed quartz substrate.

### Transport simulations
To simulate charge transport in graphene with disorder on the length scale of electron- hole puddles, we employ a linear-scaling quantum transport method capable of handling systems with many millions of atoms [51]. With this method, we first calculate the time- and energy-dependent mean-square displacement (MSD) of an initial state $|\psi\rangle$,

$$
\operatorname{MSD}(E, t)=\Delta X^{2}(E, t)+\Delta Y^{2}(E, t), \tag{5}
$$

$$
\Delta X^{2}/\Delta Y^{2}(E, t)=\frac{\langle\psi_{X/Y}(t)|\delta(E-\hat{H})|\psi_{X/Y}(t)\rangle}{\langle\psi|\delta(E-\hat{H})|\psi\rangle}, \tag{6}
$$

where $|\psi(t)\rangle=\hat{U}(t)|\psi\rangle$, $|\psi_{X/Y}(t)\rangle=[\hat{X}/\hat{Y},\hat{U}(t)]|\psi\rangle$, $\hat{X}$ ($\hat{Y}$) is the position operator along the $x$ ($y$) direction, $\hat{U}(t)=\exp(-\mathrm{i}\hat{H}t/\hbar)$ is the time evolution operator, and $\hat{H}$ is the tight-binding Hamiltonian of graphene,

$$
\hat{H}=t \sum_{\langle i,j\rangle} \hat{c}_i^\dagger \hat{c}_j + \sum_i \left[ \sum_{j=1}^{N_\text{eh}} V_j \exp\left( -\frac{|r_i - r_j|^2}{2\xi^2} \right) \right] \hat{c}_i^\dagger \hat{c}_i. \tag{7}
$$

The first term in $\hat{H}$ is the nearest-neighbor hopping with $t=-2.7$ eV. The second term captures the effect of electron-hole puddles, with each puddle modeled as a Gaussian variation of the onsite electrostatic potential [47, 48]. There are a total of $N_\text{eh}$ puddles, each with random center $r_j$, random height $V_j\in[-W,W]$, and uniform spatial width $\xi=10$ nm. Here we let $N_\text{eh}/N=0.04\%$, with $N=8\times10^6$ the number of atoms in our simulated system.

Rather than diagonalizing the Hamiltonian, the operators $\hat{U}(t)$ and $\delta(E-\hat{H})$ are expanded as a series of Chebyshev polynomials using the kernel polynomial method [59]. Here we use the Jackson kernel and 7000 polynomials, corresponding to an energy broadening of 6 meV. The initial state is chosen as a random-phase state in the site basis $|\psi\rangle=\frac{1}{\sqrt{N}}[\mathrm{e}^{\mathrm{i}\xi_1}...\mathrm{e}^{\mathrm{i}\xi_N}]^T$, where $\xi_n$ is a random number evenly distributed in $[0,2\pi)$. To reduce numerical noise, we average over 10 initial states and puddle configurations. From the MSD, we then calculate the diffusivity and the conductivity as

$$
D(E,t)=\frac{1}{4}\frac{\partial}{\partial t}\text{MSD}(E,t), \tag{8}
$$

$$
\sigma(E)=e^2\rho(E)D_\text{sat}(E), \tag{9}
$$

where $\rho$ is the density of states and $D_\text{sat}$ is the saturated value of $D$ at long times.

## Acknowledgments

X.J. acknowledges the financial support by DFG through the Excellence Initiative by the Graduate School of Excellence Materials Science in Mainz (MAINZ) (GSC 266) and support from the Max Planck Graduate Center mit der Johannes Gutenberg-Universität Mainz (MPGC). The ICN2 is funded by the CERCA programme / Generalitat de Catalunya. The ICN2 is supported by the Severo Ochoa Centres of Excellence programme, Grant CEX2021-001214-S, funded by MCIU/AEI/10.13039.501100011033. K.-J.T. acknowledges funding from the European Union's Horizon 2020 research and innovation program under Grant Agreement No. 101125457 (ERC CoG "EQUATE"), Spanish MCIN/AEI project PID2022-142730NB-I00 "HYDROPTO", and Flag-ERA grant ENPHOCAL, by MICIN with No. PCI2021-122101-2A (Spain).

[1] M. C. Lemme, F. H. L. Koppens, A. L. Falk, M. S. Rudner, H. Park, L. S. Levitov, and C. M. Marcus, Nano Lett. 11, 4134 (2011).

[2] J. C. W. Song, M. S. Rudner, C. M. Marcus, and L. S. Levitov, Nano Lett. 11, 4688 (2011).

[3] X. Cai, A. B. Sushkov, R. J. Suess, M. M. Jadidi, G. S. Jenkins, L. O. Nyakiti, R. L. Myers- Ward, S. Li, J. Yan, D. K. Gaskill, et al., Nat. Nanotechnol. 9, 814 (2014).

[4] S. Schuler, D. Schall, D. Neumaier, L. Dobusch, O. Bethge, B. Schwarz, M. Krall, and T. Mueller, Nano Lett. 16, 7107 (2016).

[5] J. E. Muench, A. Ruocco, M. A. Giambra, V. Miseikis, D. Zhang, J. Wang, H. F. Y. Watson, G. C. Park, S. Akhavan, V. Sorianello, et al., Nano Lett. 19, 7632 (2019).

[6] A. Antidormi and A. W. Cummings, Phys. Rev. Appl. 15, 054049 (2021).

[7] S. M. Koepfli, M. Baumann, R. Gadola, S. Nashashibi, Y. Koyaz, D. Rieben, A. C. Güngör, M. Doderer, K. Keller, Y. Fedoryshyn, et al., Nature Communications 15, 7351 (2024), ISSN 2041-1723.

[8] L. Vicarelli, M. S. Vitiello, D. Coquillat, A. Lombardo, A. C. Ferrari, W. Knap, M. Polini, V. Pellegrini, and A. Tredicucci, Nature Materials 11, 865 (2012), ISSN 1476-1122, 1203.3232.

[9] S. Castilla, B. Terrés, M. Autore, L. Viti, J. Li, A. Y. Nikitin, I. Vangelidis, K. Watanabe, T. Taniguchi, E. Lidorikis, et al., Nano Letters 19, 2765 (2019), ISSN 1530-6984, 1905.01881.

[10] L. Viti, D. G. Purdie, A. Lombardo, A. C. Ferrari, and M. S. Vitiello, Nano Letters 20, 3169 (2020), ISSN 1530-6984.

[11] K. P. Soundarapandian, S. Castilla, S. M. Koepfli, S. Marconi, L. Kulmer, I. Vangelidis, R. de la Bastida, E. Rongione, B. Terrés, S. A. Tongay, et al., Nature Communications 17, 2627 (2026), ISSN 2041-1723, 2411.02269.

[12] H. A. Hafez, S. Kovalev, J.-C. Deinert, Z. Mics, B. Green, N. Awari, M. Chen, S. Germanskiy, U. Lehnert, J. Teichert, et al., Nature 561, 507 (2018), ISSN 0028-0836.

[13] G. Soavi, G. Wang, H. Rostami, D. G. Purdie, D. De Fazio, T. Ma, B. Luo, J. Wang, A. K. Ott, D. Yoon, et al., Nature Nanotechnology 13, 583 (2018), ISSN 1748-3387, 1710.03694.

[14] T. Jiang, D. Huang, J. Cheng, X. Fan, Z. Zhang, Y. Shan, Y. Yi, Y. Dai, L. Shi, K. Liu, et al., Nature Photonics 12, 430 (2018), ISSN 1749-4885.

[15] A. Martinez and Z. Sun, Nature Photonics 7, 842 (2013), ISSN 1749-4885.

[16] A. Autere, H. Jussila, Y. Dai, Y. Wang, H. Lipsanen, and Z. Sun, Advanced Materials 30, 1705963 (2018), ISSN 15214095.

[17] T. Tan, X. Jiang, C. Wang, B. Yao, and H. Zhang, Advanced Science 7, 2000058 (2020), ISSN 2198-3844.

[18] Y. D. Kim, H. Kim, Y. Cho, J. H. Ryoo, C.-H. Park, P. Kim, Y. S. Kim, S. Lee, Y. Li, S.-N. Park, et al., Nature Nanotechnology 10, 676 (2015), ISSN 1748-3387.

[19] F. Luo, Y. Fan, G. Peng, S. Xu, Y. Yang, K. Yuan, J. Liu, W. Ma, W. Xu, Z. H. Zhu, et al., ACS Photonics 6, 2117 (2019), ISSN 2330-4022.

[20] R.-J. Shiue, Y. Gao, C. Tan, C. Peng, J. Zheng, D. K. Efetov, Y. D. Kim, J. Hone, and D. Englund, Nature Communications 10, 109 (2019), ISSN 2041-1723.

[21] M. Massicotte, G. Soavi, A. Principi, and K.-J. Tielrooij, Nanoscale 13, 8376 (2021), ISSN 2040-3364.

[22] D. Brida, A. Tomadin, C. Manzoni, Y. J. Kim, A. Lombardo, S. Milana, R. R. Nair, K. S. Novoselov, A. C. Ferrari, G. Cerullo, et al., Nature Communications 4, 1987 (2013), ISSN

2041-1723, 1209.5729.

[23] I. Gierz, J. C. Petersen, M. Mitrano, C. Cacho, I. C. E. Turcu, E. Springate, A. Stöhr, A. Köh- ler, U. Starke, and A. Cavalleri, Nature Materials **12**, 1119 (2013), ISSN 1476-1122, 1304.1389.

[24] K. J. Tielrooij, J. C. W. Song, S. A. Jensen, A. Centeno, A. Pesquera, A. Zurutuza Elorza, M. Bonn, L. S. Levitov, and F. H. L. Koppens, Nature Physics **9**, 248 (2013), ISSN 1745-2473, arXiv:1210.1205v2.

[25] J. C. Song, K. J. Tielrooij, F. H. Koppens, and L. S. Levitov, Physical Review B - Condensed Matter and Materials Physics **87**, 1 (2013), ISSN 10980121, 1209.4346.

[26] S. A. Jensen, Z. Mics, I. Ivanov, H. S. Varol, D. Turchinovich, F. H. L. Koppens, M. Bonn, and K. J. Tielrooij, Nano Letters **14**, 5839 (2014), ISSN 1530-6984.

[27] F. Rana, P. A. George, J. H. Strait, J. Dawlaty, S. Shivaraman, M. Chandrashekhar, and M. G. Spencer, Physical Review B **79**, 115447 (2009), ISSN 1098-0121.

[28] M. Breusing, S. Kuehn, T. Winzer, E. Malić, F. Milde, N. Severin, J. P. Rabe, C. Ropers, A. Knorr, and T. Elsaesser, Physical Review B **83**, 153410 (2011), ISSN 1098-0121.

[29] H. Wang, J. H. Strait, P. A. George, S. Shivaraman, V. B. Shields, M. Chandrashekhar, J. Hwang, F. Rana, M. G. Spencer, C. S. Ruiz-Vargas, et al., Applied Physics Letters **96**, 081917 (2010), ISSN 0003-6951, 0909.4912.

[30] L. M. Malard, K. Fai Mak, A. H. Castro Neto, N. M. R. Peres, and T. F. Heinz, New Journal of Physics **15**, 015009 (2013), ISSN 1367-2630.

[31] J. C. W. Song, M. Y. Reizer, and L. S. Levitov, Physical Review Letters **109**, 106602 (2012), ISSN 0031-9007.

[32] M. W. Graham, S.-F. Shi, Z. Wang, D. C. Ralph, J. Park, and P. L. McEuen, Nano Letters **13**, 5497 (2013), ISSN 1530-6984.

[33] W. Yang, S. Berthou, X. Lu, Q. Wilmart, A. Denis, M. Rosticher, T. Taniguchi, K. Watan- abe, G. Fève, J.-M. Berroir, et al., Nature Nanotechnology **13**, 47 (2018), ISSN 1748-3387, 1702.02829.

[34] K.-J. J. Tielrooij, N. C. H. Hesp, A. Principi, M. B. Lundeberg, E. A. A. Pogna, L. Banszerus, Z. Mics, M. Massicotte, P. Schmidt, D. Davydovskaya, et al., Nature Nanotechnology **13**, 41 (2018), ISSN 17483395, 1702.03766.

[35] X. Yu, A. Principi, K.-j. Tielrooij, M. Bonn, and N. Kavokine, Nature Nanotechnology **18**, 898 (2023), ISSN 1748-3387.

[36] E. A. A. Pogna, X. Jia, A. Principi, A. Block, L. Banszerus, J. Zhang, X. Liu, T. Sohier, S. Forti, K. Soundarapandian, et al., Arxiv **2103.03527** (2021), 2103.03527.

[37] M. W. Graham, S.-F. Shi, Z. Wang, D. C. Ralph, J. Park, and P. L. McEuen, Nano Letters **13**, 5497 (2013), ISSN 1530-6984.

[38] E. A. A. Pogna, A. Tomadin, O. Balci, G. Soavi, I. Paradisanos, M. Guizzardi, P. Pedrinazzi, S. Mignuzzi, K.-J. Tielrooij, M. Polini, et al., ACS Nano **16**, 3613 (2022), ISSN 1936-0851.

[39] J. Crossno, J. K. Shi, K. Wang, X. Liu, A. Harzheim, A. Lucas, S. Sachdev, P. Kim, T. Taniguchi, K. Watanabe, et al., Science **351**, 1058 (2016), ISSN 0036-8075, 1509.04713.

[40] A. Block, A. Principi, N. C. Hesp, A. W. Cummings, M. Liebel, K. Watanabe, T. Taniguchi, S. Roche, F. H. Koppens, N. F. van Hulst, et al., Nature Nanotechnology **16**, 1195 (2021), ISSN 17483395.

[41] M. Kim, S. G. Xu, A. I. Berdyugin, A. Principi, S. Slizovskiy, N. Xin, P. Kumaravadivel, W. Kuang, M. Hamer, R. Krishna Kumar, et al., Nature Communications **11**, 2339 (2020), ISSN 2041-1723.

[42] O. Madelung, ed., *Static Dielectric Constants of Pure Liquids and Binary Liquid Mix-*

tures, vol. 6 of Landolt-Börnstein - Group IV Physical Chemistry (Springer-Verlag, Berlin/Heidelberg, 1991), ISBN 3-540-54417-8.

[43] A. J. Frenzel, C. H. Lui, Y. C. Shin, J. Kong, and N. Gedik, Physical Review Letters 113, 056602 (2014), ISSN 0031-9007, 1403.3669.

[44] H. I. Wang, M.-L. Braatz, N. Richter, K.-J. Tielrooij, Z. Mics, H. Lu, N.-E. Weber, K. Müllen, D. Turchinovich, M. Kläui, et al., The Journal of Physical Chemistry C 121, 4083 (2017), ISSN 1932-7447.

[45] A. Tomadin, S. M. Hornett, H. I. Wang, E. M. Alexeev, A. Candini, C. Coletti, D. Turchinovich, M. Kläui, M. Bonn, F. H. L. Koppens, et al., Science Advances 4, eaar5313 (2018), ISSN 2375-2548, 1712.02705.

[46] S. Wu, L. Wang, Y. Lai, W.-Y. Shan, G. Aivazian, X. Zhang, T. Taniguchi, K. Watanabe, D. Xiao, C. Dean, et al., Science Advances 2, e1600002 (2016), ISSN 2375-2548, 1603.04934.

[47] S. Adam, P. W. Brouwer, and S. Das Sarma, Phys. Rev. B 79, 201404 (2009).

[48] J. W. Kłos and I. V. Zozoulenko, Phys. Rev. B 82, 081414 (2010).

[49] A. Deshpande, W. Bao, F. Miao, C. N. Lau, and B. J. LeRoy, Phys. Rev. B 79, 205411 (2009).

[50] J. Xue, J. Sanchez-Yamagishi, D. Bulmash, P. Jacquod, A. Deshpande, K. Watanabe, T. Taniguchi, P. Jarillo-Herrero, and B. J. LeRoy, Nat. Mater. 10, 282 (2011).

[51] Z. Fan, J. H. Garcia, A. W. Cummings, J. E. Barrios-Vargas, M. Panhans, A. Harju, F. Ort- mann, and S. Roche, Phys. Rep. 903, 1 (2021).

[52] S. Adam, S. Jung, N. N. Klimov, N. B. Zhitenev, J. A. Stroscio, and M. D. Stiles, Phys. Rev. B 84, 235421 (2011).

[53] P. Sharma and Z. L. Mišković, J. Chem. Phys. 143, 134118 (2015).

[54] D. Domaretskiy, Z. Wu, V. H. Nguyen, N. Hayward, I. Babich, X. Li, E. Nguyen, J. Barrier, K. Indykiewicz, W. Wang, et al., Nature 644, 646 (2025).

[55] U. Sivan and Y. Imry, Phys. Rev. B 33, 551 (1986).

[56] J. Duan, X. Wang, X. Lai, G. Li, K. Watanabe, T. Taniguchi, M. Zebarjadi, and E. Y. Andrei, Proc. Natl. Acad. Sci. U.S.A. 113, 14272 (2016).

[57] H. J. Hwang, S.-Y. Kim, S. K. Lee, and B. H. Lee, Carbon 201, 467 (2023).

[58] M. S. Foster and I. L. Aleiner, Phys. Rev. B 79, 085415 (2009).

[59] A. Weiße, G. Wellein, A. Alvermann, and H. Fehske, Rev. Mod. Phys. 78, 275 (2006).