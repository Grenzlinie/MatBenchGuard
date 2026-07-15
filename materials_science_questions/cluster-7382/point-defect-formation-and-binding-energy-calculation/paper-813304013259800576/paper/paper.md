# Range-Separated Approach to the RPA Correlation Applied to the van der Waals Bond and to Diffusion of Defects

Fabien Bruneval

CEA, DEN, Service de Recherches de Métallurgie Physique, F-91191 Gif-sur-Yvette, France
(Received 1 February 2012; published 19 June 2012)

The random-phase approximation (RPA) is a promising approximation to the exchange-correlation energy of density functional theory, since it contains the van der Waals (vdW) interaction and yields a potential with the correct band gap. However, its calculation is computationally very demanding. We apply a range-separation concept to RPA and demonstrate how it drastically speeds up the calculations without loss of accuracy. The scheme is then successfully applied to a layered system subjected to weak vdW attraction and is used to address the controversy of the self-diffusion in silicon. We calculate the formation and migration energies of self-interstitials and vacancies taking into account atomic relaxations. The obtained activation energies deviate significantly from the earlier calculations and challenge some of the experimental interpretations: the diffusion of vacancies and interstitials has almost the same activation energy.

DOI: 10.1103/PhysRevLett.108.256403
PACS numbers: 71.15.-m, 61.72.Bb, 61.72.uf

The quest for the exact exchange-correlation energy of density functional theory (DFT) is endless of course. However, the random-phase approximation (RPA) [1,2] is now believed to be a huge step forward. It is now common- place to cite the RPA as *the* first-principles method that correctly describes the weak van der Waals (vdW) inter- action [3], which is prominent for many important prob- lems: physisorption [4–6] and layered system binding [7,8], for instance. A much less known feature of RPA is the correct prediction of band gaps, as opposed to the large underestimation of the local and semilocal approximation to DFT. It has been demonstrated recently [9] that the exchange-correlation potential obtained from RPA closely resembles the $GW$ approximation [10], which is nowadays the most robust method to predict band gap of solids.

The correctness of the band gaps would make RPA a method of choice for the properties of defects in semi- conductors and insulators. The underestimation of the band gap in the calculations is known to be the reason why the usual local and semilocal approximations fail for defects in semiconductors [11,12]. Whereas the calculation of the energetic of point defects relies on total energies only, a poor description of the band structure will still affect the final formation energies.

An approach with no band gap problem should be able to clarify the experimental controversy about the self- diffusion in silicon. Although silicon can be regarded as the best characterized material ever and although the self- diffusion is a key parameter for industrial processes, there is still no unanimous interpretation for this phenomenon for silicon [13–20]. Self-diffusion in solids is governed by the formation and the migration of point defects, namely, vacancies and self-interstitials.

For the above mentioned reasons, RPA is a very appeal- ing framework. However, its application has been limited so far to simple systems cases, because of its numerical intricacies. Its convergence behavior is so bad that most groups had to employ extrapolation techniques [7,21,22] to infer the converged properties out of a few underconverged calculations. Furthermore, the scaling with system size is dramatically high and the application to point defects in supercells would be out of reach.

In this Letter, we introduce a range-separated framework for the calculation of the RPA correlation energy. The short-range (SR) part is to be approximated with a local density approximation (LDA), whereas the long-range (LR) part is to be calculated exactly. This approach speeds up the calculations with a controlled loss of accuracy. We demonstrate its robustness calculating a wide variety of covalent crystals and a vdW bonded system, namely, hex- agonal boron nitride. Within this approach, the system size required for an accurate description of point defects is made accessible. We apply the method to the calculation of the self-diffusion in silicon and show that the commonly used *ab initio* values need to be drastically revised.

A RPA calculation relies on the calculation of the elec- tronic polarizability. The convergence of the RPA energy is surprisingly slow against both the basis representation of the polarizability and the number of empty states that should be included in the sum-over-state formula [21,23]. We propose to overcome this situation thanks to the range- separation idea. Following Toulouse and co-workers [24,25], the Coulomb interaction $v$ can be split into SR and LR components:

$$
v(r)=\frac{1-\operatorname{erf}\left(r / r_{c}\right)}{r}+\frac{\operatorname{erf}\left(r / r_{c}\right)}{r}, \tag{1}
$$

where $r_{c}$ is a cutoff radius (Hartree atomic units are em- ployed throughout the Letter).


