# Terahertz dielectric response of cubic BaTiO₃

I. Ponomareva,¹ L. Bellaiche,¹ T. Ostapchuk,² J. Hlinka,² and J. Petzelt²

¹Department of Physics, University of Arkansas, Fayetteville, Arkansas 72701, USA
²Institute of Physics, Academy of Sciences of the Czech Republic, Na Slovance 2, 18221 Prague 8, Czech Republic

(Received 14 November 2007; published 24 January 2008)

A first-principles-based approach is developed to study the dielectric response of paraelectric BaTiO₃, as a function of frequency and temperature. *Two* different overdamped modes of comparable strengths are found to contribute to such response, in the $\approx 1-150$ cm⁻¹ frequency range for temperatures up to $\approx 750$ K. The lower frequency mode softens toward the Curie point, while the higher-frequency mode stays in the $60-100$ cm⁻¹ range and is associated with temperature-independent short-range correlations. Our far-infrared reflectivity measurements confirm the existence of these two modes, and yield a very good agreement with calculations.

DOI: 10.1103/PhysRevB.77.012102
PACS number(s): 77.22.Ch, 77.22.Gm, 77.84.−s, 78.30.−j

Ferroelectrics are of growing importance for a variety of device applications.¹,² One property of technological importance in these materials is the frequency-dependent complex dielectric response. Optimizing such property will lead to the design of desired optimized devices (such as phase arrays) combining low dielectric loss and high tunability in the gigahertz to terahertz regime.³ However, several fundamental features of the complex dielectric response in ferroelectrics are presently still unclear. For instance, the most recent infrared reflectivity measurement⁴ conducted in the paraelectric phase of one of the most studied ferroelectric systems,⁵,⁶ BaTiO₃, reports a single mode that levels off near 60 cm⁻¹ close to the Curie temperature $T_C$, which dramatically contrasts with hyper-Raman scattering results⁷,⁸ and transmission spectroscopy in near-millimeter range⁶ that display a single mode that continuously decreases almost to the zero frequency when approaching from above $T_C$. Reference 9 attempted to reconcile the contradictory data of Refs. 4 and 7 by evoking the possibility that the dielectric response of BaTiO₃ results, in fact, from *two* modes. However, Ref. 9 did not find any conclusive evidence for that. Moreover, the microscopic characteristics of these two modes remain unclear, if they both indeed exist. Obviously, accurate atomistic simulations are needed to predict and understand at a microscopic level the complex dielectric response $\varepsilon$ of ferroelectrics. Since the beginning of the 1990s, first-principles methods have emerged as a powerful tool for investigating ferroelectrics.¹⁰⁻¹⁴ However, predicting $\varepsilon$ as a function of frequency and temperature is an important challenge that has not yet been accomplished by first-principles-based approaches.

The purpose of this Brief Report are two fold: (1) to demonstrate that it is possible to develop such a scheme for ferroelectrics; (2) to apply it to reveal that the dielectric response of cubic BaTiO₃ is dominated, in the $\approx 1-150$ cm⁻¹ frequency range, by two modes, and to provide microscopic insight of these two modes. We also conducted far-infrared measurements that confirm the simultaneous existence of these two modes, and yield data in very good agreement with our predictions.

Calculations are performed in the framework of the first-principles-based scheme of Ref. 15. Previous *Monte Carlo* simulations¹⁵ with a $14\times 14\times 14$ supercell of BaTiO₃ yielded the correct cubic-tetragonal-orthorhombic-rhombohedral transition sequence with transition temperatures of 385, 280, and $230\pm 5$ K, respectively, in good agreement with the corresponding experimental values of $\approx 400$, 280, and 180 K.¹⁷ Here, we use the same supercell to undertake *molecular dynamics* (MD) simulations, with Newton's equations of motion being solved for all the variables included in the effective Hamiltonian approach, namely, the local soft modes (which are proportional to the dipoles and are associated with the lowest optical phonon modes), and the inhomogeneous and homogeneous strain variables.¹⁸ To determine the phase sequence within MD, we perform computations associated with a constant number of particles $N$, pressure $P$, and temperature $T$ ($NPT$ ensemble¹⁹), using an Evans-Hoover thermostat¹⁹⁻²¹ and the barostat being mimicked through the $PV$ energetic term of the effective Hamiltonian approach, which allows the simulation cell to vary in size and shape. The $NPT$ simulations (40 000 MD steps, each step being 1 fs) exactly reproduced the transition temperatures obtained in Ref. 15. To determine the complex dielectric response from MD simulations, we follow the approach of Ref. 22:

