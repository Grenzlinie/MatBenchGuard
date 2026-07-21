# Probing universal phase diagram of dimensional crossover with an atomic quantum simulator

Jinyuan Tian, $^{1, \ast}$ Zhongcheng Yu, $^{1, \ast}$ Jing Liu, $^{2,3}$ Chi-Kin Lai, $^{1}$ Lorenzo Pizzino, $^{4}$ Chengyang Wu, $^{1}$ Hongmian Shui, $^{1,3}$ Thierry Giamarchi, $^{4, \dagger}$ Hepeng Yao, $^{1, \ddagger}$ and Xiaoji Zhou $^{1,3, \S}$

$^{1}$State Key Laboratory of Photonics and Communications,
School of Electronics, Peking University, Beijing 100871, China
$^{2}$Institute of Advanced Functional Materials and Devices, Shanxi University, Taiyuan 030031, China
$^{3}$Institute of Carbon-based Thin Film Electronics, Peking University, Shanxi, Taiyuan 030012, China
$^{4}$DQMP, University of Geneva, 24 Quai Ernest-Ansermet, CH-1211 Geneva, Switzerland

(Dated: June 24, 2025)

Dimensionality is a fundamental concept in physics, which plays a hidden but crucial role in various domains, including condensed matter physics, relativity and string theory, statistical physics, etc. In quantum physics, reducing dimensionality usually enhances fluctuations and leads to novel properties. Owing to these effects, quantum simulators in which dimensionality can be controlled have emerged as a new area of interest. However, such a platform has only been studied in specific regimes and a universal phase diagram is lacking. Here, we produce an interacting atomic quantum simulator with continuous tunability of anisotropy and temperature, and probe the universal phase diagram of dimensional crossover. At low temperatures, we identify the regimes from quantum three to zero dimensions. By increasing temperature, we observe the non-trivial emergence of a thermal regime situated between the quantum zero and integer dimensions. We show that the quantum-to-thermal transition falls into four different universality classes depending on the dimensionality. Surprisingly, we also detect a fifth type where the high-dimensional quantum system can reach the thermal phase by crossing a low-dimensional quantum regime. Our results provide a crucial foundation for understanding the projective condensed matter structures in unconventional dimensions.

The Euclidian space we live in is three-dimensional (3D), where the equations of states or motions are well defined and studied. In recent years, research objects with dimensionality different from three are widely found naturally or artificially. They usually lead to novel physical properties, quite different from the ones of the 3D world. For instance, relativity and string theory, which plays an important role in particle physics and cosmology, mostly rely on dimensions larger than three [1]. In condensed matter physics, fractal structures can play an important role. They are usually characterized by the so-called fractal dimension, which is non-integer [2, 3].

In microscopic physics, be it classical or quantum, the role of dimensionality is also essential. Even for a classical system which can be described by the Boltzmann distribution, the probability density function of kinetic energy exhibits totally different dependence between three and low dimensions [4]. In quantum physics, the distinction is even stronger owing to the very different properties of quantum fluctuation in different dimensions. Various types of high-temperature and organic superconductors show novel properties arising from reduced dimensionality [5–7]. However, controlling parameters like the tunneling rates along different directions (e.g. with pressure or chemistry) accurately and continuously, remains challenging [8, 9]. Therefore, the atomic quantum simulators, mainly realized by ultracold atoms in optical potentials, has been widely extended to low dimensional structures in recent years owing to high controllability [10–12]. In one or two dimensions, they reveal remarkable phenomena, such as the fermionization of bosons [13, 14], Tomonaga-Luttinger Liquid (TLL) [15] type of correlation, topological properties [16, 17], frustrated phase [18] and the Berezinskii-Kosterlitz-Thouless (BKT) transition [19, 20]. Although most systems are firmly based in one of the integer dimensions, some systems can, as a function of parameters, show behavior pertaining to several dimensionalities, known as dimensional crossover. In recent experiments, this phenomenon was analyzed using quantum simulators based on atomic [21–23] and photonic systems [24] in certain regimes. In these simulators, special behaviors of superfluidity and quantum correlation are observed, which reflect properties of multiple dimensions.

Temperature and interaction are two important parameters for the dimensional crossover of the quantum simulators. At zero temperature, the mechanism is clear [10, 25]. For a quantum system at dimension $D$, providing a constraint on $D'$ directions will suppress the tunneling rate along them and produce a system with dimensionality $D-D'$, see the sketch in Figs. 1(a1) and (b1). Moving to finite temperature with zero interactions, temperature will simply provoke dimensional crossover when it coincides with the kinetic energy in the transverse directions $D'$. However, the mechanism with both finite temperature and interactions is non-trivial, since the tunneling between the blocks is not of the free-particle type any more. Previous works have only carried out studies for such a system in specific regimes or for specific quantities, theoretically [15, 26–29] and experimentally [21–23, 30]. However, a study which reflects the universal properties of dimensional crossover for such a quantum simulator is lacking. Especially, the universal nature of the finite-temperature phase diagram for an interacting system is not clear.

In this work, we provide the first probe of the universal phase diagram of dimensional crossover with an atomic quantum simulator. Loading ultracold atomic system into trian

---
$^\ast$ These authors contributed equally to this work.
$^\dagger$ thierry.giamarchi@unige.ch
$^\ddagger$ hepeng.yao@pku.edu.cn
$^\S$ xjzhou@pku.edu.cn

![](./images/1144326485893447708_1.jpg)

Figure 1. **Illustration of the experiment.** (a1) Sketch of the BEC system loading into a laser potential consisting of crossover optical dipole trap (OT, red cylinders), 1D optical lattice (1D OL, green arrows, z direction) and 2D triangular optical lattices (OL, blue arrows, x-y plane). The gravity is along the y-direction, while 1D lattice is aligned along the z-direction. The yellow arrows show the two probes. (a2) The momentum distribution from the TOF images for the case with lattice depths $V_{2D}=5.0E_{r}$ and $V_{1D}=0.0E_{r}$, and temperature $T=23$ nK. The red dashed lines mark the zero-momentum area, which contains $N_{0}^{y}$ atoms. (a3) The typical behavior of $f_{c}^{y}$ (blue circles) as a function of $V_{2D}$ with the same $T$ and $V_{1D}$ as (a2). The red dashed line is the piecewise fit which decides the critical potential $V_{c}$. The grey dashed line is $f_{c}^{y}$ computed by harmonic trap approximation. (b1) The sketch for the phase diagram of dimensional crossover at zero temperature, where the quantum 3D (purple), 2D (blue), 1D (green) and 0D (yellow) regimes are presented. In each phase, the subplot depicts the structural diagram, where lattice sites (orange sphere) are connected by coupling (blue and green lines), be it coherent(solid) or incoherent(dashed). (b2) The sketch for the finite-temperature behavior observed in this work. For fixed temperature, we find a thermal phase (TH) appears between zero and positive dimensions. When increasing temperature for fixed anisotropy, we find four common quantum-to-thermal transitions and one special type, where the system reaches the thermal phase via low-dimensional quantum regimes, such as 3D-1D-TH.

