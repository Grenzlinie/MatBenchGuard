# Possible High-Temperature Superconductivity in Hygrogenated Fluorine

D. A. Papaconstantopoulos¹

¹Department of Computational and Data Sciences,
George Mason University, Fairfax, Virginia 22030, USA*

Recent computational studies confirmed by experiment have established the occurrence of superconducting temperatures, $T_c$, near 200 K when the pressure is close to 200 GPa in the compound H₃S. Motivated by these findings we investigate in this work the possibility of discovering high-temperature superconductivity in the material H₃F. We performed linearized augmented plane wave(LAPW) calculations followed by the determination of the angular momentum components of the density of states, the scattering phase shifts at the Fermi level and the electron-ion matrix element known as the Hopfield parameter. Our calculated Hopfield parameters are much larger than those found in H₃S suggesting that they may lead to large electron-phonon coupling constant and hence a large Tc similar or even larger than that of H₃S. However, calculations of elastic constants are inconclusive regarding the stability of this material.

PACS numbers: 74.20.Fg, 74.10.-v, 74.20.Pq, 74.62.Bf

## I. INTRODUCTION

Back in the late sixties, Ashcroft¹ made the bold prediction of room temperature superconductivity in metallic hydrogen under very high pressures. Later in the seventies, a quantitative evaluation of the electron-phonon (e-p) coupling²,³ using the Gaspari-Gyorffy-McMillan (GGM) theories⁴,⁵ supported Ashcroft's ideas. In Ref. 2 an e-p coupling $\lambda = 1.86$ gave a superconducting transition temperature $T_c = 234$ K at an estimated pressure of 4.6 Mbar.

The ideas of Ashcroft have been recently confirmed by the experiments of Drozdov et al.⁶ and a series of theoretical papers⁷⁻¹⁴ that confirm hydrogen-based high-temperature superconductivity is realized in the sulfur compound H₃S under 200 GPa pressure. Reference 8 presents a comprehensive set of calculations for H₃S using the GGM theory. In a subsequent paper (Ref.15), we extended the work of Ref.8 studying substitutions of S by Si, P, and Cl in the framework of the virtual crystal approximation. In the present paper we pursue another study in this class of hydrides by substituting S by F. So we have performed band structure and total energy calculations using the linearized augmented plane wave(LAPW) method. The resulting angular-momentum components of the densities of states (DOS) at the Fermi level ($E_f$) and the phase shifts obtained from the computed band structure potentials are the input to the GGM theory for the evaluation of the Hopfield parameter ($\eta$).

## II. COMPUTATIONAL DETAILS

We have applied the LAPW code developed at NRL¹⁶,¹⁷, using the Hedin-Lunqvist form of exchange and correlation, to calculate the band structure and total energy of the H₃F and H₂F systems in the Im$\overline{3}$m and Fluorite crystal structures respectively. The total energy minimization was done using the third-order Birch equation¹⁸. The total and angular momentum decomposition densities of electronic states were obtained by the tetrahedron method using LAPW results on a $k$-point uniformly distributed grid of 1785 k-points and 505 k-points for the respective irreducible Brillouin zones to ensure very accurate convergence. Subsequently, we applied the Gaspari-Gyorffy (GG) formula to obtain the parameter $\eta$, then the Allen-Dynes modification¹⁹ of the McMillan equation to determine $T_c$. The main steps here are to determine the electron-phonon coupling constant $\lambda_j$ given by McMillan⁵ as

$$
\lambda_j = \frac{N(E_f)\langle I_j^2\rangle}{M_j\langle\omega_j^2\rangle} \equiv \frac{\eta_j}{M_j\langle\omega_j^2\rangle} \tag{1}
$$

where $N(E_f)$ is the total DOS per spin at $E_f$, $< I_j^2 >$ is the electron-ion matrix element, $< \omega_j^2 >$ is the average phonon frequency and the index $j$ corresponds to hydrogen and fluorine. The Hopfield parameter $\eta_j$ for the two components is computed by the GG formula shown below:

$$
\eta_j = \frac{1}{N(E_f)} \sum_{l=0}^{2} 2(l+1)\sin^2(\delta_l^j - \delta_{(l+1)}^j)v_l^j v_{(l+1)}^j \tag{2}
$$

where $\delta_l^j$ is the scattering phase shift for the $j$-th atom, the sum of which is related to the deformation potential, and $v_l^j = N_l^j(E_f)/N_l^{j(1)}$ is the ratio of the $l$-th partial DOS of the $j$-th atom to $N^{(1)}$, the free scatterer DOS, for

the given atomic potential in a homogeneous system.The phase shifts $\delta_{l}^{j}$ are calculated using the following expression:

