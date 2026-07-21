# Electromechanical Conversion Efficiency of Biased Semiconductor Transducers

E. L. ADLER

Department of Electrical Engineering and Eaton Electronics Laboratory,
McGill University, Montreal, Quebec, Canada

The effect of drifting carriers on the electromechanical-conversion efficiency of a thin-film piezoelectric transducer deposited onto a delay rod is analyzed. When the acoustic loss in the transducer is due to the carriers only, significant improvement in the efficiency occurs near the half-wavelength or quarter-wavelength frequencies of the transducer, depending on whether the mechanical load presented by the delay rod is small or large. For supersonic carrier velocities, electromechanical-conversion gain is obtained near the mechanical resonances. A linear theory based on the acoustic-amplification mechanism is outlined and the extent of this electromechanical amplification illustrated by computations for a $2$-$\mu$-thick ZnO film.

## INTRODUCTION

HIGHLY efficient thin-film transducers made of piezoelectric semiconductors CdS, ZnO, and ZnS have been successfully operated at GHz frequencies.${}^{1,2}$ In the presence of carriers drifting with supersonic velocities, all three materials are capable of amplifying acoustic traveling waves, and in CdS oscillations have been observed at frequencies harmonically related to the acoustic resonant frequency of the samples.${}^{3,4}$ It has been shown that these instabilities are the direct result of the amplified acoustic waves, and calculations of the impedance of a suitably biased bar of CdS exhibit regions of negative resistance when the ends of the bar are stress free.${}^{5,6}$

The performance of a biased transducer mechanically loaded at once face by an acoustic delay rod differs from the above only in the boundary conditions that exist. Any power flow into the delay rod appears as an increase in the input resistance relative to the stress-free condition; for very light mechanical loads, we still find negative-resistance regions, whereas for higher loads, the extra resistance yields a net positive input resistance. A suitably biased transducer loaded by a delay rod acts like a negative-resistance amplifier when the acoustic power in the delay rod exceeds the electric rf power supplied to the transducer.

The analysis that follows describes these conditions, while calculations for a ZnO film show the amount of electromechanical conversion gain for various conditions of bias, conductivity, and mechanical loading.

## I. PHYSICAL CONFIGURATION

A transducer-delay-rod configuration consists of a thin-film transducer deposited onto a delay rod, where the transducer and delay rod are many wavelengths transverse to the direction of acoustic wave propagation, and the transducer electrodes are very much thinner than the acoustic wavelength. These conditions are typical of practical structures and justify a one-dimensional plane-wave analysis. The transducer is of length $L$ and active cross-sectional area $A$; the delay rod has a mechanical impedance $Z_{\text{R}}$.

## II. ACOUSTOELECTRIC PLANE-WAVE PROPAGATION

For plane waves in a piezoelectric semiconductor, the equations of state are

$$
T = cS - eE, \tag{1}
$$

$$
D = eS + \epsilon E, \tag{2}
$$

where $T$ and $S$ are the stress and strain, $D$ and $E$ the electric displacement and field, $c$ the elastic constant at constant field, $\epsilon$ the permittivity at constant strain, and

---
${}^{1}$ R. M. Malbon, D. J. Walsh, and D. K. Winslow, Appl. Phys. Letters **10**, 9-10 (1967).
${}^{2}$ N. F. Foster and G. A. Rozgonyi, Appl. Phys. Letters **8**, 221-223 (1966).
${}^{3}$ D. L. White and W. C. Wang, Phys. Rev. **149**, 628-30 (1966).
${}^{4}$ E. L. Adler and G. W. Farnell, Proc. IEEE **53**, 483-484 (1965).
${}^{5}$ A. R. Hutson, IEEE Ultrasonics Symp., Paper D7 (1965).
${}^{6}$ E. L. Adler and G. W. Farnell, J. Acoust. Soc. Am. **39**, 960-964 (1966).

SEMICONDUCTOR TRANSDUCERS

![](./images/812135975693058048_1.jpg)

FIG. 1. Efficiency response near half-wavelength frequency for
1.5-Ω·m resistivity film, 1.5×10⁵ kg sec·m⁻² delay-rod impedance.

$e$ the piezoelectric constant. For the one-dimensional case, the variables in Eqs. 1 and 2 are scalars, and when $U$ is the medium displacement, $S=\partial U/\partial x$. The equation of motion is

$$
\rho\partial^2 U/\partial t^2=\partial T/\partial x, \tag{3}
$$

where $\rho$ is the mass density.

It has been previously shown⁷ that the above Equation, together with Maxwell's equations and the constitutive equations for the medium, results in a quartic dispersion equation in the wave vector $k$:

