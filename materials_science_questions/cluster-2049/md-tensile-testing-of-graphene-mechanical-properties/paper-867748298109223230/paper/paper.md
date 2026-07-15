# Rupture of amorphous graphene via void formation

Sandeep K. Jain$^{*, \dagger}$ and Gerard T. Barkema$^{*, \ddagger}$

$^\dagger$Institute for Theoretical Physics, Universiteit Utrecht, Princetonplein 5, 3584 CC Utrecht,
The Netherlands

$^\ddagger$Department of Information and Computing Science, Universiteit Utrecht, Princetonplein
5, 3584 CC Utrecht, The Netherlands

E-mail: sandeepiitr7@gmail.com; G.T.Barkema@uu.nl

### Abstract
Apart from its unique and exciting electronic properties, many sensor based applications of graphene are purely based on its mechanical and structural properties. Here we report a numerical and analytical study of a void in amorphous (small domain polycrystalline) graphene, and show that the energetics of a void is a balance between the line tension cost versus the increased area gain. Using the concepts of classical nucleation theory, we show that the critical radius of a void formed in amorphous graphene at constant pressure is simply the ratio of line tension at the void and the applied pressure. The values of the critical radius of the void for flat and buckled graphene are $3.48\mathring{A}$ and $3.31\mathring{A}$, respectively at $2\ \mathrm{eV/\mathring{A}^2}$ pressure. We also show that the dominant finite size correction to the line tension is inversely proportional to the radius of the void in both flat and buckled cases. Contrary to conventional wisdom, with the help of a simple analytical model we find that the shear modulus sets the lower limit of the line tension in the samples. This makes our study relevant for other two-dimensional amorphous materials such as h-BN, phosphorene, borophene, and transition metal dichalcogenides. Our results are useful for the better understanding of polycrystalline graphene under tension and therefore have direct implications on the very fascinating field of strain engineering known as "straintronics" to manipulate or improve graphene's properties.

## INTRODUCTION
The discovery of graphene has provoked a revolution in nanotechnology, as the structural, thermal, and electronic properties of graphene make it a very useful component for a large variety of devices. $^{1-4}$ Most of these applications require a high quality, large graphene samples. The quality of the samples is very important for the observation of the special features of graphene, such as ultrahigh electron mobility, $^{5-7}$ very high thermal conductivity, $^{8}$ half integer quantum-Hall effect, $^{9,10}$ massless Dirac fermions $^{11}$ as well as for its mechanical and

chemical properties, e.g., its permeability¹² and very high Young's modulus.¹³,¹⁴ Graphene is claimed to be the strongest material ever, as it has extraordinary elastic properties.

Recently, with the help of the chemical vapor deposition (CVD) technique; synthesis and production of large graphene samples became possible.¹⁵ However, in reality, chemical vapor deposition (CVD) grown graphene is a polycrystalline material, hence contains many defects, and naturally buckles out of the crystalline plane.¹⁶⁻¹⁹ These defects limit the visibility of the special properties of pristine graphene, but on the other hand have positive effects when graphene is used as an anode material for metal-ion batteries.²⁰ Study of lattice defects in graphene is of both fundamental and practical relevance, since they are inevitably present in the samples and have direct consequences on the physical and chemical properties, thereby impeding its applications in the semiconductor industry.²¹ Amorphous two-dimensional carbon structures are also very important since the ordered hexagon arrangement of carbon atoms in graphene is not directly suitable for many practical studies and applications like chemical sensor and nanoelectronics.²²

Since graphene is a one-atom thick two-dimensional layer, deformations via stretching offer very tempting aspects to control or manipulate its properties.²³⁻²⁷ Graphene is known to be very flexible and can be stretched by as much as 20% without inducing defects and rupture.²⁸ It has been shown that in graphene, strain can induce many fascinating effects such as pseudo-magnetic fields greater than 300 T at room temperature,²⁹ zero field quantum Hall effect,³⁰ enhancement of electron-phonon coupling,³¹ and superconducting states in pseudo- Landau-levels.³² Defects combined with strain is also very interesting, as they lead to some new effects, not present otherwise.³³,³⁴ Mechanical properties of large domain polycrystalline graphene samples have been reported in literature.³⁵⁻⁴⁰ Various empirical methods were used to study the deformations and tensile properties in graphene, carbon nanotubes and the amorphous carbon structures.⁴¹⁻⁴⁵ A comprehensive and detailed study of the effect of stretching on the structural properties of amorphous graphene is missing.

