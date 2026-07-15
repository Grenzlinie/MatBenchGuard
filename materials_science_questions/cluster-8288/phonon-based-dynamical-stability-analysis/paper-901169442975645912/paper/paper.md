# Imaginary phonon modes and phonon-mediated superconductivity in $Y_2C_3$

Niraj K. Nepal$^1$, Paul C. Canfield$^{1,2}$, and Lin-Lin Wang$^{1*}$

[1] Ames National Laboratory, Ames, Iowa 50011, USA and
[2] Department of Physics and Astronomy, Iowa State University, Ames, Iowa 50011, USA
(Dated: August 23, 2023)

## Abstract

For $Y_2C_3$ with a superconducting critical temperature ($T_c$) $\sim$18 K, zone-center imaginary optical phonon modes have been found for the high-symmetry $I$-$43d$ structure due to C dimer wobbling motion and electronic instability from a flat band near Fermi energy. After lattice distortion to the more stable lowest symmetry $P1$ structure, these stabilized low-energy phonon modes with mixed C and Y characters carry a strong electron-phonon coupling to give arise to the observed sizable $T_c$. Our work shows that compounds with the calculated dynamical instability should not be simply excluded in high-throughput search for new phonon-mediated superconductors.

Computational search for new phonon-mediated super-conducting (SC) compounds has become an active field since the discovery of SC critical temperature ($T_c$) near room temperature for metal hydrides under high pressure ($\sim$200 GPa) [1–6]. The search requires the computation of electron-phonon coupling (EPC) matrices within the density functional perturbation theory (DFPT) [7, 8] to estimate $T_c$ using Migdal-Eliashberg approximations [9–13]. However, compounds with calculated imaginary phonon modes are regarded as dynamically unstable and often discarded as promising candidates in high-throughput[6]. On the other hand, some well-known SC are metastable, such as $YPd_2B_2C$ [14, 15]. In this letter, using yttrium sesquicarbide ($Y_2C_3$) as an example among rare-earth carbides $R_2C_3$ (R = rare-earth, Y or La) with their SC being discovered and improved over the years [16–21], we find that the high-symmetry body-centered cubic (BCC) structure in space group $I$-$43d$ (220) is dynamically unstable with zone-center imaginary optical phonon modes, which once stabilized carry a large EPC strength ($\lambda$) to give the sizable $T_c$. We emphasize that such behaviors are also found in several other known SC compounds with computed dynamically instability; thus, overlooking them during high-throughput search can leaves out some promising candidates.

$Y_2C_3$ in the $Pu_2C_3$-type structure of space group $I$-$43d$ (220) with C-C dimers was first synthesized in 1969 using high-pressure, high-temperature techniques[16] to show $T_c$ ranging from a low of 6 K to a high of 11.5 K [16]. Subsequent experiments with Thorium (Th) alloying increased the $T_c$ to 17 K in $(Y_{0.7}Th_{0.3})_2C_3$ [22]. Recently in 2004, for the samples prepared under 4.0-5.5 GPa followed by different heat treatment and sintering conditions, a $T_c$ up to 18 K in the binary $Y_2C_3$ has been observed[17]. Electronic structure calculations [23–25] have found that the states near the Fermi level ($E_F$) are hybridized between Y $4d$ and C-C antibonding $2p$ orbitals with an interesting flat band close to the $E_F$, as well as highly degenerated Kramers-Weyl points at $\sim$1 eV below the $E_F$ [26]. It has been proposed that the sensitivity of SC properties for the related $La_2C_3$ [27] with respect to synthesis condition is due to the change of density of states (DOS) at the $E_F$ from C deficiency[24, 25]. An earlier EPC calculation[25, 28] on $Y_2C_3$ has focused only on two zone-center modes; a Y-dominated mode at 175 cm$^{-1}$ (5.2 THz) and the C-C bond stretching mode at 1442 cm$^{-1}$ (43.3 THz), and found a much larger EPC contribution from the Y-dominated than C-C bond stretching mode. However, here with DFPT calculation over all the phonon modes, we find that the high-symmetry $I$-$43d$ structure is dynamically unstable with zone-center imaginary phonon modes of C dimer wobbling motion due to electronic instability from the flat band along the $\Gamma$-N direction at $E_F$. By following the lattice distortion of the imaginary modes with full relaxation, more stable low-symmetry structures of $Y_2C_3$ have been found, where the imaginary modes become stabilized in a low-energy range, lower than the Y-dominated modes. These stabilized low-energy phonon modes carry large $\lambda$, which contributes significantly to $T_c$. The imaginary phonon modes can also be stabilized with a large electronic smearing and under pressure, with the latter enhancing the $T_c$ in a trend agreeing with experiments.

