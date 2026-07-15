Journal of the Physical Society of Japan
Vol. 70, No. 9, September, 2001, pp. 2593-2597

# Pressure-Controlled Tight-Binding Molecular Dynamics Simulation of Carbon Nanotubes

Takanori ITO\*, Kazume NISHIDATE, Mamoru BABA and Masayuki HASEGAWA

Faculty of Engineering, Iwate University, Morioka 020-8551

(Received October 30, 2000)

Properties of (10, 10) single-walled carbon nanotubes under uniaxial pressure are investigated by means of pressure-controlled molecular dynamics simulations using an order-$N$ tight-binding method. We use an extended Andersen method in order to control pressure of system. This scheme allows us to investigate the pressure-dependence of structural stability as a function of time in the presence of many-body quantum mechanical effect. At small strains, the potential energy of the carbon nanotube increases in accordance with the Hooke's law. In this elastic regime, the carbon nanotube keeps straight as a whole. The finite temperature effects on the strains are analyzed.

KEYWORDS: carbon nanotube, tight-binding molecular dynamics, uniaxial pressure

## §1. Introduction

Carbon nanotube is a completely new material discovered as a by-product of the study for the fullerene molecule$^{1)}$ and has attracted great attention from viewpoint of its perceived novel structural and electronic properties in many fields of science and technology. They have the quasi one-dimensional structure formed by rolling up a two-dimensional graphite sheet cylindrically and are uniquely characterized by chiral index $(n, m)$, where $n$ and $m$ are integers.

Recently, several groups have reported theoretical and experimental studies on the physical properties of single-walled carbon nanotubes (SWNTs) under strain. Tang $et$ $al.^{2)}$ have estimated compressibility and polygonization of SWNTs under hydrostatic pressure. They have determined the volume compressibility by using synchrotron x-ray diffraction method. Yakobson $et$ $al.^{3,4)}$ have simulated morphological changes of carbon nanotubes with the variation of tubule length using the classical molecular dynamics (MD) method without controlling pressure. Nardelli $et$ $al.^{5)}$ have reported the mechanism of strain release in armchair carbon nanotubes under uniaxial tension. They have performed first-principle MD simulation, again without controlling pressure, for (5,5) armchair SWNT up to 10% tensile strain, and investigated a mechanism of strain release. Quite recently, Ozaki $et$ $al.^{6)}$ have reported the buckling of SWNTs under large strain using an order-$N$ $(O(N))$ tight-binding MD (TBMD) without controlling pressure. They also evaluated the variation of the strain energy for the (10,10) and (17,0) SWNTs. However, since the strain energy value was obtained from the conjugate gradient optimization for atomic positions, finite temperature effects which is particularly important to investigate the dynamics was missing.

In present paper, we investigate the finite temperature properties of (10,10) SWNT under pressure along the tubule axis using the pressure-controlled TBMD simulation. We use a transferable TBMD potential for carbon reported by $Xu$ $et$ $al.,^{7)}$ which has been successfully applied to the carbon family ranging from two-dimensional graphite and diamond to liquid carbon and fullerene.$^{8-10)}$ The computational cost of this method is still heavy if we use the standard diagonalization algorithm to calculate eigenvalues of the TB Hamiltonian. Since the computational cost of this algorithm is generally proportional to the cube of system size (order-$N^3$ scheme), Goedecker $et$ $al.^{11)}$ and Colombo$^{8)}$ have used the Fermi matrix method and localized-orbital algorithm to achieve $O(N)$ computational cost. This method is rather simple and its implementation is relatively straightforward.$^{8)}$ Using this $O(N)$ TBMD method, we have estimated dynamical structure factors of SWNTs in the previous work.$^{12)}$ In the present work, we introduce an extended Andersen method$^{13,14)}$ in the $O(N)$ TBMD method in order to control the uniaxial pressure of system in the direction of tubule axis. This method is simple but very useful to perform a TBMD simulation under pressure. In $\S2$, we give a brief overview of the pressure-control method for the $O(N)$ TBMD simulation. The results of simulation for the (10,10) SWNT under uniaxial strains are discussed in $\S3$.

