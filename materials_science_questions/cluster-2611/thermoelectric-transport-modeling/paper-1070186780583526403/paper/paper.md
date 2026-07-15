https://doi.org/10.1038/s41524-024-01459-4

# First principles methodology for studying magnetotransport in narrow gap semiconductors with $ZrTe_5$ example

Hanqi Pi$^{1,2}$, Shengnan Zhang$^{1}$ 📧, Yang Xu$^{1,2}$, Zhong Fang$^{1,2}$, Hongming Weng$^{1,2,3}$ 📧 & Quansheng Wu$^{1,2}$ 📧

The origin of resistivity peak and sign reversal of Hall resistivity in $ZrTe_5$ has long been debated. Despite various theories proposed to explain these unique transport properties, there's a lack of comprehensive first principles studies. In this work, we employ first principles calculations and Boltzmann transport theory to explore transport properties of narrow-gap semiconductors across varying temperatures and doping levels within the relaxation time approximation. We simulate the temperature-sensitive chemical potential and relaxation time in semiconductors through proper approximations, then extensively analyze $ZrTe_5$'s transport behaviors with and without an applied magnetic field. Our results reproduce crucial experimental observations such as the zero-field resistivity anomaly, nonlinear Hall resistivity with sign reversal, and non-saturating magnetoresistance at high temperatures, without introducing topological phases and/or correlation interactions. Our approach provides a systematic understanding based on multi-carrier contributions and Fermi surface geometry, and could be extended to other narrow-gap semiconductors to explore novel transport properties.

The galvanomagnetic properties of solids, describing transport behaviors of charge carriers driven by electric and magnetic fields, have been intensively studied for their potential applications in both fundamental and industrial research. In the realm of fundamental scientific research, the galvanomagnetic response is a powerful tool to investigate the electronic structure$^{1-7}$, topological properties$^{8-11}$ and scattering mechanism$^{12,13}$ of materials. In industrial applications, materials with strong magnetic responses are promising candidates for magnetometer$^{14-17}$ and hard drives$^{18}$. However, the galvanomagnetic phenomena influenced by both intrinsic and extrinsic effects have distinct origins in various systems. This complexity makes it challenging to interpret certain magneto-transport behaviors despite extensive studies. For instance, the extremely large magnetoresistance (XMR) can be attributed to nontrivial band topology$^{19,20}$, charge carrier compensation$^{21,22}$ and open orbitals of charge carriers$^{23,24}$. The planar Hall effect can arise from the strong spin-orbital coupling in magnetic material$^{25-27}$, anisotropy of Fermi surfaces$^{28-32}$ and the chiral anomaly in topological semimetals$^{33-36}$. Furthermore, the nonlinearity of Hall resistivity might indicate the presence of multi-carrier behavior or suggest the occurrence of the anomalous Hall effect.

$ZrTe_5$ has been extensively studied since the 1970s due to its remarkable thermoelectric properties and its resistivity anomaly accompanying sign reversal of Hall resistivity and Seebeck coefficients$^{37-42}$. Plenty of mechanisms have been proposed to explain this anomalous peak, such as the Lifshitz transition$^{43}$, topological phase transition$^{44}$, formation of Dirac polarons$^{45}$ and thermally excited charge carriers$^{46}$. In addition, the nonlinear Hall resistivity has been regarded as the anomalous Hall effect (AHE) originating from the Berry curvature$^{47-51}$. Many other novel properties, such as the topological edge states$^{52-55}$, chiral magnetic effect$^{48,56}$, and quantum Hall effect$^{1}$, are believed to be connected with the nonzero Berry curvature in $ZrTe_5$. However, some experimental results cannot be explained by the Berry curvature mechanism. For example, the Landé $g$-factor of $ZrTe_5$, ranging between 21 and $26^{57-59}$, is insufficient to induce Weyl nodes through Zeeman splitting$^{48,50}$ and hence generate the nonzero Berry curvature. Meanwhile, the multi-carrier model has proved to be efficient in some recent experiments and theoretical works$^{37,57,60}$.

Various models have been proposed to explain the unusual transport properties of $ZrTe_5$, yet there's a lack of comprehensive first principles studies that simulate without assumed parameters. Moreover, $ZrTe_5$ is a typical narrow-gap semiconductor, of which the transport behaviors sensitively depend on the temperature and chemical potential. Therefore we employ first principles calculations combined with the Boltzmann transport

---

$^{1}$Beijing National Laboratory for Condensed Matter Physics and Institute of Physics, Chinese Academy of Sciences, Beijing, 100190, China. $^{2}$University of Chinese Academy of Sciences, Beijing, 100049, China. $^{3}$Songshan Lake Materials Laboratory, Dongguan, Guangdong, 523808, China.
📧 e-mail: shengnan.zhang@iphy.ac.cn; hmweng@iphy.ac.cn; quansheng.wu@iphy.ac.cn

https://doi.org/10.1038/s41524-024-01459-4

Article

theory to systematically investigate the galvanomagnetic property of ZrTe₅ at different doping densities and temperatures. We want to stress that the method for ZrTe₅ is more complicated than our previous one for metals/semimetals²⁴. On the one hand, the chemical potential and charge carrier density of ZrTe₅ varies with the temperature sensitively. Meanwhile, the relaxation time cannot be obtained simply and directly as in metals/semi- metals. Therefore it is important to treat these two variables with proper approximations to enhance the alignment between the simulation and experiment, which is the innovation and necessity of this work. To achieve this, we first calculate the temperature-dependent chemical potential by fixing the total electron density, then obtain the product of temperature- dependent resistivity and relaxation time for different doping densities through an interpolation scheme. Finally, we fit the relaxation time using Bloch-Grüneisen model and get the magneto-resistivity at different tem- peratures and doping densities.

Our method, without incorporating topological effects or correlation interactions, successfully reproduces the essential experimental character- istics, including the anomalous peak of the temperature-dependent resis- tivity, the nonlinearity and sign reversal of Hall resistivity, and the non- saturating magnetoresistance (MR) at high temperatures³⁷⁴⁷⁶⁰⁻⁶². More generally and importantly, our methodology can be extended to study other narrow-gap semiconductors. We believe our work provides invaluable insights into the unique behaviors exhibited by ZrTe₅ and paves the way for further understanding and exploration of other materials with similar properties.