We used quantum espresso (QE) package [29, 30] with ultrasoft pseudopotentials [31, 32] for ground-state and EPC calculations. The exchange-correlation energy is approximated by Perdew-Burke-Ehrnzerhof (PBE) functional [33]. Kinetic energy cutoff of 50 Ry, Brillouin zone (BZ) sampling of $(6{\times}6{\times}6)$ k-point mesh, and a Gaussian smearing of 0.05 eV are utilized for ground-state calculations. Phonon calculations are performed with momentum transfer grid ($\mathbf{q}$) of $(2{\times}2{\times}2)$. Further $\mathbf{k}$-mesh and $\mathbf{q}$-mesh are interpolated to $(12{\times}12{\times}12)$ fine-mesh to compute EPC properties. The Coulomb potential $\mu_c^*$ is kept fixed at 0.16. The Fermi surfaces are plotted using the Fermi surfer package [34].

Figure 1(a) shows the $I$-$43d$ structure of $Y_2C_3$ in the primitive unit cell (20 atoms), where eight Y atoms occupy $16c$ sites and twelve C atoms at $24d$ sites form six dimers. Our PBE-relaxed lattice constant of $8.239\mathring{A}$ agrees well with the experimental $8.237\mathring{A}$ [35] and also $8.254\mathring{A}$ from previous DFT calculation[23]. The DFPT-

![](./images/901169442975645912_1.jpg)

FIG. 1. (a) Primitive unit cell of $Y_2C_3$ in the body-centered cubic $Pu_2C_3$-type structure of space group $I$-$43d$ (220). (b) The structure viewed along the [111] direction with atomic displacements represented by black arrows according to the imaginary eigenmode 4. (c) Formation energy ($\Delta E_f$) with respect to volume (V) for $I$-$43d$ (220), rhombohedral structure in space group $R3c$ (161), and the low-symmetry structure relaxed from eigenmode 4 in space group $P1$ (1), compared to the experimental data around the equilibrium. (d) Atom-projected phonon dispersion of $I$-$43d$ structure exhibiting imaginary modes shown as negative frequencies ($\omega$). First Brillouin zone (BZ) and high-symmetry paths are in inset. (e) Atom-projected phonon dispersion $<$10 THz zoomed from (d). Red represents for Y, blue for C, and purple for contributions from both as defined in Eq. 1.

calculated $I$-$43d$ phonon dispersion is plotted in Fig. 1(d) with the inset showing the high-symmetry points. To analyze the contribution of different atomic species to phonon eigenmodes, we have summed the atomic displacements of each eigenmode for different species ($|{\bf e}_{\nu{\bf k}}^i|^2$) as in Eq. 1 and color-coded the dispersion,

$$
|{\bf e}_{\nu{\bf k}}^i|^2 = \sum_{j=1}^{N_i} |{\bf e}_{\nu{\bf k}}^{ij}|^2,
\tag{1}
$$

where ${\bf e}_{\nu{\bf k}}^{ij}$ are the displacements obtained for atom type $i$ from the eigenvector of mode $\nu$ for $k$-point ${\bf k}$ by diagonalizing dynamical matrix, and index $j$ runs to $N_i$ as the number of atoms for type $i$. For $Y_2C_3$ in Fig. 1(d), the modes with the highest frequency $\sim$40 THz are well separated from the rest and solely contributed from the C dimer stretching mode. Our atomic projection also reveals that the modes from 10 to 15 THz are dominated by other C-related motion (blue). In contrast, the Y contributions (red) are mostly around 5 THz due to the much larger mass of Y than C. As zoomed in panel (e) for the frequency $<$10 THz, there are modes with mixed contributions from both Y and C (purple). Interestingly, we find three zone-center modes at $\Gamma$ are imaginary shown by the negative frequency and are also dominated by C contributions. Figure 1(b) shows one of imaginary modes (eigenmode 4) with the arrows representing the direction and size of the atomic displacements for the eigenvector. Usually the C-related modes are assumed to have high frequency due to the tendency of C to form stronger covalent bonds and smaller mass than Y. But as shown in Fig.S1(a)-(c) with the conventional unit cell, each Y is surrounded by 12 C dimers in a twisted prism, while each C dimer is surrounded by eight Y atoms in a cage of two trapezoids. The wobbling motion of the C dimers within these cages have zero to even negative energy cost, giving arise to the three imaginary optical modes.

