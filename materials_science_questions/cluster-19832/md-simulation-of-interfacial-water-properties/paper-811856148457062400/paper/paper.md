# Hydroelectric Voltage Generation Based on Water-Filled Single-Walled Carbon Nanotubes
Quanzi Yuan and Ya-Pu Zhao*

State Key Laboratory of Nonlinear Mechanics, Institute of Mechanics, Chinese Academy of Sciences, Beijing 100190, People’s Republic of China

Received November 29, 2008; E-mail: yzhao@imech.ac.cn (Ya-Pu Zhao)

The filling structure and transfer characteristics of water confined in one-dimensional nanotubes have drawn considerable attention over the past decade because of their potential applications in the field of micro/nanoelectromechanical systems (MEMS/NEMS), biomedicine, biosensing, etc. $^{1-9}$ With the rapid development of in situ and real time nanotechnologies, nanoscale, wireless or implantable devices capable of being self-powered are highly desirable. Therefore, it is essential to explore innovative nanotechnologies for converting and collecting ambient energy into usable electric energy to power nanodevices without using a battery. Because of the polarity of water molecules, weak couplings are formed between water dipoles and free charge carriers in nanotubes $^{10,11}$ and induce voltage between two ends of a nanotube, making potential applications of the structure of a water-filled single-walled carbon nanotube (SWCNT) in the field of a nanopower cell and energy harvesting device. Král and Shapirop $^{12}$ first theoretically predicted the generation of electric current in metallic carbon nanotubes immersed in flowing liquid. They believed that the mechanism of current generation involved the momentum in the flowing liquid molecule transfering to the acoustic phonon in the nanotube as a phonon quasi-momentum, which drags the free charge carriers in the nanotube. $^{13}$ Then the flows of a variety of polar liquids over SWCNT bundles were studied experimentally by Ghosh et al. $^{14}$ They found that voltage was generated in the sample along the flowing direction. $^{10}$ Recently power converters based on deionized water-filled SWCNTs have been realized by Zhao et al. $^{15}$ They considered that this energy conversion process may be realized by the mutual coupling of water dipoles and free charge carriers present in SWCNTs. However, a fundamental understanding of the voltage generation mechanism is still lacking. In this work we give insights into the mechanism of voltage generation based on water-filled SWCNTs using the mutual iterative method of density functional theory (DFT) and molecular dynamics (MD). Our work validates this structure as a promising candidate for a synthetic nanoscale power cell and a nanopower harvesting device at the atomic level.

We first performed the MD simulation on an uncapped finite-length armchair-type (6, 6) SWCNT, which was $12.3\ \mathring{A}$ in length and $8.14\ \mathring{A}$ in diameter, to obtain the filling structure. The MD simulation domain is illustrated in Figure 1. The TIP4P water model was used to describe electric behaviors of water dipoles precisely. A constant force was imposed on a layer of bulk water molecules to simulate an osmotic pressure, pushing water molecules into the nanotube. $^{8,16,17}$ The simulations were performed for 10 ns with a 1.0 fs time step under a constant temperature of 300 K using LAMMPS. $^{18}$ The characteristic time scale for dipolar reorientation in a uncharged tube is in approximately nanoseconds, $^{19}$ while that for a single water molecule in bulk fluid is approximately in picoseconds. Therefore the simulations can fully reflect all the behaviors of the filling structure without losing any motion of the water molecule. The water molecules in the tube were pushed by the hydrogen bonds between the water molecules and formed a single-file water chain along the $z$ direction, $^{20}$ as illustrated in Figure 2b.

![](./images/811856148457062400_1.jpg)

Figure 1. Visualization of the MD simulation domain. Atoms displayed in ball-and-stick style were calculated with DFT.

Then we studied the influence of the dipole chain on the electronic performance of a nanotube. To investigate the effect of water molecules on the charge distribution of tube, we used GAUSSION03 $^{21}$ to calculate the four different transient configurations obtained from MD simulations, which consisted of an SWCNT and the water molecules inside the tube and near the tube entrance. The B3LYP method with the 6-31 g** basis was used to fully consider the interactions between the water dipoles and charge carriers in the tube. To explore the dipole moment in this system, convergence criteria for the self-consistent field (SCF) were set to be “tight”. The CHELPG scheme was used to calculate partial charges on atoms and the electrostatic potential distribution, as not to change widely with the theoretical method and basis set.

