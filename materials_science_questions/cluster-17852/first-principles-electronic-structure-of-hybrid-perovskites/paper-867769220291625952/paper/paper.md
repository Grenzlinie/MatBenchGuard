# Modeling of Lead Halide Perovskites for Photovoltaic Applications

Radi A. Jishi*¹, Oliver B. Ta², Adel A. Sharif³

¹ Department of Physics, California State University, Los Angeles, CA
² Department of Mechanical Engineering,
California State University, Los Angeles, CA

(Dated: May 22, 2014)

We report first-principles calculations, using the full potential linear augmented plane wave method, on six lead halide semiconductors, namely, ${\text{CH}}_{3}{\text{NH}}_{3}{\text{PbI}}_{3}$, ${\text{CH}}_{3}{\text{NH}}_{3}{\text{PbBr}}_{3}$, ${\text{CsPbX}}_{3}$ (X=Cl, Br, I), and ${\text{RbPbI}}_{3}$. Exchange is modeled using the modified Becke-Johnson potential. With an appropriate choice of the parameter that defines this potential, an excellent agreement is obtained between calculated and experimental band gaps of the six compounds. We comment on the possibility that the cubic phase of ${\text{CsPbI}}_{3}$, under hydrostatic pressure, could be a topological insulator.

PACS numbers:

Keywords: density functional theory, DFT, halide perovskites, solar cells, photovoltaics, mBJ, GW, topological insulators, WIEN2k

## I. INTRODUCTION

Recently, materials with halide perovskite structure, with the general formula ${\text{ABX}}_{3}$, have attracted great interest, primarily because of their potential applications as light harvesters in solar cells¹ and as topological insulators.²,³ Many studies have ensued with the aim of both improving the performance of these materials in photovoltaic cells and of understanding which physical parameters may determine the efficiencies.⁴⁻¹⁹ For example, Lee et al.¹⁶ report a solution-processable solar cell which uses a perovskite of mixed halide form, namely methylammonium lead iodide chloride, ${\text{CH}}_{3}{\text{NH}}_{3}{\text{PbI}}_{2}\text{Cl}$ (abbreviated as ${\text{MAPbI}}_{2}\text{Cl}$), with a solar-to-electrical power conversion efficiency of 10.9%. Using chemically-tuned ${\text{MAPb(I}}_{(1-x)}{\text{Br}}_{x}{\text{)}}_{3}$ perovskites as light harvesters, a mesoporous titanium dioxide ($\text{TiO}_{2}$)

film, and a hole-conducting polymer, Noh et al.¹⁷ demonstrate solar cells with a 12.3% power conversion efficiency. Burschka et al.¹⁸ describe a sequential deposition method whereby MAPbI₃ nanoparticles are formed within porous TiO₂, resulting in a power conversion ef- ficiency of 15%. Liu et al.¹⁹ have subsequently shown that such nanostructuring is not necessary for high efficiencies; a planar heterojunction solar cell, with a deposited thin film of MAPbI₂Cl acting as a light absorber, can achieve an efficiency exceeding 15%.

MAPbI₃ and similar compounds are derived from a class of trihalide perovskite structures with the formula ABX₃ (A=Cs, Rb; B=Pb; X=Cl, Br, I) by replacing the alkali-metal atom with methylammonium (MA). Such a replacement causes a large downshift in the semiconducting energy gap, making the compounds useful for photovoltaic applications. It is anticipated that different band gaps may be obtained by replacing methylammonium with other entities such as NH₄ or CH₂CH, by applying pressure, or by using thin films consisting of only a few layers.

To maximize the usefulness of such materials in photovoltaic applications, it is important to begin by developing computational techniques that accurately describe their electronic structure. Density functional theory in the Kohn-Sham formulation²⁰ is the most widely- used method. Here, the exchange-correlation potential is approximated by a functional of the electronic density. The most common approximations are the local density approximation (LDA),²⁰ the generalized gradient approximation (GGA),²¹ and the hybrid approximation.²² While LDA and GGA provide a successful description of ground-state properties in crystals, this success does not extend to a description of excited states. In many semiconductors, LDA and GGA strongly underestimate the value of the energy gap. Improved values for the band gaps are usually obtained by using the GW method.²³ However, the high computational cost of this method limits its applicability to crystals with a small number of atoms in the unit cell.

