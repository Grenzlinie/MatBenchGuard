# Intrinsic spin noise in MgO magnetic tunnel junctions.
F. Delgado, $^{1}$ K. Lopez, $^{2,3}$ R. Ferreira, $^{1}$ and J. Fernández-Rossier $^{1,4}$
$^{1)}$ International Iberian Nanotechnology Laboratory (INL), Av. Mestre José Veiga, 4715-330 Braga, Portugal
$^{2)}$ Department of Mechanical Engineering, Massachusetts Institute of Technology, Cambridge, MA 02139 USA
$^{3)}$ Mechanical Engineering Department, Stanford University, Stanford, CA 94305 USA
$^{4)}$ Departamento de Física Aplicada, Universidad de Alicante, 03690 San Vicente del Raspeig, Spain

We consider two intrinsic sources of noise in ultra-sensitive magnetic field sensors based on MgO magnetic tunnel junctions, coming both from $^{25}$Mg nuclear spins ($I=5/2$, 10% natural abundance), and $S=1$ Mg-vacancies. While nuclear spins induce noise peaked in the MHz frequency range, the vacancies noise peaks in the GHz range. We find that the nuclear noise in submicron devices has a similar magnitude than the $1/f$ noise, while the vacancy-induced noise dominates in the GHz range. Interestingly, the noise spectrum under a finite magnetic field gradient may provide spatial information about the spins in the MgO layer.

Magnetic tunnel junctions (MTJ) with ferromagnetic electrodes and a MgO tunnel barrier have a very large room temperature tunneling magnetoresistance (TMR).$^{1,2}$ As a result, they are widely used for magnetic sensing applications where room-temperature ultra-high sensitivity, circuit integration and low fabrication cost are essential. Engineering of multilayer MTJ devices has allowed building devices whose resistance scales linearly with the applied magnetic field. If this linear relation holds at arbitrarily small field, the devices can operate as sensors for magnetic fields as small as permitted by the different sources of noise. Broadly speaking, these can be classified in two groups, electric and magnetic.$^{3-8}$ The former includes shot-noise, Johnson-Nyquist noise, electric $1/f$ noise or noise due to charge trapping in the oxide barrier. The second includes fluctuations in the magnetic orientation of the electrodes due to collective precessional modes, $1/f$ magnetic noise, domain wall motion and so on.

MgO based TMR sensors with an area of $1\mu$m$^2$ feature sensitivities of up to $pT/\sqrt{\text{Hz}}$ limited by white noise background.$^{6,7}$ This striking sensitivity leads us to address the following intriguing question: to which degree the magnetic field created by spins in the subnanometer thick MgO barrier can be a source of noise that limits the performance of these devices? Or reversing the terms of the question: could the electrical noise of a MgO-MTJ probe the spin noise of the barrier?

The MgO barrier certainly hosts the only stable Mg spinful nuclear isotopes, $^{25}$Mg ,with nuclear spin, $I=5/2$. Thus, taking into account that the lattice constant of the MgO is $4.212$ Å, and its natural relative abundance of 10%,$^{9}$ the volumetric density of nuclear spins is $\rho_m=1.32$ spins/nm$^3$. The maximal magnetic field created by one of such nuclear spins, at a distance $l$, reaches $4.3$nm$^3$/$l^3$ $\mu$T. In addition, the MgO barrier hosts a density of Mg vacancies$^{10-13}$ which have electronic spin $S=1$, each of which will create a magnetic field 3 orders of magnitude larger.

In standard MTJ sensing devices, one magnetic layer is designed to have its magnetization pinned by exchange coupling to an antiferromagnet while the other is free to rotate, see Fig. 1(a).$^{4,6}$ Then, the relevant figure of merit is given by the sum of all nuclear fields, averaged over the entire free layer (FL) sensing electrode

$$
\vec{\mathcal{B}}\left(\vec{m}_{i}\right) \equiv \frac{1}{V} \int_{V} \vec{B}\left[\vec{m}_{i}\right](\vec{r}) d V, \tag{1}
$$

where the integral is over the volume $V$ of the detector and $\vec{B}[\vec{m}_{i}](\vec{r})$ corresponds to the magnetic field created at position $\vec{r}$ by the set of magnetic dipoles $\{\vec{m}_{i}\}$. If all the nuclear spins were fully polarized, they would create an average field that, for a cylindrical device with $R=100nm$, would lead to $\mathcal{B}_{max}\sim0.1$ $\mu$T, which motivates a detailed study of the nuclear spin noise in this system.

![](./images/867746826638328252_1.jpg)

