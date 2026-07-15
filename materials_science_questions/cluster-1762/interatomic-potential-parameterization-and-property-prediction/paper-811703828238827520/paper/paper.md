# Interpretation of the Co K-edge EXAFS in LaCoO₃ using molecular dynamics simulations

A. Kuzmin $^{a,*}$, V. Efimov $^{b}$, E. Efimova $^{b}$, V. Sikolenko $^{c}$, S. Pascarelli $^{d}$, I.O. Troyanchuk $^{e}$

$^{a}$ Institute of Solid State Physics, University of Latvia, Kengaraga street 8, LV-1063 Riga, Latvia
$^{b}$ Joint Institute for Nuclear Research, RU-141980 Dubna, Russia
$^{c}$ Laboratory of Neutron Scattering, ETH Zurich and Paul Scherrer Institute, CH-5232 Villigen, Switzerland
$^{d}$ European Synchrotron Radiation Facility, B.P. 220, F-38043 Grenoble Cedex, France
$^{e}$ Scientific-Practical Materials Research Centre NAS of Belarus, BY-220072 Minsk, Belarus

---

## A R T I C L E  I N F O

**Article history:**
Received 25 May 2010
Received in revised form 12 September 2010
Accepted 22 September 2010
Available online 12 November 2010

**Keywords:**
LaCoO₃
EXAFS
Co K-edge
Molecular dynamics
Thermal disorder

---

## A B S T R A C T

Temperature dependent (180–400 K) Co K-edge EXAFS spectra from perovskite-type rhombohedral ($R\ 3c$) LaCoO₃ have been successfully interpreted using a combination of classical NVT molecular dynamics (MD) and ab initio multiple-scattering (MS) theory. The method allowed us to account entirely for thermal disorder and to interpret reliably the contribution from the coordination shells beyond the first one into the total EXAFS spectrum taking into account many-body effects. The best agreement between experimental and configuration-averaged EXAFS spectra was obtained for pure ionic La³⁺ and partially ionic Co¹.³⁵⁺ and O¹.⁴⁵⁻ charges indicating the mixed ionic-covalent character of the Co—O bonds.

© 2010 Elsevier B.V. All rights reserved.

---

### 1. Introduction

Lanthanum cobaltite based perovskites are promising mixed ionic and electronic conducting materials for high temperature oxygen permeation membranes [1,2], catalysts and cathodes in solid oxide fuel cells (SOFCs) [3–5]. These materials possess high ionic conductivity at elevated temperatures due to a large oxygen vacancy concentration and a high vacancy diffusivity even in an oxidizing atmosphere [6,7]. The electronic conductivity of cobaltites is even higher and becomes metallic at high temperature [8–10]. The magnetic properties of cobaltites, related to the spin-state transitions of cobalt ions, are also of great interest [11].

LaCoO₃ has ABO₃-type perovskite structure with the rhombohedral space group $R\ 3c$ (No. 167), which is observed in the temperature range from 4 to 1248 K [12–14]. In the rhombohedral axes settings, the structure is described by lattice constant $a$, rhombohedral angle $\alpha$, and oxygen coordinate $x$. The La, Co, and O atoms occupy, respectively, $2a$ (1/4,1/4,1/4), $2b$(0,0,0), and $6e(x,1/2-x,3/4)$ Wyckoff positions in the unit cell containing two chemical formulas ($Z=2$). The rhombohedral symmetry involves an alternating rotation of the corner sharing $\text{CoO}_6$ octahedra along all three crystallographic axes of the undistorted, cubic ABO₃-type perovskite parent structure. Above ~1610 K, LaCoO₃ follows the second order structural phase transition from rhombohedral to cubic symmetry with one chemical formula per unit cell ($Z=1$) [15].

At low temperatures ($T$<50 K), LaCoO₃ shows nonmagnetic insulating ground state based on the low spin-state of trivalent cobalt (LS, $t_{2g}^6e_g^0$, $S=0$). Upon temperature increase, LaCoO₃ undergoes two magnetic transitions at ~100 K (diamagnetic-to-paramagnetic) and ~500 K (insulator-to-metal) connected with excitations either to the intermediate spin (IS, $t_{2g}^5e_g^1$, $S=1$) or to the high-spin state (HS, $t_{2g}^4e_g^2$, $S=2$) [16]. The magnetic susceptibility and the thermal expansion of LaCoO₃ show strongly anomalous temperature dependence and give an evidence of Jahn-Teller distortions of the $\text{CoO}_6$ octahedra in the IS state below 500 K [17].