$$
\varepsilon(\nu)-1=\frac{1}{3\varepsilon_0 Vk_B T}\left[\langle\mathbf{M}^2\rangle+i2\pi\nu\int_{0}^{\infty}dte^{i2\pi\nu t}\langle\mathbf{M}(t)\cdot\mathbf{M}(0)\rangle\right],
\tag{1}
$$

where "$\langle\,\rangle$" denotes thermal averages, while $V$, $t$, and $\nu$ are the volume of the chosen supercell, the time, and the frequency, respectively. $\langle\mathbf{M}^2\rangle$ is the time-averaged square of the total dipole moment of the supercell and $\langle\mathbf{M}(t)\cdot\mathbf{M}(0)\rangle$ is the dipole moment autocorrelation function¹⁹,²² (ACF). Practically, we first run 20 000 MD steps of $NPT$ simulations to equilibrate the system at a chosen temperature. After that, both the thermostat and the barostat are turned off and the homogeneous strain variables are frozen, and another 5 000 MD steps are performed to equilibrate the system at fixed number of particles $N$, volume $V$, and average total energy $E$ ($NVE$ ensemble, which is required to obtain dynamical properties¹⁹). Subsequent 2 975 000 additional $NVE$ steps are conducted to obtain 10 000 individual $\mathbf{M}(t)\cdot\mathbf{M}(0)$ functions—for *any* time $t$ ranging from 0 to 8.2 ps by steps of 4 fs—via the overlap approach.¹⁹ These 10 000 individual


![](./images/811940855270080513_1.jpg)

FIG. 1. Complex dielectric response of cubic BaTiO₃ versus frequency at T=440 (bold lines) and 470 K (thin lines). Panels (a) and (b) display the $\varepsilon'$ real and $\varepsilon''$ imaginary parts, respectively. The solid lines show our predictions, while the dashed lines report our measurements. The arrows emphasize the frequencies of the two peaks of $\varepsilon''$ associated with Eq. (2).

$\mathbf{M}(t)\cdot\mathbf{M}(0)$ are then averaged to obtain the ACF. The $\mathbf{M}^2$ is averaged over the last 2 975 000 $NVE$ steps to obtain $\langle\mathbf{M}^2\rangle$, and then used, along the Fourier transform$^{23}$ of the ACF, to determine $\varepsilon$ from Eq. (1).

One definite result arising from our numerical approach is that, for any temperature ranging between $T_C$ and $\simeq$750 K, a good fit of the predicted dielectric function requires two classical damped harmonic oscillators$^{24,25}$ rather than a single one:
$$
\varepsilon(\nu)=\varepsilon_{\infty}+\frac{S_{1}}{\nu_{1}^{2}-\nu^{2}+i \nu \gamma_{1}}+\frac{S_{2}}{\nu_{2}^{2}-\nu^{2}+i \nu \gamma_{2}},\tag{2}
$$
where $\nu_1$, $\gamma_1$, $S_1$ (respectively, $\nu_2$, $\gamma_2$, $S_2$) are the frequency, damping constant, and oscillator strength of the first (respectively, second) oscillator. Here, we omit the high-frequency permittivity $\varepsilon_\infty$ in the simulated response since our model accounts for a single ionic polar displacement per unit cell only.$^{26}$ The coexistence of two modes contrasts with previous observations in the paraelectric phase of BaTiO₃ for which only one single mode was reported down to $T_C$.$^{4,7}$ Let us note that $S_1$ and $S_2$ are found to be of comparable magnitude and fairly temperature independent. We also conducted far-infrared measurements on a melt-grown single crystal (for which $T_C$$\simeq$406 K), and used a Fourier transform IR interferometer Bruker 113v with the near-normal specular reflectance, as well as a custom-made oven to heat the sample up to 760 K. The interferogram of the nonilluminated sample (measured with the masked IR source) was subtracted from the interferogram of the illuminated one,$^{25}$ in order to exclude the distortion of the spectra caused by the thermal emission of the sample. Our reflectivity spectra above $T_C$ were fitted with the damped harmonic oscillators model$^{25}$ to extract the complex dielectric response. Furthermore, we used the low-frequency reflectivity data from Ref. 27 and dielectric function from Ref. 6, to accurately fit the lowest mode. Our measurements do confirm that two modes are indeed necessary to describe properly the dielectric function below 150 $\text{cm}^{-1}$ from $T_C$ up to $\simeq$750 K.

