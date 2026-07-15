![](./images/812433149534404609_1.jpg)

Journal of Computer-Aided Materials Design, 6: 129-136, 1999.
KLUWER/ESCOM
© 1999 Kluwer Academic Publishers. Printed in the Netherlands.

# A bond-order potential for atomistic simulations in iron

GENRICH L. KRASKO$^{a, *}$, B. RICE$^{b}$ and S. YIP$^{a}$

$^{a}$Department of Nuclear Engineering, Massachusetts Institute of Technology, Cambridge, MA 02139-4307,
U.S.A.
$^{b}$Weapons and Materials Research Division, Army Research Laboratory, Aberdeen Proving Ground,
MD 21005-5069, U.S.A.

Received 5 July 1999; Accepted 6 August 1999

**Abstract.** A new semi-empirical potential for Fe based on the quantum chemistry concept of bond order has been developed. The potential consists of two parts: the repulsive short-range exponential potential, and the attractive potential, also of the exponential form, with a bond-order prefactor. The latter depends on angles between the Fe- Fe bonds, and uses the environmental parameter similar to that of the Tersoff bond-order potential for tetrahedrally bonded semiconductors. The bond order function (depending on the above environmental parameter), however, is of a more general form than that of the Tersoff potential. The new potential was calibrated using the traditional fitting to the Universal Scaling and the equilibrium volume and cohesive energy of BCC Fe. The introduced 'punishment functions' also directed the multi-variate minimization process towards minimizing the deviations between the calculated and experimental values of the elastic moduli $C'$ and $C_{44}$, the energies of FCC and HCP Fe modifications, and the (111) free surface energy. With the total of 15 fitted parameters, the potential reproduces with only minor deviations the elastic moduli, the volume-pressure equation of states in BCC phase, the energies in FCC and HCP modifications, the BCC-HCP phase transformation under pressure, and the energy of the (111) free surface. Other tests of the new potential are being currently performed. The potential will be used in atomistic simulations of lattice stability, and deformation and chemisorption processes in Fe.

**Keywords:** Atomistic simulation, Bond order potential, Iron

## 1. Introduction

Among the elemental solids which have received special attention in materials theory and ap- plications, Fe is rather unique in its scientific and technological importance, ranging from un- derstanding earth's inner core in seismology [1] to that of property changes in structural appli- cations, such as radiation embrittlement of nuclear reactor pressure vessels [2] and toughness of high-strength Fe-base alloys [3]. In fact, in spite of emerging families of new, non-metallic materials, Fe still constitutes the technological core of our civilization.

Ever since the early days of computational modeling, developing a capability to reliably predict the strength and other physical properties of Fe has been a recognized challenge. In the current context of modeling materials properties and behavior across various length scales, there continues to be interest in gaining a more fundamental and quantitative understanding of how this particular material deforms under stress or behaves under other physical or chemical exposures.

Two approaches currently exist for modeling Fe. Development in the recent decade of efficient methods of ab initio calculations and proliferation of high-speed computers made it possible to perform high-precision first-principles calculations on Fe. This approach has

*To whom correspondence should be addressed.

essentially improved our understanding of structural properties of Fe under high pressure [4], as well as elucidated the energetics of important polymorphic transformations in Fe: BCC-FCC [5], and BCC-HCP [6,7]. Ab initio modeling of Fe grain boundaries has resulted in gaining an understanding, at atom-electron level, of the effect of interstitial impurities on cohesion-decohesion processes at grain boundaries, and grain-boundary embrittlement [8,9]. The state-of-the-art ab initio calculations on Fe free surfaces have enabled one to better understand the multilayer relaxation and chemisorption of hydrogen [10,11].

In atomistic simulations it is often the case that one has to strike a balance between robustness and accuracy of the model and computational feasibility of the study. BCC transition metals pose particular challenges because the use of empirical potential functions is well known to be of questionable validity. At the same time, properties such as strong directional bonding and ferromagnetism make it necessary to consider the electronic degrees of freedom explicitly in describing the interatomic interactions.

