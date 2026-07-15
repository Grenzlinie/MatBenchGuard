equilibrium state of that phase, corresponding to the minimum of the total energy as a function of the lattice parameters. The total energy differences between the sigma phase and the SER structure of the pure constituents can be implemented into the new model of description of the sigma-phase [12].

The aim of this paper is to verify this approach in the case of the Co-Cr system.

## Calculations

### Calculation of Phase Diagrams

The behaviour of the system is defined by the minimum of the total Gibbs energy $G^{\text{tot}}$ at given conditions of pressure and temperature. $G^{\text{tot}}$ is equal to the sum of the Gibbs energies of all phases $(G^{\text{f}})$ multiplied by their volume fraction $(w^{\text{f}})$, i.e.

$$
G^{\text{tot}} = \sum_{\text{f}} w^{\text{f}} G^{\text{f}} . \tag{1}
$$

The $G^{\text{f}}$ is again a function of the thermodynamic conditions considered above, and it is defined as

$$
G_{.}^{\text{f}} = \sum_{\text{i}} y_{\text{i}} {^0} G_{\text{i}}^{\text{f}} + G^{\text{id}} + G^{\text{E}} + G^{\text{mag}} + G^{\text{pres}}, \tag{2}
$$

where $y_{\text{i}}$ is the lattice fraction of the component i, $^0 G_{\text{i}}^{\text{f}}$ is the Gibbs energy of a pure constituent i in the phase f, the term $G^{\text{id}}$ describes the Gibbs energy of ideal mixing, $G^{\text{E}}$ is the excess Gibbs energy describing real mixing, $G^{\text{mag}}$ is the magnetic contribution and $G^{\text{pres}}$ is the pressure contribution to the Gibbs energy. The $^0 G_{\text{i}}^{\text{f}}$ constitute the main input information for phase diagram calculations based on the CALPHAD approach. These values are easily available for many structures of the pure elements, e.g. bcc, fcc, hcp, because they are usually quite well measurable. They are summarised in various databases, e.g. [13]. However, there is a problem in the case of the sigma phase because it is much more complicated, it is unstable for the pure constituents and its region of stability is too narrow for reasonable extrapolation. This experimentally unsolvable problem can be treated using ab initio calculations. The ab initio approach allows us to replace methods of construction of the Gibbs energy for the sigma phase that use the combination of Gibbs energies of bcc and fcc structures according to similarity in coordination number [14,15], or that estimate it using extrapolation of experimental data [16].

The model of a substitutional structure $(B)_8(A)_4(A,B)_{18}$ or $(B)_{10}(A)_4(A,B)_{16}$ is the one of the most widely used methods in recent time [14,15] but it has some disadvantages. The first step of description of the sigma phase in this model is the reduction of number of sublattices. It is known from X-ray experiments that the sigma phase (space group No. 136, $P4_2/mnm$) contains 30 atoms in the unit cell distributed into five crystallographically inequivalent sublattices (2a, 4f, 8i, 8i' and 8j) [17], too many for a reasonable CALPHAD description. Therefore, the number of sublattices should be reduced [14,15,18]. In [14], some general rules for such a reduction in the number of sublattices and for their occupation were formulated:

(i) All sublattices with the same coordination number (CN) and similar point symmetry are combined into one.

(ii) If more than one sublattice remains, combine the two with the highest CN into one.

(iii) The reduced set of sublattices must be arranged in the order of increasing CN.

(iv) B elements will go preferentially into the first sublattice but it may dissolve some A.

(v) The next sublattice will be preferentially filled with A but it may dissolve some B.

(vi) If there is a third sublattice, it will be reserved for A.

If A is an element of the $\text{VI}^{\text{th}}$ group of the Periodical Table or lower, and B is an element of the $\text{VII}^{\text{th}}$ group or higher, then, in the case of a binary sigma phase, the CN of individual sublattices in Co(A)-Cr(B) are, by analogy to [18], as follows: 2a (CN=12), 4f (CN=15), 8i (CN=12), 8i' (CN=14) and 8j (CN=14). The first and third sublattice and the fourth and fifth sublattice are combined according to the point (i) above to obtain the preliminary formula 16(8i'+8j) 4(4f) 10 (2a+8i). Then the sublattices are arranged in the order of increasing CN and are occupied by atoms in order to satisfy the points (iv) - (vi) getting 10(A,B):16(A,B):4(A). At the end of the procedure for reducing the number of model parameters, it is assumed [18] that the occupation of the second sublattice by A atoms is negligible, i.e. we have 10(B):16(A,B):4(A), and the sublattice with mixed occupation is moved to the end of the formula. So the resulting formula is 10(B) 4(A) 16(A,B) or, alternatively, $(B)_{10}(A)_4(A,B)_{16}$.

