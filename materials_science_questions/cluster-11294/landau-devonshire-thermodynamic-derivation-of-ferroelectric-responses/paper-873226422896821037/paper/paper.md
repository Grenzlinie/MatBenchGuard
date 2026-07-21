# An Electroacoustic Lumped Element Model of a Dielectric Elastomer Membrane

C. Solano
Department of Mechanical Engineering, FAMU-FSU College of Engineering,
Tallahassee, FL 32310

Y. Zhang and L. N. Cattafesta III
Mechanical, Materials, and Aerospace Engineering Department, Illinois Institute of
Technology, Chicago, IL 60616

E-mail: cad12e@fsu.edu

**Abstract.** Dielectric elastomers are widely studied for their use in robotic and medical devices due to their shape changing properties. Recently, they have also been incorporated into acoustic devices, motivating the development of an electroacoustic model for dielectric elastomers. This paper provides a lumped element model based on a prestretched membrane approximation of a dielectric elastomer actuated by a dc voltage. The electroacoustic model is validated via experiments using a laser Doppler vibrometer and acoustic impedance tube measurements. Good agreement between the experiments and model are demonstrated. The resulting validated model is expected to be useful in design optimization for acoustic applications.

## 1. Introduction

Acoustic liners are a type of noise absorber commonly used in aircraft engines. Relatively simple acoustic liners are comprised of a perforate face sheet (FS) backed by honeycomb cells and terminated with a rigid backing. These single degree of freedom (SDOF) devices have an effective noise suppression bandwidth of approximately one octave [1]. Absorption can be increased at the expense of added size and weight to approximately two octaves by increasing the honeycomb depth and adding a second perforate layer, creating what is known as a two degree of freedom (2DOF) liner [1]. More complex liners have been formulated to further increase absorption bandwidth. For example, active liners have been created that can change their physical dimensions, such as modifying the cavity volume [2, 3, 4] or changing the facesheet hole area [5, 6]. These types of liners are able to change their characteristic resonance frequency. Another well known type of adaptive liner is the bias flow liner. In this design, flow enters from the back of the cavity and exits through the FS resulting in a wide tunable sound absorption

range as a function of the variable flow rate [7, 8]. However, active designs that require moving parts or bias flow can be heavy, complex, and require energy.

With the advancement of smart materials, researchers have devised creative ways to simplify adaptive liner technology while still obtaining broadband absorption. For example, changes in liner geometry have been performed through the use of shape memory materials. The cavity volume was varied using shape memory polymers in Hermiller et al. [9], with a resultant 500 - 600 Hz modification of the resonance frequency. Kreitzman et al. [10] and Dodge et al. [11] incorporated a shape memory alloy wire into a multilayered FS, changing the effective hole diameter of the FS and modifying the resonance frequency by 350 Hz. Liu et al. [12] replaced the rigid backing of a simplified acoustic liner (a Helmholtz resonator) with a piezoceramic diaphragm coupled to a passive electrical shunt network, allowing a tunable absorption range. Although compact and simple, a major disadvantage is that the piezoceramic disc is stiff relative to the cavity. This provides poor coupling, which limits the tunable range of the device. Their results motivated a softer active material that would better couple with the acoustics of the cavity. An example of a compliant material with modifiable properties is a dielectric elastomer (DE) - a smart material capable of changing shape when subjected to an electric field [13, 14, 15, 16]. This material has been incorporated into acoustic liners by Abbad et al. [17] and Dodge et al. [18]. Abbad et al. [17] replaced the rigid FS with a DE and was able to actuate the DE to modify the solid portion of the FS compliance. This shifted the resonance of the liner by 32 Hz and also achieved sound attenuation below 500 Hz. The work in Dodge et al. [18] split the cavity of an acoustic liner with a DE and saw a shift in the resonance frequency of approximtately 100 Hz, or 11%.

Researchers have incorporated the stress reduction of a DE into high fidelity finite element models to simulate the hyperelastic properties of dielectric elastomers [19, 20] when subjected to electric fields. Analytical models encompassing the complexities of hyperelastic material properties of DEs were developed using a Kelvin model [21] and Kelvin Voigt model [22] to capture its response to an electric field in terms of speed and relaxation [23, 24]. Others have developed a lumped parameter model for strip-shaped dielectric elastomer membrane transducers [23]. Further simplified models have incorporated variations of the stress expression, Eq. 27, into dynamical models to determine how the resonance frequency of a DE is affected by voltage [25]. These models are concerned with the mechanical response of the DE when subjected to a variable voltage loading and how its viscoelastic properties affect the corresponding time response in terms of speed and relaxation.

The current paper is specifically focused on developing an electroacoustic lumped element model (LEM) of a DE membrane subjected to a static voltage and time-harmonic, uniform pressure loading experienced in acoustic applications. In an effort to adjust the in-plane stress to tune the stiffness of the DE membrane, this paper develops an electroacoustic lumped element model for a uniformly biaxial tensioned DE membrane subject to constant voltage loading for acoustic applications. The resulting

model is experimentally validated and thus enables the design of a DE membrane in an acoustic liner application.

The paper is organized as follows. In Section 2, the LEM parameters and fundamental frequency of a DE membrane are derived based on its quasi-static response to a uniform pressure loading. The predicted response is a function of prestretch and applied pressure. Section 3 describes the fabrication procedure of the DE membrane sample as well as the experimental setup using an acoustic impedance tube and laser Doppler vibrometer. The stress dependence on voltage (Eq. 27) will then be substituted into the resonance expression and compared to experimental results in Section 4 to validate the DE membrane model. Finally, Section 5 will provide conclusions and future work on this topic.