Practically all current atomistic simulations in Fe are concerned with BCC structure using variants of a many-body potential in one of two forms: the so-called Embedded Atom Method (EAM) [12], and the so-called N-body or Finnis–Sinclair potential [13] (for references see, e.g. [14]).

The most advanced models, allowing for directionality of interatomic bonds, explore two ideas: (i) the tight-binding analysis utilizing moments of the electronic density of states [15], and (ii) the well-known quantum chemistry concept of ‘bond-order’ (BO) [16]. In recent years the BO-type empirical potentials have been widely used in atomistic modeling of diamond-structure semiconductors and their alloys and compounds (see, e.g. [17,18]).

Recently, a new approach, explicitly allowing for ferromagnetic effects via the Stoner model, has been suggested [19]. In this paper, however, we explore the ideas behind the Tersoff BO approach [17] and develop a BO potential to be used in atomistic simulations of Fe.

Section 2 briefly outlines the Tersoff approach [17] which serves as a prototype for our new potential. In Section 3 we describe this potential and the procedure of fitting its parameters. Section 4 gives our conclusions.

## 2. Tersoff bond-order potential

At the present time there exist quite a few bond-order models for calculating the energetics of covalent crystals (for a review see [20]). Among these models, for our purposes, the so-called Tersoff potentials [17] are of prime interest. Formulated initially for Si crystals, the potentials were also used for C and Ge, and later generalized to allow for description of multi-component systems [17,18]. The Tersoff potentials explicitly take into account the directionality of bonds. For a one-component covalent crystal, the total energy is taken to be:

$$
\mathrm{E}=1 / 2 \Sigma_{\mathrm{i} \neq \mathrm{j}} \mathrm{f}_{\mathrm{c}}\left(\mathrm{R}_{\mathrm{i}}-\mathrm{R}_{\mathrm{j}}\right)\left[\mathrm{V}_{\mathrm{rep}}\left(\mathrm{R}_{\mathrm{i}}-\mathrm{R}_{\mathrm{j}}\right)+\mathrm{V}_{\mathrm{bo}}\left(\mathrm{R}_{\mathrm{i}}, \mathrm{R}_{\mathrm{j}}\right)\right] \tag{1}
$$

Here $\mathrm{f}_{\mathrm{c}}(|\mathrm{R}|)$ is the cut-off function:

$$
\mathrm{f}_{\mathrm{c}}(|\mathrm{R}|)= \begin{cases}1, & \mathrm{R}<\mathrm{r}_{\mathrm{c} 1} \\ 1 / 2+1 / 2 \cos \left[\pi\left(\mathrm{R}-\mathrm{r}_{\mathrm{c} 1}\right) /\left(\mathrm{r}_{\mathrm{c} 2}-\mathrm{r}_{\mathrm{c} 1}\right)\right], & \mathrm{r}_{\mathrm{c} 1}<\mathrm{R}<\mathrm{r}_{\mathrm{c} 2} \\ 0, & \mathrm{R}>\mathrm{r}_{\mathrm{c} 2}\end{cases} \tag{2}
$$

$\mathrm{r}_{\mathrm{c} 1}$ and $\mathrm{r}_{\mathrm{c} 2}$ are the cut-off radii; $\mathrm{V}_{\mathrm{rep}}\left(\mathrm{R}_{\mathrm{i}}-\mathrm{R}_{\mathrm{j}}\right)$ is a repulsive pair-wise potential, having a simple exponential form:

$$
\mathrm{V}_{\mathrm{rep}}(\mathrm{R})=\mathrm{A} \exp \left(-\beta_{1}|\mathrm{R}|\right) \tag{3}
$$

A and $\beta_1$ are the adjustable parameters. $\mathrm{V_{bo}(R_i, R_j)}$ is a BO potential, defined as follows:

$$
\mathrm{V_{bo}(R_i, R_j)} = -\mathrm{Bb(R_i, R_j)} \exp(-\beta_2|\mathrm{R_i - R_j}|), \tag{4}
$$

where $\mathrm{b(R_i, R_j)}$ is a 'BO function', defined as:

$$
\mathrm{b(R_i, R_j)} = \chi[1 + \beta^{\mathrm{n}} \zeta_{\mathrm{ij}}^{\mathrm{n}}]^{(-1/2\mathrm{n})} \tag{5}
$$

$$
\zeta_{\mathrm{ij}} = \Sigma_{\mathrm{k \neq i,j}} \mathrm{f_c}(|\mathrm{R_i - R_k}|)\mathrm{g(\theta_{ijk})} \tag{6}
$$

$$
\mathrm{g(\theta_{ijk})} = 1 + \mathrm{c} \left\{1 - 1/\left[1 + \mathrm{d(h - \cos \theta_{ijk})^2}\right]\right\} \tag{7}
$$

In Equations 3-7, A, $\beta_1$, B, $\beta_2$, $\beta$, $\chi$, n, c, d, and h are the adjustable parameters and $\theta_{ijk}$ is the angle between the bonds i-j and i-k.

Below we will describe a BO potential which, though based on the Tersoff ideology, uses functions that are different from Tersoff's, making the method applicable to transition metals.

### 3. The bond-order potential for Fe

We preserve the Tersoff expression for the total energy:

$$
\mathrm{E} = 1/2\Sigma_{\mathrm{i \neq j}} \mathrm{f_c(R_i - R_j)} \left[\mathrm{V_{rep}(R_i - R_j)} + \mathrm{V_{bo}(R_i, R_j)}\right] \tag{1a}
$$

The repulsion part, $\mathrm{V_{rep}(R_i - R_j)}$, has been modified to allow for a strong repulsion at the distances which are smaller than half the nearest neighbor distance in the BCC lattice, $\mathrm{R_0}$:

$$
\mathrm{V_{rep}(R)} = \mathrm{A} \exp(-\beta_1|\mathrm{R}| + \beta_4(0.5\mathrm{R_0/R})^\alpha) \tag{3a}
$$

The attractive BO part of the energy is also preserved:

$$
\mathrm{V_{bo}(R_i, R_j)} = -\mathrm{B} \exp(-\beta_2|\mathrm{R_i - R_j}|)\mathrm{b(R_i, R_j)}. \tag{4a}
$$

However, $\mathrm{b(R_i, R_j)}$ is now

$$
\mathrm{b(R_i, R_j)} = \zeta_{\mathrm{ij}}^{\mathrm{f}} \left(1 + \gamma_1 \zeta_{\mathrm{ij}} + \gamma_2 \zeta_{\mathrm{ij}}^2 + \gamma_3 \zeta_{\mathrm{ij}}^3 + \gamma_4 \zeta_{\mathrm{ij}}^4 + \gamma_5 \zeta_{\mathrm{ij}}^{5+} \gamma_6 \zeta_{\mathrm{ij}}^6\right) \tag{5a}
$$

where

$$
\zeta_{\mathrm{ij}} = \Sigma_{\mathrm{k \neq i,j}} \mathrm{f_c} \left(|\mathrm{R_i - R_k}|\right) \exp \left(-\beta_3|\mathrm{R_i - R_k}|^{\mathrm{nz}}\right) \mathrm{g} \left(\theta_{\mathrm{ijk}}\right) \tag{6a}
$$

(we use the same cut-off function $\mathrm{f_c}$, Equation 2, with the cut-off radii $\mathrm{r_{c1}}$ and $\mathrm{r_{c2}}$ between the second and third coordination spheres; see Table 2 below), and

$$
\mathrm{g} \left(\theta_{\mathrm{ijk}}\right) = 1 + \mathrm{c} \left\{1 - \beta/\left[1 + \mathrm{d} \left(\mathrm{h}^2 - \cos \theta_{\mathrm{ijk}}^2\right)^2\right]\right\}^{(2\delta)} \tag{7a}
$$

