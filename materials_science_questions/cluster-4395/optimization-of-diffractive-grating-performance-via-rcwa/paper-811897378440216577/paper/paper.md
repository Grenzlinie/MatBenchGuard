# Widely Wavelength-Selectable Lasers With Digital Concatenated Grating Reflectors—Proposal and Simulation

Xiaoying He, Dexiu Huang, Yonglin Yu, Member, IEEE, D. N. Wang, Wen Liu, and Shan Jiang

**Abstract**—A digital concatenated grating is presented to tackle that problem of creating a flat "top-hat" comb reflector for tunable lasers. A novel, monolithic, widely tunable semiconductor laser with these gratings is proposed and demonstrated theoretically.

**Index Terms**—Grating, laser tuning, semiconductor lasers.

## I. INTRODUCTION

M
ONOLITHIC widely tunable semiconductor lasers [1]–[7] are emerging in the past few years as fundamental components for agile optical networks and fiber optical sensor. These lasers utilize a variety of complex grating structures to enhance the tuning range of the device, typically by use of comb reflectors. It is highly desirable to achieve a comb reflector with flat-top-hat envelop response and equal spaced peaks in tunable lasers, which lead to a small output power variation across all available channels due to the fact that the strength of the feedback into the laser cavity can be maintained.

Several methods can be employed in order to produce a flat "top-hat" comb reflector. One approach is to use a superstructure grating or phase grating [3], [5], [7]. These techniques apply chirps or phases to the grating. However, the level of control required writing an e-beam pattern with such subtle variation in the grating pitch and phase means that this style of grating is hard to ensure reproducibly.

Another one is the binary superimposed grating [4], such as a binary sequence on a grid that is finer than the basic pitch of the grating. Even though this method is powerful, it is merely realized on the theoretical analysis.

![](./images/811897378440216577_1.jpg)

Fig. 1. Designing DCG. (a) Reflection-spectrum envelopes of sampled gratings; (b) five sampled gratings; (c) resultant reflection-spectrum envelope; (d) DCG structure.

An alternative approach is the interleaved sampled grating [6], which is made by interleaving a small-duty-cycle sampled grating with fixed $\pi$ phase shift into the sampled grating. It is hard for controlling the fabrication precision with slight variations in the interleaved grating.

While for some of the aforementioned approaches wide quasi-continuous wavelength tuning has been demonstrated, the overall performance of these devices has not yet been sufficient for practical deployment. In this letter, we propose a novel design with operational capability. Digital concatenated grating (DCG) based on our multiple reflection-spectrum envelopes concatenated technology [8] is employed to provide a judicious approach to tackle the problem of creating a flat "top-hat" comb reflector which is ideal for tunable lasers. We will show how to design the DCG theoretically and give an example of the modeled refelection spectrum. In addition, we investigate a style of distributed Bragg reflector (DBR) laser using the DCGs as its comb reflectors.

## II. GRATING AND LASER DESIGNS

### A. Grating Design

The DCG consists of $M$ sampled gratings (denoted as subgratings), as shown in Fig. 1. Thus, the e-beam resolution of our grating required would be the same as the conventional sampled grating. This is an advantage over other modulated gratings. The flat-top reflection envelope in Fig. 1(c) is obtained by concatenating a series of reflection-spectrum envelopes [five curves in Fig. 1(a)] of sampled gratings; their Bragg wavelengths are different, while the other parameters, such as sampling period, duty cycle, etc., are identical. There is no chirped modulation and

Manuscript received April 9, 2008; revised July 14, 2008. Current version published October 8, 2008. This work was supported by the National Natural Science Foundation of China under Grant 60677024, by the National High Technology Research Development Program of China under Grant 2006AA03Z0427, and by Hong Kong Polytechnic University Research Grant A-PH82.

X. He is with the Division of Optoelectronic Deivices and Technology, Wuhan National Laboratory of Optoelectronics, Huazhong University of Science and Technology, 430074 Wuhan, China. She is also with the Department of Electrical Engineering, the HongKong Polytechnic Univeristy, Hong Kong (e-mail: hxyhust@yahoo.com.cn).