FIG. 1. (color online) (a) Scheme of a MTJ sensing device. (b) Variation of the standard deviation of the average field in the free layer with the detector radius $R$ for a device with $d=0.5$ nm.

At room temperature the average nuclear spin orientation is vanishingly small, and so it is the average magnetic field they create, but statistical fluctuations of the nuclear spin orientation create magnetic noise. For the calculation of its statistical properties, the following relation between the average sensing layer field, Eq. (1), and the nuclear magnetic moments $\vec{m}_{i}$ is extremely useful:

$$
\mathcal{B}_{a}=\sum_{i, b} \Xi_{a b}(i) m_{b}(i), \tag{2}
$$

where
$$
\Xi_{a b}(i)=\frac{\mu_{0}}{4 \pi} \frac{1}{V} \int_{V} d V \frac{n_{b}(i) n_{a}(i)-\delta_{a b}}{\left|\vec{r}-\vec{r}_{i}\right|^{3}}. \tag{3}
$$

$\Xi_{ab}(i)$ is a geometrical factor that relates the $a$ component of the average detector field to the $b$ component of the nuclear magnetic moment $i$, with $a,b=x,y,z$ . The linear relation in Eq. (3) permits relating the quantum statistical properties of the nuclear spins to those of the sensing layer average in a straightforward way, in particular if one assumes that different nuclear spins are uncorrelated. In this way, the standard deviation of the $a$-magnetic field component created by the fully randomized nuclear spins, defined as $\sigma_{\mathcal{B}_{a}}^{2} \equiv\langle(\mathcal{B}_{a}-\langle\mathcal{B}_{a}\rangle)^{2}$, where the brackets stand for the quantum statistical average, can be written as
$$
\sigma_{\mathcal{B}_{a}}^{2}=\left(g^{*} \mu_{N}\right)^{2} I(I+1) \sum_{i, b} \Xi_{a b}(i)^{2}, \tag{4}
$$
where we have used $\langle m^{2}\rangle=g^{* 2} \mu_{N}^{2} I(I+1)$, with $\mu_{N}$ the nuclear magneton and $g^{*}$ the effective g-factor $(g^{*} \approx$ 0.342 for the $^{25} Mg).^{14}$

The quantity $\sigma_{\mathcal{B}_{a}}$ represents the $a$-component of the nuclear magnetic field noise integrated over the entire frequency range. In addition, if the nuclear spins are randomized, we will find that in cylindrical devices like the one in Fig. 1(a), $\sigma_{\mathcal{B}_{x}}=\sigma_{\mathcal{B}_{y}}$. Since we can safely neglect changes in the magnitude of the magnetization, the nuclear noise field can only be efficient in rotating the FL magnetization, which by design of these sensors, can only happen in the plane of the layer. Therefore, only the noise along the in-plane direction $x$ perpendicular to the equilibrium magnetization, will compromise the sensor accuracy. Figure 1(b) shows the numerically calculated $\sigma_{\mathcal{B}_{x}}$ for two devices with FL thickness $w=2$ and $3 nm$, and barrier thickness $d=0.5 nm$ a function of $R$. Positions $\vec{r}_{i}$ in the MgO layer have been randomly chosen and we have checked that results do not significantly depend on the random distribution. From Fig.1, we can extrapolate and get that for $R=1\ \mu m$ and $w=3 nm$, $\sigma_{\mathcal{B}_{x}} \approx 10 nT$.

From our numerics, we find that $\sigma_{\mathcal{B}_{x}}$ grows linearly with $1/R$ except for very small devices $R \lesssim 10 nm$. Thus, the relevance of the nuclear spin noise increases for smaller sensors. Notice that from Eq. (4) it is ostensible that $\sigma_{\mathcal{B}_{a}}^{2}$ scales proportionally to $N$, the number of nuclear spins in the barrier. This is a consequence of the linear relation in Eq. (2) on one hand, and the linear scaling between the statistical fluctuations of the total magnetic moment and the number of spins. $^{15,16}$ Nevertheless, in our case the $1/R$ scaling of the standard deviation of the magnetic field comes from the scaling of integral (3).