gular optical lattices, we obtain an interacting simulator with high tunability of anisotropy and temperature. At tens of nano-Kelvin, we can identify quantum regimes at different di- mensionalities. By measuring the detailed phase diagram at different temperatures, two important universal features ap- pear, see Fig. 1(b2). On the one hand, for each fixed temper- ature, the thermal (TH, classical) regime always appears be- tween 0D and positive integer-D quantum regimes, which can be explained by the interplay of quantum and thermal fluctu- ations. On the other hand, by increasing temperature for fixed anisotropy, we find the quantum-to-thermal transitions falling into different universality classes for different dimensionali- ties, namely the BEC transition (3D), BKT transition (2D), TLL transition (1D) and melting effect of Mott insulator (0D) accordingly. Strikingly, we also detect a new type of transition different from these four. For some special cases, the quantum 3D system can reach the thermal state via a low dimensional quantum phase, instead of a direct transition. This suggests that, by increasing temperature, a dimensional crossover be- tween quantum systems may happen before the thermal transi- tion. Our experimental data are in good agreement with quan- tum Monte Carlo.

Our experiment starts from a Rb-87 Bose-Einstein Con- densate (BEC) in the hyperfine state $F=1$ trapped in a crossed optical dipole trap containing typically $2.5\times10^{5}$ atoms [31], see Fig. 1(a1). Its 3D s-wave scattering length is $a_{3D}=107(4)a_{0}$. By properly adjusting the magneto-optical trap (MOT) loading time before evaporative cooling, we can control the system's temperature from 16 nK up to 455 nK without significantly altering the atomic number. Then, we adiabatically ramp up a 3D optical lattice with lattice spac- ing $a=\lambda/2=532$ nm in 80 ms and hold it for 20 ms. As shown in Fig. 1(a1), our optical lattices consist of a 2D trian- gular lattice ($x$-$y$ plane, blue arrows) parallel to the direction of gravity ($y$ direction) and a 1D lattice ($z$ direction, green arrows) perpendicular to it. The laser beams for the 1D and 2D lattices have a frequency difference of 110 MHz to ensure no interference between their laser beams. The lattice depths of the 2D triangular lattice $V_{2D}$ and the 1D constrained lattice $V_{1D}$ range from 0 to $25\ E_{r}$ and 0 to $70\ E_{r}$, respectively, with an accuracy of $0.2\%$, where $E_{r}=\pi^{2}\hbar^{2}/(2ma^{2})$ is the recoil energy, with $\hbar$ the reduced Planck's constant and $m$ the mass of particles.

The experimental sequence starts from preparing the BEC at the targeted temperature. Then, we independently tune the depths of the 2D triangular and 1D lattices to tune the anisotropy of the system. After holding it for another 20 ms, we make sure the system reaches an equilibrium state [32]. Next, we remove both the optical dipole traps and lattices for 28 ms time-of-flight (TOF) and take the absorption image. With the images from the two probes along the $x$ and $z$ direc- tions (yellow arrows in Fig. 1(a1)), we observe the momentum distribution from which we extract useful information. More specifically, as suggested by Refs. [23, 28, 29, 33], we access the zero-momentum fraction along a certain direction. For in- stance, for the $y$ direction, it is defined as
$$
f_{c}^{y}=\frac{\int_{-\infty}^{+\infty}dk_{x}\int_{-\infty}^{+\infty}dk_{z}\int_{-\Delta k_{y}}^{+\Delta k_{y}}n(k)dk_{y}}{\int_{-\infty}^{+\infty}dk_{x}\int_{-\infty}^{+\infty}dk_{z}\int_{-\infty}^{+\infty}n(k)dk_{y}}, \tag{1}
$$
with $n(k)$ the momentum distribution, $\Delta k_{y}=2\pi/L_{y}$ the zero-momentum width and $L_{y}$ the system size. Such a quan- tity reflects the quantum coherence properties along certain

![](./images/1144326485893447708_2.jpg)

Figure 2. The universal phase diagram of dimensional crossover at different temperatures. (a1)-(a4) are the experimentally measured phase diagrams at initial BEC temperatures $T=23(5), 36(3), 199(25)$ and $223(29) \mathrm{nK}$, as a function of the lattice amplitudes $V_{2 \mathrm{D}}$ and $V_{1 \mathrm{D}}$. Here, we observe quantum regimes at 3D (purple), 2D (blue), 1D (green), 0D (yellow) as well as the thermal regime (TH, red). The transition points are judged by zero-momentum fraction (blue and green circles) and correlation function (yellow circles). Insets in (c1) and (d1) are a zoom around the low-lattice-depth area. Error bars are obtained from the piecewise fit as in Fig. 1 (a3). The experimental parameters are particle number $N=2.0(3) \times 10^{5}$ and 3D s-wave scattering length $a_{3 D}=107(4) a_{0}$ with trap frequencies $\left(\omega_{x}, \omega_{y}, \omega_{z}\right) / 2 \pi$ ranging from $(27,84,80) \mathrm{Hz}$ to $(60,135,121) \mathrm{Hz}$ depending on the temperature considered. (a2)-(d2) are the counterpart for (a1)-(d1), which presents the QMC simulations for equivalent homogeneous systems.

directions. It is more accurate than the visibility of the momentum diffraction peak [34] and has been proved to be efficient for studying the dimensional crossover [23, 28, 29]. From the typical momentum distribution as in Fig. 1(a2), we compute the $f_{c}^{y}$ and construct Fig. 1(a3). Clearly, we can apply a piecewise fit (dashed red line) and determine the critical lattice depth $V_{c}$ (see details in Supplementary Information). For systems at low temperatures, we always find that the large enough potential regime fits nicely with that of a harmonic oscillator (dashed grey line).

At zero temperature, the physics of such a system is qualitatively clear, see Fig. 1(b1). When both $V_{2 \mathrm{D}}$ and $V_{1 \mathrm{D}}$ are small, the system is a 3D BEC with modulated density. When increasing $V_{1 \mathrm{D}}\left(V_{2 \mathrm{D}}\right.$ resp.) while keeping $V_{2 \mathrm{D}}\left(V_{1 \mathrm{D}}\right.$ resp.) small, the coupling along the $z$ direction ( $x, y$ directions resp.) becomes incoherent, while it remains coherent along the others. This is the regime of the 2D (1D resp.) atomic quantum simulator. In the limit where both $V_{2 \mathrm{D}}$ and $V_{1 \mathrm{D}}$ are large, the system becomes effectively 0D. All sites are decoupled due to quantum fluctuations and this is equivalent to the 3D Mott-insulator regime observed in Refs. [32]. However, as mentioned above, the interacting systems at finite temperatures remain unclear and form the central focus.