The local atomic structure in LaCoO₃ has been intensively studied by the extended x-ray absorption fine structure (EXAFS) technique [18–24], which provides information complementary to that observed by diffraction methods. The extraction of reliable information from EXAFS spectra is based on a complex theoretical simulations and is still a challenge, especially, when many-body multiple-scattering (MS) effects contribute to the EXAFS spectrum, as it is in perovskites. A set of constraints is normally used to reduce the number of free parameters, describing the outer coordination shell contribution into the total EXAFS spectrum [23].

In this work we present the interpretation of the temperature dependent Co K-edge EXAFS spectra in LaCoO₃ by recently developed approach [25], which combines classical molecular dynamics (MD) and ab initio MS EXAFS theory. The advantage of our technique is its

---

* Corresponding author.
E-mail address: a.kuzmin@cfi.lu.lv (A. Kuzmin).
URL: http://www.cfi.lv (A. Kuzmin).

0167-2738/$ – see front matter © 2010 Elsevier B.V. All rights reserved.
doi:10.1016/j.ssi.2010.09.036

ability to significantly reduce the number of model parameters and to account entirely for disorder and many-body contributions.

## 2. Experimental and simulations
The polycrystalline $LaCoO_3$ sample was prepared by the ceramic method from a mixture of $La_2O_3$ and $Co_3O_4$ powders taken in stoichiometric ratios. The details of sample preparation procedure were published by us previously in [20,21,26].

The Co K-edge x-ray absorption spectra of $LaCoO_3$ were measured with high accuracy at the ESRF BM29 beamline (Grenoble, France). The storage ring operated at the energy 6.0 GeV and average current 180 mA. The synchrotron radiation was monochromatized using a Si (311) double-crystal monochromator. The spectra were recorded in transmission mode by two ionization chambers filled with argon gas. The gas pressure was approximately 0.08 and 0.25 bars in the first and second chambers, respectively. The closed-loop liquid helium cryostat was used to maintain the temperature of the sample.

The EXAFS oscillations $\chi(k)$ were extracted from the x-ray absorption spectra using the EDA software package following conventional procedure [27,28]. The EXAFS $\chi(k)$ was defined as

$$
\chi(k)=\left[\mu_{\exp }(E)-\mu_{0}(E)-\mu_{b}(E)\right] / \mu_{0}(E)
\tag{1}
$$

where $\mu_{\exp }(E)$ is the experimental absorption coefficient, $\mu_{b}(E)$ is the pre-edge background extrapolated beyond the absorption edge, $\mu_{0}(E)$ is the atomic-like contribution, and $k=[(2m_e/\hbar^2)(E-E_0)]^{1/2}$ is the wave vector, with $E_0$ being the photoelectron energy origin placed at the threshold energy of 7714 eV.

The Co K-edge EXAFS spectra $\chi(k)$ were interpreted by recently developed approach, based on the calculation of configuration-averaged EXAFS spectra for a set of atomic configurations obtained as a result of molecular dynamics (MD) simulations [25]. The classical NVT-type MD simulations were performed by the GULP3.1 code [29]. The force-field (FF) potential model accounted for pairwise (Co-O, La-O, and O-O) and three-body (Co-O-Co) interactions. The simulations were done using a $5a \times 5a \times 5a$ supercell (1250 atoms) with periodic boundary conditions. The lattice constant $a$ was equal to the experimental value [14] at corresponding simulation temperature.

The two-body interactions were described by the following potential

$$
U_{ij}(r_{ij})=A_{ij}exp(-r_{ij}/\rho_{ij})-C_{ij}/r_{ij}^{6}+Z_{i}Z_{j}e^{2}/r_{ij}.
\tag{2}
$$

Here the first two terms correspond to the Buckingham-type potential consisting of the Born-Mayer repulsive interaction between overlapping electron densities due to the Pauli principle and the attractive van der Waals interaction. The last term represents the Coulomb interaction between pairs of ions having charges $Z_i$ and $Z_j$.

The three-body interactions were accounted to reproduce the rotational motion of the $CoO_6$ octahedra and were described by the harmonic potential

$$
U_{ijk}=1/2k(\theta-\theta_{0})^{2}
\tag{3}
$$

where $k$ is the force constant, and $\theta_0$ is the equilibrium angle.

