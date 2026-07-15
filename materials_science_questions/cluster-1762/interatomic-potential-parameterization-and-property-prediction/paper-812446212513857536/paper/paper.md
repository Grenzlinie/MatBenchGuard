# ELECTRONIC STRUCTURE OF CeAg
S.W. LUH and T.L. LIU

Department of Physics, National Tsing Hua University, Hsinchu, Taiwan

Received 25 February 1987
Revised manuscript received 1 October 1987

The Slater-Koster interpolation method is used in combination with the standard KKR method to get a set of quickly applicable energy bands for a mixed valence intermetallic compound CeAg.

## 1. Introduction

Cerium compounds have attracted much interest lately because of their unusual properties obviously associated with the 4f electrons. To understand these properties it is usually necessary to obtain rather detailed knowledge of their electronic structure. Here in this short article we like to report the calculated results on the electronic energy bands of a cerium intermetallic compound, CeAg, by a method combining the KKR [1,2] and Slater-Koster (SK) [3,4] methods, which we think, should give a quickly applicable band profile without too much lengthy and complicated computations.

We know that the KKR method is one of the most powerful and reliable methods in band calculations. However the complexity of the computational techniques can be handled properly only by experts. What we intend to do in this work is to evaluate the $E(k)$ values by the KKR method only at the high symmetry points in the Brillouin zone and let the intermediate $E(k)$ values be determined by the interpolation scheme of the Slater-Koster method. In this way, the accuracy may not be as high as that of a standard KKR calculation, but the general features of the electronic properties can be quickly observed.

CeAg has the CsCl-type structure at low temperature with a lattice constant of $3.78 \AA$, and becomes ferromagnetic below 6 K with a very small magnetic moment of $0.95 \mu_{\mathrm{B}}$ per atom [5]
which shows that weak hybridization between f and s, d bands may occur in this alloy [6]. In order to see the effect of the mixed valence nature of Ce in the alloy, we have done the calculations for both the two configurations of Ce, i.e. $4 \mathrm{f}^{1} 5 \mathrm{~d}^{1} 6 \mathrm{~s}^{2}$ and $4 \mathrm{f}^{2} 5 \mathrm{~d}^{0} 6 \mathrm{~s}^{2}$.

In section 2 we shall give a brief description of the methods, including KKR, SK and KKR-SK fitting and the way by which we determine the potential. Then in section 3 we shall present the results and give a conclusive discussion.

## 2. Methods

The details of the KKR method have been given elsewhere [1,2,7]. Here we shall simply review the basic working formula that will be used in this work. In the KKR method, if a muffin-tin type potential is assumed the crystal wave functions inside the muffin-tin can be expanded in the form:

$$
\Psi(E, r)=\sum_{l=0}^{\infty} \sum_{m=-l}^{+l} C_{l m} R_{l}(E, r) Y_{l m}(\theta, \phi), \quad \text { (1) }
$$

where the $Y_{l m}$'s are the spherical harmonics and the $R_{l}$'s satisfy the radial part of the Schrödinger equation. The determination of the constants $C_{l m}$ leads to a secular determinant

$$
\operatorname{det}\left|A_{l m, l^{\prime} m^{\prime}}+\kappa \delta_{l l^{\prime}} \delta_{m m^{\prime}} \cdot\left(\frac{n_{l^{\prime}}-n_{l} L_{l}}{j_{l^{\prime}}-j_{l} L_{l}}\right)_{r=r_{i}}\right|=0,
\tag{2}
$$

where $\kappa=\sqrt{E}$ and $A_{l m, l^{\prime} m^{\prime}}$ are the structure constants which depend only on the structure of the crystals and are dependent on energy $E$ and the reciprocal lattice vector $\boldsymbol{k}$. The second term in the determinant corresponds to the partial wave scattering phase shifts, and depends only on the properties of the atoms through the choice of potentials and is dependent of energy $E$. The $L_{l}$'s are the logarithmic derivatives of the $l$th-order radial functions, the $j$'s and $n$'s are the standard spherical Bessel functions. The energy eigenvalues are then evaluated by the zeros of the secular determinant. In energy band calculations by this method, the main part of the computation is in the evaluation of the structure constants. To get the detailed structure of the bands, particularly the d or f bands, one must have a very large number of $E$ and $\boldsymbol{k}$ values. That is to say, we have to calculate the structure constants with a very fine grid of $E$ and $\boldsymbol{k}$ values. Even by using the simplified method [8], one needs long computing time to get these many structure constants. However, it will save a lot of computation if we calculate the $E(\boldsymbol{k})$ values by this method only at several high symmetry points in the Brillouin zone. We shall let the intermediate $E(\boldsymbol{k})$ values be determined by the interpolation scheme of the Slater-Koster method [3,4].

