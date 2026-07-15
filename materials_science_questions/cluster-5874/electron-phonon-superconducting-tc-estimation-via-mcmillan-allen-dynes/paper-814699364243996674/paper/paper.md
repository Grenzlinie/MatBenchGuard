# Phase with pressure-induced shuttlewise deformation in dense solid atomic hydrogen

Takahiro Ishikawa, $^{1,*}$ Hitose Nagara, $^{2}$ Tatsuki Oda, $^{3}$ Naoshi Suzuki, $^{4}$ and Katsuya Shimizu $^{1}$

$^{1}$ Center for Science and Technology under Extreme Conditions, Osaka University, 1-3 Machikaneyama, Toyonaka, Osaka 560-8531, Japan
$^{2}$ Department of Applied Mathematics and Physics, Tottori University, 4-104 Koyama-cho-minami, Tottori, Tottori 680-8552, Japan
$^{3}$ Institute of Science and Engineering, Kanazawa University, Kakuma, Kanazawa 920-1192, Japan
$^{4}$ Department of Pure and Applied Physics, Faculty of Engineering Science, Kansai University, 3-3-35 Yamate, Suita, Osaka 564-8680, Japan

(Received 19 May 2013; revised manuscript received 31 July 2014; published 5 September 2014)

A phase which shows pressure-induced shuttlewise structural deformation between orthorhombic $Fddd$ and tetragonal $I4_1/amd$ structures has been predicted in solid atomic hydrogen by means of the first-principles calculations, including harmonic zero-point energy contributions of proton motions. The $Fddd$ structure is formed by shear distortion from the $I4_1/amd$ structure, and the angle specifying the distortion changes with pressure in the range 84-96$^\circ$ around 90$^\circ$, which corresponds to $I4_1/amd$. In the shuttlewise deforming phase, the electron-phonon interaction is enhanced owing to phonon softenings, which brings about superconductivity at elevated temperatures.

DOI: 10.1103/PhysRevB.90.104102
PACS number(s): 61.50.Ah, 61.50.Ks, 61.66.Bi, 62.50.$-$p

## I. INTRODUCTION

Hydrogen has attracted much scientific interest because it has the simplest electronic structure of all elements and is the most abundant element in the universe. However, its physical behaviors under high pressure (i.e., structural phase transitions, insulator-to-metal transition, superconducting transition, etc.) have not been sufficiently clarified owing to the experimental difficulty [1]. At low temperatures, the molecules forming solid hydrogen are in a spherical rotational state on the close-packed lattice (phase I) [2], and the state transforms into the broken-symmetry states (phase II) at around 110 GPa [3], in which the spherical rotational state changes to an anisotropic one owing to the intermolecular interactions. By further compression below 125 K, it transforms into another state (phase III) at around 155 GPa [4,5], accompanying large discontinuities in vibron frequencies. Very recently, a new phase (phase IV) has been discovered at 220 GPa and 300 K by Raman and visible transmission spectroscopy, where the structure has been thought to be an orthorhombic $Pbcn$ structure forming a mixture of molecular and atomic hydrogens [6].

On another front, first-principles studies, which fill up the insufficiency of experimental data, predict that a hexagonal $P6_3/m$ is slightly more stable up to around 105 GPa than $Cmc2_1$ [7,8], $Pca2_1$ [3,9-11], $P2_1/c$ [12], and $Pa3$ type [13,14], and then a monoclinic $C2/c$ of a layered structure prevails to around 270 GPa [15]. Vibrational spectra of $C2/c$ agree somewhat well with the experimental Raman data collected from phase III [15]. The $C2/c$ structure is predicted to transform into an orthorhombic $Cmca$ with a primitive cell containing 12 atoms ($Cmca$-12) and into another $Cmca$ with a primitive cell containing four atoms ($Cmca$-4) by further compression [15]. Subsequent transition into an exotic quasimolecular $mC24$ structure is expected at around 470 GP, which has a space group of a monoclinic $C2/c$ [16]. Above 590 GPa, an atomic metallic phase of a tetragonal $I4_1/amd$, which is the same as the structure of cesium phase IV (Cs-IV), is predicted to become the most stable structure [16,17]. The tetragonal $I4_1/amd$ prevails over a wide range of pressure and transforms into another atomic phase with a space group of an orthorhombic $Cmcm$, called $oC12$ structure, above 2100 GPa [16]. A trigonal $R\overline{3}m$ structure with an ABC stacking is also predicted as another higher-pressure structure, which transforms into the face-centered-cubic structure near 3500 GPa [17].

