Computer simulations of the dynamical properties of the metallic superlattices, Au/Ni

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1984 J. Phys. F: Met. Phys. 14 L167

(http://iopscience.iop.org/0305-4608/14/9/001)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 160.36.178.25
This content was downloaded on 18/08/2015 at 19:33

Please note that terms and conditions apply.

# LETTER TO THE EDITOR

## Computer simulations of the dynamical properties of the metallic superlattices, Au/Ni

Y Sasajima, M Imafuku, R Yamamoto and M Doyama

Department of Metallurgy and Materials Science, Faculty of Engineering, The University of Tokyo, Bunkyo-ku, Tokyo, Japan

Received 19 June 1984

**Abstract.** The atomic arrangements of the metallic superlattices, Au/Ni, were simulated by molecular dynamics using the empirical two-body interatomic potentials. Young's modulus along the stacking direction, $Y[111]$, was calculated from the model structure simulated in the computer. $Y[111]$ shows anomalous enhancement in the regime of short modulation wavelength, 4.5-40 $\mathring{A}$, which is in qualitative agreement with experimental results. The vibrational local densities of states (LDOS) of atoms at and near the interface between gold and nickel layers were computed for the first time by the recursion method. The low-frequency part of the LDOS was enhanced due to the lattice mismatch.

Metallic superlattices exhibit some unique and unexpected properties such as magnetic, superconducting and elastic properties (Schuller and Falco 1982). Strongly enhanced biaxial elastic moduli have been found in Au/Ni and Cu/Pd by Yang *et al* (1977), in Cu/Ni by Testardi *et al* (1981) and Tsakalakos and Hilliard (1983) and in Ag/Pd by Henein and Hilliard (1983). These metallic superlattices have biaxial elastic moduli $Y[111]$ enhanced by a factor of 2-4 at short modulation wavelength $(<30\ \mathring{A})$. Hilliard (1979) pointed out that this supermodulus effect is closely related to the coherent structure of the superlattices. Pickett (1982) ascribed it to the additional Brillouin zone which appears in Cu/Ni and Ag/Pd. Schuller and Rahman (1983) have attempted to simulate this supermodulus effect in a simplified model using molecular dynamics. In this Letter we have simulated the atomic arrangements of Au/Ni metallic superlattices with various modulation wavelengths using molecular dynamics and we have calculated the vibrational local density of states (LDOS) of atoms in this system.

The FCC/FCC metallic superlattices including the Au/Ni system have a strong [111] texture. We have simulated several structural models of the Au/Ni superlattice (1-layer/1-layer, 3/3, 5/5, 7/7 and 9/9) in a similar manner to the construction of a realistic model for grain boundaries in metals. We do not repeat the detailed description of the method here; details are given by Hashimoto *et al* (1984). The interatomic potential used in the present simulations is the Morse function,

$$\varphi(r)=D(\exp\left[-2\alpha(r-r_0)\right]-2\exp\left[-\alpha(r-r_0)\right]). \tag{1}$$

The constants of the pair potentials for Ni-Ni and Au-Au, $D$, $\alpha$ and $r_0$, were determined from the lattice constant $a_0$, the compressibility $K$ at 0 K and the formation energy of a vacancy $E_f^\text{v}$, which are summarised in table 1. Since the potential energy between different kinds of metallic atoms is not fully understood theoretically or experimentally, we

Letter to the Editor

Table 1. The lattice constant $a_0$, the compressibility $K$ (at 0 K) and the formation energies of a vacancy $E_{\mathrm{f}}^{\mathrm{v}}$ of pure Au and pure Ni.

<table>
  <thead>
    <tr>
      <th></th>
      <th>$a_0$ (Å)</th>
      <th>$K$ ($10^{-12}\ \mathrm{cm^2\ dyn^{-1}}$)</th>
      <th>$E_{\mathrm{f}}^{\mathrm{v}}$ (eV)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ni</td>
      <td>3.524</td>
      <td>0.535</td>
      <td>1.65</td>
    </tr>
    <tr>
      <td>Au</td>
      <td>4.079</td>
      <td>0.607</td>
      <td>0.97</td>
    </tr>
  </tbody>
</table>

computed the potential constants using the combination rules (Das *et al* 1977)

$$
D_{\mathrm{Au-Ni}}=(D_{\mathrm{Au}} D_{\mathrm{Ni}})^{1/2} \tag{2}
$$

$$
\alpha_{\mathrm{Au-Ni}}=\frac{1}{2}(\alpha_{\mathrm{Au}}+\alpha_{\mathrm{Ni}}) \tag{3}
$$

$$
r_{0\ \mathrm{Au-Ni}}=(\alpha_{\mathrm{Au}} \alpha_{\mathrm{Ni}})^{1/2}+\ln 2/\alpha_{\mathrm{Au-Ni}}. \tag{4}
$$

These parameters are summarised in table 2. The potential between Au and Ni atoms is an average of the Au-Au and Ni-Ni pair potentials. The combination rules are only an approximation to determine the pair potential between different kinds of atoms in a solid solution. Whether or not this approximation is valid is an open question. It is necessary to investigate the interaction energy between heterogeneous atoms by the electron theory of metals. These empirical rules were applied rather successfully to some problems (Fujiwara 1982) and so we simply used them in the present problem as the first step towards understanding the atomic arrangements in metallic superlattices. We have constructed a model of the metallic superlattice in the computer by stacking the (111) lattice planes of Au and Ni alternately in a cylindrical shape (radius $20\ \mathring{\mathrm{A}}$) consisting of about 2000 atoms. The lattice mismatch between gold and nickel is so large that the number of atoms existing in the two-dimensional superlattice formed is not tractable in limited computer time. Therefore we have treated only a finite region within (111) planes in this study. The relative positions of the gold and nickel (111) planes and the equilibrium layer spacings were determined iteratively. The model structure of Au/Ni was then relaxed by the method of molecular dynamics, with a periodic boundary condition along the [111] direction. In order to calculate Young's modulus, $Y[111]$, the system was strained in the [111] direction and the increment of potential energy, $W$, was then computed as a function of strain. The elastic energy, $W$, can be written as

$$
W=\frac{1}{2}Y[111]\varepsilon^2 \tag{5}
$$

where $\varepsilon$ and $Y[111]$ are the strain and Young's modulus along the [111] direction, respectively. $Y[111]$ was estimated from the slope of the plot of $W$ against $\varepsilon^2$. The recursion method developed by Haydock (1980) has been used to calculate the vibrational LDOS. By this method, one can directly obtain the frequency spectrum along an arbitrary

Table 2. The parameters $D$, $\alpha$ and $r_0$ for Au-Au, Ni-Ni and Au-Ni pair potentials.

<table>
  <thead>
    <tr>
      <th></th>
      <th>$\alpha$ (Å)</th>
      <th>$r_0$ (Å)</th>
      <th>$D$ (eV)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Au-Au</td>
      <td>3.113</td>
      <td>2.891</td>
      <td>0.155</td>
    </tr>
    <tr>
      <td>Au-Ni</td>
      <td>2.729</td>
      <td>2.700</td>
      <td>0.185</td>
    </tr>
    <tr>
      <td>Ni-Ni</td>
      <td>2.346</td>
      <td>2.538</td>
      <td>0.221</td>
    </tr>
  </tbody>
</table>

direction of vibration for individual atoms. The LDOS of a particular atom $0, g_{00}^{i}(\omega)$ is written as
$$
g_{00}^{i}(\omega)=2 \omega \sum_{n}|\langle 0, i \mid n\rangle|^{2} \delta\left(\omega_{n}^{2}-\omega^{2}\right)
\tag{6}
$$
where $|n\rangle$ is the $n$th eigenvector and $\omega_{n}^{2}$ is the $n$th eigenvalue of the dynamical matrix
$$
\mathbf{D}=\mathbf{M}^{-1 / 2} \boldsymbol{\Phi} \mathbf{M}^{-1 / 2}
\tag{7}
$$
and $i$ denotes the direction of vibration of atom 0. Using the Green function $G_{00}\left(\omega^{2}\right)$, defined by
$$
G_{00}\left(\omega^{2}\right)=\left\langle 0, i\left|\left(\omega^{2} \mathbf{E}-\mathbf{D}\right)^{-1}\right| 0, i\right\rangle,
\tag{8}
$$
the LDOS can be rewritten as
$$
g_{00}^{i}(\omega)=-(2 \omega / \pi) \lim _{\varepsilon \rightarrow+0} \operatorname{Im} G_{00}\left(\omega^{2}+\mathrm{i} \varepsilon\right).
\tag{9}
$$

Changing the basis vector by the recurrence relations, the Green function $G_{00}\left(\omega^{2}\right)$ can be expressed as a continued fraction. We have calculated the recursion coefficients up to $n=10$ and have examined the convergence of the Green function when changing $n$ and the number of atoms in the system. The model structures of Au/Ni (1/1, 3/3, 5/5, 7/7 and 9/9) were obtained by molecular dynamics. For example, the (111) plane spacings of Au/Ni (3/3) structure are shown in table 3. It is seen clearly that the (111) spacings of the Au-Au and Ni-Ni planes increased, but that of the Au-Ni planes decreased. Within the (111) plane, both gold and nickel atoms scarcely shifted (about $10^{-4} \AA$ compared with a displacement of about $10^{-2} \AA$ along the [111] direction). In the preliminary simulations we fixed the positions of atoms outside the cylinder throughout the relaxation procedure. This effect may provide one of the reasons why the displacements of atoms are rather small. We performed the simulations again by using the 'free-surface' condition and found that almost all the results were the same. We could not find any misfit dislocation in the model structures either. This is in good agreement with the experimental result that misfit dislocations are introduced only when the modulation length is greater than about $10 \AA$.

The plots of $W$ against $\varepsilon^{2}$ of Au/Ni multilayer systems are shown in figure 1. The theoretical values of $Y[111]$ for pure Au and pure Ni were estimated to be 3.22 and 3.56 $(\times 10^{12} \mathrm{dyn} \mathrm{cm}^{-2})$ respectively, which are to be compared with the experimental values of 1.90 and $3.91(\times 10^{12} \mathrm{dyn} \mathrm{cm}^{-2})$ respectively. The elastic deformation of metallic superlattices does not obey Hooke's law. $Y[111]$ was estimated here as the slope of $W$ against $\varepsilon^{2}$, where $1.0 \times 10^{-6}<\varepsilon^{2}<12 \times 10^{-6}$. In figure 2 we show the theoretical values of biaxial $Y[111]$ as a function of the modulation length $\lambda$. The supermodulus effect of the Au/Ni superlattice is reproduced well in the present computer simulation. To gain further insight into the supermodulus effect, FCC Ni was strained by $1 \%$ along the [111] direction and the increase in the elastic energy was calculated for the strained lattice. $Y[111]$

Table 3. The (111) plane spacings $(\AA)$ and strains of the Au/Ni (3/3) structure.

<table>
  <thead>
    <tr>
      <th></th>
      <th>Before MD</th>
      <th>After MD</th>
      <th>Strain</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ni-Ni</td>
      <td>2.035</td>
      <td>2.070</td>
      <td>1.747%</td>
    </tr>
    <tr>
      <td>Ni-Au</td>
      <td>2.445</td>
      <td>2.382</td>
      <td>---</td>
    </tr>
    <tr>
      <td>Au-Au</td>
      <td>2.355</td>
      <td>2.382</td>
      <td>1.168%</td>
    </tr>
  </tbody>
</table>

![](./images/812653335432658950_1.jpg)

Figure 1. The plots of $W$ against $\varepsilon^{2}$ of Au/Ni metallic superlattices, where $W$ is the elastic energy and $\varepsilon$ is the strain along the [111] direction.

increased to $22.8\ (\times 10^{12}\ \mathrm{dyn\ cm^{-2}})$, which is much greater than the bulk value of 3.56 $(\times 10^{12}\ \mathrm{dyn\ cm^{-2}})$. From this result, the supermodulus effect of Au/Ni is considered to arise mainly from the modulated strain along the [111] direction. The LDOS of some atoms at and

![](./images/812653335432658950_2.jpg)

Figure 2. The theoretical values of $Y[111]$ as a function of the modulation length $\lambda$.

![](./images/812653335432658950_3.jpg)

Figure 3. The LDOS of (a) a gold atom at an interface, (b) a gold atom between gold planes, (c) a nickel atom at an interface, (d) a nickel atom between nickel planes. The panels show (reading upwards) the LDOS in the $x$, $y$ and $z$ directions and the average. The broken curve shows the spectrum from the bulk.

near the interface of Au/Ni (3/3) are shown in figure 3. As can be seen from the figure, the low-frequency region around $4 \times 10^{12}$ Hz is enhanced for atoms at the interface, while the high- and low-frequency peaks are broadened with respect to the bulk spectrum. This result is quite interesting because phonon softening may lead to high-$T_c$ superconductivity on the basis of the BCS mechanism. We may conclude that other metallic superlattices with large lattice mismatch (as in the case of Au/Ni) could show the same supermodulus effect.

## References

Das S K, Roy D and Sengupta S 1977 *J. Phys. F: Met. Phys.* **7** 5
Fujiwara T 1982 *J. Phys. F: Met. Phys.* **12** 661
Hashimoto M, Ishida Y, Wakayama S, Yamamoto R, Doyama M and Fujiwara T 1984 *Acta. Metall.* **32** 13
Haydock R 1980 *Solid State Phys.* **35** 215 (New York: Academic)
Henein G E and Hilliard J E 1983 *J. Appl. Phys.* **54** 728
Hilliard J E 1979 *AIP Conf. Proc.* **53** 407
Pickett W E 1982 *J. Phys. F: Met. Phys.* **12** 2195
Schuller I K and Falco C M 1982 *VSLI Electronics Microstructure Science* ed. N G Einspruch (New York: Academic) p 4
Schuller I K and Rahman A 1983 *Phys. Rev. Lett.* **50** 1377
Testardi L R, Williams R H, Krause J T, McWhan D B and Nakahara S 1981 *J. Appl. Phys.* **52** 510
Tsakalakos T and Hilliard J E 1983 *J. Appl. Phys.* **54** 734
Yang W M C, Tsakalakos T and Hilliard J E 1977 *J. Appl. Phys.* **48** 876