## 2. Lumped Element Model

Dielectric elastomers are polymer films with a thickness and bending stiffness dependent on the material. Generally, a DE film can be thinner than 100 microns, especially if prestretched as is the case here. If the material is very thin and cannot support a bending moment, it can be modeled as a tensioned membrane. Therefore, the problem of interest is the 2-D damped wave equation with the configuration as illustrated in Figure 1.

![](./images/873226422896821037_1.jpg)

Figure 1: Schematic and coordinate system of a rectangular tensioned DE membrane.

The governing equation can be written as [26]
$$
c^{2} \nabla^{2} w-\frac{\partial^{2} w}{\partial t^{2}}-\frac{R}{\rho_{a}} \frac{\partial w}{\partial t}=\frac{q}{\rho_{a}}, \tag{1}
$$
where $c$ is the wave speed of the membrane given by $c^{2}=\sigma / \rho$, the stress $(\sigma)$ is given by Eq. 27, $\rho$ is the membrane density, $\rho_{a}=\rho h$ is the areal density, $w$ is the membrane displacement, $R$ is damping, and $q$ is the applied pressure. The initial stress in Eq. 27 can be expressed by the Yeoh model [27] as
$$
\sigma_{0}(\lambda)=2\left(\lambda^{2}-\frac{1}{\lambda^{4}}\right) \sum_{i=1}^{3} i C_{i 0}\left(I_{1}-3\right)^{i-1}, \tag{2}
$$

where the first strain invariant is
$$
I_{1}=2 \lambda^{2}+\frac{1}{\lambda^{4}},\qquad(3)
$$
and the constants $(C_{i 0})$ for Elastosil Film 2030, the material used here, are shown in
Table 1.

**Table 1: Elastosil Film 2030 material constants used in the Yeoh model [28].**

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Value [kPa]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$C_{10}$</td>
      <td>180.7</td>
    </tr>
    <tr>
      <td>$C_{20}$</td>
      <td>-16.7</td>
    </tr>
    <tr>
      <td>$C_{30}$</td>
      <td>6.6</td>
    </tr>
  </tbody>
</table>

The pinned boundary conditions are
$$
w(0, y, t)=w(a, y, t)=w(x, 0, t)=w(x, b, t)=0,\qquad(4)
$$
where $a$ and $b$ are the rectangular membrane side lengths as shown in Figure 1. Assuming
a uniform time-harmonic pressure loading, $q_{0} e^{j \Omega t} \ (j=\sqrt{-1})$, and using separation of
variables, the modal solution is of the form
$$
w(\hat{x}, \hat{y}, \hat{t})=\sum_{m=1}^{\infty} \sum_{n=1}^{\infty} \sin (m \pi k \hat{x}) \sin (n \pi \hat{y}) T_{m n}(\hat{t}),\qquad(5)
$$
where $\hat{x}=x / b$, $\hat{y}=y / b$, $\hat{t}=\omega_{11} t$, $k=b / a$ is the membrane aspect ratio (1 for a square
membrane), $q_{0}$ is a uniform pressure loading, and $T_{m n}$ is the time dependent solution.
$T_{m n}$ may be transformed into a dimensionless displacement given by
$$
\hat{T}=\frac{T_{m n} \sigma h}{q_{0} b^{2}}.\qquad(6)
$$

Substituting Eq. 5 into Eq. 1 and simplifying yields the dimensionless differential
equation
$$
\ddot{\hat{T}}+2 \zeta_{m n} \hat{\omega}_{m n} \dot{\hat{T}}+\hat{\omega}_{m n}^{2} \hat{T}=\hat{q}_{m n} e^{j \hat{\Omega} \hat{t}}, \quad m=n=1,3,5, \ldots\qquad(7)
$$

The damping ratio $(\zeta_{m n})$, normalized resonance frequency $(\hat{\omega}_{m n})$, and normalized
amplitude of the forcing function $(\hat{q}_{m n})$ are
$$
\zeta_{m n}=\zeta_{11} \frac{\sqrt{k^{2}+1}}{\sqrt{m^{2} k^{2}+n^{2}}},\qquad(8)
$$

$$
\hat{\omega}_{m n}=\frac{\omega_{m n}}{\omega_{11}}=\frac{\sqrt{m^{2} k^{2}+n^{2}}}{\sqrt{k^{2}+1}},\qquad(9)
$$
and
$$
\hat{q}_{m n}=\frac{16}{m n \pi^{4}\left[k^{2}+1\right]}.\qquad(10)
$$

Here, $\zeta_{11}$ is the damping ratio for the fundamental mode, $\omega_{m n}$ is the radian resonance
frequency that is dependent on mode $(m, n)$, $\omega_{11}$ is the fundamental resonance frequency,

and $\hat{\Omega} = \Omega/\omega_{11}$. The governing equation is an SDOF system such that the modal resonance frequencies are
$$
f_{mn} = \frac{\omega_{mn}}{2\pi} = \frac{c}{2b}\sqrt{(mk)^2 + n^2}. \tag{11}
$$

Since $c^2 = \sigma/\rho$, the fundamental resonance frequency, $m = n = 1$, for a square membrane $(k=1)$ is thus
$$
f_{11} = \frac{1}{b\sqrt{2}}\sqrt{\frac{\sigma}{\rho}} \approx \frac{0.707}{b}\sqrt{\frac{\sigma}{\rho}}. \tag{12}
$$