Gibbs energy of the sigma phase for the pure constituents on a physically correct energy basis.

Let us note, however, that we are not able to incorporate the contribution from the zero-point motion. It is not excluded that, when evaluating the structural energy differences, this contribution may play quite an important role.

There is only one disadvantage in this model. We are not able to calculate the entropy of the system and, therefore, it is still adjusted to phase equilibrium data. This model was already successfully used in the case of Cr-Fe system [20] and the Co-Cr system is modelled in the present paper using existing assessments for remaning phases.

## Calculation Of Total Energy Differences

The total energies of both structures (SER and sigma phase) at their equilibrium volumes were calculated within the Full-Potential Linearized Augmented Plane Waves (FLAPW) method incorporated in the WIEN97 code [21] using the Generalised Gradient Approximation (GGA) [22] for the exchange-correlation term.

At the beginning of our calculations, the internal parameters (i.e. the positions of all atoms in the unit cell) of the hypothetical sigma phase for pure cobalt were chosen. The total energies of the mentioned structure were calculated at constant lattice parameters [23] using various internal parameters of binary sigma-phases that contained cobalt (e.g. Co-Cr, Co-Mo etc.). We have chosen that set of internal parameters, which exhibited the lowest total energy [24]. The same procedure was applied for the choice of the internal parameters of a hypothetical Cr in the sigma phase structure. The lowest total energy of Cr sigma phase was found at the lattice parameters given in [25] and internal parameters given in [23].

In the following calculations, the internal parameters were kept constant because we have found that their optimisation does not have any significant influence on the total energy of the sigma phase. The changes in total energy caused by changing the internal parameters within the limits found in the literature did not exceed the value of 2 mRy/atom and, on average; they amounted to 0.5 mRy/atom.

Now, to estimate the equilibrium values of the lattice constants of the sigma-phase, we performed auxiliary calculations with the Linear Muffin-Tin Orbital method in the Atomic Sphere Approximation (LMTO-ASA) [26].

Then we continued the FLAPW calculations. The optimal RMT (muffin-tin radius) and number of k-points needed for the calculations were chosen. The RMT parameters used in this work are 1.97 a.u. in the case of cobalt and 2.1 a.u. in the case of chromium. Concerning the number of k-points in the irreducible zone found by preliminary optimisation, the used values are 42 in the case of cobalt and 36 in the case of chromium.

The process of optimisation of the lattice parameters is very simple. It is based on repeating two steps until the change in the total energy is small enough. These steps are the optimisation of the volume at constant $c/a$ ratio (constant shape of unit cell) and optimisation of the $c/a$ ratio at constant volume ($V_{min}$ from the previous step).

The calculations for the SER-phases (ferromagnetic hcp Co and antiferromagnetic bcc Cr) were not so time-consuming because the LMTO-ASA calculations had not been performed and the RMT parameters had been taken from the sigma phase calculations. The k-points convergence tests resulted in using 320 k-points for cobalt and 120 k-points for chromium in all following calculations. The optimisation of the unit cells with two atoms had the same theoretical basis as in the sigma phase calculations but the optimisation of the $c/a$ ratio was not employed in the case of the cubic structure, and therefore the calculations of the bcc structure were finished already after the first optimisation step.

## Results And Discussion

The calculated total energies for the pure constituents in both structures were used for evaluating the lattice stability of the sigma phase characterized by the total energy difference $\Delta^0\mathrm{E}_i^{\sigma-\mathrm{SER}}=\mathrm{^0E}_i^{\sigma}-\mathrm{^0E}_i^{\mathrm{SER}}$.