We first prepare our interacting BEC at different values of initial finite temperature $T$ and measure the phase diagram as a function of $V_{2 \mathrm{D}}$ and $V_{1 \mathrm{D}}$, see Fig. 2 for four typical cases. The blue and green circles are the critical lattice depths along the two directions respectively, judged by $f_{c}^{y}$ and $f_{c}^{z}$. Notably, we benefit from the use of a triangular lattice which allows us to more easily tune the effective dimension of the system (see details in Supplementary materials). Here we always load the lattice adiabatically and thus each diagrams is isentropic. At the lowest temperature we realized, i.e., $23 \mathrm{nK}$, we find the four quantum regimes at different dimensionalities as predicted in Fig. 1(b1). To further locate the thermal regime, we scan the zero-momentum fraction and correlation length as a function of $T$ for a large scale of data points, and check when these quantities saturate at a small value (yellow circles, see details below). Interestingly, we find the thermal regime appears to be located between the zero- and positive integer dimensional quantum regimes. This behavior can be explained by the different effects of thermal fluctuations. For the 0D system, it is an incompressible insulator with finite gaps whose correlation length is independent of temperature. The quantum-to-thermal transition for such a system is the melting of the gap [35, 36], leading to a compressible thermal phase with a $T$-dependent correlation length. Thus, systems with smaller gap, i.e., smaller lattice amplitude, will be melted first. On the other hand, for quantum systems at positive integer dimensionalities, the quantum-to-thermal transition is induced by the joint contribution of quantum and thermal fluctuations. When the effective dimensionality is larger, i.e., smaller lattice amplitude, the quantum fluctuation is smaller and it calls for a higher temperature to enter the thermal phase [10-12, 37]. Thanks to the two processes mentioned above, the thermal phase appears in the mid-

![](./images/1144326485893447708_3.jpg)

Figure 3. Special category of finite temperature transition We show the zero-momentum fraction along two directions $f_c^y$ (blue circles) and $f_c^z$ (green circles) as a function of temperature $T$, for two different cases: (a1) $V_{2\mathrm{D}}=3.0\ E_{\mathrm{r}}$, $V_{1\mathrm{D}}=20.0\ E_{\mathrm{r}}$ and (b1) $V_{2\mathrm{D}}=7.0\ E_{\mathrm{r}}$, $V_{1\mathrm{D}}=5.0\ E_{\mathrm{r}}$. Error bars represent the standard deviation of five measurements. The colored areas represent the judged regimes. The white region is the estimated transition temperature from piecewise fit of experimental data and its with represent the errorbars. (a2) and (b2) are illustration for the physical pictures, where blue (red resp.) layers or tubes indicate quantum (thermal resp.) gases. Light blue (red resp.) legs indicate coherent (incoherent resp.) coupling. (a3) and (b3) are the corresponding correlation function $G^{(1)}$ along $y$ and $z$ directions at different temperatures. Experimental parameters: particle number $N=2.0(3)\times10^5$ and 3D s-wave scattering length $a_{3D}=107(4)a_0$.

dle of the phase diagram as in Fig. 2(a1). As the temperature increases, the quantum regimes shrink successively and the thermal regime expands, see Fig. 2(a1)-(d1). We find that the 0D, 1D, 2D, 3D quantum regimes disappear at the temperature of $T=36$ nK (b1), 199 nK (c1), 223 nK (d1) and 250 nK, correspondingly. This fits with our previous statement.

To further confirm our observations, we run QMC simulations of an equivalent homogeneous system (see details in Method) and generate the phase diagram by studying the superfluid stiffness, see Fig. 2(a2)-(d2). We qualitatively recover the same experimental phase diagrams. The quantitative discrepancy might be due to different factors such as the presence of the harmonic trap and the variation of the number of particles.

In order to further study the properties of the quantum-to-thermal transition, we now choose six typical points (I-VI) in Fig. 2(a1), and scan $f_c^y$ and $f_c^z$ as a function of temperature $T$ while maintaining the particle numbers $N$ almost unchanged.

The results are shown in Fig. 3 and Fig. 4. Notably, here we use $f_c^y$ to study the coherence properties in the 2D $xy$-plane thanks to the rotational symmetry of the triangular lattices (see Supplementary Information).

Although most of the cases fall into typical universality classes of quantum-to-thermal phase transition, there are some special points which show strikingly different behaviors, for instance points I and II in Fig. 2(a1). Their finite temperature properties are shown in Fig. 3. In Fig. 3(a1), we consider the lattice depth as point I and scan temperature. Interestingly, we find that $f_c^y$ and $f_c^z$ drop to a plateau at different values of temperature, namely $T_1=88\pm28$ nK and $T_2=142\pm14$ nK (white lines). This suggests, instead of a direct transition from 3D quantum to thermal phase, an intermediate 1D quantum regime emerges in between. It can be viewed as thermal fluctuation induced dimensional crossover, such that we name it "TFDC" type. Similar behavior has also been observed for another anisotropy case where $V_{1\mathrm{D}}$ is large, see Fig. 3(b1). The two $f_c$ drop to the plateau at two different temperatures, namely $T_1=119\pm19$ nK and $T_2=177\pm20$ nK (white lines). Similarly, it suggests a 3D-2D-TH process.

The TFDC behavior will happen if the system has certain anisotropy i.e., lattice amplitudes along directions $j$ and $j'$ have a certain ratio. How should we understand it? As suggested by theoretical works [26, 28, 29], the temperature competes with the effective hopping amplitude, renormalized by the interaction, leading to the dimensional crossover. When it reaches the smaller hoping amplitude $t_j$, the particles are driven by thermal fluctuations along that direction. Effectively, we have one less direction where the system behaves coherently, see illustration in Fig. 3(a2) and (b2). Therefore, as long as it happens below the thermal transition temperature, increasing temperature only eliminates the quantum coherence along $j$ direction but not the others like $j'$. This leads to a crossover from 3D quantum system to thermal regime via a low-D quantum phase.

Notably, in order to probe these behaviors, one always needs to carefully pick up a point nearby the crossover line between the 3D and low-D regimes at low temperature, such that the temperature of dimensional crossover is much lower than the one to thermal phase. Although such mechanism was proposed in condensed matter systems, detecting it precisely is challenging given the difficulty to controlling the anisotropy accurately. Thanks to the high tunability of parameters in our triangular lattice platform, we provide the first controlled test of this phenomenon.

To further confirm our demonstration, we perform two additional analyzes. First, we estimate the 3D-1D crossover temperature via field theory [29]. By treating the system as coupled quantum chains, we can perform a mean-field (MF) decoupling estimate the crossover temperature [26, 29]

$$
T_{3\text{-}1\mathrm{D}}=A_B t_\perp^{-\nu}. \tag{2}
$$

with $\nu=\frac{2K}{4K-1}$ the scaling exponent and $K$ the Luttinger parameter encoding the effect of interactions. $A_B$ is the prefactor which depends on Luttinger parameters $K$, particle density $n$ and system size $L$. Using the experimental parameters,

we find the temperature to be $T_{3\text{-1D}} = 108$ nK (purple dashed line), which fits with $T_1$ within errorbars in Fig. 3(a1).