## §2. Simulation Method

The simulation for a SWNT is performed by using the $O(N)$ TBMD method. To calculate the total energy of the system, we use the transferable TB parameter set obtained by $Xu$ $et$ $al.^{7)}$ The TB energy calculation is carried out in the framework of the Fermi matrix expansion,$^{8,9,11,15)}$ where the Fermi matrix is a Fermi-Dirac (FD) distribution function in the matrix representation. The chemical potential $\mu$ which appears in the FD distribution function is adjusted every time step so as to preserve the number of electrons in the system during simulation. By the use of the Fermi matrix, we can obtain the TB energy without using the $O(N^3)$ standard diagonalization scheme. The interatomic force from the electronic band structure is evaluated using the Hellmann-Feynman theorem, and its repulsive part is

*E-mail: taka@devXc.elc.iwate-u.ac.jp

represented as the short-ranged two-body force. We also introduce a localization region associated with each atom $^{11,15)}$ in order to achieve the $O(N)$ calculation, in which the computational cost is linearly proportional to the size of system.

The simulation is performed for the (10,10) SWNT of length $L_{y}^{0}=19.68$ Å at zero strain, which consists of eight SWNT unit cells (320 carbon atoms in total). This axial length of the SWNT is large enough to evaluate the finite temperature effects for the strain energy at small strain region without buckling. A large vacuum region around the target SWNT is introduced in order to avoid interactions between periodic MD cell images, while the periodic boundary condition is imposed only on the direction of the tubule axis which corresponds to $y$-direction in our MD system. Thus, the volume size of the MD supercell is $L_{x} \times L_{y} \times L_{z}=50 \times L_{y}^{0} \times 50$ Å$^{3}$ at initial time step. The Verlet algorithm $^{16,17)}$ is used to solve the equation of motion for atoms with the time step interval of $\Delta t=0.7 \times 10^{-15} \mathrm{~s}$ (0.7 fs). The temperature of the system is regulated every 5 time steps by using the velocity scaling method. $^{17)}$

The pressure of system is controlled by changing the MD supercell size $L_{y}$ so as to balance the internal uniaxial pressure $P_{y}$ evaluated with the external prescribed uniaxial pressure $P_{y}^{\text {set }}$:
$$
L_{y}^{\prime}=s L_{y}, \tag{2.1}
$$

$$
s=1.0+b \arctan \left(c\left(P_{y}-P_{y}^{\text {set }}\right)\right), \tag{2.2}
$$
where the constants $b$ and $c$ are appropriately chosen. $^{13,14)}$ Using the virial theorem, the internal uniaxial pressure $P_{y}$ is determined as $^{15,18)}$

$$
P_{y}=\frac{1}{V}\left\{N k_{\mathrm{B}} T+\frac{1}{6} \sum_{i, j}^{i \neq j} \boldsymbol{F}_{i, j} \cdot\left(\boldsymbol{r}_{i}-\boldsymbol{r}_{j}\right)\right\}_{y y}, \tag{2.3}
$$

where $V$ is the volume, $N$ the number of atoms in the system, $k_{\mathrm{B}}$ the Boltzmann constant, $T$ the temperature of the system, $\boldsymbol{r}_{i}$ the position vector of atom $i$, and $\boldsymbol{F}_{i, j}$ the interatomic force between atoms $i$ and $j$. The suffix $y y$ of the right-hand-side of eq. (2.3) indicates that only the diagonal tensor element for the tubule axis corresponding to the $y$-direction is used to evaluate the uniaxial pressure $P_{y}$. We increase the prescribed external pressure $P_{y}^{\text {set }}$ stepwise by $0.2 \mathrm{GPa}$ every 1000 time steps in the compressive strain process, and regulate the internal pressure every 100 time steps accordingly. Here, the new parameter $c$ is introduced in order to adjust the pressure of system efficiently. We found that an efficient stabilization of the system at a prescribed pressure is achieved using the parameter set of $b=0.5$ and $c=0.1 \mathrm{GPa}^{-1}$, and these value were used throughout our simulation runs.