The zone-center imaginary phonon modes indicate that the $I$-$43d$ structure of $Y_2C_3$ is dynamically unstable. To search for more stable structures, we have used the imaginary modes to distort the primitive unit cell to perform full relaxation with atomic positions and cell dimensions, and we find new low-symmetry structures with total energies of 2.34 (mode 4 and 10) and 0.9 meV/atom (mode 1) below that of the $I$-$43d$ structure. For the most stable structure of mode 4, the lattice symmetry is also the lowest in space group $P1$ (1). We have also considered the cubic to rhombohedral distortion along the [111] direction to retain some symmetry as in space group $R3c$ (161). In Fig. 1(c), the formation energy ($\Delta E_f$) is plotted with respect to volume (V) close to the equilibrium for the three structures with gradually lowered symmetry. The $\Delta E_f$ of $-281$meV/atom agrees well with the experimental $-261$meV/atom [36]. The relaxed C-C (Y-C) bond length in the $I$-$43d$ structure around 1.34 (2.51)$\mathring{\text{A}}$ is consistent with previous DFT calculation [23], and also comparable to the experimental 1.298 (2.51)$\mathring{\text{A}}$ [35]. Compared to the high-symmetry $I$-$43d$ structure, the $R3c$ and $P1$ structures are more stable at the equilibrium and larger volumes with $P1$ being the most stable in the lowest symmetry. But at volumes smaller than the equilibrium or under increasing pressure, the three equation of states converge to the same curve. In other words, $I$-$43d$ structure becomes the ground state under pressure.

To find out the origin of such instability in BCC $Y_2C_3$, we have calculated the electronic structures. As plotted in Fig. 2(a), the partial DOS (PDOS) projected on atomic orbitals shows that the bonding states of C dimer with $2s$ and $2p$ orbitals dominate from $-8$ to $-3$ eV, while the Y $4d$ orbitals dominate the empty states above $+2$ eV. In the middle, the hybridization between the C dimer antibonding states and Y $4d$ form a pseudo-gap from $-0.5$ to $+0.5$ eV. However, inside this broad pseudo-gap, there is a sharp local DOS maximum at $E_F$, which hints at an electronic instability. From the calculated electronic band structures in Fig. 2(b) in the range of $\pm 1$ eV, there are four bands crossing $E_F$ with the corresponding 3D Fermi surface (FS) plotted in panel (c). As numbered from low to high energy in Fig. 2(b-c), the first two va-

2

![](./images/901169442975645912_2.jpg)

FIG. 2. (a) Projected density of states (PDOS) of $Y_2C_3$ in the $I$-$43d$ structure on Y $5s$, Y $4d$, C $2s$ and C $2p$ orbitals, showing a DOS peak near the Fermi-level ($E_F$). (b) Electronic band structure in the range of $E_F{\pm}1$ eV showing four bands crossing the $E_F$ (3 valence and 1 conduction bands indicated by black arrow, indexed from "1" to "4" at the top). The flat band section is along the $\Gamma$-N direction ($4^{th}$ band indicated by red arrow). (c) Fermi surface (FS) corresponding to the four different bands, labelled by their band index defined in (b). (d) Fermi velocity ($\mathbf{v}_F$) plotted on the FS. 2D FS contour on the (111) and (001) planes are also shown.

