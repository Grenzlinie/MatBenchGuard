# Choice of testing conditions for gamma radiometry methods

Z. GODLEWSKI

The Kinetic, geometric and radiological factors affecting the detection of flaws are discussed theoretically and checked against experimental results. The results obtained from each method proved to be almost identical.

In the most frequently used radiometric method of testing, the collimated radiation beam is emitted by a stationary source of radiation in the direction of the object under investigation, which is travelling at a constant velocity. The radiation beam passes through the object under test, reaches the collimator which is mounted on a probe, and falls on a stationary radiation counter. The increase of pulses caused by the increase of radiation indicates the presence of a flaw.
The flashes, caused by radiation quanta in the scintil- lation counter, are transformed by a photomultiplier into electrical pulses, which in turn are integrated into an RC system (resistance integrator condenser). Integration of pulses requires RC time dependence called the 'integrator time constant'. Some radiation is scattered, and the spectrum recorded by the coun- ter is therefore made up of quanta of both primary and scattered radiation. In view of this, the measure- ment of radiation, and therefore the detection of flaws by a radiometric method is affected by the following factors:

Kinetic factors comprising the shape and dimen- sions of the flaw and the radiation beam, the speed of the tested object and the integrator time constant.

Geometric factors comprising position, shape and dimensions of the source, the collimators, the tested object and the flaw.

Radiological factors comprising the type of radiation source, the thickness and nature of the material to be tested, and the dimensions and type of scintillator.

## KINETIC FACTORS

The number of pulses recorded by a counter when a beam of radiation is passed through the flawed material is determined by the equation

$$
\mathrm{N}_{\mathrm{W}}=\mathrm{N}\left[1+\mathrm{f}\left(\mathrm{e}^{\mu \mathrm{X}}-1\right) / \mathrm{F}\right] \tag{1}
$$

where N is the number of pulses from material with- out flaws, $N_W$ is the number of pulses from material with flaws, f is the surface area of the flaw illuminat- ed by the radiation beam, F is the surface area of the radiation beam on the material, $\mu$ is the attenuation coefficient in the tested material, and x is the thick- ness of the flaw.

It is also known that the number of impulses recorded are in direct proportion to the voltage in the integrat- ing system. Therefore, the number of pulses $N_t$ with rectangular shape shown by the integrator in time t is

$$
\mathrm{N}_{\mathrm{t}}=\mathrm{N}_{\mathrm{W}}\left(1-\mathrm{e}^{-\mathrm{t} / \tau}\right) \tag{2}
$$

where $N_W$ is the number of impulses from the mate- rial with a flaw corresponding to the saturation volt- age for the illuminated flaw area and $\tau$ is the RC-time constant of the integrator.

The relative increase of pulses with time as the flaw passes through the radiation beam can be calculated using eqns 1 & 2, assuming that the flaw is of uniform thickness, and that the ratio of the flaw cross-section in the radiation beam to the field F of this beam, increases linearly in time t as the flaw passes through the beam. The relative increase after time $t > t_3 > t_2 > t_1$ becomes

$$
\begin{aligned}
\Delta \mathrm{N} / \mathrm{N} &=\alpha\left(\mathrm{e}^{\mu \mathrm{X}}-1\right)\left[\mathrm{t}_{1}+\mathrm{t}_{2}-\mathrm{t}_{3}+\right. \\
&\tau\left(\mathrm{e}^{-\left(\mathrm{t}-\mathrm{t}_{1}\right) / \tau}+\mathrm{e}^{-\left(\mathrm{t}-\mathrm{t}_{2}\right) / \tau}-\right. \\
&\left.\left.\mathrm{e}^{-\left(\mathrm{t}-\mathrm{t}_{3}\right) / \tau}-\mathrm{e}^{-\mathrm{t} / \tau}\right)\right]
\end{aligned} \tag{3}
$$

where $\alpha$ is the constant, characteristic of the linear increase of the ratio of the flaw cross-section to the beam cross-section, or the rate of change of this ratio with time as the flaw passes through the radia- tion beam. $t_1$ is the time after which the maximum

The author is Head of the Radiometry Laboratory, Institute for Electrotechnics, Warsaw, Poland.

126 non-destructive testing April 1971