An exchange potential was recently proposed by Becke and Johnson (BJ), designed to yield the exact exchange potential in atoms.²⁴ Unfortunately, the use of this potential led to a slight improvement in the energy gap values for many semiconductors.²⁵ A simple modification of the BJ potential was proposed by Tran and Blaha.²⁶ In this method, known as TB-mBJ, the exchange potential is given by

$$
V_{x}^{TB\text{-}mBJ}(\mathbf{r}) = cV_{x}^{BR}(\mathbf{r}) + (3c - 2)\frac{1}{\pi}\sqrt{\frac{5}{12}}[2t(\mathbf{r})/\rho(\mathbf{r})]^{1/2}
\tag{1}
$$

where

$$
\rho(\mathbf{r}) = \sum_{i=1}^{N} |\psi_{i}(\mathbf{r})|^2
\tag{2}
$$

is the electron density ($N$ is the number of occupied orbitals and $\psi_{i}$ is the Kohn-Sham (KS) $i^{th}$ orbital wave function),

$$
t(\mathbf{r}) = \frac{1}{2}\sum_{i=1}^{N}[\nabla\psi_{i}^{*}(\mathbf{r}) \cdot \nabla\psi_{i}(\mathbf{r})]
\tag{3}
$$

is the KS kinetic energy density, and

$$
V_{x}^{BR}(\mathbf{r}) = -\frac{1}{b(\mathbf{r})}\left[1 - e^{-x(\mathbf{r})} - \frac{1}{2}x(\mathbf{r})e^{-x(\mathbf{r})}\right]
\tag{4}
$$

is the Becke-Roussel exchange potential.$^{27}$ The function $x(\mathbf{r})$ in the above equation is determined by a nonlinear equation involving $\rho$, $\nabla\rho$, $\nabla^2\rho$, and $t$. Once $x(\mathbf{r})$ is found, $b(\mathbf{r})$ is determined by

$$
b = x[e^{-x}/(8\pi\rho)]^{1/3}
\tag{5}
$$

In the TB-mBJ potential given in Eq (1),

$$
c = A + B\sqrt{g}
\tag{6}
$$

where

$$
g = \frac{1}{\Omega} \int \frac{1}{2}\left(\frac{|\nabla\rho_{\uparrow}(\mathbf{r})|}{\rho_{\uparrow}(\mathbf{r})} + \frac{|\nabla\rho_{\downarrow}(\mathbf{r})|}{\rho_{\downarrow}(\mathbf{r})}\right)d^3r
\tag{7}
$$

is the average of $|\nabla\rho/\rho|$ over the unit cell of volume $\Omega$. The parameters $A = -0.012$ and $B = 1.023$ bohr$^{1/2}$ were chosen because they produce the best fit to the experimental band gaps of many semiconductors. Studies have shown that the TB-mBJ potential is generally as accurate in predicting the energy gaps of many semiconductors as the much more expensive GW method.$^{28}$

Despite its many successes, however, the performance of the TB-mBJ method is not very satisfactory in certain cases, especially for transition metal oxides. To improve the band gap prediction, Koller, Tran, and Blaha$^{29}$ consider a more general form for c,

$$
c = A + Bg^{e} \tag{8}
$$

They vary the values of parameters $A$, $B$, and $e$ in order to improve the quality of the fit between the calculated and the experimental energy gaps of many semiconductors. There is an overall improvement in predicting the energy gaps of semiconductors with moderate gaps when $A = 0.267$, $B = 0.656$, and $e = 1$. The modified BJ method employing these values for $A$, $B$, and $e$ will be referred to as the KTB-mBJ method. It should be pointed out that, in terms of computational time and resources, the requirements for the TB-mBJ and KTB-mBJ methods are essentially the same as those for standard LDA or GGA methods. Therefore, these methods may be easily used to calculate the electronic structure of crystals with large unit cells, where the cost of the GW method is prohibitive.

In this work, we present first-principles calculations on the electronic structure of six compounds, namely $MAPbI_3$, $MAPbBr_3$, $CsPbX_3$ (X=Cl, Br, I), and $RbPbI_3$. All of these compounds have a perovskite structure, characterized by a Pb atom that is octahedrally coordinated to six halogen atoms. We show that GGA, when spin-orbit coupling (SOC) is included, severely underestimates the band gaps in these semiconducting materials. Though TB-mBJ and KTB-mBJ methods lead to significant improvement in the values of the gaps, both methods still underestimate the energy gaps by a wide margin. We then show that keeping parameters $B$ and $e$ essentially the same as in TB-mBJ, while adopting a new value for $A$ leads to results that are in excellent agreement with experimental values.