lence bands form small spherical hole pockets around $\Gamma$. The third and highest valence band has disc-like features along the $\Gamma$-H direction besides a cubic hole pocket. The 4th and lowest conduction band forms spike-like features along the $\Gamma$-N direction besides a spherical double-layered shell around $\Gamma$. The spike-like features come from the flat band along the $\Gamma$-N direction in (b) and corresponds to the sharp local DOS maximum at $-10$ meV (red arrow). The Fermi velocity ($\mathbf{v}_F$), $\nabla_k E_k$, has also been calculated and overlaid on FS in panel (d). The maximum value appears on the outer surface of the disc-like feature of FS3. 2D cuts of FS along (111) and (001) planes show that the distribution of $\mathbf{v}_F$ with high values across FS1 and FS2, relatively lower value for FS3 except for the disc-like feature, and the lowest for FS4 (blue and green patches), consistent with previous result[23]. Although the presence of the flat band in $Y_2C_3$ has been noted before, its implication on the structural instability has only been revealed in our current work by finding the zone-center imaginary phonon modes and the more stable structures via distortion according to the imaginary phonon modes.

![](./images/901169442975645912_3.jpg)

FIG. 3. (a) Atom-projected phonon dispersion for low-symmetry $P1$ structure of $Y_2C_3$ relaxed from eigenmode 4. Atom-projections are highlighted by red for Y, blue for C, and purple for both contributions. The mode-resolved electron-phonon coupling (EPC) strength ($\lambda$) is represented by green shade. (b) Atom-projected phonon dispersion without the shade of EPC zoomed $<4$ THz to show the contributions from both Y and C atoms to the $\lambda$. (c) Fermi velocity ($\mathbf{v}_F$) plotted over the Fermi surfaces (FS), which are indexed with the same numbers as in Figure. 2 but become distorted because of the relaxation. The 2D FS contour on (111) plane is also shown. (d) Electronic band structure of $P1$ structure showing the absence of flat band, thereby flattening the density of states peak (red arrows) at the Fermi-level ($E_F$). (e) Isotropic Eliashberg spectral function ($\alpha^2F(\omega)$) of $P1$ structure gives the overall integrated $\lambda$=0.92.

After establishing the electronic origin of the instability in BCC $Y_2C_3$ and finding the more stable low-symmetry $P1$ structure, next we calculate EPC in DFPT to explain SC properties. In Figure. 3, we plot the phonon dispersion of the $P1$ structure relaxed from eigenmode 4 ($\sim$2.34 meV/atom more stable than $I$-$43d$) in (a) with and (b) without the mode-resolved EPC projections. Atomic characters are also similarly projected as in Fig. 1(d-e). Due to the lowest symmetry, many degeneracy at the high-symmetry points have been lifted in $P1$ (Fig. 3(a)) when compared to the $I$-$43d$ phonon dispersion (Fig. 1(e)). Importantly, the $P1$ structure does not have imaginary modes and is dynamically stable. The original imaginary modes in $I$-$43d$ are now stabilized in the low frequency range of 2-3 THz at $\Gamma$. Moreover, the

3

largest EPC contribution is found around $\Gamma$ (green shade) along the $\Gamma$-H, $\Gamma$-N, and $\Gamma$-P directions within the same low frequency range, where both C dimers and Y atoms provide significant contributions (see purple in Fig. 3(b) without EPC). As confirmed in the Eliashberg spectral function of Fig 3(e), the largest EPC contribution peak comes from the 2-3 THz range, followed by another peak around the 6 THz, both have the mixed C and Y characters, giving an overall EPC strength $\lambda$ of 0.92, logarithmic average of phonon frequencies ($\omega_{log}$) of 219.6 K, and $T_c$ of 9.3 K as listed in Table I. The calculated $T_c$ is in a good agreement to the experimental data. For the change in electronic structures, the FS of the $P1$ structure now consists of only three bands, completely removing the spike-like features due to the flat band along the $\Gamma$-N direction [Fig. 3(b)]. As the result, the electronic instability associated with the flat band is eliminated, and the local DOS maximum at $E_F$ is flattened out, as seen in Fig. 3(c) (red arrows). The results from the other $I$-$43d$ imaginary phonon modes, namely mode 1 ($\sim$ 0.9 meV/atom lower) and 10 ($\sim$ 2.34 meV/atom lower, similar to eigenmode 4) are presented in Fig.S2. The corresponding properties are listed in Table I showing a similar $T_c$ to the $P1$ structure of eigenmode 4. Thus, one of the key findings of our work is that the EPC for the phonon-mediated SC in $Y_2C_3$ with a sizable $T_c$ arise from the stabilized imaginary phonon modes after removing the flat band and electronic instability, and the largest EPC contributions are from these low-energy optical phonon modes of mixed C and Y characters.

