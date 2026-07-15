# RESEARCH ARTICLE

## Tunable nano Peltier cooling device from geometric effects using a single graphene nanoribbon

Wan-Ju Li¹, Dao-Xin Yao²,*, E. W. Carlson¹,†

¹Department of Physics, Purdue University, West Lafayette, IN 47907, USA
²State Key Laboratory of Optoelectronic Materials and Technologies, Sun Yat-Sen University, Guangzhou 510275, China

Corresponding authors. E-mail: * yaodaoz@mail.sysu.edu.cn, † ewcarlson@purdue.edu
Received January 2, 2014; accepted February 12, 2014

Based on the phenomenon of curvature-induced doping in graphene we propose a class of Peltier cooling devices, produced by geometrical effects, without gating. We show how a graphene nanoribbon laid on an array of curved nano cylinders can be used to create a targeted and tunable cooling device. Using two different approaches, the Nonequilibrium Green's Function (NEGF) method and experimental inputs, we predict that the cooling power of such a device can approach the order of $kW/cm^2$, on par with the best known techniques using standard superlattice structures. The structure proposed here helps pave the way toward designing graphene electronics which use geometry rather than gating to control devices.

**Keywords** Peltier cooling device, graphene nanoribbon, superlattice structure, graphene electronics, cooling power, Nonequilibrium Green's Function (NEGF)

**PACS numbers** 72.15.Jf, 73.50.Lw, 72.80.Vp

As electronics become smaller, one problem facing the industry is that of targeted, on-demand cooling, conventionally achieved by semiconductor-based Peltier coolers [1–5], containing arrays of n-type and p-type pellets. However, one limitation of Peltier coolers made with conventional fabrication techniques is that carrier concentration for each pellet is set by doping level and cannot be adjusted after fabrication, which in turn results in that the cooler's cooling power cannot be dynamically changed. Therefore, new materials and novel structures are desired to fabricate a cooler with dynamically changeable cooling power.

Graphene, a two-dimensional atomic layer, is a potential candidate for a high-performance thermoelectric cooler. As a result of its unique energy spectrum, the doping level can be controlled by shifting the Fermi level either above (n-type) or below (p-type) the Dirac point. Therefore, remarkable efforts have been focused on both electrical [6–12] and chemical [13, 14] methods for fabricating graphene-based p-n junctions, which are the main constituents of a Peltier cooler. However, due to the geometry of these p-n junctions, the direction of heat transfer is parallel to the fabrication substrate. For this reason, the geometry of coolers has to be such that the p- and n-type regions are perpendicular to the surface which needs to be cooled, like a stack of books on a shelf. This extra level of manufacturing makes the devices less likely to be of use, especially in nanoscale applications.

Whereas the currently available fabrication techniques of the graphene-based p-n junction are confined to surfaces, the *three dimensional* configurations of this flexible 2D membrane may eventually be exploited to develop integrated circuits with components not achievable before. In this paper, we show how a single, continuous graphene nanoribbon (GNR) may be used to create a nanoscale Peltier array without need for lithography or gating. The key ingredients in any Peltier cooler are an array of p-n junctions which are electrically in series yet thermally in parallel, such that the junctions which evolve heat are on one side of the device, and the junctions which absorb heat are on the other. Upon application of a current from left to right through the GNR shown in Fig. 1, heat will be pumped from the junctions near the bottom of the structure to the junctions near the top. From two different methods which agree, we estimate the cooling power of the proposed device to be on the order of $kW/cm^2$.

Curvature-induced doping provides a route to creating the p-n junctions required by Peltier coolers. When the local curvature of graphene resembles that of a sphere (large mean curvature), or that of a saddle (small mean curvature), the change in orbital energies and overlap integrals associated with the curvature causes the en-

© Higher Education Press and Springer-Verlag Berlin Heidelberg 2014

RESEARCH ARTICLE

ergy spectrums and the Dirac points to shift differently in these two cases, leading to n-type or p-type doping [15]. By draping a single Armchair metallic GNR over a curved cylindrical protrusion [such as a bent nanotube may provide, see Fig. 2(b)], a region of large mean curvature is created next to a region of small mean curvature, and a p-n junction is created.

![](./images/813155164234973186_1.jpg)

Fig. 1 A single GNR laid on an array of curved nanotubes. A GNR bent into the geometry shown becomes a Peltier cooling device with cooling power $\approx 1$ kW/cm². The large mean curvature of the blue regions leads to spontaneous n-type doping, and the low mean curvature of the red regions leads to spontaneous p-type doping. Upon application of a current from left to right, heat is pumped from bottom to top. The cooling power may be adjusted by changing the curvature, via, e.g., the application of uniaxial pressure on the device.