Since the Tersoff form of function $\mathrm{b(R_i, R_j)}$ was quite arbitrary, with the only requirement of 'correct' (reciprocal square root) behavior at large $\zeta$, we decided to try a more general form. The exponent, f, was allowed to take both positive and negative values.

The adjustable parameters: A, $\beta_1$, B, $\beta_2$, $\beta_3$, $\beta$, c, d, $\delta$, h, $\gamma_1$, ... $\gamma_6$, were chosen from the following conditions.

<table><caption>Table 1. Experimental and fitted properties of Fe</caption>
<thead>
<tr>
<th>
</th>
<th>Exp.
</th>
<th>Calc.
</th>
</tr>
</thead>
<tbody>
<tr>
<th>BCC
</th>
<td>
</td>
<td>
</td>
</tr>
<tr>
<th>a
</th>
<td>2.8589
</td>
<td>2.8589
</td>
</tr>
<tr>
<th>$\Omega_0$
</th>
<td>11.6833
</td>
<td>11.6833
</td>
</tr>
<tr>
<th>$E_{\text{coh}}$
</th>
<td>$-4.28$
</td>
<td>$-4.28$
</td>
</tr>
<tr>
<th>($\text{E}_{\text{rep}} = 2.1151\ \text{E}_{\text{bo}} = -6.3952$)
</th>
<td>
</td>
<td>
</td>
</tr>
<tr>
<th>C11
</th>
<td>2.4310
</td>
<td>2.3675
</td>
</tr>
<tr>
<th>C12
</th>
<td>1.3810
</td>
<td>1.3191
</td>
</tr>
<tr>
<th>C44
</th>
<td>1.2190
</td>
<td>1.2190
</td>
</tr>
<tr>
<th>C′
</th>
<td>0.5250
</td>
<td>0.5242
</td>
</tr>
<tr>
<th>K
</th>
<td>1.7310
</td>
<td>1.6686
</td>
</tr>
<tr>
<th>$\text{E}_{\text{surf(111)}}^\text{a}$
</th>
<td>2.5
</td>
<td>2.2439
</td>
</tr>
<tr>
<th>$\text{FCC}\ (\Omega_0 = 11.152)^\text{b}$
</th>
<td>
</td>
<td>
</td>
</tr>
<tr>
<th>$E_{\text{coh}}$
</th>
<td>$-4.223$
</td>
<td>$-4.2229$
</td>
</tr>
<tr>
<th>($\text{E}_{\text{rep}} = 2.4019\ \text{E}_{\text{bo}} = -6.6249$)
</th>
<td>
</td>
<td>
</td>
</tr>
<tr>
<th>$\text{HCP}\ (\Omega_0 = 10.398)^\text{c}$
</th>
<td>
</td>
<td>
</td>
</tr>
<tr>
<th>$E_{\text{coh}}$
</th>
<td>$-4.213$
</td>
<td>$-4.2134$
</td>
</tr>
<tr>
<th>($\text{E}_{\text{rep}} = 2.9406\ \text{E}_{\text{bo}} = -7.1540$)
</th>
<td>
</td>
<td>
</td>
</tr>
</tbody>
</table>

Energies in eV, distances in $\mathring{\text{A}}$, atomic volumes in $\mathring{\text{A}}^3$, elastic moduli in $10^2$ GPA, surface energy in eV/surface atom.
$^\text{a}$Estimated based on ab initio calculations [10].
$^\text{b}$The atomic volume and energies as found from experiments on high-temperature BCC-FCC polymorphic transformation [22].
$^\text{c}$The atomic volume and energy at the point of BCC-HCP phase transformation (130 kbar) [23].

A and B were found (at fixed values of the other parameters) from two linear equations for the cohesive energy in BCC modification, $E_{\text{coh}}$, at the experimental equilibrium volume $\Omega_0$, and the pressure $\text{P} = 0$ at $\Omega_0$. These equations were solved exactly in an analytical form.