The experimentally reported drop of the melting temperature of hydrogen with increase of pressure above 100 GPa [18] is another interesting problem, but its behavior at further high pressures is still unclear. There remains a possibility that the dropping is suppressed in an extremely high-pressure region, such as dense sodium [19]. Hence, in the present study, we search for the crystal structures of dense solid hydrogen via a first-principles genetic algorithm (GA) technique [20-24] and compare the enthalpies including zero-point energy (ZPE) contributions of proton motions. We also study the superconducting properties among candidate structures in the pressure region from 430 to 2400 GPa.

## II. COMPUTATIONAL DETAILS

We used a homemade GA code which has been developed along the line proposed by Glass *et al.* [25], and combined it with the QUANTUM ESPRESSO (QE) code [26] which is based on density functional theory and uses plane-wave basis functions and pseudopotentials. In our GA search, we carried 10 structures in each generation, where five structures are created by "crossover" and the others by "mutation." We continued the simulation up to 50 generations at the pressure of 400 GPa using a 16-atom system. The generalized gradient approximation by Perdew, Burke and Ernzerhof [27] was used for the exchange-correlation functional, and the Rabe-Rappe-Kaxiras-Joannopoulos ultrasoft pseudopotential [28] was employed. The $k$-space integration over the Brillouin zone (BZ) was performed on a $6\times6\times6$ grid, and the energy cutoff of the plane-wave basis was set at 80 Ry.

For the calculation of enthalpy including the ZPE contribution, we first determined the stable structure by the

*ishikawa@stec.es.osaka-u.ac.jp

optimization at a given pressure and obtained the static total energy $E_{\text{static}}$ and the volume $V$. We subsequently calculated ZPE for the optimized structures within the harmonic approximation, $E_{\text{ZP}}$, as follows:

$$
E_{\mathrm{ZP}}=1 / 2 \sum_{\mathbf{q}, j} \hbar \omega_{\mathbf{q}, j}, \tag{1}
$$

where $\omega_{\mathbf{q}, j}$ is the phonon frequency of the $j$th mode at wave vector $\mathbf{q}$ in BZ. The frequency $\omega_{\mathbf{q}, j}$ was computed by the density functional perturbation theory (DFPT) for lattice dynamics, which is implemented in the QE code [26]. We also calculated $E_{\text{static}}$ and $E_{\text{ZP}}$ for the structures slightly expanded and compressed against the optimized structure and estimated the pressure $P$ and enthalpy $H$ with the inclusion of the ZPE contribution as follows:

$$
P=-\frac{\partial\left(E_{\text {static }}+E_{\mathrm{ZP}}\right)}{\partial V} \tag{2}
$$

and

$$
H=\left(E_{\text {static }}+E_{\mathrm{ZP}}\right)+P V, \tag{3}
$$

where the derivative was estimated from the slope of a quadratic curve fitted to the three data points.

The superconducting transition temperature $T_{\mathrm{c}}$ was estimated by the use of the Allen-Dynes formula [29],

$$
T_{\mathrm{c}}=\frac{\omega_{\log }}{1.2} \exp \left[-\frac{1.04(1+\lambda)}{\lambda-\mu^{*}(1+0.62 \lambda)}\right]. \tag{4}
$$