Very recently, our preliminary results showed that mechanical stretching also has an


interesting and significant impact on the polycrystalline properties of the graphene. We observed that via regulated stretching, one can suppress the point and line defects in the samples and hence ultimately can have a single crystalline domain in graphene. An excess amount of stretching, however can rupture the sample via void formation. It is, therefore, of both practical and fundamental importance to address the effect of stretching on the structural properties of the amorphous graphene. Experimentally also it is very relevant since during the synthesis, production, and transfer process structural strains are expected to be present in the samples due to the surface corrugations of the substrate or the lattice mismatch between substrate and graphene layer. In this article, we report the energetics of void formation in amorphous graphene.

## METHOD

In our simulations, we use a recently-developed semi-empirical potential for graphene⁴⁶ given by

$$
E=\frac{3}{16} \frac{\alpha}{d^{2}} \sum_{i, j}\left(r_{i j}^{2}-d^{2}\right)^{2}+\frac{3}{8} \beta d^{2} \sum_{j, i, k}\left(\theta_{j i k}-\frac{2 \pi}{3}\right)^{2}+\gamma \sum_{i, j k l} r_{i, j k l}^{2}.\tag{1}
$$

Here, $r_{i j}$ is the length of the bond between two atoms $i$ and $j$, $\theta_{j i k}$ the angle between the two bonds connecting atom $i$ to $j$ and $k$, respectively. $r_{i, j k l}$ is the distance between atom $i$ and the plane through the three neighboring atoms $j$, $k$ and $l$ connected to atom $i$. The parameters $\alpha=26.060$ eV/Å², $\beta=5.511$ eV/Å², $\gamma=0.517$ eV/Å², and $d=1.420$ Å are used, which were obtained from density-functional theory (DFT) calculations.⁴⁶ This potential was effectively used to study vibrational properties of graphene⁴⁷ and carbon nanotubes,⁴⁸ effect of boundary conditions in graphene samples,⁴⁹ structure of twisted bilayer graphene,⁵⁰ and graphene nanobubbles.⁵¹

# RESULTS AND DISCUSSION

To generate an unbiased isotropic three-fold connected random network, we use an approach based on Voronoi networks.⁵² We place N/2 random points in a periodic box, and determine the Voronoi cells around each of these random points. The boundaries between two neighboring cells are then transformed into carbon-carbon bonds, and at the locations where three Voronoi cells meet, we place a carbon atom. Note that the initial random points cease to play a role. The resulting highly strained network with N carbon atoms is then relaxed. In our simulations we use force free (FF) boundary conditions.⁴⁹

Rupture is a dynamical phenomenon, hence we need to specify our dynamics. Per unit of time, we propose N bond transpositions, i.e. there is a fixed rate at which each possible bond switch is attempted. In our simulations, we start with an initial three-fold coordinated amorphous graphene sample with 5000 carbon atoms, generated with the Voronoi approach described above. As these networks are highly strained, we first do a quick relaxation over 5 units of time via Monte Carlo dynamics with bond transposition moves as illustrated in Figure 1. From there, we study the time evolution under further Monte Carlo dynamics. In more detail, we use the improved bond-switching algorithm in our simulations,⁵³ using our empirical potential (Eq: 1) to describe its energy. A random switch is made in the explicit list of bonds, after which the coordinates are adjusted to the minimal energy state. The new configuration is accepted with a Metropolis probability given by

$$
P = \min\left[1, \exp\left(\frac{E_b - E_f}{k_B T}\right)\right]. \tag{2}
$$

Here $E_b$ is the energy of the system before the bond transposition, $E_f$ is the energy after the bond transposition and $k_B T$ is the thermal energy of the system (0.083 eV). We apply a continuous stretching pressure ($P$) at the system and the stretching energy of the system

is given by the following term and added to the potential (Eq:1) while relaxing the system

$$
E_{s}=-P L_{x} L_{y} sin (\theta). \tag{3}
$$

Here, $P$ is the pressure applied on the sample, $L_{x}$, $L_{y}$ are the periodicity vectors, and $\theta$
is the angle between these periodicity vectors.

As the system evolves via bond transposition moves at constant pressure, we observe the
formation of void at higher order of the carbon rings ($n \geq 15$) in amorphous graphene. To
calculate the effective radius of the void ($r_{v}$), we first calculate the total area inside the void.
For that we identify the carbon atoms at the periphery of the void and divide the whole
area into small triangles as shown in Figure 2. The total area is equated with the area of a
circle to extract the effective radius of the void. Notably, we observe lots of three-membered
rings around the periphery of the void. Interestingly, if a crystalline sample is stretched well
beyond 20%, our bond transposition dynamics cause it to rupture while retaining three-fold
coordination.