flaw area has been covered by the radiation beam.
$t_2$ is the time after which the flaw area in the radiation beam has decreased, $t_3$ is the time, after which the radiation beam has passed through the flaw. In the periods of time when

$$t_3 > t > t_2 > t_1 \text{ and } (t - t_3) = 0$$

then $t_3 = t$

$$t_3 > t_2 > t > t_1, \text{ and } (t - t_2) = 0$$

then $t_2 = t_3 = t$

$$t_3 > t_2 > t_1 > t \text{ and } (t - t_1) = 0$$

then $t_1 = t_2 = t_3 = t$

The accuracy of this method of detecting a flaw is determined by the maximum relative increase of pulses from the area of a flaw in relation to the number of pulses from areas without flaws. This relative increase is recorded by an integrator when the object with a flaw passes through the radiation beam.

This maximum relative increase is calculated from eqn 3, which for a time period $t < t_3$ but $t > t_2 > t_1$ becomes

$$
\begin{aligned}
{[\Delta N/N]}_{\text{max}} = \alpha\ \left(\mathrm{e}^{\mu X} - 1\right)\bigl[t_1 + t_2 - \tau \ln\\
\left(\mathrm{e}^{t_2/\tau} - \mathrm{e}^{t_1/\tau} - 1\right)\bigr]
\end{aligned}
\tag{4}
$$

In order to investigate the influence on the flaw detectability and therefore on the relative increase in pulses, the flaw size, shape and speed, the integrator time constant and the radiation beam size; the following tests were carried out on flaws shaped like cylindrical apertures and rectangular grooves. The apertures of constant depth, x, had axes parallel to the radiation beam and centres displaced along the diameter of the circular cross-section of the radiation beam.

Therefore after substituting the values $t_1 = 2r/v$ and $t_2 = 2R/v$ into eqn 4 the following equation is obtained

$$
\begin{aligned}
{[\Delta N/N]}_{\text{max}} = \left\{ r^2/R^2 + \left[ 1 + \frac{v\tau}{2R}\ \left( \mathrm{e}^{2R/v\tau} + \right. \right.\\
\left.\left.\mathrm{e}^{2R/v\tau} -1\right)\right] r/R\right\}\ \left(\mathrm{e}^{\mu X} - 1\right)
\end{aligned}
\tag{5}
$$

where r is the radius of the aperture, R is the radius of the circular cross-section of the radiation beam and v is the velocity of the flawed object. The grooves made in a plane perpendicular to the beam direction moved so that their longest sides were perpendicular to the direction of travel. In this case

$$
\begin{aligned}
{[\Delta N/N]}_{\text{max}} = \frac{f_a}{F}\left[ 1 + \frac{2R}{a} + \frac{v\tau}{a}\ \ln\left( \mathrm{e}^{(2R+a)v\tau} + \right. \right.\\
\left.\left.\frac{f_m}{f_a}\ \cdot\ \frac{a}{v\tau} + \mathrm{e}^{(f_m/f_a)(a/v\tau)} - 1\right)\right]\\
\left(\mathrm{e}^{\mu X} 1\right)
\end{aligned}
\tag{6}
$$

where $f_a$ is the cross-section of the flaw radiated by the beam field after time $t = a/v$, (after which the total width of groove was covered by the radiation beam). $f_m$ is the maximum cross-section of the flaw in the radiation beam, (ie after time $t = (2R + a)/2v$) and a is the groove width.

The change of $[\Delta N/N]_{\text{max}}$ in relation to the ratio 2R/vr, the coefficient of velocity, is shown in Fig 1.

![](./images/812415232151388161_1.jpg)

Fig 1 Change of $(\Delta N/N)_{\text{max}}$ in relation to the ratio $2R/V_\tau$

![](./images/812415232151388161_2.jpg)

Fig 2 Ratio of relative increase of pulses for a given coefficient of velocity to the increase in the number of pulses when the object is at rest

Each curve corresponds to an aperture with fixed ratio r/R, that is, the ratio of aperture diameter to the diameter of radiation beam field. In the case of grooves this ratio is called the 'coefficient of dimension'.