In Fig. 1, blue regions denote areas of large mean curvature and red regions denote areas of small mean curvature. The curvature-induced Dirac-point shift is given by [15]

$$
\Phi(\boldsymbol{x})=-3 \alpha a^{2}(H(\boldsymbol{x}))^{2} \tag{1}
$$

$H(\boldsymbol{x})$ is the mean curvature of the surface at the point $\boldsymbol{x}$,

$$
H=\frac{1}{2}\left(\frac{1}{r_{1}}+\frac{1}{r_{2}}\right) \tag{2}
$$

where $r_1$ and $r_2$ are the principal radii of curvature at the point $\boldsymbol{x}$, $a$ is the nearest-neighbor distance, $a=2.5$ Å, and $\alpha \sim 9.23$ eV. In our proposed device, see Fig. 2(a), $r_1=R_2$ and $r_2=r$ for the outer surface while $r_1=R_1$ and $r_2=r$ for the inner surface. Because the Dirac-point shift depends on the square of $H$ [15], it is independent of the coordinate system. The Dirac points in the regions with a larger magnitude of the mean curvature (locally like a sphere) are lowered more while the Dirac points in the regions with smaller magnitude of the mean curvature (regions which are flat, or alternatively which are saddle-like) are lowered less. This effect implies that regions with large magnitude of the mean curvature are locally electron-doped, while the regions with small magnitude of the mean curvature are locally hole-doped.

![](./images/813155164234973186_2.jpg)

Fig. 2 (a) Creating two curvatures by bending. Two curvature radii with equal signs results in large mean curvature while two radii with different signs results in small mean curvature. $R_1$ and $r$ are the two radii for the inner side and $R_2$ and $r$ are for the outer side of the tube. (b) A schematic illustration of making our proposed nanocooler. At first, a GNR is put on the surface of a insulating nanotube. Secondly, curvatures are introduced on the GNR by bending the nanotube. The curving angle $\theta_x$ ($\theta_y$) defined by $L_x$ and $R_1$ ($L_y$ and $r$).

The optimal cooling power $P_m$ for one Peltier cooling element can be derived from the rate of heat absorption [16]

$$
P_{m}=K\left(\frac{1}{2} Z T_{C}^{2}-\Delta T\right)=\frac{(\Delta S)^{2} T_{C}^{2}}{2 R}-K \Delta T \tag{3}
$$

where $\Delta T=T_H-T_C$ is the temperature difference between the two heat reservoirs, $\Delta S=S_p-S_n$, is the difference between Seebeck coefficients in the p-doped (with smaller mean curvature) and n-doped (with larger mean curvature) regions, and $Z=(\Delta S)^2/(KR)$, the figure of merit of the p-n junction. $K$ and $R$ are the thermal conductance and electric resistance, respectively, of the p-n junction. When electrical current equal to $I=I_{opt}=(\Delta S)T_C/R$ is driven through one Peltier cooling element, the optimal cooling power $P_m$ is reached.

In the following, we use two approaches to estimate the cooling power of our proposed device under the condition that $\Delta T=T_H-T_C=0$. For the first approach, we use Nonequilibrium Green's Function (NEGF) method to perform calculations from the atomic scale. For the second approach, we estimate the cooling power from experimental measurements of the Seebeck coefficient [17]. Results from these two approaches are similar.

The NEGF method can be used to calculate the transmission coefficient $T_0(E)$ for a perfect GNR from the atomic scale [18]. The system contains one channel and two contacts. The Green's function $G$ for the transport channel is defined as

$$
G=\left[(E+\mathrm{i} \eta) I-H-\Sigma_{1}-\Sigma_{2}\right]^{-1} \tag{4}
$$

where $E$ is the incident energy of electrons, $I$ is the identity matrix with the same dimension as that of the channel Hamiltonian $H$, $\eta$ is a small number accounting for

---

Wan-Ju Li, Dao-Xin Yao, and E. W. Carlson, Front. Phys.

RESEARCH ARTICLE

the energy level broadening, and $\Sigma_1$ and $\Sigma_2$ represent the effects from two contacts. In order to describe the tunnelling processes between the channel and two contacts, two functions, $\Gamma_1$ and $\Gamma_2$, are introduced for two contacts respectively,
$$
\Gamma_{1}=\mathrm{i}\left[\Sigma_{1}-\Sigma_{1}^{+}\right] ; \quad \Gamma_{2}=\mathrm{i}\left[\Sigma_{2}-\Sigma_{2}^{+}\right]
\tag{5}
$$