### Energetics of the void

For a small void, it is energetically unfavorable to grow because of the line tension. Beyond
a certain critical size, however, the pressure dominates the line tension, as the first should
be multiplied by the boundary length and the second by the area, and the void starts to
grow. Using the concepts of classical nucleation theory, we analytically determine the critical
radius of the void in a two-dimensional system. At the constant stretching combined with
the bond switching, critical radius of the void is defined as the particular size of the void
from where the void will only grow in size.

The free energy cost due to the line tension ($F_{s}$) in the sample can be given as

$$
F_{s}=2 \pi r_{v} \sigma\left(r_{v}\right) \tag{4}
$$

where $r_v$ is the radius of the void and $\sigma(r_v)$ is the line tension along the void (free energy per unit length in $\mathrm{eV}/\mathring{\mathrm{A}}$).

The free energy gain due to the strain relieved from stretching ($F_a$) can be written as

$$
F_a = -\pi r_v^2 P \tag{5}
$$

where $P$ is the pressure acting on the sample in $\mathrm{eV}/\mathring{\mathrm{A}}^2$.

The total free energy (summation of line energy and strain energy) as a function of the void size ($r_v$) can be written as

$$
F(r_v) = 2\pi r_v \sigma(r_v) - \pi r_v^2 P. \tag{6}
$$

The formation of the void and the evolution of the structure (various snapshots at constant pressure) in 5000 carbon atom sample is shown in Figure 3. The radius of the void ($r_v$) continuously increases during the bond transpositions at constant pressure ($P=2$ $\mathrm{eV}/\mathring{\mathrm{A}}^2$), once the void crosses the value of the critical radius. We start with a highly amorphous graphene sample with a void ($r_v=8.03$ $\mathring{\mathrm{A}}$) as shown in Figure 3 a). As the pressure is continuously applied on the sample together with bond transposition, the whole sample starts to rupture along the void.

To further characterize the void, we calculate the local energy distribution along the sample as shown in Figure 4. In our samples, we define a local energy per atom (eV/atom) as follows: contributions due to two-body interactions are equally divided over the two interacting atoms, and contributions due to the three-body (angular) interactions are attributed to the central atom. Thus, the sum of the local energy over all atoms equals the total energy of the sample. This definition of local energy helps us to visualize the local degree of mechanical and structural relaxation in the sample. The bulk of the total energy is concentrated along the periphery of void as shown in Figure 4 b).

The summation of the local energy in the sample from the center of the void for $r \geq r_v$ can

be given as

$$
\int_{r'=0}^{r} E(r') d r' = a \pi (r^2 - r_v^2) + 2 \pi r_v \sigma(r_v). \tag{7}
$$

Here, $r$ is measured in $\text{\AA}$ from the center of the void, $a$ is a fitting parameter in $\text{eV}/\text{\AA}^2$, and $\sigma(r_v)$ is the line tension $(\text{eV}/\text{\AA})$ along the void as a function of radius of the void $r_v$.

We calculate the summation of the energy $\left(\int E(r)\right)$ as a function of $(r^2 - r_v^2)$ at different values of $r_v$ for both flat and buckled amorphous graphene samples as shown in Figure 5 a) and b) respectively. By fitting a straight line with our numerical simulation data points in the plot, we extract the value of line tension $\sigma(r_v)$, from the range of $(r_v + 2)$ to $(r_v + 15)$ of $r$. We observe the finite size scaling in the line tension as a function of radius of the void $r_v$ for both flat and buckled samples. In general, the line tension $(\sigma(r_v))$ of a void can be written as

$$
\sigma(r_v) = \sigma(\infty) + f(r_v). \tag{8}
$$

Here $\sigma(\infty)$ is the value of the line tension in the thermodynamic limit and $f(r_v)$ is the nature of the finite size scaling in the line tension.

We plot the line tension as a function of inverse of the radius of the void and fit with a straight line for both flat and buckled cases as shown in Figure 5. The value of the $\sigma(r_v)$ in the thermodynamic limit approaches to $6.95\ \text{eV}/\text{\AA}$ and $6.61\ \text{eV}/\text{\AA}$ for flat and buckled amorphous graphene, respectively. To get a better understanding of the finite size scaling of the line tension we develop an analytical model which is discussed in the next section.

### Analytical model for the finite size scaling of the line tension