In the SK method, the matrix elements of the Hamiltonian $H$ between Bloch states can be written as

$$
\begin{aligned}
\left\langle\Psi_{n}|H| \Psi_{m}\right\rangle= & \sum_{\boldsymbol{R}_{j}} \exp \mathrm{i} \boldsymbol{k} \cdot\left(\boldsymbol{R}_{j}-\boldsymbol{R}_{i}\right) \int \Phi_{n}^{*}\left(\boldsymbol{r}-\boldsymbol{R}_{i}\right) \\
& \times H \Phi_{m}\left(\boldsymbol{r}-\boldsymbol{R}_{j}\right) \mathrm{d} \tau,
\end{aligned}
\tag{3}
$$

where the $\boldsymbol{R}$'s are the vector positions of the atoms and the $\Phi$'s are the atomic orbitals. The integrals in the above equation, called energy integrals or SK parameters, can be determined empirically by experimental data or fitting with accurate calculations, and the coefficients of the integrals for different type of crystal structures are dependent only the $\boldsymbol{k}$ values.

For simple cubic crystals, the interactions of s electrons on nearest neighbors can be expressed as

$$
\begin{aligned}
(\mathrm{s} / \mathrm{s})= & E_{\mathrm{s}, \mathrm{s}}(000)+2 E_{\mathrm{s}, \mathrm{s}}(100) \\
& \times(\cos \xi+\cos \eta+\cos \zeta)+4 E_{\mathrm{s}, \mathrm{s}}(110) \\
& \times(\cos \xi \cos \eta+\cos \xi \cos \zeta+\cos \eta \cos \zeta) \\
& +8 E_{\mathrm{s}, \mathrm{s}}(111) \cos \xi \cos \eta \cos \zeta,
\end{aligned}
\tag{4}
$$

where $\xi=a k_{x}, \eta=a k_{y}, \zeta=a k_{z}$, and $E_{n, m}(p, q, t)$ $=\int \Psi_{n}^{*}(\boldsymbol{r}) H \Psi_{m}(\boldsymbol{r}-p a \boldsymbol{i}-q a \boldsymbol{j}-t a \boldsymbol{k}) \mathrm{d} \tau$ are the energy integrals between Bloch sums of symmetry types $n$ and $m$, and the atoms are located at position $p a \boldsymbol{i}+q a \boldsymbol{j}+t a \boldsymbol{k}$ with $p, q, t$ being integers. The basic formula for the interactions between s, p, d and higher momentum orbitals have been constructed and tabulated in refs. [3,4] for simple cubic, fcc, bcc and diamond structures. SK fittings to APW calculations for CsCl-structured transition-metal alloys have been done before [9,10], and the energy integrals in terms of s, p, and d orbitals are tabulated there. The SK parameters as well as the energy bands and the density of states for 53 elements are given in ref. [11].

For CsCl-type structure, if only the nearest neighbors are counted, and the calculated $\Gamma$ values are involved in each fitting band, then the only matrix components of energy that remained nonzero in this case are (s/s), (x/x), (xy/xy), $(3 z^{2}-r^{2})$ abbreviated as $(d_{2}/d_{2})$, (xyz/xyz), and $(z(x^{2}-y^{2})/z(x^{2}-y^{2}))$ abbreviated as $(f_{4}/f_{4})$. The detailed forms of the first four are given in table 2 of [3]. The last two represent the f-f interactions, the explicit forms of which can be found in ref. [4]. Under the conditions mentioned above, only the parameters $E_{nm}(000)$ and $E_{nm}(111)$ are left in each formula. All terms containing $\sin \xi, \sin \eta, \sin \zeta$ are out. For instance

$$
(\mathrm{s} / \mathrm{s})=E_{\mathrm{s}, \mathrm{s}}(000)+8 E_{\mathrm{s}, \mathrm{s}}(111) \cos \xi \cos \eta \cos \zeta,
\tag{5a}
$$