$$
\tan \delta_{l}^{j}\left(R_{s}, E\right)=\frac{j_{l}^{\prime}\left(k R_{s}\right)-j_{l}\left(k R_{s}\right) L_{l}\left(R_{s}, E\right)}{n_{l}^{\prime}\left(k R_{s}\right)-n_{l}\left(k R_{s}\right) L_{l}\left(R_{s}, E\right)} \tag{3}
$$

where $L_{l}=\frac{u_{l}^{\prime}}{u_{l}}$ is the logarithmic derivative.

The free scatterer DOS is defined as

$$
N_{l}^{j(1)}=(2 l+1) \int_{0}^{R_{s}}\left[u_{l}^{j}\left(r, E_{f}\right)\right]^{2} r^{2} d r \tag{4}
$$

where $u_{l}$ is the radial wave function and the upper limit of the integral is the muffin-tin radius $R_{s}$. In previous works, equations (2) and (3) contain multiplying factors of $E_{f} / \pi^{2}$ and $\sqrt{E_{f}} / \pi$, respectively. But by examining these equations it is easy to see that these factors cancel out.

Finally, we use the Allen-Dynes equation to determine the superconducting transition temperature $T_{c}$ as follows:

$$
T_{c}=f_{1} f_{2} \frac{\omega_{\log }}{1.2} \exp \left[-\frac{1.04(1+\lambda)}{\lambda-\mu^{*}(1+0.62 \lambda)}\right] \tag{5}
$$

In Eq. (4) we have set the Coulomb pseudopotential $\mu^{*}=$ 0.1 and $f_{2}=1$. $f_{1}$ is the strong coupling factor given by

$$
f_{1}=\left[1+\left(\frac{\lambda}{2.46+9.35 \mu^{*}}\right)^{1.5}\right]^{1 / 3}. \tag{6}
$$

It turns out for this material, $f_{1}$ can provide an additional $10 \%$ enhancement to $T_{c}$. We have used the values for $\omega_{\log }$ and $\langle\omega_{j}^{2}\rangle$ found in Ref. 8 from the analysis of the results of Duan *et al.* (Ref. 7). Our choice of $\mu^{*}=0.1$ can be justified by the empirical formula proposed by Bennemann and Garland$^{20}$.

## III. RESULTS

In Fig. 1 we show the Pressure v. Volume relationships found from the Birch fit for the $\mathrm{H}_{3} \mathrm{~S}$ and $\mathrm{H}_{3} \mathrm{~F}$ compounds. It is worth noting that there is a significant difference between the two graphs showing that the $\mathrm{H}_{3} \mathrm{~S}$ reaches the pressure of 200 GPa at much higher volume than in $\mathrm{H}_{3} \mathrm{~F}$. So at $V=87.8$ (lattice constant $=5.6$ Bohr) the pressure is around 210 GPa in $\mathrm{H}_{3} \mathrm{~S}$ while at the same volume $\mathrm{H}_{3} \mathrm{~F}$ reaches a pressure of only 82 GPa. This suggests that $\mathrm{H}_{3} \mathrm{~F}$ might reach high superconducting temperature at much lower pressure than $\mathrm{H}_{3} \mathrm{~S}$.

![](./images/867768207736308624_1.jpg)

FIG. 1: Pressure v. Volume relationships for $\mathrm{H}_{3} \mathrm{~S}$ and $\mathrm{H}_{3} \mathrm{~F}$.

Fig. 2 displays the energy bands of $\mathrm{H}_{3} \mathrm{~F}$ in the bcc-like $\mathrm{Im} \overline{3} \mathrm{~m}$ structure for lattice constant $a=5.6$ Bohr $(P=82$ GPa). We note that the low energy band near -1.0 Ry is almost 100 per cent of s-like fluorine character. At the Fermi level, $E_{f}$, at about 0.9 Ry the bands consist of 70 per cent p-like fluorine character ,22 per cent hydrogen s-like, 5 per cent fluorine s-like and 3 per cent fluorine d-like. Our Birch fit found that P=0 corresponds to a lattice constant of 6.33 Bohr.

![](./images/867768207736308624_2.jpg)

FIG. 2: Energy bands of $\mathrm{H}_{3} \mathrm{~F}$ for lattice constant $a=5.6$ Bohr $(P=82$ GPa).

In Fig. 3 we present the total and angular momentum and site-decomposed(DOS) for $\mathrm{H}_{3} \mathrm{~F}$ in the $\mathrm{Im} \overline{3} \mathrm{~m}$ structure for lattice constant $a=5.6$ Bohr . We note the narrow s-like fluorine dominated peak at -1.0 Ry. This is followed by a gap of about 1 Ry where two fluorine dominated p-like peaks appear. Then at an energy of 0.5 Ry a tiny gap is found which is followed by another two peaks with both fluorine p-like and hydrogen s-like contributions. In the middle of the latter two peaks $E_{f}$ is found. The $N(E_{f})$ is decomposed as discussed above in the description of the bands. It is important to state here that the overall features of the DOS shown in Fig. 3 are very different from those calculated by many groups for $\mathrm{H}_{3} \mathrm{~S}$. But at $E_{f}$ both the DOS values and the per site decomposition are very similar.