## Results
### Resistivity anomaly
ZrTe₅, a typical transition-metal pentatelluride compound and a repre- sentative narrow-gap semiconductor, has been extensively studied due to its prominent thermoelectric properties. Before subjecting it to the magnetic field, we shall first study its temperature-dependent resistivity at zero field due to its inherent thermal sensitivity as a semiconductor. We present the calculated band structure of ZrTe₅ and the corresponding high symmetry path in the Brillouin zone in Fig. 1a, b. It is shown in Fig. 1b that an indirect narrow gap of about 73 meV occurs along the $\Gamma-Z$ direction with strong electron-hole asymmetry. The applied current and magnetic field are par- allel to the crystallographic $a$ and $b$ axis, respectively and the orientation of magnetic field is denoted as the $z$-axis as shown in Fig. 1a.

Because the transport behavior is highly dependent on the doping levels⁶⁰, we calculated the temperature-dependent chemical potential $\mu(T)$ with a series of doping levels, as shown in Fig. 1c. The calculation details could be found in the Methods section. The doping level is denoted as $n_0 = n_e - n_h$, where positive/negative values represent electron/hole doping systems. As shown in Fig. 1c, the chemical potentials move towards the middle of the energy gap with increasing temperature, irrespective of the type of doping. This agrees qualitatively with the angle-resolved photo- emission spectroscopy (ARPES) observation⁵⁴ and results from the intrinsic thermodynamics of materials that the chemical potential favors a lower density of states (DOS) with increasing temperatures⁶³. Note that when the doping level is fixed as $n_0 = 0$, the chemical potential is ill-defined at low temperature. Therefore we only sketch the tendency of $\mu$ at low temperature relying on the results at higher temperatures, as shown by the green dashed line segment in Fig. 1c.

Furthermore, we calculate the temperature-dependent resistivity at different doping levels as shown in Fig. 1d. The procedure of calculating resistivity across various temperatures and doping densities is described in the Methods section. The resistivities of all doped systems (excluding the charge-neutral system) increase at low temperatures and then drop quickly after attaining their peaks at critical temperatures $T_P$. In order to discuss the origin of the resistivity anomaly, we introduce two important variables: the total charge carrier concentration $n_t = n_e + n_h$, which might vary with temperature due to thermal excitation, and the doping level $n_0 = n_e - n_h$, assumed as a constant. At low temperatures, where the thermal energy is insufficient to excite electrons from valence bands to conduction bands, $n_t$ remains nearly unchanged. Because the relaxation time decreases with temperature, the resistivity increases and ZrTe₅ behaves like a metal. However, as the temperature rises sufficiently to excite electrons from valence bands to conduction bands and generate electron-hole pairs, $n_t$ increases and ZrTe₅ behaves like a semiconductor.

The contradictory dependence on temperature of relaxation time and total charge carrier concentration implies the existence of a critical tem- perature $T_P$, at which the resistivity stops increasing with temperature. To further investigate the resistivity anomaly, we mark resistivity peaks at $T_P$ with black squares in Fig. 1d. We found that $T_P$ grows with the magnitude of $n_0$. This behavior is due to the higher temperatures required to generate thermal electron-hole pairs in systems with larger doping densities. More- over, given that ZrTe₅ has a significant particle-hole asymmetry, $T_P$ of electron-doped is lower than that of the hole-doped with the same mag- nitude of $n_0$, owing to the larger DOS of conduction bands³⁷⁶⁰. Similar multi- carrier and thermally-excited-carrier theories have been proposed in pre- vious works³⁷⁴⁵⁴⁶⁶⁰.

### Sign reversal of Hall resistivity
Until now, we have been only concerned with the resistivity in the absence of a magnetic field. In the following, we are going to investigate the magne- totransport properties. The computation of magnetoconductivity is based on Eq.(4)-(6) and utilizes the interpolation methods described in the Methods

![](./images/1070186780583526403_1.jpg)

Fig. 1 | The Brillouin zone, band structure, temperature-dependent chemical potential, and zero-field resistivity of ZrTe₅. a The Brillouin zone of ZrTe₅. The applied current and magnetic field are parallel to the crystallographic $a$- and $b$- axes, respectively. The orientation of magnetic field is denoted as $z$ axis throughout the text. b The band structure of ZrTe₅. c The temperature-dependent chemical potential with different doping densities $n_0$ indicated by different colors. ZrTe₅ with $n_0>0$ is electron doped while $n_0<0$ means hole-doped ZrTe₅. The low and high horizontal black dashed lines denote the valence band maximum (VBM) $=-40$ meV and conduction band minimum (CBM) $=33$ meV, respectively. The green dash line is the extrapolated che- mical potential of $n_0=0$ cm⁻³ at $T<70K$ which cannot be well determined with non-zero energy gap. d The temperature-dependent zero-field resistivity with different doping densities. The inset shows the resistivity of hole-doped ZrTe₅. The small black square denotes the peak of resistivity. We use a color bar to indicate the relation between colors and doping densities.

npj Computational Materials|(2024)10:276

section. This section also explains the relationship between low-field Hall conductivity and electron trajectories, detailed in Eq. (7). Here, the transverse conductivity, $\sigma_{xy}$, is expressed in terms of the area, $\mathcal{A}(k_z)$, swept by the "scattering path length" $l \equiv v(\boldsymbol{k})\tau$ (see Supplementary Information for detailed derivation of Eq. (7)). Meanwhile, the orbital trajectories of electrons in $\boldsymbol{k}$ space can be divided into two categories. One is the orbits only composed of convex part, which is transformed to a simple $I$ path with single loop and a certain circulation orientation. Thus the corresponding Hall resistivity exhibits the expected sign. The other one is the orbits with concave segments, which are converted into intersected $I$ path with second loops adjacent to the primary one and hence might change circulation orientations of the whole (or part of) orbit. Whether and to what extent the circulation orientation of the orbit changed depends on the fine curvature of the $\boldsymbol{k}$ orbits and decides the final sign of Hall conductivity of this single orbit⁶⁴.