D. Huang, Y. Yu, and W. Liu are with the Division of Optoelectronic Deivices and Technology, Wuhan National Laboratory of Optoelectronics, Huazhong University of Science and Technology, 430074 Wuhan, China (e-mail: wnlo2@hust.edu.cn; yonglinyu@hust.edu.cn; wen.liu@accelink.com).

D. N. Wang is with the Department of Electrical Engineering, the HongKong Polytechnic Univeristy, Hong Kong (e-mail: eednwang@polyu.edu.hk).

S. Jiang is with Accelink Technologies Co. Ltd., 430074 Wuhan, China (e-mail: shan.jiang@accelink.com).

Color versions of one or more of the figures in this letter are available online at http://ieeexplore.ieee.org.

Digital Object Identifier 10.1109/LPT.2008.2004676

**TABLE I**
DESIGN PARAMETERS OF THE FRONT AND REAR DCG SECTIONS

<table>
  <tbody>
    <tr>
      <td colspan="5">Front DCG reflector</td>
    </tr>
    <tr>
      <td>The $i$th sub-grating</td>
      <td>Bragg wavelength $\lambda$</td>
      <td>Bragg period $\Lambda$</td>
      <td>Bragg period number</td>
      <td>Grating segment length $Zg$</td>
    </tr>
    <tr>
      <td>$i$=1</td>
      <td>1522.3nm</td>
      <td>224nm</td>
      <td>57</td>
      <td>12.768$\mu$m</td>
    </tr>
    <tr>
      <td>$i$=2</td>
      <td>1550nm</td>
      <td>228nm</td>
      <td>56</td>
      <td>12.768$\mu$m</td>
    </tr>
    <tr>
      <td>$i$=3</td>
      <td>1577.7nm</td>
      <td>232nm</td>
      <td>55</td>
      <td>12.768$\mu$m</td>
    </tr>
    <tr>
      <td colspan="5">Rear DCG reflector</td>
    </tr>
    <tr>
      <td>The $i$th sub-grating</td>
      <td>Bragg wavelength $\lambda$</td>
      <td>Bragg period $\Lambda$</td>
      <td>Bragg period number</td>
      <td>Grating segment length $Zg$</td>
    </tr>
    <tr>
      <td>$i$=1</td>
      <td>1527.2nm</td>
      <td>225nm</td>
      <td>69</td>
      <td>15.504$\mu$m</td>
    </tr>
    <tr>
      <td>$i$=2</td>
      <td>1550nm</td>
      <td>228nm</td>
      <td>68</td>
      <td>15.504$\mu$m</td>
    </tr>
    <tr>
      <td>$i$=3</td>
      <td>1572.8nm</td>
      <td>231nm</td>
      <td>67</td>
      <td>15.504$\mu$m</td>
    </tr>
  </tbody>
</table>

![](./images/811897378440216577_2.jpg)

Fig. 2. Calculated reflection spectrum of two DCG; rear DCG reflection spectrum with dashed line and front DCG reflection spectrum with solid line.

empty region in the DCG structure. The phase at the interface of the adjacent grating segment is also zero.

In our design, the Bragg period of the $i$th subgrating must satisfy the following condition:

$$
\Lambda_{(i)}=\frac{\lambda_{c}}{2n_{\text{eff}}}+\left[\frac{H}{Z_{0}}\left(\frac{\lambda_{c}}{2n_{\text{eff}}}\right)^{2}\right] \tag{1}
$$

where

$$
H=m\times\left(i-\frac{M+1}{2}\right),\quad i=1,2,\cdots\cdots,M \tag{2}
$$