In Fig. 4 we show the values of the Hopfield parameter $\eta$ comparing $\mathrm{H}_{3} \mathrm{~F}$ to $\mathrm{H}_{3} \mathrm{~S}$. The results shown in this figure establish a dramatic increase of the fluorine component of

![](./images/867768207736308624_3.jpg)

FIG. 3: Total and angular momentum-decomposed DOS for H₃F. Although this DOS has a different overall shape than that of H₃S, it turns out that at the Fermi level both the actual values and the decomposition are very similar between the two compounds

η in H₃F over the corresponding value of the sulfur component in H₃S while the hydrogen component is comparable to that in H₃S. More specifically from Fig. 4 we can see that at $P = 128$ GPa (lattice constant $a = 5.4$ Bohr) and for $P = 82$ GPA (lattice constant $a = 5.6$), the corresponding values of the $\eta$ fluorine are $17.5\ \mathrm{eV/\mathring{A}^2}$ and $13.9\ \mathrm{eV/\mathring{A}^2}$ respectively. As can be seen from the figure these values are almost a factor of three larger than those of both the sulfur and hydrogen components in H₃S which are actually achieved at higher pressures. This large increase of the parameter $\eta$ in H₃F is a signal that we should be looking for a high superconducting transition temperature in this compound if it can be synthesized.

![](./images/867768207736308624_4.jpg)

FIG. 4: Comparison of the Hopfield parameters $\eta$ as a function of pressure for H₃F and H₃S. Note that the values for the hydrogen components have been multiplied by three.

However, in order to obtain a quantitative prediction of the transition temperaturerge $T_c$, a large value of the Hopfield parameter is not a sufficient condition. It is necessary to estimate the force constants $(M\omega^2)_j$ so that values for the electron-phonon coupling constants $\lambda$ can be obtained. Using our previous analysis⁸ for pure H₃S and the results of Duan et al.⁷, we derived the following values of the averaged phonon frequencies in H₃S: $\langle\omega\rangle_S = 615$K, $\langle\omega\rangle_H = 1840$ K, and $\omega_{\log} = 1560$K. Now we assume that the $M\omega^2$ of H (optic mode) to be nearly the same as in H₃S. We then estimate the $M\omega^2$ of the fluorine site by scaling the H₃S results by the fluorine mass also introducing a volume dependence by considering the square of the phonon frequency as proportional to the bulk modulus $B$. Hence, as shown in (Eq.1), by dividing our calculated parameters $\eta$ by the above estimated values of the force constants we obtain an estimate of $\lambda$ which is shown as a function of pressure in Fig. 5.

![](./images/867768207736308624_5.jpg)

FIG. 5: Comparison of the electron-phonon coupling constants $\lambda$ as a function of pressure for H₃F and H₃S

Finally, using the Allen-Dynes equation (Eq.5) we calculated the superconducting transition temperature $T_c$. This estimate of $T_c$ for H₃F together with that of H₃S are shown in Fig. 6. It is interesting that for the fluorine compound we predict transition temperature well over 200K for a pressure of only about 130 GPa.

![](./images/867768207736308624_6.jpg)

FIG. 6: Comparison of the superconducting transition temperature $T_c$ as a function of pressure for H₃F and H₃S

### IV. FURTHER DISCUSSION

We now proceed with further analysis of our results. The main result of our calculation is the finding that the fluorine component of the Hopfield parameter $\eta$ is very large in H₃F (see Fig. 4). This is due to the very large contribution from the pd channel of F in the GG formula (Eq.3),which has the value of $13.7\ \mathrm{eV/\mathring{A}^2}$ and $11.3\ \mathrm{eV/\mathring{A}^2}$

for a=5.4 a.u. and a=5.6a.u.respectively. It is worth noting in $H_3F$ the hydrogen component of $\eta$ is much smaller than in $H_3S$. In summarizing the situation we recognize that while our $\eta$ calculations are reliable, our estimates of the force constants are less reliable since we have not calculated the phonon frequencies from first principles. Nevertheless, the large values of $\eta$ are very intriguing especially since they are not due to large value of N(Ef) which has modest values of less than 7 states/Ry. Further support for the large $\eta$ is found from a calculation we performed in the Fluorite structure compound $H_2F$ where we find even larger values of $\eta$ exceeding $27\ eV/\AA^2$. Therefore, it becomes important to check the stability of $H_3F$ by calculating the elastic constants c11-c12 and c44. We performed such calculations for the lattice constants a=5.4 a.u. and a=5.6 a.u which correspond to the highest pressures we considered. The results are shown in Fig. 7 which depicts the energy versus the square of the distortion for c44 and c11-12.