TABLE I. EPC strength $\lambda$, logarithmic average of phonon frequencies $\omega_{log}$, and critical temperature $T_c$ computed from isotropic Eliashberg approximation with distorted structures, pressure, and large electronic smearing for $Y_2C_3$ and other compounds using the Coulomb potential $\mu_c^*$ of 0.16. (These quantities are not available for the dynamically unstable structures with imaginary modes, for example $Y_2C_3 < 20$ GPa, $\sigma < 0.10$ Ry and distorted structure with mode 1.) Experimental $T_c$ for $Y_2C_3$ ranges from 6 K to 18 K depending on synthesis conditions and measurement techniques [16, 17].

<table>
  <thead>
    <tr>
      <th>Compound</th>
      <th>Stabilization</th>
      <th>$\lambda$</th>
      <th>$\omega_{log}$ (K)</th>
      <th>$T_c$ (K)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5">$Y_2C_3$ [I-43d]</td>
      <td>Mode 4</td>
      <td>0.92</td>
      <td>219.6</td>
      <td>9.3</td>
    </tr>
    <tr>
      <td>Mode 10</td>
      <td>0.93</td>
      <td>219.4</td>
      <td>9.5</td>
    </tr>
    <tr>
      <td>20 GPa</td>
      <td>3.14</td>
      <td>96.1</td>
      <td>16.0</td>
    </tr>
    <tr>
      <td>30 GPa</td>
      <td>1.38</td>
      <td>263.6</td>
      <td>22.3</td>
    </tr>
    <tr>
      <td>$\sigma = 0.10$ Ry</td>
      <td>1.14</td>
      <td>228.5</td>
      <td>14.5</td>
    </tr>
    <tr>
      <td>$La_2C_3$ [I-43d]</td>
      <td>$\sigma = 0.10$ Ry</td>
      <td>1.15</td>
      <td>219.4</td>
      <td>14.3 (13.4 [37])</td>
    </tr>
    <tr>
      <td>$Sc_2C_3$ [I-43d]</td>
      <td>$\sigma = 0.10$ Ry</td>
      <td>1.99</td>
      <td>205.6</td>
      <td>25.5</td>
    </tr>
    <tr>
      <td>$W_2B$ [I4/mcm]</td>
      <td>Distortion</td>
      <td>0.81</td>
      <td>215.7</td>
      <td>6.6 (3.10 [38])</td>
    </tr>
    <tr>
      <td>$La_3InC$ [Pm-3m]</td>
      <td>Distortion</td>
      <td>1.04</td>
      <td>108.6</td>
      <td>5.8 (2.6 [39])</td>
    </tr>
    <tr>
      <td>$MoB_2$ [P6/mmm]</td>
      <td>$\sigma = 0.10$ Ry</td>
      <td>1.96</td>
      <td>208.9</td>
      <td>25.6 (32 [40])</td>
    </tr>
  </tbody>
</table>

Besides distorting the $I$-$43d$ structure for more stable low-symmetry structures, increasing pressure and electronic smearing are other ways to stabilize the imaginary phonon modes. As plotted in Fig. 4(d), a large electronic smearing of 0.1 Ry on the $I$-$43d$ structure reasonably mimics the results of the low-symmetry $P1$ structure,as seen in phonon dispersion of Fig. 4(e) and spectral function ($\alpha^2$F($\omega$)) of Fig. 4(f). But pressure stabilizes these imaginary phonon modes with additionally interesting behaviors. As shown in Fig. 4(a) and Fig. S3(c), pressure of 20 GPa stabilizes the imaginary phonon modes, one at $\sim$4 THz and the other at as low as $\sim$2 THz, with unusually large $\lambda$ coming from those modes with large contribution from C dimers. The increasing pressure also shifts the flat band and the associated local DOS maximum peak first to cross $E_F$ and then to higher energy away from $E_F$, resulting in a smooth part of DOS at $E_F$, thereby stabilizing the imaginary phonon modes (Fig. S3(a)). As listed in Table. I, the large $\lambda \sim 3.14$ at 20 GPa and low $\omega_{log} \sim 96.1$ K are the results of the extremely soft or low-energy modes with a large EPC con-

![](./images/901169442975645912_4.jpg)