Comparison of $\varepsilon$ obtained from our simulations and measurements at two different temperatures$^{28}$ is shown in Fig. 1.

![](./images/811940855270080513_2.jpg)

FIG. 2. (Color online) Temperature evolution of the $\nu_1'$ and $\nu_2'$ frequencies [panel (a)], and of the $\nu_1$ and $\nu_2$ frequencies [panel (b)]. Our first-principles-based data are shown in open symbols, while the solid symbols display experimental results. The solid circles and squares report our own measurements, while the solid diamonds and triangles indicate the observations of Refs. 4 and 7, respectively.

The correspondence is very satisfactory. In particular, the simulations reproduce rather well the observed increase in $\varepsilon'(\nu)$ at the smallest displayed frequencies, when decreasing $T$ toward $T_C$. Both techniques also yield the second peak (shoulder) of $\varepsilon''(\nu)$. The temperature dependence of the characteristic frequencies of the two modes is displayed in Fig. 2. Figure 2(a) shows the $\nu_1'$ and $\nu_2'$ frequencies for which the imaginary part of the dielectric function associated with the first and second oscillators of Eq. (2) peaks, respectively. These two frequencies are appreciably lower than $\nu_1$ and $\nu_2$, respectively, for oscillators having non-negligible damping constants, as shown in Fig. 2(b). Clearly, our calculations and observations agree with each other for the positions of the two peaks for a wide range of temperatures—especially, from $T_C$ to 550 K. [The agreement is less satisfactory for $\nu_1'$ above 550 K, likely because of the coupling of the soft mode with other degrees of freedom at high $T$. Also, our predicted $\nu_2$ close to $T_C$ slightly differ from our measured ones, likely because it is difficult to reliably determine both $\nu_2$ and $\gamma_2$ independently from each other$^{24}$ in Eq. (2).] Both techniques indicate that (1) $\nu_1'$ approaches zero when decreasing the temperature toward the Curie point, (2) $\nu_2'$ saturates around 60–70 $\text{cm}^{-1}$ close to $T_C$, and (3) the two oscillators occur for any temperature from $T_C$ up to $\simeq$750 K.$^{29}$

Let us now try to use our predictions and measurements to understand previous experimental data$^{4,7}$ that qualitatively differ from each other upon cooling down to $T_C$ [see Fig. 2(b)]: Ref. 7 reports a single mode that continuously softens while the mode of Ref. 4 saturates around 60 $\text{cm}^{-1}$. Figure 2(b) demonstrates a rather good agreement with our own observations and those reported in Ref. 7, for the fitted values of $\nu_1$. Reference 7 did not report the second mode $\nu_2$ because they fitted their dielectric data (as deduced from their hyper-Raman data) by a single oscillator. Such fit resulted in an unusually large damping parameter, which implies that their dielectric data can also be fitted by two overdamped oscillators—with the first mode having a frequency close to the single one they reported while the second mode