## §3. Simulation Results

In order to investigate temperature effects of the (10, 10) SWNT under uniaxial pressure, we have performed pressure-controlled $O(N)$ TBMD simulation at finite temperature. Figure 1 shows the variations of the pressure as a function of time step at temperatures of $T=50$ to $900 \mathrm{~K}$. The pressure is well controlled up to $9500,7200,6700$, and 6000 time steps at temperatures of $T=50,300,600$, and $900 \mathrm{~K}$, respectively. However, at late stages of each simulation, the pressure changes rapidly and becomes uncontrollable under the large strain. Therefore, we concentrate our interest on physical properties in small strain region where the structural stability is well conserved. Insets of Figs. 1(a) to 1(d) are the variation of strains for the (10,10) SWNT at each temperature around the time steps where the pressure becomes uncontrollable. As can be seen, the (10,10) SWNT keeps its structure stable up to the strains of $\varepsilon=-0.08,-0.07,-0.06$, and -0.055 at temperatures of $T=50,300,600$, and $900 \mathrm{~K}$, respectively. Here, the strain $\varepsilon$ is calculated as $\varepsilon=\left(L_{y}-\right.$ $L_{y}^{0}) / L_{y}^{0}$ with the initial length $L_{y}^{0}$ of the (10,10) SWNT. It is clear that the axial strength of the (10,10) SWNT depends on temperature of the system.

Next in Fig. 2, we show the variation of the potential energy per an atom of the (10,10) SWNT at finite temperatures as a function of the strain. These were directly obtained by each single TBMD simulation at corresponding temperature in Fig. 1. Here, the small strain region in which the pressure is well controlled is indicated by the vertical dashed lines. At each temperature, it is found that the potential energy of the (10,10) SWNT increases in proportion to square of the strain up to the critical point. Therefore, in such a small strain region, the Hooke's law holds for the (10,10) SWNT over the wide range of temperatures. In order to analyze the elastic properties of the (10,10) SWNT, we have fitted a quadratic equation $E(\varepsilon)=(1 / 2) a \varepsilon^{2}+b \varepsilon+c$ to the calculated data of the potential energy applying the least-squares method for the small strain region. Obtained coefficients $a, b$, and $c$ for each temperature are listed in Table I. Here, the parameter $a$ is the modulus of axial elasticity, while $b$ and $c$ are introduced to describe the deviation. Figure 3 gives the variation of quadratic equation $E(\varepsilon)$ at temperatures of $T=50$ to $900 \mathrm{~K}$. The vertical solid lines represent the minimum of the potential energies $\left(\varepsilon_{0}=-b / a\right)$. Particularly, the minimum of the potential energy shifts to left with increasing the temperature of system. Here, the strains at the minimum points of the potential energies are obtained as $\varepsilon_{0}=-0.0029,-0.0096,-0.0150$, and -0.0204 at temperatures of $T=50,300,600$, and $900 \mathrm{~K}$, respectively. This negative change of the minimum point with increasing the temperature of the system is due to the strong anisotropy of the thermal expansion properties along the axial and radial directions.

To estimate the diameter and geometry dependences of the strains, we have performed TBMD simulations for (8,8), (12,12), and (17,0) SWNTs. In Table. II, we present the diameter and geometry dependences of the strains $\varepsilon_{0}$ at temperatures of $50 \mathrm{~K}, 300 \mathrm{~K}, 600 \mathrm{~K}$, and $900 \mathrm{~K}$. The strains $\varepsilon_{0}$ of each SWNT for the minimum potential energy shifted to negative with increasing the temperature of the system. However, $\varepsilon_{0}$ of the (17,0) zigzag type SWNT shows more negative shifts than that of