$$
\begin{aligned}
\left[1-v_{\mathrm{D}}\left(\frac{k}{\omega}\right)+i\left(\frac{\omega}{\omega_{\mathrm{D}}}\right)\left(\frac{k}{\omega}\right)^{2}+i\left(\frac{\omega_{\mathrm{c}}}{\omega}\right)\right]\left[\left(\frac{k}{\omega}\right)^{2}-\frac{1}{v_{\mathrm{s}}{ }^{2}}\right] \\
+\left(\frac{e^{2}}{\epsilon C}\right)\left(\frac{k}{\omega}\right)^{2}\left[1-v_{\mathrm{D}}\left(\frac{k}{\omega}\right)+i\left(\frac{\omega}{\omega_{\mathrm{D}}}\right)\left(\frac{k}{\omega}\right)^{2}\right]=0,
\end{aligned}
$$

where $v_{\mathrm{D}}$ is the carrier drift velocity, $\omega_{\mathrm{c}}$ and $\omega_{\mathrm{D}}$ the conductivity and diffusion frequencies, $v_{\mathrm{s}}$ the velocity of sound at constant field, and $e^{2}/\epsilon c$ is essentially the square of the electromechanical-coupling constant. The solution of this quartic yields four allowed plane waves of form $\exp[i(kx-\omega t)]$, two quasiacoustic waves, and two quasicarrier waves characterized by a wave vector $k_j, j=1,2,3,4$.

⁷ D. L. White, J. Appl. Phys. 33, 2547-2554 (1962).

From Eqs. 3 and 1, the wave equation

$$
\rho\partial^2 u/\partial t^2=c\partial^2 U/\partial x^2-e\partial E/\partial x \tag{4}
$$

is obtained. It follows that for any plane wave corresponding to the wave vector $k_j$, the amplitude

$$
E_j=(ic/e)(k_j-\omega^2/v_{\mathrm{s}}{ }^{2}k_j{ }^{2})U_j, \tag{5}
$$

where $v_{\mathrm{s}}=(c/p)^{\frac{1}{2}}$.

Since the film thickness is finite, all waves will be present when the film is driven by an ac field, $E_0$, and the total material displacement, electric field, strain, stress, and velocity⁶ are:

$$
U_{\mathrm{F}}=\sum_{j=1}^{4} U_j \exp(ik_j x), \tag{6}
$$

$$
E_{\mathrm{F}}=E_{0}+i\frac{c}{e}\sum_{j=1}^{4}\left(1-\frac{\omega^{2}}{v_{\mathrm{s}}{ }^{2}k_{j}{ }^{2}}\right)k_j U_j \exp(ik_j x), \tag{7}
$$

$$
S_{\mathrm{F}}=\sum_{j=1}^{4} ik_j U_j \exp(ik_j x), \tag{8}
$$

$$
T_{\mathrm{F}}=-e E_{0}+\left(\frac{ic\omega^{2}}{v_{\mathrm{s}}{ }^{2}}\right)\sum_{j=1}^{4}\left(\frac{U_{j}}{k_{j}}\right)\exp(ik_j x), \tag{9}
$$

![](./images/812135975693058048_2.jpg)

FIG. 2. Efficiency near quarter-wavelength frequency for
2.2-Ω·m resistivity film, 1.5×10⁶ kg·sec·m⁻² delay-rod impedance.

The Journal of the Acoustical Society of America 843

![](./images/812135975693058048_3.jpg)

FIG. 3. Efficiency response near half-wavelength frequency for $v_{\mathrm{D}}=1.5 v_{\mathrm{s}}$, and $1.5 \times 10^{6} \mathrm{~kg} \cdot \mathrm{sec} \cdot \mathrm{m}^{-2}$ delay-rod impedance.

$$
G=\left(\frac{e^{2}}{\epsilon C}\right) \frac{\operatorname{Re}\left\{-\left[-i \omega \sum \lambda_{j} \exp \left(i k_{j} L\right)\right]\right\} *\left[-1+\left(i \omega^{2} / v_{\mathrm{s}}{ }^{2}\right) \sum\left(\lambda_{j} / k_{j}\right) \exp \left(i k_{j} L\right)\right]}{\operatorname{Re}\left(\omega_{\mathrm{c}}-i \omega\right) *\left\{L+\sum \lambda_{j}\left(1-\omega^{2} / v_{\mathrm{s}}{ }^{2} k_{j}{ }^{2}\right)\left[\exp \left(i k_{j} L\right)-1\right]\right\}},
$$

with the $\lambda_{j}=c U_{j} / e E_{0}$, a set of amplitude ratios that depend on boundary conditions. For any given frequency, drift velocity, and conductivity, the $k_{j}$ are obtained from the dispersion quartic, and for any given set of boundary conditions, the $\lambda_{j}$ can be obtained, thus completely specifying $G$.