At variance with Toulouse and co-workers, the purpose of the splitting is not to fix some SR deficiencies of the RPA, but simply to accelerate the convergence of the RPA energies. We intend to benefit from the fast decay of the LR part of the Coulomb interaction in Fourier space $4\pi/q^{2}\exp[-(r_{c}q)^{2}/4]$. In comparison, the bare Coulomb interaction does not contain the exponential term.

A LDA evaluation of the RPA energy [26] noticeably overestimates the computed RPA energy. It is sensible to anticipate that the LDA is a reliable approximation for the SR part of RPA but not for the LR. Hence, we propose to evaluate the total RPA correlation energy as follows:

$$
\begin{aligned}
E_{c}^{\mathrm{RPA}}= & \int d \mathbf{r} \epsilon_{c}^{\mathrm{RPA}, \mathrm{jellium}}[n(\mathbf{r})] n(\mathbf{r}) \\
& -\int d \mathbf{r} \epsilon_{c}^{\mathrm{LR}-\mathrm{RPA}, \mathrm{jellium}}[n(\mathbf{r}), r_{c}] n(\mathbf{r}) \\
& +E_{c}^{\mathrm{LR}-\mathrm{RPA}, \mathrm{calc}}\left(r_{c}\right),
\end{aligned}
\tag{2}
$$

where $n(\mathbf{r})$ is the electronic density, $\epsilon_{c}^{\mathrm{RPA},\mathrm{jellium}}$ is the RPA correlation energy density of the jellium subjected to the bare Coulomb interaction, $\epsilon_{c}^{\mathrm{LR-RPA,jellium}}$ is the RPA correlation energy density of the jellium with the LR-only interaction, and finally $E_{c}^{\mathrm{LR-RPA,calc}}$ is the calculated RPA correlation energy with the same LR-only interaction. The expression for the LR-RPA correlation energy can be easily derived from the usual expression of the RPA energy (see, e.g., Ref. [22]). The modified interaction is governed by the cutoff radius $r_{c}$, which plays the role of a convergence parameter in our scheme. Indeed, if $r_{c}$ is set to 0, the LR interaction turns out to be the full interaction and we recover the usual expression for the RPA correlation energy. If $r_{c}$ is set to $\infty$, the LR interaction vanishes and the scheme turns out to be equal to the usual LDA evaluation to the RPA correlation energy.

In order to implement Eq. (2) in solid state calculations, an explicit expression for the LR-RPA correlation energy density of jellium had to be establish. We numerically evaluated the RPA integrals in jellium [27] using either the Coulomb interaction or the LR interaction for different $r_{c}$ values. The calculated energies were then interpolated with a Padé approximant [28]. Figure 1 shows the behavior of the computed RPA energies based on LDA wave functions and energies as a function of the cutoff of the modified interaction. As the correlation energy is not linear with respect to the interaction, the SR contribution is defined as the difference between the total correlation and the LR-only correlation. First of all, our RPA correlation energy for the full interaction is in very good agreement with previously published values: 6.12 eV/atom to be compared to 6.11 eV/atom from Ref. [29]. The discrepancy between the LDA evaluation of the RPA correlation energy and the computed one arises mainly from the LR part: the LDA evaluation of the SR contribution nicely reproduces the explicit calculation for radius as large as $r_{c}=4$ bohr.

![](./images/813304013259800576_1.jpg)

FIG. 1 (color online). LR-RPA (filled symbols) and SR-RPA (open symbols) correlation energies of bulk silicon for lattice constant $a=10.26$ bohr, as a function of the cutoff radius $r_{c}=1/\omega$. The SR-RPA correlation energy is obtained as the RPA correlation energy minus the LR-RPA correlation energy. The explicit calculation is displayed with squares and LDA with circles. The total correlation is displayed with crosses. The horizontal line emphasizes the calculated RPA correlation energies with full Coulomb interaction. Each point is associated with the corresponding convergence parameters necessary to achieve a 2 meV/atom accuracy: first, the cutoff energy for the polarizability (Ha), and second, the number of states to be included in the expression of the polarizability.

This observation confirms the assumption we made in Eq. (2) when approximating the total RPA correlation energy. The approximated total correlation energy (cross symbols) closely follows the full calculation shown with the horizontal line.