$$
\begin{aligned}
\left(\mathrm{d}_{2} / \mathrm{d}_{2}\right)= & E_{\mathrm{d}_{2}, \mathrm{~d}_{2}}(000) \\
& +8 E_{\mathrm{d}_{2}, \mathrm{~d}_{2}}(111) \cos \xi \cos \eta \cos \zeta, \\
& (5 \mathrm{~b})
\end{aligned}
$$

$$
\begin{aligned}
(x y z / x y z)= & E_{x y z, x y z}(000) \\
& +8 E_{x y z, x y z}(111) \cos \xi \cos \eta \cos \zeta. \\
& (5 \mathrm{c})
\end{aligned}
$$

All the other interactions mentioned above have similar forms as eqs. (5). The energy values at $\Gamma$, $\mathrm{R}, \mathrm{X}$, and $\mathrm{M}$ can be written as

$$E\left(\Gamma_{1}\right)=E_{\mathrm{s}, \mathrm{s}}(000)+8 E_{\mathrm{s}, \mathrm{s}}(111),\qquad(6a)$$

$$E\left(\Gamma_{15}\right)=E_{x, x}(000)+8 E_{x, x}(111),\qquad(6b)$$

$$E\left(\Gamma_{25^{\prime}}\right)=E_{x y, x y}(000)+8 E_{x y, x y}(111),\qquad(6c)$$

$$E\left(\Gamma_{12}\right)=E_{d_{2}, d_{2}}(000)+8 E_{d_{2}, d_{2}}(111),\qquad(6d)$$

$$E\left(\Gamma_{2^{\prime}}\right)=E_{x y z, x y z}(000)+8 E_{x y z, x y z}(111),\qquad(6e)$$

$$E\left(\Gamma_{25}\right)=E_{\mathrm{f}_{4}, \mathrm{f}_{4}}(000)+8 E_{\mathrm{f}_{4}, \mathrm{f}_{4}}(111),\qquad(6f)$$

and

$$E\left(\mathrm{X}_{1}\right)=E_{\mathrm{s}, \mathrm{s}}(000)-8 E_{\mathrm{s}, \mathrm{s}}(111),\qquad(7a)$$

$$E\left(\mathrm{X}_{4^{\prime}}\right)=E_{x, x}(000)-8 E_{x, x}(111),\qquad(7b)$$

$$E\left(\mathrm{X}_{5}\right)=E_{x y, x y}(000)-8 E_{x y, x y}(111),\qquad(7c)$$

$$E\left(\mathrm{X}_{2^{\prime}}\right)=E_{x y z, x y z}(000)-8 E_{x y z, x y z}(111),\qquad(7d)$$

$$E\left(\mathrm{X}_{3^{\prime}}\right)=E_{\mathrm{f}_{4}, \mathrm{f}_{4}}(000)-8 E_{\mathrm{f}_{4}, \mathrm{f}_{4}}(111).\qquad(7e)$$

The formulae relating the energy values of $\mathrm{R}$ states with the SK parameters are the same as eqs. (6) except that the plus sign in each formula should be changed to a minus sign. And the same relations hold for $\mathrm{M}$ and $\mathrm{X}$ states. The energy values on the left-hand side of eqs. (6) and (7) are calculated by the KKR method. Then the parameters $E_{\mathrm{s}, \mathrm{s}}$ etc. can be solved. The total number of parameters in this case is 12 . The parameters that couple the different orbitals cannot be determined from these first-neighbor linear relations. More parameters can be deter- mined if second-nearest and farther neighbors are taken into account, and more calculated energy values are available. Of course the results will be more accurate, but the computation will be much more lengthy and complicated.

After these parameters are solved, we vary $k$ continuously. Then through the variation of $\xi, \eta$ and $\zeta$, we can get the continuously varying $E(k)$ values. The real interactions are definitely more complicated than what can be described by this approximation. Nevertheless, since we are here trying to see whether such a readily applicable method can exhibit the general features of the bands, this should be a reasonably good approxi- mation. In other words, what we claim here is not high accuracy but quick applications.