## II. METHODS

Total energy and band structure calculations are carried out using the all-electron, full potential, linear augmented plane wave (FP-LAPW) method as implemented in the WIEN2k code.$^{30}$ Here, each atom is surrounded by a muffin-tin sphere, and the total space is divided into two regions. One region consists of the interior of these nonoverlapping spheres, while the rest of the space constitutes the interstitial region. The radii of the muffin-tin spheres are $2.5\ a_0$ for Cs, Rb, Pb, I, and Br, $2.37\ a_0$ for Cl, $1.27\ a_0$ for N, $1.33\ a_0$ for C, and $0.68\ a_0$

for H, where $a_0$ is the Bohr radius. In GGA calculations, the exchange correlation potential is that proposed in reference. $^{21}$

The valence electrons' wave functions inside the muffin-tin spheres are expanded in terms of spherical harmonics up to $l_{max}=10$. In the interstitial regions, they are expanded in terms of plane waves, with a wave vector cutoff of $K_{max}$. Because of the small muffin-tin radius of hydrogen atoms, we set $R_H K_{max}=3$ in $CH_3NH_3PbI_3$ and $CH_3NH_3PbBr_3$, where $R_H=0.68\ a_0$ is the muffin-tin radius of the H atom. In the remaining four compounds, we set $R_{mt}K_{max}=9$, where $R_{mt}$ is the smallest muffin-tin radius. The charge density is Fourier expanded up to a maximum wave vector of $G_{max}$, where $G_{max}=20\ a_0^{-1}$ for $MAPbI_3$ and $MAPbBr_3$, and $G=13\ a_0^{-1}$ for the remaining compounds. The convergence of the self-consistent calculations is achieved with a total energy tolerance of 0.1 mRy and a charge convergence of 0.001 e.

## III. III. RESULTS AND DISCUSSION

At high temperatures, lead halide perovskites have a simple cubic unit cell, where Pb sits at the center of the cube and is octahedrally coordinated to six halogen atoms, while alkali atoms sit at the cube corners, as shown in Fig. 1. As the temperature is lowered, distortions lead to tetragonal and/or orthorhombic structures. In our calculations, we use the room temperature crystal structures of the various compounds. These are listed in Table I. For $CsPbI_3$, which is orthorhombic at room temperature, we also study the high temperature cubic phase, which was predicted to be a topological insulator when subjected to hydrostatic pressure. $^{2}$

We carried out band structure calculations on the six compounds shown in Table I. Using GGA, we found that, upon including the effect of SOC, the band gaps of all compounds are severely underestimated. The values of the gaps are improved by using the TB-mBJ method, and are improved further by using the KTB-mBJ method. However, the improvement does not go far enough, and the gaps are still far below the experimental values. We thus considered a new set of values for the parameters that appear in Eq. (8), namely,

$$
A=0.4,\ B=1.0,\ e=0.5 \tag{9}
$$

The parameters $B$ and $e$ are essentially the same as in the TB-mBJ method, but the

![](./images/867769220291625952_1.jpg)

FIG. 1: (Color online) Cubic perovskite structure with alkali atoms occupying the A sites, Pb atoms occupying the B sites, and halogen atoms occupying the X sites.

<table>
<caption>Crystal structure and lattice constants for the compounds studied in this work.</caption>
<thead>
<tr>
<th>Compound</th>
<th>Structure</th>
<th>Lattice constants (Å)</th>
</tr>
</thead>
<tbody>
<tr>
<td>CH₃NH₃PbI₃</td>
<td>Tetragonal</td>
<td>a=8.856, c=12.655ᵃ</td>
</tr>
<tr>
<td>CH₃NH₃PbBr₃</td>
<td>Cubic</td>
<td>a=5.933ᵇ</td>
</tr>
<tr>
<td>CsPbCl₃</td>
<td>Cubic</td>
<td>a=5.605ᶜ</td>
</tr>
<tr>
<td>CsPbBr₃</td>
<td>Orthorhombic</td>
<td>a=8.244, b=11.735, c=8.198ᵈ</td>
</tr>
<tr>
<td>RbPbI₃</td>
<td>Orthorhombic</td>
<td>a=10.276, b=4.779, c=17.393ᵉ</td>
</tr>
<tr>
<td>CsPbI₃</td>
<td>Orthorhombic</td>
<td>a=10.458, b=4.801, c=17.776ᵉ</td>
</tr>
<tr>
<td>CsPbI₃</td>
<td>Cubic</td>
<td>a=6.2894ᵉ</td>
</tr>
</tbody>
</table>