When both electron and hole charge carriers contribute to electric current, the competition between them is crucial to diagnose the behavior of $\rho_{yx}$, such as the nonlinearity or sign reversal features. Intuitively, the charge carrier with a larger concentration dominates the transport. However, it only holds under the condition of sufficiently strong magnetic fields. At the low magnetic field, charge carriers only trace part of the orbit, the specific area $\mathcal{A}(k_z)$ swept by $I$ sensitively depends on the fine structure of the Fermi surface and orientation of the magnetic field. Accordingly, we classify the characteristic quantities of the cyclotron movement $\omega_c\tau=\frac{eB\tau}{m^*}$ ($m^*$ is the cyclotron mass) into two limiting cases, i.e., $\omega_c\tau \ll 1$ (low-field limit) and $\omega_c\tau$ $\gg 1$(high-field limit), where the magnetoresistance (MR) and Hall resistivity might exhibit distinct features as shown in the following.

We begin with the Hall resistivity of ZrTe₅ with doping level $n_0 = -3.0 \times 10^{18}\ \text{cm}^{-3}$ (hole-doped), $1.0 \times 10^{18}\ \text{cm}^{-3}$ (electron-doped), and $3.0 \times 10^{18}\ \text{cm}^{-3}$ (electron-doped), which are shown in Fig. 2. Results for additional doping levels are presented in Fig. S3. The shape of the Hall resistivity varies drastically with increasing temperature. However, there is an obvious difference between the Hall resistivity of the hole and electron-doped system. The Hall resistivity curves for hole-doped in Fig. 2a only exhibit nonlinear feature, while the ones for electron-doped in Fig. 2b, c show both sign reversal and nonlinear features. At low temperatures where there is only one single type of charge carrier, the magnitude of Hall resistivity monotonically increases with the magnetic field and the system shows the expected Hall sign, i.e., positive/negative for hole/electron-doped systems. With increasing temperature, the magnitude of Hall resistivity $\rho_{yx}$ drops for both electron and hole-doped systems, due to the thermal excitation and the increasing charge carriers contributing to the transport process. When reaching the intermediate temperature (around 155 K), the Hall resistivity of the electron-doped system undergoes a sign reversal with a strong nonlinear slope as shown in Fig. 2 (b, c). On the contrary, the Hall resistivity of the hole-doped system only exhibits nonlinear features without sign reversal as temperature rises.

According to our analysis of $\sigma_{xy}$, the nonlinear and sign reversal features of Hall resistivity probably stem from the complicated competition between electron and hole carriers (including both intrinsic and thermally excited ones). In order to verify this, we plot representative calculated $\boldsymbol{k}$-orbits and their corresponding $I$-paths at different chemical potentials $\mu_0 = -55$, $-50$ and 40 meV in Fig. 3. The corresponding Fermi surfaces are shown in Fig. S2. All the representative $\boldsymbol{k}$-orbits in the hole-doped system have concave segments (Fig. 3a, b), which give rise to the intersected $I$-path with a tiny secondary loop and the opposite circulation. It means a small part of charge carriers on these hole pockets behave like electrons. According to Eq. (7), the resistivity slope, which depends linearly on $\boldsymbol{B}$ in the low-field limit, is influenced by both the charge carrier density and the presence of these secondary loops. In contrast, at high magnetic fields, the slope of resistivity is governed primarily by the charge carrier density. This discrepancy between the slopes in the low- and high-field limits contributes to the subtle nonlinearity observed in the Hall resistivity for the hole-doped case at low temperatures, as depicted in Fig. 2a. Conversely, the electron pockets are all spherical surfaces and the corresponding $I$-paths are simple as shown in Fig. 3c, f, indicating linear Hall resistivity in electron-doped systems at low temperatures.

When temperature increases, the sign reversal at low magnetic field only happens in the electron-doped systems, which is difficult to explain by the qualitative orbits analysis. Therefore we employ the two-band model, where the Hall resistivity is written as,

$$
\rho_{yx}=-\frac{1}{e} \frac{\left(n_{h} \mu_{h}^{2}-n_{e} \mu_{e}^{2}\right) B+\left(n_{h}-n_{e}\right) \mu_{e}^{2} \mu_{h}^{2} B^{3}}{\left(n_{e} \mu_{e}+n_{h} \mu_{h}\right)^{2}+\left(n_{h}-n_{e}\right)^{2} \mu_{e}^{2} \mu_{h}^{2} B^{2}} \tag{1}
$$

where $n_{e/h}, \mu_{e/h}$ are the concentration and mobility of electron/hole carriers, respectively. With the fixed doping level $n_0 = n_e - n_h$, we use $n_e = n_e^0+\delta_n, n_h=\delta_n$ for electron-doped, and $n_h = n_h^0+\delta_n, n_e=\delta_n$ for hole-doped in Eq. (1) as following,

$$
\rho_{yx}^{hole}=-\frac{1}{e} \frac{\left\{\left[\delta_{n}\left(\mu_{h}^{2}-\mu_{e}^{2}\right)+n_{h}^{0} \mu_{h}^{2}\right]+n_{h}^{0} \mu_{e}^{2} \mu_{h}^{2} B^{2}\right\} B}{\left(n_{e} \mu_{e}+n_{h} \mu_{h}\right)^{2}+\left(n_{h}-n_{e}\right)^{2} \mu_{e}^{2} \mu_{h}^{2} B^{2}} \tag{2}
$$

$$
\rho_{yx}^{ele}=-\frac{1}{e} \frac{\left\{\left[\delta_{n}\left(\mu_{h}^{2}-\mu_{e}^{2}\right)-n_{e}^{0} \mu_{e}^{2}\right]-n_{e}^{0} \mu_{e}^{2} \mu_{h}^{2} B^{2}\right\} B}{\left(n_{e} \mu_{e}+n_{h} \mu_{h}\right)^{2}+\left(n_{h}-n_{e}\right)^{2} \mu_{e}^{2} \mu_{h}^{2} B^{2}} \tag{3}
$$

where $n_e^0$ and $n_h^0$ are the concentration of electron and hole carriers at zero-temperature. Because the mobility of hole carrier is larger than that of electron in ZrTe₅³⁷,⁶⁰, the Hall resistivity $\rho_{yx}^{hole}$ is always positive due to the positive terms, $n_h^0 \mu_h^2$ and $\delta_n(\mu_h^2-\mu_e^2)$, in Equation (2). However, the numerator of electron-doped $\rho_{yx}$ in Equation (3) are firstly negative due to the term $-n_e^0 \mu_e^2 B -n_e^0 \mu_e^2 \mu_h^2 B^3$ and then might change sign because of the growing amount of excited carriers $\delta_n$ with increasing temperature.