The potential in this work is assumed to be of the muffin-tin type, i.e. one which is spherically symmetric within nonoverlapping spheres with centers at the atomic sites and constant outside. The spherically symmetric potential around the atoms are obtained by using the Hartree-Fock atomic potentials as tabulated in Herman and Skillman's book [12] except the exchange poten- tial for which we adopt the Kohn-Sham-Gaspar type [13] instead of the Slater type. Then we use Matheiss' method [14] to add the effect of neigh- boring atoms to the spherically symmetric poten- tial about the atoms. The muffin-tin radii are so chosen that at the surface of the spheres, the difference between the spherical potentials and the average potential at this position is smallest [15], and of course the sum of the radii about neighboring atomic sites must be less than and almost equal to the nearest-neighbor distance.

### 3. Results

According to the method described briefly in the last paragraph, we construct the spherically symmetric potentials around the $\mathrm{Ce}$ and $\mathrm{Ag}$ sites. The potentials at the surface of the muffin- tin spheres are respectively $V_{\mathrm{Ce}}=-0.6684 \mathrm{Ry}$ and $V_{\mathrm{Ag}}=-0.7032 \mathrm{Ry}$. The muffin-tin radii are found to be $r_{\mathrm{Ce}}=3.490 a_{0}$ and $r_{\mathrm{Ag}}=2.645 a_{0}$. Then by the standard KKR method, we evaluate the eigenvalues at $\Gamma, \mathrm{X}, \mathrm{M}$ and $\mathrm{R}$, which are shown as the end points of the bands in fig. 1.

![](./images/812446212513857536_1.jpg)

Fig. 1. Energy bands of CeAg.

These values are then substituted into the interaction energy formula, i.e. eqs. (6) and (7), to determine the SK parameters for various bands. The SK parameters so obtained are shown in table I. The rms errors range from $1.5 \times 10^{-3}$ Ry for the 6th band to 0.5231 Ry for the 12th band. After the SK parameters are determined, we vary the $k$ values, i.e. the $\xi$, $\eta$ and $\zeta$ values in equations like eqs. (5) to get the continuous bands. The bands so obtained along the three principal directions for CeAg with Ce in the configuration $4f^{1}5d^{1}6s^{2}$ are shown in fig. 1. The density of states is shown in fig. 2. If more detailed structure of the bands is needed we may calculate the energy values $E(k)$ for one or more $\Delta$, $\Sigma$, and $\Lambda$ points along the three principal directions and consider interactions between farther neighbors to get more SK parameters, and better fitting.

One can see in fig. 1 that there is a very narrow f-band of about 0.03 Ry (~0.4 eV) mixed with some s and d states, and the total width of the mixed band is approximately 0.11 Ry (~1.5 eV). This indicates a weak hybridization effect which makes the 4f electrons of cerium more itinerant than that represented by the very narrow band width. This seems to be able to explain, at least qualitatively, the small magnetic moment $(0.95 \mu_{B})$ of CeAg [16]. The Fermi level is found to be at the bottom of the narrow f-band. From the value of the density of states at the Fermi level we find the specific heat coefficient $\gamma$ to be about $51 ~mJ / mol K^{2}$ by the relation ship $\gamma=(\pi / 3) k_{B}^{2} N(k_{F})$. Comparing with the $\gamma$-values of other materials, this is much larger than that of the ordinary metals (e.g 0.6 mJ/ mol $K^{2}$ for Ag), and much smaller than that of the well known heavy fermion compounds (e.g. $450 ~mJ / mol K^{2}$ for $UPt_{3}$ or $1600 ~mJ / mol K^{2}$ for $CeAl_{3}$ ) [17]. However the term "heavy fermion"