Figure 1 also shows the convergence parameters for the different values of $r_{c}$. The use of a LR-only interaction is very convenient for a plane-wave expansion. Firstly, the polarizabilities, which are required for a RPA calculation, are two point functions and therefore their calculation is massively accelerated when lowering in the plane-wave cutoff energy. Secondly, the number of empty states required to achieve convergence is largely reduced, since the exponential decay in the LR-only interaction in Fourier space drastically decreases the coupling between the occupied states and the high energy empty states.

For practical applications, one has to determine the largest radius $r_{c}$ that still captures the desired physical effects. The cutoff radius has to be considered as a convergence parameter. In order to appreciate the relevant range for $r_{c}$, Table I shows the atomization energy of selected crystals. The list includes a metal, narrow and wide band gap semiconductors, zinc blende and wurzite semiconductors. The atomization energy can be considered as a difficult test for the range-separation technique, since it compares solids to atoms, which have noticeably

<table><caption>TABLE I. Atomization energy or binding energy of a selection of crystals in eV per atom. RPA evaluation is given with our range-separated scheme using different values of $r_c$ and with the standard expression as a reference.</caption>
<thead>
  <tr>
    <th rowspan="2">Crystal</th>
    <th rowspan="2">PBE</th>
    <th colspan="3">RPA with $r_c$</th>
    <th rowspan="2">RPA</th>
    <th rowspan="2">Expt.</th>
  </tr>
  <tr>
    <th>2.0</th>
    <th>1.0</th>
    <th>0.5</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Al</td>
    <td>3.56</td>
    <td>3.45</td>
    <td>3.53</td>
    <td>3.50</td>
    <td>3.44</td>
    <td>3.39</td>
  </tr>
  <tr>
    <td>Si</td>
    <td>4.63</td>
    <td>4.56</td>
    <td>4.60</td>
    <td>4.64</td>
    <td>4.63</td>
    <td>4.62</td>
  </tr>
  <tr>
    <td>$\beta$-SiC</td>
    <td>6.49</td>
    <td>6.01</td>
    <td>6.08</td>
    <td>6.11</td>
    <td>6.12</td>
    <td>6.34</td>
  </tr>
  <tr>
    <td>Diamond</td>
    <td>7.82</td>
    <td>7.11</td>
    <td>7.27</td>
    <td>7.34</td>
    <td>7.27</td>
    <td>7.37</td>
  </tr>
  <tr>
    <td>$w$-AlN</td>
    <td>6.54</td>
    <td>4.96</td>
    <td>4.92</td>
    <td>5.52</td>
    <td>5.65</td>
    <td>5.83</td>
  </tr>
  <tr>
    <td>$c$-BN</td>
    <td>7.80</td>
    <td>5.90</td>
    <td>5.84</td>
    <td>6.29</td>
    <td>6.28</td>
    <td>6.68</td>
  </tr>
</tbody>
</table>

different spatial extension. If we compare the range-separated RPA to the standard RPA, we conclude that $r_c = 0.5$ bohr yield converged results. When dealing with larger atoms, not in the first row of the periodic table, a larger value for $r_c$ can be safely retained. The overall agreement of RPA with respect to experiment is very good.

The proposed range-separated technique is highly relevant for vdW bonded system. Indeed, our scheme should automatically describe the covalent bond with the LDA quality and the distant vdW bonds with the RPA precision. This statement is exemplified in Fig. 2 with the interlayer spacing of hexagonal boron nitride. In this system, LDA is correct thanks to a fortunate compensation of errors and PBE [30] largely overestimates the interlayer spacing. Genuine RPA is known to be excellent for $h$-BN [7] and clearly superior to the modelized vdW-DF approach [31]. Whereas $r_c = 4$ bohr is definitely too large; the range separation using $r_c = 1$ or 2 bohr is sufficient to yield the correct interlayer spacing and the correct elastic constant $C_{33}$.

![](./images/813304013259800576_2.jpg)

FIG. 2 (color online). Energy as a function of the interlayer spacing $d = c/2$ of hexagonal BN within LDA (dashed line), PBE (solid line), RPA with $r_c = 4$, 2, or 1 (respectively, circles, squares, or diamonds). The equilibrium spacing $d_0$ and elastic constant $C_{33}$ are shown and compared to the modelized method vdW DF [31] and to experiment [41,42].

We now turn to the large supercells necessary to predict self-diffusion of silicon. The RPA potential yields a good evaluation of the band gap (1.30 eV to be compared to the experimental value of 1.17 eV) and therefore the energetics of point defects in silicon should be strongly corrected with respect to the LDA or PBE values. For completeness, we also performed hybrid functional calculations within HSE06 [32] and PBE0 [33]. For instance, HSE06 yields a nice band gap of 1.20 eV for silicon.