Furthermore, we can employ Eq. (3) to understand the sign change of electron-doped Hall resistivity with increasing magnetic field at intermediate temperatures (see green dashed curves in Fig. 2b, c). Supposing the

![](./images/1070186780583526403_2.jpg)

Fig. 2 | The field-dependent Hall resistivity at different temperatures and doping densities. The Hall resistivity for doping densities of (a) $n_0=-3.0 \times 10^{18}\ \text{cm}^{-3}$, (b) $1.0 \times 10^{18}\ \text{cm}^{-3}$, and (c) $3.0 \times 10^{18}\ \text{cm}^{-3}$, respectively. The dashed lines indicate the Hall resistivities that reverse sign with the increasing magnetic field. Temperature is varied from 35 K to 275 K at steps of 10 K. The relation between the temperature and color is indicated in the color bar.

![](./images/1070186780583526403_3.jpg)

Fig. 3 | The cross section of Fermi surfaces and corresponding $I$-paths. a–c The typical cross section of Fermi surfaces and (d–f) their corresponding $I$-paths with the magnetic field along $z$ direction. The chemical potentials are set to (a, d) $\mu=-55$ meV, (b, e) $\mu=-50$ meV, and (c, f) $\mu=40$ meV, respectively.

![](./images/1070186780583526403_4.jpg)

Fig. 4 | The field-dependent MR at different temperatures and the doping densities. The field-dependent MR for doping densities of (a) $n_0=-3.0\times10^{18}\text{cm}^{-3}$, (b) $1.0\times10^{18}\text{cm}^{-3}$, and (c) $3.0\times10^{18}\text{cm}^{-3}$, respectively. Temperature is varied from 35 K to 275 K at steps of 10 K. The relation between the temperature and color is indicated in the color bar.

Hall resistivity at weak magnetic field is positive, the numerator of Eq. (3) satisfies the condition that $\{[\delta_n(\mu_h^2-\mu_e^2)-n_e^0\mu_e^2]-n_e^0\mu_e^2\mu_h^2B^2\}>0$ when $\omega_c\tau\ll1$. With the increasing magnetic field, the second term of the numerator $-n_e^0\mu_e^2\mu_h^2B^2$ will increase and leads to the negative Hall resistivity at critical $\boldsymbol{B}$ field. Nevertheless, if the temperature rises at the same time, $\delta_n$ would increase and compensate the effect induced by a stronger magnetic field. It suggests the occurrence of sign reversal necessitates a higher magnetic field under elevated temperatures. This phenomenon is displayed in Fig. 2b, c, where we show the Hall resistivity with sign reversal by dashed lines. It is noteworthy that at the higher temperature (indicated by the curves in reds), the magnitude of $\boldsymbol{B}$ field required for sign reversal is far beyond our calculation and experimental measurement scope.

Although the understanding based on the two-band model is rudimentary, the physical mechanism in the above discussion, i.e., competition between electron and hole carriers driven by the magnetic field and thermal excitation, is the key origin of the nonlinear and sign reversal features of the Hall resistivity. Furthermore, by using Eq. (7) to analyze the Hall resistivity in electron/hole-doped systems under low fields ($\omega_c\tau\ll1$) and the well-established fact that charge carriers with the larger concentration dominate under high fields ($\omega_c\tau\gg1$), we arrive at the same conclusion. To avoid redundancy, we will not not give detailed repetitive explanations.

### Nonsaturating magnetoresistance
To proceed with investigating the MR of ZrTe₅, we plot our calculated MR results for the same doping levels as those used in the Hall resistivity studies in Fig. 4. Results for additional doping levels are shown in Fig. S3. It's apparent that at high temperatures, the MR of all doped levels exhibit non-saturating behavior. This phenomenon is due to the presence of both electron and hole carriers in those doped systems because of the thermal excitation. The nearly charge carrier compensation leads to the consistent rise in MR with the magnetic field, which agrees well with the experimental measurement⁴⁷,⁶⁰.

In the low-temperature range, the MR of electron and hole doped cases both show the trend toward saturation. However, the details of saturation are slightly different for electron and hole-doped systems. For the hole-doped case as shown in Fig. 4a, the MR saturates more slowly and at a larger magnetic field than that in electron-doped systems Fig. 4b, c (see curves in blues). We again refer to Fig. 3 to explain the distinction between these two systems. At low temperatures, where few excited charge carriers are present and intrinsic carriers dominate transport, the discrepancy arises from distinct Fermi surface geometries in different doping systems. Regarding the fact that the hole pockets with concave segments give rise to both electron and hole-like charge carriers, the slightly compensation between them postpones the saturation of MR. On the contrary, because the electron pockets possess only spherical surfaces, electron-doped systems exhibit rapid saturation of MR as expected. Furthermore, electron-doped MR has the largest enhancement at $T_p$, while the hole-doped one decreases with increasing temperature, consistent with experimental findings³⁷,⁶⁰. Nonetheless, our calculations does not capture the negative MR and quantum oscillations observed at low temperatures in experiments. Moreover,

https://doi.org/10.1038/s41524-024-01459-4

experimental MR saturation at low temperatures is more obvious in electron-doped ZrTe₅. Here we must point out that our calculated results is constricted in the semiclassical Boltzmann transport framework, i.e., without taking the Landau level, weak localization, and possible Berry curvature into account. For simplicity, we also ignore the $k$-dependence of the relaxation time $\tau$, which may also contribute to the deviation of our calculation from the experimental measurements.

## Discussion
To conclude, we developed an effective methodology to study the magnetoresistance and Hall resistivity of narrow-gap semiconductors based on the combination of first principles method and semiclassical Boltzmann transport theory. This approach is applied to study the temperature-dependent galvanomagnetic properties of ZrTe₅, taking into account variations in chemical potential and charge carrier concentrations. Our calculated results successfully reproduce observed transport behaviors in experiments, such as the resistivity anomaly, sign reversal and nonlinearity of Hall resistivity in electron-doped ZrTe₅, and non-saturating magnetoresistance at high temperatures. Our analysis demonstrates that these transport anomalies can be explained in terms of multi-carrier behavior and Fermi surface geometry.