For a uniform pressure loading, $q_0$, the dimensionless static deflection is
$$
\hat{\delta}(\hat{x}, \hat{y}) = \frac{16}{\pi^4} \sum_{m=1}^{\infty} \sum_{n=1}^{\infty} \frac{\sin(m\pi k\hat{x})\sin(n\pi \hat{y})}{mn[(mk)^2 + n^2]}, \quad m = n = 1, 3, 5, \dots \tag{13}
$$
where $\hat{\delta} = \delta(\sigma h/q_0 b^2)$ is the dimensionless deflection.

### 2.1. Acoustic Impedance
The static displacement solution, Eq. 13, can be used to determine the acoustic impedance of the DE in terms of lumped parameters as described in Merhaut [29] and Beranek et al. [30]. The lumped acoustic compliance can be calculated by relating it to the ratio of volume displacement to the applied uniform pressure load with no applied voltage
$$
C_{aM} = \frac{\Delta \mathrm{Vol}}{q_0}, \tag{14}
$$
where the subscript $a$ refers to acoustic, $M$ refers to membrane, and the variable $\Delta \mathrm{Vol}$ is given by
$$
\Delta \mathrm{Vol} = \frac{q_0 b^4}{\sigma h} \int_0^1 \int_0^{1/k} \hat{\delta} d\hat{x}d\hat{y}. \tag{15}
$$

Substituting the volume displacement expression into Eq. 14, evaluating the summation for $\hat{\delta}$ (Eq. 13), and assuming a square membrane $(k=1)$ yields
$$
C_{aM} = \frac{0.0351b^4}{\sigma h}. \tag{16}
$$

The lumped acoustic mass can be found by equating the distributed kinetic energy to that of an acoustic mass, resulting in
$$
M_{aM} = \frac{\rho h b^2}{(\Delta V ol)^2} \int_0^1 \int_0^{1/k} \left( \frac{q_0 b^2}{\sigma h} \right)^2 \hat{\delta}^2 d\hat{x}d\hat{y}. \tag{17}
$$

Evaluating the integral and simplifying yields the acoustic lumped mass
$$
M_{aM} = \frac{1.3785\rho h}{b^2}. \tag{18}
$$

The lumped resistance for the fundamental frequency $(m,n)=(1,1)$ is given by
$$
R_{aM} = 2\zeta_{11}\sqrt{\frac{M_{aM}}{C_{aM}}}. \tag{19}
$$

The final acoustic impedance expression is given by
$$
Z_{a M}=s M_{a M}+\frac{1}{s C_{a M}}+R_{a M}, \tag{20}
$$
where $s=j \omega$ and $\omega$ is the radian frequency. Finally, the resonance frequency in the lumped approximation is given by
$$
f_{r e s}=\frac{1}{2 \pi \sqrt{M_{a m} C_{a M}}}=\frac{0.7235}{b} \sqrt{\frac{\sigma}{\rho}}, \tag{21}
$$
which differs from the exact value given in Eq. 12 by $2.3 \%$.

### 2.2. Acoustic Radiation Mass
The physical parameters derived thus far are for a membrane vibrating in a vacuum, while the sample is actually vibrating in air. The air surrounding the membrane exerts a pressure force on it that can be considered a complex radiation impedance, which reduces to an acoustic mass at low values of $\nu b$, where $\nu=\omega / c$ is the acoustic wavenumber. This mass must be included in Eq. 20. We make the standard assumption here that the radiation mass of a membrane is approximately the same as an infinite baffled piston. The normalized specific acoustic impedance of a rectangular piston at low values of $\nu b$ is given in Mellow et al. [31]. Using this approach, a lumped acoustic radiation mass is given by
$$
M_{a P}=0.946 b \frac{\rho}{2 S}, \tag{22}
$$
where $S=b^{2}$ is the area of the square membrane. Note that this is for the case of a square piston in an infinite baffle. However, the tested sample in the current study acts as a recessed square piston, where air in the recess is also moving in unison with the piston at low frequencies. The mechanical mass in the recess is $m_{r e c}=\rho S t_{r e c}$, where $t_{r e c}$ is the thickness of the recess. This can be converted to acoustic mass via division by $S^{2}$. Reorganizing to maintain the same form as Eq. 22 yields
$$
M_{a R e c}=\frac{t_{r e c}}{b / 2} b \frac{\rho}{2 S}. \tag{23}
$$

The total acoustic radiation mass is therefore
$$
M_{a R a d}=M_{a P}+M_{a R e c}=\left(0.946+\frac{t_{r e c}}{b / 2}\right) \frac{b \rho}{2 S}. \tag{24}
$$

Substituting the recess depth (6.86 mm) and the sample side length (see Table 2 in the following section) into the parenthesis simplifies the expression to
$$
M_{a R a d}=1.486 \frac{b \rho}{2 S}. \tag{25}
$$

### 2.3. Voltage Effect

The physical mechanism of an actuated DE is that of a material being squeezed when an electric field is applied across a thin tensioned membrane. This process is analogous to an applied pressure and results in an areal expansion when the material is unconstrained. This results in a reduction of the in-plane stress. An alternative approach is to constrain the DE at its peripheral boundaries as shown in Figure 2; this approach is adopted in this paper. The DE in its initial (reference) state is shown in Figure 2a. The DE can then be stretched in each direction by some desired prestretch $\lambda_i = l_i/L_i$, where $L$ and $l$ are the before and after stretch dimensions, respectively, and subscript $i$ is the direction index (Figure 2b). The DE is then pinned at its boundaries by a rigid frame as shown in Figure 2c. Finally, a thin, compliant electrode is applied on either side of the DE membrane (Figure 2d) and an electric field is applied across its thickness.

![](./images/873226422896821037_2.jpg)