The defect calculations are performed within 16, 64, and 216 atom cubic supercells. Care was taken about the $\mathbf{k}$-point convergence for RPA ($2 \times 2 \times 2$ grid) and for the exact exchange ($4 \times 4 \times 4$ grid) [29]. The validity of a cutoff radius $r_c = 1.0$ bohr was checked against a smaller radius of $r_c = 0.5$ eV. The number of empty states was then further reduced using an acceleration scheme [34].

The RPA scheme does not provide the forces easily. Thanks to the similarity between the elastic constant of LDA and RPA, we manually relaxed the few degrees of freedom directly involved in the defect structure, and the other ones were relaxed within LDA. This procedure yields basically negligible energetical changes except for the vacancy that experiences a large Jahn-Teller distortion as exemplified in Fig. 3. In contrast with LDA, RPA massively favors the Jahn-Teller configuration against the tetrahedric environment (0.7 eV gain within RPA, almost 0 eV within LDA).

The formation and migration energies relevant for the self-diffusion through neutral defects are summarized in Table II. HSE06 and RPA show very similar trends, even

![](./images/813304013259800576_3.jpg)

FIG. 3 (color online). Silicon vacancy $V_{\text{Si}}$ formation energy in a 63-atom supercell as a function of the nearest neighbor atom distances. In the left-hand panel, the longest distance $r_{\text{long}}$ is fixed and the shortest one $r_{\text{short}}$ is varied. In the right-hand panel, $r_{\text{long}}$ is fixed and $r_{\text{short}}$ is varied. The absence of Jahn-Teller distortion corresponds to $r_{\text{long}} = r_{\text{short}}$. The atomic configuration is displayed in the inset: The cube stands in the empty lattice site.

<table><caption>TABLE II. Formation energies and migration barriers in eV of the self-interstitial and vacancy in silicon within different ab initio schemes for different supercell sizes. The results for HSE06 [32] and for PBE0 [33] are given for comparison. The QMC value is taken from Ref. [35].</caption>
<tbody><tr><th></th><th>LDA</th><th>PBE</th><th>HSE06</th><th>PBE0</th><th>RPA</th><th>QMC</th></tr>
<tr><td colspan="7">16-atom supercell</td></tr>
<tr><td>Si<sub>split⟨110⟩</sub></td><td>3.45</td><td>3.65</td><td>4.50</td><td>4.61</td><td>5.06</td><td>4.94</td></tr>
<tr><td colspan="7">64-atom supercell</td></tr>
<tr><td>Si<sub>split⟨110⟩</sub></td><td>3.45</td><td>3.62</td><td>4.40</td><td>4.50</td><td>4.49</td><td></td></tr>
<tr><td>Si<sub>hex</sub></td><td>3.48</td><td>3.67</td><td>4.52</td><td>4.63</td><td>4.74</td><td></td></tr>
<tr><td>Si<sub>split⟨110⟩</sub> → Si<sub>hex</sub></td><td>0.37</td><td>0.40</td><td>0.47</td><td>0.49</td><td>0.77</td><td></td></tr>
<tr><td>Si<sub>hex</sub> → Si<sub>hex</sub></td><td>0.12</td><td>0.21</td><td>0.49</td><td>0.69</td><td>1.01</td><td></td></tr>
<tr><td>V<sub>Si</sub></td><td>3.66</td><td>3.71</td><td>4.56</td><td>4.64</td><td>4.24</td><td></td></tr>
<tr><td>V<sub>Si</sub> → V<sub>Si</sub></td><td>0.40</td><td>0.28</td><td>0.40</td><td>0.58</td><td>0.83</td><td></td></tr>
<tr><td colspan="7">216-atom supercell</td></tr>
<tr><td>V<sub>Si</sub></td><td>3.58</td><td>3.72</td><td></td><td></td><td>4.33</td><td></td></tr>
</tbody></table>

though the energetics can differ in the details. We present the small 16-atom supercell in order to allow comparison with earlier quantum Monte Carlo (QMC) calculations [35,36]. RPA seems to nicely approximate the high level QMC method. However, our results show that the 16 atom supercell is too small to achieve convergence, mainly because of the long-ranged exchange interaction.

