# Response and energy dissipation of rock under stochastic stress waves
DENG Jian(邓 建)¹, BIAN Li(边 利)²

(1.School of Resources and Safety Engineering, Central South University, Changsha 410083, China;
2. School of Business, Central South University, Changsha 410083, China)

**Abstract:** The response and energy dissipation of rock under stochastic stress waves were analyzed based on dynamic fracture criterion of brittle materials integrating with Fourier transform methods of spectral analysis. When the stochastic stress waves transmit through rocks, the frequency and energy ratio of harmonic components were calculated by analytical and discrete analysis methods. The stress waves in shale, malmstone and liparite were taken as examples to illustrate the proposed analysis methods. The results show the harder the rock, the less absorption of energy, the more the useless elastic waves transmitting through rock, and the narrower the cutoff frequency to fracture rock. When the whole stress energy doubles either by doubling the duration time or by increasing the amplitude of stress wave, ratio of the energy of elastic waves transmitting through rock to the whole stress energy (i.e. energy dissipation ratio) is decreased to 10%-15%. When doubling the duration time, the cutoff frequency to fracture rock remains constant. However, with the increase of the amplitude of stress wave, the cutoff frequency increases accordingly.

**Key words:** stochastic stress waves; dynamic fracture criterion; Fourier transform; energy dissipation; rock

## 1 Introduction
It is well known that rock fracture by dynamic load occurs in a wide range of technologically important applications such as mining, earthquake engineering, high speed impact and blasting, etc. During the process of rock fracture, many cracks are nucleated and they propagate simultaneously in the material, ultimately coalescing and separating the solid into fragments. Some energy of stress waves is used in crack expansion and propagation and formation of new rock surface as well, other energy dissipates uselessly as elastic waves. In order to break rocks or stabilize rocks effectively, analysis of response and energy dissipation of rock under stress waves is urgently needed⁽¹⁻⁷⁾.

The dynamic load in rocks is very complicated. In mechanical impact, different shapes and lengths of indentors will generate different waveforms and duration time. Even if the explosive and rock impedance are coupled, different volumes and structures of explosives also lead to different amplitudes, forms and duration time of explosive stress waves. Generally speaking, most dynamic load in rock is irregular or stochastic, and rare stress waves are regular. Dynamic load is difficult to describe as deterministic process. Regular stress waves such as rectangular, sine, and triangular waves cannot be simply used to depict the stress in rocks. However, the stochastic process is regarded as the best method to explain the stress waves⁽⁸⁾. In this study, the response and energy dissipation of rock under stochastic stress waves were analyzed based on dynamic fracture criterion of brittle materials in conjunction with Fourier transform methods of spectral analysis. The frequency and energy ratio of harmonic components in stress waves were calculated. The stress waves in shale, malmstone and liparite were taken as examples to illustrate the proposed analytical and discrete analysis method.

## 2 Stochastic stress wave and rock crack expansion
### 2.1 Dynamic fracture criterion of rock
STEVERDING et al⁽⁹⁾ proposed a dynamic fracture criterion for brittle materials. Given any waveform of stress impulse $\sigma(t)$, the criterion for brittle material ruptures is
$$
\int_{0}^{\tau} \sigma^{2}(t) \mathrm{d} t \geqslant \frac{\pi \gamma E}{C} \tag{1}
$$
where $\sigma(t)$ is any stress wave, $\tau$ is the duration time, $\gamma$ is the specific surface energy of a material, $E$ is the elastic modulus, $C$ is the longitudinal velocity of the material.

### 2.2 Fourier transform and crack expansion (analytical method)
Given a stress wave function $\sigma(t)$, its Fourier transform is

---
Foundation item: Projects(50404010, 50574098) supported by the National Natural Science Foundation of China; project(05jj10010) supported by the Hunan Provincial Natural Science Foundation of Distinguished Young Scholars
Received date: 2006-04-28; Accepted date: 2006-06-15
Corresponding author: DENG Jian, Professor, PhD; Tel:+86-731-8879612; E-mail: jdengj@sina.com

$$
\begin{aligned}
F(\omega)= & \int_{-\infty}^{+\infty} \sigma(t) \mathrm{e}^{-\mathrm{j} \omega t} \mathrm{~d} t= \\
& \int_{-\infty}^{+\infty} \sigma(t) \cos (\omega t) \mathrm{d} t-\mathrm{j} \int_{-\infty}^{+\infty} \sigma(t) \sin (\omega t) \mathrm{d} t \quad (2)
\end{aligned}
$$