The 'coefficient of velocity' gives a measure of the velocity of the tested object, of integrator time constant and of radiation beam dimensions. The 'coefficient of dimension' gives the influence of flaw size and beam dimensions on the detectivity of flaws.

As can be seen from Fig 1, the influence of the coefficient of velocity on the relative increase of number of impulses, ceases when $2R/v\tau = 4$. It can also be seen, that the value for which the velocity coefficient does not effect the $(\Delta N/N)_{\text{max}}$ is lower when the coefficient of dimension, r/R or a/2R is small, ie either for flaws of small dimensions or when the coefficient of dimension becomes much greater than 1 (ie for flaws with larger dimensions than that of the radiation beam).

To find the influence of the coefficient of dimension on the value of the coefficient of velocity when it no longer has any influence on detectability, the ratios of the relative increase in the number of pulses at a given coefficient of velocity to the relative increase of pulses when the object is at rest and the maximum area of a flaw is irradiated was calculated. The values of these ratios in relation to the values of the coefficient of dimension are shown in Fig 2. Each

non-destructive testing April 1971 127

curve corresponds to one coefficient of velocity.
When the object is at rest, v = 0, and eqn 5 becomes
$$
\ln \left[\mathrm{e}^{2 \mathrm{R} / \mathrm{V} \tau}+\mathrm{e}^{2 \mathrm{r} / \mathrm{V} \tau}-1\right] \rightarrow 2 \mathrm{R} / \mathrm{v} \tau
$$

Similarly when $v \to 0$, eqn 6 becomes
$$
\begin{aligned}
& \ln \left[\mathrm{e}^{2 \mathrm{R}+\mathrm{a}) / \mathrm{V} \tau}-\frac{\mathrm{f}_{\mathrm{m}}}{\mathrm{f}_{\mathrm{n}}} \cdot \frac{\mathrm{a}}{\mathrm{v} \tau}+\right. \\
& \left.\mathrm{e}^{\left(\mathrm{f}_{\mathrm{m}} / \mathrm{f}_{\mathrm{a}}\right)(\mathrm{a} \mathrm{v} \tau)}-1\right]-\frac{(2 \mathrm{R}+\mathrm{a})}{\mathrm{v} \tau}
\end{aligned}
$$

In both cases
$$
[\Delta \mathrm{N} / \mathrm{N}]_{\max }=\mathrm{f}_{\mathrm{m}}\left(\mathrm{e}^{\mu \mathrm{x}}-1\right) / \mathrm{F}
$$

From these curves it can be seen that the influence of the coefficient of velocity at $2 \mathrm{R} / \mathrm{v} \tau=4$ causes the ratio of relative increase in impulses at a given v and v=0 to decrease by only $15 \%$. This is in the worst case, when the coefficient of dimension $\mathrm{r} / \mathrm{R}=$ $\mathrm{Q} / 2 \mathrm{R}=1$

The growth of the ratio of relative increases of pulses at v and v=0 at flaws with dimensions smaller than the beam dimensions, is the result of the growth of the ratio R/r. This does not mean that smaller flaws are easier to detect, for the relative increase of impulses decrease simultaneously. This increase may be so small that the flaw may not register on the integrator or it may be within the limits of error. The given curves have been verified experimentally.

## GEOMETRICAL FACTORS

The geometry of the system from source to flaw to probe should ensure the maximum utilization of radia- tion. The source surface is shaped like a cylinder and mounted in a collimator in such a way that its axis coincides with the axis of radiation. If the intensity of radiation is distributed evenly on the surface of the source, the area of the radiation beam with constant intensity over the flaw can be calculated. This area depends on the position of the flaws, the dimensions and shape of the collimators, and on the distance of

![](./images/812415232151388161_3.jpg)

Fig 3 Diagram showing variations in dimensions of the collimator

![](./images/812415232151388161_4.jpg)

Fig 4 Diagram showing testing of objects with vary- ing thicknesses

the source from the probe (Fig 3). The greatest allowable area of a beam with constant radiation intensity is equal to the area of the source collimator. To irradiate the whole thickness of the object under test a large collimator should be fixed to the probe. Unfortunately the coefficient of dimension r/R causes a decrease in $\Delta N / N$. By decreasing the collimator diameter on the probe considerably, we can assume that the half of the tested object thickness on the side of the source will receive a beam with maximum area and intensity

