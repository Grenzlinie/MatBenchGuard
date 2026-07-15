![](./images/812530553172525057_1.jpg)
![](./images/812530553172525057_2.jpg)

Article

# Optimal Design of Annular Phased Array
Transducers for Material Nonlinearity Determination
in Pulse–Echo Ultrasonic Testing

Sungjong Cho $^{1}$ , Hyunjo Jeong $^{2,*}$ and Ik Keun Park $^{3}$

1 NDT Research Center, Seoul National University of Science and Technology, Seoul 01811, Korea;
cho-sungjong@seoultech.ac.kr
2 Department of Mechanical Engineering, Wonkwang University, Iksan 54538, Korea
3 Department of Mechanical and Automotive Engineering, Seoul National University of Science and
Technology, Seoul 01811, Korea; ikpark@seoultech.ac.kr
* Correspondence: hjjeong@wku.ac.kr; Tel.: +82-063-850-6690

Received: 3 November 2020; Accepted: 3 December 2020; Published: 6 December 2020

![](./images/812530553172525057_3.jpg)

**Abstract:** Nonlinear ultrasound has been proven to be a useful nondestructive testing tool for micro-damage inspection of materials and structures operating in harsh environment. When measuring the nonlinear second harmonic wave in a solid specimen in the pulse–echo (PE) testing mode, the stress-free boundary characteristics brings the received second harmonic component close to zero. Therefore, the PE method has never been employed to measure the so-called "nonlinear parameter $(\beta)$", which is used to quantify the degree of micro-damage. When there are stress-free boundaries, a focused beam is known to improve the PE reception of the second harmonic wave, so phased-array (PA) transducers can be used to generate the focused beam. For the practical application of PE nonlinear ultrasonic testing, however, it is necessary to develop a new type of PA transducer that is completely different from conventional ones. In this paper, we propose a new annular PA transducer capable of measuring $\beta$ with improved second harmonic reception in the PE mode. Basically, the annular PA transducer (APAT) consists of four external ring transmitters and an internal disk receiver at the center. The focused beam properties of the transducers are analyzed using a nonlinear sound beam model which incorporates the effects of beam diffraction, material attenuation, and boundary reflection. The optimal design of the APAT is performed in terms of the maximum second harmonic reception and the total correction close to one, and the results are presented in detail.

**Keywords:** phased array transducer; transducer optimization; beam focusing; pulse–echo mode; harmonic generation; stress-free boundary; total correction

---

## 1. Introduction

Power generation facilities in nuclear power and thermal power plants that are operated at high temperature and high pressure can lead to various types of micro-damage (e.g., deterioration, residual stress, fatigue, creep, and micro-cracks) as the number of years of use increases. The management of such damage is an essential part of ensuring the soundness and safe operation of power plants. In particular, a more reliable diagnosis technology is required for major components and parts made of nickel alloy or carbon steel welding because they are susceptible to micro-damage.

Currently, in nondestructive testing of power generation facilities, conventional radiography testing (RT) is being replaced by ultrasonic testing. Among the various ultrasonic methods, phased array ultrasonic testing is widely applied to the inspection of power generation facilities and pressure vessels [1–4]. However, it is not easy to detect various types of micro-damage described above with conventional linear ultrasonic testing techniques. Nonlinear ultrasonic technology uses nonlinear

Materials 2020, 13, 5565; doi:10.3390/ma13235565
www.mdpi.com/journal/materials

acoustic effects that occur when a strong ultrasonic wave is incident inside a material. The nonlinear ultrasound, such as the second harmonic wave, is known to be sensitive to micro-damage [5-10], and mainly measures the nonlinear parameter, $\beta$, which is defined by the displacement amplitudes of the fundamental and second harmonic waves to quantify the degree of damage. Studies on nonlinear ultrasonic applications are actively being conducted [11-20], and the use of longitudinal waves dominates in most cases, although surface and Lamb waves are also used. Damage types include fatigue, deterioration, creep, and irradiation, and most studies measure the uncorrected nonlinear parameter, $\beta'$, for ease and convenience of measurement.

Although nonlinear parameters are mainly measured in the through-transmission (TT) mode, pulse-echo (PE) measurements are frequently required for field applications. According to Bender et al. [21], the amplitude of the second harmonic received after reflection from the stress-free boundary of a sample in the PE mode is theoretically zero. This was the main reason the PE method has not been applied until recently. However, the zero reception of the second harmonic in the PE mode was the result of the pure plane wave. In the case of a real transducer of finite size, the second harmonic wave can be received owing to the diffraction effect, but it is extremely small and can only be measured when the specimen is thick enough [22,23]. Therefore, increasing the amplitude of the received second harmonic in applications of nonlinear PE method for thin samples is of utmost importance for obtaining the second harmonic signal with high signal-to-noise ratio and for accurate and reliable measurement of $\beta$.