The starting values of the Buckingham potential parameters $(A, \rho$, and $C)$ were taken from [30]. However, the FF model in Ref. [30] corresponds to the cubic $LaCoO_3$ phase and is not able to describe the rhombohedral distortion. Therefore, the potential parameters were re-optimized by empirical fitting to observed structural properties [12-14] and bulk modulus $B_0=150$ GPa [31]. The final values of the potential parameters are reported in Table 1.

<table>
<caption>Table 1<br>Force-field potential model for $LaCoO_3$ used in the classical MD simulations. The ion charges $Z$ are also given.</caption>
<tbody>
<tr>
<td>Interaction</td>
<td colspan="3">Buckingham two-body potential (cutoff $20\ \mathring{A}$)</td>
</tr>
<tr>
<td></td>
<td>$A$ (eV)</td>
<td>$\rho$ ($\mathring{A}$)</td>
<td>$C$ (eV$\mathring{A}^6$)</td>
</tr>
<tr>
<td>$La^{3+}-O^{1.45-}$</td>
<td>1357.85</td>
<td>0.3456</td>
<td>0.0</td>
</tr>
<tr>
<td>$Co^{1.35-}-O^{1.45-}$</td>
<td>961.199</td>
<td>0.2795</td>
<td>0.0</td>
</tr>
<tr>
<td>$O^{1.45-}-O^{1.45-}$</td>
<td>22750.7</td>
<td>0.0552</td>
<td>37.01</td>
</tr>
<tr>
<td></td>
<td colspan="3">Three-body harmonic potential</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$k$ (eV/rad²)</td>
<td>$\theta$ (°)</td>
</tr>
<tr>
<td>$Co-O-Co$</td>
<td></td>
<td>347.67</td>
<td>163.79</td>
</tr>
</tbody>
</table>

The integration of Newton's equations during MD run was performed by the leapfrog Verlet method [29]. In each simulation, the structure was first equilibrated during 20 ps at the required temperature (180, 300, or 400 K), corresponding to that of the EXAFS experiment, and a set of instantaneous atomic configurations was accumulated during the 20 ps production run with a time step of 0.5 fs. Thus obtained sets of instantaneous atomic configurations were used to calculate the total and pair radial distribution functions (RDFs) (Fig. 1), which were used to evaluate the values of the structural parameters for the first six coordination shells (Table 2). Note that the MD simulations at 300 K were performed for several sets of ion charges to study their influence on the total EXAFS spectrum (Fig. 2).

The EXAFS spectra $\chi(k)k^{2}$ for each atomic configuration were calculated by the ab initio MS code FEFF8 [32]. At the first step of the MS calculations [25], the scattering cluster potential and partial phase shifts were evaluated only once for the cluster representing a part of the $LaCoO_3$ structure: it was centered at the absorbing cobalt atom and had a radius of 8 Å. Next, the EXAFS spectra $\chi(k)$ were calculated taking into account all MS contributions up to the 6th order with the half-path length up to 6 Å, that covers the range up to the sixth cobalt coordination shell. The complex exchange-correlation Hedin-Lundqvist potential and default values of muffin-tin radii, as provided within the FEFF8 code [32], were used. Finally, by averaging over all EXAFS

![](./images/811703828238827520_1.jpg)

Fig. 1. Upper panel: total and pair (Co-O, Co-La, and Co-Co) radial distribution functions (RDF) $G(R)$ for $LaCoO_3$ at 300 K obtained from the MD simulations. The first six coordination shells are indicated. Lower panel: total RDFs at 180, 300, and 400 K.

