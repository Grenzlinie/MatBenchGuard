# Electronic structure of $\text{CsBi}_4\text{Te}_6$: A high-performance thermoelectric at low temperatures

P. Larson and S. D. Mahanti
Department of Physics & Astronomy, Michigan State University, East Lansing, Michigan 48824

D.-Y. Chung and M. G. Kanatzidis
Department of Chemistry, Michigan State University, East Lansing, Michigan 48824

(Received 27 July 2001; published 3 January 2002)

Recently, a novel narrow-gap semiconductor $\text{CsBi}_4\text{Te}_6$ has been discovered with greater potential for low-temperature applications than the best existing high-performance thermoelectrics, $\text{Bi}_2\text{Te}_3$ and its alloys. Electronic structure calculations in this bulk system display reduced dimensionality of hole transport whose origin can be traced to the presence of Bi-Bi bonds (instead of Bi-Te and Te-Te bonds), unique for bismuth chalcogenide systems. This reduced dimensionality of charge transport along with the low thermal conductivity of this compound can explain the observed large thermoelectric figure of merit $ZT$ in hole doped $\text{CsBi}_4\text{Te}_6$.

DOI: 10.1103/PhysRevB.65.045205
PACS number(s): 72.15.Jf, 71.15.Ap, 71.15.Mb

## I. INTRODUCTION

In recent years, there has been renewed interest in discovering new materials with better room and low temperature thermoelectric (TE) characteristics¹ compared to the currently used narrow-gap semiconductor $\text{Bi}_2\text{Te}_3$ and its alloys. Since bulk materials are more easily amenable for fabrication in electronic circuitry and superconducting devices, classes of materials such as skutterudites,² half-Heusler alloys,³ clathrates,⁴ and pentatellurides⁵ are being studied both experimentally and theoretically for their potential thermoelectric properties. These systems are investigated for large carrier effective masses, high carrier mobility, large degeneracy of the conduction and valence band extrema, and low lattice thermal conductivity to enhance the thermoelectric figure of merit $ZT=\sigma S^2T/(\kappa_L+\kappa_e)$. (Here $\sigma$ is electrical conductivity, $\kappa_L$ and $\kappa_e$ are, respectively, the lattice and electronic contributions to thermal conductivity, $S$ is thermopower, and $T$ is temperature.) Based on a rather different idea, Hicks and Dresselhaus (HD) argued that systems displaying large anisotropy or reduced dimensionality (quantum confinement) in their charge transport can also exhibit a significant enhancement in their thermoelectric figure of merit.⁶ Mahan and Sofo also predicted that in good thermoelectric materials the energy distribution of carriers should be narrow and have a high carrier velocity in the direction of the applied field,⁷ which is possible in a highly anisotropic system. Consequently, nanofabrication of one- and two-dimensional arrays of materials have been attempted, and high values of $ZT$ have been reported in PbTe-PbSeTe quantum-dot superlattices by Harman et al.⁸ and in $p$-type $\text{Bi}_2\text{Te}_3/\text{Sb}_2\text{Te}_3$ superlattice films by Venkatasubramanian.⁹ The major reason governing the observed enhanced $ZT$ in these superlattice systems appears to be in their reduced thermal conductivity rather than an increase in the power factor $(\sigma S^2)$.

In contrast to the above superlattice systems, a new layered compound $\text{CsBi}_4\text{Te}_6$, has been recently discovered and it has a larger figure of merit ($ZT\sim0.8$ at 225 K) than conventional optimized $\text{Bi}_{2-x}\text{Sb}_x\text{Te}_{3-y}\text{Se}_y$ alloys at these temperatures ($ZT\sim0.6$).¹⁰ The thermal conductivities of these two materials are comparable, which suggests that the improved figure of merit for the former may be of electronic origin. In this paper we discuss the results of $ab$ initio electronic structure calculations in this rather complex material: We find a large anisotropy in the carrier effective masses, which can explain the large value of $ZT$ seen in the hole doped systems. Our electronic structure calculations suggest that the holes near the top of the valence band (responsible for thermoelectric properties of $p$-doped samples) move in quasi-two-dimensional layers which are separated by poorly conducting regions of about $13$ Å width. Surprisingly, the layers in which the charges are confined to move are almost perpendicular to the crystallographic layers formed by Bi-Te slabs separated by layers of Cs ions. This, as we will show, is due to the presence of Bi-Bi bonds which is unique for systems consisting of Bi/Te networks. Indeed, the novel quantum architecture of $\text{CsBi}_4\text{Te}_6$ provides the possibility of using a bulk material for fabrication while the reduced dimensionality of the charge transport enhances the thermoelectric properties.