Another proof is the data of the one-body correlation func- tion $G^{(1)}(r)=\int\langle\Psi^{\dagger}(r)\Psi(r')\rangle dr'$, which can be computed by the Fourier transform of the measured momentum dis- tribution. It reflects clearly the correlation decay pattern along single directions. In Fig. 3(a3), we show the decay of $G^{(1)}(y)$ and $G^{(1)}(z)$ at different temperatures. Clearly, above $T_1 = 88\pm28$ nK, the correlation along $y$ direction drops extremely fast (faster than 1 site) and remains unchanged for higher temperatures. On the contrary, along the $z$ direction, the correlation drops faster while temperature increases, and only remains unchanged after $T_2 = 142\pm14$ nK. This further confirms the existence of the 3D-1D-TH transition at these two temperatures. In Fig. 3(b3), similar behaviors are found for case II, where a signature of 3D-2D-TH transition is pre- sented.

Now, we turn back to discuss the other common cases of the quantum-to-thermal transitions. In Fig. 2(a2), cases like I and II are minority. The majority should fall into four dif- ferent universality class of phase transitions, namely the BEC transition (3D), BKT transition (2D), TLL transition (1D) and Mott melting (0D). Here, we pick up four points deeply in the regimes of 3D (III), 2D ( IV), 1D (V) and 0D (VI), and study the behavior of measured $f_c^y$ and $f_c^z$ as a function of temperature $T$, see Fig. 4(a)-(d), correspondingly.

In Fig. 4(a), the system starts from a 3D BEC at low tem- perature. By increasing temperature, both $f_c^y$ and $f_c^z$ drop together and reach a plateau at an identical value of $T_{3D}^{exp} = 236\pm17$ nK. Here, the transition temperature for a trapped 3D BEC writes [38]

$$
T_{3 \mathrm{D}}=T_{\mathrm{BEC}}=0.94 \frac{\hbar \bar{\omega} N^{1 / 3}}{k_{\mathrm{B}}}, \tag{3}
$$

with $N$ the atom number, $\bar{\omega}=(\omega_{x}\omega_{y}\omega_{Z})^{1/3}$ the average trap- ping frequency of the optical dipole trap, and $k_B$ the Boltz- mann constant. It gives $T_{\text{BEC}}=230$ nK (black dashed line) with our experimental parameters and fit nicely with our mea- sured $T_{3D}^{exp}$ within $2.6\%$.

For the 2D case, $f_c^z$ is always very small regardless of the value of temperature, while $f_c^y$ drops at $T_{2D}^{exp} = 151\pm23$ nK and then remains constant, see Fig. 4(b). This transition should be captured by the BKT transition class, whose transi- tion temperature can be computed as [39, 40]

$$
n_{2 \mathrm{D}} \lambda_{T_{2 \mathrm{D}}}^{2}=\ln (\xi / 4 \pi)+\ln \ln \left(1 / n_{2 \mathrm{D}} a_{2 \mathrm{D}}^{2}\right) \tag{4}
$$

where $n_{2 \mathrm{D}}$ is the 2D density, $\lambda_{T}=\sqrt{h^{2}/2\pi m k_{B}T}$ is the thermal de Broglie wavelength, $a_{2 \mathrm{D}}$ is the 2D scatter- ing length. The numerical coefficient $\xi=380$ is calculated in [39]. Here, we find $T_{\text{BKT}}=176.3$ nK (black dashed line) which fits with the observed temperature $T_{2D}^{exp}$ within $15.5\%$. Notably, for the case in Fig. 3(b1), we can also esti- mate the 2D-TH transition temperature with Eq. (4). It gives $T_{2 \mathrm{D}}=172.6$ nK (black dashed line) which fits nicely with the experimental observation within $2.5\%$.

For the 1D case, while temperature increases, we find $f_c^y$ remains a small constant while $f_c^z$ decreases up to $T_{1D}^{exp} = 95\pm23$ nK, see Fig. 4(c). This transition can be captured by the Tomonaga-Luttinger liquid theory [15, 41]. Specifically, its transition temperature writes

$$
\xi(T=T_{1 \mathrm{D}})=\frac{3 \hbar^{2} \bar{n}_{1 \mathrm{D}}}{2 m k_{B} T_{1 \mathrm{D}}} \ll L \tag{5}
$$

with $\xi$ the correlation length, $n_{1 \mathrm{D}}$ the 1D density and $L$ the system size. In practice, we take $\xi(T=T_{1 \mathrm{D}})=L/10$ and it predicts $T_{1 \mathrm{D}}=130.9$ nK (black dashed line), which fits with our observation within $31.8\%$. Similarly, we can apply this to the 1D-TH transition in Fig. 3(a1). It gives $T_{1 \mathrm{D}}=155.5$ nK (black dashed line), which fits with our observation within $8.7\%$ .

![](./images/1144326485893447708_4.jpg)

Figure 4. The common quantum-to-thermal transition for differ- ent integer dimensionalites The behavior of zero-momentum frac- tion $f_c$ along the y (blue) and z (green) directions as a function of temperature $T$. At the lowest temperature, the system is a quantum gas in the 3D (a, $V_{2 \mathrm{D}}=0.5\ E_r$, $V_{1 \mathrm{D}}=1\ E_r$), 2D (b, $V_{2 \mathrm{D}}=3.0\ E_r$, $V_{1 \mathrm{D}}=50.0\ E_r$), 1D (c, $V_{2 \mathrm{D}}=21.0\ E_r$, $V_{1 \mathrm{D}}=5.0\ E_r$) and 0D (d, $V_{2 \mathrm{D}}=25.0\ E_r$, $V_{1 \mathrm{D}}=60.0\ E_r$) regimes, respectively. Error bars represent the standard deviation of five measurements. The white region is the estimated transition temperature from the experimental data and the dashed lines are theoretical predictions. The inset of (d) shows the correlation length $\xi$ as a function of $T$. Experimental parameters: particle number $N=2.0(3)\times10^5$ and 3D s-wave scat- tering length $a_{3D}=107(4)a_0$.

The finite temperature effect for a 0D quantum system cor- responds to the melting effect discussed above. Both $f_c^y$ and $f_c^z$ are small at low temperature and remain almost un- changed with temperature, see Fig. 4(d). To further capture this melting effect, we obtain the correlation function $G_1(x)$ from the measured $n(k)$, and by performing an exponential fit $G_1(x)\sim\exp(-|x|/\xi)$, we extract the correlation length $\xi$. The temperature dependence of $\xi$ is shown in the inset. At low temperature, it exhibits a plateau. Above the melting temper- ature $T_{0D}^{exp}=35\pm8$ nK, it increases with temperature first,

reaches a maximum value and then decreases. We argue that this stems from the competition between the increasing mobil- ity of particles induced by particle-hole pair excitations, and the increasing thermal fluctuations. The scale of the melting temperature writes [42]

$$
T_{0 \mathrm{D}}=T_{\text {melt }} \sim \frac{\Delta}{k_{B}}, \quad(6)
$$

with $\Delta$ the Mott gap. Taking the parameters of our lattices, we find $\Delta=57 \mathrm{nK}$. In practice, we take $T_{\text {melt }}=0.4 \Delta / k_{B}=$28 nK and find good agreement with experiment in both Fig. 2 and Fig. 4(d).

Summarizing, we probe the universal phase diagram of di- mensional crossover for a quantum simulator at various tem- peratures, using interacting ultracold atoms in 3D anisotropic optical lattices. At various temperatures, we find quan- tum systems at different integer dimensionalities with a ther- mal phase existing in between. Furthermore, we study the quantum-to-thermal transition for systems with fixed anisotropy. Five categories of transitions are identified. Es- pecially, we provide the first controlled test of the TFDC type, benefiting from the high tunability of both temperature and anisotropy in our triangular lattice setup. Our result provides important basis for quantum simulators with unconventional dimensionalities. Given such a platform, one can potentially carry out various further detailed tests, such as what is the mixed dimensional properties at various temperatures. This kind of test also paves way to the understanding of their pro- jective structures in condensed matter systems, especially the organic conductors and high-temperature superconductors.

### Acknowledgements
The authors thank Tianwei Zhou and Zekai Chen for their helpful discussions. This work is supported by the National Key Research and Development Program of China (Grants No. 2021YFA0718300 and No. 2021YFA1400900), National Natural Science Foundation of China (Grants No. 92365208). This work is also supported by the Swiss National Science Foundation under grant number 200020-219400.

### Author Contributions:
The work was conceived by J.T., H.Y., X.Z., T.G. and Z.Y. Experiments were performed by J.T., Z.Y and C.W. Data were analyzed by J.T. and J. L. Theo- retical models and simulation were done by J.L., C.L., and L.P. Experiment preparations were done by Z.Y., C.W.,and H.S. X.Z., H.Y. and T.G. supervised this work. H.Y., J.T., Z.Y., T.G., C.L. wrote the manuscript with input from all au- thors. All authors discussed the results.

### Data Availability:
The data shown in this manuscript is available via Zenodo [43].

# Methods

## I. CONTROL OF TEMPERATURE

Our experiment starts from a Rubidium-87 Bose-Einstein Condensate (BEC) with a typical atomic number of $2.0(3) \times$ $10^{5}$ in the hyperfine state $|F=1, m_{F}=-1\rangle$, as shown in
Fig. 1. To further control the temperature of the produced BEC, we adjust the parameters of the evaporative cooling se- quence as well as the initial state before this process. On the one hand, we prepare systems with different atom numbers before the evaporative cooling. This can be achieved by ad- justing the magneto-optical trap (MOT) loading time prior to the evaporative cooling. On the other hand, we control the evaporative cooling sequence by varying both the decreasing rate and the final laser intensity. Combining these two pro- cesses properly, we can reach different temperatures while maintaining the same final atom number within a $15 \%$ dif ference. In our measurement, the temperature of the BEC can be adjusted between 23 nK and 455 nK, as inferred from the TOF images using bimodal fitting [31].

## II. THE OPTICAL LATTICE POTENTIAL

Here, we clarify the details about the 1D and 2D lattice po- tentials. In the 2D $xy$-plane, our triangular lattice is formed by three traveling beams that intersect at an enclosing angle of $120^{\circ}$, with their linear polarization perpendicular to the2D plane. The generated triangular lattice potential in the $xy$-plane is given by [30]:

$$
\begin{aligned}
V(x, y) & =-\left|E_{1}+E_{2}+E_{3}\right|^{2} \\
& =-\left|\frac{\sqrt{V_{2 \mathrm{D}}}}{2} e^{-i \vec{k}_{1} \cdot \vec{r}}+\frac{\sqrt{V_{2 \mathrm{D}}}}{2} e^{-i \vec{k}_{2} \cdot \vec{r}}+\frac{\sqrt{V_{2 \mathrm{D}}}}{2} e^{-i \vec{k}_{3} \cdot \vec{r}}\right|^{2} \\
& =-\frac{V_{2 \mathrm{D}}}{4}\left(3+2 \cos \left(\left(\vec{k}_{1}-\vec{k}_{2}\right) \cdot \vec{r}\right)\right. \\
& \quad+2 \cos \left(\left(\vec{k}_{2}-\vec{k}_{3}\right) \cdot \vec{r}\right)+2 \cos \left(\left(\vec{k}_{3}-\vec{k}_{1}\right) \cdot \vec{r}\right) \\
& =-\frac{V_{2 \mathrm{D}}}{4}\left(3+2 \cos \left(k_{0} \sqrt{3} x\right)+4 \cos \left(k_{0} \frac{\sqrt{3}}{2} x\right) \cos \left(k_{0} \frac{3}{2} y\right)\right)
\end{aligned}
$$

where $V_{2 \mathrm{D}}$ is the lattice depth of 2D triangular lattice, $k_1$,$k_2$,$k_3$ are the wave vectors of three lattice beams. In our experiment, we always have $\vec{k}_{1}=\frac{2 \pi}{\lambda}(\frac{\sqrt{3}}{2},-\frac{1}{2}), \vec{k}_{2}=$ $\frac{2 \pi}{\lambda}(-\frac{\sqrt{3}}{2},-\frac{1}{2}), \vec{k}_{3}=\frac{2 \pi}{\lambda}(0,1)$, and $|\vec{k}_{1}|=|\vec{k}_{2}|=|\vec{k}_{3}|=k_{0}$. Along the $z$-direction, we also load a 1D optical lattice formed by a 1064 nm standing wave light. This potential can be ex- pressed as $V(z)=V_{1 \mathrm{D}} \cos ^{2}(k_{0} z)$, where $V_{1 \mathrm{D}}$ is lattice depth of 1D lattice, and $k_{0}=\frac{2 \pi}{\lambda}$ the wave vector with $\lambda=1064 \mathrm{~nm}$ the laser wavelength.

## III. THE QUANTUM MONTE CARLO CALCULATIONS

Using the quantum Monte Carlo method with worm algo- rithm [48, 49], we simulate our experimental system based on the Bose-Hubbard model description at finite temperatures. Taking different temperature $T$, chemical potential $\mu$, on-site interaction $U$, and tunneling $t_{x,y,z}$ along three directions, we calculate the superfluid fraction along $i$-direction $f_{s}^{i}=\rho_{s}^{i}/\rho$($i=x,y,j$) by:

$$
f_{s, i}=\frac{m}{\hbar^{2}} \frac{\left\langle W_{i}^{2}\right\rangle L_{i}^{2-d}}{\rho d \beta}, \quad(8)
$$

where $W_i$ is the winding number along $i$ direction, $L_i$ is the corresponded system size, $d$ is the total dimensionality of the simulation and $\beta = 1/k_B T$ is the inverse temperature. For generating the phase diagrams in the main text (Fig. 2(a2)-(d2)), we compute the superfluid fraction $f_s$ as a function of lattice depth $V$ and temperature $T$. Typically, we perform $10^5$ iterations with $10^6$ warmup steps in advance, in order to make sure the Monte Carlo statistics is sufficient. The error bars of the QMC data originates from the statistical fluctuations of the sampling. Then, we determine the transition point as discussed in Fig. 1(a3) and Fig. 4. In practice, we define the criteria $f_s < 0.1\%$ [28].

[1] R. M. Wald, *General relativity* (University of Chicago press, 2010).
[2] E. Akkermans, *Statistical mechanics and quantum fields on fractals*, Contemp. Math. 601, 1 (2013).
[3] A. Jagannathan, *The fibonacci quasicrystal: Case study of hidden dimensions and multifractality*, Rev. Mod. Phys. 93, 045001 (2021).
[4] R. Pathria and P. D. Beale, in *Statistical Mechanics* (Fourth Edition) (Academic Press, 2022).
[5] J. Orenstein and A. J. Millis, *Advances in the physics of high-temperature superconductivity*, Science 288, 468 (2000).
[6] T. Giamarchi, *Theoretical framework for quasi-one dimensional systems*, Chem. Rev. 104, 5037 (2004).
[7] D. Jerome and C. Bourbonnais, *Quasi one-dimensional organic conductors: from Fröhlich conductivity and Peierls insulating state to magnetically-mediated superconductivity, a retrospective*, Comptes Rendus. Physique 25, 17 (2024).
[8] M. I. Eremets, *High Pressure Experimental Methods* (Oxford University Press, 1996).
[9] M. Dressel, K. Petukhov, B. Salameh, P. Zornoza, and T. Giamarchi, *Scaling behavior of the longitudinal and transverse transport in quasi-one-dimensional organic conductors*, Phys. Rev. B 71, 075104 (2005).
[10] I. Bloch, J. Dalibard, and W. Zwerger, *Many-body physics with ultracold gases*, Rev. Mod. Phys. 80, 885 (2008).
[11] Z. Hadzibabic and J. Dalibard, *Two-dimensional Bose fluids: An atomic physics perspective*, Riv. Nuovo Cim. 34, 389 (2011).
[12] M. A. Cazalilla, R. Citro, T. Giamarchi, E. Orignac, and M. Rigol, *One dimensional bosons: From condensed matter systems to ultracold gases*, Rev. Mod. Phys. 83, 1405 (2011).
[13] B. Paredes, A. Widera, V. Murg, O. Mandel, S. Folling, I. Cirac, GV. Shlyapnikov, TW. Hansch, and I. Bloch, *Tonks-Girardeau gas of ultracold atoms in an optical lattice*, Nature 429, 277 (2004).
[14] T. Kinoshita, T. Wenger, and D. S. Weiss, *Observation of a one-dimensional Tonks-Girardeau gas*, Science 305, 1125 (2004).
[15] T. Giamarchi, *Quantum physics in one dimension*, vol. 121 of *International Series of Monographs on Physics* (Oxford University Press, Oxford, 2004).
[16] N. Goldman, J. Dalibard, A. Dauphin, F. Gerbier, M. Lewenstein, P. Zoller, and I. B. Spielman, *Direct imaging of topological edge states in cold-atom systems*, Proc. Natl. Acad. Sci. U.S.A. 110, 6736 (2013).
[17] M. Tarnowski, F. N. Ünal, N. Fläschner, B. S. Rem, A. Eckardt, K. Sengstock, and C. Weitenberg, *Measuring topology from dynamics by obtaining the Chern number from a linking number*, Nat. Commun. 10, 1728 (2019).
[18] J. Struck, C. Ölschläger, R. L. Targat, P. Soltan-Panahi, A. Eckardt, M. Lewenstein, P. Windpassinger, and K. Sengstock, *Quantum simulation of frustrated classical magnetism in triangular optical lattices*, Science 333, 996 (2011).

[19] Z. Hadzibabic, P. Krüger, M. Cheneau, B. Battelier, and J. Dalibard, *Berezinskii-kosterlitz-thouless crossover in a trapped atomic gas*, Nature 441, 1118 (2006).
[20] L.-C. Ha, C.-L. Hung, X. Zhang, U. Eismann, S.-K. Tung, and C. Chin, *Strongly interacting two-dimensional bose gases*, Phys. Rev. Lett. 110, 145302 (2013).
[21] G. Chauveau, C. Maury, F. Rabec, C. Heintze, G. Brochier, S. Nascimbene, J. Dalibard, J. Beugnon, S. M. Roccuzzo, and S. Stringari, *Superfluid fraction in an interacting spatially-modulated Bose-Einstein condensate*, Phys. Rev. Lett. 130, 226003 (2023).
[22] J. Tao, M. Zhao, and I. B. Spielman, *Observation of anisotropic superfluid density in an artificial crystal*, Phys. Rev. Lett. 131, 163401 (2023).
[23] Y. Guo, H. Yao, S. Ramanjanappa, S. Dhar, M. Horvath, L. Pizzino, T. Giamarchi, M. Landini, and H.-C. Nägerl, *Observation of the 2D–1D crossover in strongly interacting ultracold bosons*, Nat. Phys. 20, 934 (2024).
[24] K. Karkihalli Umesh, J. Schulz, J. Schmitt, M. Weitz, G. von Freymann, and F. Vewinger, *Dimensional crossover in a quantum gas of light*, Nat. Phys. 20, 1810 (2024).
[25] A. Ho, M. Cazalilla, and T. Giamarchi, *Deconfinement in a 2D optical lattice of coupled 1D boson systems*, Phys. Rev. Lett. 92, 130405 (2004).
[26] M. A. Cazalilla, A. F. Ho, and T. Giamarchi, *Interacting bose gases in quasi-one-dimensional optical lattices*, New J. Phys. 8, 158 (2006).
[27] G. Bollmark, N. Laflorencie, and A. Kantian, *Dimensional crossover and phase transitions in coupled chains: Density matrix renormalization group results*, Phys. Rev. B 102, 195145 (2020).
[28] H. Yao, L. Pizzino, and T. Giamarchi, *Strongly-interacting bosons at 2D-1D dimensional crossover*, SciPost Phys. 15, 050 (2023).
[29] L. Pizzino, H. Yao, and T. Giamarchi, *Finite size analysis for interacting bosons at the one-two dimensional crossover*, Phys. Rev. Res. 7, 013021 (2025).
[30] S. Jin, X. Guo, P. Peng, X. Chen, X. Li, and X. Zhou, *Finite temperature phase transition in a cross-dimensional triangular lattice*, New J. Phys. 21, 073015 (2019).
[31] S. Jin, W. Zhang, X. Guo, X. Chen, X. Zhou, and X. Li, *Evidence of potts-nematic superfluidity in a hexagonal $sp^2$ optical lattice*, Phys. Rev. Lett. 126, 035301 (2021).
[32] M. Greiner, O. Mandel, T. Esslinger, T. W. Hänsch, and I. Bloch, *Quantum phase transition from a superfluid to a mott insulator in a gas of ultracold atoms*, Nature 415, 39 (2002).
[33] T. Plisson, B. Allard, M. Holzmann, G. Salomon, A. Aspect, P. Bouyer, and T. Bourdel, *Coherence properties of a two-dimensional trapped bose gas around the superfluid transition*, Phys. Rev. A 84, 061606 (2011).
[34] Y. Kato, Q. Zhou, N. Kawashima, and N. Trivedi, *Sharp peaks in the momentum distribution of bosons in optical lattices in the normal state*, Nat. Phys. 4, 617 (2008).

[35] B. DeMarco, C. Lannert, S. Vishveshwara, and T.-C. Wei, Structure and stability of mott-insulator shells of bosons trapped in an optical lattice, Phys. Rev. A 71, 063601 (2005).

[36] H. Yao, T. Giamarchi, and L. Sanchez-Palencia, Lieb-liniger bosons in a shallow quasiperiodic potential: Bose glass phase and fractal mott lobes, Phys. Rev. Lett. 125, 060401 (2020).

[37] L. Pitaevskii and S. Stringari, Bose-Einstein Condensation (Clarendon Press, Oxford, 2003).

[38] M. H. Anderson, J. R. Ensher, M. R. Matthews, C. E. Wieman, and E. A. Cornell, Observation of Bose-Einstein Condensation in a dilute atomic vapor, Science 269, 198 (1995).

[39] N. Prokof'ev, O. Ruebenacker, and B. Svistunov, Critical point of a weakly interacting two-dimensional bose gas, Phys. Rev. Lett. 87, 270402 (2001).

[40] S. Pilati, S. Giorgini, and N. Prokof'ev, Critical temperature of interacting bose gases in two and three dimensions, Phys. Rev. Lett. 100, 140405 (2008).

[41] A. Del Maestro and I. Affleck, Interacting bosons in one dimen- sion and the applicability of luttinger-liquid theory as revealed by path-integral quantum monte carlo calculations, Phys. Rev. B 82, 060515 (2010).

[42] F. Gerbier, Boson mott insulators at finite temperatures, Phys. Rev. Lett. 99, 120405 (2007).

[43] Data set is available from zenodo at doi: 10.5281/zen- odo.15308183.

[44] Y. Guo, H. Yao, S. Dhar, L. Pizzino, M. Horvath, T. Giamarchi, M. Landini, and H.-C. Nägerl, Anomalous cooling of bosons by dimensional reduction, Sci. Adv. 10, eadk6870 (2024).

[45] N. Fabbri, M. Panfil, D. Clément, L. Fallani, M. Inguscio, C. Fort, and J.-S. Caux, Dynamical structure factor of one- dimensional bose gases: Experimental signatures of beyond- luttinger-liquid physics, Phys. Rev. A 91, 043617 (2015).

[46] F. Meinert, M. Panfil, M. J. Mark, K. Lauber, J.-S. Caux, and H.-C. Nägerl, Probing the excitations of a lieb-liniger gas from weak to strong coupling, Phys. Rev. Lett. 115, 085301 (2015).

[47] K.-Y. Li, Y. Zhang, K. Yang, K.-Y. Lin, S. Gopalakrishnan, M. Rigol, and B. L. Lev, Rapidity and momentum distributions of one-dimensional dipolar quantum gases, Phys. Rev. A 107, L061302 (2023).

[48] M. Boninsegni, N. Prokof'ev, and B. Svistunov, Worm algo- rithm for continuous-space path integral monte carlo simula- tions, Phys. Rev. Lett. 96, 070601 (2006).

[49] M. Boninsegni, N. V. Prokof'ev, and B. V. Svistunov, Worm algorithm and diagrammatic monte carlo: A new approach to continuous-space path integral monte carlo simulations, Phys. Rev. E 74, 036701 (2006).

# Supplemental Material for

## Probing universal phase diagram of dimensional crossover with an atomic quantum simulator

In this supplemental material, we provide details about the comparison between different lattice geometries, experimental details, determination of the critical potentials and the properties in the 2D planes.

## S1. COMPARISON BETWEEN DIFFERENT LATTICE GEOMETRIES

![](./images/1144326485893447708_5.jpg)

Figure S1. **Plot of $zt-V$ for different lattice geometries.** The product of tunneling coefficient $t$ and coordination number $z$ as a function of the lattice depth $V$ is shown for the two-dimensional triangular (blue), square (red), and honeycomb lattices (yellow). The dashed line on the graph represents $zt=0.002\ E_\text{r}$. Its intersection with the $V-zt$ curve for the triangular lattice occurs at $8.5\ E_\text{r}$, indicating the lattice depth at which the system undergoes a 3D-1D dimensional crossover at low temperatures. Based on this criterion, the critical lattice depths for the square and honeycomb lattices are found to be $29.5\ E_\text{r}$ and $92.2\ E_\text{r}$, respectively.

In this section, we discuss the effect of different lattice geometries on the phase diagrams and verify the advantages of using a triangular lattice. As we argued in the main text, when we use different lattice structures with different nearest neighbor values $z$, the physics remains unchanged. For instance, the critical tunneling value of the 3D-1D crossover writes [26]

$$
t_c = \frac{1}{z}\alpha(\rho, v_s, m)T^{2-1/2K}, \tag{S1}
$$

where pre-factor $\alpha(\rho_0, v_s, m)$ is the function of the sound velocity $v_s$, 1D density $\rho_0$, and atomic mass $m$. The temperature dependence of $t_c$ is a power law whose exponent is determined by the Luttinger parameter $K$. The product of $K$ and $v_s$ is fixed by Galilean invariance, as $v_sK=\hbar\pi\rho_0/m$ [26].

For the triangular lattice, we observe a clear 3D to 1D crossover at 23 nK when $V_{2\text{D}}$ is approximately $8.5\ E_\text{r}$, as shown in Fig. 2 of the main text. According to Eq. S1, when the other parameters are the same, the 3D to 1D crossover occurs at the same $zt$ for different lattice geometries. For triangular lattices ($z=6$) that we studied, we find $zt=0.002\ E_r$ for $V_\text{tri}=8.5\ E_\text{r}$. In contrast, for square lattices ($z=4$) and honeycomb lattices ($z=3$), $zt=0.002\ E_r$ leads to $V_\text{sq}=29.5\ E_\text{r}$ and $V_\text{hon}=92.2\ E_\text{r}$, correspondingly, as shown in Fig. S1. This suggests that much higher laser power is required to detect the full phase diagram of dimensions in square and honeycomb lattices. On the one hand, this may exceed the actual laser power limit of the experiment. On the other hand, such high laser power may heat transmissive optical components, causing laser intensity feedback fluctuations and beam waist displacement, ultimately leading to instability in lattice depths.

## S2. ADDITIONAL EXPERIMENTAL DETAILS

After preparing the BEC, it is loaded into the optical lattice, which divides the BEC into either 2D layers or 1D tubes, allowing us to investigate different dimensionalities in the system. During the loading process, the BEC exhibits a 3D density distribution $n(x,y,z)$ that follows the Thomas-Fermi (TF) profile and is normalized such that $\int dx dy dz\ n(x,y,z)=N$, where $N$ is the

total particle number. By projecting this 3D distribution onto the discretized lattice configuration $n(i,j,k)$, we can calculate the atom number in layers along the lattice sites for the constrained lattice $N_k$ (2D case) or in tubes allocated at lattice sites in the triangular lattice $N_{i,j}$ (1D case). The weighted atom numbers for the effective 2D layer or 1D tube are evaluated as: [23, 44-47]

$$
\overline{N}_{2 \mathrm{D}}=\frac{\sum_{k} N_{k}^{2}}{\sum_{k} N_{k}} \quad \text { and } \quad \overline{N}_{1 \mathrm{D}}=\frac{\sum_{i, j} N_{i, j}^{2}}{\sum_{i, j} N_{i, j}}. \tag{S2}
$$

In practice, we find that the weighted atom numbers for the effective 2D and 1D systems in our experiment are $\overline{N}_{2 \mathrm{D}}=13,000$ and $\overline{N}_{1 \mathrm{D}}=620$, respectively.

Moreover, for distinguishing the 0D and thermal phases, we need to measure the correlation length $\xi$. By applying Fourier transform to the momentum distribution $n(k)$ obtained from the TOF images, we obtain the integrated correlation function $G^{(1)}$ which can be written:

$$
G^{(1)}(x)=\int \frac{d x^{\prime}}{L}\left\langle\Psi\left(x^{\prime}+x\right) \Psi\left(x^{\prime}\right)\right\rangle \tag{S3}
$$

For 1D atomic gases under the typical experimental condition, i.e.at nano-Kelvin temperature scale and with the presence of a harmonic trap, the $G^{(1)}$ is usually dominated by an exponential decay [23]. This is also the case for all of our experimental measurements. Therefore, by fitting $G^{(1)}(x) \sim e^{-x / \xi}$, we obtain the correlation length at various temperatures and lattice depths, as shown in Fig. 4(d) of the main text. Such a curve allows us to distinguish the 0D phase from the thermal phase.

![](./images/1144326485893447708_6.jpg)

Figure S2. Zero-momentum fraction $f_c$ versus lattice depths. The zero-momentum fraction in the $z$-direction $f_c^z$ (left panel) and $y$-direction $f_c^y$ (right panel) is displayed as a function of the lattice depths $V_{1 \mathrm{D}}$ and $V_{2 \mathrm{D}}$. The figure combines experimental data with interpolated values to provide a smooth presentation of the underlying trend. Experimental parameters: Temperature $T=16 \mathrm{nK}, N=2.0(3) \times 10^5$, 3D s-wave scattering length $a_{3 \mathrm{D}}=107(4) a_0$. and the trap frequencies $(\omega_x, \omega_y, \omega_z) / 2 \pi=(27,84,80) \mathrm{Hz}$.

## S3. DETERMINATION OF THE CRITICAL POTENTIALS

To calculate the critical points for the dimensional crossover, we use the zero-momentum fraction $f_c^i$ along the $i$-direction as the criterion. According to Refs. [23, 29], this quantity is as effective as the superfluid fraction for determining the crossover point.

From the TOF images in our experiment, we can extract the zero-momentum fractions in the $y$- and $z$-directions, denoted by $f_c^y$ and $f_c^z$, which reflect the coherence in the 2D triangular lattice plane and the 1D constrained lattice direction, respectively. In Fig. S2, we show typical examples of their behavior as functions of the lattice depths $V_{1 \mathrm{D}}$ and $V_{2 \mathrm{D}}$. Clearly, the zero-momentum fraction $f_c^j$ decays as the lattice depth along the corresponding direction $i$ increases. In each subfigure, we observe two distinct regions. At low lattice depths along the $j$-direction, $f_c^j$ remains high, but as $V_j$ increases, $f_c^j$ rapidly decays and then converges to a constant. Theoretically, the superfluid fraction should exhibit a similar qualitative behavior.

Next, we focus on specific cuts of Fig. S2, as illustrated by the four representative cases in Fig. S3. At low lattice depths, increasing the depth exponentially reduces the tunneling coefficient between lattice sites, causing $f_c$ to decay rapidly. When the lattice depth exceeds the dimensional crossover point, the lattice sites become incoherently coupled, and the system can be treated as a collection of separate harmonic oscillators along the transverse direction. Further increasing the lattice depth only increases the trapping frequency, which in turn broadens the momentum distribution of the ground state. As shown in Fig. S3, we apply the piecewise fitting to the $f_c$ curves to determine the critical lattice depth $V_c$.

![](./images/1144326485893447708_7.jpg)

Figure S3. Typical $f_c - V$ curves across dimensional crossovers at low temperatures. We present four typical dimensional crossover measurements by studying $f_c^y$ and $f_c^z$ as a function of both $V_{1D}$ and $V_{2D}$. The four plots correspond to: (1). 3D-1D crossover with $V_{1D}=0\ E_r$; (2) 2D-0D/TH crossover with $V_{1D}=60\ E_r$; (3) 3D-2D crossover with $V_{2D}=0\ E_r$; (4) 1D-0D/TH crossover with $V_{2D}=21\ E_r$. The red dashed line represents piecewise fitting, and the inflection point of the line marks the critical point of crossover. The gray dashed line represents the $f_c^y$ or $f_c^z$ calculated using the harmonic oscillator (HO) approximation for a single lattice site, where the deviation occurs from the data indicating the critical point. The error bars represent the standard deviation from five measurements. Experimental parameters: Temperature $T=16$ nK, $N=2.0(3)\times10^5$, 3D s-wave scattering length $a_{3D}=107(4)a_0$, and the trapping frequencies $(\omega_x,\omega_y,\omega_z)/2\pi=(27,84,80)$ Hz.

Additionally, we calculate the zero-momentum fraction for an equivalent quantum harmonic oscillator, denoted as $f_{\text{harm}}^i$, represented by the grey dashed lines [23]

$$
f_{\text{harm}}^i = \frac{\int_{-\Delta k_i}^{-\Delta k_i} n_{\text{HO}}(k_i)dk_i}{\int_{-\infty}^{+\infty} n_{\text{HO}}(k_i)dk_i}, \quad n_{\text{HO}}(k_i) = \left(\frac{1}{\pi\hbar m\omega_i}\right)^{1/2} \exp\left(-\frac{\hbar k^2}{m\omega_i}\right) \tag{S4}
$$

where $m$ and $\omega_i/2\pi$ are the atomic mass and the transverse trapping frequency, respectively. At low temperatures, the point where $f_c^i$ and $f_{\text{harm}}$ begin to coincide corresponds to the critical point $V_c$, at which the superfluid fraction disappears [23]. For all subfigures in Fig. S3, we observe that $f_{\text{harm}}$ fits well with the experimental data when $V>V_c$, while the two curves separate when $V<V_c$. However, at higher temperatures, due to thermal excitation, atoms occupy excited states in addition to the ground state of the harmonic trap, causing $f_c^i$ to be lower than $f_{\text{harm}}$ even at high lattice depths. Despite this, the two distinct decay regimes of $f_c$ remain apparent, allowing us to determine $V_c$ based on a piecewise fit.

### S4. PROPERTIES IN THE 2D PLANE

In this section, we verify why we can use the information along $y$ directions to represent the physics in the 2D $x-y$ plane. Thanks to the $C_6$ rotational symmetry of the triangular lattice, we expect $f_c$ along x and y directions to exhibit the same property. To prove this, we take TOF images in the $x-y$ plane for typical parameter values. One example is shown in Fig. S4, where we take the 1D lattice depth $V_{1D}=5\ E_r$ and temperature $T=16$ nk. We modify the 2D lattice depth to achieve a dimensional crossover from 3D to 1D. When $V_{2D}$ increases, the central atomic cluster gradually becomes dispersed showing no anisotropy, which suggests the superfluid along x and y directions disappear at the same time.

Furthermore, we use a set of experimental data to illustrate our statement quantitatively, as shown in Fig. S4. Apparently, the $f_c$ line shapes in both $x$ and $y$ directions are consistent, with similar magnitudes, and the phase transition points are essentially

![](./images/1144326485893447708_8.jpg)

Figure S4. $f_c - V_{2D}$ curves along $x$, $y$ directions and angular averaged. The blue circles show the zero-momentum fraction along x direction $f_c^x$, y direction $f_c^y$, and the angular averaged radius $f_c^r$. The red dashed lines represent the common critical point $V_c$ obtained from these three curves. The error bars represent the standard deviation of five measurements. Experimental parameters: Temperature $T = 16$ nK, $N = 2.0(3) \times 10^5$, 3D s-wave scattering length $a_{3D} = 107(4)a_0$.

identical. We also perform angular averaging of the TOF image to obtain the momentum distribution as a function of the scalar momentum $|\mathbf{k}|$, which allows us to calculate the angularly averaged zero-momentum fraction $f_c^r$. In Fig. S4 , we find that the behavior of $f_c^r$ is consistent with that of $f_c^x$ and $f_c^y$, in terms of the line shapes, magnitudes, and critical points. This proves our statement and assures that we can determine the phase transition points solely by measuring $f_c^y$ in the $y$-$z$ plane.