Then the multi-variate minimization procedure (IMSL routine DUMINF) was used. We minimized the rms deviation of the calculated energy from that according to the Smith–Banerjia universal scaling law [21].

The other conditions to be imposed on the adjustable parameters were:

– The calculated elastic moduli C′ and $\text{C}_{44}$ had to be as close as possible to their experimental values in the BCC lattice (the bulk modulus K would be automatically close to its experimental value if the rms universal scaling minimization has been achieved);

– The calculated energies of FCC and HCP modifications at the corresponding volumes had to be as close as possible to the corresponding experimental energies for FCC and HCP lattices.

– The calculated (111) free surface energy for the BCC lattice had to be as close as possible to the corresponding experimental or ab initio value.

![](./images/812433149534404609_2.jpg)

Figure 1. Comparison of the calculated volume dependence of the cohesive energy curve (E), with the Universal Scaling energies (Eus).

The above three conditions were fulfilled by making use of five punishment functions, equal to 1 if the experimental and calculated quantities to be fitted are exactly equal, otherwise growing as a factor times the corresponding quadratic deviation. By changing the values assigned to the factors, the minimization process could be directed towards damping down the undesirable deviation.

Parameter nz, which enters the expressions for the total energy, was set by trial-and-error tests: $nz = 6$. At present we 'switched off' the short range repulsion: $\beta_4 = 0$. In the future, a more appropriate choice of the value for $\beta_4$ will be accepted. However, a strong increase of the short-range repulsion practically will not affect the energy at physically reasonable distances but may be important in molecular dynamics simulations to prevent unphysical particle configurations from occurring.

Tables 1 and 2 present the results of the parameter optimization. One can see from Table 1 that the new potential reproduces the elastic moduli with very high precision. It is well known that $C_{44}$ is especially sensitive to directional bonding and is not reproduced well by the traditional EAM. One can also see that the energies of FCC and HCP are discriminated very well.

Figures 1 through 3 illustrate some of the results of the parameter fitting. Figure 1 shows the total energy as a function of the volume ratio $\Omega/\Omega_0^{BCC}$ ($\Omega_0^{BCC}$ is the atomic volume of BCC Fe at equilibrium) as compared to the Universal Scaling curve, Equation 14.

Figure 2 compares the calculated volume-pressure equation of state $\Omega/\Omega_0^{BCC}(P)$ with experimental data. One can see that the agreement is excellent.

As was mentioned above, fitting the energies of FCC and HCP phases of Fe was part of the procedure of the potential calibration. The HCP experimental energy was estimated from the enthalpy at the point of BCC-HCP phase transformation under pressure at 130 kbar. Figure 3 shows the enthalpies of BCC and HCP phases as functions of pressure. One can see that the phase transformation occurs at $P = 110$ kbar. This should be considered as a reasonable agreement with the experimental value of 130 kbar.

![](./images/812433149534404609_3.jpg)

Figure 2. The calculated equation of states for BCC Fe.