## II. STRUCTURE AND METHOD OF CALCULATION

The unit cell of $\text{CsBi}_4\text{Te}_6$ is $c$-centered monoclinic (Space group: $C2/m$) with 88 atoms/unit cell. The lattice parameters are $A=97.425$ a.u., $B=8.264$ a.u., $C=27.424$ a.u., $\beta=101.438^\circ$, where a.u. is the atomic unit (1 Bohr).¹⁰ Figure 1 gives the crystal structure of $\text{CsBi}_4\text{Te}_6$ where the coordinates of all the 88 atoms have been projected onto the $ac$ plane. Also different atoms in the cell have been numbered for later reference. This compound has a layered anisotropic structure with anionic $[\text{Bi}_4\text{Te}_6]$ laths connected through Bi-Bi bridges to form two-dimensional slabs, and these Bi/Te slabs are separated by layers of $\text{Cs}^+$ ions. It should be noted that Bi-Bi bonds have not been found in chalcogenide compounds before. The axis of the laths (normal to the plane of the paper) is the direction of highest charge mobility and is usually referred to as the needle axis. There is a gross structural resemblance of this compound with $\text{Bi}_2\text{Te}_3$ and $\text{BaBiTe}_3$ where the Bi/Te slabs are separated by a Van der Waals gap and a $\text{Ba}^{++}$ ion layer respectively.¹¹ In the latter compound there is also a lath structure but the laths are con-

![](./images/812687490065367043_1.jpg)

FIG. 1. Monoclinic crystal structure of $CsBi_4Te_6$. Filled dark circles: Bi; open circles: Te; Filled light circles: Cs.

nected by Te-Te bonds. We will show later that the Bi-Bi (Bi7 and Bi8 atoms in Fig. 1) bonds in $CsBi_4Te_6$ are very important in understanding the anisotropy of the electronic structure and charge transport in this material.

As discussed above the unit cell is $c$-centered monoclinic and has 88 atoms/unit cell. Since the compound contains heavy atoms and has many more atoms per unit cell than the two compounds $Bi_2Te_3$ and $BaBiTe_3$ that we have studied before, the computation time is considerably more. To reduce the computation time we have chosen a smaller unit cell but with lower symmetry. The $c$-centered monoclinic unit cell is replaced by a triclinic unit cell (space group: $P-1$) with 44 atoms/unit cell. The unit vectors of the triclinic unit cell are $\mathbf{A}'=(\mathbf{A}-\mathbf{B})/2$, $\mathbf{B}'=(\mathbf{A}+\mathbf{B})/2$, $\mathbf{C}'=\mathbf{C}$, where $\mathbf{A},\mathbf{B},\mathbf{C}$ are the unit cell vectors of the monoclinic cell. The lattice parameters of the triclinic unit cell used in the present calculation are $A'=49.233$ a.u., $B'=49.233$ a.u., $C'=27.424$ a.u., $\alpha'=101.438^\circ$, $\beta'=101.438^\circ$, $\gamma'=9.693^\circ$. These values are slightly different from what would have been obtained by using the values of $A$, $B$, $C$, and the angle $\beta$ for the monoclinic structure reported earlier in Ref. 10. The Brillouin zone for the triclinic unit cell is given in Fig. 2.

Electronic structure calculations were performed using the full-potential linearized augmented plane wave (FLAPW) method$^{12}$ within density-functional theory (DFT)$^{13}$ using the generalized gradient approximation (GGA) of Perdew, Burke, and Ernzerhof$^{14}$ for exchange and correlation potential. The calculations were carried out with the WIEN97 package.$^{15}$ The muffin tin radii were taken to be the same for all the three types of atoms and were chosen to be 2.8 a.u. to minimize the regions between the atomic spheres. For the computation of the self-consistent charge density we used 13 $\mathbf{k}$ points in $\frac{1}{4}$ of the Brillouin zone. The number of plane waves used in the interstitial region is characterized by a parameter $RK_{\text{max}}=R_{mt}*K_{\text{max}}$, where $R_{mt}$ is the smallest muffin tin radius and $K_{\text{max}}$ is the maximum plane wave vector. Typically $RK_{\text{max}}$ is chosen between 7 to 9, and we have used a value of 8 in our calculation. The convergence in the total energy was found to be of the order of 0.0001 Ry. Scalar relativistic corrections were included in the calculation along with spin-orbit interactions which were included in a second variational procedure.$^{16}$ As has been noted in our previous electronic structure calculations in the related systems $Bi_2Te_3$ and $BaBiTe_3$, spin orbit interaction plays a significant role in determining the gap structure and should be included in any serious calculation of the electronic structure of Bi and Te containing compounds.$^{11,17}$