Figure 2: Schematic of the prestretch and voltage actuation process for a DE membrane.
(a) In the reference state, the membrane is not stretched. (b) The membrane is prestretched in both directions resulting in an initial in-plane stress of $\sigma_0$. (c) A support frame is added. (c) Grease electrodes are added, and the membrane is subject to a voltage $V$ across its thickness.

The electrostatic pressure imposed on the DE is [13]

$$
P=\epsilon_{0} \epsilon_{r}\left(\frac{V}{h}\right)^{2},
\tag{26}
$$

where $\epsilon_0$ is the permittivity of free space, $\epsilon_r$ is the relative permittivity of the material, $V$ is the applied voltage across the membrane, and $h$ is the thickness of the membrane. Equation 26 represents the stress reduction of the initial prestretch imposed on the DE [32]. For the pinned configuration shown in Figure 2d, the in-plane stress reduction due to the application of an electric field for an incompressible material is [33]

$$
\sigma=\sigma_{0}-\epsilon_{0} \epsilon_{r}\left(\frac{\lambda^{2}}{h_{0}} V\right)^{2},
\tag{27}
$$

where $\sigma_0$ is the initial prestress, $\lambda = \lambda_1 = \lambda_2$ for biaxial prestretch, and $h_0$ is the initial thickness of the unstretched DE membrane.

The effect of voltage can be incorporated into the membrane impedance. Neglecting the mass of the electrodes, the applied voltage only modifies the membrane stress.

Hence, only the lumped compliance term needs to be updated. This is accomplished by noting that $h = h_0/\lambda^2$ and substituting Eq. 27 into the lumped compliance expression, Eq. 16,

$$
C_{a M}=\frac{0.0351 \ b^{4} \ \lambda^{2}/h_{0}}{\sigma_{0}-\epsilon_{r} \epsilon_{0}\left(\frac{\lambda^{2}}{h_{0}} V\right)^{2}}. \tag{28}
$$

The resonance frequency expression can be updated accordingly. The fundamental resonance frequency of the membrane in Eq. 21, can be rewritten as

$$
f=\frac{1}{2 \pi} \sqrt{\frac{1}{C_{a M}\left(M_{a M}+M_{a R a d}\right)}}. \tag{29}
$$

Substituting in Eq. 28 yields

$$
f=\frac{1}{2 \pi} \sqrt{\frac{\sigma_{0}-\epsilon_{r} \epsilon_{0}\left(\frac{\lambda^{2}}{h_{0}} V\right)^{2}}{0.0351 \ b^{4} \ \lambda^{2}/h_{0} \ (M_{a M}+M_{a R a d})}}, \tag{30}
$$

and normalizing by the unactuated ($V=0$) resonance expression yields

$$
\frac{f(V)}{f(V=0)}=\sqrt{\frac{\sigma_{0}-\epsilon_{r} \epsilon_{0}\left(\frac{\lambda^{2}}{h_{0}} V\right)^{2}}{\sigma_{0}}}. \tag{31}
$$

The relative permittivity $(\epsilon_{r})$ is a function of both material properties and prestretch. For the material used here, Elastosil Film 2030, the relative permittivity was given in Hodgins et al. [34] as a function of the prestretch

$$
\epsilon_{r}=-0.28 \lambda+2.76 \tag{32}
$$

This allows us to compare the resonance frequency variation of DE membranes as a function of both prestretch and voltage.

### 3. Experimental Setup
#### 3.1. Sample Preparation
The sample is a 25.4 mm square DE membrane. The material used is Elastosil Film 2030, which has an initial-unstretched thickness, $h_0$, of 100 microns. Before the DE is sandwiched between the two square frames, it is prestretched by the same factor, $\lambda$, in both directions. Figure 3 shows the steps: 1) the DE membrane is laid on a flat surface; 2) an $L\times L$ square is sketched onto the surface before 3) clamping the DE on its sides and stretching. The stretching is done in two parts: the edges along direction $x$ are stretched first followed by direction $y$ to minimize tearing. While stretching, the original marker lines drawn on the sample (the $L\times L$ square) are stretched as well. This results in thicker reference lines, which makes it difficult to accurately estimate the stretched dimensions. This can be seen in Figure 3 as the exaggerated difference in the thickness of the dashed lines. The maximum uncertainty of the prestretch is approximately $\pm 0.15$, caused by enlargement of the marker lines. Finally, when the

nominal desired stretch is reached, the electrode is applied if needed. The DE is then adhered to the rigid square frame using Very High Bond (VHB) tape.

Two types of samples are made, one with electrodes and one without. The type without electrodes has a dot(s) added to its surface using a thin silver sharpie to reflect light back to the laser vibrometer. The other sample is coated with a thin layer of carbon grease electrode. The coating is applied using a cotton swab and excess is removed with a soft spatula, resulting in a very thin layer. Carbon grease is commonly used by researchers [13, 19] and is readily available for purchase. Table 2 provides dimensions of the sample and density of both the membrane and electrodes. Note that the density of the DE membrane and carbon-grease electrode are very close. Finally, copper tape is used to connect the edge of the grease electrodes to the wires of a high voltage amplifier (Trek Model 10/40A).

![](./images/873226422896821037_3.jpg)

Figure 3: Steps for preparing a prestretched square DE membrane.

Table 2: Material properties and dimensions of DE membrane sample.