![](./images/812300886498869249_1.jpg)

Fig. 1. The variations of the pressure as a function of time step at temperatures of $T=50$ K (a), 300 K (b), 600 K (c), and 900 K (d), respectively. The insets of (a) to (d) are the variations of strains around the time steps where the pressure becomes uncontrollable.

<table>
<caption>Table I. The coefficients of the quadratic equation obtained by the least-squares fit.</caption>
<thead>
<tr>
<th colspan="4">$E(\varepsilon)=(1/2)a\varepsilon^{2}+b\varepsilon+c$</th>
</tr>
<tr>
<th></th>
<th>$a$ (eV/atom)</th>
<th>$b$ (eV/atom)</th>
<th>$c$ (eV/atom)</th>
</tr>
</thead>
<tbody>
<tr>
<td>50 K</td>
<td>59.22</td>
<td>0.17</td>
<td>−8.44</td>
</tr>
<tr>
<td>300 K</td>
<td>65.36</td>
<td>0.63</td>
<td>−8.39</td>
</tr>
<tr>
<td>600 K</td>
<td>67.98</td>
<td>1.02</td>
<td>−8.32</td>
</tr>
<tr>
<td>900 K</td>
<td>74.22</td>
<td>1.52</td>
<td>−8.26</td>
</tr>
</tbody>
</table>

the armchair type SWNTs with increasing the temperature. Since the diameters of (17,0) and (10,10) SWNTs are about the same, it can be inferred that the strain $\varepsilon_{0}$ is more sensitive to the geometry rather than to the diameter of the SWNT.

### §4. Conclusion

We have performed pressure-controlled $O(N)$ TBMD simulations for the (10,10) SWNT at finite temperatures. The pressure of the system has been controlled by means of an extended Andersen method. We have demonstrated that the simple pressure-control method used in this simulation is quite efficient to investigate the elastic properties of carbon nanotube under uniaxial pressure. The critical strain of the (10,10) SWNT has been obtained in the temperature range 50 to 900 K. The absolute value of the critical strain has become small as the temperature increases. This fact indicates that the axial strength and stability of the (10,10) SWNT strongly depend on temperature of the system. Under the small strain region the potential energy per an atom of the (10,10) SWNT increases in accordance with the Hooke's law. Moreover, the strains at the minimum

![](./images/812300886498869249_2.jpg)

Fig. 2. The variations of the potential energy per an atom of the (10,10) SWNT as a function of the strain at temperatures $T=50$ K (a), 300 K(b), 600 K (c), and 900 K (d). The small strain region in which the pressure is well controlled is indicated by the vertical dashed lines.

<table>
  <thead>
    <tr>
      <th></th>
      <th>geometry</th>
      <th>直径 (Å)</th>
      <th>50 K</th>
      <th>300 K</th>
      <th>600 K</th>
      <th>900 K</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>(8,8)</td>
      <td>armchair</td>
      <td>10.85</td>
      <td>−0.0036</td>
      <td>−0.0090</td>
      <td>−0.0154</td>
      <td>−0.0194</td>
    </tr>
    <tr>
      <td>(10,10)</td>
      <td>armchair</td>
      <td>13.56</td>
      <td>−0.0029</td>
      <td>−0.0096</td>
      <td>−0.0150</td>
      <td>−0.0204</td>
    </tr>
    <tr>
      <td>(12,12)</td>
      <td>armchair</td>
      <td>16.27</td>
      <td>−0.0050</td>
      <td>−0.0101</td>
      <td>−0.0156</td>
      <td>−0.0181</td>
    </tr>
    <tr>
      <td>(17,0)</td>
      <td>zig-zag</td>
      <td>13.31</td>
      <td>−0.0073</td>
      <td>−0.0150</td>
      <td>−0.0179</td>
      <td>−0.0232</td>
    </tr>
  </tbody>
</table>