![](./images/812687490065367043_2.jpg)

FIG. 2. Brillouin zone of alternative triclinic representation of $CsBi_4Te_6$.

![](./images/812687490065367043_3.jpg)

FIG. 3. Band structure of $CsBi_4Te_6$ (a) before adding spin-orbit interaction and (b) after adding spin-orbit interaction.

### III. RESULTS AND DISCUSSION

The band structure calculations show that $CsBi_4Te_6$ is a narrow-gap semiconductor with a band gap of approximately 0.04 eV (Fig. 3), comparable to but smaller than the measured value of 0.05-0.11 eV.$^{10}$ A preliminary version of this work has been reported earlier.$^{18}$ This is not surprising because a smaller band gap is usually obtained in LDA/GGA calculations for many semiconductors.$^{19}$ In the absence of spin-orbit interaction, the band gap is 0.37 eV. The introduc-

tion of spin-orbit interaction produces a shift of the conduc- tion band toward the valence band, changing both the band gap and also the band curvature. Clearly the effect of spin- orbit interaction is to reduce the band gap and bring it to a much better agreement with experiment. A similar shift ofthe conduction band was also seen in $BaBiTe_{3}$ and $Bi_{2} Te_{3},^{11}$  but in the latter compound the shift was so large that new hybridization gaps formed, thereby giving completely differ- ent positions for the valence and conduction band extrema. Figure 3 shows that in $CsBi_{4} Te_{6}$ , the top of the valence band occurs at the $\Gamma$ point while the bottom of the conduction band occurs at a general point in the Brillouin zone (denoted as $C^{*}).[C^{*}=(0.881,0.881,0.175)$ in terms of the recipro cal lattice vectors.] In addition, there are several local con- duction band minima appearing slightly above this point(~0.1 eV above), along IZ and RV directions of the Bril- louin zone which can contribute to the transport. By a simple argument, $^{11}$ one can show that for the same carrier concen tration the thermopower S will increase for multiple hole or electron pockets, which will then increase the dimensionless figures of merit ZT.
Although multiple conduction band extrema may be a rea- son for anticipating a large ZT value in the electron-doped $CsBi_{4} Te_{6}$ (we note that large thermopower values in n-doped systems have not yet been seen in this compound), the single maximum of the valence band at the $\Gamma$ point requires another explanation for the observed large values of ZT in the hole- doped compound. In order to explore whether anisotropy in the charge transport (confinement idea of HD) may play a role, we have computed the effective carrier masses along different directions and also have analyzed the detailed na- ture of the electronic states (orbital character and parentage, i.e., Bi-p or Te-p, etc.) associated with the valence band maxima (holes) and conduction band minima (electrons). The value of ZT depends on a dimensionless parameter
$$B=\frac{1}{3 \pi^{2}}\left[\frac{2 k_{B} T}{h^{2}}\right]^{3 / 2} \sqrt{m_{x} m_{y} m_{z}} \frac{k_{B} T \mu_{x}}{e \kappa_{p h}}.$$

[Here $m_{x}$ , etc., are the effective masses along three principal directions, $\mu_{x}$ is the mobility along the direction of the cur rent flow (chosen as the x direction), and $\kappa_{p h}$ is the lattice thermal conductivity. $]^{6} B$ is a material parameter and for a fixed B one can maximize ZT by changing the doping level. This optimized value of ZT is then found to increase with B. Since the mobility $\mu_{x}$ depends inversely on $m_{x}$ , the effective mass dependence of B is $\sqrt{m_{y} m_{z} / m_{x}}=R \sqrt{m_{x}}$ . For an isotropic system R=1. For an anisotropic system we can assume that the smallest effective mass is along the x axis, the direc- tion of charge transport, while one or both of the effective masses associated with the other two directions are larger.Considering two cases (i) $m_{x}=m_{y}=m_{z} / \gamma$ , (ii) $m_{x}=m_{y} / \gamma$ =m,/y, y>1, we find that the ratio R is larger than the isotropic case by a factor $\sqrt{\gamma}$ for (i) and by a factor $\gamma$ for (ii).(When the three masses are different one has to generalize this slightly.) Thus the effective mass anisotropy can signifi- cantly affect ZT.
In $CsBi_{4} Te_{6}$ the effective masses along three specific di rections, i.e., the needle growth direction $(\Gamma X)$ , the direction