ᵃ Poglitsch and Weber³¹
ᵇ Mashiyama et al.³²
ᶜ Moreira and Dias³³
ᵈ Stoumpos et al.³⁴
ᵉ Trots and Myagkota³⁵

parameter $A$ is different. With this new set of values for $A$, $B$, and $e$, the calculated band gaps of all six compounds are in excellent agreement with the experimental values. Our results are summarized in Table II where we present the band gaps calculated by using different methods. The gaps obtained by using the above values for $A$, $B$, and $e$ are given

<table>
<caption>TABLE II: Calculated and experimental band gaps, in eV, for the compounds that are studied in this work. The band gaps obtained by using parameters in Eq. (9) are reported under "Present method."</caption>
<thead>
<tr>
<th>Compound</th>
<th>GGA</th>
<th>GGA+so</th>
<th>TB-mBJ</th>
<th>KTB-mBJ</th>
<th>Present method</th>
<th>Experimental</th>
</tr>
</thead>
<tbody>
<tr>
<td>CH₃NH₃PbI₃</td>
<td>1.492</td>
<td>0.377</td>
<td>0.844</td>
<td>0.921</td>
<td>1.544</td>
<td>1.5-1.6[a,b]</td>
</tr>
<tr>
<td>CH₃NH₃PbBr₃</td>
<td>1.668</td>
<td>0.453</td>
<td>1.183</td>
<td>1.406</td>
<td>2.233</td>
<td>2.28[a]</td>
</tr>
<tr>
<td>CsPbCl₃</td>
<td>2.498</td>
<td>0.707</td>
<td>1.585</td>
<td>1.889</td>
<td>2.829</td>
<td>2.86[c]</td>
</tr>
<tr>
<td>CsPbBr₃</td>
<td>1.794</td>
<td>0.669</td>
<td>1.316</td>
<td>1.461</td>
<td>2.228</td>
<td>2.24[c,d]</td>
</tr>
<tr>
<td>RbPbI₃</td>
<td>2.468</td>
<td>1.828</td>
<td>2.387</td>
<td>2.446</td>
<td>3.302</td>
<td>3.17[e]</td>
</tr>
<tr>
<td>CsPbI₃</td>
<td>2.504</td>
<td>1.876</td>
<td>2.426</td>
<td>2.476</td>
<td>3.330</td>
<td>3.14[e]</td>
</tr>
<tr>
<td>CsPbI₃ (cubic)</td>
<td>1.324</td>
<td>0.072</td>
<td>0.485</td>
<td>0.529</td>
<td>1.072</td>
<td>-</td>
</tr>
</tbody>
</table>

$^{\mathrm{a}}$ Noh $et$ $al.^{17}$
$^{\mathrm{b}}$ Baikie $et$ $al.^{36}$
$^{\mathrm{c}}$ Liu $et$ $al.^{37}$
$^{\mathrm{d}}$ Stoumpos $et$ $al.^{34}$
$^{\mathrm{e}}$ Yunakova $et$ $al.^{38}$

in the column labeled 'Present method.'

The calculated energy bands of MAPbI₃ along high symmetry directions in the Brillouin zone (BZ), in addition to the electronic density of states, are presented in Fig. 2. The valence band maximum (VBM) and conduction band minimum (CBM) occur at the $\Gamma$-point, the BZ center. In cubic perovskites, the gap occurs at point R(1/2, 1/2, 1/2). However, at room temperature, MAPbI₃ has a body-centered tetragonal crystal structure with two formula units per primitive cell. Its conventional unit cell, containing four formula units, is a slightly distorted $\sqrt{2} \times \sqrt{2} \times 2$ supercell of the high temperature cubic phase unit cell. The distortion consists mainly of a rotation of the octahedron by 10.45 $^\circ$ about the c-axis. Point R of the cubic lattice BZ is zone-folded into the $\Gamma$-point of the body-centered tetragonal lattice BZ.