If we presume that all radiation from the source will reach the probe scintillator; the interdependence between the heights H and h of the cylindrical colli- mators of the source and the probe, and the thickness of the object under test, (Fig 4a) can be given by
$$
(\mathrm{h}+\mathrm{d}) / \mathrm{H}-(2 \mathrm{~h}+\mathrm{d}) /(2 \mathrm{H}+\mathrm{d}) \prec 1 \tag{7}
$$
where h is the probe collimator height, H is the source collimator heights, and a is the thickness of the tested object (Fig 4). Tapered collimators were used for convenience, so enabling the radiation inlet diameter to be even further decrease (Fig 4c). In this case the collimator dimensions can be calculated from the following equation
$$
\mathrm{d}(\mathrm{h}+\mathrm{d})+(4 / \mathrm{H}+\mathrm{h}+\mathrm{d})(1+\phi / \psi) \prec 1 \tag{8}
$$
where $\phi$ is the diameter of the source collimator and $\psi$ is the larger diameter of the probe collimator

## RADIOLOGICAL FACTORS

The gamma radiation travelling from the source to the scintillator is weakened by the material under test, and the scattering due to the collimators. Phenomenon causing the weakening of radiation such as absorption, scattering and creation of vapours take place in the scintillating crystal.

Investigations with spectrum $\mathrm{Cs}^{137}$ and $\mathrm{Co}^{60}$ were continued, varying the absorption thickness by means

128 nor.-destructive testing April 1971

of steel plates. With the increase of absorbent thickness the intensity of scattered radiation increases only slightly in comparison with the intensity of primary radiation (Fig 5).

An identical increase of scattered radiation was observed using collimators with tapered apertures (Fig 6) and a scintillating crystal with larger dimensions (Fig 7). With very large thicknesses of about 100 mm and with a scintillating crystal $2'' \times 2''$ it can be seen that the recorded growth of scattered radiation intensity is greater than when a smaller crystal $(1'' \times 1'')$ was applied. This is because the efficiency of gamma quanta counting increases with growth of crystal height The correct spectrum of high energy radiation $Co^{60}$ was obtained only in a scintillating crystal $2'' \times 2''$. The spectrum shows a large quantity

![](./images/812415232151388161_5.jpg)

Fig 5 Radiation spectrum showing slight increase in intensity of scattered radiation with increase of absorbent thickness (a) thickness 20mm, (b) thickness 40mm, (c) thickness 80mm.

![](./images/812415232151388161_6.jpg)

Fig 6 Radiation spectrum showing increase in scattered radiation, using collimators with tapered apertures. (a) thickness 20mm, (b) thickness 120mm, (c) thickness 140mm

non-destructive testing April 1971 129

of scattered radiation (Fig 8) at zero thickness and its variation. The peak corresponding to energy 1.16 MeV is lower than that corresponding to energy 1.33 MeV in spite of the fact that the quanta for both ener- gies give the same spectrum, equal only at steel thicknesses of 100 mm.

This proves that the scintillator output is smaller for high energy radiation.

The conclusion can be drawn that for the measure- ment of high energy gamma radiation a scintillating crystal of larger height should be used To establish the influence of absorbent thickness on the recorded number of impulses of secondary and primary radia- tion, diagrams of the change of measured number of pulses of secondary radiation and primary radiation $J$ were made. These are called 'the attenuation curves' and are given as examples in Fig 9, for sources $Cs^{137}$ of scintillator $1'' \times 1''$ with collimation on the source and cylindrical probe. The gradient of the curves decreases with the diminution of absorbent thickness

![](./images/812415232151388161_7.jpg)

Fig 7 Radiation spectrum similar to Fig 9, but using a scintillation counter with larger dimensions.
(a) thickness 60mm, (b) thickness 80mm, (c) thickness 120mm

![](./images/812415232151388161_8.jpg)

Fig 8 Spectrum showing variation of scattered radiation at zero thickness. (a) thickness 40mm, (b) thickness 80mm, (c) thickness 100mm

130 non-destructive testing April 1971

This is caused by the scintillation counter, which in a pulsing system of scintillator and photomultiplier at a high intensity of radiation is unable to transmit all the impulses to the integrator.