Generally speaking, the energy of all the defects is underestimated by 0.7–1.0 eV by LDA and PBE compared to HSE06 or RPA. The RPA formation energy compares favorably with earlier $GW$ calculations [37]. The migration barriers are also underestimated with LDA and PBE. Noticeably, the migration of self-interstitial in the hexagonal sites Si<sub>hex</sub> had a very low barrier (0.12 eV for LDA) and, as a consequence, was the preferred mechanism for self-interstitial migration for both LDA and PBE. When turning to RPA (and HSE06), this diffusion path is completely ruled out against the following two-step path: Si<sub>split⟨110⟩</sub> → Si<sub>hex</sub> → Si<sub>split⟨110⟩</sub>. The corresponding diffusion activation energy (formation + barrier) is 4.87 eV within HSE06 and 5.26 eV within RPA. These values lie in the range of the experimental values 4.95 eV [38] and 5.15 eV [39], obtained from the self-interstitial assisted diffusion of zinc in silicon.

Concerning the vacancy diffusion, the situation is even more debated. The positron annihilation spectroscopy is not conclusive [13,14] and the diffusion measurements have difficulties isolating the vacancy contribution [15–20]. In calculations, the vacancy is known to converge slowly with system size [40]. We therefore performed a 216-atom supercell calculation to ensure a 0.1 eV convergence as shown in Table II. The vacancy diffusion activation energy within RPA 5.16 eV and HSE06 4.96 eV are much higher than the corresponding LDA estimate 4.06 eV. We confirm the warnings raised recently by some authors [18]: the agreement between theory at the LDA level and experiment seems to be completely fictitious. The diffusion activation energy of interstitials and of vacancies is almost the same: this piece of information is much of a surprise.

In conclusion, we demonstrated in this Letter the practical advantages of range separation when applied to RPA. The SR is approximated within LDA and the LR part is calculated exactly. This procedure is perfectly suited to Fourier space approaches. The efficiency gain without accuracy loss is so substantial that the application to the properties of point defects becomes accessible using supercells as large as 216 atoms. RPA is a relevant trade-off between the fast but not reliable LDA and the slow but accurate QMC calculations. The described scheme allowed us to produce an estimate for the activation energies of self-diffusion in silicon. Our energies, which significantly deviate from the corresponding LDA or PBE values, are in good agreement with respect to experiment for interstitials. The diffusion path of interstitials is identified as a transformation between two different configurations Si<sub>split⟨110⟩</sub> and Si<sub>hex</sub>. Surprisingly, the vacancy and the interstitial activation energies are calculated to be very close.

We acknowledge insightful discussions with J.-P. Crocombette, G. Roma, and E. Clouet. The calculations presented here are performed with the plane-wave codes ABINIT [43] and QUANTUM-ESPRESSO [44]. This work was performed using HPC resources from GENCI-CINES and GENCI-CCRT (Grant No. 2012-gen6018).

[1] D. Bohm and D. Pines, Phys. Rev. 92, 609 (1953).
[2] D. C. Langreth and J. P. Perdew, Phys. Rev. B 15, 2884 (1977).
[3] J. F. Dobson and J. Wang, Phys. Rev. Lett. 82, 2123 (1999).
[4] X. Ren, P. Rinke, and M. Scheffler, Phys. Rev. B 80, 045402 (2009).
[5] L. Schimka, J. Harl, A. Stroppa, A. Grueneis, M. Marsman, F. Mittendorfer, and G. Kresse, Nature Mater. 9, 741 (2010).
[6] J. Ma, A. Michaelides, D. Alfe, L. Schimka, G. Kresse, and E. Wang, Phys. Rev. B 84, 033402 (2011).
[7] A. Marini, P. García-González, and A. Rubio, Phys. Rev. Lett. 96, 136404 (2006).
[8] S. Lebègue, J. Harl, T. Gould, J. G. Ángyán, G. Kresse, and J. F. Dobson, Phys. Rev. Lett. 105, 196401 (2010).
[9] Y.-M. Niquet and X. Gonze, Phys. Rev. B 70, 245115 (2004).
[10] L. Hedin, Phys. Rev. 139, A796 (1965).
[11] W. R. L. Lambrecht, Phys. Status Solidi B 248, 1547 (2011).
[12] M. Giantomassi, M. Stankovski, R. Shaltaf, M. Grning, F. Bruneval, P. Rinke, and G.-M. Rignanese, Phys. Status Solidi B 248, 275 (2011).
[13] S. Dannefaer, P. Mascher, and D. Kerr, Phys. Rev. Lett. 56, 2195 (1986).
[14] R. Würschum, W. Bauer, K. Maier, A. Seeger, and H.-E. Schaefer, J. Phys. Condens. Matter 1, SA33 (1989).

