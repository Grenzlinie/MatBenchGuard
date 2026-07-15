# Electronic Fabry-Pérot cavity engineered nanoscale thermoelectric generators

Swarnadip Mukherjee and Bhaskaran Muralidharan*
Department of Electrical Engineering, Indian Institute of Technology Bombay, Powai, Mumbai 400076, India

In this work, we aim to design a heterostructure based nanoscale thermoelectric generator that can maximize the waste-heat conversion efficiency at a given output power. The primary objective to be achieved for this is to realize a boxcar-shaped (bandpass) electronic transmission function (R. S. Whitney, Phys. Rev. Lett. 112, 130601 (2014)). In order to achieve that, we propose the use of an electronic analog of optical Fabry-Pérot cavity over a central resonant tunneling structure. We further explore the optimum design possibilities by varying the geometry of the cavity wall to ensure a nearly perfect bandpass energy filtering of electrons. Based on our findings, we propose a general design guideline to realize such transmission and demonstrate that such devices can be excellent thermoelectric generators compared to the existing proposals in terms of boosting the output power without a cost in efficiency. It is theoretically demonstrated using the non-equilibrium Green's function technique coupled with self-consistent charging effects that an enhancement in the maximum output power up to 116% can be achieved through this scheme at a 10% higher efficiency as compared to resonant tunneling based devices. Furthermore, an elaborate comparative study of the linear response parameters is also presented and explained in terms of the physical transport properties. This study suggests an optimal device design strategy for an improved thermoelectric generator and sets the stage for a new class of thermoelectric generators facilitated via transmission lineshape engineering.

## I. INTRODUCTION

Nanostructuring of thermoelectric (TE) materials has acquired unabated precedence over their bulk counterparts [1–8] since last two decades due to their highly efficient energy harvesting capability. Over the years, research in this field was primarily focused on achieving high thermoelectric figure-of-merit by means of lineshape engineering [1–6], thermal conductivity reduction through interface engineering [9–11] and enhancement of power factor utilizing energy filtering effects [12–14]. The figure of merit concept typically assists in determining whether a material is a good thermoelectric or not. However, when actual device designs are considered, non-linear transport studies [15, 16] dealing with the trade-off between conversion efficiency and output power of the entire set up [5, 17–23] have gained precedence.

In this context, an important work by R. S. Whitney [24, 25] suggested that in a thermoelectric device set up, a boxcar type electronic transmission function of a particular bandwidth can offer optimum trade-off by maximizing the efficiency at a given power. However, practical design guidelines of such type of devices are not well addressed. Several efforts have been made after that to realize such an electronic transmission feature by proper arrangements of tunnel coupled quantum dots (QD) [15, 26].

A few recent studies [16, 27] utilized the miniband feature of superlattice based devices [28, 29] to achieve the boxcar transmission profile. Further advancing on such ideas, recently, thermoelectric generator (TEG) setups augmented with an electronic anti-reflection cavity (ARC) [27, 30] have been proposed using the basic thumb rule for ARC design [31]. These ideas proved to be far superior in terms of achieving excellent power-efficiency trade-off in comparison with the competing device proposals [16–18]. However, it should be noted that, in the presence of charging effects, the superlattice designs [27] suffer from serious lineshape imperfections which badly affects the power and trade-off characteristics. Moreover, the large number of constituting layers in such devices poses a serious threat to the precise epitaxial growth with the existing technology. On the other hand, the ARC based proposal [30] although produced improved result but was never optimized for further scope of improvements. The object of this paper is to hence propose

![](./images/867773434023641602_1.jpg)

FIG. 1. Device schematic of an electronic Fabry-Pérot cavity engineered heterostructure based thermoelectric generator setup. The central region, in general, consists of a multi period heterostructure sandwiched between two electronic cavity sections. This work considers the use of a simple double barrier resonant tunneling structure embedded by cavities of varying wall geometry to optimize the desired shape of transmission spectrum.

* bm@ee.iitb.ac.in

a TEG device structure and explore its design space to provide a robust design guideline after examining and taking into consideration all the aforementioned aspects.

In this work, we consider a simple double barrier resonant tunneling (RT) structure embedded in an electronic Fabry-Pérot (FP) cavity as shown schematically in Fig. 1. The dotted rectangle in the cavity region denotes the variation of the width and height of the electronic potential barrier. This cavity is similar to a Fabry-Pérot setup used in optics where the mirrors are replaced by rectangular tunneling electronic barriers which act as cavity walls. The transmission function, being strongly dependent on the tunneling probability through these barriers, can be tuned by varying their height and width. We show that by following a specific design guideline, a nearly band-pass transmission can be achieved by varying the wall geometry. A careful examination of the transmission function reveals that one can achieve even wider band-pass profile compared to that of the conventional ARC based design [30, 32] by following the proposed guideline. This setup when used as a thermoelectric generator can significantly raise the output power at a high conversion efficiency as compared to the existing proposals [5, 17, 27]. Exploring the design space further, it is seen that an improvement of output power up to 18% can be achieved without any degradation in the efficiency over the ARC based structure [30].

The rest of the paper is structured as follows. In Sec. II, the variation of the transmission function with respect to the different cavity designs is thoroughly examined and explained in the lights of ARC physics. Based on the obtained result, three unique designs are picked for further investigation on their capability of being good thermoelectric generator. The band schematics of all the devices are depicted in Sec. III with a clear description of their physical properties. Section IV briefly discusses the simulation setup and illustrates the formalism used. In Sec. V, the results are thoroughly discussed in terms of all the performance parameters and a detailed comparative study is presented in order to highlight the improvements achieved through the proposed design scheme. We conclude the paper in Sec. VI.

## II. CAVITY PHYSICS AND TRANSMISSION FUNCTION

In this section, we closely inspect the variation of the transmission function, $T(E)$, with respect to the stoichiometric and geometric changes of the cavity wall. The thumb rule of designing ARC says that the width ($b_{FP}$) and height ($h_{FP}$) of the rectangular cavity barriers should exactly be half and equal, respectively, to that of the central barrier region [31]. The reason behind this can be qualitatively explained in terms of the electronic Bloch states in the neighborhood of the transmission peaks of the central heterostructure [30, 31, 33, 34]. According to the modified Kronig-Penney model, the transmission peaks of the periodic heterostructure occur when [31, 35]