The gradient of the curves of secondary radiation also decreases with higher absorbent thicknesses This is caused by the increase of the number of pulses derived from scattered radiation when the gradient of primary radiation remains constant The change of differences of gradients of primary and secondary radiation curves with the growth of absor- bent thickness is illustrated by the ratio of the number of pulses of primary to secondary radiation (Fig 10). It can be seen from Fig 10 that at some thicknesses, the gradients are equal and their difference is zero. Above some absorbent thicknesses, the gradient of secondary radiation curve decreases. It is known that at a higher attenuation coefficient, $u$, which corres- ponds to the gradient mentioned, there is a relative increase of impulses caused by a flaw, so better detectability is obtained. Therefore, when materials of a greater thickness than that at which the difference of gradients of primary and secondary curves have been found, the discriminator of impulses should be applied. The range of thicknesses for which dis- crimination should be applied is affected also by the scintillator size (height and collimation) by radiation energy and the nature of the investigated material

![](./images/812415232151388161_9.jpg)

Fig 9 Attenuation curves showing the changes in primary and secondary radiation

![](./images/812415232151388161_10.jpg)

Fig 10 Curve showing the ratio of the number of pulses of primary to secondary radiation

## EXPERIMENTAL RESULTS FOR DETECTABILITY OF FLAWS

To check these theories, experiments to detect flaws were carried out The flaws were in the form of rectangular grooves of either determined but varying depth and constant width of 1mm or of a determined but varying width and constant depth of 3mm. The other imposed flaws were in the form of apertures of either constant diameter of 4 mm but of varying depth or of constant depth of 5mm but of varying diameter.

These flaws were made in steel plates to which were added additional steel plates without flaws, so that the

![](./images/812415232151388161_11.jpg)

Fig 11 Graph showing the change of volume of the smallest flaw or groove in relation to the thickness of the steel

non-destructive testing April 1971

final thickness of the investigated material was 40-200 mm. These plates were then moved across a radiation beam at a constant speed

Such investigations were carried out at 5 speeds, namely $20, 10, 5, 2.5$, and $1.25\ \text{mm sec}^{-1}$ (ie when applying the collimator with aperture of 5 mm diameter and with 0.5 sec integrator time constant, the speed criterion was equal to $0, 5, 1, 2, 4$ and $8$). In the experiments, sources of $\text{Cs}^{137}$ were used for primary radiation with the application of discrimination $8.8\text{V}$ and of $\text{Co}^{60}$ with discrimination $7.7\text{V}$. The measuring apparatus consisted of a probe, a stabilized high tension intensifier, a low tension intensifier, an analyser with a discriminator and an integrator, and an automatic recorder with 6 band speeds. The speed of the band travel was selected so that the ratio of band speed to the speed of the plates with flaws was always $1:4$.

![](./images/812415232151388161_12.jpg)

Fig 12 Graph showing the change of volume of the smallest flaws and holes in relation to the thickness of steel

From this, the curves of relative increase of number of impulses in relation to the depth of recorded flaws with the given investigation speed and thickness of steel plates were plotted. Then assuming a probability of 0.95 that the obtained deviations in the diagrams correspond to the flaws and not to the recording errors due to fluctuation of radioactive decay, the relative increase of impulses in areas without flaws and time constant 0.5 sec was calculated using the known interdependence. For the relative increase of impulses calculated, the depths and widths of the detected flaws were determined using the curves (obtained from eqns $5 \& 6$) of the coefficient of dimensions. The volumes of the smallest detected flaws at various thicknesses of steel and velocity coefficients were then calculated. These results were plotted on a graph for flaws and grooves (Fig 11) and flaws and holes (Fig 12), so that each curve represents the change of volume of the smallest flaw detected in relation to the thickness of the investigated steel at the given coefficient of velocity

The curves obtained with the source $\text{Cs}^{137}$ correspond to thicknesses of 40-120mm, while the curves obtained by the application of a source $\text{Co}^{60}$ correspond to steel of thicknesses from 120 to 200mm. The curves obtained from experimental data and from eqns $5 \& 6$ are nearly identical, thus verifying the calculation methods of radiometric investigations experimentally.