The transmission coefficient for a perfect GNR is then given as [18]
$$
T_{0}(E)=\operatorname{Trace}\left[\Gamma_{1} G \Gamma_{2} G^{+}\right]
\tag{6}
$$

In real systems, scattering processes have to be taken into account. The electron–electron interaction usually causes phase relaxation, which destroys the coherence of the electronic wave functions. The electron–phonon interaction and the electron–impurity interaction result in backscattering and momentum relaxation processes. For high voltage bias between two contacts, effects from inelastic scatterings are also involved. Dominant scattering processes are determined by the physical system under consideration.

Under usual experimental conditions, where the voltage bias is small and the whole system is in the linear response regime, there is a way to take elastic scattering effects into account within NEGF. For quantum transport, it is well known that the transmission coefficient $T(E)$ can be related to its ballistic limit counterpart $T_0(E)$ in the following way [18],
$$
T(E)=\frac{\lambda}{\lambda+L} T_{0}(E)
\tag{7}
$$
where $L$ is the system size along the transport direction and $\lambda$ is the backscattering mean-free path and is assumed to depend only on disorder and not on the incident energy $E$. Therefore, once $T_0(E)$ is obtained, it is straightforward to calculate $T(E)$. For this paper, calculations of the the transmission coefficient are based on the GNR system with $L_x=75$ nm, $L_y=25$ nm, and $\lambda=400$ nm.

After obtaining $T(E)$ we can calculate the Seebeck coefficient $S$ and the electrical conductance $g$. An intermediate function $L_n$ is defined as [19]
$$
L_{n}(\mu, T)=\frac{2}{h} \int \mathrm{d} E T(E)(E-\mu)^{n}\left(-\frac{\partial f(E, \mu, T)}{\partial E}\right)
\tag{8}
$$
where $h$ is the Plank constant, and $f$ is the Fermi distribution function. Based on these intermediate functions, $g$ and $S$ can be computed as
$$
g(\mu)=e^{2} L_{0}(\mu, T)
\tag{9}
$$

$$
S(\mu)=\frac{1}{e T} \frac{L_{1}(\mu, T)}{L_{0}(\mu, T)}
\tag{10}
$$
where $e$ is the electron charge, $\mu$ is the chemical potential and $T$ is the average temperature. In Fig. 3, we show the electric conductance and the Seebeck coefficient at $T=300$ K as functions of the on-site voltage for clean and disorder cases. We find that the electrical conductance of the clean case is slightly larger than that of the disordered case while the Seebeck coefficient behaves similarly in both cases. We furthermore find that the maximum of the Seebeck coefficient is on the order of $100\ \mu\text{V/K}$, consistent with the experimental measurements for Graphene [17].

![](./images/813155164234973186_3.jpg)

Fig. 3 The sample size is that $L_x=75$ nm, $L_y=25$ nm and $T=300$ K. (a) The electric conductance for the perfect GNR. (b) The electric conductance for the disordered GNR with $\lambda=400$ nm. (c) The Seebeck coefficient as a function of gate voltage for the perfect GNR. (d) The Seebeck coefficient as a function of gate voltage for the disordered GNR with $\lambda=400$ nm.

The cooling power $P$ of our proposed device can be evaluated using the calculated Seebeck coefficient and electrical conductance with disorder. When the surface of a GNR is curved, Dirac points for different regions are shifted up or down, similar to applying a gate voltage. Therefore, the calculated Seebeck coefficient as a function of on-site voltage can be used as the Seebeck coefficients for different Dirac-point shifts caused by the curvatures. Combined with the calculated electric conductance, the cooling power can be calculated by using Eq. (3) with $\Delta T=0$.

In Fig. 4, we show the cooling power as a function of two curvature radii $R=R_1$ and $r$, where $R=L_x/\theta_x$, $r=L_y/\theta_y$, $T=300$ K, and the distance between two nano tubes $d=15$ nm. $L_x$ and $L_y$ are fixed and $0<\theta_x,\theta_y<\pi$. Therefore $R$ and $r$ have lower limits $L_x/\pi$ and $L_y/\pi$, respectively. As we expect, the maximum cooling power takes place for small $R$ and $r$, which is on the order of $\text{kW/cm}^2$. As an example, if we take as inputs $L_x=75$ nm $=\theta_x R$, $L_y=25$ nm $=\pi r$,

Wan-Ju Li, Dao-Xin Yao, and E. W. Carlson, Front. Phys.