To understand the energetics of a void in the amorphous sample, we study a simple analytical model of a polygon having $n$ equal length $(d)$ edges as shown in Figure 6 a). The angle between two consecutive edges can be written as

$$
\theta_n = \pi \left[ 1 - \frac{2}{n} \right]. \tag{9}
$$

8

The effective energy of the polygon $(E_p)$ calculated from Hamiltonian defined for graphene (Eq: 1) will only be determined by three-body energy term (bond shearing therm) since the two body energy contribution will be zero (equal length edges) and can be written as

$$
E_{p}=\beta d^{2} \pi^{2}\left(\frac{3 n}{63}-\frac{1}{2}\right). \tag{10}
$$

The area of a polygon is given by

$$
A_{p}=\frac{n d^{2}}{4 \tan (\pi / n)}. \tag{11}
$$

The effective radius of the polygon for large values of $n$ can be written as, where $\tan(\theta) \sim \theta$,

$$
r_{p}=\frac{d n}{2 \pi}. \tag{12}
$$

The line tension along the void is obtained from the following equation

$$
2 \pi r_{p} \sigma_{p}\left(r_{p}\right)=E_{p}, \tag{13}
$$

which gives

$$
\sigma_{p}\left(r_{p}\right)=\frac{3 \beta d \pi^{2}}{63}-\frac{\beta d^{2} \pi}{4 r_{p}}. \tag{14}
$$

This equation sets the lower limit of the line tension of a void in completely flat samples. In this equation we also observe the $1/r$ finite size scaling of the line tension of the void which is in the excellent agreement with our full simulations on amorphous graphene. In reasonable

approximation, the lower limit of the line tension is set by the shear modulus of the sample. Since the line tension scales linearly with $\beta$, the energetics of the void also behaves linearly with the shear modulus of the sample. This analytical argument should be equally valid for other two-dimensional materials such as h-BN, phosphorene, borophene and other transition metal dichalcogenides.

In our simulations we also tried to capture the effect of the bulk modulus on the energetic of the voids in two-dimensional materials. In particular we changed the values of $\alpha$ in the Hamiltonian (Eq: 1) for graphene and minimized the energies of the various amorphous samples with voids. Counter-intuitively we observe that the two-body energy term increases by reducing the bulk modulus and vice versa. However the total energy of the sample (combined with stretching energy Eq: 3) decreases since reduction in bulk modulus makes sample less stiff and therefore more stretchable. These observations on the dependency of the energetic of the void in two-dimensional structures might be useful in strain engineering and tailored applications of these materials.

### Critical radius of the void in 2D materials
We have shown that the line tension of the void scales as the inverse of the radius of the void and thus the expression can be written as

$$
\sigma(r_v) = \sigma(\infty) + \frac{C}{r_v}. \tag{15}
$$

Here $C$ is a fitting parameter which has a value of $-30.70$ Å and $-33.67$ Å for flat and buckled graphene, respectively, as shown in Figure 5 b). Eq: 6 can be rewritten as

$$
F(r_v) = 2\pi r_v \sigma(r_\infty) + 2\pi C - \pi r_v^2 P. \tag{16}
$$


To calculate the critical radius of the void $r_{v(cri)}$ we put $\partial F(r_v)/\partial r_v = 0$ and get

$$
r_{v(cri)} = \frac{\sigma_{\infty}}{P}. \tag{17}
$$

Hence, the total free energy at the critical radius of the void can be written as

$$
F(r_{v(max)}) = \frac{\pi \sigma_{\infty}^2}{P} + 2\pi C. \tag{18}
$$

The values of $\sigma_{\infty}$ from our numerical simulations are $6.95$ eV/Å and $6.61$ eV/Å for flat and buckled graphene respectively. The critical radius of the void for flat and buckled amorphous samples are $3.48$Å and $3.31$Å respectively.

# CONCLUSIONS

In conclusion, we show the effective mechanism and energetics of the rupturing process via void formation of amorphous (small domain polycrystalline) graphene under mechanical stretching. In amorphous samples even at 3-5% of the stretching, samples start to rupture via formation of large voids whereas in crystalline graphene the stretching can be much higher (upto 20%). Using the concepts of classical nucleation theory combined with simulations, we find the critical radius of the void is simply the ratio between line tension and the applied pressure on the samples.The values of the critical radius of the void for flat and buckled graphene are $3.48$Å and $3.31$Å, respectively at $2$ eV/Å$^2$ pressure. Line tension of the void has a finite size correction which scales as the inverse of the radius of the void for both flat and buckled samples. Line tension is directly proportional to the shear modulus of the sample and therefore future predictions regarding to the energetic of the voids in other two-dimensional materials can be achieved with the help of our results. Our results provide significant insight into the structural and energetics aspects of the voids in the polycrystalline