In Eq. (4), the parameters of electron-phonon coupling constant $\lambda$ and logarithmic-averaged phonon frequency $\omega_{\log }$ represent a set of characters for the phonon-mediated superconductivity. We calculated the parameters using the QE code, while we assumed the value of the screened Coulomb interaction constant, $\mu^{*}=0.089$, which is deduced as a reasonable value for atomic metallic hydrogen by Richardson and Ashcroft [30].

## III. RESULTS AND DISCUSSIONS

### A. Application of genetic algorithm

Figure 1(a) shows the results of the crystal structure search by GA at 400 GPa, in which enthalpies of structures at each generation are plotted. Among the ten structures randomly created at the zeroth generation, the lowest enthalpy structure consisted of $\mathrm{H}_{2}$ molecules. At later generations, a structure consisting of partially dissociated $\mathrm{H}_{2}$ molecules became the lowest enthalpy structure, and finally an atomic structure, in which no $\mathrm{H}_{2}$ molecules are remaining, was obtained as a lowest enthalpy structure from the 26th through 50th generations. The obtained structure has an orthorhombic $F d d d$ space group [Fig. 1(b)], and the lattice parameters are as follows: $a=3.54$ a.u., $b / a=0.9063$, and $c / a=1.6660$. The atoms are located on the $8 a$ site, and the nearest-neighbor atomic distance is 1.90 a.u., which is longer than the atomic distance in the molecule at ambient pressure. The $F d d d$ structure is characterized by an angle $\theta$ defined in Fig. 1(b), and the value of $\theta$ is $95.6^{\circ}$ for the above lattice parameters. At $\theta=90^{\circ}$, the structure becomes the Cs-IV structure, and hence $F d d d$ is regarded as a distorted Cs-IV structure. The electronic band structure, which is nearly the same as that of the Cs-IV structure, shows that hydrogen in the $F d d d$ structure is metallic.

![](./images/814699364243996674_1.jpg)

FIG. 1. (Color online) (a) Evolution of the enthalpy in the first-principles GA searching. (b) Orthorhombic $F d d d$ structure obtained by the searching.

### B. Total-energy curve with respect to the change of angle $\theta$

The $F d d d$ structure was recently reported by Geng $e t$ al. [31], but the detailed study of the structural and energetic relationship between $F d d d$ and Cs-IV at each pressure has not been reported. Therefore, we investigated $F d d d$ further by calculating its total energy as a function of the angle $\theta$ under constant volume condition (Fig. 2). In this calculation, we used a primitive cell consisting of four hydrogen atoms and increased the number of the $k$-point samplings to $48 \times 48 \times 24$. First the lattice parameters of the structure with $\theta=90^{\circ}$, i.e., Cs-IV, were optimized at pressures of 400, 1400, and 2400 GPa, and then $\theta$ was changed continuously from $80^{\circ}$ to $100^{\circ}$ with the volume fixed. Here, $a$ and the $b / a$ ratio were changed according to the $\theta$ value, and the $c / a$ ratio was fixed at the value optimized for $\theta=90^{\circ}$ because the total-energy curve is less affected by the change of $c / a$. At the volume of 7.14 a.u. $^{3}$ /proton corresponding to the pressure of 400 GPa, the energy curve has a nearly flat bottom from 87 to $93^{\circ}$, and an extremely small local maximum at $90^{\circ}$ (see the inset of Fig. 2), which indicates the instability of the Cs-IV structure. The ripple on the energy curve grows with compression and at 3.87 a.u. $^{3}$ /proton corresponding to 2400 GPa, distinct local minima appear at 84, 87, 90, 93, and $96^{\circ}$ [32]. The total-energy landscape of $F d d d$ undergoes very little change for the above shear distortions around $90^{\circ}$ and there exist multiple local minima depending on pressure.

These features are the same as the prediction of Geng $e t$ al. [31] that dense hydrogen has many very broad and flat basins on the energy surface.

![](./images/814699364243996674_2.jpg)