<table>
  <thead>
    <tr>
      <th></th>
      <th>Description</th>
      <th>Variable</th>
      <th>Value [unit]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">DE: Elastosil<br>Film 2030</td>
      <td>side length</td>
      <td>$a, b$</td>
      <td>25.4 [mm]</td>
    </tr>
    <tr>
      <td>thickness (prior to stretch)</td>
      <td>$h_0$</td>
      <td>100 [$\mu$m]</td>
    </tr>
    <tr>
      <td>density</td>
      <td>$\rho$</td>
      <td>1000 [kg/m$^3$]</td>
    </tr>
    <tr>
      <td>Electrodes</td>
      <td>density</td>
      <td>$\rho_E$</td>
      <td>1010 [kg/m$^3$]</td>
    </tr>
    <tr>
      <td rowspan="2">Frame</td>
      <td>side length</td>
      <td>$a, b$</td>
      <td>25.4 [mm]</td>
    </tr>
    <tr>
      <td>thickness</td>
      <td>$t_{rec}$</td>
      <td>6.86 [mm]</td>
    </tr>
  </tbody>
</table>

### 3.2. Acoustic Tube and Vibrometer Setup

A schematic of the experimental setup is shown in Figure 4 and depicts the Two Microphone Method (TMM) to determine the acoustic impedance of the sample [35]. The Brüel and Kjær (B&K) wide-spacing large circular impedance tube type 4206 with

![](./images/873226422896821037_4.jpg)

Figure 4: Sketch of the normal incidence tube setup with a vibrometer setup behind to measure DE vibrations.

a diameter of 100 mm is used. The length between the catenoidal horn exit and the test specimen is 875 mm. Microphone 1 is closest to the speaker and the second microphone is 100 mm away from the first microphone, which is 575 mm from the test specimen. The signal sent to the speaker is either a single-frequency sinusoid or psuedo-random periodic noise covering an octave band, where the SPL at the sample face is held constant for each frequency.

Normal velocity measurements of the sample are taken along the center line every 1.25 mm using a Polytec scanning laser vibrometer, type PSV 300. A laser Doppler vibrometer measures the frequency shift of a laser by the Doppler effect, which can be used to find the velocity at a point. The measurement is synced with the pseudo-random periodic noise signal sent to the speaker using a trigger signal. The standoff distance between the DE membrane sample and vibrometer is between 21.6 cm and 55.3 cm. The data is sampled at 16384 Hz and analyzed using a DFT with a frequency resolution of 1 Hz. Forty spectral averages are taken to compute the frequency response between the speaker excitation and the velocity response at multiple points.

## 4. Results and Discussion

The LEM prediction of the displacement response of the sample is compared to experimental measurements in the following section. The first step is to determine the prestretch applied to the sample. This is then substituted in the model of the static response (Eq. 13) and resonance frequency (Eq. 31) of the membrane, from which the effect of the excitation voltage can be determined.

### 4.1. Membrane prestretch

Although an approximate value of prestretch is known using the sketch drawn on the membrane surface, the actual prestretch falls within a range of values as explained in Section 3.1. The precise prestretch value is therefore estimated by minimizing the differences between the computed static displacement and resonance frequency, and the experimentally observed values. Both quantities are directly related to the in-plane stress (Eqs. 13 and 21, respectively), which is a function of prestretch via Eq. 2. An example computation of the displacement and resonance frequency is shown here.

The frequency response of the membrane center for an 80 dB pressure loading is plotted in Fig. 5. The static or dc response is estimated by measuring the center displacement at low frequencies where the response asymptotes to a constant. A zoomed view of the frequency response below 120 Hz where the response asymptotes is shown in Fig. 5. The mean of the response in this frequency range is approximately 51 nm with a standard deviation of 4 nm. Comparison to the static solution theory (Eq. 13) will be for a selected frequency in this range, 100 Hz for the analysis here. Figure 5 also shows three peaks in the response. The first peak, and the global maximum, is the fundamental frequency used for comparison to the LEM resonant frequency Eq. 29. The two smaller peaks are higher-order modes where the center response reaches a relative maximum.

![](./images/873226422896821037_5.jpg)

Figure 5: Measured displacement frequency response at the center of the membrane. Mean = 51 nm; standard deviation $\sigma = 4$ nm.

The center response is measured for two prestretches at 100 Hz for eight SPLs and is plotted in Fig. 6. Each of the eight responses is compared to the static displacement solution and the prestretch is estimated by setting Eq. 13 equal to the measured response, resulting in eight prestretch values. The average prestretch is computed

and shown in the second column of Table 3. For a visual prestretch of 1.1 and 1.3,
the approximate prestretch using the static displacement solution is 1.17 and 1.46,
respectively.

![](./images/873226422896821037_6.jpg)

Figure 6: Measured membrane displacement response at 100 Hz compared to the
theoretical static membrane response for two prestretch values.

Table 3: Prestretch estimated from visual inspection, static displacement, resonance
frequency, and the difference minimization considering both static displacement and
resonance frequency.

<table>
  <thead>
    <tr>
      <th>Visual</th>
      <th>Static Disp.</th>
      <th>Resonance</th>
      <th>Difference Min.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1.1</td>
      <td>1.17</td>
      <td>1.13</td>
      <td>1.15</td>
    </tr>
    <tr>
      <td>1.3</td>
      <td>1.46</td>
      <td>1.29</td>
      <td>1.38</td>
    </tr>
  </tbody>
</table>

The frequency response is also measured and the resonant frequency identified as
390 Hz and 530 Hz for a visual prestretch of 1.1 and 1.3, respectively. The frequency
value is accurate to $\pm$ 0.5 Hz for the 1 Hz frequency resolution of the measurement.
The prestretch is numerically determined by setting the measured resonance equal to
Eq. 29, noting the negligible difference between the natural and resonance frequency due
to very low damping. For the visual prestretches in Table 3, the approximate prestretch
corresponding to the measured resonance frequency is 1.13 and 1.29, respectively. These
values are lower than those from the static solution and closer to the visual prestretch
values.