samples and have direct implications on the tailoring of the properties of graphene via strain engineering. $^{23,54}$

![](./images/867748298109223230_1.jpg)

Figure 1: Bond transposition mechanism in crystalline graphene. a) A string of four random atoms are selected in the sample to switch the bonds (A–B and C–D). b) In a move a connection is made between atoms A and C and similarly between atoms B and D, replacing bonds between atoms A and B as well as C and D. c) The sample is then relaxed.

![](./images/867748298109223230_2.jpg)

Figure 2: Structure of a void in an amorphous graphene sample with 5000 carbon atoms at a constant pressure of $P=2$ eV/Å$^2$ (Eq. 3). Here we show an effective method to determine the radius of the void $(r_v)$ which we used in our calculations. The whole area of the void $(a_v)$ is divided into small triangles connecting to two consecutive atoms at periphery of the void from a point inside the void (as shown in green colored lines). The summation of all the area contribution from these small triangles resulted into the total effective area of the void $(a_v)$ and then the effective radius of the void (shown in the blue colored circle in the zoomed in figure) is calculated by $a_v = \pi \times r_v^2$.

![](./images/867748298109223230_3.jpg)

Figure 3: Structure and evolution of a void in amorphous graphene, simulated at a constant pressure of $P=2$ eV/Å$^2$. We start with an amorphous sample of graphene and evolve it via bond transposition moves with Metropolis acceptance probability (Eq. 2) using the Hamiltonian given in Eq. 1. This method is widely used to study the dynamics and evolution of amorphous materials such as a-Si.⁵³ Here we show various snapshots of the graphene sample captured during the evolution process. The radius of the voids are (a) $r_v=8.03$\AA. (b) $r_v=11.94$\AA. (c) $r_v=22.37$\AA. (d) $r_v=53.28$\AA. Once the critical radius of the void is crossed, the size of the void will keep on increasing as shown in the figure, and sample will start to rupture along the void.

![](./images/867748298109223230_4.jpg)

Figure 4: Local energy distribution in the sample with a void radius of 16.92 Å. In our samples, we define a local energy per atom (eV/atom) as follows: contributions due to two- body interactions are equally divided over the two interacting atoms, and contributions due to the three-body (angular) interactions are attributed to the central atom. Thus, the sum of the local energy over all atoms equals the total energy of the sample. (a) Most of the energy is localized at the periphery of the void in the sample. (b) Energy distribution along with the structure of the sample shows the amorphous nature of the sample (dark blue regime around the hexagonal rings).

![](./images/867748298109223230_5.jpg)

Figure 5: The total summation of the elastic energy $(\int E(r))$ in the sample from the center of the void is plotted as a function of square of the distance $(r^2 - r_v^2)$ for both flat and buckled samples. The summation of the energy in the sample from the center of the void can be written as $(r \geq r_v): a \times \pi(r^2 - r_v^2) + 2\pi r_v \sigma$; where $r$ is the distance from the center of the void, $r_v$ is the radius of the void, $\sigma$ is the line tension and $a$ is a fitting parameter. We fit these plots from $(r_v + 2)$ to $(r_v + 15)$ with a straight line to extract the values of $\sigma$ for different radius of the voids. Due to the additional relaxation the third direction in buckled samples the value of line tension of void is lower than that of the flat case.

16

![](./images/867748298109223230_6.jpg)

Figure 6: The line tension of the void $(\sigma(r))$ is plotted as a function of inverse of the radius of the void and fitted with a straight line for both flat and buckled samples. (a) An analytical model based on three fold isotropic do-decagon with edge length of $1.42\ \mathring{A}$ (crystalline carbon-carbon bond length in graphene) to numerically calculate the lower limit of the line tension is purely based on bond shearing. Analytical expression (Eq. 14) suggests that there is $1/r_v$ finite size correction in the line tension which is consistent with our full simulations. (b) Finite size scaling behavior of line tension in both flat (red colored dots) and buckled (blue colored dotes) amorphous graphene. These data points at various values of radius of the voids are then fitted with a straight line (black line) to show that the line tension scales as inverse of the radius of the void and in the thermodynamic limit achieves the value of $6.95\ \text{eV}/\mathring{A}$ for flat and $6.61\ \text{eV}/\mathring{A}$ for buckled graphene samples.