<table>
<caption>Table 2
Structural parameters for the first six coordination shells around cobalt in LaCoO₃ obtained from the MD simulations. $N$ is the coordination number, $R$ is the interatomic distance, and $\sigma^{2}$ is the MSRD.</caption>
<tbody>
<tr>
<td>
</td>
<td>
O₁
</td>
<td>
La₂
</td>
<td>
Co₃
</td>
<td>
O₄
</td>
<td>
O₅
</td>
<td>
Co₆
</td>
</tr>
<tr>
<td colspan="7">
Neutron diffraction data at $T = 300$ K [14]
</td>
</tr>
<tr>
<td>
$N$
</td>
<td>
6
</td>
<td>
$2 + 6$
</td>
<td>
6
</td>
<td>
$6 + 6$
</td>
<td>
$6 + 6$
</td>
<td>
$6 + 6$
</td>
</tr>
<tr>
<td>
$R$ (Å)
</td>
<td>
1.93
</td>
<td>
3.28
</td>
<td>
3.83
</td>
<td>
4.09
</td>
<td>
4.44
</td>
<td>
5.38
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
3.33
</td>
<td>
</td>
<td>
4.13
</td>
<td>
4.48
</td>
<td>
5.45
</td>
</tr>
<tr>
<td colspan="7">
$T = 180$ K
</td>
</tr>
<tr>
<td>
$N$
</td>
<td>
6.0
</td>
<td>
8.0
</td>
<td>
6.0
</td>
<td>
12.1
</td>
<td>
12.1
</td>
<td>
12.0
</td>
</tr>
<tr>
<td>
$R$ (Å)
</td>
<td>
1.93
</td>
<td>
3.31
</td>
<td>
3.82
</td>
<td>
4.11
</td>
<td>
4.45
</td>
<td>
5.41
</td>
</tr>
<tr>
<td>
$\sigma^{2}$ (Å²)
</td>
<td>
0.0016
</td>
<td>
0.0038
</td>
<td>
0.0024
</td>
<td>
0.0049
</td>
<td>
0.0048
</td>
<td>
0.0048
</td>
</tr>
<tr>
<td colspan="7">
$T = 300$ K
</td>
</tr>
<tr>
<td>
$N$
</td>
<td>
6.0
</td>
<td>
8.0
</td>
<td>
6.0
</td>
<td>
12.1
</td>
<td>
12.2
</td>
<td>
12.0
</td>
</tr>
<tr>
<td>
$R$ (Å)
</td>
<td>
1.93
</td>
<td>
3.32
</td>
<td>
3.83
</td>
<td>
4.12
</td>
<td>
4.45
</td>
<td>
5.42
</td>
</tr>
<tr>
<td>
$\sigma^{2}$ (Å²)
</td>
<td>
0.0032
</td>
<td>
0.0077
</td>
<td>
0.0048
</td>
<td>
0.0080
</td>
<td>
0.0085
</td>
<td>
0.0070
</td>
</tr>
<tr>
<td colspan="7">
$T = 400$ K
</td>
</tr>
<tr>
<td>
$N$
</td>
<td>
6.0
</td>
<td>
8.0
</td>
<td>
6.0
</td>
<td>
12.1
</td>
<td>
12.1
</td>
<td>
12.0
</td>
</tr>
<tr>
<td>
$R$ (Å)
</td>
<td>
1.94
</td>
<td>
3.33
</td>
<td>
3.84
</td>
<td>
4.14
</td>
<td>
4.46
</td>
<td>
5.43
</td>
</tr>
<tr>
<td>
$\sigma^{2}$ (Å²)
</td>
<td>
0.0040
</td>
<td>
0.0097
</td>
<td>
0.0063
</td>
<td>
0.0098
</td>
<td>
0.0098
</td>
<td>
0.0079
</td>
</tr>
</tbody>
</table>

![](./images/811703828238827520_2.jpg)

Fig. 2. Fourier transforms (FT) of the experimental (circles) and calculated for different ion charges configuration-averaged (solid lines) EXAFS $\chi(k)k^{2}$ spectra at 300 K. Both modulus and imaginary parts of FTs are shown.

![](./images/811703828238827520_3.jpg)

Fig. 3. Fourier transforms (FT) of the experimental (circles) and calculated configuration-averaged (solid and dashed lines) EXAFS $\chi(k)k^{2}$ spectra at 180, 300, and 400 K. Both modulus and imaginary parts of FTs are shown. SS means the single-scattering model which takes into account contributions only from the pair distribution functions. SS + MS means the model taking into account both pair and many-body (up to the 6th order) distribution functions.

spectra, one obtains configuration-averaged spectrum, which is directly compared with the experimental one (Fig. 3). Note that no adjustable parameters were used in the calculation of configuration- averaged EXAFS spectra. The position of the absorption edge in the experimental x-ray absorption spectrum was set once during the EXAFS spectrum extraction and was not varied further.

## 3. Results and discussion