To minimize the overall uncertainty, the prestretch is varied over a range of values
and the relative-difference in both the static deflection and the measured resonance
frequency is calculated. The total difference of the two is taken as the square root of the

sum of the squared differences and the local minimum is found. The results are listed in the last column of Table 3 and happen to be the averaged values between the two methods because the slope near the intercept is linear. The updated prestretch values are approximately 1.15 and 1.38 for the visual prestretches of 1.1 and 1.3, respectively. The updated prestretch values will be called "prestretch" for the remainder of the paper. The static displacement and resonant frequency predictions will now be updated with the prestretch values for comparison to the experimental results.

The experimentally measured center response at 100 Hz is plotted versus incident SPL together with the model (Eq. 13) in Fig. 6. The experimental values are plotted with random uncertainty estimates with a 95% confidence level calculated based on the procedures in Bendat et al. [36]. The model shape aligns with the measured response and falls within the estimated uncertainty, indicating an accurate prediction of the prestretch and static displacement amplitude. The membrane response remains linear, tracking the modeled response up to at least a 132 dB pressure loading, the maximum achievable SPL. Additionally, the resonant frequency is calculated based on the estimated prestretch value with the results shown in Table 4. The resonance is over predicted by a maximum of 9.4% for the cases tested, which is deemed reasonable for a lumped element model.

Table 4: Resonance frequency measured vs. calculated using the minimized composite difference value from column four of Table 3.

<table>
<thead>
<tr>
<th>Prestretch</th>
<th>Measured</th>
<th>Calculated</th>
<th>Difference</th>
</tr>
</thead>
<tbody>
<tr>
<td>1.15</td>
<td>390</td>
<td>417</td>
<td>6.9%</td>
</tr>
<tr>
<td>1.38</td>
<td>530</td>
<td>580</td>
<td>9.4%</td>
</tr>
</tbody>
</table>

### 4.2. Model Validation

The center line displacement of the DE membrane is measured for validation of the static mode shape. The laser vibrometer measures the response across the surface at a sinusoidal forcing of 100 Hz and an incident pressure of 80 dB. Figure 7 plots the normalized displacement response and the static model prediction given by Eq. 13. The experimental values are plotted with random uncertainty estimates with a 95% confidence level calculated based on the procedures in Bendat et al. [36]. Uncertainty in the $x$-axis values is determined via consideration of mapping the scanning points from the camera using the estimated control target locations. Considering the uncertainties in the measurements, the mode shape agrees well with the analytical model predictions. This validates the mode shape predicted by the model while the amplitude itself is validated in the previous section, as shown in Fig. 6.

![](./images/873226422896821037_7.jpg)

Figure 7: Normalized displacement of the measured membrane response at 100 Hz and
theoretical static membrane response for a prestretch of 1.38.

### 4.3. Membrane Actuation

#### 4.3.1. Added Mass due to Electrodes
To actuate the DE membrane, electrodes must
be added to its surface. This affects the membrane response since the membrane is very
thin (less than $100\ \mu\text{m}$ thick) and has approximately the same density as the electrodes
used. To understand how the electrode loads the membrane, the measured frequency
response of the membrane with and without the carbon grease electrodes is plotted
in Figure 8. It was assumed that the electrodes only modified the mass and not the
stiffness of the membrane. Starting with Eq. 29, we thus assume that $M_{aM}$ is affected.
The resonance frequencies of the membrane with and without electrodes can extracted
from Figure 8 as 444 Hz and 532 Hz, respectively, and are documented in Table 5.

Table 5: Resonance frequency measured in experiments and lumped parameter values.

<table>
  <thead>
    <tr>
      <th></th>
      <th>Description</th>
      <th>Variable</th>
      <th>Value [units]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">DE<br>Membrane</td>
      <td>Resonance w/o Electrodes</td>
      <td>$f$</td>
      <td>532 [Hz]</td>
    </tr>
    <tr>
      <td>Resonance w/ Electrodes</td>
      <td>$f_E$</td>
      <td>444 [Hz]</td>
    </tr>
    <tr>
      <td>Lumped acoustic mass</td>
      <td>$M_{aM}$</td>
      <td>109.0 [$\text{kg}/\text{m}^4$]</td>
    </tr>
    <tr>
      <td rowspan="2">Electrodes</td>
      <td>Added acoustic mass</td>
      <td>$M_{aE}$</td>
      <td>78.2 [$\text{kg}/\text{m}^4$]</td>
    </tr>
    <tr>
      <td>Thickness</td>
      <td>$h_E$</td>
      <td>25 [$\mu\text{m}$]</td>
    </tr>
  </tbody>
</table>

The resonance frequency expression (Eq. 29) can be updated to include the added
electrode mass, $M_{aE}$,

$$
f_{exp,E} = \frac{1}{2\pi} \sqrt{\frac{1}{C_{aM} \left(M_{aM} + M_{aRad} + M_{aE}\right)}}. \tag{33}
$$

![](./images/873226422896821037_8.jpg)

Figure 8: Measured response of the DE membrane with and without carbon grease electrode for a prestretch of 1.38.

The ratio of the added acoustic mass to that of the membrane as a function of the observed fractional change, $df/f$, in the resonance frequency can be expressed as
$$
\frac{M_{aE}}{M_{aM}+M_{aRad}}=\frac{1}{\left(1-\frac{df}{f}\right)^2}-1. \tag{34}
$$

The approximate value of the lumped mass due to the electrodes is $78.2\ \text{kg/m}^4$ using Eq. 34 and is shown in Table 5. As a check, the mechanical mass (in kg) from the electrodes can be estimated by multiplying the added mass by the area squared $(b^4)$ and dividing by the electrode density. The thickness of the electrode layer on either side of the DE membrane can then be estimated. Substituting the values from Tables 2 and 5, the thickness of the electrode layer is approximately $25\ \mu\text{m}$. This value is consistent with the thickness of the carbon-grease electrode estimated via visual inspection.