FIG. 2. (Color online) Total-energy curves without ZPE as a function of the angle $\theta$ in $Fddd$ under constant volume condition. The volumes of 7.14, 4.96, and 3.87 a.u.³/proton approximately correspond to pressures of 400, 1400, and 2400 GPa, respectively. The structure at $\theta = 90^\circ$ is the Cs-IV structure. Inset: The closeup of the energy curve around $90^\circ$.

### C. Exploration of local minima for $\theta$ with inclusion of the zero-point energy

In our calculations shown so far, the ZPE contribution has been excluded. The ZPE is thought to be very important in light elements such as hydrogen. Here, we carefully study the $Fddd$ structure, taking ZPE into account, and search for stable $\theta$'s up to 2400 GPa. Geng *et al.* pointed out the importance of anharmonic zero-point motions for highly compressed atomic phases of hydrogen [31]. However, we show here the ZPE contributions for $Fddd$ in harmonic approximation because the details of the harmonic ZPE for the $Fddd$ structure have not yet been reported, while it is thought to be of some help for reliable predictions [17].

First, we explored the local minima of the enthalpy surface by the structural optimizations, starting from multiple $\theta$'s between $90^\circ$ to $100^\circ$ at a given pressure. We subsequently calculated $E_{\text{ZP}}$ using a $4 \times 4 \times 4$ $q$-point grid and obtained $P$ and $H$, including the ZPE contribution for optimized structures by the method described in Sec. II. The upper panel of Fig. 3 shows $\theta$'s corresponding to the local minima with the ZPE contribution. We found that up to four $\theta$'s of local minima exist at each pressure and the average value among them increases with increase of pressure. At the volume around the pressures of 430, 740, 1360, 1580, 1790, 1890, and 2000 GPa, the local minima reside only on $Fddd$ structures, and the Cs-IV structure ($\theta = 90^\circ$) takes a local maximum. The data points showing the lowest $H$ at each pressure are connected with a solid line in the upper panel. Repeating up and down, $\theta$ with the lowest $H$ gradually increases with increase of pressure and reaches approximately $96^\circ$ above 2000 GPa.

![](./images/814699364243996674_3.jpg)

FIG. 3. (Color online) The angles at the local minima of the $Fddd$ structure with inclusion of the ZPE contribution, where $\theta = 90^\circ$ corresponds to the Cs-IV structure. In the lower panel, the enthalpies of the local minima relative to that of Cs-IV are plotted. The data points of the lowest enthalpy at each pressure are connected with a solid line.

The lower panel of Fig. 3 shows $H$ at the local minima relative to that of Cs-IV. Though the phonon modes of Cs-IV become unstable at around 430, 740, 1360, 1580, 1790, 1890, and 2000 GPa, they show only small imaginary frequency and can be ignored in the calculation of $E_{\text{ZP}}$. The relative $H$ obtained is in the very small energy range from $-0.15$ to 0.15 mRy/proton, which means that the $Fddd$ and Cs-IV structures exist in the energy range corresponding to approximately 40 K.

From first-principles path-integral simulations, Biermann *et al.* predicted that the structure of hydrogen at very high pressures is diffuse due to the quantum effect [33]. Recently, Geneste *et al.* reported quantum nuclear zero-point motions of solid hydrogen and deuterium in phase II by first-principles path-integral molecular dynamics simulations and reported that only hydrogen shows large quantum fluctuations [34]. If such quantum nuclear zero-point motions are realized in the $Fddd$ and Cs-IV structures, the structures merge in a

![](./images/814699364243996674_4.jpg)

FIG. 4. (Color online) Comparison of the enthalpy relative to Cs-IV among $Fddd$, $Cmca$-$4$, $mC24$, $oC12$, and $R\bar{3}m$. The upper and lower panels show the enthalpy without and with the ZPE contribution, respectively. In the lower panel, the data points corresponding to the structure having imaginary phonon frequencies are eliminated.

single phase with the fluctuation center shifted from the Cs-IV. Therefore, the structures shown above are considered to be in a phase showing pressure-induced shuttlewise deformation between the $Fddd$ and Cs-IV structures.

### D. Enthalpy comparison