<table>
<caption>Table I<br>Slater-Koster parameters for CeAg in Ry with $d_{z}$ standing for $3z^{2}-r^{2}$ and $f_{4}$ for $z(x^{2}-y^{2})$</caption>
<tbody>
<tr>
<td>$E_{s,s}(000)$</td>
<td>0.1267</td>
<td>$E_{s,s}(111)$</td>
<td>$-0.0111$</td>
</tr>
<tr>
<td>$E_{x,x}(000)$</td>
<td>0.4532</td>
<td>$E_{x,x}(111)$</td>
<td>0.0150</td>
</tr>
<tr>
<td>$E_{xy,xy}(000)$</td>
<td>$-0.0934$</td>
<td>$E_{xy,xy}(111)$</td>
<td>0.0003</td>
</tr>
<tr>
<td>$E_{d_{z},d_{z}}(000)$</td>
<td>0.2941</td>
<td>$E_{d_{z},d_{z}}(111)$</td>
<td>0.0037</td>
</tr>
<tr>
<td>$E_{xyz,xyz}(000)$</td>
<td>$-0.2831$</td>
<td>$E_{xyz,xyz}(111)$</td>
<td>$-0.0009$</td>
</tr>
<tr>
<td>$E_{f_{4},f_{4}}(000)$</td>
<td>$-0.3320$</td>
<td>$E_{f_{4},f_{4}}(111)$</td>
<td>0.0039</td>
</tr>
</tbody>
</table>

![](./images/812446212513857536_2.jpg)

Fig. 2. Density of states of CeAg.

has also been used to describe systems with $\gamma$-values comparable to the present result (e.g. $75\ \text{mJ/mol}\ \text{K}^2$ for $\text{U}_2\text{PtC}_2$ [18] and $24\ \text{mJ/mol}\ \text{K}^2$ for $\text{U}_6\text{Fe}$ [19]). Hence we may also call CeAg a heavy fermion compound. Besides the Ce con- figuration mentioned above i.e. $4\text{f}^15\text{d}^16\text{s}^2$, we also made a set of calculations using another configuration of Ce i.e. $4\text{f}^25\text{d}^06\text{s}^2$. The results from the two sets of calculations are almost identical except a very slight shift which does not change the relative position nor the shape of the bands. This result may tell that CeAg has also some valence fluctuation. A crude estimate of the effective number of f electrons is 1.15 by considering the critical band width to be approxi- mately $0.4\ \text{eV}$ [20]. Few experimental data on the electronic properties of CeAg are available to make detailed comparison with. However we may say that such a simple combination of KKR and SK methods could give a readily applicable band structure of CeAg, which reveals most of the important electronic features of the cerium compound.

### References

[1] J. Korringa, Physica 13 (1947) 392.

[2] W. Kohn and N. Rostoker, Phys. Rev. 94 (1954) 1111.

[3] J.C. Slater and G.F. Koster, Phys. Rev. 94 (1954) 1498.

[4] R.R. Sharma, Phys. Rev. B 19 (1979) 2813.

[5] H. Ushizaka, S. Murayama, Y. Miyako and Y. Tazuke, J. Phys. Soc. Japan 53 (1984) 1136.

[6] G.W. Crabtree, J. Mag. Mat. 52 (1983) 169.

[7] B. Segall and F.S. Ham, Methods in Computational Physics, Vol 8, B. Adler, S. Fernbach and M. Roten- berg, eds. (Academic Press, New York, 1968).

[8] B. Segall and T.W. Yang, Phys. Rev. B 21 (1980) 3737.

[9] R. Bruinsma, Phys. Rev. B 25 (1982) 2951.

[10] J.D. Shore and D.A. Papaconstantopoulos, J. Phys. Chem. Solids 45 (1984) 439.

[11] D.A. Papaconstantopoulos, Handbook of the Band Structures of Elements (Plenum, New York, 1986).

[12] F. Herman and S. Skillman, Atomic Structure Calcula- tions, Prentice-Hall, Englewood Cliffs, NY, 1963).

[13] W. Kohn and L.J. Sham, Phys. Rev. 140 (1965) 1133.

[14] L.F. Mattheiss, Phys. Rev. 133 (1964) 1399.

[15] S. Rao, K. Majumdar and P. Singh, Phys. Rev. B 19 (1979) 6274.

[16] G. Schneider, Handbook on the Physics and Chemistry of Rare Earths (North-Holland, Amsterdam, 1978).

[17] G.R. Stewart, Rev. Mod. Phys. 56 (1984) 755.

[18] G.P. Meisner, A.L. Giorgi, A.C. Lawson, G.R. Stewart, J.O. Willis, M.S. Wise and J.L. Smith, Phys. Rev. Lett. 53 (1984) 1829.

[19] L.E. Delong, J.G. Huber, K.N. Yang and M.B. Maple, Phys. Rev. Lett. 51 (1983) 312.

[20] W.A. Harrison, Phys. Rev. B 29 (1984) 2917.