$$
\cos(kL) = \cos\left(\frac{i\pi}{N}\right),\quad i=1,2,...,N-1,\tag{1}
$$

where $L$ is the length of the periodic structure, $N$ is the number of periods and $k$ is the Bloch wave vector which is defined as $k=\frac{2\pi}{\lambda}$, where $\lambda$ is the wavelength. Replacing $k$ by $\lambda$ in Eq. 1, we get $\lambda_i=2L/i$, which says that twice the length of the structure should be equal to integer multiple of the allowed wavelengths. The concept of electronic anti-reflection is actually borrowed from the well-known Fabry-Pérot setup used in optics. To satisfy the anti-reflection condition, the reflected waves from the two boundaries of the cavity barrier should exactly be out of phase of each other. In other words, the cavities should act as Bragg-reflector at a wavelength $\lambda'$ which satisfies the condition for thin film interference, given by

$$
2b_{FP}=\left(m+\frac{1}{2}\right)\lambda',\tag{2}
$$

where $\lambda'$ lies in the neighborhood of $\lambda$ and $m$ is an integer. Therefore, for $m=0$, a unity transmission peak occurs at $\lambda'$ if the cavity barriers are $\lambda'/4$ layers ($b_{FP}=\lambda'/4$). This condition along with aforementioned relation of $L=i\lambda/2$ suggest that $b_{FP}$ should be around half the width of the central barrier region ($b$) as the width of the well regions ($w$) throughout the structure are considered to be uniform.

In this context, one should always ponder that unlike the optical setup, the height of the cavity wall plays a crucial role in tailoring the lineshape of the transmission. To be more specific, the combined effect of $b_{FP}$ and $h_{FP}$ controls the phase of the reflected waves from the cavity wall boundaries which in turn determines the transmission probability. By carefully examining the transmission of a setup shown in Fig. 1, we note that the amount of aberration from the bandpass nature caused by a tiny reduction in $b_{FP}$ from $b/2$, can be compensated by a proportional upscaling of $h_{FP}$ from $h$. To explain this, we draw a connection between the potential energy of the cavity barrier region ($h_{FP}$) and its refractive index ($n$). It should be noted that for a medium with refractive index $n$, the associated wavelength ($\lambda_n$) is defined as $\lambda_n=\lambda/n$, where $\lambda$ is the corresponding vacuum wavelength. Therefore, replacing $\lambda'$ by $\lambda'/n$ in Eq. 2 for $m=0$, the condition for anti-reflection becomes