<table><caption>TABLE I. Effective masses associated with the valence and con- duction band extrema along three principal axes and the angles these axes make with a set of three suitably chosen orthogonal axes(see text).</caption>
<thead>
  <tr>
    <th>Valence band $(\Gamma)$</th>
    <th>Angle</th>
    <th>$m_{ii}/m_{e}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$X$ (needle)</td>
    <td>$12.37^{\circ}$</td>
    <td>0.02</td>
  </tr>
  <tr>
    <td>$Y$ (Bi-Bi bonds)</td>
    <td>$0.97^{\circ}$</td>
    <td>1.16</td>
  </tr>
  <tr>
    <td>$Z$ (Cs layers)</td>
    <td>$12.35^{\circ}$</td>
    <td>0.09</td>
  </tr>
  <tr>
    <td>Conduction band $(C^{*})$</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>$X$ (needle)</td>
    <td>$12.38^{\circ}$</td>
    <td>0.04</td>
  </tr>
  <tr>
    <td>$Y$ (Bi-Bi bonds)</td>
    <td>$3.17^{\circ}$</td>
    <td>0.47</td>
  </tr>
  <tr>
    <td>$Z$ (Cs layers)</td>
    <td>$11.98^{\circ}$</td>
    <td>0.16</td>
  </tr>
</tbody>
</table>

of the Bi-Te slabs $(\Gamma V)$ , and through the $Cs^{+}$ atom layer(ΓZ) were computed. Since the calculated system is triclinic, the full reciprocal mass tensor must be computed and diagonalized. $^{20}$ This has been done by choosing three or thogonal directions lying closest to the three directions men- tioned above, which we will denote as X, Y, and Z, respec- tively. The effective masses obtained from the eigenvalues of the inverse mass tensor are given in Table I. $^{21}$ The corresponding eigenvectors define different directions in the k space. For both the electrons and the holes the lightest effec- tive mass direction makes an angle of about $12^{\circ}$ with the needle axis while that with the intermediate mass direction also makes an angle of $12^{\circ}$ with the axis perpendicular to the $Cs^{+}$ layers. The direction of heaviest carriers lie within $1-3^{\circ}$  of the Y axis, i.e., parallel to the Bi-Bi bonds. The heaviest valence band mass is a factor of 50 larger than the lightest valence band mass while the heaviest conduction band mass is only a factor of 10 larger than the lightest conduction band mass. Thus the valence band holes are more spatially re- stricted than the electrons, particularly along the direction of the Bi-Bi bonds. These results suggest that the effective hole transport take place not along Bi/Te slabs but in planes nearly perpendicular to the slabs containing the needle axis. A similar situation was also found in $BaBiTe_{3}$ , but the de gree of anisotropy was much smaller. $^{11}$ Also the effectivemasses in $BaBiTe_{3}$ were found to be about a factor 5-6 higher leading to a lower mobility (lower conductivity). The transport in $Bi_{2} Te_{3}$ is different from that in $CsBi_{4} Te_{6}$ , the effective carrier transport is primarily in the needle direction and through the $Bi_{2} Te_{3}$ network. The effective masses in the transport directions are, however, comparable to those of $CsBi_{4} Te_{6} \cdot^{11}$ 
To understand the nature of the electron and hole states near the respective band extrema further, we have analyzed the wave functions in some detail. When the strengths of the orbital character associated with these states are studied for different atoms, it is seen that the valence band density forms a quasi-two-dimensional layer lying almost perpendicular to the $[Bi_{4} Te_{6}]$ slabs while the conduction band density is more three-dimensional, consistent with our effective mass calcu- lations. We find the states corresponding to the valence bandmaxima consist of Bi (Bi1, Bi6) and Te (Te1, Te3, Te6, Te8)(Fig. 1) atoms and the charge density associated with these

![](./images/812687490065367043_4.jpg)

FIG. 4. Quasi-two-dimensional sheets contributing to hole trans- port overlying the crystal structure of $CsBi_{4}Te_{6}$. Filled dark circles: Bi; Open circles: Te; Filled light circles: Cs.