Next, we compared the enthalpy of the above phase with those of the structures predicted earlier without and with inclusion of the ZPE contributions. In Fig. 4, we plotted the enthalpies of $Fddd$, $Cmca$-$4$, $mC24$, $oC12$, and $R\bar{3}m$, relative to the Ca-IV structure, from 400 to 2400 GPa in 100 GPa intervals of pressure. The $k$-point samplings used in the calculations are as follows: a $24\times 24\times 24$ grid for $Cmca$-$4$, a $16\times 16\times 16$ grid for $mC24$, a $24\times 24\times 24$ grid for $oC12$, and a $48\times 48\times 24$ grid for $R\bar{3}m$. The upper panel shows the enthalpies excluding the ZPE contributions. The $Cmca$-$4$ structure has the lowest $H$ of all the structures at 430 GPa [35] and then $mC24$, the shuttlewise deforming phase, and $oC12$ emerge as the lowest enthalpy structures at 470, 590, and 2350 GPa, respectively. These pressures of structural transitions are almost consistent with those predicted earlier by the all-electron projector-augmented wave (PAW) method [16]. The $R\bar{3}m$ structure has higher enthalpy than $oC12$ by 0.3 mRy/proton at 2400 GPa, and the enthalpy difference is predicted to increase further above 2400 GPa.

With the inclusion of the ZPE contributions, the enthalpy landscape changes, as is shown in the lower panel of Fig. 4. In the figure, we plotted the data points at the pressures where the structure has stable phonon frequencies. The $q$-point samplings for the ZPE calculations were on a $4\times 4\times 4$ grid for $Cmca$-$4$, $oC12$, and $R\bar{3}m$, and a $2\times 2\times 2$ grid for $mC24$. The obtained values of $E_{ZP}$ are 22 mRy/proton at 500 GPa for Cs-IV, 24 mRy/proton at 500 GPa for $Cmca$-$4$, and 33 mRy/proton at 2200 GPa for $R\bar{3}m$, which are consistent with those reported by McMahon and Ceperley [17], and Takezawa *et al.* [36]. The increases of the pressure by the ZPE contributions are 5.3% for $Cmca$-$4$, 6.6% for $mC24$, 8.6% for Cs-IV, and 7.3% for $Fddd$ at 500 GPa, and 4.4% for $mC24$, 5.0% for Cs-IV, 5.0% for $Fddd$, 4.9% for $oC12$, and 4.1% for $R\bar{3}m$ at 1800 GPa. The ZPE contributions cause the increase of enthalpy difference among the structures and the destabilization of $Cmca$-$4$ and $mC24$ against the shuttlewise deforming phase over the entire pressure range investigated in the present study. We note here that by the inclusion of ZPE, the stability region of this shuttlewise deforming phase shifts to the pressure region, lower than 450 GPa, which may be attainable in present experimental studies.

Above 1790 GPa, the $oC12$ structure becomes mechanically stable and its enthalpy becomes the lowest of all the structures. In the pressure region above 2300 GPa, however, $oC12$ becomes mechanically unstable and $R\bar{3}m$ emerges as the most stable structure of the six structures.

### E. Superconductivity

The enhancement of the superconducting $T_{\rm c}$ can be expected in the structures with soft phonon modes, and the shuttlewise deforming phase is also included in them. Therefore, we calculated $T_{\rm c}$ of Cs-IV and $Fddd$ and investigated the superconductivity and its pressure dependency of the phase. Figure 5 shows $\lambda$, $\omega_{\rm log}$, and $T_{\rm c}$ for the two structures in the pressure range from 430 to 2400 GPa. The $k$-space integration for the calculations of the dynamical matrix and the electron-phonon matrix element at each $q$ point was performed over a $48\times 48\times 24$ grid for both Cs-IV and $Fddd$. The parameters, $\lambda$ and $\omega_{\rm log}$ were obtained by a $4\times 4\times 4$ $q$-point grid. In the estimation of $T_{\rm c}$, the increase of $\lambda$ from unity ($\lambda\geqslant 1$) works as an enhancement for $T_{\rm c}$ and $\omega_{\rm log}$ proportionally scales $T_{\rm c}$. The softening on the phonon mode is induced by a strong electron-phonon coupling (large $\lambda$), resulting in a decrease of $\omega_{\rm log}$. Therefore, $T_{\rm c}$ will be determined by a balance between $\lambda$ and $\omega_{\rm log}$.