has a higher frequency.⁷ However, the authors of Ref. 7 decided to disregard this possible two-mode behavior partly due to a lack of microscopic understanding about the origin of the dielectric response. Regarding the mode reported in Ref. 4, the saturation of its frequency below 550 K indicates that it is related to our second mode. We would like to suggest that the data of Ref. 4 are not accurate for frequencies below 40 cm⁻¹, which led to a response of the low-frequency mode being substantially suppressed while the high-frequency mode contribution became more pronounced. Fitting these data with only one oscillator explains why the frequency of the mode of Ref. 4 falls in between the frequencies of our two modes, $\nu_1$ and $\nu_2$, both for our predictions and own measurements [see Fig. 2(b)]—since the mode reported in Ref. 4 likely contains both a (weak) contribution from our low-in-frequency mode and a (large) contribution from our high-in-frequency mode.

We also performed calculations using our proposed scheme to compute $\varepsilon$ of disordered $\text{Pb}(\text{Zr}_{0.4}\text{Ti}_{0.6})\text{O}_3$ and $(\text{Ba}_x\text{Sr}_{1-x})\text{TiO}_3$, with $x>0.4$, in their paraelectric phase. We chose these two materials because effective Hamiltonian parameters are already avaliable for them,¹⁵ˣ³⁰ and because they exhibit a tetragonal *versus* a rhombohedral ground state, respectively. The former is found to adopt a *single-mode* behavior while the latter exhibits a two-mode behavior as in $\text{BaTiO}_3$. Moreover, changing the sign of the so-called $\gamma$ parameter of the effective Hamiltonian¹⁶ of $\text{BaTiO}_3$ (to make it ferroelectric tetragonal at the lowest temperatures) led to the dielectric data of this "artificial" $\text{BaTiO}_3$ being well fitted by a single mode in its paraelectric phase. (Note that this $\gamma$ parameter is related to the anharmonicity of the underlying potential.) All these findings suggest that a two-mode behavior is more likely to occur in systems exhibiting a ferroelectric ground state of rhombohedral rather than tetragonal symmetry. The precise reason behind the need for a rhombohedral symmetry of the ground state to have a two-mode behavior may be connected with the eight-site model proposed in Ref. 31 but is beyond the scope of this Brief Report.

To get an additional insight behind the two-mode structure of $\varepsilon$ of $\text{BaTiO}_3$ in its paraelectric phase, we found it convenient to express the total dipole moment of the supercell as $\mathbf{M}=\sum_i m_i$, where $m_i$ is the dipole moment of unit cell $i$, and to rewrite Eq. (1) as

$$
\varepsilon(\nu)-1=\sum_{\mathbf{r}} \chi(\nu, \mathbf{r})
$$

with

$$
\begin{aligned}
\chi(\nu, \mathbf{r})= & \frac{1}{3 \varepsilon_0 V k_B T}\left[\left\langle\sum_i \mathbf{m}_i \cdot \mathbf{m}_{i+\mathbf{r}}\right\rangle\right. \\
& \left.+i 2 \pi \nu \int_0^\infty d t e^{i 2 \pi \nu t}\left\langle\sum_i \mathbf{m}_i(t) \cdot \mathbf{m}_{i+\mathbf{r}}(0)\right\rangle\right], \quad (3)
\end{aligned}
$$

where $\mathbf{r}=(x,y,z)$ is a vector connecting the unit cells $i$ and $i+\mathbf{r}$. Equation (3) provides a real-space decomposition of $\varepsilon$ in terms of correlations between dipoles located at cells separated by $\mathbf{r}$. Figure 3 displays the two-dimensional cross sections of the (normalized) imaginary part of $\chi(\nu, \mathbf{r})$ for three different temperatures at the corresponding $\nu_i'$ frequencies. Figure 3 reveals that the high-frequency response of $\text{BaTiO}_3$ is associated with (mostly) temperature-independent short-range correlations along the $\langle 100\rangle$ directions, while the low-frequency response is clearly associated with the soft mode since a long-range correlation between all the different cells continuously develops as the temperature decreases toward $T_C$. Interestingly, short-range correlations along the $\langle 100\rangle$ directions were previously obtained in molecular dynamics simulations of $\text{KNbO}_3$,³² and are known to produce the characteristic x-ray or neutron diffuse scattering in $\text{BaTiO}_3$-type ferroelectrics.³³ˣ³⁴