The density of states of MAPbI₃ is shown in Fig. 2, where we see that the low-lying conduction bands are derived from Pb p states. On the other hand, the bands in the range -4 eV to -2 eV are dominated by iodine-derived states. The valence band just below the Fermi energy is derived from lead s and iodine p states. These observations become clear

![](./images/867769220291625952_2.jpg)

FIG. 2: (Color online) Band structure and density of states of $CH_3NH_3PbI_3$.

upon considering the atomic orbital character of the bands, which is presented in Fig. 3.
The size of the circles is indicative of the contribution of the chosen atomic orbital to the
eigenstates at each $\mathbf{k}$-point. The CBM is derived mostly from Pb 6p states. The VBM, on
the other hand, is a mixture of Pb 6s and I 5p states. The antibonding state formed from
these s and p states is pushed up in energy close to the Fermi level. The large contribution
of Pb 6s ($l=0$) states to the VBM and Pb 6p ($l=1$) states to the CBM suggests that there
are strong optical transitions between the VBM and CBM ($\Delta l=1$), hence the usefulness of
this material in solar applications.

$CH_3NH_3PbBr_3$ ($MAPbBr_3$) has a cubic unit cell. Its band structure is shown in Fig. 4,
and, as expected, the band gap occurs at point R(1/2, 1/2, 1/2) in the Brillouin zone. As
with the case of $MAPbI_3$, its VBM is a mixture of Pb 6s and Br 4p states, whereas its
CBM is derived from Pb 6p states. In the absence of SOC, its CBM is six-fold degenerate
(including spin degeneracy). Due to SOC, its CBM is split into a doublet ($j=1/2$) and a
quartet ($j=3/2$). The doublet is lowered in energy by an amount $\lambda$, whereas the quartet
is raised in energy by $\lambda/2$, where $\lambda\approx1.1$ eV. Similar perovskite structures, namely $CsSnX_3$
(X=Cl, Br, I), where Sn replaces Pb, show a much smaller spin splitting of $\sim0.4$ eV.$^{39}$ Since
the VBM is composed of Pb s and Br p orbitals, it is shifted slightly upward due to SOC
on Br atoms. The large energy split of the CBM is, of course, due to the strong SOC on Pb

![](./images/867769220291625952_3.jpg)

FIG. 3: (Color online) Orbital character of the valence and conduction bands of $CH_3NH_3PbI_3$.
The contribution of the selected orbital is proportional to the size of the circle, with a single point
denoting zero contribution. (a) Pb 6s orbital, (b) Pb 6p orbital, and (c) I 5p orbital.

atoms.

Finally, we consider the $CsPbI_3$ crystal. At high temperature ($>634$K), the crystal is
cubic, but at room temperature, it is strongly distorted to an orthorhombic structure. Based
on LDA and sx-LDA calculations, it has been suggested that, under hydrostatic pressure, the
cubic phase might become a topological insulator.$^2$ Calculations made using sx-LDA suggest
a gap of 0.566 eV for $CsPbI_3$ and 0.218 eV for $CsSnI_3$. With decreasing lattice constants, the
band width increases and the band gap decreases; at some critical pressure, band inversion
occurs. For $CsPbI_3$ and $CsSnI_3$, those critical pressures are predicted to be 3.33 GPa and
0.96 GPa, respectively. However, GW calculations on $CsSnI_3$ give a much larger band gap
of 1.008 eV.$^{39}$ Our calculation on the cubic phase of $CsPbI_3$ shows that the band gap is 1.07
eV, larger by 0.5 eV than predicted by sx-LDA. Assuming linear dependence of the energy
gap on lattice constant,$^2$ a critical pressure of 6.6 GPa has to be applied to cause band
inversion.

The band structure of cubic $CsPbI_3$ is shown in Fig. 5. The band gap occurs at point
R. As in the cases discussed previously, its CBM is derived from Pb 6p states, whereas its

![](./images/867769220291625952_4.jpg)

FIG. 4: (Color online) Band structure and partial density of states of CH₃NH₃PbBr₃.

VBM is a mixture of Pb 6s and I 5p states. Without SOC, the calculated band gap is 2.27 eV, and the CBM is six-fold degenerate (including spin degeneracy). SOC on Pb splits its CBM into a doublet ($j=1/2$) and a quartet ($j=3/2$). The doublet is lowered in energy by 1.1 eV, while the quartet is raised by 0.55 eV. On the other hand, SOC on the I atoms raises the VBM by 0.1 eV.