[15] H. Bracht, E. E. Haller, and R. Clark-Phelps, *Phys. Rev. Lett.* **81**, 393 (1998).

[16] A. Ural, P. B. Griffin, and J. D. Plummer, *Phys. Rev. Lett.* **83**, 3454 (1999).

[17] Y. Shimizu, M. Uematsu, and K. M. Itoh, *Phys. Rev. Lett.* **98**, 095901 (2007).

[18] H. Bracht and A. Chroneos, *J. Appl. Phys.* **104**, 076108 (2008).

[19] H. Bracht and E. E. Haller, *Phys. Rev. Lett.* **85**, 4835 (2000).

[20] A. Ural, P. B. Griffin, and J. D. Plummer, *Phys. Rev. Lett.* **85**, 4836 (2000).

[21] F. Furche, *Phys. Rev. B* **64**, 195120 (2001).

[22] J. Harl and G. Kresse, *Phys. Rev. B* **77**, 045136 (2008).

[23] M. Fuchs and X. Gonze, *Phys. Rev. B* **65**, 235109 (2002).

[24] J. Toulouse, F. Colonna, and A. Savin, *Phys. Rev. A* **70**, 062505 (2004).

[25] J. Toulouse, I. C. Gerber, G. Jansen, A. Savin, and J. G. Ángyán, *Phys. Rev. Lett.* **102**, 096404 (2009).

[26] S. Vosko, L. Wilk, and M. Nusair, *Can. J. Phys.* **58**, 1200 (1980).

[27] U. von Barth and L. Hedin, *J. Phys. C* **5**, 1629 (1972).

[28] S. Goedecker, M. Teter, and J. Hutter, *Phys. Rev. B* **54**, 1703 (1996).

[29] H.-V. Nguyen and S. de Gironcoli, *Phys. Rev. B* **79**, 205114 (2009).

[30] J. P. Perdew, K. Burke, and M. Ernzerhof, *Phys. Rev. Lett.* **77**, 3865 (1996).

[31] H. Rydberg, M. Dion, N. Jacobson, E. Schröder, P. Hyldgaard, S. I. Simak, D. C. Langreth, and B. I. Lundqvist, *Phys. Rev. Lett.* **91**, 126402 (2003).

[32] J. Heyd, G. E. Scuseria, and M. Ernzerhof, *J. Chem. Phys.* **124**, 219906 (2006).

[33] C. Adamo and V. Barone, *J. Chem. Phys.* **110**, 6158 (1999).

[34] F. Bruneval and X. Gonze, *Phys. Rev. B* **78**, 085125 (2008).

[35] E. R. Batista, J. Heyd, R. G. Hennig, B. P. Uberuaga, R. L. Martin, G. E. Scuseria, C. J. Umrigar, and J. W. Wilkins, *Phys. Rev. B* **74**, 121102 (2006).

[36] W.-K. Leung, R. J. Needs, G. Rajagopal, S. Itoh, and S. Ihara, *Phys. Rev. Lett.* **83**, 2351 (1999).

[37] P. Rinke, A. Janotti, M. Scheer, and C. G. Van de Walle, *Phys. Rev. Lett.* **102**, 026402 (2009).

[38] H. Bracht, N. A. Stolwijk, and H. Mehrer, *Phys. Rev. B* **52**, 16542 (1995).

[39] V. Voronkov and R. Falster, *Mater. Sci. Eng. B* **134**, 227 (2006).

[40] F. Corsetti and A. A. Mosto, *Phys. Rev. B* **84**, 035209 (2011).

[41] A. Bosak, J. Serrano, M. Krisch, K. Watanabe, T. Taniguchi, and H. Kanda, *Phys. Rev. B* **73**, 041402 (2006).

[42] J. Green, T. Bolland, and J. Bolland, *J. Chem. Phys.* **64**, 656 (1976).

[43] X. Gonze *et al.*, *Comput. Phys. Commun.* **180**, 2582 (2009).

[44] P. Giannozzi *et al.*, *J. Phys. Condens. Matter* **21**, 395502 (2009).

256403-5