Figure 2a and b show the CHELPG charge distribution on the carbon atoms in the (6, 6) CNT without and with the confined water molecules, respectively. The charges were averaged for the atoms with the same axial position in view of the geometric symmetry. Comparing Figure 2a and b, we can find the following. First, the carbon atoms in the SWCNT acted as donors, transferred the charges to the water molecules, and made the total charges of the tube positive. Second, the water dipole chain resulted in the polarity of the SWCNT. The total charges on the left were 0.134 e and on the right were $-0.005$ e. The electrostatic potential at a certain position was calculated by integrating the SCF density in the simulation domain

$$
U_{i}=\int \frac{q(\tau)}{4 \pi \varepsilon_{0} r_{i k}} \mathrm{~d}^{3} \tau \tag{1}
$$

where $U_{i}$ is the electric potential at position $i$, $q(\tau)$ represents the charge density, $\epsilon_{0}$ is the vacuum permittivity $\epsilon_{0}=8.854 \times 10^{-12}$ F/m, and $r_{i k}$ is the distance between atom $k$ and position $i$. The voltage difference between the two ends of the tube was gained by $\Delta U=U_{\text {right }}-U_{\text {left }}=17.2 \mathrm{mV}$, which is well consistent with

![](./images/811856148457062400_2.jpg)
![](./images/811856148457062400_3.jpg)

Figure 2. Charge distribution on C atoms of (6, 6) CNT (a) without and (b) with water molecules calculated with DFT. Blue dash lines in (b) represent hydrogen bonds between water molecules. The charges were averaged for the atoms with the same axial position.

experimental observations. $^{14,15}$ Because of the symmetric boundary conditions in our calculations, the electric potential will flip if the direction of the water flow is reversed, as observed in Zhao's work. $^{15}$ This phenomenon was confirmed by our simulations, which indicated that the polar nature of water molecules is essential for the interaction between water molecules and nanotubes. Since the tube is metallic, electric current flow forms due to the voltage between the two ends of the CNT. the theoretical work predicts the resistance of the SWCNT is $R=h / e^{2} \approx 10^{4} \Omega$ , which isconfirmed by Maiti's calculations $^{22}$ that the resistance of a (6,6) SWCNT $13.5 \AA$ in length is $\sim 10^{4} \Omega$ . Hence, the electric currentflow in the tube was calculated as $I=U / R ≈17.2 mV / 10^{4} \Omega=$ 1.72 μA.

In the process of water transportation in an SWCNT, two problems disturb the voltage generation (i.e., the end effect of CNT and the flip of water dipoles). The end effect of a CNT, $^{11}$ which is visualized in Figure 2, results in the phenomenon in which the charges at the ends of the tube are much more than those in themiddle of tube. The water dipoles are affected by this end effect, $^{11}$  which makes the average water dipoles in the CNT to be almost zero, raises an L-defect, and results in no voltage difference. By using the charge distribution on the tube with water molecules subtracting that without water molecules, we can get the differential charge distribution, which is visualized in Figure 3. This differential charge distribution can approximately represent the charge distribu- tion on a long CNT without being affected by the end effect. Placing the differential charge distribution in the MD simulation, we found the water dipoles all pointed toward one end of the tube and rarely flipped due to the effect of the opposite dipoles on the tube wall induced by the water dipoles, as illustrated in Figure 4. The water chain with an unchanged orientation produced a constant voltage difference between the two ends of the tube (note the direction and voltage difference fluctuate slightly).

![](./images/811856148457062400_4.jpg)

Figure 3. Differential charge distribution of (6, 6) CNT.

![](./images/811856148457062400_5.jpg)

Figure 4. Dipole angles of water molecules in CNT with respect to simulation time. Each point is the average of water dipoles per frame. Water dipole orientation angle is defined as the angle between the water dipole vector and the tube axis z. Blue dash line at $90^{\circ}$ denotes water dipole vector pointing to the normal of the tube axis. $0^{\circ}$ denotes water dipole vector pointing along $+z$ direction.

![](./images/811856148457062400_6.jpg)

Figure 5. Dimensionless radial local water density $\rho^{*}=\rho_{c} / \rho_{b}$ , where $\rho_{c}$ is the actual density of water inside (a) uncharged (blue dash line) and (b) charged (red line) SWCNT; $\rho_{b}$ is the density of bulk water.