and $\theta_x = \pi/2$, then the corresponding Dirac-point shifts for the inner side $(\Phi_1)$ and outer side $(\Phi_2)$ can be obtained after considering charge neutrality: $\Phi_1 \approx 1.96$ mV, and $\Phi_2 \approx -1.96$ mV. By using the calculated Seebeck coefficient and the electrical conductance [Figs. 3(d) and (b), respectively], we find that the cooling power is $0.3$ kW/cm$^2$. When the cooling device is curved more, $\theta_x = 2\pi/3$, the cooling power can be estimated in a similar way to be $0.5$ kW/cm$^2$. This shows that the cooling power can be tuned by changing the curvature of the device, for example, by applying uniaxial pressure.

![](./images/813155164234973186_4.jpg)

Fig. 4 The cooling power as a function of two curvature radii for the GNR with $L_x = 75$ nm, $L_y = 25$ nm, and $\lambda = 400$ nm, which is from NEGF calculations.

We now use an entirely different approach to estimate the cooling power of our proposed device, in which the Seebeck coefficients are taken directly from experimental measurements [Fig. 3(b)]. Given the applied gate voltage $V_g$, the resulting Dirac-point shift of the Graphene sample $V_r$ can be derived as [20]
$$
V_r = \frac{\hbar v_F}{e} \sqrt{\frac{\epsilon_0 \epsilon \pi}{t e}} \sqrt{V_g} \tag{11}
$$
where $t$ is the thickness of the $S_iO_2$ substrate, $v_F$ is the Fermi velocity of graphene, and $\epsilon_0$ and $\epsilon$ are the permittivities of free space and $S_iO_2$, respectively. By using experimentally determined Seebeck coefficient [17] and electrical conductivity [20], the cooling power can be similarly estimated from Eq. (3).

In Fig. 5, we report the cooling power as functions of the two curvature radii $r$ and $R$ as we do for the first approach. Results are consistent with that from the first approach, which is on the order of kW/cm$^2$. As an example, if we take as inputs $L_x = 75$ nm $= \theta_x R$, $L_y = 25$ nm $= \pi r$, and $\theta_x = \pi/2$, then the corresponding Dirac-point shifts for the inner side $(\Phi_1)$ and outer side $(\Phi_2)$ can be obtained: $\Phi_1 \approx 1.96$ mV, and $\Phi_2 \approx -1.96$ mV. This corresponds to applied gate voltages of $\Phi_{1g} \approx 1.38$ V, and $\Phi_{2g} \approx -1.38$ V. Given these two gate voltages, the Seebeck coefficients in both the n-type and p-type regions [17] can be obtained. Combined with experimental data for the electric conductance $(10^6 \frac{1}{\Omega - m}$, corresponding to the mobility $10^4 \frac{\text{cm}^2}{\text{V-S}})$, the cooling power $P$ can be estimated to be $P \approx 0.57$ kW/cm$^2$. When the cooling device is curved more, $\theta_x = 2\pi/3$, from similar calculations, the cooling power is obtained to be $\approx 0.9$ kW/cm$^2$. This result again shows that we can tune the cooling power by bending the nanotubes through, e.g., applying uniaxial pressure.

![](./images/813155164234973186_5.jpg)

Fig. 5 The cooling power as a function of two curvature radii, $R$ and $r$ for a GNR with $L_x = 75$ nm, $L_y = 25$ nm. The calculation is performed by using the experimental input [17].

In conclusion, we have proposed a graphene-based nano mechanical cooling device and estimated its cooling power using two different approaches: the NEGF method and experimental inputs. As a result of geometry alone, a series of P-N junctions are created in the proposed device such that by applying electric current, heat can be pumped perpendicular to the surface of the substrate. We find $P \sim 0.5$ kW/cm$^2$, close to that achievable with the best cooling devices $\sim 1$kW/cm$^2$. Most importantly, the cooling power of the proposed device can be adjusted by changing the curvatures, via, e.g., applying uniaxial pressure to the device.

Acknowledgements It is a pleasure to thank Y. Chen, E.-A. Kim, and Y. L. Loh for conversations. W. J. Li would like to thank Vinh Quang Diep and Seokmin Hong for many useful discussions. W. J. Li, D. X. Yao, and E. W. Carlson acknowledge support from Research Corporation for Science Advancement and NSF Grant No. DMR 11-06187. W. J. Li acknowledges support from the Purdue Research Foundation. D. X. Yao acknowledges support from the National Basic Research Program of China (No. 2012CB821400), the National Natural Science Foundation of China (Grant Nos. 11074310 and 11275279), Research Fund for the Doctoral Program of Higher Education of China (20110171110026), and NCET-11-0547. EWC thanks École Supérieure de Physique et de Chimie Industrielles (ESPCI) for hospitality.