where $M$ and $n_{\text{eff}}$ are the number of subgratings and the effective refractive index of the grating waveguide, respectively. $\lambda_{c}$ is the central wavelength of reflection spectrum of the DCG, and here it is 1550 nm. $m$ is an integer with the value $\leq M+1$ and $\geq M-1$. In our design, the design parameters of the front and rear reflectors of our DCG-DBR laser are listed in Table I. Just following the formula of (1) and (2) to design grating, we can obtain a good DCG with flat-top-hat envelope response. Two calculated reflection spectra are shown in Fig. 2 by the transfer matrix method. Clearly, the comb peaks of two DCG reflectors are almost uniform. Only tuning the injection current of the front DCG reflector from 0 to 1 mA, the coincided reflectivity peak switches from the center peak [in Fig. 2(a)] to the adjacent peak [in Fig. 2(b)], and then the lasing wavelength is tuned from one channel to another, by use of Vernier principle.

![](./images/811897378440216577_3.jpg)

Fig. 3. Schematics structure of the DCG-DBR laser.

![](./images/811897378440216577_4.jpg)

Fig. 4. Wavelength tuning as a function of injection currents of two DCG reflections.

### B. Laser Structure

Fig. 3 shows the schematic configuration of the DCG-DBR laser, which is similar to the familiar Vernier-tuned sampled-grating DBR (SG-DBR) laser except for structures of two grating reflectors. There is a slight difference between the reflection peaks spacing of the two DCG reflectors, which is inversely proportional to their sampling periods. The sampling period $Z_{0}$ of the rear and the front DCG reflector are selected as 46.512 and 38.304 $\mu$m, respectively. The phase section offers a continuous and precise tuning with adjustment of the effective cavity length of the DCG-DBR laser for realizing longitudinal cavity mode tracking. Moreover, two grating reflectors are both composed by three sampled gratings with different Bragg periods. Such a grating could be realized by using the e-beam lithography method. Therefore, the fabrication process technology of the tunable DCG-DBR laser is similar to conventional SG-DBR laser process technology in the GaInAsP-InP material system [9], such as growing by metal-organic chemical vapor deposition, and integrating the active and passive section by the butt-joint growth technology. $\text{H}^{+}$ ions can be implanted into interfaces of the waveguide as electrically isolation. Thus, each section can be driven independently by injection current.

## III. SIMULATION RESULTS AND DISCUSSION

The active section can be biased at 150 mA, and the current to the phase section can be 0 mA. By tuning the currents of two DCG reflector sections from 0 to 100 mA, a wavelength tuning map is clearly shown in Fig. 4 in which a qualitative resemblance to that of SG-DBR laser [2] can be found due to the same tuning operation, i.e., Vernier-tuning operation. The full tuning range of the device is from about 1514 to about

![](./images/811897378440216577_5.jpg)

Fig. 5. Optical emission spectra of DCG-DBR laser of six supermodes, illus- trating the high spectral purity.

![](./images/811897378440216577_6.jpg)

Fig. 6. Output power as a function of injection currents of two DCG reflections.

1568 nm, which is sufficient to span over the whole $C$-band.
Wavelength tuning map of Fig. 4 demonstrates six supermodes with six colors, where the alignment of the front and rear reflec- tivity peaks was switched from one pair to others. Unlike other Vernier-tuning DBR lasers, the supreme tuning range of wave- length in these DCG-DBR lasers is not limited by the repeat mode wavelength spacing, but limited by numbers of uniform reflectivity peaks in the DCG, because the wavelength range of uniform reflectivity peaks is no more than the repeat mode wavelength spacing. In Fig. 4, the map of each supermode can be divided into several saddle girds, and the small sidesteps indi- cate borderlines of each saddle girds and the boundaries of the longitudinal cavity modes, which is related with cavity-mode hops. Unstable operation is observed at the boundary due to mode competition. The high spectral purity of the laser is illus- trated in Fig. 5, showing optical emission spectra of six neigh- boring supermodes. Keeping the current of the active section with 150 mA, the power variation of these six supermodes is sufficient less than 0.6 over 10 dBm. The output powers map is shown in Fig. 6. Furthermore, output power from the front DCG section facet within the whole useful channels is mostly over 10 dBm, which would be larger than other DBR-type lasers [2]–[7] under the same current of the active section. Since the output light has to pass through the front DCG section, this sec- tion plays a key role of output power variation. With the in- crease of injection currents in two grating sections, the output power generally decreases in the SG-DBR laser [2], [7]. For our DCG-DBR laser, however, the output power only presents a slightly decreasing trend. That is due to the fact that the sam- pled grating has $Sinc$ envelop response, while the DCG has flat-top-hat envelop response. An illustration of the sidemode suppression ratio (SMSR) map with respect to the wavelength tuning map is in Fig. 7. Single-mode operation of the DCG-DBR laser with SMSR greater than 40 dB is obtained. The high SMSR is observed at each mode grid center, which is directly attribut- able to the perfect alignment of the coincided reflector peaks with a cavity mode.