In the pressure region approximately below 800 GPa, $\lambda$ and $\omega_{\rm log}$ increase and decrease with increase of pressure, respectively. The behavior indicates that the structure softens and soft phonon modes contribute to the enhancement of the electron-phonon coupling with compression, which is related to the flattening of the energy curve around $\theta=90^\circ$ shown in the top panel of Fig. 2. The superconducting $T_{\rm c}$ shows increase with compression in the pressure region for both Cs-IV and $Fddd$. Approximately above 900 GPa, the structure mechanically stabilizes owing to the emergence of the local minima with respect to $\theta$, and $\lambda$ and $\omega_{\rm log}$ show decrease and

![](./images/814699364243996674_5.jpg)

FIG. 5. (Color online) Superconductivity of Cs-IV, $Fddd$, and $oC12$: electron-phonon coupling constant $\lambda$ (top), logarithmicaveraged phonon frequency $\omega_{\log}$ (middle), and superconducting transition temperature $T_{\rm c}$ (bottom). $T_{\rm c}$ was estimated from the Allen-Dynes formula, in which the effective screened Coulomb repulsion constant is assumed to be $\mu^{*}=0.089$.

increase with compression, respectively. $T_{\rm c}$ reaches 327 K at 1150 GPa for Cs-IV and 328 K at 1360 GPa for $Fddd$, and then gradually decreases with further compression. These results can be compared with those by McMahon and Ceperlay in which their data are missing in the pressure range of 1500-2500 GPa [37,38]. In the pressure region below 1500 GPa, the values of $\lambda$, $\omega_{\log}$, and $T_{\rm c}$ show a good agreement with their results [38].

In the pressure range from 1500-1900 GPa, where the increase of the anharmonicity for Cs-IV is expected again (see the middle of Fig. 2) and $Fddd$ mainly emerges, $\lambda$ and $T_{\rm c}$ show re-increase with pressurization. $T_{\rm c}$ reaches the maximum value of 351 K with $\theta=90.2$-$90.3^{\circ}$ at the pressures of 1790 and 1890 GPa.

At around 2100 GPa, the results of $oC12$ are shown with those of Cs-IV and $Fddd$. For the calculations of $oC12$, we used a $24\times24\times24$ $k$-point grid and a $4\times4\times4$ $q$-point grid. Compared with the two structures, $\lambda$ of $oC12$ is larger by approximately 1.0 and its $\omega_{\log}$ is smaller by approximately 1200 K, which indicates that $oC12$ is softer than Cs-IV and $Fddd$. The superconducting $T_{\rm c}$ of $oC12$ is 293 K, which is not so different from those of Cs-IV and $Fddd$.

As we have shown in Sec. III C, the shuttlewise deforming phase has a width of 0.3 mRy/proton, corresponding to the temperature of 40 K, in the enthalpy landscape (see the lower panel of Fig. 4). This enthalpy width is much smaller than the superconducting $T_{\rm c}$, and it is difficult to determine the structure at the onset of the superconducting state at each pressure.

## IV. CONCLUSIONS

In summary, we searched for the crystal structure of highly compressed solid hydrogen using the first-principles GA technique and confirmed the orthorhombic $Fddd$ structure. This structure is created by a shear distortion of the earlierpredicted Cs-IV structure of a space group $I4_{1}/amd$, i.e., by the change of an angle $\theta$ from $90^{\circ}$. We found that the Cs-IV structure shows very little change in the total energy and enthalpy by the shear deformations. We carefully studied the pressure dependence of $\theta$ in the $Fddd$ structure from 400 to 2400 GPa, taking the harmonic ZPE contributions into account, and obtained up to four local minima of the enthalpy surface as a function of $\theta$ at each pressure. The Cs-IV structure takes the local maximum at some pressures, which indicates that the structure repeatedly changes between Cs-IV and $Fddd$ with increase of pressure. The general trend of the $\theta$ value of $Fddd$ at the lowest enthalpy gradually gets larger with compression in the range 90-$96^{\circ}$.