The total and partial RDFs Co-O, Co-La, and Co-Co were obtained from the MD simulations and are shown in Fig. 1. The presence of rhombohedral distortion is evidenced by the existence of two groups of oxygen atoms $(O_{4}$ and $O_{5})$ , which form a single shell in the cubic phase. Note that in the rhombohedral phase, the $La_{2}, O_{4}, O_{5}$ , and $Co_{6}$ shells are additionally split into two sub-shells [14] (Table 2), which are not observed separately in the RDFs due to thermal disorder. The temperature increase from 180 to 400 K induces mainly the broadening of the RDF peaks, which is reflected by an increase of the mean square relative displacement (MSRD) values (Table 2). Besides, a small shift $(\sim 0.01 \AA)$ of the peaks position occurs due to the lattice thermal expansion.

Fourier transforms (FTs) of the experimental and calculated for several models configuration-averaged EXAFS $\chi(k) k^{2}$ spectra are compared in Figs. 2 and 3.

The MD simulations performed with different ion charges result in appreciably different FT shapes, in particular, in the region of outer coordination shells above $3 \AA$ (Fig. 2). The best agreement at 300 K isfound for purely ionic $La^{3+}$ and partially ionic $O^{1.35+}$ and $O^{1.45-}$  charges that indicates the mixed ionic-covalent character of the Co-O bonds [33,34]. Therefore, these charges were used further in the MD simulations at 180 and 400 K.

Temperature dependent results are shown in Fig. 3. Here, the contributions from the pairwise RDFs (single-scattering model) are also reported. As one can see, the amount of many-body effects is large in the region of the peak at $3.2 \AA$ , corresponding to the second $(La_{2})$ and third $(Co_{3})$ coordination shells. This result is expected in theperovskite-type compounds [35], since the multiple-scattering (MS) contributions from the Co-O-Co atomic chains are amplified due to the so-called focusing effect caused by the middle oxygen atom. Note that neglecting MS effects leads to significant underestimation of the peak amplitude at $3.2 \AA$ , especially at higher temperatures due to the weaker sensitivity of the MS spectra to disorder.

Note that the difference in the amplitude of the FT peak at $3.2 \AA$ for180 K arises because the classical MD fails to account for quantum effects. As a result, the MD simulation underestimates thermal disorder.

## 4. Conclusions

In this work a combination of classical NVT molecular dynamics(MD) and ab initio multiple-scattering (MS) theory [25) allowed us to reliably interpret temperature dependent (180-400 K) Co K-edge EXAFS spectra from perovskite-type rhombohedral $(R 3 c) LaCoO_{3}$ . The MD simulations were performed within a simple rigid-ion model based on the pairwise (Co-0, La-0, and 0-0) and three-body(Co-0-Co) interactions.

The approach allows reliable interpretation of the total EXAFS spectra taking into account both thermal disorder and many-body effects. Moreover, the model sensitivity to the ionic charges indicates the mixed ionic-covalent character of the Co-O bonds.

## Acknowledgments

This work was supported by ESF Project 2009/0202/1DP/1.1.1.2.0/09/APIA/VIAA/141, Latvian Government Research Grant No. 09.1518, and Russian Fund for Fundamental Research (Projects 09-02-01446-a and 10-02-01234-a). The experimental measurements at ESRF were performed within the project No. HS-3207.

## References