The profiles of the total energy as a function of volume in the case of both constituents in the sigma phase arrangement obtained from the last step of optimisation are shown in Fig. 1. The crossing points with previous optimisation curves are represented by full symbols. The difference in total energies obtained in the

last two steps was smaller than 0.2 mRy/at, and therefore we could stop the optimisation at this level. The lattice parameters of the unit cell corresponding to the minimum of total energy are listed in the Table 1.

Table 1. FLAPW calculated equilibrium volumes per atom (a.u.³) and lattice parameters (a.u.) of the thirty-atom unit cell of hypothetical sigma phase of end members Cr and Co.

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Cr</th>
      <th>Co</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Volume</td>
      <td>76.7127</td>
      <td>69.1070</td>
    </tr>
    <tr>
      <td>$a$</td>
      <td>16.3792</td>
      <td>15.8602</td>
    </tr>
    <tr>
      <td>$c$</td>
      <td>8.5783</td>
      <td>8.2419</td>
    </tr>
  </tbody>
</table>

The optimised total energy profiles for the SER structures (the first one for antiferromagnetic Cr in the bcc structure and the third one in the case of ferromagnetic Co in the hcp structure) are presented in Fig.2. The optimised lattice parameters together with the experimental ones are listed in Table 2.

Table 2. Values of experimental and FLAPW equilibrium lattice parameters (a.u.) for the SER phase of antiferromagnetic Cr and ferromagnetic Co.

<table>
  <thead>
    <tr>
      <th rowspan="2">Lattice parameter</th>
      <th colspan="2">Cr</th>
      <th colspan="2">Co</th>
    </tr>
    <tr>
      <th>ab-initio</th>
      <th>experiment [30]</th>
      <th>ab-initio</th>
      <th>experiment [2]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$a$</td>
      <td>5.41653</td>
      <td>5.44</td>
      <td>4.62149</td>
      <td>4.74</td>
    </tr>
    <tr>
      <td>$c$</td>
      <td>5.41653</td>
      <td>5.44</td>
      <td>7.40598</td>
      <td>7.69</td>
    </tr>
  </tbody>
</table>

The deviation of the calculated equilibrium lattice constant from the experimental values is -0.43% for Cr and -2.41% for the $a$ lattice parameter and -3.68% for the $c$ lattice parameter in the case of Co. The calculated total energies for the optimised structures and their differences are summarised in Table 3.

Table 3. Ab initio calculated values of equilibrium total energies per atom (Ry/atom) for sigma phase and SER phase of Cr and Co and their differences.

<table>
  <thead>
    <tr>
      <th>Variable</th>
      <th>Cr</th>
      <th>Co</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Total energy per atom of $\sigma$-phase</td>
      <td>-2 101.7603</td>
      <td>-2 786.8954</td>
    </tr>
    <tr>
      <td>Total energy per atom of SER</td>
      <td>-2 101.7832</td>
      <td>-2 786.9190</td>
    </tr>
    <tr>
      <td>Total energy difference per atom ($\sigma$-SER)</td>
      <td>0.0229</td>
      <td>0.0236</td>
    </tr>
  </tbody>
</table>

It is well known that the energy difference between the bcc and fcc structures and fcc and hcp structures of Cr and Co, predicted by first principles methods [27], are substantially larger than those estimated by the CALPHAD approach. So, it is not surprising that the energy differences between the bcc and sigma-phase Cr or hcp and sigma-phase Co are so large.

These total energy differences were used in the new two-sublattices model presented in [12] for phase diagram calculations. The temperature dependence of the excess Gibbs energy of the sigma phase (entropy term) had still to be adjusted to phase equilibrium data, following the traditional CALPHAD method.

The calculations of phase diagram and thermodynamic values were performed by means of the THERMO-CALC program [28]. The recent assessment [29] gave us the Gibbs energies of all phases (bcc, fcc, hcp, and liquid) that exist in the Co-Cr system using data for the pure constituents from [13]. The final calculated phase diagram is given in Fig.3 (full lines). The dashed lines represent the phase diagram calculated by the old model [29]. There is an important improvement in the position of the line that describes the equilibrium between the sigma phase, the paramagnetic hcp, and the ferromagnetic hcp phases at the Co-rich side. Our calculated position corresponds better to that reported in [30] which is approximately 610 K. The

