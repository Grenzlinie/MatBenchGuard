PHYSICAL REVIEW B 66, 115207 (2002)

# Properties of two-dimensional photonic crystals in elastomers

Hiroyuki Takeda and Katsumi Yoshino

Department of Electronic Engineering, Graduate School of Engineering, Osaka University,
2-1 Yamada-oka, Suita, Osaka 565-0871, Japan
(Received 14 March 2002; published 27 September 2002)

Properties of two-dimensional photonic crystals in elastomers are theoretically demonstrated. The locations of the rods periodically change with outer vibrations under the influence of the elasticities of elastomers. We have performed calculations of the photonic crystals composed of GaAs rods of square lattices in silicone elastomers for the TM mode ($E$ polarization). The band schemes of the photonic crystals significantly change and the band gaps periodically open and close with vibrations in the case of the existence of elastomers. They also depend on the directors of the change of the rods. On the other hand, guided modes appear in the case of the existence of elastomers in a certain array. These properties may provide novel applications to optical modulators.

DOI: 10.1103/PhysRevB.66.115207

PACS number(s): 42.70.Qs

## I. INTRODUCTION

Recently, two-dimensional periodic dielectric structures have attracted much attention as photonic crystals from both fundamental and practical viewpoints, because novel concepts such as photonic band gaps (PBG's) have been predicted, and also various new applications of photonic crystals have been proposed.$^{1-3}$ In earlier work, two fundamentally new optical principles, namely, the localization of light$^{4-6}$ and the controllable inhibition of spontaneous emission of light,$^{7-10}$ were considered to be the most important. The PBG's were inferred from similarities between electromagnetic waves and electron waves in solid states. The wavelengths of the electron waves in crystals mostly correspond to lattice constants, which causes Bragg diffractions and electronic band gaps. Similarly, the dielectric lattice constants corresponding to the wavelengths of electromagnetic waves cause the appearance of PBG's. Therefore, it is important to learn a lot from solid states in studies of photonic crystals.

In solid states, for example, atoms mutually interact and phonons play important roles and affect the electronic states. Moreover, there exist dispersion relations between frequencies of vibrations and propagations of elastic waves, and the frequencies greatly depend on the propagations. In conventional photonic crystals, however, none of the above interactions exist among dielectric materials.

Thus, we propose the use of elastomers as backgrounds of photonic crystals. Due to the elastomers, elastic waves propagate in the photonic crystals. Therefore, the dielectric materials can vibrate with outer vibrations. The band structures greatly depend on the locations of dielectric materials. Naturally, the properties of band structures also change due to the changes of the locations of dielectric materials with vibrations. Some of the most important characteristics of optical devices are tunability and modulation. Even if there exist superior properties such as wide PBG's and the existence of guided modes in photonic crystals, applications to optical devices are limited without tunability and modulation. As mentioned above, however, one can modulate the properties of photonic crystals with outer vibrations due to the elasticities of elastomers. Therefore, photonic crystals in elastomers may provide novel applications to optical modulators. Although three-dimensional periodic structures of elastomers have been formed by the infiltration method,$^{11}$ no detailed theoretical studies have been carried out thus far.

In this report, we perform calculations of two-dimensional photonic crystals composed of GaAs rods of square lattices in silicone elastomers. Two-dimensional photonic crystals have been expected for applications to optical devices, because of ease of fabrication. We demonstrate photonic crystals only in the TM mode ($E$ polarization) although both the TM mode and the TE ($H$ polarization) mode exist in two-dimensional photonic crystals, because photonic crystals with square lattices possess wider PBG's in the case of the TM mode than in the case of the TE mode. For larger changes of the locations of rods, the photonic crystals of square lattices are more appropriate than those of triangular lattices because photonic crystals of square lattices possess wide PBG's with rods whose radii are small, while those of triangular lattices possess wide PBG's with rods whose radii are large. The properties of photonic crystals change markedly as the changes of the locations of rods become larger. Therefore, we adopt the photonic crystals of square lattices in which the locations of rods change more significantly. For two-dimensional photonic crystals in elastomers, we take as the simplest model the concept that rods in elastomers are mutually connected with springs under the influence of elasticities of the elastomers, which causes regular, periodic changes of the locations of rods with time. We consider two cases, that is, the case in which elastomers exist throughout and the case of the existence of elastomers in a certain array.

## II. THEORY

In order to determine photonic band structures of photonic crystals in elastomers, we start with the wave equation satisfied by the magnetic field for two-dimensional periodic structures

$$
\nabla \times\left\{\boldsymbol{\epsilon}^{-1}(\mathbf{r}) \nabla \times \mathbf{H}(\mathbf{r})\right\}=\frac{\omega^{2}}{c^{2}} \mathbf{H}(\mathbf{r}), \tag{1}
$$

0163-1829/2002/66(11)/115207(6)/$20.00

66 115207-1

©2002 The American Physical Society

where $\nabla \cdot \mathbf{H}(\mathbf{r})=0$. The dielectric constant $\boldsymbol{\epsilon}(\mathbf{r})=\boldsymbol{\epsilon}(\mathbf{r}+\mathbf{R})$ is periodic with respect to the lattice vector $\mathbf{R}$ generated by the primitive translation and it may be expanded in a Fourier series on $\mathbf{G}$, the reciprocal lattice vector

$$
\boldsymbol{\epsilon}(\mathbf{r})=\sum_{\mathbf{G}} \boldsymbol{\epsilon}(\mathbf{G}) \exp (i \mathbf{G} \cdot \mathbf{r}). \tag{2}
$$

Equation (1) comprises a set of three coupled differential equations with periodic coefficients. In two-dimensional photonic crystals, we can define $\mathbf{e}_{\mathbf{G}}$ as the director which is perpendicular to the axes of the rods. Using Bloch's theorem, we may expand the magnetic field as

$$
\mathbf{H}(\mathbf{r})=\sum_{\mathbf{G}} h(\mathbf{G}) \mathbf{e}_{\mathbf{G}} \exp \{i(\mathbf{k}+\mathbf{G}) \cdot \mathbf{r}\} \tag{3}
$$

in the case of the TM mode ($E$ polarization). Inserting Eqs. (2) and (3) into Eq. (1) and multiplying by $\mathbf{e}_{\mathbf{G}}$ result in the following infinite matrix eigenvalue problem:

$$
\sum_{\mathbf{G}^{\prime}} H_{\mathbf{G}, \mathbf{G}^{\prime}} h\left(\mathbf{G}^{\prime}\right)=\frac{\omega^{2}}{c^{2}} h(\mathbf{G}), \tag{4a}
$$

where

$$
H_{\mathbf{G}, \mathbf{G}^{\prime}}=\boldsymbol{\epsilon}^{-1}\left(\mathbf{G}-\mathbf{G}^{\prime}\right)|\mathbf{k}+\mathbf{G}|\left|\mathbf{k}+\mathbf{G}^{\prime}\right|. \tag{4b}
$$

For numerical purposes, Eq. (4a) is truncated by retaining only a finite number of reciprocal lattice vectors. The main numerical problem in obtaining the eigenvalue is the evaluation of the Fourier coefficients of the inverse dielectric constants in Eq. (4b). The best method is to calculate the matrix of Fourier coefficients of real space constants and then take its inverse in order to obtain the required Fourier coefficients. This method was shown by Ho, Chan, and Soukoulis (HCS).$^{12}$

In the case where elastomers exist throughout, the simplest model in which the rods in elastomers are mutually connected with springs is shown in Fig. 1. We define the displacement of a rod at $(ma,na)$ in the $x$-$y$ coordinates as

$$
\mathbf{u}_{m, n}=\mathbf{u}^{(0)} \exp \left\{i\left(q_{x} m a+q_{y} n a-\Omega t\right)\right\}, \tag{5}
$$

where $q_{x}$ and $q_{y}$ are the wave vectors of elastic waves, $\Omega$ is the frequency of elastic waves, and $a$ is the lattice constant of conventional photonic crystals. The rod at $(ma,na)$ satisfies the following equation of motion:

$$
\begin{aligned}
M \frac{d^{2} \mathbf{u}_{m, n}}{d t^{2}}= & k\left(\mathbf{u}_{m+1, n}+\mathbf{u}_{m-1, n}-2 \mathbf{u}_{m, n}\right) \\
& +k\left(\mathbf{u}_{m, n+1}+\mathbf{u}_{m, n-1}-2 \mathbf{u}_{m, n}\right), \tag{6}
\end{aligned}
$$

where $M$ and $k$ are the mass of a rod and the spring constant, respectively. By inserting Eq. (5) into Eq. (6), we can obtain the following dispersion relation with respect to $q_{x}, q_{y}$ and $\Omega$:

$$
\Omega=2 \sqrt{\frac{k}{M}\left\{\sin ^{2}\left(\frac{q_{x} a}{2}\right)+\sin ^{2}\left(\frac{q_{y} a}{2}\right)\right\}}. \tag{7}
$$

![](./images/812452545682210817_1.jpg)

FIG. 1. Schematic diagram of two-dimensional photonic crystals constituted by GaAs rods of square lattices in the case of existence of silicone elastomers throughout at (a) $\mathbf{u}^{(0)}=(0.25a,0.25a)$ and (b) $\mathbf{u}^{(0)}=(0.3a,0)$. Lengths of arrows indicates those of displacements of locations of rods at $t=T/4$.

Because the frequency $\Omega$ is maximum at $(q_x,q_y)$ $=(\pi/a,\pi/a)$, we consider the propagations only at $(q_x,q_y)=(\pi/a,\pi/a)$. We suppose that dielectric indices of GaAs rods and silicone elastomers are $\epsilon_1=11.4$ and $\epsilon_2$ $=1.96$, respectively, and the radius of the rod is $r=0.2a$. Figures 1(a) and 1(b) indicate the displacements of rods at amplitudes of $\mathbf{u}^{(0)}=(0.25a,0.25a)$ and $\mathbf{u}^{(0)}=(0.3a,0)$, respectively. The shaded regions correspond to elastomers. We adopt the imaginary part of $\mathbf{u}_{m,n}$, thus $\mathbf{u}_{m,n}$ is zero at $t=0$. The lengths of arrows in Figs. 1(a) and 1(b) correspond to those of displacements at $t=T/4$ where $T=2\pi/\Omega$, and the rods drawn by dashed lines indicate the locations at that time. We note that the region embedded in dashed lines becomes a unit cell at $t\neq0$, that is, the primary vectors of lattices change from $\mathbf{a}_1=(1,0)a$ and $\mathbf{a}_2=(0,1)a$ at $t=0$ to $\mathbf{a}_1=(1,1)a$ and $\mathbf{a}_2=(-1,1)a$ at $t\neq0$. The eigenfrequencies

![](./images/812452545682210817_2.jpg)

FIG. 2. Schematic diagram of two-dimensional photonic crystals constituted by GaAs rods of square lattices in the case of existence of silicone elastomers in a certain array at $\mathbf{u}^{(0)}=(0,0.3a)$. Lengths of arrows indicates those of displacements of locations of rods at $t=T/4$.

computed with the HCS method for 245 plane waves are estimated to be in error less than 1 % in the case where elastomers exist throughout.

In the case of the existence of elastomers in a certain array, on the other hand, the simplest model in which the rods in a certain array are mutually connected with springs is shown in Fig. 2. We suppose that the dielectric indices of the backgrounds except elastomers are the same as those of silicone elastomers. We define the displacement of the rod at $(0,na)$ in the $x$-$y$ coordinates as
$$
\mathbf{u}_{n}=\mathbf{u}^{(0)} \exp \left\{i\left(q_{y} n a-\Omega t\right)\right\}. \tag{8}
$$

The rod at $(0,na)$ satisfies the following equation of motion:
$$
M \frac{d^{2} \mathbf{u}_{n}}{d t^{2}}=k\left(\mathbf{u}_{n+1}+\mathbf{u}_{n-1}-2 \mathbf{u}_{n}\right). \tag{9}
$$

By inserting Eq. (8) into Eq. (9), we obtain the following dispersion relation with $q_{y}$ and $\Omega$:
$$
\Omega=2 \sqrt{\frac{k}{M}}\left|\sin \left(\frac{q_{y} a}{2}\right)\right|. \tag{10}
$$

Because the frequency $\Omega$ is maximum at $q_{y}=\pi/a$, we consider the propagations only at $q_{y}=\pi/a$. Figure 2 indicates the displacements of rods at amplitudes of $\mathbf{u}^{(0)}=(0,0.3)a$. The shaded regions correspond to elastomers. We adopt the imaginary part of $\mathbf{u}_{n}$, thus $\mathbf{u}_{n}$ is zero at $t=0$. The lengths of the arrows in Fig. 2 correspond to those of displacements at $t=T/4$ where $T=2\pi/\Omega$, and the rods drawn by dashed lines indicate the locations at that time. The structure in Fig. 2 is not essentially periodic, however, we can use a supercell technique. We note that the region embedded in dashed lines becomes a unit cell at $t\neq0$. For the structure considered here, the interval between arrays of elastomers is $ma$. In this calculation, we take $m=8$. Then the primary vectors of the supercell are $\mathbf{a}_{1}=(m+1,0)a$ and $\mathbf{a}_{2}=(0,2)a$. $\mathbf{a}_{1}$ indicates the sum of an array and an interval between arrays. The eigenfrequencies computed with the HCS method for 441 plane waves are estimated to be in error less than 1% in the case of the existence of elastomers in a certain array.

Moreover, $k$ is approximately $0.5(N/m)$ in conventional elastomers, the density of GaAs is $\rho=5.71$ (kg/m$^{3}$) and $M$ is $\rho \pi r^{2}h$, where $h$ is the height of the rod. From $r\sim1$ $\mu$m and $h\sim10$ $\mu$m, $\Omega/2\pi\sim100$ MHz can be obtained in the experimental studies. Therefore, $\omega/2\pi\gg\Omega/2\pi$ is satisfied because the frequency of light is $\omega/2\pi\sim c/a\sim10$ THz, which shows that we can use above the plane-wave expansion method based on steady states even if the locations of rods temporarily change.

![](./images/812452545682210817_3.jpg)

FIG. 3

FIG. 3. Band structure of two-dimensional photonic crystals constituted by GaAs rods of square lattices in the case of existence of silicone elastomers throughout at $t=0$.

### III. NUMERICAL CALCULATION AND DISCUSSION

In Fig. 3, we present the band scheme of conventional photonic crystals composed of GaAs rods of square lattices in silicone elastomers at $t=0$ in the TM mode. Figure 3 shows that this photonic crystal possesses a PBG and dispersion relations between wave vectors and frequencies. We perform calculations of photonic crystals in the case where elastomer exist throughout. However, it is difficult to compare properties of photonic crystals by dispersion relations because the unit cell changes at $t\neq0$ as mentioned above. Therefore, we determine the properties by calculations of the density of states (DOS) values which are obtained at 1521 k points inside the first Brillouin zone for square lattices.

Figure 4(a) indicates the DOS of photonic crystals at $\mathbf{u}^{(0)}=(0.25a,0.25a)$ for $t$ changes from 0 to $T/4$. For $t$ $\geqslant T/4$, the properties repeat the same changes. In Fig. 4(a), it is shown that the band gap at the frequencies of $(0.28-0.33)2\pi c/a$ at $t=0$ decreases and becomes zero as $t$ increases. We display the dependence of the band gap to the midgap on $t$ changing from 0 to $T/4$ in Fig. 4(b). Figure 4(b) indicates that the bandgap periodically opens and closes with time $T$. Moreover, we note that the DOS values decrease around the frequency of $0.216(2\pi c/a)$, which corresponds

![](./images/812452545682210817_4.jpg)

FIG. 4. (a) DOS of two-dimensional photonic crystals consti- tuted by GaAs rods of square lattices on $t$ changing 0 to $T/4$ at $\mathbf{u}^{(0)}=(0.25a,0.25a)$. (b) Dependence of bandgap to midgap on $t$ changing 0 to $T/4$ at $\mathbf{u}^{(0)}=(0.25a,0.25a)$.

to a frequency $1/\sqrt{2}$ times as large as the center of band gap frequencies of $(0.28-0.33)2\pi c/a$. This is because the prop- erties of the unit cell composed of $|\mathbf{a}_{1}|=|\mathbf{a}_{2}|=\sqrt{2}a$ become stronger than those of the unit cell composed of $|\mathbf{a}_{1}|=|\mathbf{a}_{2}|$ $=a$ as $t$ changes from 0 to $T/4$. More remarkable changes are shown in Fig. 5(a), which indicates the DOS of photonic crystals at $\mathbf{u}^{(0)}=(0.3a,0)$ on $t$ changing from 0 to $T/4$. A new band gap appears around the frequency of $0.216(2\pi c/a)$, while the band gap at frequencies of $(0.28-0.33)2\pi c/a$ at $t=0$ decreases for $t$ changing from 0 to $T/4$. We define the former and latter band gaps as the first band gap and second band gap, respectively. Figure 5(b) shows for the first and second band gaps the dependences of bandgaps to midgaps on $t$ changing from 0 to $T/4$. Figure 5(b) also shows that the two bandgaps periodically open and close with time. The biggest difference between Figs. 4 and 5 is the changes of the DOS around the frequency of $0.216(2\pi c/a)$, that is, the DOS values in the latter become zero although those in the former do not become zero.

The changes of the DOS greatly depend on those of the locations of rods. At $t=T/4$, the rods represented by dotted lines in Fig. 1(a) are separately arranged, while the two rods in Fig. 1(b) are closely arranged. In band structures, the first and second bands are called dielectric and air bands, respec- tively. The electric fields tend to remain at isolated dielectric spots in the case of the TM modes. Electric fields tend to remain at each separated rod in the case of Fig. 1(a), while they tend to remain at the two closer rods as $t$ approaches $T/4$ in the case of Fig. 1(b), that is, electric energies remain at more isolated dielectric spots in Fig. 1(b) than in Fig. 1(a). This makes the dielectric and air bands separate, and a band gap appears between the first and second bands. Therefore, the band gap appears around the frequency of $0.216(2\pi c/a)$ in Fig. 1(b). A more detailed explanation of the above inter- pretation is given in Ref. 13. The finding means that one can obtain desirable optical modulators by controlling the direc- tors of changes of rods and bring further information to light by opening and shutting of band gaps periodically with time.

![](./images/812452545682210817_5.jpg)

FIG. 5. (a) DOS of two-dimensional photonic crystals consti- tuted by GaAs rods of square lattices on $t$ changing 0 to $T/4$ at $\mathbf{u}^{(0)}=(0.3a,0)$. (b) Dependence of bandgap to midgap on $t$ chang- ing 0 to $T/4$ at $\mathbf{u}^{(0)}=(0.3a,0)$.

In the case of the existence of elastomer in a certain lim- ited array, on the other hand, we can obtain guided modes in photonic crystals. It is well known that guided modes appear with the elimination of rods in an array. $^{14}$ As mentioned above, however, the periodicity in the $y$ direction changes to double at $t\neq 0$, as shown in Fig. 2. The guided modes propa- gate in the (01) direction. In Fig. 6, we present the guided mode dispersion relations in the band gap for the TM mode.


![](./images/812452545682210817_6.jpg)

FIG. 6. Guided mode dispersion relations in the bandgap for the TM mode.

The shaded regions correspond to crystal bulk bands. We note that wave vectors become half those of conventional photonic crystals due to double periodicity.

As is shown in Fig. 6, there exist solutions in the band gaps. These solutions decay on both sides of the bulk, that is, these modes become guided modes because they exist only in a certain array. The arrows in this figure indicate the changes of guided modes for $t$ changing from 0 to $T/4$. For $t\geqslant T/4$, the properties of guided modes also repeat the same changes. In conventional photonic crystals with eliminations of arrays, there exists only one mode in the band gap. The remarkable difference from conventional photonic crystals is that two modes exist at a certain time. This is because the periodicity in the $y$ direction changes to double, and continuous guided modes for conventional photonic crystals in the range from $ka/2\pi c=0$ to $ka/2\pi c=0.5$ become discontinuous at a certain wave vector.

Figure 7 shows the TM guided mode behavior as a function of $t$ for $t$ changing from 0 to $T/4$ at $ka/2\pi c=0.1$. The shaded regions correspond to crystal bulk bands. As is shown in this figure, two guided modes appear as $t$ increases. Figures 6 and 7 show that the two guided modes tend to remain in the center of the band gap as $t$ increases, that is, they become more stable. This means that electric fields parallel to the rods tend to localize at the two closer rods in Fig. 2 as $t$ approaches $T/4$. In the case of the TM mode, electric fields parallel to rods tend to remain at isolated dielectric spots, and the electric energies also tend to remain at those spots. $^{13}$ Therefore, stronger guided modes appear in the band gap. These results mean that one can bring further information to light by periodic modulation with time even for guided modes.

The devices in which optical properties are changed by the use of vibrations of transducers are well known as acoustooptic devices. These devices are very important with respect to optical modulators that bring further information to light in the field of optical communications. For example, the devices that periodically stop the flow of lights by mechanical movements are known as optical choppers. Due to the mechanical movements, however, the modulation frequencies are at most 1–10 kHz. As mentioned above, modulation frequencies of photonic crystals in elastomers are about 100 MHz. One of the most important properties of photonic crystals is that they have complete band gaps for any direction of light. Therefore, we can expect to realize optical choppers superior to conventional ones. Even if photonic crystals in elastomers have no band gaps, the DOS values can be changed by vibrations of transducers, which means that the transmission power of light from any direction can be modulated. In optical communications, moreover, it is also important that the directions of lights can be controlled. By the use of guided modes, we can bend the flow of light. $^{14}$ Under the influence of elastomers, we can also modulate the flows of the lights. These properties may provide novel applications to optical devices.

![](./images/812452545682210817_7.jpg)

FIG. 7. TM guided mode behavior as a function of $t$ for $t$ changes 0 to $T/4$ at $ka/2\pi c=0.1$.

## IV. CONCLUSION

In conclusion, we demonstrated band schemes of photonic crystals composed of GaAs rods of square lattices in silicone elastomers for the TM mode ($E$ polarization). We found that the band schemes of photonic crystals greatly change, and the band gaps periodically open and close with vibrations in the case where elastomers exist throughout. They also depend on the directors of change of the rods. On the other hand, it is also found that guided modes appear in the case of the existence of elastomers in a certain limited array and that there exist two modes in the bandgap at a certain time because the periodicity become double. These properties may provide novel applications to optical modulators, not only for band gaps but also for guided modes.

## ACKNOWLEDGMENTS

This work was partly supported by a Grant-in-Aid for Scientific Research from the Ministry of Education, Culture, Sports, Science and Technology and from the Japan Society for the Promotion of Science and by a NEDO International Joint Research Grant.

$^{1}$S. John, Phys. Rev. Lett. $\textbf{58}$, 2486 (1987).

$^{2}$E. Yablonovitch, Phys. Rev. Lett. $\textbf{58}$, 2059 (1987).

$^{3}$S. John and T. Quang, Phys. Rev. Lett. $\textbf{74}$, 3419 (1995).

$^{4}$S. John, Phys. Rev. Lett. $\textbf{53}$, 2169 (1984).

$^{5}$A.Z. Genack and N. Garcia, Phys. Rev. Lett. $\textbf{66}$, 2064 (1991).

$^{6}$D. Wiersma, P. Bartolini, A. Lagendijk, and R. Righini, Nature (London) $\textbf{390}$, 671 (1997).

$^{7}$V.P. Bykov, Sov. J. Quantum Electron. $\textbf{4}$, 861 (1975).

$^{8}$S. John and J. Wang, Phys. Rev. Lett. $\textbf{64}$, 2418 (1990).

$^{9}$S. John and T. Quang, Phys. Rev. A $\textbf{50}$, 1764 (1994).

$^{10}$T. Quang, M. Woldeyohannes, S. John, and G.S. Agarwal, Phys. Rev. Lett. $\textbf{79}$, 5238 (1997).

$^{11}$K. Yoshino, Y. Kawagishi, M. Ozaki, and A. Kose, Jpn. J. Appl. Phys. $\textbf{38}$, L786 (1999).

$^{12}$K.M. Ho, C.T. Chan, and C.M. Soukoulis, Phys. Rev. Lett. $\textbf{65}$, 3152 (1990).

$^{13}$J.D. Joannopoulos, R.D. Meade, and J.N. Winn, *Photonic Crys- tals* (Princeton University Press, Princeton, 1995).

$^{14}$A. Mekis, S. Fan, and J.D. Joannopoulos, Phys. Rev. B $\textbf{58}$, 4809 (1998).