In addition to the unavoidable nuclear spin noise, MgO can have a certain density of oxygen and magnesium vacancies. $^{10-12,17}$ The most likely spinfull vacancy in MgO are the Mg vacancies, $V_{Mg}$, with concentrations that vary between $10^{19} cm^{-3}$ and $10^{21} cm^{-3} \cdot^{10-13}$ According to density functional calculations, $^{13}$ the magnetic moment of these vacancies is $m_{V_{M g}} \approx 1.9 \mu_{B}$. Whereas the number of vacancies might be smaller than the density of spinfull Mg nuclei, their magnetic moment is also2000 times larger. Thus, they could also be the source of more spin noise. The analysis of the numerical data shows that, in both cases, $\sigma_{\mathcal{B}_{a}} \propto \sqrt{\langle m^{2}\rangle} \sqrt{\rho} /(w R)$ for $R \gg d, w$, so the standard deviation of the field scales with the square root of the barrier spin density, $\rho$.

We now consider the spectral properties of the nuclear and vacancy magnetic field noise. For that matter, we assume that every nuclear and vacancy spin precess freely under the influence of the magnetic field created by the ferromagnetic electrodes, $\vec{B}_{ext }$. Thus, we neglect the mutual coupling between spin centers in the barrier, except for a phenomenological relaxation time $T_{1}$ explained below. Notice that the precession frequency of nuclear and electronic spins is very different, on account of their different magnetic moment. Then, for a MgO average field of 0.1 T, the nuclear and electronic precession frequencies are in the range of MHz and GHz respectively.

We assume that the magnetic field felt by the barrier spins is time independent and it only varies in the direction perpendicular to the interfaces $(z)$. This approximation works well as long as the time fluctuations of the magnetic field created by the barrier are slow compared to the barrier spin dynamics. Under these approximations, the correlation function for the detector average at different times, $S_{a}^{2}(t) \equiv\langleB_{a}(t)B_{a}(0)\rangle$, with $t>0$, is related to the spin correlation functions as
$$
S_{a}^{2}(t)=\sum_{i i^{\prime}, b b^{\prime}} \Xi_{a b}(i) \Xi_{a b^{\prime}}\left(i^{\prime}\right)\left\langle m_{b}(i ; t) m_{b^{\prime}}\left(i^{\prime} ; 0\right)\right\rangle. \tag{5}
$$

The evaluation of this quantity is greatly simplified using the fact that, to a very good approximation, different barrier spins are uncorrelated. Accordingly, the experimentally relevant noise spectrum, $S_{x}^{2}(\omega)=\int_{-\infty}^{\infty} e^{-i \omega t} S_{x}^{2}(t) d t$, can be expressed as:
$$
S_{x}^{2}(\omega)=\sum_{i, b b^{\prime}} \Xi_{x b}(i) \Xi_{x b^{\prime}}(i)\left\langle m_{b}(i) m_{b^{\prime}}(i)\right\rangle[\omega]. \tag{6}
$$

If we quantize the system along the magnetic field orientation at each nuclear spin, and denoting as $|n\rangle$ the nuclear spin eigenstates, the barrier spin spectral function reads, in the limit $k_{B} T \gg|\vec{m}| B_{ext }$,
$$
\begin{aligned}
\left\langle m_{b}(i) m_{b^{\prime}}(i)\right\rangle[\omega] &=\frac{\delta_{i, i^{\prime}}}{(2 I+1)} \sum_{n n^{\prime}}\left\langle n\left|m_{b}\right| n^{\prime}\right\rangle \\
& \times\left\langle n^{\prime}\left|m_{b^{\prime}}\right| n\right\rangle \delta\left(\omega-\omega_{n n^{\prime}}(i)\right), \tag{7}
\end{aligned}
$$
where $\hbar \omega_{n n^{\prime}}(i)=|\vec{m}| B_{ext }(i)(n-n^{\prime})$ is the energy of the spin transition $n \to n^{\prime}$, which depends on local the value of the external field. Some straightforward algebra permits obtaining the following relation between the spectral noise response $S_{x}(\omega)$ and $\sigma_{\mathcal{B}_{x}}$
$$
\int_{-\infty}^{\infty} S_{x}^{2}(\omega) d \omega=\frac{\sigma_{\mathcal{B}_{x}}^{2}}{3}. \tag{8}
$$

![](./images/867746826638328252_2.jpg)

FIG. 2. (a) Spectral response $S_x(\omega)$ versus frequency $f = \omega/2\pi$ for a detector of radius $R = 100$ nm (black line) and $R = 50$ nm (blue line), $d = 1$ nm, $w = 3$ nm, $B_{ext} = 0.1$ T and $T_1 = 10$ ms. b) Scheme of the variation of the field along a 1 nm thick MgO layer.

As a first approach, let us assume that all the barrier spins feel the same magnetic field intensity. Then, the $^{25}$Mg nuclear spins spectral function has a single finite-frequency peak at the Larmor frequency $\omega_B = |\vec{m}| B_{ext}/\hbar$.