FIG. 4. (a) Atom-projected phonon dispersion of $Y_2C_3$ in the $I$-$43d$ structure under 20 GPa. Atom-projections are highlighted by red for Y, blue for C, and purple for both contributions. The mode-resolved electron-phonon coupling (EPC) strength ($\lambda$) is represented by green shade. (b) Atom-projected phonon dispersion without the shade of EPC zoomed around the modes with the largest EPC to show the contributions from both Y and C atoms to the $\lambda$. (c) Isotropic Eliashberg spectral function ($\alpha^2 F(\omega)$) of the $I$-$43d$ structure under 20 GPa giving the overall $\lambda$=3.14. (d)-(f) Similar plots to (a)-(c) with a large electronic smearing of 0.1 Ry at zero pressure. The overall integrated $\lambda$=1.14. The spectral function ($\alpha^2 F(\omega)$) is computed in isotropic Eliashberg approximation and then integrated (dashed lines) for the overall $\lambda$.

tribution, also seen in Fig. 4(c). For a further increase of pressure to 30 GPa, the lowest soft mode is pushed up- ward to bring the two stabilized phonon modes close to each other at $\Gamma$, similar to the cases of the $P 1$ structure and the large electronic smearing, but achieving both a larger $\lambda$ of 1.38 and a larger $\omega_{log}$ of 263.6 K (Fig. S3(c)), thereby enhancing the $T_{c}$ from 9.3 and 14.5 K to 22.3 K. This trend of higher $T_{c}$ for smaller lattice constants under pressure is consistent with the experimental obser- vation [16,17], where an increase of $T_{c}$ from sub-10 K to 18 K has been observed when the lattice constant is decreased from 8.24 to $8.20 \AA$ mostly due to different heat treatment and sintering conditions.

Lastly, as listed in Table. I and shown in supplemen- tary Fig.S4-S7 for the related $La_{2} C_{3}$ as well as different structures and compounds of $W_{2} B, La_{3} InC$ and $MoB_{2}$ , although they all have dynamical instability, the calcu- lated $T_{c}$ after the imaginary phonon modes being stabi lized agree well with experimental $T_{c}$ . We also predict a higher $T_{c}$ in $Sc_{2} C_{3}$ than $Y_{2} C_{3}$ and $La_{2} C_{3}$ . Such a general behavior emphasizes that compounds with calculated dy- namical instability should not be discarded in the high throughput search for EPC-mediated SC.

In conclusion, we find that the high-symmetry $I-43 d$  structure of $Y_{2} C_{3}$ is dynamically unstable with zone center imaginary optical phonon modes from $C$ dimer wobbling motion due to the electronic instability from a flat band at the Fermi level $(E_{F})$ . Once the imagi nary modes are stabilized in a more stable low-symmetry structure, under pressure or with a large electronic smearing, these low-energy modes of mixed $C$ and $Y$  characters give arise to strong electron-phonon coupling(EPC) strength determining the superconducting prop- erties. Our work demonstrates the necessity of further exploration in the compounds with imaginary phonon modes. EPC calculations may not always be feasible for the distorted structures due to low symmetry for large unit cells, however, pressure and electronic smearing are the alternatives to stabilize them and study the super- conductivity. This can open a myriad of opportunities to discover high-temperature superconductors via high- throughput screening.

We acknowledges Dr. Lorenzo Paulatto for the helpful discussion of atom-projected phonon dispersion. This work was supported by Ames National Laboratory LDRD and U.S. Department of Energy, Office of Basic Energy Science, Division of Materials Sciences and Engi- neering. Ames National Laboratory is operated for the U.S. Department of Energy by Iowa State University un- der Contract No. DE-AC02-07CH11358.

* llw@ameslab.gov

[1] Y. Li, J. Hao, H. Liu, Y. Li, and Y. Ma, The metalliza- tion and superconductivity of dense hydrogen sulfide, J. Chem. Phys. 140, 174712 (2014).

[2] G. Webb, F. Marsiglio, and J. Hirsch, Superconductivityin the elements, alloys and simple compounds, Phys. C: Supercond. Appl. 514, 17 (2015).

[3] A. Drozdov, M. Eremets, I. Troyan, V. Ksenofontov, and S. I. Shylin, Conventional superconductivity at 203 kelvin at high pressures in the sulfur hydride system, Nature525, 73 (2015).