Although our method effectively accounts for most of the experimental observations, certain detailed characteristics such as quantum oscillations and negative magnetoresistance were not captured due to the omission of Landau levels, Berry curvature, and the influence of interactions on the $k$-dependence of relaxation time. Nevertheless, our approach allows us to identify properties that can be explained by semiclassical contributions, and highlights nontrivial features in ZrTe₅ for future investigations. Moreover, our methodology can be extended to other narrow-gap semiconductors. Although theoretical models can explain some anomalous transport properties, first principles calculations remain a powerful tool for gaining deeper insights into galvanomagnetic behavior, thereby paving the way for further exploration.

## Methods
### Magnetoconductivity calculations
One can obtain the Boltzmann conductivity tensor in presence of the magnetic field by solving the Boltzmann transport equation within the relaxation time approximation as $^{65,66}$,

$$
\sigma^{(n)}(\boldsymbol{B})=\frac{e^{2}}{\alpha \pi^{3}} \int d \boldsymbol{k} \tau_{n} \boldsymbol{v}_{n}(\boldsymbol{k}) \overline{\boldsymbol{v}}_{n}(\boldsymbol{k})\left[-\frac{\partial f}{\partial \varepsilon_{n}(\boldsymbol{k})}\right], \tag{4}
$$

where $\alpha$ is a spin degeneracy related number, $\alpha=4(8)$ if spin-orbit coupling is excluded (included) in the Hamiltonian, $n$ is the band index, $f$ is the Fermi-Dirac distribution. $\varepsilon_{n}(\boldsymbol{k}), \tau_{n}$ and $\boldsymbol{v}_{n}(\boldsymbol{k})$ are the eigenvalue, relaxation time and group velocity of the $n$-th band, respectively. $\overline{\boldsymbol{v}}_{n}(\boldsymbol{k})$ describes the weighted average velocity during the past trajectory of the charge carriers,

$$
\overline{\boldsymbol{v}}_{n}(\boldsymbol{k})=\int_{-\infty}^{0} \frac{d t}{\tau_{n}} e^{\frac{t}{\tau_{n}}} \boldsymbol{v}_{n}[\boldsymbol{k}(t)]. \tag{5}
$$

The orbital motion of charge carriers in the reciprocal space follows the semiclassical equation of motion,

$$
\dot{\boldsymbol{k}}=-e \boldsymbol{v}_{n}(\boldsymbol{k}) \times \boldsymbol{B}, \tag{6}
$$

where the driven force of electric field was dropped off since the corresponding displacement is negligible compared to the scale of the Brillouin zone $^{65}$.

The trajectory of the charge carriers in $k$ space is confined on a cross-section of the Fermi surface by a plane perpendicular to $\boldsymbol{B}$, since the Lorentz force does not change the energy and only alters the velocity directions perpendicular to the magnetic field, as described by Equation (6). In order to have a more convenient and straightforward discussion of the motion of charge carriers, we define a "scattering path length" vector as $\boldsymbol{l} \equiv \boldsymbol{v}(\boldsymbol{k}) \tau$ which maps the orbitals in $\boldsymbol{k}$ space to the real space $^{64}$. Consequently, assuming the magnetic field is along $\hat{z}$ axis, we rewrite the Hall conductivity in weak fields in terms of the $\boldsymbol{l}$-paths as,

$$
\sigma_{y x}=\frac{e^{3}}{(2 \pi)^{3} \hbar^{2}} \int d \varepsilon\left(-\frac{\partial f}{\partial \varepsilon}\right)\left[\int d k_{z} \mathcal{A}\left(k_{z}\right)\right]_{\varepsilon} B, \tag{7}
$$

where $\mathcal{A}\left(k_{z}\right)=\frac{1}{2}\left(d \boldsymbol{l}_{\perp} \times \boldsymbol{l}_{\perp}\right) \cdot \frac{\boldsymbol{B}}{B}$ is the area swept by vector $\boldsymbol{l}$ as the charge carriers traced out the orbitals in $\boldsymbol{k}$ space with $\boldsymbol{l}_{\perp}=\boldsymbol{l}-l_{z} \hat{z}^{64}$.

## Calculation protocols applying to semiconductors
Different from the metals with large Fermi surfaces where the carrier density does not change significantly with temperature variation, the chemical potential and concentration of charge carriers in narrow-gap semiconductors, such as Zirconium Pentatelluride ZrTe₅, are sensitive to the change of temperature, necessitating the precise dynamic calculations. Therefore we list our self-contained calculation procedure in the following.
(i) Obtain $\rho(\boldsymbol{B} \tau, \mu, T) \tau$: First of all, we calculate the band-resolved magneto-conductivity over the relaxation time, denoted as $\sigma_{n}(\boldsymbol{B} \tau) / \tau_{n}$, on a suitable $(\mu, T)$ grid by employing Eq. (4). Then we obtain the product of resistivity and relaxation time, $\rho \tau=\left[\sum_{n} \sigma_{n}(\boldsymbol{B} \tau) / \tau_{n}\right]^{-1}$. Here we assume that relaxation time for all carriers have the same temperature dependence but with different ratios. For example, in ZrTe₅, we take $\tau_{h}(T)=5 \tau_{e}(T)$ as implied by experiment measurement $^{60}$.
(ii) Get $\mu(T)$: We assume that the net carrier concentration, defined as $n_{0}=n_{e}-n_{h}$, remains constant with varying temperature. This assumption is mostly valid for semiconductors below their melting point. Consequently, the temperature dependent chemical potential $\mu(T)$, is determined by the condition:

$$
\begin{aligned}
n_{0} & =n_{e}-n_{h} \\
& =\int_{E_{\mathrm{CBM}}}^{+\infty} g_{c}(\varepsilon) f(\varepsilon-\mu) d \varepsilon \\
& -\int_{-\infty}^{E_{\mathrm{VBM}}} g_{h}(\varepsilon)[1-f(\varepsilon-\mu)] d \varepsilon,
\end{aligned} \tag{8}
$$