<table><tbody><tr><td colspan="2">Table 2. Parameters of the potential</td></tr><tr><td colspan="2">$\mathbf{V_{rep}=Aexp(-\beta_1|R|+\beta_4(R/0.5R_0)^\alpha)}$</td></tr><tr><td></td><td>$\mathrm{A}=0.2346154 \mathrm{E}+04$</td></tr><tr><td></td><td>$\beta_1=0.3465077E + 01; \beta_4=0; \alpha=0.$</td></tr><tr><td colspan="2">$\mathbf{V_{bo}(R_i,R_j)=-Bexp(-\beta_2|R_{ij}|)b(R_i.R_j)}$</td></tr><tr><td></td><td>$\mathrm{B}=0.1580257 \mathrm{E}-04$</td></tr><tr><td></td><td>$\beta_2=0.1117197E + 01$</td></tr><tr><td colspan="2">$\mathbf{b=\zeta^f(1+\gamma_1\zeta+...\gamma_6\zeta^6)}$</td></tr><tr><td></td><td>$\mathrm{f}=0.4534376 \mathrm{E}+00$</td></tr><tr><td></td><td>$\gamma_1=0.3718635E + 03$</td></tr><tr><td></td><td>$\gamma_2=0.1664427E + 04$</td></tr><tr><td></td><td>$\gamma_3=-0.6539821E + 02$</td></tr><tr><td></td><td>$\gamma_4=0.9013512E + 00$</td></tr><tr><td></td><td>$\gamma_5=-0.1142012E - 01$</td></tr><tr><td></td><td>$\gamma_6=0.1385744E - 03$</td></tr><tr><td colspan="2">$\mathbf{\zeta=\Sigma f_c(|R_{ik}|)exp(-\beta_3|R_{ik}|^{nz})g(\theta_{ijk})}$</td></tr><tr><td></td><td>$\mathbf{f_c}$ (Equation 5): Cut-off radii:</td></tr><tr><td></td><td>$\mathrm{r_{c1}}=3.70, \mathrm{r_{c2}}=3.60$</td></tr><tr><td></td><td>$\mathrm{nz}=6, \beta_3=0.6034363 \mathrm{E}+00$</td></tr><tr><td colspan="2">$\mathbf{g=1+c\{1-\beta/[1+d(h^2-\cos\theta^2)^2]\}^{(2\delta)}}$</td></tr><tr><td></td><td>$\beta=0.9433671E + 00$</td></tr><tr><td></td><td>$\delta=0.9870393E + 00$</td></tr><tr><td></td><td>$\mathrm{c}=0.4199031 \mathrm{E}+01$</td></tr><tr><td></td><td>$\mathrm{d}=0.3752465 \mathrm{E}+02$</td></tr><tr><td></td><td>$\mathrm{h}=0.6915982 \mathrm{E}+00$</td></tr></tbody></table>

![](./images/812433149534404609_4.jpg)

Figure 3. The BCC-HCP phase transformation under pressure.

## 4. Conclusions

We have developed a semi-empirical BO potential for Fe. The preliminary results look encouraging. Although some further testing, and, possibly, further readjustment of the potential parameters may be needed, one may hope that the new potential will be instrumental in atomistic simulations of both deformation processes in Fe and chemisorption reactions on Fe surfaces.

As was mentioned in the Introduction, recently a method of explicitly calculating ferromagnetic contributions to the total energy in Fe based on the Stoner model of itinerant ferromagnetism was suggested [19]. If successful, this method may become an ultimate tool for atomistic simulations in Fe. While the detailed implementation and testing of this method are still in the future, the new BO potential will enable one to obtain valuable information on some important processes in Fe. A BO potential of the same type will also be used in the Stoner model method for evaluating the non-magnetic contributions to the total energy.

## References

1. Mao, H.K. et al., Nature, 398 (1998) 741.
2. Wirth, B.D., Odette, G.R., Marvudas, D. and Lukas, G.E., J. Nucl. Mater., 244 (1997) 185.
3. Olson, G.B., In Olson, G.B., Azrin, M. and Wright, E.S. (Eds.) Innovation in Ultra-Strength Steel Technology, Proceedings of the 34th Sagamore Conference, Aug. 30-Sept. 3, 1987, p. 3.
4. Soderling, P., Moriarty, J.A. and Willis, J.M., Phys. Rev. B, 53 (1996) 14063.
5. a. Krasko, G.L., Phys. Rev. B, 36 (1987) 8565.
    b. Krasko, G.L., Solid State Commun., 12 (1989) 1099.
    c. Krasko, G.L. and Olson, G.B., Phys. Rev. B, 40 (1989) 11536.