Amplitude-frequency spectrum of the stress wave is
$$
|F(\omega)|=\sqrt{\left|\int_{-\infty}^{+\infty} \sigma(t) \cos (\omega t) \mathrm{d} t\right|^{2}+\left|\int_{-\infty}^{+\infty} \sigma(t) \sin (\omega t) \mathrm{d} t\right|^{2}} \quad (3)
$$

For single harmonic component whose frequency is $\omega$ the stress wave can be written in the form of cosine: $\widetilde{\sigma}(t)=\sigma_{\omega} \cos (\omega t)$. Its corresponding energy density is $e_{\omega}=\int_{-\pi}^{\pi}[\widetilde{\sigma}(t)]^{2} \mathrm{~d} t=\sigma_{\omega}^{2} \pi / \omega$ . According to the STEVERDING LEHNIGK dynamic fracture criterion $^{[9]}$, the sub-wave with frequency of $\omega$ has the capability to fracture a rock, if
$$
\frac{\sigma_{\omega}^{2}}{\omega^{2}} \geqslant \frac{\gamma E}{C \omega} \quad (4)
$$
and by PARSEVAL theorem $^{[3,10]}$:
$$
\int_{-\infty}^{\infty}[\sigma(t)]^{2} \mathrm{~d} t=\frac{1}{2 \pi} \int_{-\infty}^{\infty}|F(\omega)|^{2} \mathrm{~d} \omega \quad (5)
$$
then we obtain $^{[3]}$
$$
\frac{\sigma_{\omega}^{2}}{\omega^{2}}=|F(\omega)|^{2} \quad (6)
$$

The criterion for crack expansion is
$$
|F(\omega)|^{2} \geqslant \frac{\gamma E}{C \omega} \quad (7)
$$

Substitute Eqn.(2) into Eqn.(7), it gives
$$
\left|\int_{-\infty}^{+\infty} \sigma(t) \mathrm{e}^{-\mathrm{j} \omega t} \mathrm{~d} t\right|^{2} \geqslant \frac{\gamma E}{C \omega} \quad (8)
$$
or substitute Eqn.(3) into Eqn.(7), it gives
$$
\left|\int_{-\infty}^{+\infty} \sigma(t) \cos (\omega t) \mathrm{d} t\right|^{2}+\left|\int_{-\infty}^{+\infty} \sigma(t) \sin (\omega t) \mathrm{d} t\right|^{2} \geqslant \frac{\gamma E}{C \omega}
$$

The cut-off frequency of the harmonic components and energy dissipation ratio in rock crack expansion can be obtained with Eqn.(8) or (9). The energy dissipation ratio is defined as the ratio of the transmitted (useless) energy to the whole energy. For some simple waveforms, the stress wave is described in analytical formula, and Eqn.(8) can be used in this circumstance. However, to some complicated stochastic stress waves, numerical computation such as numerical integral and numerical equation solver is needed in Eqn.(9).