4.3.2. Actuation The normalized resonance frequency for both the experiment and the model (Eq. 31) versus voltage is shown in Figure 9. The resonant frequency is normalized by the no voltage case and so the value at zero voltage is unity. The resonance decreases quadratically with voltage, as expected based on Eq. 31. There is good agreement between experiments and theory for a majority of the range. The maximum difference for $\lambda=1.15$ and $\lambda=1.38$ is $2.3\%$ at $5\ \text{kV}$. This is the same difference as was found between the LEM resonance frequency (Eq. 21) vs. the exact resonance frequency (Eq. 12). This indicates that the membrane model of the DE is appropriate for the material used here.

![](./images/873226422896821037_9.jpg)

Figure 9: Normalized resonance frequency versus voltage for the experiment and model.

## 5. Conclusions
An LEM of a square dielectric elastomer membrane was derived. The damped wave equation in Cartesian coordinates was used to derive the static deflection of a square membrane. Using the relationship between pressure loading and volume displacement as a function of static deflection, the LEM was created. The effect of a dielectric elastomer was added to the model via an actuation term expressed as voltage. Voltage was incorporated into the stress term, which for the LEM affects the membrane's acoustic compliance (i.e., 1/stiffness). The resonant frequency expression was updated accordingly and reduces quadratically with voltage. Material properties and dimensions are parameters that may be chosen to achieve the desired impedance or resonant properties. Then the dimensions, prestretch, and voltage can be designed to achieve a desired impedance or resonance of the DE membrane.

A scanning laser vibrometer was used to validate the static response of the membrane. The membrane was subjected to various sound pressure levels and behaved linearly over the entire range tested. This validates the model up to 132 dB pressure loading, the maximum achievable pressure in the experimental setup. In order to actuate the DE membrane, electrodes were added to its surface. Therefore, the impedance was modified to include the effects of electrode mass. The model and experimental resonance frequency had good agreement with a maximum difference of 2.3% at 5 kV of applied voltage for the two prestretches tested. This validates the use of the membrane approximation for the DE used here.

With the validation of the model, a rectangular DE membrane may now be incorporated as a lumped element of a distributed electroacoustic system. This provides analytic scaling and rapid parametric studies for the initial phase of design. We

are interested in using the LEM to predict the impedance of acoustic liners with an active embedded membrane. Further development will incorporate an optimization scheme to maximize sound absorption or impedance tuning of the liner, combined with experimental demonstrations of the optimized design(s).

## References

[1] R. E. Motsinger and R. E. Kraft. *Aeroacoustics of Flight Vehicles: Theory and Practice, Volume 2: Noise Control*, chapter 14. Acoustical Society of America, New York, 2 edition, 1995.

[2] W. Neise and G.H. Koopmann. Reduction of centrifugal fan noise by use of resonators. *Journal of Sound and Vibration*, 73(2):297–308, November 1980.

[3] A. M. Mcdonald, S. M. Hutchins, I. Stothers, and P. J. Crowther. Method and apparatus for attenuating acoustic vibrations in a medium, November 19 1997. EP Patent App. 92,905,463 A.

[4] H. Matsuhisa, B. Ren, and S. Sato. Semiactive control of duct noise by a volume-variable resonator. *JSME international journal. Ser. 3, Vibration, control engineering, engineering for industry*, 35(2):223–228, 1992.

[5] R. Gaeta Jr. and K. Ahuja. A tunable acoustic liner. In *4th AIAA/CEAS Aeroacoustics Conference*. American Institute of Aeronautics and Astronautics, June 1998. AIAA Paper 1998-2298.

[6] K. Nagaya, Y. Hano, and A. Suda. Silencer consisting of two-stage helmholtz resonator with auto-tuning control. *The Journal of the Acoustical Society of America*, 110(1):289–295, July 2001.

[7] P. D. Dean and B. J. Tester. Duct wall impedance control as an advanced concept for acoustic impression. Technical report, November 1975. No. NASA-CR-134998.

[8] X. Jing and X. Sun. Experimental investigations of perforated liners with bias flow. *The Journal of the Acoustical Society of America*, 106(5):2436–2441, November 1999.

[9] J. M. Hermiller and M. R. Maddux. Morphing resonators for adaptive noise reduction. *The Journal of the Acoustical Society of America*, 134(5):3963, 2013.

[10] J. R. Kreitzman, F. Calkins, D. Nicholson, A. Lafranchi, L. Cattafesta, and C. Dodge. Active acoustic liners enabled by shape memory alloy technology. In *AIAA AVIATION 2020 FORUM*. American Institute of Aeronautics and Astronautics, June 2020. AIAA Paper 2020-2617.

[11] C. Dodge, B. M. Howerton, and M. G. Jones. An acoustic liner with a multilayered active facesheet. In *28th AIAA/CEAS Aeroacoustics 2022 Conference*. American Institute of Aeronautics and Astronautics, June 2022. AIAA Paper 2022-2902.

[12] F. Liu, S. Horowitz, T. Nishida, L. Cattafesta, and M. Sheplak. A multiple degree of freedom electromechanical helmholtz resonator. *The Journal of the Acoustical Society of America*, 122(1):291–301, July 2007.

[13] R. E. Pelrine, R. D. Kornbluh, and J. P. Joseph. Electrostriction of polymer dielectrics with compliant electrodes as a means of actuation. *Sensors and Actuators A: Physical*, 64(1):77–85, January 1998.