where $n_{e}$ and $n_{h}$ are the concentration of electron and hole charge carriers respectively. $E_{\mathrm{CBM}}$ and $E_{\mathrm{VBM}}$ are the conduction band minimum and valence band maximum, respectively. $g_{c}(\varepsilon)$ and $g_{h}(\varepsilon)$ are DOS of conduction and valence bands, respectively.
(iii) Interpolation to get $\rho(\boldsymbol{B} \tau, \mu(T), T) \tau$: For a fixed $n_{0}$, corresponding to a specified doped sample or a thin film at a particular gate voltage, we can obtain the product of temperature-dependent resistivity and relaxation time, $\rho(\boldsymbol{B} \tau, \mu(T), T) \tau$, by interpolating the calculated $\rho(\boldsymbol{B} \tau) \tau$ on a dense grid of $(\mu, T)$ in the step (i), see Figure. S1.
(iv) Fitting $\tau(T)$ with experiments: Finally, for any given doping concentration $n_{0}$, we obtain the magneto-resistivity $\rho(\boldsymbol{B})$ at arbitrary temperature by substituting the fitted $\tau(T)$ in $\rho(\boldsymbol{B} \tau, \mu(T), T) \tau$. Fitting $\tau(T)$ in semiconductors with experimental data is not as straightforward as in metals/semimetals. In metals/semimetals, the charge carrier concentration does not change significantly, allowing a consistent treatment of $\tau(T)$ across the whole temperature range. However, in semiconductor like ZrTe₅, which exhibits different properties with varying temperature, we need to separate the high temperature regime from the low one. The metallic behavior of ZrTe₅ at low temperature allows us to fit $\tau(T)$ with corresponding experiment results in this regime. On the contrary, the semiconductor behavior in the high temperature regime precludes the direct derivation of $\tau(T)$ from experimental measurements. Nonetheless, it is well-known that the electron-phonon scattering described by $\tau(T) \propto 1 / T$ dominates at the high temperature regime. We assume $\tau(T) \propto 1 / \rho_{\mathrm{sc}}(T)$, and $\rho_{\mathrm{sc}}(T)$ represents the scattering-related resistivity which is comprised in the relaxation time. The distinct scattering behavior of ZrTe₅ across

npj Computational Materials | (2024)10:276

https://doi.org/10.1038/s41524-024-01459-4

Article

different temperature regime could be depicted jointly by the Bloch-
Grüneisen model⁶⁰,⁶⁷ as,

$$
\rho_{s c}(T)=\rho_{0}+\alpha\left(\frac{T}{\Theta_{R}}\right)^{n} \int_{0}^{\frac{\Theta_{R}}{T}} \frac{x^{n}}{\left(e^{x}-1\right)\left(1-e^{-x}\right)} d x, \tag{9}
$$

with the parameters $\rho_0=1.06, \alpha=11, n=2$, and $\Theta_R=600$ obtained by fitting the experiment data⁶⁰ at low temperature. $\tau(T)$ in this work are calculated by Eq. (9) and the hypothesis $\tau(T) \propto 1/\rho_{sc}(T)$.

Our methodology for calculating magneto-resistivity is broadly applicable to narrow-gap semiconductors, not just to the compound $ZrTe_5$. Furthermore, the hypothesis $\tau(T) \propto 1/\rho_{sc}(T)$ can be extended to metals and doped semiconductors that display metallic behavior. The validity of this relationship is supported by the relaxation time approximation and the weak field assumption about the electric field, making it applicable primarily in conditions where the system shows metallic characteristics and the charge carrier concentration remains relatively stable. It should be noted that this proportional relationship allows for the analysis of the temperature dependence of $\tau$ but not its precise value. For the determination of $\tau$, one can fit the experimental $\rho(B)$ with the theoretically calculated $\rho\tau(B\tau)$ when the carrier density is relatively constant.

### Ab initio calculations
The band structure was calculated using the Vienna ab initio simulation package (VASP)⁶⁸ with the generalized gradient approximation of Perdew, Burke, and Ernzerhof for the exchange-correlation potential⁶⁹. We performed the self-consistent calculation on a k-mesh of $11 \times 11 \times 11$ with energy cutoff of 550 eV. The temperature-dependent chemical potential was calculated using BoltzTrap⁷⁰ package and performed on the k-mesh of $50 \times 50 \times 25$. Magneto-conductivity and Fermi surface were calculated using the WANNIERTOOLS package⁷¹ based on a tight-binding model constructed by the WANNIER90 package⁷²⁻⁷⁵. In the Magneto-conductivity calculation, we use a k-mesh of $201 \times 201 \times 201$ and set the broadening width of Fermi-Dirac distribution function to 200 meV.

### Data availability
The data that support the findings of this study are available from the corresponding author upon reasonable request.

Received: 27 April 2024; Accepted: 27 October 2024;
Published online: 30 November 2024