### 2.3 Discrete Fourier transform and crack expansion (discrete method)
When the stress wave is expressed by irregular form or a finite set of data, discrete Fourier transform is needed. Given a stochastic stress wave function $\sigma(t)$, sampling is performed to obtain a finite set of data $\sigma(n)$. Only at points $n=0$ to $(N-1)$ the values of $\sigma(n)$ are not zero, i.e.
$$
\sigma(n)=\left\{\begin{array}{lc}
\sigma(n), & 0 \leqslant n \leqslant N-1 \\
0, & \text { others }
\end{array}\right. \quad (10)
$$

The sequence $\sigma(n)$ can be extended to a cyclic sequence $\widetilde{\sigma}(n)$ with a cycle of $N$,
$$
\widetilde{\sigma}(n)=\sum_{r=-\infty}^{+\infty} x(n+r N) \quad (11)
$$

Let
$$
\sigma(n)=\left\{\begin{array}{lc}
\widetilde{\sigma}(n), & 0 \leqslant n \leqslant N-1 \\
0, & \text { others }
\end{array}\right. \quad (12)
$$

The formula of Fourier series and inverse Fourier series are
$$
\begin{gathered}
\widetilde{X}(k)=\sum_{n=0}^{N-1} \widetilde{x}(n) W_{N}^{k n}, \quad \widetilde{x}(n)=\frac{1}{N} \sum_{k=0}^{N-1} \widetilde{X}(k) W_{N}^{-k n} \\
\text { where } W_{N}=\exp \left[-\mathrm{j}\left(\frac{2 \pi}{N}\right)\right], \quad \widetilde{X}(k) \text { is the coefficient of }
\end{gathered}
$$
the $k$ th harmonic component.

Discrete Fourier transform of a finite set of stress data $\sigma(n)$ is
$$
F(k)=\sum_{n=0}^{N-1} \sigma(n) W_{N}^{k n}, \quad 0 \leqslant k \leqslant N-1 \quad (14)
$$

The inverse discrete Fourier transform is
$$
\sigma(n)=\frac{1}{N} \sum_{k=0}^{N-1} F(k) W_{N}^{-k n}, \quad 0 \leqslant n \leqslant N-1 \quad (15)
$$

Discrete Fourier transform can be readily performed by the function 'fft' in the software MATLAB. The criterion for rock crack expansion is
$$
|F(\omega)|^{2} \geqslant \frac{\gamma E}{C \omega} \quad (16)
$$

The cutoff frequency of the harmonic components and energy dissipation ratio in rock crack expansion can be obtained by Eqn.(16).

## 3 Examples
Take rectangular stress wave as an example to illustrate the proposed analysis method. Fourier transform and rock dynamic fracture criterion are applied to analyze the energy dissipation of stress waves. The results obtained by analytical method are compared with those by discrete method.

The specific surface energy $\gamma$ of rocks can be calculated as $^{[11-12]}$
$$
\gamma=\frac{K_{\mathrm{IC}}^{2}}{\rho C^{2}}=\frac{K_{\mathrm{IC}}^{2}}{E} \quad (17)
$$

where $K_{IC}$ is the rock's dynamic fracture toughness($\text{Pa·m}^{1/2}$), $E$ is the rock elastic modulus, $C$ is rock's longitudinal wave velocity, $C=(E/\rho)^{1/2}$。The stress waves in shale, malmstone and liparite are taken as examples to obtain energy dissipation law of rocks under stress waves. The physical and mechanical parameters of common rocks are listed in Table 1.

Table 1 Physical and mechanical parameters of common rocks$^{[13]}$
| Rock      | Density/ ($\text{g·cm}^{-3}$) | Uniaxial compressive strength/ MPa | Elastic modulus/ GPa | Specific surface energy/ ($\text{J·m}^{-2}$) | Longitudinal wave velocity/ ($\text{m·s}^{-1}$) |
|-----------|-------------------------------|------------------------------------|----------------------|----------------------------------------------|-------------------------------------------------|
| Shale     | 2.31                          | 37.0–67.0                          | 19.4                 | 1.0–1.2                                      | 2 920                                           |
| Malmstone | 2.42                          | 69.0–107.0                         | 26.6                 | 1.4–1.6                                      | 4 020                                           |
| Liparite  | 3.20                          | 81.1                               | 35.5                 | 1.3–1.5                                      | 4 500                                           |

The amplitude of rectangular stress wave is supposed to be $\sigma$, the duration time is $\tau$, which is from $-\tau/2$ to $\tau/2$. The stress wave and the corresponding frequency spectrum are
$$
\sigma(t)=
\begin{cases}
\sigma, & |t| \leqslant \tau/2 \\
0, & \text{others}
\end{cases} \tag{18}
$$

$$
F(\omega)=\int_{-\tau / 2}^{\tau / 2} \sigma(t) \mathrm{e}^{-\mathrm{j} \omega t} \mathrm{~d} t=2 \sigma \frac{\sin (\omega \tau / 2)}{\omega} \tag{19}
$$

Substitute Eqns.(18) and (19) into Eqn.(8), when $\sigma^{2} \tau<0.69 \gamma E / C$, the energy of stress wave is dissipated as elastic wave which is wholly transmitted through rocks, i.e. the energy dissipation ratio is 100%. The cutoff frequency of harmonic components is $2.32 / \tau$. When $\sigma^{2} \tau<0.69 \gamma E / C$, the energy dissipation ratio is 14.28%. The cutoff frequency of harmonic components is between $0.321\ 8/\tau$ and $4.929\ 4/\tau$. Three cases are discussed as follows. The difference between Case 1 and Case 2 is duration time of stress waves, and difference between Case 1 and Case 3 is the amplitude of stress waves.

Case 1 When the amplitude of stress wave $\sigma$=50 MPa, the duration time $\tau$=10 $\mu\text{s}$, and rock is shale, the $\sigma^{2}\tau$=3.42$\gamma E/C$, the cutoff frequency of harmonic components is between $0.294\ 4/\tau$ and $4.987\ 0/\tau$, the energy dissipation ratio is 16.45%. When the discrete method is used, the energy dissipation ratio is 16.53%. The cases for malmstone rock and liparite rock are listed in Table 2.

Case 2 When the amplitude of stress wave $\sigma$=50 MPa, the duration time $\tau$=20 $\mu\text{s}$, the energy of stress wave doubles compared with case 1. The cutoff frequency of harmonic components and energy dissipation ratio for three rocks are listed in Table 3.

Case 3 When the amplitude of stress wave $\sigma$=70 MPa, the duration time $\tau$=10 $\mu\text{s}$, the energy of wave stress almost doubles as compared with case 1. The cutoff frequency of harmonic components and stress wave energy dissipation ratio for three rocks are listed in Table 4.

From Tables 2–4, the conclusions can be made that the results from analytical method and discrete method coincide with each other. The harder the rock, the less the absorption of energy, the more the useless elastic waves transmitting through rock, and the narrower the cutoff frequency to fracture rock. When the whole stress energy doubles either by doubling the duration time or by increment of the amplitude of stress wave, the energy

<table>
<caption>Table 2 Results of energy dissipation in different rocks for Case 1($\sigma$=50 MPa, $\tau$=10 $\mu\text{s}$)</caption>
<thead>
<tr>
<th>Rock</th>
<th>Energy of stress wave</th>
<th>Cutoff frequency</th>
<th colspan="2">Energy dissipation ratio/%</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th>Analytical method</th>
<th>Discrete method</th>
</tr>
</thead>
<tbody>
<tr>
<td>Shale</td>
<td>$3.42\frac{\gamma E}{C}$</td>
<td>$\left(\frac{0.294\ 4}{\tau},\frac{4.987\ 0}{\tau}\right)$</td>
<td>16.45</td>
<td>16.53</td>
</tr>
<tr>
<td>Malmstone</td>
<td>$2.52\frac{\gamma E}{C}$</td>
<td>$\left(\frac{0.405\ 6}{\tau},\frac{4.760\ 4}{\tau}\right)$</td>
<td>20.72</td>
<td>20.72</td>
</tr>
<tr>
<td>Liparite</td>
<td>$2.28\frac{\gamma E}{C}$</td>
<td>$\left(\frac{0.446\ 6}{\tau},\frac{4.683\ 6}{\tau}\right)$</td>
<td>21.98</td>
<td>22.11</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 3 Results of energy dissipation in different rocks for Case 2 ($\sigma$=50 MPa, $\tau$=20 $\mu\text{s}$)</caption>
<thead>
<tr>
<th>Rock</th>
<th>Energy of stress wave</th>
<th>Cutoff frequency</th>
<th colspan="2">Energy dissipation ratio/%</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th>Analytical method</th>
<th>Discrete method</th>
</tr>
</thead>
<tbody>
<tr>
<td>Shale</td>
<td>$6.84\frac{\gamma E}{C}$</td>
<td>$\left(\frac{0.146\ 4}{\tau},\frac{5.365\ 8}{\tau}\right)$</td>
<td>11.27</td>
<td>11.29</td>
</tr>
<tr>
<td>Malmstone</td>
<td>$5.04\frac{\gamma E}{C}$</td>
<td>$\left(\frac{0.199\ 2}{\tau},\frac{5.215\ 6}{\tau}\right)$</td>
<td>13.10</td>
<td>13.10</td>
</tr>
<tr>
<td>Liparite</td>
<td>$4.55\frac{\gamma E}{C}$</td>
<td>$\left(\frac{0.220\ 6}{\tau},\frac{5.160\ 4}{\tau}\right)$</td>
<td>13.85</td>
<td>13.85</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 4 Results of energy dissipation in different rocks for Case 3 ($\sigma$=70 MPa, $\tau$=10 $\mu$s)</caption>
<thead>
<tr>
<th rowspan="2">Rock</th>
<th rowspan="2">Energy of stress wave</th>
<th rowspan="2">Cutoff frequency</th>
<th colspan="2">Energy dissipation ratio/%</th>
</tr>
<tr>
<th>Analytical method</th>
<th>Discrete method</th>
</tr>
</thead>
<tbody>
<tr>
<td>Shale</td>
<td>$6.71 \frac{\gamma E}{C}$</td>
<td>$\left( \frac{0.149\ 4}{\tau},\frac{5.356\ 6}{\tau} \right)$</td>
<td>11.37</td>
<td>11.38</td>
</tr>
<tr>
<td>Malmstone</td>
<td>$4.94 \frac{\gamma E}{C}$</td>
<td>$\left( \frac{0.203\ 2}{\tau},\frac{5.205\ 0}{\tau} \right)$</td>
<td>13.24</td>
<td>13.24</td>
</tr>
<tr>
<td>Liparite</td>
<td>$4.44 \frac{\gamma E}{C}$</td>
<td>$\left( \frac{0.226\ 4}{\tau},\frac{5.146\ 0}{\tau} \right)$</td>
<td>14.05</td>
<td>14.08</td>
</tr>
</tbody>
</table>

dissipation ratio decrease to 10%−15%. A further study shows that if the energy of stress wave increases continually, the energy dissipation ratio does not decrease any more and remains at 10% or so. This result coincides very well with that in Ref.[14]. When doubling the duration time, the cutoff frequency to fracture rock remains constant. However, as to the increase of the amplitude of stress wave, the cutoff frequency increases accordingly.

### References

[1] CHAU K T, WEI X X, WONG R H C, et al. Fragmentation of brittle spheres under static and dynamic compressions: experiments and analyses[J]. Mechanics of Materials, 2000, 32(9): 543−554.

[2] MILLER O, FREUND L B, NEEDLEMAN A. Modelling and simulation of dynamic fragmentation in brittle materials[J]. International Journal of Fracture[J]. 1999, 96(2): 101−125.

[3] LI Xi-bing, GU De-sheng. Energy dissipation of rock under impluse loading with different waveforms[J]. Explosion and shock waves, 1994, 14(2): 129−139.(in Chinese)

[4] ZHANG Y, LU Y, MA G Investigation of dynamic response of brittle materials under high-rate loading[J]. Mechanics Research Communications, 2006, 33(3): 359−369.

[5] ZHOU F, MOLINARI J F, RAMESH K T. Characteristic fragment size distributions in dynamic fragmentation[J]. Applied Physics Letters, 2006, 88(26): 1918−1920.

[6] ZUO Yu-jun, LI Xi-bing, ZHOU Zi-long. Damage and failure rule of rock undergoing uniaxial compressive load and dynamic load[J]. Journal of Central South University of Technology, 2005, 12(6): 742−748.

[7] PENG Huai-sheng, DENG Jian. Earth slope reliability analysis under seismic loadings using neural networks[J]. Journal of Central South University of Technology, 2005, 1295): 606−610.

[8] LIU Bao-jian, XIE Ding-yi. Test and analysis of soil dynamic nature under stochastic load[M]. Beijing: People's Transportation Press, 2001.(in Chinese)

[9] STEVERDING B, LEHNIGK S H. The Fracture penetration depth of stress pulses[J]. International Journal of Rock Mechanics and Mining Sciences, 1976, 13(3): 75−80.

[10] YING Huai-qiao. Waveform, frequency spectrum and stochastic data[M]. Beijing: China Railway Press, 1983.(in Chinese)

[11] WU De-yi, YAO Jian-dong. Analysis of explosive in fracture control explosion[J]. Explosion in Coal Mine, 1999, 11(2): 11−13.(in Chinese)

[12] ZHANG Li-guo, LI Shou-ju. Research on energy ratio of rock fragment in explosive[J]. Journal of Liaoning Technical University: Natural Science, 1998, 17(2): 133−137.(in Chinese)

[13] TAO Zhen-yu. Foreign application examples and empirical data in rock mechanics of hydraulic engineering[M]. Beijing: China Water and Electrical Press, 1976. (in Chinese)

[14] GOLDSMITH W, WU W Z. Response of rocks to impact loading by bars with pointed ends[J]. Rock Mechanics, 1981, 13(3): 157−182.

(Edited by CHEN Wei-ping)