points of the potential energy has shifted to negative with increasing the temperature of the system. This negative change of the minimum point with increasing the temperature of the system is due to the strong anisotropy of the thermal expansion properties along the axial and radial directions.

Next, to estimate the diameter and geometry depen- dences of the strains for the minimum potential energies at temperatures of 50 K, 300 K, 600 K, and 900 K, we have performed TBMD simulations for (8,8), (12,12), and (17,0) SWNTs. We have found that the strain $\varepsilon_{0}$ at minimum point of the potential energy is more sensitive to the geometry rather than to the diameter of the SWNT.

Finally, the external conditions of pressure applied in the present TBMD simulations are experimentally not feasible at present, but the results of these finite temperature dynamical simulations are expected to provide a useful information in interpreting future experiment.

![](./images/812300886498869249_3.jpg)

Fig. 3. The potential energy curves $E(\varepsilon)$ at each temperature. The vertical solid lines represent the minimum points of the potential energies.

### Acknowledgements
The authors wish to thank Dr. K. Nishikawa, Dr. K. Shindo, and Dr. Y. Kashiwaba for helpful advice. We are also grateful to Dr. H. Chiba, K. Funatogawa, Y. Sakai, K. Seki, and K. Ohta for assistance in performing the computation. Part of the computation in this work has been done using the facilities of the Supercomputer Center, Institute for Solid State Physics, University of Tokyo. This work has been supported by the Grant-in-
Aid for Scientific Research from the Ministry of Education, Culture, Sports, Science and Technology of Japan under Grant No. 10640360.

1) S. Iijima: **Nature** 354 (1991) 56.
2) J. Tang, L. C. Qin, T. Sasaki, M. Yudasaka, A. Matsushita and S. Iijima: Phys. Rev. Lett. **85** (2000) 1887.
3) B. I. Yakobson, C. J. Brabec and J. Bernholc: Phys. Rev. Lett. **76** (1996) 2511.
4) B. I. Yakobson, M. P. Campbell, C. J. Brabec and J. Bernholc: Comput. Mater. Sci. **8** (1997) 341.
5) M. B. Nardelli, B. I. Yakobson and J. Bernholc: Phys. Rev. B **57** (1998) R4277.
6) T. Ozaki, Y. Iwasa and T. Mitani: Phys. Rev. Lett. **84** (2000) 1712.
7) C. H. Xu, C. Z. Wang, C. T. Chan and K. M. Ho: J. Phys.: Condens. Matter **4** (1992) 6047.
8) L. Colombo: *Annual Reviews of Computational Physics IV*, ed. D. Stauffer (World Scientific, Singapore, 1996) p. 147.
9) C. Z. Wang and K. M. Ho: *Advances in Chemical Physics*, ed. I. Prigogine and S. A. Rice (John Wiley & Sons, New York, 1996) Vol. 93, p. 651.
10) Y. Cui and L. Liu: Phys. Rev. B **56** (1997) 3624.
11) S. Goedecker and M. Teter: Phys. Rev. B **51** (1995) 9455.
12) T. Ito, K. Nishidate, M. Baba, T. Sato, K. Shindo and K. Nishikawa: J. Phys. Soc. Jpn. **69** (2000) 2531.
13) H. C. Andersen: J. Chem. Phys. **72** (1980) 2384.
14) K. Kawamura: *Molecular Dynamics Simulations*, ed. F. Yonezawa (Springer-Verlag, Heiderberg, 1990) p. 88.
15) T. Oda and Y. Hiwatari: J. Phys.: Condens. Matter **12** (2000) 1627.
16) M. P. Allen and D. J. Tildesley: *Computer Simulation of Liquids* (Clarendon Press, Oxford, 1987) p. 78.
17) J. M. Haile: *Molecular Dynamics Simulation: Elementary Methods* (John Wiley & Sons, New York, 1992) pp. 158 and 200.
18) P. Klein and H. M. Urbassek: Phys. Status Solidi B **207** (1998) 33.