### Acknowledgement

We acknowledge the support by FOM-SHELL-CSER program (12CSER049). This work is part of the research program of the Foundation for Fundamental Research of Matter (FOM), which is part of the Netherlands Organization for Scientific Research (NWO).

### References

(1) Castro Neto, A. H.; Guinea, F.; Peres, N. M. R.; Novoselov, K. S.; Geim, A. K. The electronic properties of graphene. *Rev. Mod. Phys.* **2009**, *81*, 109–162.

(2) Geim, A. K. Graphene: Status and Prospects. *Science* **2009**, *324*, 1530–1534.

(3) Geim, A. K.; Novoselov, K. S. The Rise of Graphene. *Nat. Mater.* **2007**, *6*, 183–191.

(4) Dolleman, R. J.; Davidovikj, D.; Cartamil-Bueno, S. J.; van der Zant, H. S. J.; Steeneken, P. G. Graphene Squeeze-Film Pressure Sensors. *Nano Lett.* **2016**, *16*, 568–571.

(5) Bolotin, K.; Sikes, K.; Jiang, Z.; Klima, M.; Fudenberg, G.; Hone, J.; Kim, P.; Stormer, H. Ultrahigh Electron Mobility in Suspended Graphene. *Solid State Commun.* **2008**, *146*, 351–355.

(6) Morozov, S. V.; Novoselov, K. S.; Katsnelson, M. I.; Schedin, F.; Elias, D. C.; Jaszczak, J. A.; Geim, A. K. Giant Intrinsic Carrier Mobilities in Graphene and Its Bilayer. *Phys. Rev. Lett.* **2008**, *100*, 016602.

(7) Mayorov, A. S.; Gorbachev, R. V.; Morozov, S. V.; Britnell, L.; Jalil, R.; Ponomarenko, L. A.; Blake, P.; Novoselov, K. S.; Watanabe, K.; Taniguchi, T. et al. Micrometer-Scale Ballistic Transport in Encapsulated Graphene at Room Temperature. *Nano Lett.* **2011**, *11*, 2396–2399, PMID: 21574627.

(8) Balandin, A. A. Thermal properties of graphene and nanostructured carbon materials. *Nat. Mater.* **2011**, *10*, 569-581.

(9) Zhang, Y.; Tan, Y.-W.; Stormer, H. L.; Kim, P. Experimental Observation of the Quantum Hall Effect and Berrys Phase in Graphene. *Nature* **2005**, *438*, 201-204.

(10) Novoselov, K. S.; Jiang, Z.; Zhang, Y.; Morozov, S. V.; Stormer, H. L.; Zeitler, U.; Maan, J. C.; Boebinger, G. S.; Kim, P.; Geim, A. K. Room-Temperature Quantum Hall Effect in Graphene. *Science* **2007**, *315*, 1379-1379.

(11) Novoselov, K. S.; Geim, A. K.; Morozov, S. V.; Jiang, D.; Katsnelson, M. I.; Grig- orieva, I. V.; Dubonos, S. V.; Firsov, A. A. Two-Dimensional Gas of Massless Dirac Fermions in Graphene. *Nature* **2005**, *438*, 197-200.

(12) Nair, R. R.; Wu, H. A.; Jayaram, P. N.; Grigorieva, I. V.; Geim, A. K. Unimpeded Per- meation of Water Through Helium-Leak-Tight Graphene-Based Membranes. *Science* **2012**, *335*, 442-444.

(13) Lee, C.; Wei, X.; Kysar, J. W.; Hone, J. Measurement of the Elastic Properties and Intrinsic Strength of Monolayer Graphene. *Science* **2008**, *321*, 385-388.

(14) Booth, T. J.; Blake, P.; Nair, R. R.; Jiang, D.; Hill, E. W.; Bangert, U.; Bleloch, A.; Gass, M.; Novoselov, K. S.; Katsnelson, M. I. et al. Macroscopic Graphene Membranes and Their Extraordinary Stiffness. *Nano Lett.* **2008**, *8*, 2442-2446.

(15) Zhang, Y.; Zhang, L.; Zhou, C. Review of Chemical Vapor Deposition of Graphene and Related Applications. *Acc. Chem. Res.* **2013**, *46*, 2329-2339.

(16) Yazyev, O. V.; Chen, Y. P. Polycrystalline Graphene and Other Two-Dimensional Materials. *Nat. Nanotechnol.* **2014**, *9*, 755-767.