![](./images/811940855270080513_3.jpg)

FIG. 3. (Color online) Real-space decomposition, $\chi''(\nu=\nu_i',x,y,z=0)/(\varepsilon''(\nu=\nu_i')-1)$ (for $i=1$ and 2, expressed in percent and for three different temperatures), of the two peaks of the imaginary part of the dielectric constant. The $x$, $y$, and $z$ axes are chosen along the [100], [010], and [001] directions, respectively, and their coordinates are expressed in terms of the five-atom unit cell lattice's constant (that is, $a=3.9$ Å).

In summary, we have developed a first-principles-derived computational scheme to investigate the complex dielectric response of paraelectric $\text{BaTiO}_3$ as a function of frequency and temperature. We resolved a 25 year old controversy⁴ˣ⁷ by determining that there are two modes that contribute to such response, in the $\simeq 1-150$ cm⁻¹ frequency range. One mode softens toward zero when approaching $T_C$ from above. On the other hand, the second mode is associated with small correlated regions of needlelike shape and saturates toward 70 cm⁻¹ close to $T_C$. We also conducted far-infrared measurements that confirm the existence of these two modes and yield an excellent agreement with our predictions. We are confident that the present numerical technique will lead to the design of optimized devices in the near future.


We thank I. Kornev, J. Iñiguez, and CPD scientists for useful discussions. This work is supported by NSF Grant Nos. DMR-0404335, DMR-0701558, and DMR-0080054, by ONR Grant Nos. N00014-04-1-0413 and N00014-01-1-0365, by DOE Grant No. DE-FG02-05ER46188, and by the Czech Science Foundation (GACR 202/06/0411 and 202/06/P219). Some computations were made possible thanks to the MRI Grant No. 0421099 from NSF. One of the authors (T.O.) acknowledges financial support of L'OREAL CR "For Women in Science Scholarship Program."

$^{1}$K. Uchino, *Piezoelectric Actuators and Ultrasonic Motors* (Kluwer Academic, Boston, 1996).

$^{2}$K. Abe and S. Komatsu, J. Appl. Phys. **77**, 6461 (1995).

$^{3}$A. Tagantsev, V. Sherman, K. Astafiev, J. Venkatesh, and N. Setter, J. Electroceram. **11**, 5 (2003).

$^{4}$Y. Luspin, J. Servoin, and F. Gervais, J. Phys. C **13**, 3761 (1980).

$^{5}$J. Scott, Rev. Mod. Phys. **46**, 83 (1974).

$^{6}$J. Petzelt, G. Kozlov, and A. Volkov, Ferroelectrics **73**, 101 (1987).

$^{7}$H. Vogt, J. Sanjurjo, and G. Rossbroich, Phys. Rev. B **26**, 5904 (1982).

$^{8}$K. Inoue and S. Akimoto, Solid State Commun. **46**, 441 (1983).

$^{9}$H. Presting, J. A. Sanjurjo, and H. Vogt, Phys. Rev. B **28**, 6097 (1983).

$^{10}$D. Vanderbilt, Curr. Opin. Solid State Mater. Sci. **2**, 701 (1997).

$^{11}$L. Bellaiche, Curr. Opin. Solid State Mater. Sci. **6**, 19 (2002).

$^{12}$I. Ponomareva, I. I. Naumov, I. Kornev, H. Fu, and L. Bellaiche, Curr. Opin. Solid State Mater. Sci. **9**, 114 (2005).

$^{13}$M. Dawber, K. M. Rabe, and J. F. Scott, Rev. Mod. Phys. **77**, 1083 (2006).

$^{14}$I. Kornev, H. Fu, and L. Bellaiche, J. Mater. Sci. **41**, 137 (2006).

$^{15}$L. Walizer, S. Lisenkov, and L. Bellaiche, Phys. Rev. B **73**, 144105 (2006).

$^{16}$W. Zhong, D. Vanderbilt, and K. M. Rabe, Phys. Rev. B **52**, 6301 (1995).