It has been found that a focusing beam increases the amplitude of the received second harmonic in the PE testing of a sample with the stress-free boundary. Actually, the received second harmonic amplitude was found to significantly increase when a spherically focusing transducer was used in the water-air boundary [24,25]. The spherical focusing with a linear phased array ultrasonic transducer (PAUT) is not possible on the flat surface of a solid specimen. In addition, because the current PAUT for linear ultrasonic testing achieves beam focusing using dozens of channels and short pulses, it is still difficult to apply the nonlinear ultrasonic technique that employs a high-power toneburst type signal. It is also necessary to minimize the source nonlinearity, which is an important variable in nonlinear ultrasonic measurement. This is because when source nonlinearity occurs, it is mixed with the nonlinearity caused by damage, making it difficult to observe the damage-induced nonlinearity alone. Furthermore, the receive transducer should have a broad bandwidth capable of covering both fundamental and second harmonic wave frequencies. Therefore, for the development of PAUTs applicable to PE nonlinear testing, it is necessary to minimize the number of channels by designing a new type of PAUT that is completely different from the conventional PAUT. Before fabricating and applying such PAUT, a prototype design is required, and the focused beam properties should be fully understood. Further optimization of the PAUT is possible to achieve the maximum second harmonic reception and the uncorrected nonlinear parameter ($\beta'$) close to the absolute nonlinear parameter ($\beta$).

In this paper, we propose an annular phased array transducer (APAT) and model the nonlinear acoustic fields generated by the APAT in the PE setup to determine the optimal dimensions of the transducer. Basically, the APAT for PE nonlinear testing purposes consists of the four external ring transmitters and an internal disk receiver at the center. The fundamental and second harmonic wave fields, which are focused at various positions of the 1 cm thick specimen and then reflected from the stress-free boundary, are calculated and their characteristics are examined with the received average fields. For a given specimen thickness and frequency, the optimization of the APAT is then performed in terms of the maximum possible reception of the second harmonic and the total correction as close to one as possible. The optimization results are presented in detail. The shape of the time domain waveform formed at the focal position and at the receiver position are examined through finite element (FE) simulation.

Section 2 describes the requirements of the phased array transducer to be considered when performing the nonlinear parameter measurement in the pulse-echo mode using a focused beam and introduces the conceptual design of an APAT along with its focal characteristics in linear ultrasound.

In Section 3, we outline the nonlinear acoustic model developed in our previous work [26] and define the nonlinear parameter with necessary corrections. This model combines the effects of nonlinearity, diffraction, and boundary reflection in order to calculate the fundamental and second harmonic fields in the focused beam generated by the four annular transmit elements. Section 4 compares the focused beam properties of the two types of APAT—equal width (EW) and equal area (EA). We then present details on the optimization process of the EW type APAT and provide results on the received second harmonic amplitude and the relative nonlinear parameter. The FE simulation results are also presented in Section 4 to see how well the focused and/or received waveform matches the initially incident waveform. Conclusions are drawn in Section 5.

## 2. Phased Array Transducer Design

Ultrasonic phased array techniques are widely used in nondestructive testing areas and in many medical applications. Some of the attractive features of PAs include electronic focusing and steering capabilities. To generate a focused beam at any specified angle and distance, time delays are calculated and applied electronically to each element, as shown in Figure 1. In general, PA types are classified as linear or annular depending on the shape and arrangement of the elements, as shown in Figure 1.

![](./images/812530553172525057_4.jpg)

Figure 1. Schematic illustration of phased array beam focusing through time delay and two types of phased arrays.

To utilize the PA focusing technology to the measurement of nonlinear material properties, feasibility studies (e.g., senor materials and fabrication methods) and equipment availability must be preceded at the design stage of PAUT. Material nonlinearity measurements using the finite amplitude method require high power amplifiers, and the number of such amplifiers increases as the number of PA elements increases. Therefore, it is desirable to achieve beam focusing with minimum number of elements.

The generation of second harmonic waves in solids typically requires very high input voltages at the transmitter. Therefore, it is important to minimize the source nonlinearity caused by the transmit element. Most transmit transducers use single crystal $LiNbO_3$ instead of commercial transducers made of piezoelectric materials such as PZT for the purpose of harmonic generation with minimal source nonlinearity from the transmitter. The $LiNbO_3$ piezoelectric element shows a narrowband spectrum around its fundamental resonant frequency when no backing material is used. Thus, a transducer made of $LiNbO_3$ cannot receive both fundamental and second harmonic components at the same time. To solve this problem, the practical approach is to use a separate receive transducer of a broad bandwidth.

The next thing to consider is the calibration of the receiver. For a quantitative evaluation of the material damage, an absolute nonlinear parameter $(\beta)$, not the uncorrected nonlinear parameter $(\beta')$, needs to be measured. To measure $\beta$, the receive transducer must be calibrated [27–29]. To summarize the above, the PAUT for pulse–echo nonlinearity measurement requires a minimum number of transmit elements to generate a focused beam, separation of transmit and receive elements, and calibration of the receive element.

Taking these requirements into account, the arrangement of the transmit and receive elements for the conceptual design of linear and annular PAs is shown in Figure 2. Compared with conventional PAs, the central element is used only for reception, and the other elements are used for transmission, where the transmit and receive elements have the same central axis. This design allows the application of conventional receiver calibration method. In the conceptual design and wave field simulation with a beam focusing, the number of transmit elements is limited to four. Because the central element is used for reception, the beam focusing behavior is analyzed along the central axis. The beam focusing simulation in this section was conducted using the CIVA program [30-32], a nondestructive simulation platform. In the CIVA simulation, aluminum was selected as the propagation medium, and the following acoustic properties including the nonlinear parameter were used [28]: longitudinal wave velocity, $c = 6422$ m/s; density, $\rho = 2700$ kg/m³; fundamental wave frequency, $f = 5$ MHz; and nonlinear parameter, $\beta = 5.5$. The specifications of the PAUTs used in the simulation are summarized in Table 1. The specifications of the annular phased array were imported from the optimal design of the equal width (EW) type annular phased array described in Section 4. The diameter of the receive element is 3.2 mm, and the diameter of the innermost transmit element is 10 mm. Specifications of the EW phase array can be found in Table 2. The dimensions of the linear PA along the width direction are the same as the cross-sectional dimensions of the annular PA, and the length of the linear PA was taken arbitrarily as 10 mm. In Section 4, the effect of the sizes of the transmit elements (i.e., equal width type and equal area type) on the received amplitude of the fundamental wave and the second harmonic was compared.

![](./images/812530553172525057_5.jpg)

Figure 2. Configuration of linear and annular phase arrays.

Table 1. Specifications of linear and annular phased arrays used in the simulation.

<table>
<thead>
  <tr>
    <th>Array Pattern</th>
    <th>Linear</th>
    <th>Annular</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Number of elements</td>
    <td>8</td>
    <td>4</td>
  </tr>
  <tr>
    <td>Gap between elements</td>
    <td>0.5 mm</td>
    <td>0.5 mm</td>
  </tr>
  <tr>
    <td>Element width</td>
    <td>1 mm</td>
    <td>1 mm</td>
  </tr>
  <tr>
    <td>Element length</td>
    <td>10 mm</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Total array width</td>
    <td>21 mm</td>
    <td>21 mm</td>
  </tr>
</tbody>
</table>

Beam focusing simulation results of the linear and annular phased arrays are shown in Figure 3. The simulations were performed in the linear ultrasound range. In the case of the linear PA, the focusing is hardly found, whereas, in the case of the annular PA, a distinct focusing can be seen at three focal lengths. This is due to the geometry of the annular PA, which is much more efficient in forming the focused beam. If we look at the results of the annular PA in more detail, the simulated focal spot sizes at −6 dB along the cross-axis of the beam are about 1 mm for all three focal lengths. If we treat the annular PA as a single transmit element of diameter $D$, the measured spot size is slightly larger than the estimated focal spot size using the equation $d = \lambda L/D$ where $\lambda$ is the wavelength, $L$ is the focal length, and $D$ is the total width of the array. On the other hand, the focal spot size along the on-axis of the beam increases with increasing focal length, and this is clearly seen in the simulation results of Figure 3. Increased focal spot size also means decrease of peak amplitude. The difficulty in creating

well-shaped focal zones in the annular PA can be attributed to the hollow structure and a small number of elements [33–35]. The current annular PA structure with four transmit elements is hollow in the center, but the overall beam focusing behavior is similar to that observed in the conventional linear PAs with dozens of elements. In particular, since it has a good focusing performance at the focal length of 10 mm, it can be used for pulse–echo nonlinear measurement of relatively thin specimens with a thickness of about 10 mm.

Table 2. Dimensions of two types of annular phased arrays (unit: mm).

![](./images/812530553172525057_6.jpg)

<table>
<thead>
<tr>
<th colspan="2">EW</th>
<th colspan="2">EA</th>
</tr>
<tr>
<th>Radius</th>
<th>Radius</th>
<th>Radius</th>
<th>Radius</th>
</tr>
</thead>
<tbody>
<tr>
<td>$r_{1in}$</td>
<td>5</td>
<td>$r_{1in}$</td>
<td>5</td>
<td>$r_{1out}$</td>
<td>6</td>
</tr>
<tr>
<td>$r_{2in}$</td>
<td>6.5</td>
<td>$r_{2out}$</td>
<td>7.5</td>
<td>$r_{2in}$</td>
<td>6.5</td>
<td>$r_{2out}$</td>
<td>7.3</td>
</tr>
<tr>
<td>$r_{3in}$</td>
<td>8</td>
<td>$r_{3out}$</td>
<td>9</td>
<td>$r_{3in}$</td>
<td>7.8</td>
<td>$r_{3out}$</td>
<td>8.5</td>
</tr>
<tr>
<td>$r_{4in}$</td>
<td>9.5</td>
<td>$r_{4out}$</td>
<td>10.5</td>
<td>$r_{4in}$</td>
<td>9</td>
<td>$r_{4out}$</td>
<td>9.6</td>
</tr>
</tbody>
</table>

![](./images/812530553172525057_7.jpg)

Figure 3. Beam focusing simulation results of the linear and annular phased arrays.

## 3. Annular PA Wave Fields and Definition of $\beta$

### 3.1. Theory

Second harmonic generation in the nonlinear PE testing with the stress-free boundary condition is schematically illustrated in Figure 4. The APAT consisting of four ring transmitters and a central disk receiver are also included. In Figure 4, $p_{1,i}$ is the acoustic pressure of the fundamental wave emitted from the ring transmitters, and $p_{2,i}$ is the generated second harmonic wave owing to the forcing of $p_{1,i}$. $p_{1,r}$ denotes the reflected fundamental wave when the wave $p_{1,i}$ hits the boundary, $p_{2,r1}$ is the reflected wave when the wave $p_{2,i}$ hits the boundary, and $p_{2,r2}$ is the second harmonic wave generated by the reflected $p_{1,r}$. Therefore, the total reflected second harmonic, $p_{2,r}$, can be obtained by adding $p_{2,r1}$ and $p_{2,r2}$. Both the reflected fundamental and second-harmonic waves are received by the center receiver.

![](./images/812530553172525057_8.jpg)

Figure 4. Schematic illustration of second harmonic generation process in a nonlinear PE testing with the stress-free boundary.

### 3.2. Sound Beam Solution

The second harmonic wave is produced due to material nonlinearity when the finite amplitude fundamental wave radiates from the transmitter and propagates in the solid. The related acoustic fields for a single element circular transducer have been derived previously [26,36,37]. In this section, we briefly present the mathematical equations to calculate the received acoustic fields when a phased array transducer composed of four ring elements radiates a finite amplitude longitudinal wave. The incident fundamental wave $p_{1,i}$ and the generated second harmonic $p_{2,i}$ are given by Equations (1) and (2). Pressure $p$ is used here as a field variable.

$$
p_{1,i}(x_{1}, y_{1}, z_{1})=-2ik\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}p_{1}(x', y', 0)G_{1}(x, y, z|x', y', 0)dx'dy'
\tag{1}
$$

$$
p_{2,i}(x_{1}, y_{1}, z_{1})=\frac{2\beta k^{2}}{\rho c^{2}}\int_{0}^{z}\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}p_{1}^{2}(x', y', z')G_{2}(x, y, z|x', y', z')dx'dy'dz'
\tag{2}
$$