### References
1. Tang, F. et al. Three-dimensional quantum hall effect and metal-insulator transition in $ZrTe_5$. *Nature* **569**, 537–541 (2019).
2. Zhu, Z. et al. Quantum oscillations, thermoelectric coefficients, and the fermi surface of semimetallic $WTe_2$. *Phys. Rev. Lett.* **114**, 176601 (2015).
3. Terashima, T. et al. Fermi surface with dirac fermions in cefeast determined via quantum oscillation measurements. *Phys. Rev. X* **8**, 011014 (2018).
4. Alexandradinata, A., Wang, C., Duan, W. & Glazman, L. Revealing the topology of fermi-surface wave functions from magnetic quantum oscillations. *Phys. Rev. X* **8**, 011027 (2018).
5. Chen, Q. et al. Extremely large magnetoresistance in the “ordinary” metal $ReO_3$. *Phys. Rev. B* **104**, 115104 (2021).
6. Luo, Y. et al. Hall effect in the extremely large magnetoresistance semimetal $WTe_2$. *Appl. Phys. Lett.* **107**, 182411 (2015).
7. Hou, Z. et al. High electron mobility and large magnetoresistance in the half-heusler semimetal LuPtBi. *Phys. Rev. B* **92**, 235134 (2015).
8. Son, D. & Spivak, B. Chiral anomaly and classical negative magnetoresistance of weyl metals. *Phys. Rev. B* **88**, 104412 (2013).
9. Xiong, J. et al. Evidence for the chiral anomaly in the dirac semimetal $Na_3Bi$. *Science* **350**, 413–416 (2015).
10. Hirschberger, M. et al. The chiral anomaly and thermopower of weyl fermions in the half-heusler GdPtBi. *Nat. Mater.* **15**, 1161–1165 (2016).
11. Huang, X. et al. Observation of the chiral-anomaly-induced negative magnetoresistance in 3d weyl semimetal TaAs. *Phys. Rev. X* **5**, 031023 (2015).
12. Orlita, M. et al. Carrier scattering from dynamical magnetoconductivity in quasineutral epitaxial graphene. *Phys. Rev. Lett.* **107**, 216603 (2011).
13. Leuliet, A. et al. Electron scattering spectroscopy by a high magnetic field in quantum cascade lasers. *Phys. Rev. B* **73**, 085311 (2006).
14. Heremans, J., Partin, D., Thrush, C. & Green, L. Narrow-gap semiconductor magnetic-field sensors and applications. *Semiconductor Sci. Technol.* **8**, S424 (1993).
15. Reig, C., Cubells-Beltrán, M.-D. & Muñoz, D. R. Magnetic field sensors based on giant magnetoresistance (gmr) technology: Applications in electrical current sensing. *Sensors* **9**, 7919–7942 (2009).
16. Granell, P. N. et al. Highly compliant planar hall effect sensor with sub 200 nt sensitivity. *npj Flex. Electron.* **3**, 3 (2019).
17. Henriksen, A. et al. Planar hall effect bridge magnetic field sensors. *Appl. Phys. Lett.* **97**, 013507 (2010).
18. Daughton, J. Gmr applications. *J. Magn. Magn. Mater.* **192**, 334–342 (1999).
19. He, L. et al. Quantum transport evidence for the three-dimensional dirac semimetal phase in $Cd_3As_2$. *Phys. Rev. Lett.* **113**, 246402 (2014).
20. Liang, T. et al. Ultrahigh mobility and giant magnetoresistance in the dirac semimetal $Cd_3As_2$. *Nat. Mater.* **14**, 280–284 (2015).
21. Ali, M. N. et al. Large, non-saturating magnetoresistance in $WTe_2$. *Nature* **514**, 205–208 (2014).
22. Thirupathaiah, S. et al. Mote 2: An uncompensated semimetal with extremely large magnetoresistance. *Phys. Rev. B* **95**, 241105 (2017).
23. Takatsu, H. et al. Extremely large magnetoresistance in the nonmagnetic metal $PdCoO_2$. *Phys. Rev. Lett.* **111**, 056601 (2013).
24. Zhang, S., Wu, Q., Liu, Y. & Yazyev, O. V. Magnetoresistance from fermi surface topology. *Phys. Rev. B* **99**, 035142 (2019).
25. Nazmul, A., Lin, H., Tran, S., Ohya, S. & Tanaka, M. Planar hall effect and uniaxial in-plane magnetic anisotropy in mn δ-doped GaAs/ p-AlGaAs heterostructures. *Phys. Rev. B* **77**, 155203 (2008).
26. Tang, H., Kawakami, R., Awschalom, D. & Roukes, M. Giant planar hall effect in epitaxial (Ga, Mn) as devices. *Phys. Rev. Lett.* **90**, 107201 (2003).
27. Yin, G. et al. Planar hall effect in antiferromagnetic mnte thin films. *Phys. Rev. Lett.* **122**, 106602 (2019).
28. Yang, S.-Y., Chang, K. & Parkin, S. S. Large planar hall effect in bismuth thin films. *Phys. Rev. Res.* **2**, 022029 (2020).
29. Liu, Q. et al. Nontopological origin of the planar hall effect in the type-ii dirac semimetal $NiTe_2$. *Phys. Rev. B* **99**, 155119 (2019).
30. Yang, J. et al. Current jetting distorted planar hall effect in a weyl semimetal with ultrahigh mobility. *Phys. Rev. Mater.* **3**, 014201 (2019).
31. Meng, J. et al. Planar hall effect induced by anisotropic orbital magnetoresistance in type-ii dirac semimetal $PdTe_2$. *J. Phys.: Condens. Matter* **32**, 015702 (2019).
32. Liang, D. et al. Origin of planar hall effect in type-ii weyl semimetal $MoTe_2$. *Aip Adv.* **9** (2019).
33. Nandy, S., Sharma, G., Taraphder, A. & Tewari, S. Chiral anomaly as the origin of the planar hall effect in weyl semimetals. *Phys. Rev. Lett.* **119**, 176804 (2017).
34. Burkov, A. Giant planar hall effect in topological metals. *Phys. Rev. B* **96**, 041110 (2017).
35. Kumar, N., Guin, S. N., Felser, C. & Shekhar, C. Planar hall effect in the weyl semimetal GdPtBi. *Phys. Rev. B* **98**, 041103 (2018).
36. Li, H., Wang, H.-W., He, H., Wang, J. & Shen, S.-Q. Giant anisotropic magnetoresistance and planar hall effect in the dirac semimetal $Cd_3As_2$. *Phys. Rev. B* **97**, 201110 (2018).

npj Computational Materials|(2024)10:276

https://doi.org/10.1038/s41524-024-01459-4

37. Shahi, P. et al. Bipolar conduction as the possible origin of the electronic transition in pentatellurides: metallic vs semiconducting behavior. *Phys. Rev. X* **8**, 021055 (2018).

38. Gourgout, A. et al. Magnetic freeze-out and anomalous hall effect in ZrTe₅. *npj Quantum Mater.* **7**, 71 (2022).

39. Wieting, T. J., Gubser, D. U., Wolf, S. A. & Levy, F. Giant anomalies in the resistivities of quasi-one-dimensional ZrTe₅ and HfTe₅. *Bull. Am. Phys. Soc.* **25**, 340–340 (1980).

40. Okada, S., Sambongi, T. & Ido, M. Giant resistivity anomaly in ZrTe₅. *J. Phys. Soc. Jpn.* **49**, 839–840 (1980).

41. Jones, T., Fuller, W., Wieting, T. & Levy, F. Thermoelectric power of ZrTe₅ and HfTe₅. *Solid State Commun.* **42**, 793–798 (1982).

42. Mcllroy, D. et al. Observation of a semimetal–semiconductor phase transition in the intermetallic zrte₅. *J. Phys.: Condens. Matter* **16**, L359 (2004).

43. Manzoni, G. et al. Ultrafast optical control of the electronic properties of ZrTe₅. *Phys. Rev. Lett.* **115**, 207402 (2015).

44. Xu, B. et al. Temperature-driven topological phase transition and intermediate dirac semimetal phase in ZrTe₅. *Phys. Rev. Lett.* **121**, 187401 (2018).

45. Fu, B., Wang, H.-W. & Shen, S.-Q. Dirac polarons and resistivity anomaly in ZrTe₅ and hfte 5. *Phys. Rev. Lett.* **125**, 256601 (2020).