### References
1. G. H. Zeng, X. F. Fan, C. LaBounty, E. Croke, Y. Zhang, J. Wan-Ju Li, Dao-Xin Yao, and E. W. Carlson, *Front. Phys*.

Christofferson, D. Vashaee, A. Shakouri, and J. E. Bowers,
Cooling power density of SiGe/Si superlattice micro refriger-
ators, Volume 793 of Materials Research Society Symposium
Proceedings, Materials Research Society, 2004

2. I. Chowdhury, R. Prasher, K. Lofgreen, G. Chrysler, S.
Narasimhan, R. Mahajan, D. Koester, R. Alley, and R.
Venkatasubramanian, On-chip cooling by superlattice-based
thin-film thermoelectrics, *Nat. Nanotechnol.*, 2009, 4(4):

3. X. Fan, G. Zeng, E. Croke, C. LaBounty, C. C. Ahn, D.
Vashaee, A. Shakouri, and J. E. Bowers, High cooling power
density SiGe/Si micro-coolers, *Electron. Lett.*, 2001, 37(2):

4. A. Shakouri and Yan Zhang, On-chip solid-state cooling for
integrated circuits using thin-film microrefrigerators, *IEEE
Trans. Compon. Packag. Tech.*, 2005, 28(1): 65

5. J. Zhang, N. G. Anderson, and K. M. Lau, AlGaAs super-
lattice microcoolers, *Appl. Phys. Lett.*, 2003, 83(2): 374

6. H. Y. Chiu, V. Perebeinos, Y. M. Lin, and P. Avouris, Con-
trollable p-n junction formation in monolayer graphene using
electrostatic substrate engineering, *Nano Lett.*, 2010, 10(11):

7. G. Liu, J. Velasco, and W. Bao, and C. N. Lau, Fabrica-
tion of graphene p-n-p junctions with contactless top gates.,
*Appl. Phys. Lett.*, 2008, 92(20): 203103

8. S. G. Nam, D. K. Ki, J. W. Park, Y. Kim, J. S. Kim, and H.
J. Lee, Ballistic transport of graphene p-n-p junctions with
embedded local gates, *Nanotechnology*, 2011, 22(41): 415203

9. B. Öyilmaz, P. Jarillo-Herrero, D. Efetov, D. Abanin, L.
Levitov, and P. Kim, Electronic transport and quantum Hall
effect in bipolar graphene p-n-p junctions, *Phys. Rev. Lett.*,
2007, 99(16): 166804

10. G. Rao, M. Freitag, H. Y. Chiu, R. S. Sundaram, and
P. Avouris, Raman and photocurrent imaging of electrical
stress-induced p-n junctions in graphene, *ACS Nano*, 2011,
5(7): 5848

11. J. R. Williams, L. DiCarlo, and C. M. Marcus, Quantum
Hall effect in a gate-controlled p-n junction of graphene, *Sci-
ence*, 2007, 317(5838): 638

12. T. Yu, C. W. Liang, C. Kim, and B. Yu, Local electrical
stress-induced doping and formation of monolayer graphene
P-N junction, *Appl. Phys. Lett.*, 2011, 98(24): 243105

13. H. C. Cheng, R. J. Shiue, C. C. Tsai, W. H. Wang, and
Y. T. Chen, High-quality graphene p-n junctions via resist-
free fabrication and solution-based noncovalent functional-
ization, *ACS Nano*, 2011, 5(3): 2051

14. T. Lohmann, K. von Klitzing, and J. H. Smet, Four-terminal
magneto-transport in graphene p-n junctions created by spa-
tially selective doping, *Nano Lett.*, 2009, 9(5): 1973

15. E. A. Kim and A. H. Castro Neto, Graphene as an electronic
membrane, *Europhys. Lett.*, 2008, 84(5): 57007

16. D. Rowe, Thermoelectrics Handbook: Macro to Nano, Boca
Raton: CRC/Taylor and Francis, 2006

17. P. Wei, W. Z. Bao, Y. Pu, C. N. Lau, and J. Shi, Anoma-
lous thermoelectric transport of Dirac particles in graphene,
*Phys. Rev. Lett.*, 2009, 102(16): 166808

18. S. Datta, Quantum Transport: Atom to transistor, Cam-
bridge: Cambridge University Press, 2005

19. Y. Ouyang and J. Guo, A theoretical study on thermoelec-
tric properties of graphene nanoribbons, *Appl. Phys. Lett.*,
2009, 94(26): 263107

20. K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, Y.
Zhang, S. V. Dubonos, I. V. Grigorieva, and A. A. Firsov,
Electric field effect in atomically thin carbon films, *Science*,
2004, 306(5696): 666