6. Eckman, M., Sadigh, B., Einaradotter, K. and Blaha, P., Phys. Rev. B, 58 (1998) 5296.
7. Sob, M., Friar, M., Wang, L.G. and Vitek, V., In Diaz de la Rubia, T., Kaxiras, T., Bulatov, V., Ghoniem, N.M. and Phillips, R. (Eds.) Multiscale Modeling of Materials, MRS Symp. Proc., V. 538, MRS, Pittsburgh, PA 1999 (to be published).
8. a. Krasko, G.L. and Olson, G.B., Solid State Commun., 76 (1990) 247.
    b. Krasko, G.L. and Olson, G.B., Solid State Commun., 79 (1991) 113.

9.  a. Wu, R., Freeman, A.J. and Olson, G.B., Phys. Rev. B, 50 (1994) 75.
    b. Wu, R., Freeman, A.J. and Olson, G.B., Phys. Rev. B, 53 (1996) 1.
    c. Wu, R., Freeman, A.J. and Olson, G.B., Science, 265 (1994) 376.

10. a. Wu, R. and Freeman, A.J., Phys. Rev. B, 47 (1993) 3904.
    b. Wu, R. and Freeman, A.J., Phys. Rev. B, 47 (1993) 6855.

11. Krasko, G.L., Wang, L.G., Chabalowsky, C., Hurley, M. and Rice, B., to be published.

12. a. Baskes, M.I., Daw, M.S., Dodson, B. and Foils, S.M., MRS Bull., XIII (1988) 28.
    b. Daw, M.S. and Baskes, M.I., Phys. Rev. B, 29 (1984) 6443.
    c. Foils, S.M., Baskes, M.I. and Daw, M.S., Phys. Rev. B, 33 (1986) 7983.
    d. Daw, M.S., Phys. Rev. B, 39 (1989) 7441.

13. Finnis, M.W. and Sinclair, J.E., Phil. Mag. A, 50 (1984) 45. Errata: Phil. Mag. A, 53 (1986) 161.

14. Simonelly, G., Pasianot, R. and Savino, E.J., Phys. State Sol. B, 191 (1995) 249.

15. a. Carlsson, A.E., In Ehrenreich, H. and Turnbull, D. (Eds.) Solid State Physics, Vol. 43, p. 1.
    b. Carlsson, A.E., Phys. Rev. B, 44 (1991) 6590.

16. a. Horsfield, A.P., Bratkovsky, A.M., Fern, M., Pettifor, D.G. and Aoki, M., Phys. Rev. B, 53 (1996) 12694.
    b. Horsfield, A.P., Phil. Mag. B, 73 (1996) 85.
    c. Aoki, M., Horsfield, A. and Pettifor, D.G., J. Phase Equilib., 18 (1997) 614.

17. a. Tersoff, J., Phys. Rev. Lett., 61 (1988) 2879.
    b. Tersoff, J., Phys. Rev. B, 37 (1988) 6991.
    c. Tersoff, J., Phys. Rev. B, 38 (1988) 9902.
    d. Tersoff, J., Phys. Rev. B, 39 (1989) 5566.

18. a. Tang, M. and Yip, S., Phys. Rev. Lett., 75 (1995) 2748.
    b. Tang, M. and Yip, S., Phys. Rev. B, 52 (1995) 15150.

19. a. Krasko, G.L., J. Appl. Phys., 79 (1996) 4682.
    b. Shibutani, Y., Krasko, G.L., Sob, M. and Yip, S., Mater. Sci. Res. Int., to be published.

20. Balamante, H., Halicioglu, T. and Tiller, W.A., Phys. Rev. B, 46 (1992) 2250.

21. Banerjea, A. and Smith, J.R., Phys. Rev. B, 37 (1988) 6632.

22. Bendick, W. and Pepperhoff, W., Acta Met., 30 (1982) 679.

23. Giles, P.M., Longenbach, M.H. and Marder, A.R., J. Appl. Phys., 42 (1971) 4290.

24. Clendener, R.L. and Drickamer, H.D., J. Phys. Chem. Solids, 25 (1964) 865.