As a further check on our results for cubic CsPbI₃, we repeated the calculation of the band gap using the GW approximation within the linear augmented plane wave formalism.⁴⁰ In this method, the electron's proper self energy $\Sigma^{*}$ is approximated as a product of the electron Green's function (G) and an effective interaction term (W). We carried out the calculation in the absence of spin-orbit coupling and using the G₀W₀ and GW₀ approximations. The electron's proper self energy in these approximations is shown graphically in Fig. 6. We found that within the G₀W₀ approximation, the band gap is 2.04 eV, and it increases to 2.19 eV upon employing the GW₀ approximation. This result is in excellent agreement with, the value of 2.27 eV, which we obtained for the band gap, in the absence of SOC, by using the modified Becke-Johnson form of the exchange potential.

In conclusion, we have presented electronic structure calculations on six lead halide compounds using the modified Becke-Johnson method. We used the experimental crystal structure of these compounds at room temperature. We found that by modifying the parameters

![](./images/867769220291625952_5.jpg)

FIG. 5: (Color online) Band structure and partial density of states of cubic CsPbI₃.

![](./images/867769220291625952_6.jpg)

FIG. 6: The electron's proper self energy in the (a) GW approximation, (b) GW₀ approximation,
and (c) G₀W₀ approximation. W and W₀ are given in (d) and (e), respectively. The single solid
line is the noninteracting electron propagator, while the double solid line is the interacting electron
propagator. The single dashed line is the bare Coulomb interaction. The double-dashed line (W)
is the screened Coulomb interaction in the GW approximation, while the wavy line (W₀) is the
screened Coulomb interaction in the random phase approximation.

that characterize the TB-mBJ method, we obtain band gaps that are in excellent agreement with experiment. Using this new set of parameters, one should be able to predict the elec- tronic structure of phases of these compounds that occur at different temperatures, as well as those of similar compounds obtained by replacing the alkali metal with various organic cations.

## Acknowledgments

We gratefully acknowledge support by NSF under grant No. HRD-0932421.

[1] Kojima, A.; Teshima, K.; Shirai, Y.; Miyasaka, T. Organometal Halide Perovskites as Visible- Light Sensitizers for Photovoltaic Cells. J. Am. Chem. Soc. 2009, 131, 6050-6051.

[2] Jin, H.; Im, J.; Freeman, A. J. Topological Insulator Phase in Halide Perovskite Structures. Phys. Rev. B 2012, 86, 121102.

[3] Yang, K.; Setyawan, W.; Wang, S.; Nardelli, M. B.; Curtarolo, S. A Search Model for Topo- logical Insulators with High-Throughput Robustness Descriptors. Nature Materials 2012, 11,614-619.

[4] Etgar, L.; Gau, P.; Xue, Z.; Peng, Q.; Chandiran, A. K.; Liu, B.; Nazeeruddin, M. K.; Grätzel, M. Mesoscopic $CH_{3}NH_{3}PbI_{3}/TiO_{2}$ Heterojunction Solar Cells. J. Am. Chem. Soc 2012, 134,17396-17399.

[5] Ball, J. M.; Lee, M. M.; Hey, A.; Snaith, H. J. Low-Temperature Processed Meso- Superstructured to Thin-Film Perovskite Solar Cells. Energy Env. Sci. 2013, 6, 1739-1743.

[6] Heo, H. J.; Im, S. H.; Noh, J. H.; Mandal, T. N.; Lim, C.-S.; Chang, J. A.; Lee, Y. H.; Kim, H.-j.; Sarkar, A.; Nazeeruddin, Md. K.; Grätzel, M.; Seok, S. I. Efficient Inorganic- Organic Hybrid Heterojunction Solar Cells Containing Perovskite Compound and Polymeric Hole Conductors. Nature Photonics 2013, 7, 486-491.

[7] Kim, H.-S.; Lee, J.-W.; Yantara, N.; Biox, P. B.; Kulkarni, S. A.; Mhaisalker, S.; Grätzel, M.; Park, N.-G. High Efficiency Solid-State Sensitized Solar Cell-Based on Submicrometer Rutile $TiO_{2}$ Nanorod and $CH_{3}NH_{3}PbI_{3}$ Perovskite Sensitizer. Nanolett. 2013, 13, 2412-2417.