Due to its coupling to the environment, the spectral function of a single nuclear spin, Eq. (7), acquires a finite linewidth. We model this by substituting the delta function in Eq. (7) by a Lorentzian function with a width $\delta\omega = 2\pi/T_1$, with $T_1$ the characteristic relaxation time. Typically, $T_1 \lesssim 50$ s in bulk MgO at room temperature, $^{18}$ and it is expected to be at least 1ms or larger in surfaces. $^{19}$ The resulting nuclear noise spectrum is shown in Fig. 2 for two values of $R$. The magnitude of the peak noise associated to the nuclear spins is in the range of $\text{nT}/\text{Hz}^{1/2}$, centered in the Larmor frequency ( $0.5 \text{MHz}$ for $B_{ext} \sim 0.1$ T).

This reported nuclear noise has to be compared with the noise coming from other sources, such as the $1/f$ noise. We take as a reference a $R = 20\mu\text{m}$ sensor that has a noise level of $\text{pT}/\sqrt{\text{Hz}}$ at $500 \text{KHz}.^{20,21}$ We use the fact that the $1/f$ noise also scales like $1/R$ with size, so that, extrapolating down to $R = 100nm$, the $1/f$ noise would be $0.4 \text{ nT}/\sqrt{\text{Hz}}$, comparable to the one in Fig. 2(a). Therefore the contributions of nuclear spin noise and $1/f$ noise are, under these assumptions, of the same order.

We now consider the noise due to spinful Mg vacancies. If we assume a lower limit for the $V_{Mg}$ concentration of $10^{19}\text{cm}^{-3}$, a small MgO layer of $R = 25$ nm and $d = 0.5nm$ will contain more than 10 vacancies. $10^4$ $V_{Mg}$. Since the magnetic moment of these vacancies is around $1.9\mu_B$, at least three orders of magnitude larger than in the $^{25}$Mg nuclei, even a single vacancy can produce fluctuations of the magnetic field of the order of $\mu$T for devices with $R = 100$ nm, see inset of Fig. 3. A second consequence of the large difference in magnetic moment with the nuclei is that the corresponding Larmor frequency for typical fields around $0.1T$ will be in the range of GHz.

![](./images/867746826638328252_3.jpg)

FIG. 3. Spectral response $\sigma(\omega)$ versus frequency $f = \omega/2\pi$ for a detector of radius $R = 100$ nm, $d = 1$ nm, $w = 3$ nm and $T_1 = 5\mu$s (black line) and $T_1 = 1\mu$s (red line), containing 320 $V_{Mg}$. A magnetic field gradient of $1\text{mT/nm}$ along the $z$-axis was assumed. Inset shows the integrated standard deviation $\sigma_{B_x}$ due to a single $V_{Mg}$ located at the center of the MgO layer versus the radius $R$.

The magnitude of the field, which determines the location of the spectral noise peak, is expected to change along the MgO layer since, in general, the magnetization on the FL and pinning layer is different. Magnetic field gradients up to $40 \text{ mT/nm}$ have been reported for magnetic disk heads. $^{22}$ In Fig. 3 we show the effect of a magnetic field gradient of $1 \text{ mT/nm}$. Expectedly, several peaks appear in the spectrum corresponding to different Larmor frequencies, whose position reflects variations of the field across the different Mg atomic planes, see Fig. 2(b).

The different peaks will be resolved if their spectral broadening is smaller than the splitting, $|\vec{m}|.|\partial_z B(z)|d/\hbar \gg 2\pi/T_1$. The relaxation time of these vacancies is much shorter than for the nuclear spins, below $100\mu$s. $^{23}$ Figure 3 shows the spectra corresponding to two different relaxation times, $T_1 =1$ and $5\mu$s. In both cases, the relative height of the different peaks will reflect the abundance of vacancies in each atomic plane of the MgO. Thereby, structural information concerning the distribution of Mg vacancies along the barrier could be inferred from measurements of the noise spectrum.

In conclusion, we have studied the impact of the fluctuating magnetic field created both by the $^{25}$Mg nuclear spins and Mg vacancies on a TMR magnetic field sensor with a thin MgO barrier, with circular section of radius $R$. The noise decreases inversely proportional to $R$ and it is spectrally peaked at the spin Larmor frequency, de-