![](./images/867768207736308624_7.jpg)

FIG. 7: (a) Energy v. Distortion Squared for a=5.4 and c44 (b) Energy v. Distortion Squared for a=5.6 and c44 and (c) Energy v. Distortion Squared for c11-c12

It appears that the slope for c11-c12 has a small negative value suggesting an instability. So this result casts a doubt as to whether the $H_3F$ can be a superconductor in the bcc-like structure. However, the unusually large values of the Hopfield parameter in the H-F system warrants further investigation in other crystal structures.

## V. CONCLUSION

We emphasize that using the results of band structure calculations and application of the GGM theory, the main conclusion of this work is that $H_3F$ has a very large value of the fluorine component of the Hopfield parameter. This is due to the very large electron-ion matrix element $< I_f^2 >$ on the fluorine site, and not to the $N(E_f)$, which has a modest value similar to that in $H_3S$. However, due to an instability in the calculated elastic constant c11-c12 in the $Im\overline{3}m$ structure further studies are needed for other crystal structures to verify the present prediction.

## VI. ACKNOWLEDGMENTS

I acknowledge many useful discussions with Michael J. Mehl. This work was partially supported by DOE grant de-sc0014337.

* dpapacon@gmu.edu

1 N. W. Ashcroft, Phys. Rev. Lett. **21**, 1748 (1968).

2 D. A. Papaconstantopoulos and B. M. Klein, Ferroelectrics **16**, 307 (1977), http://dx.doi.org/10.1080/00150197708237185.

3 D. A. Papaconstantopoulos, L. L. Boyer, B. M. Klein, A. R. Williams, V. L. Morruzzi, and J. F. Janak, Phys. Rev. B **15**, 4221 (1977).

4 G. D. Gaspari and B. L. Gyorffy, Phys. Rev. Lett. **28**, 801 (1972).

5 W. L. McMillan, Phys. Rev. **167**, 331 (1968).

6 A. P. Drozdov, M. I. Eremets, I. A. Troyan, V. Ksenofontov, and S. I. Shylin, Nature **525**, 73 (2015), ISSN 0028-0836, letter.

7 D. Duan, Y. Liu, F. Tian, D. Li, X. Huang, Z. Zhao, H. Yu, B. Liu, W. Tian, and T. Cui, Scientific Reports **4**, 6968 (2014).

8 D. Papaconstantopoulos, B. M. Klein, M. J. Mehl, and W. E. Pickett, Phys. Rev. B **91**, 184511 (2015).

9 N. Bernstein, C. S. Hellberg, M. D. Johannes, I. I. Mazin, and M. J. Mehl, Phys. Rev. B **91**, 060511 (2015).

10 I. Errea, M. Calandra, C. J. Pickard, J. Nelson, R. J. Needs, Y. Li, H. Liu, Y. Zhang, Y. Ma, and F. Mauri, Phys. Rev. Lett. **114**, 157004 (2015).

11 J. A. Flores-Livas, A. Sanna, and E. K. U. Gross, The European Physical Journal B89 (3), 1-6.

12 Y. Quan and W. E. Pickett, Phys. Rev. B **93**, 104526 (2016).

13 Y. Li, J. Hao, H. Liu, Y. Li, and Y. Ma, J. Chem. Phys **140**, 174712 (2014).

14 A. Bianconi and T. Jarlborg, Novel Superconducting Materials, Vol 1, Issue 1, Issue1, ISSN (Online) 2299-3193.

15 F. Fan, D.A. Papaconstantopoulos, M.J. Mehl, and B.M. Klein, Journal of Physics and Chemistry of Solids, 99, 105-110 (2016).

16 D. J. Singh, *Plane waves, pseudopotentials, and the LAPW Method* (Kluwer Academic Publishers, Boston, 1994).

17 The NRL LAPW code, originally developed by H. Krakauer and D. J. Singh, was used with Hedin-Lundqvist exchange-correlation. DOS results were generated from 1785 k points in the irreducible Brillouin zone with the tetrahedron method. Total energies were fit to the Birch equation to obtain the P(V) equation of state.

18 F. Birch, Journal of Geophysical Research: Solid Earth **83**, 1257 (1978), ISSN 2156-2202.

19 P. B. Allen and R. C. Dynes, Phys. Rev. B **12**, 905 (1975).

20 K. H. Bennemann and J. W. Garland,AIP Conf. Proc. 4,103 (1972).