(17) Aissa, B.; Memon, N. K.; Ali, A.; Khraisheh, M. K. Recent Progress in the Growth

and Applications of Graphene as a Smart Material: A Review. *Front. in Mater.* **2015**, 2, 58.

(18) Lee, S.-M.; Kim, J.-H.; Ahn, J.-H. Graphene as a flexible electronic material: mechan- ical limitations by defect formation and efforts to overcome. *Mater. Today* **2015**, 18, 336 – 344.

(19) Deng, S.; Berry, V. Wrinkled, rippled and crumpled graphene: an overview of formation mechanism, electronic properties, and applications. *Mater. Today* **2016**, 19, 197 – 212.

(20) Yu, Y.-X. Can all nitrogen-doped defects improve the performance of graphene anode materials for lithium-ion batteries? *Phys. Chem. Chem. Phys.* **2013**, 15, 16819–16827.

(21) Banhart, F.; Kotakoski, J.; Krasheninnikov, A. V. Structural Defects in Graphene. *ACS Nano* **2011**, 5, 26–41.

(22) Kotakoski, J.; Brand, C.; Lilach, Y.; Cheshnovsky, O.; Mangler, C.; Arndt, M.; Meyer, J. C. Toward Two-Dimensional All-Carbon Heterostructures via Ion Beam Pat- terning of Single-Layer Graphene. *Nano Letters* **2015**, 15, 5944–5949, PMID: 26161575.

(23) Pereira, V. M.; Castro Neto, A. H. Strain Engineering of Graphene's Electronic Struc- ture. *Phys. Rev. Lett.* **2009**, 103, 046801.

(24) Pereira, V. M.; Castro Neto, A. H.; Peres, N. M. R. Tight-binding approach to uniaxial strain in graphene. *Phys. Rev. B* **2009**, 80, 045401.

(25) Ni, Z. H.; Yu, T.; Lu, Y. H.; Wang, Y. Y.; Feng, Y. P.; Shen, Z. X. Uniaxial Strain on Graphene: Raman Spectroscopy Study and Band-Gap Opening. *ACS Nano* **2008**, 2, 2301–2305.

(26) Kim, K. S.; Zhao, Y.; Jang, H.; Lee, S. Y.; Kim, J. M.; Kim, K. S.; Ahn, J.-H.; Kim, P.; Choi, J.-Y.; Hong, B. H. Large-scale pattern growth of graphene films for stretchable transparent electrodes. *Nature* **2009**, 457, 706–710.

(27) Bao, W.; Miao, F.; Chen, Z.; Zhang, H.; Jang, W.; Dames, C.; Lau, C. N. Controlled ripple texturing of suspended graphene and ultrathin graphite membranes. *Nat. Nano* **2009**, *4*, 562-566.

(28) Si, C.; Sun, Z.; Liu, F. Strain engineering of graphene: a review. *Nanoscale* **2016**, *8*, 3207-3217.

(29) Levy, N.; Burke, S. A.; Meaker, K. L.; Panlasigui, M.; Zettl, A.; Guinea, F.; Neto, A. H. C.; Crommie, M. F. Strain-Induced Pseudo-Magnetic Fields Greater Than 300 Tesla in Graphene Nanobubbles. *Science* **2010**, *329*, 544-547.

(30) Guinea, F.; Katsnelson, M. I.; Geim, A. K. Energy gaps and a zero-field quantum Hall effect in graphene by strain engineering. *Nat. Phys.* **2010**, *6*, 30-33.

(31) Si, C.; Liu, Z.; Duan, W.; Liu, F. First-Principles Calculations on the Effect of Doping and Biaxial Tensile Strain on Electron-Phonon Coupling in Graphene. *Phys. Rev. Lett.* **2013**, *111*, 196802.

(32) Uchoa, B.; Barlas, Y. Superconducting States in Pseudo-Landau-Levels of Strained Graphene. *Phys. Rev. Lett.* **2013**, *111*, 046604.

(33) Lu, J.; Bao, Y.; Su, C. L.; Loh, K. P. Properties of Strained Structures and Topological Defects in Graphene. *ACS Nano* **2013**, *7*, 8350-8357.

(34) Lu, J.; Bao, Y.; Su, C. L.; Loh, K. P. Defects in Graphene: Generation, Healing, and Their Effects on the Properties of Graphene: A Review. *J. Mater. Sci. Technol.* **2015**, *31*, 599-606.

(35) Kotakoski, J.; Meyer, J. C. Mechanical properties of polycrystalline graphene based on a realistic atomistic model. *Phys. Rev. B* **2012**, *85*, 195447.