$$
b_{FP}=\frac{\lambda'}{4n}.\tag{3}
$$

In the wave-particle duality picture, this wavelength is called the de-Broglie wavelength of the electron which is directly related to its momentum ($p$) by the relation $\lambda=h/p$. Hence the local de-Broglie wavelength of the cavity tunnel barrier can be expressed as

$$
\lambda_n=\frac{\lambda}{n}=\frac{h}{\sqrt{2m(E-h_{FP})}},\tag{4}
$$

where $p = \sqrt{2m(E - h_{FP})}$ for a rectangular barrier of height $h_{FP}$, $m$ is the effective mass of the tunnel barrier, $h$ is the Planck's constant, $E$ is the electron energy and $\lambda$ is the reference wavelength (here, the wavelength of the well region on both sides of the tunnel barrier). The refractive index $n$ is thus given by [36, 37]

$$
n = \frac{\lambda}{\lambda_n} = \sqrt{\frac{2m(E - h_{FP})}{2m_0 E}}, \tag{5}
$$

where the well region is having an effective mass of $m_0$ and zero potential energy. As we are only concerned in the energies below the cavity barrier height $(E < h_{FP})$, the condition for anti-reflection is thus obtained by substituting the absolute value of $n$ from Eq. 5 into Eq. 3 which is given by

$$
b_{FP} = \frac{\lambda'}{4} \sqrt{\frac{2m_0 E}{2m(h_{FP} - E)}}. \tag{6}
$$

This indicates that for the anti-reflection condition to prevail, any reduction in $b_{FP}$ must be associated with a particular increase in $h_{FP}$. As the design energy $E$ can't be precisely defined, one can't establish a specific relation between $b_{FP}$ and $h_{FP}$. However, one can always predict an optimal design guideline by examining the transmission function of the RT structure embedded in an electronic FP cavity.

Above theory calls for a further investigation on the possible betterment of the boxcar nature of the transmission [30] by means of optimal cavity engineering. A quantitative measure in this regard is the transmissivity $(TM)$ which is the area under the flatband transmission function corresponding to the lowest transmission band, given by

$$
TM = \int_{0}^{E_1} |T(E)| dE, \tag{7}
$$

where the energy $E_1$ is chosen in such a way that it falls almost in between the ground and first excited band with almost zero transmission probability. The transmission function is calculated using the standard non-equilibrium Green's function (NEGF) theory [38] which will be addressed later. Figure 2(a) displays the variation of $TM$ of the aforementioned setup as a function of $b_{FP}$ and $h_{FP}$ in a gray scale color plot for a given set of RT device parameters which will be discussed in the next section. We observe that $TM$ exhibits a nearly hyperbolic trend around its maxima which monotonically increases (along the direction of the black dotted arrow) with decreasing $b_{FP}$ and increasing $h_{FP}$. A careful investigation of the transmission reveals that its boxcar nature can almost be maintained if the percentage reduction in $b_{FP}$ from $b/2$ is equal to half the percentage increase in $h_{FP}$ from $h$. This finding closely matches with the theory presented above. Therefore, the design guideline to achieve boxcar transmission can be mathematically expressed as

$$
\frac{|b_{FP} - b/2|}{b/2} = \frac{1}{2} \frac{|h_{FP} - h|}{h}. \tag{8}
$$

![](./images/867773434023641602_2.jpg)

FIG. 2. Transmission function: (a) Area under the flatband transmission function corresponding to the lowest transmission band (TM) is shown in a gray scale color plot as a function of the cavity wall width and height. The locus of its maxima follows a nearly hyperbolic trend which increases along the direction of the black dotted arrow. From the obtained trend, two new design schemes are picked (green and red) for further investigation as good thermoelectric generators and comparison with the ARC based proposal (blue). (b) Equilibrium flatband transmission function of all the cavity based devices are shown as a function of energy. The peaked transmission of the central RT region (without the ARC) is also shown here to emphasize the role of cavity engineering on transmission.

The allowed design space of $b_{FP}$ and $h_{FP}$ is given by $b_{min} \leq b_{FP} \leq b/2$, $h \leq h_{FP} \leq h_{max}$, where $b_{min}$ and $h_{max}$ are the practical bounds of cavity barrier width and height, respectively. In this case, based on the desired transmission goal, these bounds are set as $b_{min} = b/4$ and $h_{max} = 2h$.

It is also worth mentioning that within the allowed design space, the steady increase of $TM$ along the direction shown in Fig. 2(a) suggests that the boxcar nature can be further improved by utilizing other set of cavity designs. In order to justify this, we pick two sample design schemes of the FP cavity namely, FP-II (green diamond) and FP-III (red star) as indicated in Fig. 2(a) alongside the typical ARC ($b_{FP} = b/2$, $h_{FP} = h$) based proposal (FP-I, blue circle) [30, 32]. Under flatband conditions,

the equilibrium transmission function of all the FP based designs are plotted in Fig. 2(b) as a function of energy along with the standard RT transmission. The cavity design parameters corresponding to all the devices are presented in the legends of Fig. 2(b) in terms of the RT design parameters. We observe that as compared to FP-I, the new schemes (FP-II and FP-III) tend to widen the transmission further preserving its desired shape, thereby improving $TM$. One notable difference to notice here is that the new proposals exhibit a slight dip in the transmission at energies below the resonating peak unlike the ARC based design. This might cause a slight reduction in the efficiency at lower values of the contact Fermi level. It is also important to note that the cavity region, based on its design, pulls the transmission minima to unity at a particular energy which might not be the mid-band energy always. In this case, Fig. 2(b) suggests that as the width of the cavity barrier is reduced, this energy tends to rise which in turn widens the transmission bandwidth. Having obtained such transmission features, we strongly believe that the new designs can be even better thermoelectric generator and hence should be investigated further.

### III. DEVICE SCHEMATIC AND DESCRIPTION

Based on the design rules discussed in the last section, we depict the conduction band schematics of all the three cavity engineered devices (FP-I, FP-II and FP-III) along with the standard resonant tunneling device (RTD) in Fig. III(b)-(e). These devices are having an ideal infinite extent in the transverse direction with a finite length along their transport direction (here, z-direction). The central RTD structure, as shown in Fig. 3(b), is modeled with a GaAs well of width $w = 4.2nm$ in between two $Al_xGa_{1-x}As$ barriers of width $b = 2.4nm$ each, where $x$ is aluminum mole-fraction. Barrier height is kept fixed at $0.3eV$ with respect to the well by precisely tuning the mole-fraction parameter. These design parameters are chosen in accordance with a realistic ground state transmission full width at half maximum (FWHM) of $k_BT/2$, where $k_B$ is the Boltzmann's constant and $T$ denotes the temperature. For the cavity based devices, the same RTD structure is symmetrically placed within the cavity regions such that the width of the well region between any two successive barriers remains the same at $w$. However, the varying design of cavity wall gives rise to three different structures considered in this study which are listed below:

- In Fig. 3(c), FP-I: $h_{FP}=h$ and $b_{FP}=b/2$,
- In Fig. 3(d), FP-II: $h_{FP}=3h/2$ and $b_{FP}=3b/8$,
- In Fig. 3(e), FP-III: $h_{FP}=2h$ and $b_{FP}=b/4$.

The devices described above can be fairly accurately modeled using a nearest neighbor tight-binding Hamiltonian of a linear atomic chain within the single-band effective mass approximation [38]. The GaAs/AlGaAs material system is chosen here due to its less variability of effective mass over a wide range of composition and excellent lattice matching capability. Using the NEGF technique coupled with the charging effect, we present a comparative study of the devices discussed above in terms of the linear and non-linear thermoelectric performance parameters. The device dimensions used here are in the order of the relaxation length scales which eliminates the possibility of scattering to ensure a coherent

![](./images/867773434023641602_3.jpg)

FIG. 3. Simulation setup and device schematics: (a) A typical voltage-controlled thermoelectric setup is shown where the central device is connected to two contacts of different temperatures externally joined by a load. The conduction band schematics of four different TE device structures are depicted as follows: (b) RTD-TE: a standard resonant tunneling structure having the transmission $FWHM = k_BT/2$. This RTD device is embedded into three different FP cavity configurations namely, (c) FP-I: $h_{FP}=h$ and $b_{FP}=b/2$, (d) FP-II: $h_{FP}=3h/2$ and $b_{FP}=3b/8$ and (e) FP-III: $h_{FP}=2h$ and $b_{FP}=b/4$.

transport of carriers within the ballistic limit [17]. On the other hand, the presence of nano-structured inter- faces strongly restricts the flow of phonons in the device. This implies that the heat current flowing through the device is mainly due to electrons. Therefore, the lattice contribution to the thermal conductivity is ignored here.

The cavity based devices, manifest high immunity to the non-equilibrium changes in transmission function due to the charging effect. This results in an improved trade- off characteristics for a wide range of contact Fermi level. Furthermore, the widening of the transmission window allows a large number of additional transverse modes to conduct and contribute to the net charge current which in turn boosts the power. Based on the results, we can definitely assert that the width of the transmission func- tion obtained here is still below the ideal theoretical limit predicted by Whitney [24] which makes a room for fur- ther research.

## IV. SIMULATION METHODOLOGY AND SETUP

Figure 3(a) shows a typical voltage-controlled thermo- electric heat engine setup [39] which will be used through- out for the purpose of simulation. The flow of electrons due to the thermal driving force from the hot to cold contact is opposed by the voltage drop across the load resistance connecting them. The polarity of this drop is such that it lowers the quasi Fermi level of the hot con- tact with respect to the cold contact which, as a result, causes an opposite flow of electrons. In the simulation framework, the variation of the load resistance is incor- porated through the application of a positive voltage at the hot contact end.

The simulation methodology is mainly divided into two important parts, namely, (i) self-consistent estimation of the electronic transmission function and (ii) the calcu- lation of charge and heat currents from the knowledge of the obtained transmission function. For the former part, we utilize the standard atomistic NEGF formal- ism [38, 39] self-consistently coupled with the Poisson's equation. In order to analyze the device behavior under different operating conditions, we vary the equilibrium quasi Fermi levels $(E_{f})$ of the hot $(\mu_{H})$ and cold $(\mu_{C})$ contacts. For a given applied bias of $V_{a p p}$, the Fermi level of the hot (cold) contact is shifted downward (upward) from its equilibrium value by an amount of $q V_{a p p} / 2$ due to symmetric electrostatic coupling, where $q$ is the unit electronic charge. The simulation begins with a linear potential profile as an initial guess to calculate the lon- gitudinal energy $(E)$ resolved retarded Green's function G(E), given by
$$G(E)=\left[\left(E+i 0^{+}\right) \mathbb{I}-H-U(z)-\Sigma_{H}(E)-\Sigma_{C}(E)\right]^{-1}, \quad(9)$$
where $U(z)$ is the potential profile along the transport di rection, $\Sigma_{H(C)}$ is the self-energy matrix of the hot (cold) contact and $\mathbb{I}$ is the identity matrix. Having obtained $G(E)$, the carrier concentration $(n)$ can be easily cal culated from the electron correlation function, $G^{n}(E)$ , which is then fed into the Poisson's equation to calcu- late the updated potential profile. The set of equations governing the above mentioned routine are given by
$$G^{n}(E)=G\left[\Gamma_{H} f_{2 D}\left(\mu_{H}\right)+\Gamma_{C} f_{2 D}\left(\mu_{C}\right)\right] G^{\dagger}, \quad(10)$$

$$n=\frac{1}{\Delta z} \int \frac{G^{n}(E)}{2 \pi} d E,\qquad(11)$$

$$\frac{d^{2}}{d z^{2}}(U(z))=\frac{-q^{2}}{\epsilon_{0} \epsilon_{r}} n\qquad(12)$$
where $\Delta z$ is the discrete lattice spacing parameter, $\epsilon_{0}$ is the free space permittivity, $\epsilon_{r}$ is the relative permittiv ity of GaAs which is assumed to be uniform throughout the lattice and $\Gamma_{H(C)}$ represents the broadening func tion of hot (cold) contact which is defined as $\Gamma_{H(C)}=$  $i\left\lfloor\sum _{H(C)}-\sum _{H(C)}^{\dagger}\right\rfloor$ . The contribution from all the trans verse modes are encapsulated in the $f_{2 D}$ function whichis defined as [38]
$$f_{2 D}(E-\mu)=\frac{m_{e}^{*} k_{B} T}{2 \pi \hbar^{2}} \log [1+\exp \left(\frac{\mu-E}{k_{B} T}\right)],\qquad(13)$$
where $\hbar$ is the reduced Planck's constant and $m_{e}^{*}$ is the electron effective mass which is considered to be uniform throughout the lattice. For our simulations, we take a constant effective mass of $0.07 m_{0}$ across structures, where $m_{0}$ is the free electron mass. The NEGF-Poisson simulation is performed self-consistently until the conver- gence is achieved and the non-equilibrium transmission function, $T(E)$ , can thereby calculated as
$$T(E)=\operatorname{Tr}\left[\Gamma_{H} G \Gamma_{C} G^{\dagger}\right].\qquad(14)$$

The resultant transmission function is then fed into the Landauer current formula to calculate the charge $(J)$ and heat current $(J^{Q})$ densities [38]. Summing over all the current carrying transverse modes and absorbing that in the $f_{2 D}$ function, total charge current flowing through the device is given by
$$J=\frac{q}{\pi \hbar} \int d E T(E)\left[f_{2 D}\left(E-\mu_{H}\right)-f_{2 D}\left(E-\mu_{C}\right)\right].(15)$$

It is important to note that the total heat current which is the energy weighted charge current, is resolved into two components namely, $J_{H}^{Q 1}$ and $J_{H}^{Q 2}$ based on the contri butions from longitudinal and transverse energy degrees of freedom, respectively. Therefore, the total heat cur- rent flowing through the hot contact $(J_{H}^{Q})$ is expressed as $J_{H}^{Q}=J_{H}^{Q 1}+J_{H}^{Q 2}$ , where $J_{H}^{Q 1}$ and $J_{H}^{Q 2}$ are given by
$$\begin{aligned}
J_{H}^{Q 1}=\frac{1}{\pi \hbar} & \int d E T(E)\left(E-\mu_{H}\right) \\
& \times\left[f_{2 D}\left(E-\mu_{H}\right)-f_{2 D}\left(E-\mu_{C}\right)\right], \quad(16)
\end{aligned}$$

$$
J_{H}^{Q 2}=\frac{1}{\pi \hbar} \int d E T(E)\left[g_{2 D}\left(E-\mu_{H}\right)-g_{2 D}\left(E-\mu_{C}\right)\right], \quad(17)
$$

where $g_{2 D}$ function is defined as [17,30]

$$
g_{2 D}(E-\mu)=\frac{m^{*}}{2 \pi \hbar^{2}} \int_{0}^{\infty} \frac{\epsilon_{\vec{k}_{\perp}} d \epsilon_{\vec{k}_{\perp}}}{1+\exp \left(\frac{E+\epsilon_{\vec{k}_{\perp}}-\mu}{k_{B} T}\right)}. \quad(18)
$$

The integration in Eq. 18 is performed numerically where the upper limit of energy is chosen high enough to include all the significant transverse modes. We assume a parabolic dispersion relation $(\epsilon_{\vec{k}_{\perp}})$ in the transverse direction and the integration over all the momentum $(\vec{k}_{\perp})$ eigenstates is carried out with a periodic boundary condition.

Once the charge $(J)$ and heat current $(J_{H}^{Q})$ densities are calculated, the output power density $(P)$ and conversion efficiency $(\eta)$ can be obtained using the standard thermoelectric setup [39] by the following relations

$$
P=J V_{a p p}, \quad(19)
$$

$$
\eta=P / J_{H}^{Q}. \quad(20)
$$

The efficiency is usually measured as a ratio to that of the Carnot's limit $(\eta_{C})$, defined as $\eta_{C}=1-T_{C} / T_{H}$, where $T_{H(C)}$ is the temperature of the hot (cold) contact. In the simulation, a steady temperature difference of $30 K$ is maintained between the contacts by setting $T_{H}=330 K$ and $T_{C}=300 K$. The allowed range of power restricts the device operation between short circuit $(V_{app}=0)$ to open circuit $(V_{app}=V_{OC})$ condition, where $V_{OC}$ is the open circuit voltage.

## V. RESULTS AND DISCUSSION

In this section, a detailed and comparative study of the results are discussed in terms of the non-linear and linear response parameters. This study will mainly focus on the supremacy of the proposed device designs over the existing ones.

### A. Non-linear Response Analysis

Power and Efficiency: In Fig. 4, output power per unit area of all the device structures are displayed as a function of $V_{app}$ and contact $E_{f}$ in a gray scale color plot. It can be seen that the power starts to increase from the short circuit condition with increasing $V_{app}$ and reaches a local maxima before falling to zero at the onset of the open circuit condition. Strictly speaking, net current actually reverses its direction at $V_{OC}$ and therefore the setup can't be used as a generator beyond this point. Usable power in the region beyond $V_{OC}$ is thus treated as zero. This trend is almost similar irrespective of the design scheme, but, what is important to note here is the variation of power with $E_{f}$. When $E_{f}$ is moved up in the energy scale from the lowest conduction band edge, the net flow of electrons from the hot to cold contact increases steadily. This results in a monotonic rise of power until it reaches its peak value when the net electron flow becomes maximum. At this point the overlap between the electronic density-of-states (DOS) and the region where $f_{2 D}(\mu_{H})-f_{2 D}(\mu_{C})>0$ becomes maximum which also indicates to the most non-reversible state of the heat engine. With further increase in $E_{f}$, power starts to die down steadily as the reverse flow (cold to hot) of electrons increases until $E_{f}$ moves in the vicinity of the higher excited states. But, we restrict our study only within the contribution of the ground state as the excited states hardly contribute to the conduction due to their negligible electron population and is thus kept out of consideration. On the other hand, when $E_{f}$ goes way down in energy, the power becomes negligible due to the lack of available states for conduction in the Fermi window. We, therefore, set the range of $E_{f}$ between $0-10 k_{B} T$ in our simulation where the reference energy $E=0$ is chosen as the conduction band minimum of GaAs.

![](./images/867773434023641602_4.jpg)

FIG. 4. Comparative study of output power: Power density (in $MW/m^2$) of (a) RTD, (b) FP-I, (c) FP-II, and (d) FP-III devices are shown as a function of the applied bias $(V_{app})$ and contact Fermi level $(E_{f})$. Enabling ARC (FP-I) over the RTD structure nearly doubles the generated output power for the entire range of $E_{f}$. The power can be further boosted between $15-18\%$ by means of optimal cavity engineering as evident in case of the new design schemes (FP-II and FP-III).

Figure 4(a) displays the power density profile of the RTD-TE device which reveals that the maximum power of $0.49MW/m^2$ can be delivered at $E_f = 4.5k_BT$. It is also important to observe that with increasing $E_f$, $V_{OC}$ sharply falls due to the sharp nature of the transmission and therefore the power remains non-zero only for a narrow region of operation. On the other hand, the cavity based devices due to their band-pass nature of transmission, manifest a huge improvement in the power along with a broad spectrum as depicted in Fig. 4(b), (c), (d) for the configurations FP-I, FP-II and FP-III, respectively. Obtained results show that FP-II and FP-III designs can generate maximum power ($P_{max}$) up to $1.03MW/m^2$ and $1.06MW/m^2$, respectively, as compared to $0.9MW/m^2$ of the ARC based proposal (FP-I) and $0.46MW/m^2$ of the superlattice based generators [27]. The position of $P_{max}$ of the new proposals is at $E_f = 5.5k_BT$ which is slightly higher than that of FP-I whose $P_{max}$ occurs at $E_f = 5k_BT$. This result is in good agreement with the nature of the obtained transmission functions of the new designs as they are marginally shifted upward in energy when compared to that of FP-I. One must note that deploying the new design schemes, $P_{max}$ can be boosted up to a maximum of 18% and 116% over the ARC and RTD based proposal, respectively.

A device can only be qualified as a good heat engine if it can deliver considerable amount of power at a high conversion efficiency. Therefore, an important parameter to judge here is the conversion efficiency which dictates the ability of a generator to convert heat into electricity. Normalized conversion efficiency ($\eta/\eta_C$) of all the devices are shown in Fig. 5 as a function of $V_{app}$ and contact $E_f$. It is seen that the efficiency becomes maximum in the close vicinity of $V_{OC}$ at $E_f = 0k_BT$ irrespective of the design scheme and decreases monotonically afterwards with increasing $E_f$. However, theoretically the efficiency can be improved further towards the ideal Carnot's limit at the cost of generated power by pushing $E_f$ way down the conduction band edge. But those devices would hardly be of any practical use due to their poor load driving capability. Ideally, the heat current increases when the conduction takes place at higher energies. Therefore, the efficiency attains its maximum value when $E_f$ is farthest below the ground transmission band. Within the mentioned simulation range, the highest efficiency that can be achieved in the RTD-TE device is 61.5% at $E_f = 0k_BT$ as shown in Fig. 5(a). On the other hand, the cavity based devices although possessing wide transmission spectra, can offer even better efficiency due to their sharp transition profile of transmission as evident from Fig. 5(b), (c), (d) for FP-I, FP-II and FP-III, respectively. The maximum attainable limit of efficiency that can be achieved through optimal cavity engineering is 64.4% for the aforementioned range of power which is even better than 61.7% of the superlattice based generators [27]. Obtained results clearly point towards an improved power-efficiency trade-off characteristics which will be discussed next.

![](./images/867773434023641602_5.jpg)

FIG. 5. Comparative study of efficiency: Conversion efficiency normalized to Carnot's efficiency of (a) RTD, (b) FP-I, (c) FP-II, and (d) FP-III devices are shown as a function of $V_{app}$ and contact $E_f$. The efficiency in general becomes maximum in the close proximity of $V_{OC}$ at $E_f = 0k_BT$. The cavity based new proposals show almost similar range of efficiency with a hint of improvement in the maximum value as compared to the ARC based device.

Power-efficiency-product and Trade-off: So far, we have quantitatively discussed about the maximum achievable limit of the power and efficiency and their region of occurrence. We note that the variational trends followed by them are completely different in nature. But to design an efficient heat engine, one must be extremely careful in choosing the regime of operation such that the device can deliver significant amount of power at a high efficiency. In this context, instead of looking into the power and efficiency separately, their product ($PEP$) becomes more meaningful to inspect. For each value of $E_f$, the maximum of $PEP$ ($PEP_{max}$) with respect to the applied voltage is shown as a function of $E_f$ in Fig. 6(a). Besides, we also plot the maximum power ($P_{max}$) with respect to $E_f$ in Fig. 6(b) in order to compare with $PEP_{max}$. We notice that the maximum of $PEP_{max}$ occurs around $E_f = 4k_BT$ which is well ahead to that of $P_{max}$ which becomes maximum around $E_f = 5.5k_BT$. This clearly signifies that the efficiency falls rapidly with increasing $E_f$ which is also evident from the sharp fall of $PEP_{max}$ beyond its maxima in contrast to $P_{max}$. It is also worth mentioning that the margin of improvement in both the parameters becomes maximum around their

![](./images/867773434023641602_6.jpg)

FIG. 6. Comparative analysis: (a) $PEP_{max}$ and (b) $P_{max}$ are plotted with respect to different $E_f$ for all the cavity engineered devices. The difference in the range of $E_f$ pertaining to the maximum values of $PEP_{max}$ and $P_{max}$ directly point towards the trade-off between power and efficiency. It is also worth mentioning that as we move forward in the design order as in Fig. 2(a), we achieve even more improved power and $PEP$.

![](./images/867773434023641602_7.jpg)

FIG. 7. Comparative analysis of power-efficiency trade-off along the locus of (a) $P_{max}$ and (b) $PEP_{max}$ for all the cavity engineered devices. It is noted that in both the cases the new design schemes enclose a larger area on the power-efficiency plane which allows them to operate satisfactorily over a wide range of $E_f$.

respective maxima which further improves the trade-off.

Non-linear studies of thermoelectric heat engine has got precedence as they generally talk about the power-efficiency trade-off and the best operating regime of the device. Neither the power nor the efficiency is sufficient alone to judge the overall performance as they are dependent on each other. Therefore, we shift our attention towards determining the most suitable operating regime of these devices based on the specific design goals. A typical power-efficiency trade-off curve looks like a loop with the start (short-circuit condition) and end (open-circuit condition) points being the origin as shown in Fig. 3(a) in Ref. 30. At any particular $E_f$, the loop is obtained by plotting the efficiency against power for all values of $V_{app}$. For any loop, one can always see that $P_{max}$ and $PEP_{max}$ occur at different values of $V_{app}$. Considering both the aspects, we plot the trade-off boundaries along the locus of $P_{max}$ and $PEP_{max}$ for the series of loops at different values $E_f$ in Fig. 7(a) and (b), respectively. The plots show that the trade-off characteristics improve significantly (enclosing a larger area) for the FP-II and FP-III structures as compared to the ARC based (FP-I) device [30]. In this case, by improving we mean that the proposed devices can operate over a wide range of design parameters with satisfactory performance. A steady improvement in the trade-off begins to show up when $E_f$ goes past $3k_BT$ and maximizes in the range of $4-7k_BT$ for both the cases. For a given range of efficiency between $30-40\%$, the respective power (in $MW/m^2$) corresponding to $P_{max}$ and $PEP_{max}$ varies between $0.8-0.9$ and $0.75-0.87$ for FP-I, $0.94-1.03$ and $0.9-1$ for FP-II and $0.95-1.06$ and $0.94-1.03$ for FP-III. These results clearly indicate that the new proposals offer excellent trade-off characteristics and perform significantly well within the suitable operating regime of $E_f$ between $4-7k_BT$.

### B. Linear Response Analysis

Using the same simulation framework, the linear response parameters can be extracted from the coupled charge and heat current equations, given by

$$
I=G\Delta V+G_{S}\Delta T,\quad I_{Q}=G_{P}\Delta V+G_{Q}\Delta T,\tag{21}
$$

where, $G, G_S, G_P, G_Q$ are related to the corresponding Onsager coefficients [39]. $\Delta V$ and $\Delta T$ are the applied electrical and thermal bias, respectively, which are kept small enough to ensure linear operation.

Power Factor and Seebeck Coefficient: Power factor ($PF$) is defined as $PF=S^2G$, where $G$ is the electrical conductivity and $S$ is the Seebeck coefficient which is given by, $S=-G_S/G$. In Fig. 8(a), one can easily notice the sharp and steady rise of $PF$ beyond $E_f=2k_BT$ from FP-I to FP-III. The maximum improvement in $PF$ that can be achieved through optimal cavity engineering over that of the ARC based design is nearly $20\%$ in the range of $E_f$ between $5-6k_BT$. This result actually points towards a monotonic improvement of $G$ as the Seebeck coefficients of the cavity based devices remain almost same for the entire range of $E_f$ as depicted in Fig. 8(b). We understand that the marginal improvement in the transmission function although does not affect the $V_{OC}$ much, but accounts for considerable gain in the $PF$ due to the additional large number of transverse current carrying modes that participate in conduction.

Figure-of-Merit: Although the main goal of this work is to improve the non-linear performance, however, it is customary to discuss the dimensionless Figure-of-Merit ($zT$) in order to judge the device ability as an efficient heat engine. In our study, we restrict ourselves to the electronic part of heat conduction neglecting the phonon contribution. The presence of nano-structured interfaces strongly hinders the phonon transport through the lattice which in turn results in a negligible thermal conductivity in contrast to its electronic counterpart. With these

![](./images/867773434023641602_8.jpg)

FIG. 8. Comparative analysis: (a) Power factor ($PF$) and (b) Seebeck coefficient ($S$) are plotted with respect to varying contact $E_f$. A steady improvement in $PF$ is observed beyond $E_f=2k_BT$ as we move up in the design order from FP-I to FP-III. The maximum improvement achieved in $PF$ through cavity engineering is nearly $20\%$ at $E_f$ around 5 to $6k_BT$. On the other hand, there is no noticeable difference observed in $S$ among the cavity engineered devices. However, when compared with the RTD-TE device, they show serious improvement in $S$ at higher values of $E_f$.

assumptions, $zT$ can be expressed as

$$
zT = \frac{PF}{G_{K,el}}T, \tag{22}
$$

where $G_{K,el}$ is the open circuit electronic thermal conductivity, given by $G_{K,el}=G_Q-G_PG_S/G$. Figure 9(a) plots the $zT$ of all the devices as a function of $E_f$ which clearly reveals that the boxcar feature of the transmission significantly enhances the $zT$ throughout when compared to its peaked nature. This result is also in line with the variation of efficiency at maximum power ($\eta_{P_{max}}$) with $E_f$ as depicted in Fig. 9(b). It is observed that in the cavity based devices, the achievable limit of $zT$ and $\eta_{P_{max}}$ within the suitable operating range of $E_f\simeq4-7k_BT$ vary in between $2.5-4.5$ and $31-39\%$, respectively, which is pretty high as compared to $1.1-3.1$ and $20-34\%$ of a RTD-TE device. These results show that at respective maximum output power as shown in Fig. 4, the cavity based generators can operate at up to $10\%$ higher efficiency than that of a RTD-TE. One must also note that the range of $zT$ is almost similar in all the cavity based devices which dictates that the heat conversion ability does not degrade with an associated rise in output power. A close look on the obtained result reveals that the steady improvement of $PF$ from FP-I to FP-III is mostly suppressed by an equal rate of increase in the thermal conductivity, thereby maintaining a uniform $zT$. These results prove that the cavity engineered devices perform way better in terms of efficient heat conversion ability as compared to RTD [17] or QD [20] based generators.

The results discussed above are quantitatively summarized in Table I for a detailed comparative study of all the devices. This study would also help in designing suitable TE heat engines according to the specific output goals.

![](./images/867773434023641602_9.jpg)

FIG. 9. Comparative analysis: (a) Figure-of-Merit ($zT$) and (b) efficiency at maximum power ($\eta_{P_{max}}$) are plotted for all the devices as a function of varying $E_f$. The cavity based devices exhibit an almost similar $zT$ and $\eta_{P_{max}}$ for the entire range of $E_f$ with a significant improvement over the RTD-TE device. The range of $zT$ and $\eta_{P_{max}}$ of the cavity based devices vary between $2.5-4.5$ and $31-39\%$, respectively, within the best operating regime of $E_f$ between $4-7k_BT$.

## VI. CONCLUSION

In conclusion, we have vastly explored the different design features of the electronic Fabry-Pérot cavity over the RTD structure on achieving a nearly perfect bandpass electronic transmission. We show that there exists a specific cavity design guideline in such setups to achieve a boxcar type transmission. Based on the obtained transmission profile, we pick two sample design proposals from the allowed design space with a foresight to achieve even better thermoelectric performance than the QD, RTD, ARC or superlattice based similar existing proposals. Using the NEGF-Poisson formalism, we have presented a detailed and comparative study of the linear and non-linear performance parameters in order to justify the superiority of the cavity engineered proposals. Obtained results reveal that by following the design guideline, net deliverable power can be improved up to $18\%$ from the ARC based proposal at the same efficiency leading to an excellent trade-off between them. It is also shown that by means of cavity engineering one can achieve a maximum of $116\%$ more power at a $10\%$ higher efficiency over the RTD based heat engines. Besides, in the linear response regime, the steady improvement of the power factor does not lead to a consequent degradation in the Figure-of-merit and the Seebeck coefficient. Furthermore, we have also discussed the suitable operating regime of these devices based on the margin of improvement and specific design criteria. We believe that our study opens up a new avenue on designing transmission lineshape engineered solid state devices for various applications with the simplest of structures that can be fabricated within the existing technological framework.

<table><caption>TABLE I. Comparative study of key performance parameters.</caption>
<thead>
  <tr>
    <th>Device Configuration</th>
    <th>RTD</th>
    <th>FP-I</th>
    <th>FP-II</th>
    <th>FP-III</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$P_{max}(MW/m^{2})$</td>
    <td>0.49</td>
    <td>0.90</td>
    <td>1.03</td>
    <td>1.06</td>
  </tr>
  <tr>
    <td>$\eta P_{max}(\%)$</td>
    <td>44.66</td>
    <td>46.34</td>
    <td>46.42</td>
    <td>46.32</td>
  </tr>
  <tr>
    <td>$\eta_{max}(\%)$</td>
    <td>61.5</td>
    <td>64.1</td>
    <td>64.4</td>
    <td>64.4</td>
  </tr>
  <tr>
    <td>$PEP_{max}(MW/m^{2})$</td>
    <td>0.18</td>
    <td>0.37</td>
    <td>0.41</td>
    <td>0.42</td>
  </tr>
  <tr>
    <td>$PF_{max}$</td>
    <td>2.20</td>
    <td>4.03</td>
    <td>4.62</td>
    <td>4.82</td>
  </tr>
  <tr>
    <td>$zT_{max}$</td>
    <td>13.37</td>
    <td>14.98</td>
    <td>15.57</td>
    <td>15.09</td>
  </tr>
  <tr>
    <td>$zT_{E_{f}{\simeq 4-7k_{B}T}}$</td>
    <td>1.54-3.08</td>
    <td>2.99-4.49</td>
    <td>2.92-4.51</td>
    <td>2.93-4.51</td>
  </tr>
  <tr>
    <td>$S_{E_{f}{\simeq 4-7k_{B}T}}(mV/K)$</td>
    <td>0.15-0.21</td>
    <td>0.2-0.25</td>
    <td>0.2-0.25</td>
    <td>0.2-0.26</td>
  </tr>
</tbody>
</table>

Acknowlegements: The authors acknowledge funding from Indian Space Research Organization as a part of the RESPOND grant. This work is an outcome of the Re- search and Development work undertaken in the project under the Visvesvaraya PhD Scheme of Ministry of Elec- tronics and Information Technology, Government of In- dia, being implemented by Digital India Corporation (formerly Media Lab Asia).

[1] L. D. Hicks and M. S. Dresselhaus, Physical Review B 47, 727 (1993).

[2] L. D. Hicks and M. S. Dresselhaus, Physical Review B 47, 8 (1993).

[3] L. D. Hicks, T. C. Harman, X. Sun, and M. S. Dressel- haus, Physical Review B 53, R10493 (1996).

[4] G. D. Mahan and J. O. Sofo, Proceedings of the National Academy of Sciences 93, 7436 (1996).

[5] N. Nakpathomkun, H. Q. Xu, and H. Linke, Phys. Rev. B 82, 235428 (2010).

[6] J. P. Heremans, M. S. Dresselhaus, L. E. Bell, and D. T. Morelli, Nature Nanotechnology 8, 471 (2013).

[7] A. Singha, S. D. Mahanti, and B. Muralidharan, AIP Advances 5, 107210 (2015).

[8] A. Majumdar, Science 303, 777 (2004).

[9] G. J. Snyder and E. S. Toberer, Nature Materials 7, 105 (2008).

[10] T. C. Harman, P. J. Taylor, M. P. Walsh, and B. E. LaForge, Science 297, 2229 (2002).

[11] B. Poudel, Q. Hao, Y. Ma, Y. Lan, A. Minnich, B. Yu, X. Yan, D. Wang, A. Muto, D. Vashaee, et al., Science 320, 634 (2008).

[12] J.-H. Bahk, Z. Bian, and A. Shakouri, Phys. Rev. B 87, 075204 (2013).

[13] M. Thesberg, H. Kosina, and N. Neophytou, Journal of Applied Physics 120, 234302 (2016).

[14] A. Singha and B. Muralidharan, Scientific Reports 7, 7879 (2017).

[15] S. Hershfield, K. A. Muttalib, and B. J. Nartowt, Phys. Rev. B 88, 085426 (2013).

[16] H. Karbaschi, J. Lovén, K. Courteaut, A. Wacker, and M. Leijnse, Phys. Rev. B 94, 115414 (2016).

[17] A. Agarwal and B. Muralidharan, Applied Physics Let- ters 105, 013104 (2014).

[18] B. Sothmann, R. Sánchez, A. N. Jordan, and M. Bttiker, New Journal of Physics 15, 095021 (2013).

[19] B. Sothmann, R. Snchez, and A. N. Jordan, Nanotech- nology 26, 032001 (2015).

[20] B. Muralidharan and M. Grifoni, Phys. Rev. B 85, 155423 (2012).

[21] M. Esposito, K. Lindenberg, and C. Van den Broeck, Phys. Rev. Lett. 102, 130602 (2009).

[22] M. Esposito, R. Kawai, K. Lindenberg, and C. Van den Broeck, Phys. Rev. Lett. 105, 150603 (2010).

[23] B. De and B. Muralidharan, Phys. Rev. B 94, 165416 (2016).

[24] R. S. Whitney, Phys. Rev. Lett. 112, 130601 (2014).

[25] R. S. Whitney, Phys. Rev. B 91, 115425 (2015).

[26] C. H. Schiegg, M. Dzierzawa, and U. Eckern, Journal of Physics: Condensed Matter 29, 085303 (2017).

[27] P. Priyadarshi, A. Sharma, S. Mukherjee, and B. Mu- ralidharan, Journal of Physics D: Applied Physics 51, 185301 (2018).

[28] D. A. Broido and T. L. Reinecke, Physical Review B 51, 13797 (1995).

[29] H. H. Tung and C. P. Lee, IEEE Journal of Quantum Electronics 32, 507 (1996).

[30] S. Mukherjee, P. Priyadarshi, A. Sharma, and B. Mu- ralidharan, IEEE Transactions on Electron Devices 65, 1896 (2018).

[31] C. Pacher, C. Rauch, G. Strasser, E. Gornik, F. Elsholz, A. Wacker, G. Kießlich, and E. Schöll, Applied Physics Letters 79, 1486 (2001).

[32] S. Mukherjee and B. Muralidharan, Integrated Ferro- electrics 194, 37 (2019).

[33] J. Martorell, D. W. L. Sprung, and G. V. Morozov, Phys- ical Review B 69, 115309 (2004).

[34] G. V. Morozov, D. W. L. Sprung, and J. Martorell, J. Phys. D 335, 3052 (2002).

[35] G. Bastard, Phys. Rev. B 24, 5693 (1981).

[36] Z. C. Zhao and D. R. McKenzie, Scientific Reports 7, 12772 (2017).

[37] J. Stolle, C. Baum, R. Amann, R. Haman, T. Call, and W. Li, Superlattices and Microstructures 95, 140 (2016).

[38] S. Datta, Quantum Transport: Atom to Transistor (Cambridge University Press, 2005).

[39] S. Datta, Lessons from Nanoelectronics: A New Perspec- tive on Transport, Lecture notes series (World Scientific Publishing Company, 2012).