[4] W. E. Pickett, Colloquium: Room temperature super- conductivity: The roles of theory and materials design, Rev. Mod. Phys. 95, 021001 (2023).

[5] B. Lilia, R. Hennig, P. Hirschfeld, G. Profeta, A. Sanna, E. Zurek, W. E. Pickett, M. Amsler, R. Dias, M. I. Eremets, et al., The 2021 room-temperature supercon-ductivity roadmap, J. Phys. Condens. Matter 34, 183002(2022).

[6] K. Choudhary and K. Garrity, Designing high-tc su- perconductors with bcs-inspired screening, density func- tional theory, and deep-learning, Npj Comput. Mater. 8,244 (2022).

[7] S. Baroni, S. De Gironcoli, A. Dal Corso, and P. Gi- annozzi, Phonons and related crystal properties from density-functional perturbation theory, Reviews of mod- ern Physics 73, 515 (2001).

[8] A. Dal Corso, Density-functional perturbation theory with ultrasoft pseudopotentials, Physical Review B 64,235118 (2001).

[9] A. Migdal, Interaction between electrons and lattice vi-brations in a normal metal, Sov. Phys. JETP 7, 996(1958).

[10] G. Eliashberg, Interactions between electrons and latticevibrations in a superconductor, Sov. Phys. JETP 11, 696(1960).

[11] P. B. Allen, Neutron spectroscopy of superconductors, Physical Review B 6, 2577 (1972).

[12] P. B. Allen and R. Dynes, Transition temperature of strong-coupled superconductors reanalyzed, Physical Re- view B 12, 905 (1975).

[13] E. R. Margine and F. Giustino, Anisotropic migdal- eliashberg theory using wannier functions, Physical Re- view B 87, 024505 (2013).

[14] R. Cava, H. Takagi, H. Eisaki, H. Zandbergen, T. Siegrist, B. Batlogg, J. Krajewski, W. Peck Jr, S. Carter, K. Mizuhaski, et al., Good news from an abandoned gold mine: A new family of quaternary in- termetallic superconductors, Physica C: Supercond. 235,154 (1994).

[15] Y. Sun, I. Rusakova, R. Meng, Y. Cao, P. Gautier-Picard, and C. Chu, The $23 k$ superconducting phase ypd2b2c, Physica C: Supercond. 230, 435 (1994).

[16] M. Krupka, A. Giorgi, N. Krikorian, and E. Szklarz, High pressure synthesis and superconducting properties of yt- trium sesquicarbide, J. Less-Common Met. 17, 91 (1969).

[17] G. Amano, S. Akutagawa, T. Muranaka, Y. Zenitani, and J. Akimitsu, Superconductivity at $18 k$ in yttrium sesquicarbide system, y2c3, Journal of the Physical Soci- ety of Japan 73, 530 (2004).

[18] K. Sugawara, T. Sato, S. Souma, T. Takahashi, and A. Ochiai, Anomalous superconducting-gap symmetry of noncentrosymmetric la 2 c 3 observed by ultrahigh- resolution photoemission spectroscopy, Physical Review B 76, 132512 (2007).

[19] S. Kuroiwa, Y. Saura, J. Akimitsu, M. Hiraishi,

M. Miyazaki, K. Satoh, S. Takeshita, and R. Kadono, Multigap superconductivity in sesquicarbides la 2 c 3 and y 2 c 3, Physical review letters 100, 097002 (2008).

[20] J. Chen, M. Salamon, S. Akutagawa, J. Akimitsu, J. Sin- gleton, J. Zhang, L. Jiao, and H. Yuan, Evidence of nodal gap structure in the noncentrosymmetric superconductor y2c3, Physical Review B 83, 144529 (2011).

[21] S. Akutagawa, T. Ohashi, H. Kitano, A. Maeda, J. Goryo, H. Matsukawa, and J. Akimitsu, Quasiparti- cle electronic structure of a new superconductor, y2c3, in the mixed state investigated by specific heat and flux- flow resistivity, Journal of the Physical Society of Japan 77, 064701 (2008).

[22] M. Krupka, A. Giorgi, N. Krikorian, and E. Szklarz, High-pressure synthesis of yttrium-thorium sesquicar- bide: a new high-temperature superconductor, J. Less- Common Met. 19, 113 (1969).