$^{17}$C. Menoret, J. M. Kiat, B. Dkhil, M. Dunlop, H. Dammak, and O. Hernandez, Phys. Rev. B **65**, 224104 (2002).

$^{18}$The effective Hamiltonian $(\mathbf{H}_{eff})$ approach of Ref. 15 is constructed using the force-constant matrix. The mass of the soft mode in the present MD simulations is given by $M=k/\omega^{2}$, where $k$ and $\omega^{2}$ are the soft-mode eigenvalues of the force-constant matrix and dynamical matrix, respectively. We constructed a similar $\mathbf{H}_{eff}$ but with parameters derived from the dynamical matrix. Such $\mathbf{H}_{eff}$ provides transition temperatures that are further away from measurements than those predicted using the force-constant-matrix effective Hamiltonian, $^{15}$ while yielding qualitatively similar dielectric constants above the Curie temperature. For these reasons, we only report here results obtained from the force-constant-matrix-based effective Hamiltonian of Ref. 15.

$^{19}$D. Rapaport, *The Art of Molecular Dynamics Simulation* (Cambridge University Press, Cambridge, 2001).

$^{20}$W. G. Hoover, A. J. C. Ladd, and B. Moran, Phys. Rev. Lett. **48**, 1818 (1982).

$^{21}$D. J. Evans, J. Chem. Phys. **78**, 3297 (1983).

$^{22}$J. Caillol, D. Levesque, and J. Weis, J. Chem. Phys. **85**, 6645 (1986).

$^{23}$W. H. Press, S. A. Teukolsky, W. T. Vetterling, B. P. Flannery, and M. Metcalf, *Numerical Recipes in FORTRAN 90*, online: www.nr.com

$^{24}$E. Buixaderas, S. Kamba, and J. Petzelt, Ferroelectrics **308**, 131 (2004).

$^{25}$F. Gervais, in *Infrared and Millimeter Waves*, edited by K. Button (Academic, New York, 1983), Vol. 8, pp. 279–339.

$^{26}$Note that our model possesses only one polar degree of freedom per five-atom unit cell, which is the local soft mode (Refs. 15 and 16), while two contribute to the dielectric function, as seen, e.g., in Fig. 1. These two modes thus have eigenvectors (in the sense of normal coordinates as usually introduced in theory of lattice dynamics) that are completely identical, and that correspond to the soft-mode eigenvectors of the force-constant matrix, namely, +0.31, +0.75, −0.30, and −0.40 for Ba, Ti, $O_1$, and $O_3$ atoms, respectively, in which $O_1$ and $O_3$ are the two kinds of oxygen atoms that are different by symmetry when the polarization points along a $\langle 001 \rangle$ direction. These two modes are therefore associated with different correlations of the local soft modes between different five-atom unit cells, as we will see in Fig. 3.

$^{27}$J. Ballantyne, Phys. Rev. **136**, A429 (1964).

$^{28}$The theoretical temperatures are shifted upward by 20 K to account for the slight underestimation of the cubic-to-tetragonal transition temperature by the presently used effective Hamiltonian approach.

$^{29}$Above $\simeq 750$ K, our measurements and simulations can be approximated with a single classical damped harmonic oscillator.

$^{30}$L. Bellaiche, A. García, and D. Vanderbilt, Phys. Rev. Lett. **84**, 5427 (2000); Ferroelectrics **266**, 41 (2002).

$^{31}$R. Comes, M. Lambert, and A. Guinier, Solid State Commun. **6**, 715 (1968).

$^{32}$H. Krakauer, R. Yu, C.-Z. Wang, K. Rabe, and U. Waghmare, J. Phys.: Condens. Matter **11**, 3779 (1999).

$^{33}$M. Holma, N. Takesue, and H. Chen, Ferroelectrics **237**, 164 (1995).

$^{34}$R. Comes, M. Lambert, and A. Guinier, Acta Crystallogr., Sect. A: Cryst. Phys., Diffr., Theor. Gen. Crystallogr. **26**, 244 (1970).