atoms forms corrugated, two-dimensional sheets separated by approximately $13\ \mathring{A}$ (Fig. 4). There are very few atoms lying between the sheets with contributions to these states (which would have allowed for transport in the direction of the Bi-Bi bonds), consistent with the large effective mass found in this direction. On the other hand, the charge density associated with states near the conduction band minima does not show such two-dimensional sheetlike behavior, but shows a more or less isotropic behavior. The largest contri- bution to the states near the conduction band minimum comes from the Bi-Bi (Bi7 and Bi8 atoms in Fig. 1) bonds, a bonding not seen before in chalcogenides. These arise from the antibonding state of the Bi-Bi bond, the bonding state lying below the valence band maxima. This may be under- stood from stabilization of the donor electron from Cs by this Bi-Bi bond which is necessary for the formation of a semiconductor. $^{10}$ (The Cs atoms act primarily as electron do nors with little contribution near the top of the valence band or the bottom of the conduction band.) The Bi-Bi bonds, connecting the Bi/Te network together, have their antibond- ing states in the conduction band and their bonding states in the valence band but with only a small contribution from states near the valence band maxima. This implies that trans- port of holes near the valence band maxima taking place through the Bi-Bi bonds will be blocked in this direction, explaining their large effective masses in this direction. One will see a two-dimensional sheetlike transport for these holes.

As discussed briefly at the beginning of this paper, sys- tems with different structures have been synthesized to ex- ploit low-dimensional transport and have shown to give rise to an increase in the figure of merit. $^{8,9,22}$ The vast majority of these attempts revolve around nanofabrication of quantum wells or multilayer films. $CsBi_{4}Te_{6}$ , on the other hand, quite naturally displays quasi-two-dimensional hole transport with regions of the crystal of several $\mathring{A}$ width participating very little in the charge transport. These "insulating" regions are sandwiched between conducting regions, leading to struc- tures similar to quantum wells or multilayers, but in a bulk material. The source of this anisotropic hole transport arises from the Bi-Bi bonds, which are not seen in other bismuth chalcogenides. It is possible to take advantage of this novel quantum architecture in other Cs-Bi-Te compounds where the Bi-Bi bonds are closer together or further apart. While the conduction band has several degenerate minima, the transport in this band is much more isotropic. However, large values of $ZT$ are still possible for the electron-doped systems when several of these local minima get occupied. $BaBiTe_{3}$ , which has a strong structural similarity with $CsBi_{4}Te_{6}$ , does not show as large an anisotropy as the latter compound. Fur- thermore the effective mass along the optimum direction (needle axis) is a factor of 10 larger in $BaBiTe_{3}$ than $CsBi_{4}Te_{6}$ . These two features combined are responsible for the low $ZT$ values observed in $BaBiTe_{3}$ . $^{11}$

## IV. SUMMARY

In summary, the novel quantum architecture of $CsBi_{4}Te_{6}$ involving Bi-Bi bonds lead to a reduced dimensionality for hole transport in this bulk material. This, along with a very small effective mass along the needle axis, and overall low thermal conductivity, can explain the large thermoelectric figure of merit seen in this compound. $^{10,23}$ The reduced di mensionality of the transport leads to an enhancement of $ZT$ through the $B$ parameter by a factor of $\sqrt{\gamma}$ (discussed in Sec. III) for this quasi-two-dimensional system. The enhancement seen in $CsBi_{4}Te_{6}$ suggests that for thermoelectric applica tions, one should look for bulk materials which have highly anisotropic masses and reduced dimensionality in their transport.

## ACKNOWLEDGMENTS

This work was supported by DARPA Grant No. DAAG55-97-1-0184 and ONR. We acknowledge helpful dis- cussions with Dr. David Singh of NRL.

$^{1}$Thermoelectric Materials-The Next Generation Materials for Small-Scale Refrigeration and Power Generation Applications, edited by T.M. Tritt, M.G. Kanatzidis, G.D. Mahan, and H.B. Lyon, Jr., MRS Symposia Proceedings No. 545 (Materials Re- search Society, Pittsburgh, 1999); F.J. DiSalvo, Science 285, 703 (1999); T.M. Tritt, ibid. 283, 804 (1999).

$^{2}$B.C. Sales, D. Mandrus, and R.K. William, Science 272, 1325 (1996); B.X. Chen, J.H. Xu, and C. Uher, Phys. Rev. B 55, 1476 (1997).

$^{3}$P. Larson, S.D. Mahanti, S. Sportouch, and M.G. Kanatzidis, Phys. Rev. B 59, 15 660 (1999); S. Ogut and K.M. Rabe, ibid. 51, 10 443 (1995); C. Uher, J. Yang, S. Hu, D.T. Morelli, and G. P. Meisner, ibid. 59, 8615 (1999).