phase diagram calculated using the new model is in good agreement with experimental data given in [3-10]. The values of the adjustable parameters used in this calculation are summarised in Table 4.

Table 4. Values of the adjustable parameters for the sigma phase (eqs. (7), (9), and (10)) used in the calculation of the phase diagram of Co-Cr. The values of E, J, and L in eq. (10) were set to zero.

<table>
  <thead>
    <tr>
      <th>PARAMETER</th>
      <th>Cr</th>
      <th>Co</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$S^{\sigma}$</td>
      <td>+ 0.7</td>
      <td>+0.75</td>
    </tr>
    <tr>
      <td>$L^{0}$</td>
      <td colspan="2">-115 950</td>
    </tr>
    <tr>
      <td>$L^{1}$</td>
      <td colspan="2">+ 10 800</td>
    </tr>
    <tr>
      <td>$L^{2}$</td>
      <td colspan="2">- 95 000</td>
    </tr>
  </tbody>
</table>

The composition dependences of the Gibbs energy and the enthalpy were calculated for both models at 1200 K and they are shown in Figs. 4 and 5. We may see that the lines 5 and 5a obtained using the new two-sublattices model and the three-sublattices model, respectively, are quite different. Regrettably, available experimental values of enthalpy of formation provide no possibility to prefer one of them (see Fig. 5). It is worth noting that the description obtained from the old model is constrained to a limited range of concentrations while the two-sublattices model [12] provides these values in the whole range of composition.

## Conclusions

The ab initio calculations of lattice stability for various structures performed by FLAPW method provide a possibility for improving phase diagram calculations. The results of ab initio calculations may be utilised in a new two-sublattices model [12] that yields a better agreement with experimental data than the old three-sublattices model [15]. In the present paper, the procedure was tested on the Co-Cr system.

Our approach has a solid physical background and enables us to predict the region of stability of the sigma phase in metallic materials.

## Acknowledgements

This research was supported by the Grant Agency of the Czech Republic (Project No. 106/02/0877). The use of computer facilities at the MetaCenter of Masaryk University, Brno, is acknowledged.

## References

1.  E. C. Bain, *Chem. and Met. Eng.*, **28** (1923) 23.
2.  P. Villars and L.D.Calvert, *Pearson's Handbook of Crystallographic Data for Intermetallic Phases*, ASM International, Materials Park, OH, 1991.
3.  C.A. Allibert, C. Bernard, N. Valigant and M. Dombre, *J. Less-Common Met.*, **59** (1978) 221-228.
4.  F. Wever and U. Hashimoto, *Mitt. Kaiser-Wilhelm-Inst. Eisenforsch.*, **11** (1929) 293-308.
5.  Y. Matsungana, *Kinzoku-no-Kenkyu*, **8** (1931) 549-561.
6.  A.G. Metcalfe, *Trans. AIME*, **197** (1953) 357-364.
7.  A. Chiba, *Ph.D. thesis*, Tohoku Univ. Sendai, Japan, 1971.
8.  Z. Jin, *Scand. J. Metall.*, **10** (1981) 279-287.
9.  M. Hasebe, K. Oikawa and T. Nishizawa, *J. Jpn. Inst. Met.*, **46** (1982) 557-583.
10. J.W. Smits, S.B. Luitjens and F.J.A. den Broeder, *J. Appl. Phys.*, **55** (1984) 2260-2262.
11. N. Saunders and P. Miodównik, *CALPHAD – A Comprehensive Guide*, Elsevier, London, 1998.
12. J. V eš ál, *Archives of Metallurgy*, **46** (2001) 239-247.
13. A.T. Dinsdale, *Calphad*, **15** (1991) 317-425.

14. M. Hillert, *Calphad*, **22** (1998) 127-133.

15. J.-O. Anderson and B. Sundman, *Calphad*, **11** (1987) 83.

16. C. Allibert, C. Bernard, G. Effenberg, H.-D. Nüssler and P.J Spencer, *Calphad*, **5** (1981) 227.

17. J.L.C. Daams, P. Villars and J.H.N. van Vucht, *Atlas of Crystal Structure Types for Intermetallic Phases*, vols. 1-4, ASM International, 1991.