where the Green's function is given by the following equation:

$$
G_{1}(x, y, z|x', y', 0)=\frac{1}{4\pi r}exp(ikr)
\tag{3}
$$

$$
G_{2}(x, y, z|x', y', z')=\frac{1}{4\pi R}exp(i2kR)
\tag{4}
$$

Here, $r = \sqrt{(x-x')^{2}+(y-y')^{2}+z^{2}}$ and $R = \sqrt{(x-x')^{2}+(y-y')^{2}+(z-z')^{2}}$. For $p_{1}$,
the source function is $p_{1}(x',y',z'=0)$, and the integration is applied over the transducer surface
element $ds' = dx'dy'$ at the source plane $z' = 0$,

$$
p_{1}(x',y',z'=0)=p_{0},\ a^{2}\leq x'^{2}+y'^{2}\leq b^{2} \tag{5}
$$

where $p_{0}$ is the uniform acoustic pressure and $a$ and $b$ are the inner and outer radii of the ring
transmitter. $p_{1,i}$ and $p_{1,r}$ of the $m$th transmission element can be obtained by calculating $p_{1,i}^{(m)}$ and $p_{1,r}^{(m)}$
under different boundary conditions of Equation (5), and the total fields are found by adding them
together. The reflected fundamental pressure $p_{1,r}$ is given by

$$
p_{1,r}(x,y,z)=R_{1}p_{1i}(x,y,z) \tag{6}
$$

The total pressure of the reflected second harmonic $p_{2,r}$ is obtained as the sum of $p_{2,r1}$ and $p_{2,r2}$
given by

$$
p_{2,r1}(x,y,z)=-2ik\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}R_{2}p_{2,i}(x',y',z_{0})G_{2}(x,y,z|x'y',z_{0})dx'dy' \tag{7}
$$

$$
p_{2,r2}(x,y,z)=\frac{2\beta k^{2}}{\rho c^{2}}\int_{z_{0}}^{z}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}\left\{p_{1,r}(x',y',z')\right\}^{2}G_{2}(x,y,z|x',y',z')dx'dy'dz' \tag{8}
$$

In Equations (6) and (7), $R_{1}$ and $R_{2}$ are the reflection coefficients for the fundamental and second
harmonic waves at the solid-air interface and are given by $R_{1}=R_{2}=-1$. The reflected second
harmonic fields for $m$th element can be obtained by calculating $p_{2,r1}^{(m)}$ and $p_{2,r2}^{(m)}$, and the total fields are
found by adding contributions from all elements.

Next, to calculate the received pressure at a distance $z$ by the receiver of area $S_{R}$, the concept of
the average pressure can be defined and calculated as follows:

$$
\widetilde{p}_{n}(z)=\frac{1}{S_{R}}\int_{S_{R}}p_{n}(x,y,z)dS_{R}\quad\quad n=1,2 \tag{9}
$$

### 3.3. Time Delay

Consider an array of $N$ elements radiating into a solid to produce a sound beam with a focal
length $F$, as shown in Figure 5. The focusing time delays can be calculated as follows [38]:

$$
\Delta t_{N}=\frac{\sqrt{\left(\frac{r_{2N}+r_{2N-1}}{2}\right)^{2}+F^{2}}-F}{c}=\frac{\sqrt{r_{N}^{2}+F^{2}}-F}{c} \tag{10}
$$

where $\Delta t_{N}$ is the required time delay for element $N = 0,1,\ldots,N$. Note that in Equation (10) each
calculated time has a positive value, which is a time delay. The delay of the time-domain signal is
equivalent to multiplying the frequency domain signal by a phase term that is linear in frequency
and proportional to its delay. If $F(\omega)$ is the Fourier transform of the time domain signal $f(t)$, then the
Fourier transform of the time-shifted signal $f(t-\Delta t_{N})$ can be obtained as $\exp(i\omega\Delta t_{\mathrm{N}})F(\omega)$, where $\Delta t_{N}$
is the delay time.

![](./images/812530553172525057_9.jpg)

Figure 5. Geometrical parameters for calculating the focusing time delay of phased array.

### 3.4. Definition of $\beta$ with Total Correction

Equation (9) can be expressed more conveniently in terms of the plane wave solutions modified by the correction terms owing to the effects of attenuation, diffraction, and boundary reflection, i.e.,

$$
\widetilde{p}_{1, r}=\left[p_{1}^{\text {plane }}(z)\right]\left[C_{T 1}\right]
\tag{11}
$$

$$
\widetilde{p}_{2, r}=\left[p_{2}^{\text {plane }}(z)\right]\left[C_{T 2}\right]
\tag{12}
$$

Here, $p_{1}^{\text {plane }}=p_{0} \exp (i k z)$ and $p_{2}^{\text {plane }}=\frac{\beta k p_{0}^{2} z}{2 \rho c^{2}} \exp (2 i k z)$ where $k$ is the wave number, $\rho$ is the density, and $c$ is the wave velocity. In addition, the average pressure is calculated at the initial source position, i.e., at the total propagation distance $z=2 z_{0}$. In Equations (11) and (12), $C_{T n}$ is the correction due to attenuation, diffraction, and boundary reflection in the fundamental ($n=1$) and second harmonic ($n=2$) waves and is defined as follows:

$$
C_{T 1}=R_{1} M_{1} \widetilde{D}_{1}
\tag{13}
$$

$$
C_{T 2}=\left[R_{2} M_{21} \widetilde{D}_{21}+R_{1}^{2} M_{22} \widetilde{D}_{22}\right]
\tag{14}
$$

where $M_{1}, M_{21}$, and $M_{22}$ and $\widetilde{D}_{1}, \widetilde{D}_{21}$, and $\widetilde{D}_{22}$ are the attenuation corrections and diffraction corrections in $\widetilde{p}_{1, r}, \widetilde{p}_{2, r 1}$, and $\widetilde{p}_{2, r 2}$. The detailed expressions for these corrections can be found elsewhere [26]. If we put $\frac{C_{T 1}^{2}}{C_{T 2}}=C_{T}$, where $C_{T}$ is called the "total correction", combining Equations (11) and (12) yields the nonlinear parameter $\beta_{f}$ in fluids

$$
\beta_{f}=\frac{2 \rho c^{2}}{k z} \frac{\widetilde{p}_{2, r}}{\widetilde{p}_{1, r}^{2}} C_{T}=\beta_{f}^{\prime} C_{T}
\tag{15}
$$

The nonlinear parameter $\beta_{s}$ in solids can be obtained by replacing $\beta_{f}$ with $\frac{1}{2} \beta_{s}$ in Equation (15). Then, using the relationship between pressure and displacement, $\beta_{s}$ can be determined in terms of the received average displacement by

$$
\beta_{s}=\beta=\frac{8}{k^{2} z} \frac{\widetilde{u}_{2, r}}{\widetilde{u}_{1, r}^{2}} C_{T}=\beta^{\prime} C_{T}
\tag{16}
$$

Since the amplitude of the actually measured wave deviates from the plane wave, $C_{T}$ appearing in Equation (16) is to correct the attenuation, diffraction, and boundary reflection effects in the received amplitudes of the fundamental and second harmonic waves. Hence, $\beta^{\prime}$ is called the "uncorrected" nonlinear parameter.

## 4. Optimization of Phase Array Dimensions

The received second harmonic wave, $\widetilde{u}_{2, r}$, in the pulse-echo testing is in general much smaller than the through-transmission method, consequently the uncorrected nonlinear parameter, $\beta^{\prime}$, becomes also very small. To recover the correct nonlinear parameter, $\beta$, a large value of the total correction,

$C_T$, should be multiplied. For accurate and reliable determination of $\beta$, especially for thin specimens, it is necessary to maximize $\widetilde{u}_{2,r}$ and reduce the dependence on $C_T$ by optimizing the design of APAT. These two parameters depend on many variables including sample thickness, frequency, and shape and size of the transmit and receive elements. Here, the thickness of the specimen is fixed, so it is not a design variable for optimization. It is also assumed that the frequency is fixed. Then, the optimization of APAT can be considered a process of determining the size, arrangement, and shape of the transmit and receive elements. The optimization of APATs can be approached in terms of two objective functions: the second harmonic reception and the total correction. The optimized transducer should provide the largest possible second harmonic reception and the total correction value as close to one as possible.

In the simulation-based optimization here, the received amplitudes of the fundamental and second harmonics and the total correction were calculated through wave field analysis for various combinations of shape and size of the transmit and receive elements. Then, the optimized APAT is finally obtained by comparing the received second harmonic amplitude and the total correction value from various simulation cases.

As a final step, the waveform of the received signal was obtained through finite element analysis (FEA). The purpose of FEA is to check the distortion of waveforms received through focusing, and to validate the analytical model used for wave field calculation and optimization of annular phased arrays.

### 4.1. Focused Beam Field Analysis Results

APATs can be divided into two types: equal width (EW) and equal area (EA). The wave fields for these two types are analyzed and the focusing properties are compared. The source displacement used in the analysis is $u_0 = 10^{-9}$ m, and the fundamental frequency is $f_1 = 5$ MHz. The attenuation effect is not considered. For the EW type, the element width is 1 mm and the kerf is 0.5 mm. For the EA type, the area of the innermost element is the same as the first element of the EW type, and the size of the remaining elements is determined from the area of the first element. The kerf is 0.5 mm. The number of elements in both types is four. The focal length ($F$) is set to 10 mm. The central receiver has a fixed diameter of 3.2 mm. The target thickness of the specimen is assumed to be 10 mm. The dimensions used in the wave field analysis are given in Table 2.

Simulation results and comparisons between the EW and EA types of APAT for fundamental and second harmonic waves are shown in Figure 6. More specifically, the 2D beam profile and the on-axis variation of displacement are presented. When considering only the beam profile, there seems to be no difference in beam focusing between the two types. However, comparison of on-axis profiles shows a noticeable difference between the two types. The maximum amplitude of the EW type is slightly larger than that of the EA type at $F = 10$ mm in both wave types. The EA type is found to focus at a distance slightly shorter than $F = 10$ mm in the fundamental wave. Based on this, it can be said that the EW type has better focusing performance than the EA type. Therefore, optimization is performed using the EW type.

The focusing behavior of the fundamental wave along the lateral and axial directions is shown in Figure 3. Similar behavior is also observed here, as shown in Figure 6a,c.

Compared to the fundamental wave, the second harmonic wave shows a narrower beamwidth at the focal length due to the twice as large frequency, as shown in Figure 6b,d. As a result, the second harmonic wave forms a sharp focus at the specified focal length. In fact, the amplitude of the received wave is determined by a receiver of finite size. Thus, in the case of a focused beam, it is important to determine the size of the receiver according to the focal spot size in the lateral direction of the beam in order to receive maximum amplitude. In Figure 6b,d, the focal spot sizes at −6 dB along the lateral direction are estimated to be less than 1 mm, which can be treated as a point focus. Therefore, for maximum reception of the second harmonic amplitude, a point reception device such as a laser interferometer may be the best choice, but, considering the actual situation, a broadband ultrasonic receiver made of the smallest possible size piezoelectric element may be more suitable.

![](./images/812530553172525057_10.jpg)

Figure 6. Simulation results and comparisons between the EW and EA types of APAT for fundamental and second harmonic waves: (a) fundamental, EW; (b) second harmonic, EW; (c) fundamental, EA; (d) second harmonic, EA; (e) on-axis, fundamental wave; and (f) on-axis, second harmonic.

### 4.2. Optimization for Second Harmonic Generation and Total Correction

In the EW type APAT, the focal length and element width affect the received amplitude of the second harmonic and the total correction. Here, the effect of these two parameters is examined. The focal position is set at three distances, namely 10, 15, and 20 mm, corresponding to the reflection boundary of the 10 mm thick specimen, the center of the specimen equal to 1.5 times the specimen thickness, and twice the specimen thickness equal to the receiver position. The width of the element is set to 1, 1.5, 2, and 2.5 mm. Twelve simulation cases are listed in Table 3. According to the simulation results in Section 4.1, among commercially available broadband transducers, a receiver with a minimum diameter of 3.2 mm is used.

Table 3. Simulation cases for various combinations of focal length and element width.

<table>
  <thead>
    <tr>
      <th>Group</th>
      <th>Case Number</th>
      <th>Focal Length (mm)</th>
      <th>Element Width</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">A</td>
      <td>1</td>
      <td rowspan="4">10</td>
      <td>1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <td>4</td>
      <td>2.5</td>
    </tr>
    <tr>
      <td rowspan="4">B</td>
      <td>5</td>
      <td rowspan="4">15</td>
      <td>1</td>
    </tr>
    <tr>
      <td>6</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td>7</td>
      <td>2</td>
    </tr>
    <tr>
      <td>8</td>
      <td>2.5</td>
    </tr>
    <tr>
      <td rowspan="4">C</td>
      <td>9</td>
      <td rowspan="4">20</td>
      <td>1</td>
    </tr>
    <tr>
      <td>10</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td>11</td>
      <td>2</td>
    </tr>
    <tr>
      <td>12</td>
      <td>2.5</td>
    </tr>
  </tbody>
</table>

Using various combinations of focal length and element width, the received fundamental and second harmonic amplitudes were calculated. The simulation results for 12 cases are shown in Figure 7. It also includes the results of the through-transmission (TT) mode calculations when a transmitter and a receiver both 12.7 mm in diameter are used. The propagation distance for the single element TT mode is 10 mm, which is the thickness of the specimen. The received amplitude is largest in Case C-1 for both the fundamental and the second harmonic waves. This result shows that the optimal design of APAT with the beam focusing can produce a received second harmonic amplitude that is about 50% larger than the single element TT case.

![](./images/812530553172525057_11.jpg)

Figure 7. The received displacements calculated using the simulation parameters in Table 3:
(a) fundamental wave; and (b) second harmonic wave.

The uncorrected $\beta'$ was calculated using the received amplitude data in Figure 7, and the results are shown in Figure 8. Since the nonlinear parameter is given by $\beta = [\beta'][C_T]$, the total correction $C_T$ should be as close to one as possible in the optimization process. This means that the uncorrected $\beta'$ should be as close to $\beta$ as possible. It can be seen that $\beta' = 1.56$ in Case C-1, where the received second harmonic amplitude is the largest, and $\beta' = 2.53$ in Case B-1. Therefore, the optimal case for $\beta'$ or $C_T$ is Case A-1 giving $\beta' = 6.55$, which is about 19% larger than $\beta = 5.5$. These results show that the APAT specifications optimized for one objective function may not satisfy the other objective function.

![](./images/812530553172525057_12.jpg)

Figure 8. The calculated $\beta'$ using the data in Figure 7.

Next, the influence of kerf was analyzed by changing the kerf size to 0.1, 0.3, and 0.5 mm in the EW type APAT. When designing an APAT, the interelement spacing (kerf) should be less than half the wavelength to suppress the occurrence of grating lobes. All three kerf sizes selected here meet this condition. Three different focal lengths were used as before. Various combinations of focal length and kerf size are shown in Table 4.

Table 4. Simulation cases for various combinations of focal length and kerf size.

<table>
<thead>
  <tr>
    <th>Case Numbers</th>
    <th>Focal Length (mm)</th>
    <th>Kerf (mm)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>A11</td>
    <td rowspan="3">10</td>
    <td>0.1</td>
  </tr>
  <tr>
    <td>A12</td>
    <td>0.3</td>
  </tr>
  <tr>
    <td>A13</td>
    <td>0.5</td>
  </tr>
  <tr>
    <td>B11</td>
    <td rowspan="3">15</td>
    <td>0.1</td>
  </tr>
  <tr>
    <td>B12</td>
    <td>0.3</td>
  </tr>
  <tr>
    <td>B13</td>
    <td>0.5</td>
  </tr>
  <tr>
    <td>C11</td>
    <td rowspan="3">20</td>
    <td>0.1</td>
  </tr>
  <tr>
    <td>C12</td>
    <td>0.3</td>
  </tr>
  <tr>
    <td>C13</td>
    <td>0.5</td>
  </tr>
</tbody>
</table>

The simulation results for various combinations of data in Table 4 are shown in Figure 9, showing the received fundamental and second harmonic amplitudes and the uncorrected $\beta'$. From the viewpoint of the maximum second harmonic reception, the best case is B11 or C11, and, from the viewpoint of $\beta'$ or $C_T$, Case A13 may be better. Considering both of these goals, all three cases in Group A are good. These results show that the APAT specifications optimized for one objective may not satisfy the other objective. Therefore, in the optimization of the APAT specification, the objective function—second harmonic reception, total correction, or both—needs to be clearly defined.

### 4.3. Summary of Optimization Results

In relation to the measurement of nonlinear parameters of materials in the pulse–echo mode, the optimal design of the annular phased array transmitter consisting of four equal width (EW) elements was considered. With the specimen thickness, frequency, and receiver size fixed, the optimization of the APAT was performed from two viewpoints: received second harmonic amplitude and total correction. The received amplitudes of the fundamental and second harmonics and the total correction were calculated through wave field analysis for various combinations of the element width, kerf, and focal length of the transmitter. Then, the optimized specifications of the APAT were obtained by comparing the received second harmonic amplitude and the total correction from various simulation

cases. In the optimal design process of APAT, the results of the through-transmission (TT) method by a single transmitter and a single receiver were used as a reference.

![](./images/812530553172525057_13.jpg)

Figure 9. Received displacements and uncorrected nonlinear parameter calculated using the simulation parameters in Table 4: (a) fundamental wave; (b) second harmonic wave; and (c) uncorrected nonlinear parameter.

The optimization results are summarized in Table 5, where the three optimized APAT designs—A13, B13, and C13 in Table 4—are given together with the TT results. The kerf sizes of these types are all 0.5 mm, and the focal length is 10, 15, and 20 mm, respectively. From the viewpoint of the maximum second harmonic reception only, the best case is B13 or C13, and, from the viewpoint of uncorrected nonlinear parameter $\beta'$ or the total correction $C_T$ only, A13 is better. Considering both of these conditions, A13 is just fine. These results show that the APAT specifications optimized for one objective may not satisfy the other objective. Therefore, in the optimization of the APAT specification, the objective function—second harmonic reception, total correction, or both—should be clearly specified.

<table>
<caption>Table 5. Summary of optimized APAT specifications and simulation results.</caption>
<thead>
<tr>
<th>Specification</th>
<th>Single (TT)</th>
<th>PA (PE)</th>
<th>PA (PE)</th>
<th>PA (PE)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Transmitter (mm)</td>
<td>Diameter = 12.7</td>
<td colspan="3">Element width = 1<br>kerf = 0.5</td>
</tr>
<tr>
<td>Focal length (mm)</td>
<td>-</td>
<td>10</td>
<td>15</td>
<td>20</td>
</tr>
<tr>
<td>Receiver dia. (mm)</td>
<td>12.7</td>
<td>3.2</td>
<td>3.2</td>
<td>3.2</td>
</tr>
<tr>
<td>$u_1$(m)</td>
<td>$8.82 × 10^{-10}$</td>
<td>$5.20 × 10^{-10}$</td>
<td>$1.07 × 10^{-10}$</td>
<td>$1.45 × 10^{-9}$</td>
</tr>
<tr>
<td>$u_2$(m)</td>
<td>$1.46 × 10^{-13}$</td>
<td>$1.10 × 10^{-13}$</td>
<td>$1.76 × 10^{-13}$</td>
<td>$2.03 × 10^{-13}$</td>
</tr>
<tr>
<td>$\beta'$</td>
<td>6.04</td>
<td>6.54</td>
<td>2.48</td>
<td>1.56</td>
</tr>
<tr>
<td>$C_T$</td>
<td>0.91</td>
<td>0.84</td>
<td>2.22</td>
<td>3.53</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="5">Note: PA = Phased array; TT = Through-transmission; PE = Pulse-echo.</td>
</tr>
</tfoot>
</table>

We already developed the measurement procedure to determine material nonlinearity in the pulse–echo method using a single element transducer and a dual element transducer [29,36,37]. The current work is the extension of our previous work on the dual element transducer approach. The single annular transmit element was simply replaced by the four annular transmit elements to create a focused beam at a specific location in the specimen. If the annular phased array transducer with four element transmitter and a single element receiver can be made and used, similar measurement procedures can be applied, including receiver calibration.

### 4.4. FE Simulation Results

The analytical acoustic model introduced in Section 3 is a method of calculating the wave field in the frequency domain and provides the received displacement value at a specific frequency. To obtain the received waveform in the time domain, displacement must be calculated at hundreds of frequency values and then inversely Fourier-transformed. Therefore, the analytic method is not suitable for time domain waveform calculation. In ultrasonic modeling, one of the most efficient ways to directly calculate the waveform is the finite element method.

In the case of performing a nonlinear experiment using the optimized APAT of Sections 4.1 and 4.2, a tone burst waveform of tens of cycles is used as an input signal and is received by the receive transducer after being focused on a specific position in the specimen. Therefore, it may be necessary to ensure that the time-delayed signal emitted by each element of the APAT is arrived in-phase at the focal position and then received in the same waveform as the initially incident signal without distortion.

In this section, the waveform of the received signal was obtained through FEA. The purpose of FEA is to check the distortion of the received waveform after being focused on a position in the specimen, and to validate the analytical model used for wave field calculation and optimization of annular phased arrays. COMSOL Multiphysics FE program was used to simulate the nonlinear wave fields calculation. The specimen used is an aluminum with quadratic material nonlinearity [39]. The quadratic nonlinear material is defined by the third-order elastic constants $l$, $m$, and $n$, which is also called "Murnaghan material" in the built-in option of COMSOL program. Simulation was carried out using the second-order axisymmetric model. The source displacement used in the FE simulation was $u_0 = 10^{-7}\ m$, which is two orders of magnitude larger than that used in the analytical simulation. This is for easy visualization of the relatively small second harmonic component in the received signal of the FE simulation.

The three types of EW APAT in Table 4—A13, B13, and C13—were used in the FE simulation. The kerf sizes of these types are all 0.5 mm, and the focal length is 10, 15, and 20 mm, respectively. The FE simulation results are presented in Figure 10, showing the received signal waveforms for the three cases. The results show that the peak amplitude of the received waveform, measured in the order of C13 > B13 > A13, is in good qualitative agreement with the analytical simulation results shown in Figure 9a. In the case of C13, where the focal position and the receiver position are the same (Figure 10c), the signal radiated from each element appears to arrive in-phase at the specified focal position. In addition, the overall shape of the waveform seems to match the input signal well without any significant difference. In Cases A13 and B13, where the focal position and the receiver position are different, there is a slight difference in the leading and trailing edges of the received waveform compared to the input waveform. This difference may occur because the focal position and the reception position are not the same, and it occurs slightly larger in Case A13, where the difference between these two positions is larger. Since the difference in waveform is very small, it is believed that it will have little effect on the measurement of nonlinear parameters. If the reception time delay is applied to the received waveform, the waveform difference can be reduced.

However, it was determined that there is little effect on the measurement of nonlinear parameters because the distortion of the waveform was not large in the simulation results.

The frequency spectrum of the received signal in Figure 10 is shown in Figure 11. To easily visualize the second harmonic component, the spectral values were multiplied by 10. The second harmonic component can be clearly seen in all three cases. The peak magnitude of each spectrum is in the order of C13 > B13 > A13, which also agrees well with the analytical calculation results. It should be noted that a spectral component of large size is present in the very low frequency region. This is known as a zero-frequency component or a quasi-static component which is produced by nonlinear acoustic wave propagation in an elastic solid of quadratic nonlinearity. Although its existence has been proven through theory and FE simulation [39,40], it is not easy to experimentally observe this component because a wideband receiver that covers down to zero frequency cannot be easily found.

![](./images/812530553172525057_14.jpg)

Figure 10. The received signal waveforms for three different APAT cases in Table 4: (a) Case A13;
(b) Case B13; and (c) Case C13.

![](./images/812530553172525057_15.jpg)

Figure 11. The received signal spectrum for three different APAT cases in Figure 10: (a) Case A13; (b) Case B13; and (c) Case C13.

## 5. Conclusions

In this paper, we present the analytical model, optimization method, and optimized design results of annular phased array transmitter for efficient second harmonic generation and nonlinear parameter determination in the pulse–echo nonlinear ultrasonic testing. The annular phased array transducer consisting of four-element transmitter and a single-element receiver was optimized in terms of second harmonic reception and total correction. The performance of various combinations of transmitter design variables and focal lengths were tested through wave field analysis, and the optimized specifications of the transmitter were determined and presented. In the future, the fabrication and experimental verification of optimized annular phased array transducers through acoustic performance testing and nonlinear parameter measurement is required. In addition, when using the focused beam of the annular phased array transducer, applying a reception time delay will further enhance the received second harmonic amplitude in the pulse echo mode. These additional studies are expected to develop the pulse–echo nonlinear ultrasonic tests as more practical nondestructive evaluation and diagnosis techniques.

**Author Contributions:** Writing—original draft preparation, S.C.; Writing—review and supervision, H.J.; and review and editing, I.K.P. All authors have read and agreed to the published version of the manuscript.

**Funding:** This work was supported by the Korea Institute of Energy Technology Evaluation and Planning (KETEP), the Ministry of Trade, Industry and Energy (MOTIE) of the Republic of Korea, and National Research Foundation of Korea(NRF) (Grant Nos. 20181510102130 and 2019R1F1A1045480).

**Conflicts of Interest:** The authors declare no conflict of interest.

## References

1.  Ciorau, P.; Pullia, L.; Hazelton, T.; Daks, W. Phased array ultrasonic technology (PAUT) contribution to detection and sizing of microbially influenced corrosion (MIC) of service water systems and shut down coolers heat exchangers in OPG CANDU stations. In Proceedings of the 8th International Maintenance Conference for CANDU, Toronto, ON, Canada, 16–18 November 2008.

2.  Carboni, M.; Cantini, S.; Gilardoni, C. Validation of the rotating UT probe for in-service inspections of freight solid axles by means of the MAPOD approach. In Proceedings of the 5th European-American Workshop on Reliability of NDE, Berlin, Germany, 7–10 October 2013.

3.  Hagglund, F.; Robson, M.; Troughton, M.J.; Spicer, W.; Pinson, I.R. A novel phased array ultrasonic testing (PAUT) system for on-site inspection of welded joints in plastic pipes. In Proceedings of the 11th European Conference on Non-Destructive Testing (ECNDT), Prague, Czech Republic, 6–10 October 2014.

4.  Hwang, Y.I.; Park, J.; Kim, H.J.; Song, S.J.; Cho, Y.S.; Kang, S.S. Performance comparison of ultrasonic focusing techniques for phased array ultrasonic inspection of dissimilar metal welds. *Int. J. Precis. Eng. Manuf.* 2019, 20, 525–534. [CrossRef]

5.  Cantrell, J.H.; Yost, W.T. Nonlinear ultrasonic characterization of fatigue microstructures. *Int. J. Fatigue* 2001, 23, 487–490. [CrossRef]

6.  Cantrell, J.H.; Yost, W.T. Acoustic nonlinearity and cumulative plastic shear strain in cyclically loaded metals. *J. Appl. Phys.* 2013, 113, 153506. [CrossRef]

7.  Matlack, K.H.; Kim, J.Y.; Wall, J.J.; Qu, J.; Jacobs, L.J.; Sokolov, M.A. Sensitivity of ultrasonic nonlinearity to irradiated, annealed, and re-irradiated microstructure changes in RPV steels. *J. Nucl. Mater.* 2014, 448, 26–32. [CrossRef]

8.  Matlack, K.H.; Kim, J.Y.; Jacobs, L.J.; Qu, J. Review of second harmonic generation measurement techniques for material state determination in metals. *J. Nondestr. Eval.* 2015, 34, 273. [CrossRef]

9.  Wang, X.; Wang, X.; Hu, X.L.; Chi, Y.B.; Xiao, D.M. Damage assessment in structural steel subjected to tensile load using nonlinear and linear ultrasonic techniques. *Appl. Acoust.* 2019, 144, 40–50. [CrossRef]

10. Kim, J.; Kim, J.G.; Kong, B.; Kim, K.M.; Jang, C.; Kang, S.S.; Jhang, K.Y. Applicability of nonlinear ultrasonic technique to evaluation of thermally aged CF8M cast stainless steel. *Nucl. Eng. Technol.* 2020, 52, 621–625. [CrossRef]

11. Pruell, C.; Kim, J.Y.; Qu, J.; Jacobs, L.J. Evaluation of fatigue damage using nonlinear guided waves. Smart Mater. Struct. 2009, 18, 035003. [CrossRef]

12. Walker, S.V.; Kim, J.Y.; Qu, J.; Jacobs, L.J. Fatigue damage evaluation in A36 steel using nonlinear Rayleigh surface waves. NDT E Int. 2012, 48, 10-15. [CrossRef]

13. Xiang, Y.; Deng, M.; Xuan, F.Z.; Liu, C.J. Experimental study of thermal degradation in ferritic Cr-Ni alloy steel plates using nonlinear Lamb waves. NDT E Int. 2011, 44, 768-774. [CrossRef]

14. Ruiz, A.; Ortiz, N.; Medina, A.; Kim, J.Y.; Jacobs, L.J. Application of ultrasonic methods for early detection of thermal damage in 2205 duplex stainless steel. NDT E Int. 2013, 54, 19-26. [CrossRef]

15. Matlack, K.H.; Wall, J.J.; Kim, J.Y.; Qu, J.; Jacobs, L.J.; Viehrig, H.W. Evaluation of radiation damage using nonlinear ultrasound. J. Appl. Phys. 2012, 111, 054911. [CrossRef]

16. Apple, T.M.; Cantrell, J.H.; Amaro, C.M.; Mayer, C.R.; Yost, W.T.; Agnew, S.R.; Howe, J.M. Acoustic harmonic generation from fatigue-generated dislocation substructures in copper single crystals. Philos. Mag. 2013, 93, 2802-2825. [CrossRef]

17. Balasubramaniam, K.; Valluri, J.S.; Prakash, R.V. Creep damage characterization using a low amplitude nonlinear ultrasonic technique. Mater. Charact. 2011, 62, 275-286. [CrossRef]

18. Viswanath, A.; Rao, B.P.C.; Mahadevan, S.; Parameswaran, P.; Jayakumar, T.; Raj, B. Nondestructive assessment of tensile properties of cold worked AISI type 304 stainless steel using nonlinear ultrasonic technique. J. Mater. Process. Technol. 2011, 211, 538-544. [CrossRef]

19. Nucera, C.; Lanza di Scalea, F. Nonlinear wave propagation in constrained solids subjected to thermal loads. J. Sound Vib. 2014, 333, 541-554. [CrossRef]

20. Shui, G.; Wang, Y.S.; Gong, F. Evaluation of plastic damage for metallic materials under tensile load using nonlinear longitudinal waves. NDT E Int. 2013, 55, 1-8. [CrossRef]

21. Bender, F.A.; Kim, J.Y.; Jacobs, L.J.; Qu, J. The generation of second harmonic waves in an isotropic solid with quadratic nonlinearity under the presence of a stress-free boundary. Wave Motion 2013, 50, 146-161. [CrossRef]

22. Vander Meulen, F.; Haumesser, L. Evaluation of B/A nonlinear parameter using an acoustic self-calibrated pulse-echo method. Appl. Phys. Lett. 2008, 92, 214106. [CrossRef]

23. Best, S.R.; Croxford, A.J.; Neild, S.A. Pulse-echo harmonic generation measurements for non-destructive evaluation. J. Nondestr. Eval. 2014, 33, 205-215. [CrossRef]

24. Saito, S. Nonlinearly generated second harmonic sound in a focused beam reflected from free surface. Acoust. Sci. Technol. 2005, 26, 55-61. [CrossRef]

25. Zhang, S.; Li, X.; Jeong, H.; Cho, S.; Hu, H. Theoretical and experimental investigation of the pulse-echo nonlinearity acoustic sound fields of focused transducers. Appl. Acoust. 2017, 117, 145-149. [CrossRef]

26. Jeong, H.; Zhang, S.; Barnard, D.; Li, X. A novel and practical approach for determination of the acoustic nonlinearity parameter using a pulse-echo method. AIP Conf. Proc. 2016, 1706, 060006.

27. Dace, G.E.; Thompson, R.B.; Buck, O. Measurement of the acoustic harmonic generation for materials characterization using contact transducers. In Review of Progress in Quantitative Nondestructive Evaluation; Springer: Berlin/Heidelberg, Germany, 1992; Volume 11, pp. 2069-2076.

28. Jeong, H.; Barnard, D.; Cho, S.; Zhang, S.; Li, X. Receiver calibration and the nonlinearity parameter measurement of thick solid samples with diffraction and attenuation corrections. Ultrasonics 2017, 81, 147-157. [CrossRef] [PubMed]

29. Jeong, H.; Cho, S.; Shin, H.; Zhang, S.; Li, X. Optimization and validation of dual element ultrasound transducers for improved pulse-echo measurements of material nonlinearity. IEEE Sen. J. 2020, 20, 13596-13606. [CrossRef]

30. Sy, K.; Brédif, P.; Iakovleva, E.; Roy, O.; Lesselier, D. Development of methods for the analysis of multi-mode TFM images. J. Phys. Conf. Ser. 2018, 1017. [CrossRef]

31. Aizpurua, I.; Ayesta, I.; Castro, I. Characterization of anisotropic weld structure for nuclear industry. In Proceedings of the 11th European Conference on NDT, Prague, Czech Republic, 6-10 October 2014.

32. Jeong, H. Time Reversal-based beam focusing of an ultrasonic phased array transducer on a target in anisotropic and inhomogeneous welds. Mater Eval. 2014, 72, 589-596.

33. Shattuck, D.P.; Von Ramm, O.T. Compound scanning with a phased array. Ultrason. Imaging 1982, 4, 93-107. [CrossRef]

34. Von Ramm, O.T.; Smith, S.W. Beam steering with linear arrays. IEEE Trans. Biomed. Eng. 1983, 30, 438-452. [CrossRef]

35. McNab, A.; Stumpf, I. Monolithic phased array for the transmission of ultrasound in NDT ultrasonics. Ultrasonics 1986, 24, 148-155. [CrossRef]

36. Jeong, H.; Cho, S.; Zhang, S.; Li, X. Acoustic nonlinearity parameter measurements in a pulse-echo setup with the stress-free reflection boundary. J. Acoust. Soc. Am. 2018, 143, EL237-EL242. [CrossRef] [PubMed]

37. Cho, S.; Jeong, H.; Zhang, S.; Li, X. Dual element transducer approach for second harmonic generation and material nonlinearity measurement of solids in the pulse-echo method. J. Nondestr. Eval. 2020, 39, 62. [CrossRef]

38. Liaptsis, G.; Liaptsis, D.; Wright, B.; Charlton, P. Focal law calculations for annular phased array transducers. e-J. Nondestr. Test. 2015, 20, 1-7.

39. Nagy, P.B.; Qu, J.; Jacobs, L.J. Finite-size effects on the quasistatic displacement pulse in a solid sample with quadratic nonlinearity. J. Acoust. Soc. Am. 2013, 134, 1760-1774. [CrossRef] [PubMed]

40. Qu, J.; Jacobs, L.J.; Nagy, P.B. On the acoustic-radiation-induced strain and stress in elastic solids with quadratic nonlinearity (L). J. Acoust. Soc. Am. 2011, 129, 3449-3452. [CrossRef] [PubMed]

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](./images/812530553172525057_16.jpg)

© 2020 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/).