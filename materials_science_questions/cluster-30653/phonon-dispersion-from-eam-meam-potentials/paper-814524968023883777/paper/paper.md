# Comparative Study on Two Melting Simulation Methods: Melting Curve of Gold

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2016 Commun. Theor. Phys. 65 613

(http://iopscience.iop.org/0253-6102/65/5/613)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 131.247.112.3
This content was downloaded on 22/07/2016 at 14:17

Please note that terms and conditions apply.

# Comparative Study on Two Melting Simulation Methods: Melting Curve of Gold*

Zhong-Li Liu (刘中利),$^{1,\dagger}$ Jun-Sheng Sun (孙俊生),$^{2}$ Rui Li (李瑞),$^{1}$ Xiu-Lu Zhang (张修路),$^{3}$
and Ling-Cang Cai (蔡灵仓)$^{4}$

$^{1}$College of Physics and Electric Information, Luoyang Normal University, Luoyang 471022, China
$^{2}$The Unit 63615 of People's Liberation Army, Kuerle 841001, China
$^{3}$Laboratory for Extreme Conditions Matter Properties, Southwest University of Science and Technology, Mianyang 621010, China
$^{4}$Laboratory for Shock Wave and Detonation Physics Research, Institute of Fluid Physics, P.O. Box 919-102, Mianyang 621900, China

(Received January 4, 2016; revised manuscript received February 19, 2016)

**Abstract** Melting simulation methods are of crucial importance to determining melting temperature of materials efficiently. A high-efficiency melting simulation method saves much simulation time and computational resources. To compare the efficiency of our newly developed shock melting (SM) method with that of the well-established two-phase (TP) method, we calculate the high-pressure melting curve of Au using the two methods based on the optimally selected interatomic potentials. Although we only use 640 atoms to determine the melting temperature of Au in the SM method, the resulting melting curve accords very well with the results from the TP method using much more atoms. Thus, this shows that a much smaller system size in SM method can still achieve a fully converged melting curve compared with the TP method, implying the robustness and efficiency of the SM method.

PACS numbers: 64.60.-i, 81.40.Vw, 64.70.Dv, 02.70.Ns

Key words: solid-liquid transition, high-pressure, molecular dynamics, shock wave

## 1 Introduction

Melting is very common in nature and industrial processes. While, the nature of melting and the melting law still remain not very clear till now, especially at high pressure. Many melting simulation techniques have been developed to uncover the melting law that materials obey at specific conditions. The most accurate method of all is the frequently used two-phase (TP) method.$^{[1]}$

Gold is the noblest of all metals and has been widely used in daily life and industrial production throughout the whole history of human being. The recent reports$^{[2-3]}$ indicated that Au is not "noble" in that it undergeos solid structural transitions under extreme compression and heating. Furthermore, it melts when temperature goes beyond its melting temperatures at different pressures. These place natural constraints on Au used as a popular pressure calibrator in the high-pressure experiments, e.g., the diamond anvil cell (DAC) experiment.

At ambient conditions, Au exists stably in face-centered-cubic (fcc) structure. The DAC experiment$^{[2]}$ and theoretical calculations$^{[3-5]}$ discovered the structural phase transitions of Au under extreme compression. The earliest theoretical study indicated that Au transits from fcc to the hexagonal-close-packed (hcp) structure at 241 GPa.$^{[4]}$ But this was argued that fcc-hcp transition is at 151 GPa and the transition of hcp-bcc is at 400 GPa.$^{[5]}$ Recently, we reported the whole solid phase diagram of Au up to 550 GPa.$^{[6]}$ We found that Au transits from fcc to double hcp (dhcp) at 231.6 GPa, and transits to the hcp at 447.8 GPa at further compression.$^{[6]}$ However, the high-pressure melting curve is still absent up to now. As the melting curve presents a natural up-limit of temperature of Au as a pressure calibrator, we here have a detailed study on the high-pressure melting curve of Au using our recently developed shock melting (SM) method$^{[7]}$ and the popular TP method to have a crosscheck. Meanwhile, the results from the two method are also compared and the SM method is found to be very efficient and time-saving.

The rest of the paper is organized as follows. In Sec. 2, we describe the details of computational method. The results and discussion are presented in Sec. 3. Section 4 is a short summary of the conclusions.

## 2 Computational Method

### 2.1 Interatomic Potential

To select most accurate interatomic potential for bulk Au, we test four types of potentials to find which is the most appropriate one to describe the melting properties of Au at high pressure and high temperature. The first type is the embedded-atom-method (EAM) potential$^{[8]}$ devel-

---

*Supported by the National Natural Science Foundation of China under Grant No. 41574076 and the NSAF of China under Grant No. U1230201/A06, and the Young Core Teacher Scheme of Henan Province under Grant No. 2014GGJS-108

$^\dagger$E-mail: zl.liu@163.com

© 2016 Chinese Physical Society and IOP Publishing Ltd

http://www.iopscience.iop.org/ctp http://ctp.itp.ac.cn

oped by Adams *et al.* (Adams-EAM).$^{[9]}$ Within the EAM formalism, the total potential energy $E_{\text{tot}}$ of a metal system containing $N$ equal atoms can be written as a sum of the embedding energy $F$ and a pair potential $\phi$,

$$
E_{\text{tot}} = \sum_{i}^{N} F_{i}(\rho_{i}) + \frac{1}{2} \sum_{i}^{N} \sum_{j<i}^{N} \phi(r_{ij}) , \tag{1}
$$

where $r_{ij}$ is the distance between the atoms $i$ and $j$. The function $F_{i}(\rho_{i})$ is the energy to embed the atom $i$ into the background electron density $\rho_{i}$, which is the superposition of the atomic densities,

$$
\rho_{i} = \sum_{i \neq j}^{N} \rho_{i}(r_{ij}) . \tag{2}
$$

Other EAM potentials are the ones developed by Grochola *et al.* (Grochola-EAM),$^{[10]}$ Zhou *et al.* (Zhou-EAM),$^{[11]}$ and by Sheng *et al.* (Sheng-EAM).$^{[12]}$

![](./images/814524968023883777_1.jpg)

Fig. 1 The calculated 300 K isothermal curves of Au using the classical potentials,$^{[9-12]}$ in comparison with experimental data.$^{[16-18]}$

![](./images/814524968023883777_2.jpg)

Fig. 2 The calculated thermal expansion curves for both solid and liquid Au along with the experimental data.$^{[19-20]}$

In order to assess the four potentials, we achieved the 300 K isothermal compressive curves of Au from 0 to 400 GPa. All the classical MD simulations were conducted with the large-scale atomic/molecular massively parallel simulator (LAMMPS)$^{[13-15]}$ package. The simulation supercells contained 2,048 atoms located in the face-centered-cubic (fcc) crystal lattice sites. The calculated results are compared with the experimental data$^{[16-18]}$ in Fig. 1. It is clear that the Adams-EAM potential provides the best descriptions of the compressibility of bulk Au.

As for its thermal expansion properties at high temperature, we also obtained the isobar curves at 0 GPa from 0 to 2,000 K. The isobar curves of Au are presented in Fig. 2, in comparison with the experimental data. The Adams-EAM potential has also produced the best agreement of the thermal expansion properties for both solid and liquid Au with the experimental data.$^{[19-20]}$ Hence, the Adams-EAM potential was used to calculate the high-pressure melting curve of Au.

### 2.2 The Details of the Two-Phase Method

In order to crosscheck the results and compare the efficiencies, we calculate the melting curve of Au using the TP method$^{[21]}$ and the SM method.$^{[7]}$ In the TP simulations, we build an initial configuration with a solid-liquid interface (Fig. 3). The supercell contained 20,736 atoms which can ensure the full convergency of the melting temperature. Initially, we heat the whole supercell to the temperature slightly lower than the melting temperature. Then, the coexistence configuration is built by heating one half of the supercell to melt for 50 ps and keeping the other half at its initial temperature in the NPT ensemble. At this fixed pressure, the supercell with the coexistence configuration is heated to a trial temperature for 50 ps. By monitoring the motion direction of the interface, we can decide whether this trial temperature is higher or lower than the real melting temperature, at which the interface should be motionless. Then by narrowing the temperature range, we obtain the melting temperature. All the simulations of TP method are performed in the NPT ensemble. The trial temperature interval is 50 K and the total simulation time is 50 ps with the time step of 1 fs. Thus, the melting temperature deviations are limited within 25 K. More detailed description of the TP method is referred to our previous work.$^{[7,22-23]}$

![](./images/814524968023883777_3.jpg)

Fig. 3 The initial solid and liquid coexistence configuration of Au for two-phase simulations.

### 2.3 The Details of the Shock Melting Method

In the SM simulations, we only use 640 atoms, which are much fewer than those in the TP method. The SM method is based on the multi-scale shock technique (MSST).$^{[24]}$ The shock loading is performed to

drive the simulated system to the final Hugoniot end state iteratively. $^{[7]}$ The propagation of the shock wave is modeled using the 1D Euler equations for compressible flow. $^{[7,24]}$ Shocking a sample with the shock velocity $U$, the MSST $^{[24]}$ keeps it on both the Rayleigh line,
$$
p-p_{0}=U^{2}\left(1-\rho_{0} / \rho\right) / \rho_{0}, \tag{3}
$$
and the shock Hugoniot state,
$$
U-U_{0}=\frac{1}{2}\left(p+p_{0}\right)\left(V_{0}-V\right), \tag{4}
$$
by applying a uniaxial strain of the computational cell. In the MSST simulation, with the conservation of mass, momentum, and energy, the Hugoniot end state of the simulated system is achieved by adjusting its volume and temperature iteratively. The final Hugoniot state is proved to be consistent with that of the non-equilibrium molecular dynamics (NEMD) simulation. $^{[7,24]}$ It is interesting that the simulated system size and the simulation time can be substantially reduced to about several hundred atoms and dozens of ps, respectively. $^{[7,24]}$ So if one does not care about the detailed shock loading process, the MSST can save much computational cost and achieve the same final shock end states. The periodic boundary condition was used for the atoms in the simulation box. The applied fictitious box mass of $3.6 \times 10^{5} m_{e}$ guaranteed volume compression on the timescale of 100 fs to 1 ps. The length of time step and the total number of time steps are tested to be 1 fs and $5 \times 10^{4}$, respectively. The shocking direction is along $x$ direction, i.e., the [100] direction of the fcc lattice. The sample is shocked using different shock velocities with larger interval, e.g., 0.5 km/s. Then we find the sharp drop of temperature in PT plot and the corresponding shock velocity range, and in this range we shock the sample with much finer shock velocity differences, i.e., much smaller interval, typically 0.02 km/s. More detailed description of the SM method is referred to our previous work. $^{[7]}$

## 3 Results and Discussions
According to the superheating systematics, $^{[25]}$ the lower corner point of the "Z" shaped curve in P-T plot (Fig. 4) is the crosspoint of the equilibrium and non-equilibrium melting curves. Thus, the melting temperature and the corresponding pressure can be determined from this point. If we vary the initial P-T states before shock, we will obtain different shocked P-T lines, which are located in the off-Hugoniot states. $^{[7]}$ Each line has a sharp drop in temperature when shocked to melt, but the melting temperature and pressure (the lower corner point of the "Z" curve) are different from others. The whole melting curve can be determined from the shocked P-T curves starting from different initial states, $^{[7]}$ as shown in Fig. 4.

![](./images/814524968023883777_4.jpg)

Fig. 4 The Hugoniot (black line) and off-Hugoniot PT curves of Au obtained with 640 atoms from various initial temperatures and 0 GPa or various initial pressures and 300 K. The red line is the final melting curve.

![](./images/814524968023883777_5.jpg)

Fig. 5 High-pressure melting of Au. Red solid circles are melting data from the TP method, and black diamonds are the data from the SM method, with the corresponding Simon fitting lines. The up triangles are experimental melting data from Ref. [26].

The resulting melting curves from the two methods are plotted in Fig. 5. Although there were only 640 atoms used in our SM simulations, the SM method reproduced an identical melting curve with our TP method using 20,736 atoms. The Simon equation,
$$
T_{m}=T_{m 0}\left(\frac{P}{a}+1\right)^{b}, \tag{5}
$$
was fitted to the melting temperatures and pressures. After fitting, the melting curve of Au can be written as the Simon equation,
$$
T_{m}=1250.0\left(\frac{P}{28.25}+1\right)^{0.59}, \tag{6}
$$
for the TP results, and
$$
T_{m}=1250.0\left(\frac{P}{22.97}+1\right)^{0.55}, \tag{7}
$$
for the SM results. The fitting uncertainties of the parameters $a$ and $b$ in the Simon equation are shown in Table 1, from which we see that $a$ and $b$ vary slightly in fitting.

Table 1 The fitted values and their uncertainties of the parameters of Simon equation for the melting data.

| Method | $a$   | $b$   | $\Delta a$ | $\Delta b$ |
|--------|-------|-------|------------|------------|
| TP     | 28.25 | 0.59  | 1.25       | 0.01       |
| SM     | 22.97 | 0.55  | 1.41       | 0.01       |

From this comparison, it is easily seen that the SM method is indeed a cheap and accurate strategy for the computation of melting curve with the help of molecular dynamics. Moreover, the resulting melting curve is in good accordance with the experimental data.$^{[26]}$

It was previously pointed out that the simulated system sizes and the simulation time in the MSST simulations can be substantially reduced.$^{[24]}$ Nevertheless, the MSST achieves the same final shock end states as the large-scale shock simulations in the nonequilibrium molecular dynamics and saves much computational cost. Thermodynamically, the SM and the TP methods describe the same melting sates and yield equivalent melting temperature, despite that the SM method reproduces the Hugoniot PT states. It is not surprising that our SM melting data of Au and Cu$^{[7]}$ from much smaller simulation systems accords well with the TP melting data.

In this work, we once again see that the SM method is so economic and efficient that it can be widely used in the melting temperature determination via molecular dynamics in future.

## 4 Conclusion
In conclusion, we compared the efficiency of our newly developed melting simulation method, the SM method, with that of the well-established TP method by calculating the high-pressure melting curve of gold. Firstly, we optimally selected the best interatomic potential of metal gold from the ever-developed potentials. By the tests of thermal expansion properties and the isothermal compression properties, we found that the Adams-EAM potential is the most accurate for describing the high-pressure and high-temperature properties of gold. Then, we used only 640 atoms to determine the high-pressure melting curve of Au in the SM method and achieved an almost identical melting curve as the TP method using 20,736 atoms. The economy in the calculation of the high-pressure melting curve of Au indicates that the SM method is indeed a very efficient method that can be widely used in melting temperature calculation in future.

## Acknowledgments
The authors thank the support by the high-performance computing platform of Luoyang Normal University.

## References
[1] A.B. Belonoshko, Geoch. Cosm. Acta **58** (1994) 4039.
[2] L. Dubrovinsky, N. Dubrovinskaia, W.A. Crichton, *et al.*, Phys. Rev. Lett. **98** (2007) 045503.
[3] T. Ishikawa, K. Kato, M. Nomura, N. Suzuki, H. Nagara, and K. Shimizu, Phys. Rev. B **88** (2013) 214110.
[4] R. Ahuja, S. Rekhi, and B. Johansson, Phys. Rev. B **63** (2001) 212101.
[5] P. Söderlind, Phys. Rev. B **66** (2002) 176201.
[6] Z.L. Liu, Y.P. Tao, X.L. Zhang, and L.C. Cai, Comput. Mater. Sci. **114** (2016) 72.
[7] Z.L. Liu, X.L. Zhang, and L.C. Cai, J. Chem. Phys. **143** (2015) 114101.
[8] S.M. Foiles, M.I. Baskes, and M.S. Daw, Phys. Rev. B **33** (1986) 7983.
[9] J.B. Adams, S.M. Foiles, and W.G. Wolfer, J. Mater. Res. **4** (1989) 102.
[10] G. Grochola, S.P. Russo, and I.K. Snook, J. Chem. Phys. **123** (2005) 204719.
[11] X.W. Zhou, R.A. Johnson, and H.N.G. Wadley, Phys. Rev. B **69** (2004) 144113.
[12] H.W. Sheng, M.J. Kramer, A. Cadien, T. Fujita, and M.W. Chen, Phys. Rev. B **83** (2011) 134118.
[13] S.J. Plimpton, J. Comp. Phys. **117** (1995) 1.
[14] A.P. Thompson, S.J. Plimton, and W. Mattson, J. Chem. Phys. **131** (2009) 154107.
[15] http://lammps.sandia.gov/index.html.
[16] D. L. Heinz and R. Jeanloz, J. Appl. Phys. **55** (1984) 885.
[17] P. Bell, J. Xu, and H. Mao, *Shock Waves in Condensed Matter*, Plenum, New York (1986).
[18] K. Takemura and A. Dewaele, Phys. Rev. B **78** (2008) 104119.
[19] Y.S. Touloukian, R.K. Kirby, R.E. Taylor, and T.Y.R. Lee, *Thermophysical Properties of Matter*, IFI/Plenum, New York (1977).
[20] W.B. Pearson, *A Handbook of Lattice Spacings and Structures of Metals and Alloys*, Pergamon, Oxford (1967).
[21] J.R. Morris, C.Z. Wang, K.M. Ho, and C.T. Chan, Phys. Rev. B **49** (1994) 3109.
[22] Z.L. Liu, L.C. Cai, X.R. Chen, and F.Q. Jing, Phys. Rev. B **77** (2008) 24103.
[23] Z.L. Liu, J.H. Yang, L.C. Cai, F.Q. Jing, and D. Alfè, Phys. Rev. B **83** (2011) 144113.
[24] E.J. Reed, L.E. Fried, and J.D. Joannopoulos, Phys. Rev. Lett. **90** (2003) 235503.
[25] S.N. Luo and T.J. Ahrens, Phys. Earth Planet. Int. **143–144** (2004) 369.
[26] D. Errandonea, J. Appl. Phys. **108** (2010) 33517.