Until now we have two states, the water-filling structures in the uncharged and charged SWCNT. Transport properties were com- pared in three aspects (i.e., average water dipole angle, radial local water density distribution, and transfer free energy). The average water dipole angles in the uncharged and charged tubes were $37.5^{\circ}$ and $36.0^{\circ}$ , respectively. Radial local water density distributions in the uncharged and charged tube are illustrated in Figure 5. Water molecules prefer staying along the axis of the charged tube,

![](./images/811856148457062400_7.jpg)

Figure 6. Illustration of water dipoles in (a) uncharged and (b) charged SWCNT neglecting the end effect. The red dash and blue arrows denote the vectors of water dipoles and carbon dipoles, respectively.

comparing to those in the uncharged tube. The voltage between the two ends of tube induced an electric field $E=U / d \approx 10^{7} \mathrm{~V} / \mathrm{m}$. The difference between the transfer free energies in a field $E$ and in a zero field is expressed by

$$
\Delta A(E)-\Delta A(0)=-k_{\mathrm{B}} T \ln \cosh \left(\frac{N m E \cos \alpha}{k_{\mathrm{B}} T}\right) \quad(2)
$$

where $k_{\mathrm{B}}, T, N, m$, and $\alpha$ denote Boltzmann's constant, temperature, number of water molecules in the tube, water dipoles, and dipole angle, respectively. $^{23}$ Here we obtained $\Delta A \approx-10^{3} k_{\mathrm{B}} T$. Comparing these two states, we found that transportation of water molecules in an SWCNT was affected minimally by the charges in a tube. Therefore further DFT calculation is not necessary.

The highly oriented water chain, as shown in Figures $2 b$ and 4 , is responsible for the extremely high electric field in the CNT. Since the diameter of the tube is comparable to the size of a water molecule, in fact, water molecules inside the CNT cannot cross each other and they can only move in a single file. First, the nature of searching for minimum free energy results in the formation of hydrogen bonds between water molecules to gain binding energy. Hence this water-filled SWCNT structure becomes more stable. Geometric optimization $^{11}$ and MD simulations $^{24}$ validate that this oriented single-file water chain has the minimum energy. Second, the induced dipole on the CNT has a reverse orientation with the water dipole, which attracts the water chain to be oriented. This structure of a water-filled CNT is analogous to the electric double layer (EDL). The induced voltage and electric field in the tube were $17.2 \mathrm{mV}$ and $10^{7} \mathrm{~V} / \mathrm{m}$, respectively, which approached the characteristic values of EDL, $\sim 25 \mathrm{mV}$ and $10^{7} \mathrm{~V} / \mathrm{m}$, respectively.

The hydroelectric voltage generator can be expressed by the model illustrated in Figure $6 a$ and $b$. Being pushed by an external pressure into the tube, the water dipoles formed a single-file chain in the CNT, hence breaking the symmetric boundary. The charges of the CNT and water molecules interacted and redistributed. So, a voltage between the two ends of the SWCNT was induced as well as a dipole chain in the tube along the reverse flow direction. The two dipole chains were influenced reciprocally, which produced a constant direction of dipoles and a constant voltage.

A variety of factors (e.g., diameter, chirality, length of CNT, flow velocity, and defects) affect the generation of voltage. The pressure in MD was altered to investigate the influence of the flow velocity of water on voltage generation, as observed in experiments. $^{14,15}$ But the obtained voltages were nearly the same. The charge distribution in our DFT simulations was calculated at instant frame, and the obtained voltage is saturated. So, we infer the terminal voltage in experiments is the balance between the CNTconsumed voltage and water-induced voltage. The decrease of diameter, $^{25}$ the increase of the chirality angle, $^{11}$ and higher flow velocity $^{10,14,15}$ increase the interactions between water molecules and the tube. How these factors influence voltage generation needs further consideration and computations.

In summary, we have shown that voltage can be generated by the structure of water-filled SWCNT and explored the mechanism of voltage generation using the DFT/MD mutual iterative method. Our calculations showed that the end effect of the finite length CNT disturbs voltage generation and voltage can be generated in a long SWCNT, where the end effect could be neglected. It is also demonstrated that interactions between the water dipole chains and charge carriers in a tube can result in charge redistribution in an SWCNT, causing a voltage difference of $17.2 \mathrm{mV}$ between the two ends of the tube. Therefore, the structure of a water-filled SWCNT was validated at the atomic level to be a promising candidate for a synthetic nanoscale power cell, as well as a practical nanopower harvesting device.