The difference of the enthalpies with inclusion of the ZPE contributions is less than 0.3 mRy/proton among the $Fddd$ and $I4_{1}/amd$ structures. Therefore, the atomic metallic phase of solid hydrogen is considered to be a single phase showing pressure-induced shuttlewise deformation between the $Fddd$ and $I4_{1}/amd$ structures.

We compared the enthalpy with inclusion of the ZPE contribution among $Fddd$, Cs-IV, and the earlier-predicted $Cmca$-$4$, $mC24$, $oC12$, and $R\overline{3}m$ structures from 430 to 2400 GPa, and found that the shuttlewise deforming phase already emerges as the lowest enthalpy phase at 430 GPa. The phase survives up to 1790 GPa and $oC12$ takes the place of it in 1790-2300 GPa and $R\overline{3}m$ above 2300 GPa.

We investigated the superconductivity of Cs-IV and $Fddd$ structures and found that for both structures, there exist two pressure regions showing the enhancement of $\lambda$ and $T_{\rm c}$ with increase of pressure. The first increase emerges below approximately 800 GPa, which is concerned with the phonon softening in the Cs-IV structure. The second one is in the pressure range from 1500-1900 GPa, where Cs-IV gets to be mechanically unstable and transforms to $Fddd$ structures, and the superconducting $T_{\rm c}$ reaches the maximum value of 351 K in the region. Therefore, the enhancement of the superconductivity is predicted to be strongly related to the softening of the lattices of Cs-IV and $Fddd$ structures. We conclude that in atomic metallic hydrogen, high $T_{\rm c}$ of the superconducting transition is related to strong electron-phonon coupling of the soft phonon modes, which give a big contribution. The highest $T_{\rm c}$ of phonon-mediated superconductivity, which is expected to be realized in dense hydrogen, is around room temperature on Earth.

## ACKNOWLEDGMENTS

This research is supported by the Japan Society for the Promotion of Science (JSPS) through its "Funding Program for Next Generation World-Leading Researchers (NEXT Program)" Grant No. GR068, and "KAKENHI" Grants No. 25800218, No. 25400371, and No. 22340106.

104102-5

[1] H. K. Mao and R. J. Hemley, Rev. Mod. Phys. 66, 671 (1994).

[2] P. Loubeyre, R. LeToullec, D. Hausermann, M. Hanfland, R. J. Hemley, H. K. Mao, and L. W. Finger, Nature (London) 383, 702 (1996).

[3] L. Cui, N. H. Chen, and I. F. Silvera, Phys. Rev. B 51, 14987 (1995).

[4] R. J. Hemley and H. K. Mao, Phys. Rev. Lett. 61, 857 (1988).

[5] A. F. Goncharov, R. J. Hemley, H. K. Mao, and J. Shu, Phys. Rev. Lett. 80, 101 (1998).

[6] R. T. Howie, C. L. Guillaume, T. Scheler, A. F. Goncharov, and E. Gregoryanz, Phys. Rev. Lett. 108, 125501 (2012).

[7] K. Nagao and H. Nagara, Phys. Rev. Lett. 80, 548 (1998).

[8] H. Kitamura, S. Tsuneyuki, T. Ogitsu, and T. Miyake, Nature (London) 404, 259 (2000).

[9] J. Kohanoff, S. Scandolo, G. L. Chiarotti, and E. Tosatti, Phys. Rev. Lett. 78, 2783 (1997).

[10] K. Nagao, T. Takezawa, and H. Nagara, Phys. Rev. B 59, 13741 (1999).