$^{4}$G. Nolas, J.L. Cohn, G. Slack, and S.B. Schujman, Appl. Phys. Lett. 73, 178 (1998).

$^{5}$R.T. Littleton, T.M. Tritt, C.R. Feger, J. Kolis, M.L. Wilson, M. Marone, J. Payne, D. Verebeli, and F. Levy, Appl. Phys. Lett. 73, 178 (1998).


$^{6}$L.D. Hicks and M.S. Dresselhaus, Phys. Rev. B $\boldsymbol{47}$, 12 727 (1993); L.D. Hicks and M.S. Dresselhaus, ibid. $\boldsymbol{47}$, 16 631 (1993); L.D. Hicks, T.C. Harman, and M.S. Dresselhaus, Appl. Phys. Lett. $\boldsymbol{63}$, 3230 (1993).

$^{7}$G.D. Mahan and J.O. Sofo, Proc. Natl. Acad. Sci. U.S.A. $\boldsymbol{93}$, 7436 (1996).

$^{8}$T.C. Harman, P.J. Taylor, D.L. Spears, and M.P. Walsh, J. Elec- tron. Mater. $\boldsymbol{29}$, L1 (2000).

$^{9}$R. Venkatasubramanian, Phys. Rev. B $\boldsymbol{61}$, 3091 (2000).

$^{10}$D-Y Chung, T. Hogan, P. Brazis, M. Rocci-Lane, C. Kannewurf, M. Bastea, C. Uher, and M.G. Kanatzidis, Science $\boldsymbol{287}$, 1024 (2000).

$^{11}$P. Larson, S.D. Mahanti, and M.G. Kanatzidis, Phys. Rev. B $\boldsymbol{61}$, 8162 (2000).

$^{12}$D. Singh, *Planewaves, Pseudopotentials, and the LAPW Method* (Kluwer Academic, Boston, 1994).

$^{13}$P. Hohenberg and W. Kohn, Phys. Rev. $\boldsymbol{136}$, B864 (1964); W. Kohn and L. Sham, ibid. $\boldsymbol{140}$, A1133 (1965).

$^{14}$J.P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. $\boldsymbol{77}$, 3865 (1996).

$^{15}$P. Blaha, K. Schwarz, and J. Luitz, WIEN97 (Vienna University of Technology, Vienna, 1997).

$^{16}$D.D. Koelling and B. Harmon, J. Phys. C $\boldsymbol{10}$, 3107 (1977); P. Novak (unpublished).

$^{17}$S.K. Mishra, S. Satpathy, and O. Jepsen, J. Phys.: Condens. Mat- ter $\boldsymbol{91}$, 461 (1997).

$^{18}$P. Larson, S.D. Mahanti, D.-Y. Chung, and M.G. Kanatzidis, MRS Symposia Proceedings No. $\boldsymbol{626}$ (Materials Research Soci- ety, Pittsburgh, 2000).

$^{19}$W.E. Aulbur, L. Jonsson, and J.W. Wilkins, *Solid State Phys.* edited by H. Ehrenreich and F. Spaepen (Academic Press, New York, 2000), Vol. 54, p. 11.

$^{20}$N. W. Ashcroft and N. David Mermin, *Solid State Physics* (Harcourt Brace College Publishers, Orlando, FL, 1976), pp. 228–229.

$^{21}$In low-dimensional systems, such as the triclinic system dis- cussed here, the effective mass approximation is not expected to hold at large carrier concentrations. However, up to carrier con- centrations consistent with the optimum doping of this system [$∼3×10^{18}$/cm³ (Ref. 10)] the agreement between the calculated dispersions and the parabolic fit was excellent.

$^{22}$Z.B. Zhang, J.Y. Ying, and M.S. Dresselhaus, J. Mater. Res. $\boldsymbol{13}$, 1745 (1998).

$^{23}$Transport calculations within the constant relaxation time and iso- tropic effective mass [$m_{\text{eff}}=(m_xm_ym_z)^{1/3}$] approximations have been performed using the values of $m_{\text{eff}}$ obtained in this calcu- lation (Table I). For a gap of 0.04 eV and a doubly degenerate conduction band at $C^*$, a maximum in the thermopower was found to be 145 $\mu$V/K near 250 K for the hole doping ($∼1.9×10^{18}$/cm³), in fair agreement with experiment (Ref. 10).