### IV. BOUNDARY CONDITIONS

In this one-dimensional model, the film length $L$ locates the physical boundaries. It is assumed that the bar is stress free at one end $(x=0)$, loaded by a nonreflecting delay rod of mechanical impedance $Z_{\mathrm{R}}$ (real) at the other end $(x=L)$, and stress is continuous at this interface: that is,
$$
T_{\mathrm{F}}(0)=0, \quad(16)
$$
and
$$
T_{\mathrm{F}}(L)=T_{\mathrm{R}}. \quad(17)
$$

In the delay rod
$$
T_{\mathrm{R}}=-Z_{\mathrm{R}} v_{\mathrm{R}}
$$

$$
v_{\mathrm{F}}=-i \omega \sum_{j=1}^{4} U_{j} \exp \left(i k_{j} x\right), \quad(10)
$$
respectively, and $\exp (-i \omega t)$ dependence is understood

### III. POWER RELATIONS

The rf input power to the transducer is
$$
P_{\mathrm{IN}}=\frac{1}{2} \operatorname{Re}\left(V I^{*}\right), \quad(11)
$$
where * denotes complex conjugate, $V$ is the ac voltage across the film, and $I$ the current into film. The total ac voltage across the film of length $L$ is given by
$$
\begin{aligned}
V=\int_{0}^{L} E_{\mathrm{F}} d x=E_{0}\left\{L+\sum\right. & \left(\frac{c U_{j}}{e E_{0}}\right)\left(1-\frac{\omega^{2}}{v_{\mathrm{s}}^{2} k_{j}^{2}}\right) \\
& \left.\times\left[\exp \left(i k_{j} L\right)-1\right]\right\}. \quad(12)
\end{aligned}
$$

Since circuit current
$$
I=\left(\omega_{\mathrm{c}}-i \omega\right) \epsilon A E_{0}, \quad(13)
$$
the input power can be calculated.

The acoustic power into the delay rod is
$$
P_{\mathrm{OUT}}=\frac{1}{2} \operatorname{Re}\left(-A T_{\mathrm{R}} v_{\mathrm{R}}^{*}\right). \quad(14)
$$

Since stress and velocity continuity must hold at the film-rod interface, the stress $T_{\mathrm{R}}$ and the velocity $v_{\mathrm{R}}$ in the rod at the interface are simply $T_{\mathrm{F}}(L), v_{\mathrm{F}}(L)$, respectively, and are obtained by evaluating Eqs. 9 and 10 at $x=L$. The output power can be calculated from Eq. 14. The electromechanical-conversion efficiency
and from Eq. 17
$$
T_{\mathrm{F}}(L)=-Z_{\mathrm{R}} v_{\mathrm{R}}. \quad(18)
$$

Velocity continuity across the interface implies
$$
v_{\mathrm{R}}=v_{\mathrm{F}}(L)=-i \omega \sum U_{j} \exp \left(i k_{j} L\right),
$$
so that
$$
T_{\mathrm{F}}(L)=i \omega Z_{\mathrm{R}} \sum U_{j} \exp \left(i k_{j} L\right). \quad(19)
$$

From Eqs. 1, Eqs. 7-9 evaluated at the two film faces, and Eqs. 16 and 19, one obtains the following restrictions on the $\lambda_{j}$ :
$$
\sum i \omega^{2} \lambda_{j} / v_{\mathrm{s}}^{2} k_{j}=1, \quad(20)
$$
and
$$
\sum\left(i \omega / v_{\mathrm{s}}\right)\left(\omega / v_{\mathrm{s}} k_{j}-Z_{\mathrm{R}} / Z_{\mathrm{F}}\right) \lambda_{j} \exp \left(i k_{j} L\right)=1, \quad(21)
$$
where
$$
Z_{\mathrm{F}}=\rho v_{\mathrm{s}}.
$$

As electrical boundary conditions the plane-wave component of current density is set to zero at the elec-

SEMICONDUCTOR TRANSDUCERS

![](./images/812135975693058048_4.jpg)

FIG. 4. Efficiency response near half-wavelength frequency for $v_{\mathrm{D}}=1.5 v_{\mathrm{s}}$, and $1.5-\Omega \cdot \mathrm{m}$ resistivity film.

trodes. The plane-wave component of $D$ is then zero, and from Eqs. 2, 7, and 8, one obtains the following relations:

$$
\sum\left(1+e^{2} / \epsilon c-\omega^{2} / v_{\mathrm{s}}^{2} k_{j}^{2}\right) i k_{j} \lambda_{j}=0 \quad(22)
$$

$$
\sum\left(1+e^{2} / \epsilon c-\omega^{2} / v_{\mathrm{s}}^{2} k_{j}^{2}\right) i k_{j} \lambda_{j} \exp \left(i k_{j} L\right)=0. \quad(23)
$$