[23] Y. Nishikayama, T. Shishidou, and T. Oguchi, Electronic properties of y2c3 by first-principles calculations, Journal of the Physical Society of Japan 76, 064714 (2007).

[24] I. Shein and A. Ivanovskii, Electronic properties of the novel 18-k superconducting y2c3 as compared with 4-k yc2 from first principles calculations, Solid state commu- nications 131, 223 (2004).

[25] D. Singh and I. Mazin, Electronic structure and electron- phonon coupling in the 18 k superconductor $y_{2}c_{3}$, Phys- ical Review B 70, 052504 (2004).

[26] L. Jin, Y. Liu, X. Zhang, X. Dai, and G. Liu, Sixfold, fourfold, and threefold excitations in the rare-earth metal carbide $R_{2}c_{3}$, Phys. Rev. B 104, 045111 (2021).

[27] J. Kim, W. Xie, R. Kremer, V. Babizhetskyy, O. Jepsen, A. Simon, K. Ahn, B. Raquet, H. Rakoto, J.-M. Broto, et al., Strong electron-phonon coupling in the rare-earth carbide superconductor la 2 c 3, Physical Review B 76, 014516 (2007).

[28] W. E. Pickett, The next breakthrough in phonon- mediated superconductivity, Physica C Supercond 468, 126 (2008).

[29] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococ- cioni, I. Dabo, et al., Quantum espresso: a modular and open-source software project for quantum simula- tions of materials, Journal of physics: Condensed matter 21, 395502 (2009).

[30] P. Giannozzi, O. Andreussi, T. Brumme, O. Bunau, M. B. Nardelli, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, M. Cococcioni, et al., Advanced capabilities for materials modelling with quantum espresso, Journal of physics: Condensed matter 29, 465901 (2017).

[31] G. Prandini, A. Marrazzo, I. E. Castelli, N. Mounet, and N. Marzari, Precision and efficiency in solid-state pseu- dopotential calculations, npj Computational Materials 4, 1 (2018).

[32] K. F. Garrity, J. W. Bennett, K. M. Rabe, and D. Van- derbilt, Pseudopotentials for high-throughput dft calcu- lations, Computational Materials Science 81, 446 (2014).

[33] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77, 3865 (1996).

[34] M. Kawamura, Fermisurfer: Fermi-surface viewer provid- ing multiple representation schemes, Computer Physics Communications 239, 197 (2019).

[35] T. Mochiku, T. Nakane, H. Kito, H. Takeya, S. Harjo, T. Ishigaki, T. Kamiyama, T. Wada, and K. Hirata, Crystal structure of yttrium sesquicarbide, Physica C: Superconductivity 426, 421 (2005).

[36] V. Novokshonov, Synthesis of sesquicarbides of heavy rare earths and yttrium at high pressures and temper- atures, Zhurnal Neorganicheskoj Khimii 25, 684 (1980).

[37] J. Kim, W. Xie, R. Kremer, V. Babizhetskyy, O. Jepsen, A. Simon, K. Ahn, B. Raquet, H. Rakoto, J.-M. Broto, et al., Strong electron-phonon coupling in the rare-earth carbide superconductor la 2 c 3, Phys. Rev. B 76, 014516 (2007).

[38] G. F. Hardy and J. K. Hulm, The superconductivity of some transition metal compounds, Phys. Rev. 93, 1004 (1954).

[39] J.-T. Zhao, Z.-C. Dong, J. Vaughey, J. E. Ostenson, and J. D. Corbett, Synthesis, structures and properties of cu- bic r3in and r3inz phases (r= y, la; z= b, c, n, o): The effect of interstitial z on the superconductivity of la3in, J. Alloys Compd. 230, 1 (1995).

[40] C. Pei, J. Zhang, Q. Wang, Y. Zhao, L. Gao, C. Gong, S. Tian, R. Luo, M. Li, W. Yang, Z.-Y. Lu, H. Lei, K. Liu, and Y. Qi, Pressure-induced Superconductivity at 32 K in MoB2, National Sci- ence Review 10.1093/nsr/nwad034 (2023), nwad034, https://academic.oup.com/nsr/advance-article- pdf/doi/10.1093/nsr/nwad034/49182415/nwad034.pdf.