18. I. Ansara, T.G. Chart, A. Fernandez Guillermet, F.H. Hayes, U.R. Kattner, D.G. Pettifor, N. Saunders and K. Zang, *Calphad*, **21** (1997) 171-218.

19. S.H. Algie and E.O. Hall, *Acta Crystallographica*, **20** (1966) 142.

20. J. Houserová, M.Friák, M. Šob and J. V eš ál, *Computational Materials Science*, in print.

21. P. Blaha, K. Schwarz and J. Luitz, *WIEN97*, Vienna University of Technology 1997 (improved and updated Unix version of the original copyrighted WIEN code, which was published by P. Blaha, K. Schwarz, P. Sorantin and S.B. Trickey in Comput. Phys. Commun. 59 (1990) 399).

22. J.P. Perdew, J.A. Chevary, S.H. Vosko, K.A. Jackson, M.R. Pederson, D.J. Singh and C. Fiolhais, *Phys. Rev. B*, **46** (1992) 6671.

23. G.J. Dickins, Audrey M.B.Douglas and W.H.Taylor, *Acta Crystallographica*, **9** (1956) 297.

24. J.B. Forsyth, and d'Alte da Viega, *Acta Crystallographica*, **16** (1963) 509-512.

25. H.L. Yakel, *Acta Crystallographica B*, **39** (1983) 20-28.

26. G. Krier, O. Jepsen, A. Burkhardt and O.K. Andersen, *Computer code TB-LMTO-ASA version 4.6*, Max-Planck-Institut für Festkörperforschung, Stuttgart, 1994.

27. H.L. Skriver, *Phys.Rev.B*, **31** (1985) 1909.

28. B. Sundman, *THERMO-CALC*, version L, Royal Institute of Technology, Stockholm, 1997.

29. A. Kusoffski and Bo Jansson, *Calphad*, **21** (1997) 321-333.

30. G.W. Qin, K. Okinawa, T. Ikeshoji, R. Kainuma and K. Ishida, *Journal of Magnetism and Magnetic Materials*, **234** (2001) L1-L5.

31. H.B. Bell, J.p. Hajra, F.H. Putland and P.J. Spencer, *Mat.Sci Journal*, **7** (1973) 185.

32. D.B. Downie and F.Arslan, *J.Chem. Thermodynamics*, **15** (1983) 654.

33. A.A. Zubkov, B.M. Mogutnov and N.O. Shaposhnikov, *Dokl. Akad. Nauk SSSR*, **31** (1990) 388.
[Dokl. Phys. Chem., **311**, (1990) 239.]

![](./images/812393571138142209_1.jpg)

Fig. 1. Final FLAPW optimisation of the volume per atom of the sigma phase (30 atoms/cell) for pure Cr (squares) and Co (diamonds) at constant $c/a$ ratio ($c/a_{\text{Co}}=0.5237$ $c/a_{\text{Cr}}=0.5197$, respectively.). Full symbols represent the crossing points with previous optimisation profile of total energy (per atom) vs. $c/a$ ratio.

![](./images/812393571138142209_2.jpg)

Fig. 2. The volume dependence of the total energy (per atom) of antiferromagnetic Cr and ferromagnetic Co.

![](./images/812393571138142209_3.jpg)

Fig. 3. Comparison of phase diagrams of Co-Cr. Full line: calculated by the new two-sublattices model (this work, for the adjustable parameters see Table 4), dashed line: calculated by the three-sublattices model [28], the experimental data: ⊕ [3], ∇ [4], • [5], + [6], ⊖ [7], ◇ [8], * [9], △ [10]. The dotted line represents the concentration dependence of the Curie temperature [29], letter f denotes the ferromagnetic phase and p is the paramagnetic phase.

![](./images/812393571138142209_4.jpg)

Fig. 4. Concentration dependence of the Gibbs energy for the Co-Cr system at 1200 K. 1: liquid phase, 2: bcc phase, 3: hcp phase, 4: fcc phase, 5: sigma phase (new two-sublattices model), 5a: sigma phase (three-sublattices model).

![](./images/812393571138142209_5.jpg)

Fig. 5. Same as for Fig. 4 but for the concentration dependence of the enthalpy in the Co-Cr system at 1200 K.
Available experimental data are denoted as + [31], Δ [32], O [33].