[8] Bi, D.; Yang, L.; Boschloo, G.; Hagfeldt, A.; Johansson, E. M. J. Effect of Different Hole

Transport Materials on Recombination in $CH_3NH_3PbI_3$ Perovskite-Sensitized Mesoscopic Solar Cells. J. Phys. Chem. Lett. 2013, 4, 1532-1536.

[9] Cai, B.; Xing, Y.; Yang, Z.; Zhang, W.-H.; Qiu, J. High Performance Hybrid Solar Cells Sensitized by Organolead Halide Perovskites. Energy Env. Sci. 2013, 6, 1480-1485.

[10] Eperon, G. E.; Burlakov, V. M.; Docampo, P.; Goriely, A.; Snaith, H. J. Morphological Control for High Performance, Solution-Processed Planar Heterojunction Perovskite Solar Cells. Advanced Functional Materials 2014, 24, 151-157.

[11] Laban, W. A.; Etgar, L. Depleted Hole Conductor-Free Lead Halide Iodide Heterojunction Solar Cells. Energy Env. Sci. 2014, 6, 3249-3253.

[12] Stranks, S. D.; Eperon, G. E.; Grancini, G.; Menelaou, C.; Alcocer, M. J. P.; Leijtens, T.; Herz, L. M.; Petrozza, A.; Snaith, H. J. Electron-Hole Diffusion Lengths Exceeding 1 Micrometer in an Organometal Trihalide Perovskite Absorber. Science 2013, 342, 341-344.

[13] Mosconi, E.; Amat, A.; Nazeeruddin, Md. K.; Grätzel, M.; De Angelis, F. First-Principles Modeling of Mixed Halide Organometal Perovskites for Photovoltaic Applications. J. Phys. Chem. C 2013, 117, 13902-13913.

[14] Wang, Y.; Gould, T.; Dobson, J. F.; Zhang, H.; Yang, H.; Yao, X.; Zhao, H. Density Functional Theory Analysis of Structural and Electronic Properties of Orthorhombic Perovskite $CH_3NH_3PbI_3$. Phys. Chem. Chemical Phys. 2014, 16, 1424-1429.

[15] Umari, P.; Mosconi, E.; De Angelis, F. Relativistic GW calculations on $CH_3NH_3PbI_3$ and $CH_3NH_3SnI_3$ Perovskites for Solar Cell Applications. Scientific Reports 2014, 4, Article number: 4467.

[16] Lee, M. M.; Teuscher, J.; Miyasaka, T.; Murakami, T. N.; Snaith, H. J. Efficient Hybrid Solar Cells Based on Meso-Superstructured Organometal Halide Perovskites. Science 2012, 338, 643-647.

[17] Noh, J. H.; Im, S. H.; Heo, J. H.; Mandal, T. N.; Seok, S. I. Chemical Management for Colorful, Efficient, and Stable Inorganic-Organic Hybrid Nanostructured Solar Cells. Nano Lett. 2013, 13, 1764-1769.

[18] Burschka, J.; Pellet, N.; Moon, S.-J.; Humphry-Baker, R.; Gao, P.; Nazeeruddin, M. K.; Grätzel, M. Sequential Deposition as a Route to High-Performance Perovskite-Sensitized Solar Cells. Nature 2013, 499, 316-319.

[19] Liu, M.; Johnston, M. B.; Snaith, H. J. Efficient Planar Heterojunction Perovskite Solar Cells

by Vapour Deposition. **Nature** 2013, 501, 395-398.

[20] Kohn, W.; Sham, L. J. Self-Consistent Equations Including Exchange and Correlation Effects. *Phys. Rev.* 1965, 140, A1133-A1138.

[21] Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. *Phys. Rev. Lett.* 1996, 77, 3865-3868.

[22] Becke, A. D. A New Mixing of Hartree-Fock and Local Density-Functional Theories. *J. Chem Phys.* 1993, 98, 1372-1377.

[23] Bechstedt, F.; Fuchs, F.; Kresse, G. Ab-initio Theory of Semiconductor Band Structures: New Developments and Progress. *Phys. Status Solidi B* 2009, 246, 1877-1892.

[24] Becke, A. D.; Johnson, E. R. A Simple Effective Potential for Exchange. *J. Chem. Phys.* 2006, 124, 221101.