termined by the magnetic field in the barriers, which is typically in the range of 500 kHz for the nuclear spins and 2GHz for the Mg vacancies. We argue that although the nuclear-induced noise in the 0.5MHz region is around 1 $\text{nT}/\sqrt{\text{Hz}}$ for devices with $R = 100$ nm, comparable to the $1/f$ noise, the vacancies-induced noise should be larger than $1\ \text{nT}/\sqrt{\text{Hz}}$ in the 2 GHz vicinity, well above the $1/f$ noise. We show that for a linearly varying magnetic field in the barrier, the noise spectrum can show a series of peaks whose position and height reflects the variations of the magnetic field magnitude and barrier spin density at the different Mg planes. Thus, measurement of this noise, through electrical characterization, could provide some sort of spin imaging of the barrier.

We acknowledge C. Untied for fruitful discussions. This work has been financially supported by MEC-Spain (Grant Nos. FIS2010-21883-C02-01, FIS2009-08744, and CONSOLIDER CSD2007-0010) as well as Generalitat Valenciana, grant Prometeo 2012-11.

$^1$S. Parkin, C. Kaiser, A. Panchula, P. Rice, B. Hughes, M. Samant, and S. Yang, Nature materials 3, 862 (2004).
$^2$S. Yuasa, T. Nagahama, A. Fukushima, Y. Suzuki, and K. Ando, Nature materials 3, 868 (2004).
$^3$S. Ingvarsson, G. Xiao, S. S. P. Parkin, W. J. Gallagher, G. Grinstein, and R. H. Koch, Phys. Rev. Lett. 85, 3289 (2000).
$^4$S. Parkin, X. Jiang, C. Kaiser, A. Panchula, K. Roche, and M. Samant, Proceedings of the IEEE 91, 661 (2003).
$^5$K. Klaassen, X. Xing, and J. van Peppen, Magnetics, IEEE Transactions on 41, 2307 (2005).
$^6$P. Freitas, R. Ferreira, S. Cardoso, and F. Cardoso, Journal of Physics: Condensed Matter 19, 165221 (2007).
$^7$W. Egelhoff, P. Pong, J. Unguris, R. McMichael, E. Nowak, A. Edelstein, J. Burnette, and G. Fischer, Sensors and Actuators A: Physical 155, 217 (2009).
$^8$Z. Lei, G. Li, W. Egelhoff, P. Lai, and P. Pong, Magnetics, IEEE Transactions on 47, 602 (2011).
$^9$M. Berglund and M. E. Wieser, Pure and Applied Chemistry 83, 397 (2011).
$^{10}$L. E. Halliburton, L. A. Kappers, D. L. Cowan, F. Dravnieks, and J. E. Wertz, Phys. Rev. Lett. 30, 607 (1973).
$^{11}$L. E. Halliburton, D. L. Cowan, W. B. J. Blake, and J. E. Wertz, Phys. Rev. B 8, 1610 (1973).
$^{12}$B. Rose and L. Halliburton, Journal of Physics C: Solid State Physics 7, 3981 (1974).
$^{13}$C. Araujo, M. Kapilashrami, X. Jun, O. Jayakumar, S. Nagar, Y. Wu, C. Arhammar, B. Johansson, L. Belova, R. Ahuja, et al., Applied Physics Letters 96, 232505 (2010).
$^{14}$N. J. Stone, Atomic Data and Nuclear Data Tables 90, 75 (2005).
$^{15}$T. Sleator, E. L. Hahn, C. Hilbert, and J. Clarke, Phys. Rev. Lett. 55, 1742 (1985).
$^{16}$C. L. Degen, M. Poggio, H. J. Mamin, and D. Rugar, Phys. Rev. Lett. 99, 250601 (2007).
$^{17}$J. Wertz, P. Auzins, J. Griffiths, and J. Orton, Discussions of the Faraday Society 28, 136 (1959).
$^{18}$P. S. Fiske, J. F. Stebbins, and I. Farnan, Physics and Chemistry of Minerals 20, 587 (1994).
$^{19}$J. Freitas and M. Smith, Annual Reports on NMR Spectroscopy p. 25 (2012).
$^{20}$R. Chaves, P. Freitas, B. Ocker, and W. Maass, Applied Physics Letters 91, 102504 (2007).
$^{21}$R. Chaves, P. Freitas, B. Ocker, and W. Maass, Journal of Applied Physics 103, 07E931 (2008).
$^{22}$C. Tsang, C. Bonhote, Q. Dai, H. Do, B. Knigge, Y. Ikeda, Q. Le, B. Lengsfield, J. Lille, J. Li, et al., Magnetics, IEEE Transactions on 42, 145 (2006).
$^{23}$A. Ferrari and G. Pacchioni, The Journal of Physical Chemistry 99, 17010 (1995).