![](./images/811897378440216577_7.jpg)

Fig. 7. SMSR as a function of injection currents of two DCG reflections.

## IV. CONCLUSION

We have demonstrated a monolithic tunable DCG-DBR laser depending on Vernier-tuning theoretically. The DCG-DBR laser provides a large quasi-continuous wavelength tuning range over 50 nm with excellent SMSRs of better than 40 dB and high output powers of more than 10 dBm. Moreover the device can provide a small output power variation about 0.6 dBm by only tuning currents of two reflectors, thereby facilitating easy and fast calibration and control. These performances can compare well with other state-of-the-art monolithic tunable laser diodes.

### REFERENCES

[1] J. Buus and E. J. Murphy, "Tunable lasers in optical networks," *J. Lightw. Technol.*, vol. 24, no. 1, pp. 5-11, Jan. 2006.
[2] V. Jayaraman, Z.-M. Chuang, and L. A. Coldren, "Theory, design, and performance of extended tuning range semiconductor lasers with sampled gratings," *IEEE J. Quantum Electron.*, vol. 29, no. 6, pp. 1824-1834, Jun. 1993.
[3] Y. Tomori, Y. Yoshikuni, H. Ishii, F. Kano, T. Tamamura, Y. Kondo, and M. Yamamoto, "Broad-range wavelength-tunable superstructure grating (SSG) DBR lasers," *IEEE J. Quantum Electron.*, vol. 29, no.6, pp. 1817-1823, Jun. 1993.
[4] I. A. Avrutsky, D. S. Ellis, A. Tager, H. Anis, and J. M. Xu, "Design of widely tunable semiconductor lasers and the concept of binary super- imposed gratings (BSGs)," *IEEE J. Quantum Electron.*, vol. 34, no. 4, pp. 729-741, Apr. 1998.
[5] L. Ponnampalam, N. D. Whitbread, R. Barlow, Giacinto, A. J. Ward, J. P. Duck, and D. J. Robbins, "Dynamically controlled channel-to- channel switching in a full-band DS-DBR laser," *IEEE J. Quantum Electron.*, vol. 42, no. 3, pp. 223-231, Mar. 2006.
[6] M. Gioannini and I. Montrosset, "Novel interleaved sampled grating mirrors for widely tunable DBR lasers," *Proc. Inst. Elect. Eng., Opto- electron.*, vol. 148, no. 1, pp. 13-19, 2001.
[7] A. J. Ward, D. J. Robbins, D. C. J. Reid, N. D. Whitbread, G. Busico, P. J. Williams, J. P. Duck, D. Childs, and A. C. Carter, "Realization of phase grating comb reflectors and their application to widely tun- able DBR lasers," *IEEE Photon. Technol. Lett.*, vol. 16, no. 11, pp. 2427-2429, Nov. 2004.
[8] X. He, Y. Yu, D. Huang, R. Zhang, W. Liu, and S. Jiang, "Analysis and applications of reflection-spectrum envelopes for sampled gratings," *J. Lightw. Technol.*, vol. 26, no. 3, pp. 720-729, Mar. 2008.
[9] R. Zhang, L. Dong, Y. Yu, D. Wang, J. Zhang, L. Chen, and S. Jiang, "Studies on the butt-joint of a InGaAsP-waveguide realized with met- alorganic vapor phase epitaxy," *Chin. J. Semiconductors*, vol. 29, no.6, pp. 1177-1180, 2008.