[14] R. Pelrine, R. Kornbluh, Q. Pei, and J. Joseph. High-speed electrically actuated elastomers with strain greater than 100%. *Science*, 287(5454):836–839, February 2000.

[15] R. Kornbluh, R. Pelrine, J. Eckerle, and J. Joseph. Electrostrictive polymer artificial muscle actuators. In *Proceedings. 1998 IEEE International Conference on Robotics and Automation (Cat. No.98CH36146)*. IEEE.

[16] R. D. Kornbluh, R. Pelrine, J. Joseph, R. Heydt, Q. Pei, and S. Chiba. High-field electrostriction of elastomeric polymer dielectrics for actuation. In Y. Bar-Cohen, editor, *SPIE Proceedings*. SPIE, May 1999.

[17] A. Abbad, K. Rabenorosoa, M. Ouisse, and N. Atalla. Adaptive helmholtz resonator based

on electroactive polymers: modeling, characterization, and control. *Smart Materials and Structures*, 27(10):105029, September 2018.

[18] C. Dodge, Y. Zhang, L. N. Cattafesta, B. M. Howerton, and J. R. Kreitzman. A dielectric elastomer acoustic liner. In *AIAA AVIATION 2021 FORUM*. American Institute of Aeronautics and Astronautics, July 2021. AIAA Paper 2021-2244.

[19] T. Wissler. *Modeling dielectric elastomer actuators*. PhD thesis, ETH Zurich, 2007.

[20] H. S. Park, Z. Suo, J. Zhou, and P. A. Klein. A dynamic finite element method for inhomogeneous deformation and electromechanical instability of dielectric elastomer transducers. *International Journal of Solids and Structures*, 49(15-16):2187-2194, August 2012.

[21] R. Sarban, B. Lassen, and M. Willatzen. Dynamic electromechanical modeling of dielectric elastomer actuators with metallic electrodes. *IEEE/ASME Transactions on Mechatronics*, 17(5):960-967, October 2012.

[22] T. Hoffstadt and J. Maas. Analytical modeling and optimization of DEAP-based multilayer stack- transducers. *Smart Materials and Structures*, 24(9):094001, August 2015.

[23] G. Rizzello, P. Loew, L. Agostini, M. Fontana, and S. Seelecke. A lumped parameter model for strip-shaped dielectric elastomer membrane transducers with arbitrary aspect ratio. *Smart Materials and Structures*, 29(11):115030, October 2020.

[24] J. Kiser, M. Manning, D. Adler, and K. Breuer. A reduced order model for dielectric elastomer actuators over a range of frequencies and prestrains. *Applied Physics Letters*, 109(13):133506, September 2016.

[25] P. Dubois, S. Rosset, M. Niklaus, M. Dadras, and H. Shea. Voltage control of the resonance frequency of dielectric electroactive polymer (DEAP) membranes. *Journal of Microelectromechanical Systems*, 17(5):1072-1081, October 2008.

[26] A. W. Leissa and M. S. Qatu. *Vibrations of Continuous Systems.*, chapter 5. McGraw-Hill, 2011.

[27] A. G. Holzapfel. *Nonlinear solid mechanics II*, chapter 6. John Wiley & Sons, Inc., 2000.

[28] T. Hoffstadt, A. Koellnberger, and J. Maas. Characterization of enhanced silicone materials for dielectric elastomer transducers. In *ACTUATOR 2018; 16th International Conference on New Actuators*, pages 1-4. VDE, 2018.

[29] Josef Merhaut. *Theory of electroacoustics*, chapter 2. McGraw-Hill College, 1981.

[30] L. L. Beranek and T. Mellow. *Acoustics: sound fields and transducers*, chapter 3. Academic Press, 2012.

[31] T. Mellow and L. Kärkkäinen. Expansions for the radiation impedance of a rectangular piston in an infinite baffle. *The Journal of the Acoustical Society of America*, 140(4):2867-2875, October 2016.

[32] Z. Suo. Theory of dielectric elastomers. *Acta Mechanica Solida Sinica*, 23(6):549-578, December 2010.

[33] T. Lu, J. Huang, C. Jordi, G. Kovacs, R. Huang, D. R. Clarke, and Z. Suo. Dielectric elastomer actuators under equal-biaxial forces, uniaxial forces, and uniaxial constraint of stiff fibers. *Soft Matter*, 8(22):6167, 2012.

[34] M. Hodgins and S. Seelecke. Systematic experimental study of pure shear type dielectric elastomer membranes with different electrode and film thicknesses. *Smart Materials and Structures*, 25(9):095001, August 2016.

[35] ASTM E1050-98. Standard test method for impedance and absorption of acoustic materials using a tube two microphones and a digital frequency analysis system, 1998.

[36] J. S. Bendat and A. G. Piersol. *Random data: analysis and measurement procedures*, chapter 8. John Wiley & Sons, 2011.

![](./images/873226422896821037_10.jpg)

![](./images/873226422896821037_11.jpg)

![](./images/873226422896821037_12.jpg)

![](./images/873226422896821037_13.jpg)

![](./images/873226422896821037_14.jpg)

![](./images/873226422896821037_15.jpg)

![](./images/873226422896821037_16.jpg)

![](./images/873226422896821037_17.jpg)

![](./images/873226422896821037_18.jpg)

![](./images/873226422896821037_19.jpg)

![](./images/873226422896821037_20.jpg)

![](./images/873226422896821037_21.jpg)

![](./images/873226422896821037_22.jpg)

![](./images/873226422896821037_23.jpg)

![](./images/873226422896821037_24.jpg)

![](./images/873226422896821037_25.jpg)