[1] J.W. Stevenson, T.R. Armstrong, R.D. Carneim, L.R. Peder, W.J. Weber, J. Electrochem. Soc. 143 (1996) 2722.
[2] J.H.E. van Doorn, H.J.M. Bouwmeester, A.J. Burggraaf, Solid State lonics 111(1998) 263.
[3] Y. Ohno, S. Nagata, H. Sato, Solid State lonics 9 (10) (1983) 1001.
[4] Y. Teraoka, T. Nobunaga, K. Okamoto, N. Miura, N. Yamazoe, Solid State lonics 48(1991) 207.
[5] C. Xia, Y. Lang, G. Meng, Fuel Cells 4 (2004) 41.
[6] R. Maric, S. Ohara, T. Fukui, H. Yoshida, M. Nishimura, T. Inagaki, K. Miurac, J. Electrochem. Soc. 146 (1999) 2006.2006.
[7] R.H.E. van Doorn, A.J. Burggraaf, Solid State lonics 128 (2000) 65.
[8] G. Thornton, B.C. Tofield, D.E. Williams, Solid State Commun. 44 (1982) 1213.
[9] Y. Tokura, Y. Okimoto, S. Yamaguchi, H. Taniguchi, T. Kimura, H. Takagi, Phys. Rev. B58 (1998) R1699.
[10] M. Imada, A. Fujimori, Y. Tokura, Rev. Mod. Phys. 70 (1998) 1039.
[11] N.B. Ivanova, S.G. Ovchinnikov, M.M. Korshunov, I.M. Eremin, N.V. Kazak, Phys. Usp.52 (2009) 789
[12] G. Thornton, B.C. Tofield, A.W. Hewat, J. Solid State Chem. 61 (1986) 301.
[13] A. Mineshige, M. Inaba, T. Yao, Z. Ogumi, K. Kikuchi, M. Kawase, J. Solid State Chem.121(1996)423
[14] P.G. Radaelli, S.-W. Cheong. Phys. Rev. B 66 (2002) 094408.
[15] Y. Kobayashi, T. Mitsunaga, G. Fujinawa, T. Ari, M. Suetake, K. Asai, J. Harada, J. Phys. Soc. Jpn.69(2000) 3468.
[16] K. Kniiek, Z. Jirak, J. Hejtmánek, P. Henry, G. André, J. Appl. Phys. 103 (07B703)(2008)
[17] C. Zobel, M. Kriener, D. Bruns, J. Baier, M. Gruninger, T. Lorenz, Phys. Rev. B 66 (2002)020402(R)
[18] O. Haas, R.P.W.J. Struis, J.M. McBreen, J. Solid State Chem. 177 (2004) 1000.
[19] S.K. Pandey, S. Khalid, N.P. Lalla, A.V. Pimpale, J. Phys.: Condens. Matter 18 (2006)10617.
[20] V. Efimov, E. Efimova, D. Karpinski, D.I. Kochubey, V. Kriventsov, A. Kuzmin, S. Molodtsov, V. Sikolenko, S. Tiutiunnikov, I.O. Troyanchuk, A.N. Shmakov, D. Vyalikh, Phys. Status Solidi C4(2007) 805.
[21] E. Efimova, V. Efimov, D. Karpinsky, A. Kuzmin, J. Purans, V. Sikolenko, S. Tiutiunnikov, I. Troyanchuk, E. Welter, D. Zajac, V. Simkin, A. Sazonov, J. Phys. Chem. Solids 69 (2008) 2187.
[22] N. Sundaram, Y. Jiang, I.E. Anderson, D.P. Belanger, C.H. Booth, F. Bridges, J.F. Mitchell, Th. Proffen, H. Zheng. Phys. Rev. Lett. 102 (2009) 026401.
[23] Y. Jiang, F. Bridges, N. Sundaram, D.P. Belanger, I.E. Anderson, J.F. Mitchell, H. Zheng, Phys. Rev. B 80 (2009) 144423.
[24] J.L. Hueso, J.P. Holgado, R.P. Pereiiguez, S. Mun, M. Salmeron, A. Caballero, J. Solid State Chem. 183(2010) 27.
[25] A. Kuzmin, R.A. Evarestov, J. Phys.: Condens. Matter 21 (2009) 055401.
[26] V.V. Efimov, E. Efimova, D. Karpinsky, D.I. Kochubey, V. Kriventsov, A. Kuzmin, S. Molodtsov, V. Sikolenko, J. Purans, S. Tiutiunnikov, I.O. Troyanchuk, A.N. Shmakov, D. Vyalikh, Nucl. Instrum. Meth. A 575 (2007) 176.
[27] A. Kuzmin, Physica B 208-209 (1995) 175.
[28] V.L. Aksenov, M.V. Kovalchuk, A.Yu. Kuzmin, Yu. Purans, S.I. Tyutyunnikov, Cryst. Rep.51(2006)908.
[29] J.D. Gale, A.L. Rohl, Mol. Simul. 9 (2003) 291
[30] M.S. Islam, M. Cherry, C.R.A. Catlow, J. Solid State Chem. 124 (1996) 230.
[31] T. Vogt, J.A. Hriljac, N.C. Hyatt, P. Woodward, Phys. Rev. B 67 (2003) 140401 (R).
[32] A.L. Ankudinov, B. Ravel, J.J. Rehr, S.D. Conradson, Phys. Rev. B 58 (1998) 7565.
[33] M. Abbate, R. Potze, G.A. Sawatzky, A. Fujimori, Phys. Rev. B 49 (1994) 7210.
[34] T. Saitoh, T. Mizokawa, A. Fujimori, M. Abbate, Y. Takeda, M. Takano, Phys. Rev. B 55(1997)4257.
[35] A. Kuzmin, J. Purans, M. Benfatto, C.R. Natoli, Phys. Rev. B 47 (1993) 2480.