Acknowledgment. This work was jointly supported by the National High-tech R&D Program of China (863 Program, Grant Nos. 2007AA04Z348 and 2007AA021803), National Basic Re- search Program of China (973 Program, Grant No. 2007CB310500), and National Natural Science Foundation of China (NSFC, Grant Nos. 10772180 and 10721202). We would like to express our thankfulness to the constructive comments and insightful suggestions given by two anonymous referees.

Supporting Information Available: Details of MD simulation. This material is available free of charge via the Internet at http://pubs.acs.org.

### References
(1) Mattia, D.; Gogotsi, Y. *Microfluid. Nanofluid.* **2008**, 5, 289-305.
(2) Noy, A.; Park, H. G.; Fornasiero, F.; Holt, J. K.; Grigoropoulos, C. P.; Bakajin, O. *Nano Today* **2007**, 2, 22-29.
(3) Whitby, M.; Quirke, N. *Nat. Nanotechnol.* **2007**, 2, 87-94.
(4) Fang, H. P.; Wan, R. Z.; Gong, X. J.; Lu, H. J.; Li, S. Y. *J. Phys. D: Appl. Phys.* **2008**, 41, 103002.
(5) Berezhkovskii, A.; Hummer, G. *Phys. Rev. Lett.* **2002**, 89, 064503.
(6) Liu, Y. C.; Wang, Q. *Phys. Rev. B* **2005**, 72, 085420.
(7) Gong, X. J.; Li, J. Y.; Lu, H. J.; Wan, R. Z.; Li, J. C.; Hu, J.; Fang, H. P. *Nat. Nanotechnol.* **2007**, 2, 709-712.
(8) Wan, R. Z.; Li, J. Y.; Lu, H. J.; Fang, H. P. *J. Am. Chem. Soc.* **2005**, 127,7166-7170.
(9) Won, C. Y.; Aluru, N. R. *J. Am. Chem. Soc.* **2007**, 129, 2748-2749.
(10) Ghosh, S.; Sood, A. K.; Ramaswamy, S.; Kumar, N. *Phys. Rev. B* **2004**,70,205423.
(11) Won, C. Y.; Joseph, S.; Aluru, N. R. *J. Chem. Phys.* **2006**, 125, 114701.
(12) Král, P.; Shapiro, M. *Phys. Rev. Lett.* **2001**, 86, 131.
(13) Dellago, C.; Naor, M. M.; Hummer, G. *Phys. Rev. Lett.* **2003**, 90, 105902.
(14) Ghosh, S.; Sood, A. K.; Kumar, N. *Science* **2003**, 299, 1042-1044.
(15) Zhao, Y. C.; Song, L.; Deng, K.; Liu, Z.; Zhang, Z. X.; Yang, Y. L.; Wang, C.; Yang, H. F.; Jin, A. Z.; Luo, Q.; Gu, C. Z.; Xie, S. S.; Sun, L. F. *Adv. Mater.* **2008**, 20, 1772-1776.
(16) Li, J. Y.; Gong, X. J.; Lu, H. J.; Li, D.; Fang, H. P.; Zhou, R. H. *Proc. Natl. Acad. Sci. U.S.A.* **2007**, 104, 3687-3692.
(17) Zhu, F. Q.; Tajkhorshid, E.; Schulten, K. *Biophys. J.* **2002**, 83, 154-160.
(18) Plimpton, S. *J. Comput. Phys.* **1995**, 117, 1-19.
(19) Best, R. B.; Hummer, G. *Proc. Natl. Acad. Sci. U.S.A.* **2005**, 102, 6732-6737.
(20) Thomas, J. A.; McGaughey, A. J. H. *J. Chem. Phys.* **2008**, 128, 084715.
(21) Frisch, M. J.; Trudes, G. W.; Schlegel, H. B.; Scuseria, G. E. *GAUSSIAN03, revision D.01 ed.; Gaussian, Inc.: Wallingford, CT, 2004.
(22) Maiti, A.; Svizhenko, A.; Anantram, M. P. *Phys. Rev. Lett.* **2002**, 88,126805.
(23) Vaitheeswaran, S.; Rasaiah, J. C.; Hummer, G. *J. Chem. Phys.* **2004**, 121,7955-7965.
(24) Waghe, A.; Rasaiah, J. C.; Hummer, G. *J. Chem. Phys.* **2002**, 117, 10789-10795.
(25) Meng, L.; Li, Q.; Shuai, Z. *J. Chem. Phys.* **2008**, 128, 134703.

JA8093372