(36) Song, Z.; Artyukhov, V. I.; Yakobson, B. I.; Xu, Z. Pseudo HallPetch Strength Reduc- tion in Polycrystalline Graphene. *Nano Letters* **2013**, *13*, 1829-1833, PMID: 23528068.
21

(37) Mortazavi, B.; Cuniberti, G. Atomistic modeling of mechanical properties of polycrys- talline graphene. *Nanotechnology* **2014**, *25*, 215704.

(38) Sha, Z. D.; Quek, S. S.; Pei, Q. X.; Liu, Z. S.; Wang, T. J.; Shenoy, V. B.; Zhang, Y. W. Inverse Pseudo Hall-Petch Relation in Polycrystalline Graphene. *Scientific Reports* **2014**, *4*, 5991, Article.

(39) Sha, Z.; Pei, Q.; Liu, Z.; Shenoy, V.; Zhang, Y. Is the failure of large-area polycrystalline graphene notch sensitive or insensitive? *Carbon* **2014**, *72*, 200 – 206.

(40) Shekhawat, A.; Ritchie, R. O. Toughness and strength of nanocrystalline graphene. *Nature Communications* **2016**, *7*, 10546 EP –, Article.

(41) Jensen, B. D.; Wise, K. E.; Odegard, G. M. Simulation of the Elastic and Ultimate Tensile Properties of Diamond, Graphene, Carbon Nanotubes, and Amorphous Carbon Using a Revised ReaxFF Parametrization. *J. Phys. Chem. A* **2015**, *119*, 9710–9721, PMID: 26315717.

(42) Lindsay, L.; Broido, D. A. Optimized Tersoff and Brenner empirical potential param- eters for lattice dynamics and phonon thermal transport in carbon nanotubes and graphene. *Phys. Rev. B* **2010**, *81*, 205441.

(43) Hossain, M. Z.; Ahmed, T.; Silverman, B.; Khawaja, M. S.; Calderon, J.; Rutten, A.; Tse, S. Anisotropic toughness and strength in graphene and its atomistic origin. *Journal of the Mechanics and Physics of Solids* **2018**, *110*, 118 – 136.

(44) Zhao, H.; Min, K.; Aluru, N. R. Size and Chirality Dependent Elastic Properties of Graphene Nanoribbons under Uniaxial Tension. *Nano Letters* **2009**, *9*, 3012–3015, PMID: 19719113.

(45) Memarian, F.; Fereidoon, A.; Ganji, M. D. Graphene Youngs modulus: Molecular

mechanics and DFT treatments. *Superlattices and Microstructures* **2015**, *85*, 348 – 356.

(46) Jain, S. K.; Barkema, G. T.; Mousseau, N.; Fang, C.-M.; van Huis, M. A. Strong Long-Range Relaxations of Structural Defects in Graphene Simulated Using a New Semiempirical Potential. *J. Phys. Chem. C* **2015**, *119*, 9646–9655.

(47) Jain, S. K.; Juričić, V.; Barkema, G. T. Probing crystallinity of graphene samples via the vibrational density of states. *J. Phys. Chem. Lett.* **2015**, *6*, 3897–3902.

(48) Pool, A. J.; Jain, S. K.; Barkema, G. T. Structural characterization of carbon nanotubes via the vibrational density of states. *Carbon* **2017**, *118*, 58–65.

(49) Jain, S. K.; Juričić, V.; Barkema, G. T. Boundaries determine the formation energies of lattice defects in two-dimensional buckled materials. *Phys. Rev. B* **2016**, *94*, 020102(R).

(50) Jain, S. K.; Juričić, V.; Barkema, G. T. Structure of twisted and buckled bilayer graphene. *2D Mater.* **2016**, *4*, 015018.

(51) Jain, S. K.; Juričić, V.; Barkema, G. T. Probing the shape of a graphene nanobubble. *Phys. Chem. Chem. Phys.* **2017**, *19*, 7465–7470.

(52) Voronoi, G. Nouvelles Applications Des Paramtres Continus la Thorie Des Formes Quadratiques. *Journal for die reine und angewandte Mathematik* **1908**, 97102.

(53) Barkema, G. T.; Mousseau, N. High-quality continuous random networks. *Phys. Rev. B* **2000**, *62*, 4985–4990.

(54) Guinea, F. Strain engineering in graphene. *Solid State Commun.* **2012**, *152*, 1437 – 1441, Exploring Graphene, Recent Research Advances.