[25] Tran, F.; Blaha, P.; Schwarz, K. Band Gap Calculations with Becke-Johnson Exchange Po- tential. *J. Phys.: Condens. Matter* 2007, 19, 196208.

[26] Tran; F.; Blaha, P. Accurate Band Gaps of Semiconductors and Insulators with a Semilocal Exchange-Correlation Potential. *Phys. Rev. Lett.* 2009, 102, 226401.

[27] Becke, A. D.; Roussel, M. R. Exchange Holes in Inhomogeneous Systems: A Coordinate-Space Model. *Phys. Rev. A* 1989, 39, 3761-3767.

[28] Koller, D.; Tran; F.; Blaha, P. Merits and Limits of the Modified Becke-Johnson Exchange Potential. *Phys. Rev. B* 2011, 83, 195134.

[29] Koller, D.; Tran, F.; Blaha, P. Improving the Modified Becke-Johnson Exchange Potential. *Phys. Rev. B* 2012, 85, 155109.

[30] Blaha, P.; Schwarz, K.; Madsen, G. K. H.; Kvasnicka, D.; Luitz, J. WIEN2K: An Augmented Plane Wave and Local Orbitals Program for Calculating Crystal Properties, edited by Schwarz, K. Techn. Vienna University of Technology, Austria), 2001.

[31] Poglitsch, A.; Weber, D. Dynamic Disorder in Methylammoniumtrihalogenoplumbates (II) Observed by Millimeter-Wave Spectroscopy. *J. Chem. Phys* 1987, 87, 6373-6378.

[32] Mashiyama, H.; Kurihara, Y.; Azetsu, T. Disordered Cubic Perovskite Structure of CH₃NH₃PbX₃ (X=Cl,Br,I). *J. Korean Physical Soc.* 1998, 32, S156-S158.

[33] Moreira, R. L.; Dias, A. Comment on "Prediction of Lattice Constant in Cubic Perovskites". *J. Phys. Chem. Solids* 2007, 68, 1617-1622.

[34] Stoumpos, C. C.; Malliakas, C. D.; Peters, J. A.; Liu, Z.; Sebastian, M.; Im, J.; Chasapis,

T. C.; Wibowo, A. C.; Chung, D. Y.; Freeman, A. J.; Wessels, B. W.; Kanatzidis, M. G.
Crystal Growth of the Perovskite Semiconductor $CsPbBr_3$: A New Material for High-Energy
Radiation Detection. *Cryst. Growth Des.* **2013**, 13, 2722-2727.

[35] Trots, D. M.; Myagkota, S. V. High-Temperature Structural Evolution of Caesium and Ru-
bidium Triiodoplumbates. *J. Phys. Chem. Solids* **2008**, 69, 2520-2526.

[36] Baikie, T.; Fang, Y.; Kadro, J. M.; Schreyer, M.; Wei, F.; Mhaisalkar, S. G.; Graetzel, M.;
White, T. J. Synthesis and Crystal Chemistry of the Hybrid Perovskite $(CH_3NH_3)PbI_3$ for
Solid-State Sensitised Solar Cell Applications. *J. Mater. Chem. A* **2013**, 1, 5628-5641.

[37] Liu, Z.; Peters, J. A.; Stoumpos, C. C.; Sebastian, M.; Wessels, B. W.; Im, J.; Freeman,
A. J.; Kanatzidis, M. G. Heavy Metal Ternary Halides for Room-Temperature X-Ray and
Gamma-Ray Detection. *Proc. SPIE* **2013**, 8852, 88520A.

[38] Yunakova, O. N.; Miloslavskii, V. K.; Kovalenko, E. N. Exciton Absorption Spectrum of Thin
$(KI)_{1-x}(PbI_2)_x$ films. *Functional Materials* **2013**, 20, 59-63.

[39] Huang, L. Y.; Lambrecht, W. R. L. Electronic Band Structure, Phonons, and Exciton Binding
Energies of Halide Perovskites $CsSnCl_3$, $CsSnBr_3$, and $CsSnI_3$. *Phys. Rev. B* **2013**, 88, 165203.

[40] Jiang, H.; Gómez-Abal, R. I.; Li, X.-Z.; Meisenbichler, C.; Ambrosch-Draxl, C.; Scheffler, M.
FHI-gap : A GW Code Based on the All-Electron Augmented Plane Wave method. *Computer
Phys. Commun.* **2013**, 184, 348-366.