46. Wang, C. Thermodynamically induced transport anomaly in dilute metals ZrTe₅ and HfTe₅. *Phys. Rev. Lett.* **126**, 126601 (2021).

47. Lozano, P. M. et al. Anomalous hall effect at the lifshitz transition in ZrTe₅. *Phys. Rev. B* **106**, L081124 (2022).

48. Liang, T. et al. Anomalous hall effect in ZrTe₅. *Nat. Phys.* **14**, 451–455 (2018).

49. Liu, Y. et al. Induced anomalous hall effect of massive dirac fermions in ZrTe₅ and HfTe₅ thin flakes. *Phys. Rev. B* **103**, L201110 (2021).

50. Choi, Y., Villanova, J. W. & Park, K. Zeeman-splitting-induced topological nodal structure and anomalous hall conductivity in ZrTe₅. *Phys. Rev. B* **101**, 035105 (2020).

51. Wang, H.-W., Fu, B. & Shen, S.-Q. Theory of anomalous hall effect in the transition-metal pentatellurides ZrTe₅ and HfTe₅. *Phys. Rev. B* **108**, 045141 (2023).

52. Manzoni, G. et al. Evidence for a strong topological insulator phase in ZrTe₅. *Phys. Rev. Lett.* **117**, 237601 (2016).

53. Wu, R. et al. Evidence for topological edge states in a large energy gap near the step edges on the surface of ZrTe₅. *Phys. Rev. X* **6**, 021017 (2016).

54. Zhang, Y. et al. Electronic evidence of temperature-induced lifshitz transition and topological nature in ZrTe₅. *Nat. Commun.* **8**, 15512 (2017).

55. Weng, H., Dai, X. & Fang, Z. Transition-metal pentatelluride ZrTe₅ and HfTe5: A paradigm for large-gap quantum spin hall insulators. *Phys. Rev. X* **4**, 011002 (2014).

56. Li, Q. et al. Chiral magnetic effect in ZrTe₅. *Nat. Phys.* **12**, 550–554 (2016).

57. Liu, Y. et al. Zeeman splitting and dynamical mass generation in dirac semimetal ZrTe₅. *Nat. Commun.* **7**, 12516 (2016).

58. Chen, R. et al. Magnetoinfrared spectroscopy of landau levels and zeeman splitting of three-dimensional massless dirac fermions in ZrTe₅. *Phys. Rev. Lett.* **115**, 176404 (2015).

59. Sun, Z. et al. Large zeeman splitting induced anomalous hall effect in ZrTe₅. *npj Quantum Mater.* **5**, 36 (2020).

60. Liu, Y. et al. Gate-tunable multiband transport in ZrTe₅ thin devices. *Nano Lett.* **23**, 5334–5341 (2023).

61. Tritt, T. M. et al. Large enhancement of the resistive anomaly in the pentatelluride materials HfTe₅ and ZrTe₅ with applied magnetic field. *Phys. Rev. B* **60**, 7816 (1999).

62. Zhou, L. et al. Anisotropic landau level splitting and lifshitz transition induced magnetoresistance enhancement in ZrTe₅ crystals. *N. J. Phys.* **21**, 093009 (2019).

63. Colinge, J. P. C. C. A. *Physics of Semiconductor Devices* (Kluwer, 2002).

64. Ong, N. P. Geometric interpretation of the weak-field hall conductivity in two-dimensional metals with arbitrary fermi surface. *Phys. Rev. B* **43**, 193 (1991).

65. Ashcroft, N. W. & Mermin, N. D. *Solid state physics* (Cengage Learning, 2022).

66. Liu, Y., Zhang, H.-J. & Yao, Y. Ab initio investigation of magnetic transport properties by wannier interpolation. *Phys. Rev. B* **79**, 245123 (2009).

67. Ziman, M. *Electrons and Phonons* (Clarendon Press, Oxford, 1962).

68. Kresse, G. & Furthmüller, J. Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. *Phys. Rev. B* **54**, 11169 (1996).

69. Perdew, J. P., Burke, K. & Ernzerhof, M. Generalized gradient approximation made simple. *Phys. Rev. Lett.* **77**, 3865 (1996).

70. Madsen, G. K. & Singh, D. J. Boltztrap. a code for calculating band-structure dependent quantities. *Computer Phys. Commun.* **175**, 67–71 (2006).

71. Wu, Q., Zhang, S., Song, H.-F., Troyer, M. & Soluyanov, A. A. Wanniertools: An open-source software package for novel topological materials. *Computer Phys. Commun.* **224**, 405–416 (2018).

72. Marzari, N. & Vanderbilt, D. Maximally localized generalized wannier functions for composite energy bands. *Phys. Rev. B* **56**, 12847 (1997).

73. Souza, I., Marzari, N. & Vanderbilt, D. Maximally localized wannier functions for entangled energy bands. *Phys. Rev. B* **65**, 035109 (2001).

74. Marzari, N., Mostofi, A. A., Yates, J. R., Souza, I. & Vanderbilt, D. Maximally localized wannier functions: Theory and applications. *Rev. Mod. Phys.* **84**, 1419 (2012).

75. Mostofi, A. A. et al. An updated version of wannier90: A tool for obtaining maximally-localised wannier functions. *Computer Phys. Commun.* **185**, 2309–2310 (2014).

### Acknowledgements
This work was supported by the National Key R&D Program of China (Grant No.2023YFA1607400, 2022YFA1403800), the National Natural Science Foundation of China (Grant No.12274436, 11925408, 11921004, 12174439), the Science Center of the National Natural Science Foundation of China (Grant No. 12188101) and H.W. acknowledge support from the Informatization Plan of the Chinese Academy of Sciences (CASWX2021SF-0102) and the New Cornerstone Science Foundation through the XPLORER PRIZE.

### Author contributions
Q.W., H.W., proposed the project and supervised H.P. in carrying out the research and calculation. H.P. and S.Z. wrote the first draft of the manuscript. Q.W., H.W., H.P., S.Z., Y.X. and Z.F. contributed to the discussions and revision of the manuscript to its final version.

### Competing interests
The authors declare no competing interests.

### Additional information
Supplementary information The online version contains supplementary material available at
https://doi.org/10.1038/s41524-024-01459-4.

Correspondence and requests for materials should be addressed to Shengnan Zhang, Hongming Weng or Quansheng Wu.

Reprints and permissions information is available at
http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

npj Computational Materials| (2024)10:276

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2024