[11] M. Städele and R. M. Martin, Phys. Rev. Lett. 84, 6070 (2000).

[12] K. A. Johnson and N. W. Ashcroft, Nature (London) 403, 632 (2000).

[13] E. Kaxiras and Z. Guo, Phys. Rev. B 49, 11822 (1994).

[14] T. Cui, E. Cheng, B. J. Alder, and K. B. Whaley, Phys. Rev. B 55, 12253 (1997).

[15] C. J. Pickard and R. J. Needs, Nat. Phys. 3, 473 (2007).

[16] H. Liu, H. Wang, and Y. Ma, J. Phys. Chem. C 116, 9221 (2012).

[17] J. M. McMahon and D. M. Ceperley, Phys. Rev. Lett. 106, 165302 (2011).

[18] M. I. Eremets and I. A. Trojan, Lett. JETP 89, 174 (2009).

[19] E. Gregoryanz, O. Degtyareva, M. Somayazulu, R. J. Hemley, and H. K. Mao, Phys. Rev. Lett. 94, 185502 (2005).

[20] D. M. Deaven and K. M. Ho, Phys. Rev. Lett. 75, 288 (1995).

[21] T. S. Bush, C. R. A. Catlow, and P. D. Battle, J. Mater. Chem. 5, 1269 (1995).

[22] S. M. Woodley, P. D. Battle, J. D. Gale, and C. R. A. Catlow, Phys. Chem. Chem. Phys. 1, 2535 (1999).

[23] S. M. Woodley, Struct. Bonding 110, 95 (2004).

[24] A. R. Oganov and C. W. Glass, J. Chem. Phys. 124, 244704 (2006).

[25] C. W. Glass, A. R. Oganov, and N. Hansen, Comput. Phys. Comm. 175, 713 (2006).

[26] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Cereso, G. L. Chiarott, M. Cococcioni, I. Dabo et al., J. Phys.: Condens. Matter 21, 395502 (2009).

[27] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

[28] A. M. Rappe, K. M. Rabe, E. Kaxiras, and J. D. Joannopoulos, Phys. Rev. B 41, 1227 (1990).

[29] P. B. Allen and R. C. Dynes, Phys. Rev. B 12, 905 (1975).

[30] C. F. Richardson and N. W. Ashcroft, Phys. Rev. Lett. 78, 118 (1997).

[31] H. Y. Geng, H. X. Song, J. F. Li, and Q. Wu, J. Appl. Phys. 111, 063510 (2012).

[32] The same change of the total-energy curve was also obtained when we used other exchange-correlation functionals: the Perdew-Zunger local-density approximation (LDA), the Becke-Lee-Yang-Parr generalized gradient approximation (GGA), and the modified Perdew-Burke-Ernzerhof GGA (PBEsol). We also checked the curves by means of the norm-conserving pseudopotential calculation and the PAW calculation. All of the results show no essential differences.

[33] S. Biermann, D. Hohl, and D. Marx, Solid State Commun. 108, 337 (1998).

[34] G. Geneste, M. Torrent, F. Bottin, and P. Loubeyre, Phys. Rev. Lett. 109, 155303 (2012).

[35] As shown in Sec. III A, we obtained $Fddd$ as the most stable structure at 400 GPa by the application of GA. This discrepancy in the stable region of $Fddd$ is attributed to the small number of the $k$-point sampling, i.e., a $6 \times 6 \times 6$ grid, in the GA search. In the calculation condition of the GA search, $Cmca$-$4$ has higher $H$ by 1.2 mRy/proton than $Fddd$ at 400 GPa, and the transition pressure into $Fddd$ was shifted in the lower-pressure region.

[36] T. Takezawa, K. Nagao, and H. Nagara, J. Low Temp. Phys. 123, 315 (2001).

[37] J. M. McMahon and D. M. Ceperley, Phys. Rev. B 84, 144515 (2011).

[38] J. M. McMahon and D. M. Ceperley, Phys. Rev. B 85, 219902(E) (2012).