The calculation for the efficiency can now be performed as the $\lambda_{j}$ are completely established.

When $\omega<\omega_{\mathrm{D}}$, it is quite justifiable to neglect the effect of diffusion. This reduces the dispersion equation to a cubic, and for this three-wave approximation, the condition corresponding to Eq. 23 is omitted.

## V. COMPUTED RESULTS

The electromechanical efficiency of a $2-\mu \mathrm{ZnO}$ film on a delay rod has been calculated for different values of film conductivities, carrier drift velocities, and delayrod acoustic impedances. These calculations were made with both the three-wave and the four-wave conditions described, in order to show quantitatively the effect of carrier diffusion on efficiency. For longitudinal waves $v_{\mathrm{s}}=6000 \mathrm{~m} / \mathrm{sec}$, and $e^{2} / \epsilon c=0.16$.

A typical efficiency response near the half-wave frequency of the film is shown in Fig. 1. For a delay-rod mechanical impedance one hundredth that of the film, the carrier-drift velocity has a very marked effect on the conversion loss. With a carrier velocity of one and one-half times the sound velocity, an improvement in efficiency by a factor of almost 10 is obtained relative to the zero-velocity condition. In fact, over a bandwidth of about $40 \mathrm{MHz}$, a net conversion gain occurs. At higher drift velocities, the system becomes unstable and calculations of the electrical impedance of the film reveal a negative real part in the interval labeled unstable in Fig. 1.

For a very high mechanical load, the frequency where the resonance occurs is near the quarter-wave frequency of the film. The results obtained for a mechanical load impedance one hundred times that of the film is shown in Fig. 2. The behavior is virtually identical to that obtained in Fig. 1.

The effect of film conductivity is shown in Fig. 3 for five values of conductivity. The main result that this set of curves points out is that the interaction is strongest for conductivity frequency values close to the operating frequency.

In Fig. 4, the result of changing the mechanical impedance that terminates the film is shown. It is seen that as the mechanical load is increased, the response peak broadens and the efficiency at the half-wave frequency drops. This behavior is similar to any transducer performance differing only in the existence of conversion gain for light loading.

![](./images/812135975693058048_5.jpg)

FIG. 5. Improvement in efficiency relative to zero-bias value for $v_{\mathrm{D}}=1.5 v_{\mathrm{s}}$, and $1.5-\Omega \cdot \mathrm{m}$ resistivity film.

The Journal of the Acoustical Society of America 845

E. L. ADLER

![](./images/812135975693058048_6.jpg)

FIG. 6. Comparison of three-wave and four-wave calculated efficiency near half-wavelength frequency. Film resistivity is 1.1- $\Omega \cdot \mathrm{m}$, and delay-rod impedance is $1.5 \times 10^{6} \mathrm{~kg} \cdot \mathrm{sec} \cdot \mathrm{m}^{-2}$.

The extent of the improvement in efficiency due to film biasing is shown in Fig. 5. It is clear from this repre- sentation that the improvement ceases to be very sig- nificant for impedance ratios much less than 10. It should be pointed out that such high impedance ratios are not normally encountered with usual substrate materials. These ratios can be obtained by the deposi- tion of multiple layers of high- and low-impedance materials between the transducer and the substrate to form an acoustic-impedance transformer. A multilayer transformer of this type is essentially narrow band and is of practical interest only in narrow-band applications.

All the results shown have been computed using the three-wave approximation and in Fig. 6, a comparison is made between this and the full four-wave analysis at zero field and also for $v_{\mathrm{D}} / v_{\mathrm{S}}=1.5$. It is seen that there is about $50 \%$ difference between the two computations over a narrow band right at the response peak, but else- where the two curves come very close together.

Reversal of the direction of carrier drift has an in- significant effect on the results, so that the resonant conversion gain does not depend on bias polarity.

In summary, it has been shown that by suitable bias- ing of thin-film transducers, acoustic amplification gives rise to a decrease in acoustic losses, which results in a resonant increase in electromechanical-conversion effi- ciency. The magnitude of the effect has been illustrated by calculations at gigahertz frequencies for a $2-\mu \mathrm{ZnO}$ film. The results indicate that the effect is greatest under relatively narrow-band conditions of operation. In fact, by a suitable choice of mechanical load, the transducer becomes unstable, indicating the possibility of a self- oscillating acoustic generator consisting of a suitably biased thin-film transducer. Thus, such a thin film can either be biased to operate as a transducer having con- version gain, or, by biasing into an unstable region where there will be spontaneous oscillation, used as an acoustic oscillator.

## ACKNOWLEDGMENT

This research was supported by the National Re- search Council and the Defence Research Board of Canada.