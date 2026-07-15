PHYSICAL REVIEW B 69, 155112 (2004)

# Long-range contribution to the exchange-correlation kernel of time-dependent density functional theory

Silvana Botti, Francesco Sottile, Nathalie Vast, Valerio Olevano, and Lucia Reining
Laboratoire des Solides Irradiés, CNRS-CEA, École Polytechnique, F-91128 Palaiseau, France

Hans-Christian Weissker
Institut für Festkörpertieorie und Theoretische Optik, Friedrich-Schiller-Universität, D-07743 Jena, Germany

Angel Rubio
Departamento de Física de Materiales, Facultad de Ciencias Químicas, Universidad del Pais Vasco,
Donostia International Physics Center (DIPC) and Centro Mixto CSIC-UPV/EHU, Donostia, E-20018 San Sebastián, Basque Country, Spain

Giovanni Onida
Istituto Nazionale per la Fisica della Materia, Dipartimento di Fisica dell'Università di Milano, via Celoria 16, I-20133 Milano, Italy

Rodolfo Del Sole
Istituto Nazionale per la Fisica della Materia, Dipartimento di Fisica dell'Università di Roma "Tor Vergata," via della Ricerca Scientifica, I-00133 Roma, Italy

R. W. Godby
Department of Physics, University of York, Heslington, York YO10 5DD, United Kingdom

(Received 1 December 2003; revised manuscript received 6 February 2004; published 23 April 2004)

We discuss the effects of a static long-range contribution $-\alpha/q^{2}$ to the exchange-correlation kernel $f_{xc}(\mathbf{q})$ of time-dependent density functional theory. We show that the optical absorption spectrum of solids exhibiting a strong continuum excitonic effect is considerably improved with respect to calculations where the adiabatic local-density approximation is used. We discuss the limitations of this simple approach, and in particular that the same improvement cannot be found for the whole spectral range including the valence plasmons and bound excitons. On the other hand, we also show that within the range of validity of the method, the parameter $\alpha$ depends linearly on the inverse of the dielectric constant, and we demonstrate that this fact can be used to predict continuum excitonic effects in semiconductors. Results are shown for the real and imaginary part of the dielectric function of Si, GaAs, AlAs, diamond, MgO, SiC and Ge, and for the loss function of Si.

DOI: 10.1103/PhysRevB.69.155112
PACS number(s): 71.10.-w, 78.20.Bh, 71.35.-y, 71.15.Qe

The calculation of the electronic properties of many-electron systems is still a formidable task. A very efficient approach to the calculation of ground-state properties is the density functional theory (DFT) (Ref. 1), since all quantities to be calculated depend only on the electronic density and not explicitly on the many-body wave function, which considerably reduces the number of degrees of freedom that have to be considered. DFT is most often used within the Kohn-Sham (KS) approach, $^{2}$ where one solves an effective one-particle Schrödinger equation that contains the kinetic-energy operator, the external and the Hartree potentials, and the so-called exchange-correlation (xc) potential $v_{xc}$. The exact functional dependence of the latter contribution on the density is in general not known, but good approximations exist, like, e.g., the widely used local-density approximation (LDA). $^{2}$ Therefore, DFT ground state calculations are today well established for a wide range of even complex finite and infinite systems. The same is not true for the calculation of excited states, which are a priori not accessible through static ground-state DFT. Attempts to interpret KS eigenvalues as electron addition or removal energies, or KS eigenvalue differences as the energies of optical excitations, often lead to big discrepancies between theory and experiment. Good results can be obtained by using the KS electronic structure as a starting point in a Green's function-based many-body perturbation theory (MBPT) scheme, as one does in GW calculations $^{3-5}$ and in the Bethe-Salpeter equation (BSE) approach $^{6}$ (to compute the electron addition or removal energies and electron-hole excited states, respectively). However, those approaches are computationally very demanding since the simplicity of the dependence on the sole electronic density is lost, and replaced by an explicit dependence on one- or two-particle(s) Green's functions. In principle, these problems can be overcome, at least when neutral (e.g., optical) excitations are concerned, by taking into account the fact that in the absorption experiment the system is responding to a time-dependent external field. Therefore a generalization of static DFT to time-dependent DFT (TDDFT) has been proposed, $^{7,8}$ i.e., all potentials are now functionals of the time-dependent density. Beside the potentials, also their functional derivatives with respect to the density are needed (at least implicitly), since the system is re-

0163-1829/2004/69(15)/155112(14)/$22.50
69 155112-1
©2004 The American Physical Society

sponding self-consistently to the applied perturbation. Again, the main problem resides in finding a good approximation to the xc contribution [which depends in principle on the density at every point in space and (past) time (Ref. 9)].

The time-dependent DFT approach keeps the advantage of the static one to be in principle computationally efficient, and one could hope to replace in this way the successful, but more cumbersome BSE method. $^{6,9-12}$ However, there are two additional difficulties with respect to the case of static DFT: (i) In the case of a static DFT ground-state calculation, $v_{xc}$ should be good enough to describe the ground-state density and total energy, and the LDA is often sufficient. Instead, in the case of TDDFT also the KS eigenvalues are important, since their differences $\omega_{ij}^{KS}=\epsilon_{i}^{KS}-\epsilon_{j}^{KS}$ are the starting point for the calculation of the excitation energies of the system. One can suppose that in general improving the approximation for $\epsilon_{i}^{KS}$ should improve the quality of a TDDFT calculation, although even the exact KS eigenvalues should not be confused with measurable quasiparticle energies. Examples for systems where a good approximation of the KS eigenvalues has turned out to be crucial for the calculation of excitation spectra are atoms with Rydberg states. In this case, the LDA eigenvalues are quite far from the exact KS ones, because the LDA $v_{xc}$ has the wrong asymptotic behavior. In order to reproduce the Rydberg series, $v_{xc}$ has to be corrected by a $1/r$ tail (see, e.g., Ref. 13). (ii) Moreover, the time-dependent density variation of $v_{xc}$, i.e., the so-called xc kernel $f_{xc}(\mathbf{r},\mathbf{r}',t,t')=\delta v_{xc}(\mathbf{r},t)/\delta\rho(\mathbf{r}',t')$, has to be well described. Its task is to redistribute oscillator strength and also to modify excitation energies.

If one is only interested in a part of the spectrum (and not, e.g., in the time-dependent densities or in sum rules), one can also choose to ignore the question of the "exact" $v_{xc}$ and KS eigenvalues and try to find an effective kernel that yields good spectra starting from a given, not necessarily close to the true, $v_{xc}\cdot^{14-18}$ The present paper is situated in this framework.

It has turned out that TDDFT often yields good result in an approximation called TDLDA, i.e., using the LDA approximation for the xc potential and the adiabatic local-density approximation (ALDA) (Ref. 8) for the xc kernel,
$$
f_{x c}^{\mathrm{ALDA}}\left(\mathbf{r}, \mathbf{r}^{\prime}\right)=\left.\frac{\delta v_{x c}^{\mathrm{LDA}}(\mathbf{r}, \omega)}{\delta \rho\left(\mathbf{r}^{\prime}, \omega\right)}\right|_{\omega=0}=\delta\left(\mathbf{r}-\mathbf{r}^{\prime}\right) \frac{d v_{x c}^{\mathrm{LDA}}[\rho(\mathbf{r})]}{d \rho(\mathbf{r})},
\tag{1}
$$
especially when finite systems are considered. Also electron energy loss spectra (EELS) of solids are often well described in TDLDA. $^{9}$ However, in both cases a large improvement with respect to the independent-particle KS spectrum (i.e., with respect to a simple sum over independent transitions between KS states) comes from the density variation of the Hartree potential which is of course included in TDLDA right in the same way as in a random-phase approximation (RPA), where the exchange-correlation kernel is put to zero $(f_{xc}^{\mathrm{RPA}}=0)$.

On the other hand, the Hartree contribution is not sufficient to yield good absorption spectra of solids (it is then just giving rise to the crystal local-field effects), and taking into account $f_{xc}$ within TDLDA does not lead to a significant (if at all) improvement in this case. $^{19}$ Therefore, it would be extremely desirable to find a better, generally applicable, $f_{xc}$, to be used in conjunction with an electronic structure calculated from a suitable potential. Improvements might come through the inclusion of dynamical (memory) effects and/or long-range nonlocal terms. $^{8,20}$ Indeed, a big effort has been made in this direction using different starting points, such as time-dependent current-density functional theory, $^{21}$ perturbative approaches, $^{20,22}$ exact-exchange kernel $^{23-25}$ approaches, or performing tests of various exchange-correlation kernels proposed in the literature and illustrating the importance of the kernel in an extended system at the example of the homogeneous electron gas. $^{26}$

A class of kernels that have been shown to be very efficient in the description of solids are those directly derived from the Bethe Salpeter equation. A parameter-free ab initio expression has been obtained in several different ways, leading to the same formula. $^{9,14,16-18}$ The results using this kernel in conjunction with a quasiparticle band structure are in excellent agreement with those of the Bethe-Salpeter equation, with a potentially reduced computational effort; still, the calculations are significantly more cumbersome than those in RPA or TDLDA. Therefore, the question of finding reliable and efficient models for $f_{xc}$ remains open.

When proposing the ab initio expression in Ref. 14, some of us have also shown that already the asymptotic static long-range contribution (LRC) of the form
$$
f_{x c}^{\mathrm{LRC}}\left(\mathbf{r}, \mathbf{r}^{\prime}\right)=-\frac{\alpha}{4 \pi\left|\mathbf{r}-\mathbf{r}^{\prime}\right|}
\tag{2}
$$
(where $\alpha$ is a material dependent parameter) is sufficient to simulate the strong continuum exciton effect in the absorption spectrum and in the refraction index of bulk silicon when quasiparticle energies are used as a starting point. This fact merits a deeper investigation, since calculations using this expression are of course very quick, and it is worthwhile to elucidate to which extent this finding could be used in realistic applications. Several questions should therefore be addressed: first, is this result limited to bulk silicon, or can it be applied at least to a whole class of systems and if yes, what is the range of validity? Second, what is the effect of this kernel in an energy range other than the optical range that has been studied up to now? Third, can the method be used not only to describe but also to predict spectra of materials, i.e., how can one determine the parameter $\alpha$ without fitting to experiment? Finally, what is the relation to other works along similar lines, is the picture consistent?

In order to answer these questions, in addition to a very detailed analysis and new results concerning the spectra (including the loss function) of bulk silicon we present results for the real and the imaginary part of the dielectric function of bulk gallium arsenide, aluminum arsenide, diamond, magnesium oxide, silicon carbide, and germanium. We show that the real and imaginary parts of the dielectric function $\varepsilon$ at low energy are well reproduced when just this long-range contribution is taken into account, whereas a different long-

range contribution is needed to obtain good results for the loss function. We also examine more closely the parameter $\alpha$ and show its dependence on the material, in particular on the macroscopic screening of the material. We hence show that our approach can be used to *predict* continuum exciton effects in simple semiconductors. Finally, we discuss the relation to other approaches.

In the following, Sec. I gives some details on the calculations and shows the results for the various materials and spectra, including a discussion of the dielectric constants, and of the variation of $\alpha$ with the dielectric screening of the materials. Section II contains a detailed discussion of the effects of the LRC and a comparison to other works. Finally, we draw our conclusions in Sec. III.

## I. EFFECTS OF THE LONG-RANGE KERNEL

### A. Calculations

In the following we will consider several materials for which the approximation (2) works well, namely silicon, gallium arsenide, aluminum arsenide, silicon carbide, and germanium. We also extend our discussion to cases where the approximation starts to show some weaknesses, namely diamond and, to a larger extent, magnesium oxide.

We have first determined the DFT-LDA KS electronic structure of these materials in a ground-state calculation using norm-conserving pseudopotentials and a plane-wave basis. The cutoff energies used are: 18 Ry for silicon, 25 Ry for gallium arsenide, 25 Ry for aluminum arsenide, 60 Ry for silicon carbide, 80 Ry for germanium, 120 Ry for diamond, and 60 Ry for magnesium oxide. All materials have been studied at their theoretical lattice constant. Second, we have constructed the independent-particle response function $\chi^{(0)}$ using, following the suggestion of Ref. 14, Kohn-Sham DFT-LDA wave functions but quasiparticle eigenvalues evaluated in the GW approximation. The GW eigenvalues were obtained using the method of Ref. 27 for silicon, silicon carbide, and magnesium oxide. The self-energy shift has been simulated instead by applying a scissor operator of 0.7 eV, 0.8 eV, 0.9 eV, and 1.7 eV for Ge, GaAs, AlAs,³ and diamond, respectively. The latter (scissor) approximation is usually good when one is interested in light absorption from $sp$ semiconductors and insulators, since optical spectra are determined mainly by the (overall similar) bands near the Fermi level. The error introduced by this approximation can be estimated to be of the order of 0.1 eV on the peak positions for Ge, GaAs, AlAs . Of course, this does not influence our discussions since all results for a given material have been obtained consistently within the same scheme.

Third, we have performed a TDDFT calculation in frequency and reciprocal space by evaluating the matrix equation
$$
\begin{aligned}
\chi(\mathbf{q}, \mathbf{G}, \mathbf{G}^{\prime} ; \omega)= & \chi^{(0)}(\mathbf{q}, \mathbf{G}, \mathbf{G}^{\prime} ; \omega) \\
& +\sum_{\mathbf{G}^{\prime \prime}, \mathbf{G}^{\prime \prime \prime}} \chi^{(0)}(\mathbf{q}, \mathbf{G}, \mathbf{G}^{\prime \prime \prime} ; \omega) \\
& \times\left(v+f_{x c}\right)\left(\mathbf{q}, \mathbf{G}^{\prime \prime}, \mathbf{G}^{\prime \prime \prime} ; \omega\right) \chi(\mathbf{q}, \mathbf{G}^{\prime \prime \prime}, \mathbf{G}^{\prime} ; \omega).
\end{aligned}
\tag{3}
$$
Here, $\mathbf{q}$ is a vector in the first Brillouin zone, $\mathbf{G}$ are reciprocal lattice vectors, $v$ is the bare Coulomb interaction, and $\chi$ is the linear density response function matrix that relates the charge response $(\delta \rho)$ to the external potential: $\delta \rho$ $=\chi \delta v_{ext}$, and that yields the inverse dielectric matrix as $\varepsilon^{-1}=1+v \chi$. For the xc kernel $f_{x c}$ we have used the Fourier transform of Eq. (2) with a value for $\alpha$ chosen to approximately fit the experiment. The spectra for Si, SiC, Ge, and MgO have been obtained using 256 off-symmetry shifted $k$ points in the Brillouin zone (BZ) (Ref. 11) whereas 864 shifted $k$ points in the BZ have been used for GaAs, AlAs, and diamond. The number of unoccupied bands included in the calculation of the response was 4, 13, 6, 6, 4, 21, 16, and 4 for Si absorption, Si EELS, GaAs, AlAs, SiC, diamond, Ge, and MgO, respectively. Crystal local-field effects were fully taken into account by carefully converging the size of all matrices in $(\mathbf{G},\mathbf{G}')$ space. The total estimated convergence error is of the order of 5% to 10% on the imaginary part of the dielectric macroscopic function (integrated over the absorption range). The error is largest for the case of MgO, due to the finite $k$-point sampling, and smallest for diamond. Again, however, this error does not influence the comparison of TDDFT and BSE results.

To give an idea of the efficiency of our LRC approach, note that after the GW band structure has been obtained, the calculation of the optical spectrum of silicon, as shown in Fig. 1, takes about 200 sec on an AMD Athlon 2.0 GHz, which is about the same as in a TDLDA calculation.

### B. Optical spectra

Let us first look at absorption spectra. We show the results obtained for the imaginary part of the dielectric macroscopic function $\varepsilon_{2}(\omega)=\operatorname{Im}[1/\varepsilon_{\mathbf{G}=\mathbf{G}'=0}^{-1}(\mathbf{q}\to 0,\omega)]$ of Si (Fig. 1), GaAs (Fig. 2), and AlAs (Fig. 3). In all figures, the dots are the experimental results (Ref. 28 for Si, 29 for GaAs, 30 for AlAs), and dotted curves are RPA calculations (i.e., neglecting completely $f_{x c}$ in the response functions). Dot-dashed curves are used to display the results of a standard TDLDA calculation [i.e., using DFT-LDA eigenvalues and the static short-range ALDA xc kernel, Eq. (1)]. A broadening of about 0.1 eV, 0.15 eV, and 0.1 eV for Si, GaAs, and AlAs, respectively, has been used to simulate the experimental one and to smear out the artificial structures in the calculated results due to the finite $k$-point sampling. Like other authors [see e.g., (Ref. 19)] we find a TDLDA result close to the RPA one, showing the well-known discrepancies with respect to the experiment: peak positions are wrong (the spectrum exhibits a redshift), and the intensity of the first main structure (the $E1$ peak³² in Si, GaAs, and AlAs) is strongly underestimated. The dashed curve is the result obtained by replacing KS eigenvalues with GW quasiparticle energies in the RPA form of $\chi$ (where $f_{x c}=0$). This calculation, called GW-RPA in the following, corresponds to the second step of our approach, as outlined above. Again, we find the well-known discrepancies with experiment: now the calculated spectrum shows a blue shift. Moreover, the line shape has not been corrected. For all the materials, finally, the continuous curve is the result of our LRC calculation. For Si we show also the

![](./images/812354788615258113_1.jpg)

FIG. 1. Imaginary part of the macroscopic dielectric function for bulk Si. Dots (both panels): experiment (Ref. 28); dotted curve (upper panel): RPA calculation; dot-dashed curve (both panels): TDLDA calculation; dashed curve (upper panel): GW-RPA calculation; long-dashed curve (lower panel): Bethe-Salpeter calculation; solid line (lower panel): TDDFT-LRC calculation.

result obtained through a Bethe-Salpeter calculation [long-dashed curve in Fig. 1(b)]. An excellent fit to the BSE and experimental spectra is obtained within the LRC scheme by using $\alpha=0.2$, 0.2, and 0.35 for Si, GaAs, and AlAs, respectively. We have determined $\alpha$ by varying it until the BSE and TDDFT-LRC spectra look similar, which is straightforward since the calculations are as quick as an RPA calculation. As an example, in Fig. 4 we show the trend for the optical absorption of silicon when the weight $\alpha$ of the $1/q^2$ divergence is varied. Starting from the GW-RPA result, if we introduce a small $\alpha=0.1$ long-range contribution, the $E1$ peak is increased while the $E2$ peak is shifted by about 0.1 eV towards lower energies and also a bit increased. Globally a part of the oscillator strength has been transferred to lower energies and excitonic corrections begin to show up. At $\alpha=0.2$ we obtain the result that best fits the experimental curve: the $E1$ peak has reached the experimental height and it is also redshifted by about 0.15 eV with respect to GW-RPA; the $E2$ peak is redshifted by another 0.1 eV with respect to the $\alpha=0.1$ result

![](./images/812354788615258113_2.jpg)

FIG. 2. Imaginary part of the macroscopic dielectric function for GaAs. Dots: experiment; dot-dashed curve: TDLDA calculation; dashed curve: GW-RPA calculation; solid line: TDDFT-LRC calculation.

![](./images/812354788615258113_3.jpg)

FIG. 3. Imaginary part of the macroscopic dielectric function for AlAs. Dots: experiment; dot-dashed curve: TDLDA calculation; dashed curve: GW-RPA calculation; solid line: TDDFT-LRC calculation.

![](./images/812354788615258113_4.jpg)

FIG. 4. Effect of varying $\alpha$ on the imaginary part of the macroscopic dielectric function for Si. Dots: experiment (Ref. 28); dashed line: GW-RPA calculation; double-dash-dotted line: TDDFT LRC calculation using an LRC contribution with $\alpha=0.1$; solid line: $\alpha=0.2$; double-dot-dashed line: $\alpha=0.3$.

but also, from now on, its height stops to increase and begins to reduce. At this value of $\alpha$ the excitonic effects, as they are described by the resolution of the Bethe-Salpeter equation, are also correctly reproduced by the TDDFT-LRC approach. Finally at $\alpha=0.3$, most of the oscillator strength is transferred to the $E1$ peak and the result is a global overestimation of the excitonic effects.

Figures 1-3 show that one parameter is enough for each of these materials in order to correct their spectrum, which is far from trivial: there is in fact a nonuniform shift in peak positions, and a redistribution of intensities among the peaks. In the case of Si and GaAs, the task of $\alpha$ is to shift the $E2$ peak and to strengthen the $E1$ structure, whereas in the case of AlAs also $E2$ is correctly enhanced.

Moreover, in this range of frequencies other features of $\varepsilon$ are very well reproduced using the same $\alpha$, as we will discuss in the following.

The next quantity we can examine is in fact the real part of the macroscopic dielectric function, $\text{Re}(\varepsilon)$ (Fig. 5 for Si, Fig. 6 for GaAs, Fig. 7 for AlAs). One can clearly see the failure to reproduce the experimental results (dots) of the RPA (dotted curve), TDLDA (dot-dashed curve), and the GW-RPA (dashed curve) approaches. Again, both peak positions and line shapes are wrong. Instead a comparison of the LRC result (continuous curve, obtained with the same values for $\alpha$ as above) to the experiment or to the BSE result shows a striking improvement with respect to RPA and TDLDA for all three materials. This shows that the good result for bulk silicon that was already presented in Ref. 14 is not a pure coincidence, but valid for a whole class of materials.

![](./images/812354788615258113_5.jpg)

FIG. 5. Real part of the macroscopic dielectric function for Si. Dots (both panels): experiment (Ref. 31); dotted curve (upper panel): RPA calculation; dot-dashed curve (both panels): TDLDA calculation; dashed curve (upper panel): GW-RPA calculation; long-dashed curve (lower panel): Bethe-Salpeter calculation; solid line (lower panel): TDDFT-LRC calculation.

When going to large-gap materials, screening is lower and the electron-hole interaction becomes stronger. One can therefore expect that eventually this drastic LRC approximation for $f_{xc}$ will break down. In order to test the limits of usefulness of this approach, we have therefore applied the method to diamond (which has an experimental dielectric constant $\varepsilon_{\infty}$ of 5.65) and to MgO ($\varepsilon_{\infty}=3.0$).

Figure 8 (for diamond) and Fig. 9 (for MgO) show the results for the absorption spectrum, while Fig. 10 contains $\text{Re}(\varepsilon)$ for diamond calculated in the various approaches mentioned above. A broadening of about 0.5 eV has been used both for diamond and for MgO. Also in these materials

![](./images/812354788615258113_6.jpg)

FIG. 6. Real part of the macroscopic dielectric function for GaAs. Dots: experiment; dot-dashed curve: TDLDA calculation; dashed curve: GW-RPA calculation; solid line: TDDFT-LRC calculation.

LRC calculations show a significant improvement of the di- electric functions with respect to both the TDLDA and the GW-RPA ones. However, whereas using a best fit ($\alpha$=0.6) in diamond the shoulder on the low-energy side of the ab- sorption spectrum is correctly enhanced, the position of the $E2$ peak is only partially corrected (to about 50% of the error in GW-RPA). Compared to the experimental data of Ref. 34, an error of 0.9 eV is found for the $E1$ peak position in Im($\varepsilon$) and for the point at which Re($\varepsilon$) becomes negative. The shape of Re($\varepsilon$) is globally well reproduced, so that the over- all conclusion concerning diamond is still very positive.

![](./images/812354788615258113_7.jpg)

FIG. 7. Real part of the macroscopic dielectric function for AlAs. Dots: experiment; dot-dashed curve: TDLDA calculation; dashed curve: GW-RPA calculation; solid line: TDDFT-LRC calculation.

In MgO, $\alpha$=1.8 yields the best overall result. In this case, the choice of $\alpha$ is clearly a compromise which allows to enhance the first excitonic peak to a good fraction of the experimental value, without overestimating too much the strength of the subsequent structures. The worst disagree- ment concerns the weak structure at about 17.5 eV (in the experimental spectrum), which is shifted to about 20 eV by the self-energy correction [dashed curve in Fig. 9(a)]. This shift is not sufficiently counterbalanced by the backshift, to 19 eV, due to the LRC [continuous curve in Fig. 9(b)].

There is hence a significant improvement also for large- gap materials, although the, $\alpha/q^{2}$, approximation to $f_{xc}$ works clearly worse than for the semiconductors discussed before. However, this simple contribution already leads to a promising step forward, and one should not forget that alter- natively, a similar agreement can only be found using the much more cumbersome BSE approach (see, e.g., Refs. 6, 11, 12, 35, 36), or at least the still very demanding $f_{xc}$ that is derived from the BSE in Refs. 9, 14, 16–18.

![](./images/812354788615258113_8.jpg)

FIG. 8. Imaginary part of the macroscopic dielectric function for diamond. Dots: experiment (Ref. 34); dot-dashed curve: TDLDA calculation; dashed curve: GW-RPA calculation; solid line: TDDFT- LRC calculation.

### C. Dielectric constants

The low-frequency limit of Re($\varepsilon$), $\varepsilon_{\infty}=\varepsilon_{M}(\omega=0)$, de- serves special attention, since it is known that the adiabatic LDA kernel does influence this quantity significantly, $^{37,38}$ in contrast to what happens in the absorption spectrum.

Table I summarizes our results. Converged results are ob- tained by increasing the $k$-point sampling to 2048, 864, 864 $k$

![](./images/812354788615258113_9.jpg)

FIG. 9. Imaginary part of the macroscopic dielectric function for MgO. Dots (both panels): experiment (Ref. 33); dotted curve (upper panel): RPA calculation; dot-dashed curve (both panels): TDLDA calculation; dashed curve (upper panel): GW-RPA calculation; long-dashed curve (lower panel): Bethe-Salpeter calculation; solid line (lower panel): TDDFT-LRC calculation.

points in the Brillouin zone, for silicon, GaAs, and AlAs, respectively. For diamond, calculations have been obtained within density functional perturbation-theory (DFPT) (Refs. 42, 43) using 60 Monkhorst-Pack $k$ points in the irreducible Brillouin zone. No well-converged values are, to our knowledge, available yet from the BSE approach for these very simple materials, which stresses again the necessity to find an alternative strategy.

Concerning the other approaches studied here, we find the same trend for all materials: the first and second columns of Table I show the results of an RPA calculation without and with local-field effects, respectively. Available results in the literature are well reproduced. Also the significant increase of the dielectric constant when a TDLDA calculation is performed (column 4) as well as the decrease when GW, instead of KS-LDA, eigenvalues are used in an RPA calculation (column 5) are consistent with previous findings (take, for example the data of Ref. 44 where, however, calculations are performed at the experimental lattice constant whereas we use the theoretical equilibrium value). TDLDA values are consistently higher, GW-RPA values lower than the experimental dielectric constants (column 7). For diamond the TDLDA results are in very close agreement with the experiment as previously reported. $^{45}$ The sixth column shows the results which are obtained in a TDDFT calculation starting from GW eigenvalues and using the same LRC kernel (i.e., the same $\alpha$) as the one that yields the good optical spectra. As in TDLDA, the resulting dielectric constants are larger than the measured ones, but the error has decreased by about $25-50$ %. Finally, the eighth column of Table I also gives the values of $\alpha$ which, used in our TDDFT-LRC calculation starting from GW, would yield the experimental dielectric constant. These values of $\alpha$ are systematically smaller than the ones which yield the correct spectra in the optical range. This is consistent with the expectation that a constant $\alpha$ can only reproduce a finite range of frequencies. We will come back to this point in the following section and in Sec. III.

![](./images/812354788615258113_10.jpg)

FIG. 10. Real part of the macroscopic dielectric function for diamond. Dots: experiment (Ref. 34); dot-dashed curve: TDLDA calculation; dashed curve: GW-RPA calculation; solid line: TDDFT-LRC calculation.

### D. Loss spectra

The fact that the problem of electronic spectra involving neutral excitations cannot be overcome by just determining one number $\alpha$ is illustrated in a much more striking way by going higher up in energy, looking at electron energy loss spectroscopy. As discussed in Refs. 9,14, the role of long-range interactions is fundamentally different in the loss spec-

<table>
<caption>Table I. Static dielectric constants ($\varepsilon_\infty$) and weights of the LRC ($\alpha$) for the different materials considered. The theoretical values have been obtained at the theoretical lattice constant. $\alpha_{ok}^{\text{GW}}$ and $\alpha_{ok}^{\text{LDA}}$ are the values for $\alpha$ which should be used together with $f_{xc}=-\alpha/q^2$ in order to reproduce the experimental value of $\varepsilon_\infty$, starting from the GW and the LDA bandstructures, respectively.</caption>
<thead>
  <tr>
    <th>Material</th>
    <th>RPA-NLF</th>
    <th>RPA-LF</th>
    <th>TDLDA</th>
    <th>GW-RPA</th>
    <th>TDDFT-LRC</th>
    <th>EXPT.</th>
    <th>TDDFT-LRC</th>
    <th>TDDFT-LRC</th>
  </tr>
  <tr>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th></th>
    <th>$\alpha=\alpha_{ok}^{\text{GW}}$</th>
    <th>$\alpha=\alpha_{ok}^{\text{LDA}}$</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Silicon</td>
    <td>13.6</td>
    <td>12.2</td>
    <td>12.9</td>
    <td>10.7</td>
    <td>12.2</td>
    <td>11.4$^{\text{a}}$</td>
    <td>11.4</td>
    <td>11.4</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>($\alpha=0.2$)</td>
    <td></td>
    <td>($\alpha=0.09$)</td>
    <td>($\alpha=-0.09$)</td>
  </tr>
  <tr>
    <td>GaAs</td>
    <td>13.90</td>
    <td>12.42</td>
    <td>13.22</td>
    <td>10.29</td>
    <td>11.92</td>
    <td>10.6$^{\text{b}}$</td>
    <td>10.6</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>($\alpha=0.2$)</td>
    <td></td>
    <td>($\alpha=0.05$)</td>
    <td></td>
  </tr>
  <tr>
    <td>AlAs</td>
    <td>10.18</td>
    <td>8.85</td>
    <td>9.47</td>
    <td>7.60</td>
    <td>9.1</td>
    <td>8.2$^{\text{c}}$</td>
    <td>8.2</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>($\alpha=0.35$)</td>
    <td></td>
    <td>($\alpha=0.15$)</td>
    <td></td>
  </tr>
  <tr>
    <td>Diamond</td>
    <td>5.88</td>
    <td>5.45</td>
    <td>5.72</td>
    <td></td>
    <td></td>
    <td>5.65$^{\text{d}}$</td>
    <td></td>
    <td></td>
  </tr>
</tbody>
<tfoot>
  <tr>
    <td colspan="9">$^{\text{a}}$From Ref. 39.</td>
  </tr>
  <tr>
    <td colspan="9">$^{\text{b}}$From Ref. 40.</td>
  </tr>
  <tr>
    <td colspan="9">$^{\text{c}}$From Ref. 40.</td>
  </tr>
  <tr>
    <td colspan="9">$^{\text{d}}$From Ref. 41.</td>
  </tr>
</tfoot>
</table>

tra, and one can in particular expect that a small long-range contribution to the kernel will have much less effect than in the case of absorption spectra, since in the case of energy loss it is added to another, strong, long-range contribution (i.e., the full bare Coulomb interaction $v$), whereas in the case of absorption it is added to only the microscopic part of $v.^{9}$

This is in fact what we find. Since we now want to show that the simple LRC method is not working at the same time for absorption and for loss spectra, it is sufficient to discuss just one example, e.g., silicon. First, the upper panel of Fig. 11 demonstrates the quite general finding that in the case of loss spectra both the RPA (dotted curve) and, even better, the TDLDA (dot-dashed curve) already manage to reasonably reproduce the experimental plasmon peak (dots taken from Ref. 46). Some further improvement is found when the BSE approach is used (Fig. 11 upper panel, long-dashed curve, taken from Ref. 47). As it was found in Ref. 47, the good result of the RPA and the TDLDA derives from a partial cancellation of self-energy and excitonic effects. The full BSE calculation of a valence plasmon is however today still at the limit of computer resources, $^{49}$ and one might hope to obtain a real breakthrough using TDDFT for those cases where TDLDA fails. Unfortunately, as expected above the one-parameter LRC approach not only does not improve upon TDLDA, but even breaks down for this application. In the bottom panel of Fig. 11, the dashed curve is in fact the GW-RPA result shown in Ref. 47, which is in bad agreement with experiment. The dot-dashed curve is the LRC result using the same $\alpha=0.2$ as used for the absorption spectrum. Only a small effect with respect to GW-RPA is seen on the loss spectrum, and one is thus left essentially with the rather unsatisfying GW-RPA result. Instead, using the much larger value $\alpha=2.0$ (continuous curve), the result becomes again satisfactory.

It is hence obvious that, if one wants to treat the dielectric function over the whole frequency range including the optical and the loss spectra, one has to use a different $\alpha$ in the different regions of the spectrum (i.e., introduce a frequency dependence) (Ref. 15), or to use the more complex form given in Refs. 14, 16–18, 50.

## E. Material-dependence of the kernel

Being conscious of the limitations of this approach, one can however use the latter not only for understanding the role of $f_{xc}$, but also for predicting optical properties of semiconductors with a very moderate computational effort. To do that we have to remind that Eq. (2) was derived in Ref. 14 by choosing matrix elements of $f_{xc}$ in the basis of Kohn-Sham transitions to be equal to matrix elements of the attractive, screened Coulomb kernel$-W$. This tells us immediately that $f_{xc}$ should be negative, and roughly proportional to the inverse dielectric constant $\varepsilon_{\infty}^{-1}$. If this is true, it can give a hint of how to estimate the excitonic correction to an absorption spectrum for a material without adding computational complexity beyond the RPA, i.e., without solving the BSE and without evaluating more complicated expressions for $f_{xc}.^{16}$ We therefore show in Fig. 12, a graph displaying the values of $\alpha$ (as used to optimize the optical absorption spectrum, Sec. I B) and their relation to the inverse of the dielectric constant for all the materials which we are considering. It turns out that the relation can be well fitted by a straight line,

$$\alpha=4.615\varepsilon_{\infty}^{-1}-0.213,\tag{4}$$

which almost crosses the origin (i.e., it respects the thumb rule of large screening/weak excitonic effects). This is reassuring regarding the consistency of the derivation, the simple approximation adopted, and the results. Moreover it allows one to guess a reasonable $\alpha$ for other materials.

We have tested this idea by calculating the absorption spectrum of cubic silicon carbide and germanium. We have used their experimental dielectric constant ($\varepsilon_\infty=6.5$ for SiC, $\varepsilon_\infty\simeq16$ for Ge) in order to deduce from Eq. (4) that $\alpha$ should be about 0.5 for SiC and 0.08 for Ge. These values of $\alpha$ lead to the calculated optical absorption spectra reported in Fig.

![](./images/812354788615258113_11.jpg)

FIG. 11. Energy-loss function for Si. Dots (both panels): experiment (Ref. 46); dotted line (upper panel): RPA calculation; dot-dashed line (upper panel): TDLDA calculation; long-dashed line (upper panel): Bethe-Salpeter calculation; dashed line (lower panel): GW-RPA calculation; double-dot-dashed line (lower panel): TDDFT-LRC calculation using $\alpha=0.2$; solid line (lower panel): TDDFT-LRC calculation using $\alpha=2.0$.

13(b) for SiC and Fig. 14 for Ge, and to the real part shown in Fig. 15(b) for SiC. In SiC the results (solid line) turn out to be close to those of a Bethe-Salpeter calculation (long-dashed line), and the improvement with respect to TDLDA (dash-dotted line in Figs. 13 and 15) is impressive. For Ge the improvement obtained by this approach (solid line) with respect to TDLDA (dot-dashed line) is equally significant. The test case of germanium allows us hence to extend the straight line of Fig. 12 to larger values of $\varepsilon_{\infty}$, and therefore to extend the range of the validity of this approach. It can be supposed that similarly good results can be obtained for other $sp$ semiconductors, with a workload that is equal to a simple RPA calculation, yielding an accuracy comparable to that of BSE calculations.

![](./images/812354788615258113_12.jpg)

FIG. 12. Material dependence of the parameter $\alpha$ with respect to the inverse of the dielectric constant. Filled circles: $\alpha$ fitted on optical spectra; solid line: linear fit for $\alpha(\varepsilon_{\infty}^{-1})$ on filled circles [Eq. (4)]; empty circles: $\alpha$ calculated from Eq. (4).

## II. DISCUSSION AND RELATION TO OTHER WORK

### A. Effects of the long-range contribution

Regarding the above results, two important points should be noted.

First, in the range of materials where the approach has turned out to work, the effect of this kernel is not to shift transition energies, but more properly to redistribute oscillator strength, which can lead to an apparent shift of peaks. This is in agreement with the behavior of the Bethe-Salpeter approach in the case of materials dominated by continuum excitons, i.e., materials with a small to moderate electron-hole interaction. However, the performance of the BSE and TDDFT-LRC approaches differs noticeably in the case of materials with strongly bound excitons (absorption peaks appearing inside the photoemission band gap). Indeed, the Bethe-Salpeter approach is able to create new poles inside the band gap, corresponding to excitonic peaks occurring in the experimental spectra, give them the correct weight and contemporaneously redistribute in the correct way the oscillator strength at higher energies. On the contrary, the same does not happen for the LRC kernel. This can already be detected by inspection of the results for MgO presented above (Fig. 9), where the first peak of the BSE and experimental result is an exciton bound by about 0.5 eV: the LRC curve shown in Fig. 9 is the result corresponding to $\alpha=1.8$, which gives the best fit to the experiment and the BSE result. That is, it tries to reproduce at the same time both the bound peak and the higher-energy part of the spectrum, with

![](./images/812354788615258113_13.jpg)

FIG. 13. Imaginary part of the macroscopic dielectric function for cubic SiC. Dots: experiment (Ref. 48); dotted curve: RPA calculation; dot-dashed curve: TDLDA calculation; dashed curve: GW-RPA calculation; long-dashed curve: Bethe-Salpeter calculation; solid line: TDDFT-LRC calculation, with $\alpha$ determined from Eq. (4).

moderate success. The $\alpha$ we have chosen is about 40% higher than the value $\alpha \simeq 1.3$ evaluated calculating Eq. (4) for the dielectric constant of MgO, as can also be seen by direct inspection of Fig. 12, and still the peak position is wrong. A larger $\alpha$, on the other hand, would further deteriorate the agreement for the low-energy part of the continuum. Therefore, the simple static approximation $f_{xc}=-\alpha/|\mathbf{q}+\mathbf{G}|^{2}$ is not able to describe such materials (see also a discussion of models for bound excitons in Ref. 51).

Analogously, the first (GW-shift) part of the kernel, which truly has to change excitation energies, cannot be simulated by a static LRC alone. Moreover a static LRC is not sufficient to yield a good total $f_{xc}$ to be used on top of the KS-LDA band structure (instead of the GW band structure used throughout this work up to here): such an $f_{xc}$ should simultaneously push the spectrum to higher energies, and also enhance the structures on the low-energy side. This complicated task cannot be achieved by just one effective LRC contribution. We illustrate the situation for the case of silicon in Fig. 16, showing for different values of $\alpha$ the discouraging absorption spectra that result when one uses the approximation given in Eq. (2) on top of a KS-LDA band structure. Negative values of $\alpha$ shift in fact oscillator strength to higher energies, but excitation energies are not shifted, and with increasing $|\alpha|$ the spectrum is strongly suppressed. One can overcome this problem, as it is done in the present work, by using directly GW energies.

![](./images/812354788615258113_14.jpg)

FIG. 14. Imaginary part of the macroscopic dielectric function for Ge. Dots: experiment; dot-dashed curve: TDLDA calculation; dashed curve: GW-RPA calculation; solid line: TDDFT-LRC calculation, with $\alpha$ determined from Eq. (4).

Finally, we want to stress that the crucial part of the electron-hole interaction represented by the Fourier transform of Eq. (2), $f_{xc}(\mathbf{q},\mathbf{G},\mathbf{G}')=-\alpha\delta_{\mathbf{G},\mathbf{G}'}/|\mathbf{q}+\mathbf{G}|^{2}$ is in its $\mathbf{G}=\mathbf{G}'=0$ contribution (which diverges for $q\to0$). We have in fact carried out calculations for silicon neglecting all $\mathbf{G}\neq0$ terms, and obtained results that are indistinguishable from the ones that are obtained using the same $\alpha$ and $f_{xc}(\mathbf{q},\mathbf{G},\mathbf{G}')=-\alpha\delta_{\mathbf{G},\mathbf{G}'}/|\mathbf{q}+\mathbf{G}|^{2}$ for all $\mathbf{G}.^{52}$

### B. Link and comparison to other approaches

The need for a long-range contribution$^{53}$ to the exchangecorrelation kernel has been invoked in previous works, starting from the argument that in a periodic infinite system the total energy should be written as a functional of the periodic charge density, and of the macroscopic polarization $\mathbf{P}$. In

![](./images/812354788615258113_15.jpg)

FIG. 15. Real part of the macroscopic dielectric function for cubic SiC. Dots (both panels): experiment (Ref. 48); dotted curve (upper panel): RPA calculation; dot-dashed curve (both panels): TDLDA calculation; dashed curve (upper panel): GW-RPA calculation; long-dashed curve (lower panel): Bethe-Salpeter calculation; solid line (lower panel): TDDFT-LRC calculation.

fact, Godby and Sham⁵⁴ have pointed out that long-range density changes give rise to an effective exchange-correlation electric field. Gonze, Ghosez, and Godby⁵⁵ have shown that the origin of this exchange-correlation field lies in the macroscopic polarization, introducing an explicit functional dependence of the exchange-correlation energy on this quantity. They have also shown that one could avoid this problem by introducing a scissor-operator quasiparticle correction to the Kohn-Sham gap. The long-range contribution stemming from this discussion is hence simulating a gap correction, and, consequently, has a positive sign. In the framework of the derivation of Ref. 14, it corresponds to the contribution to the kernel which has been simulated here by explicitly using a GW (instead of a Kohn-Sham) band structure, consistently with the proposal of Ref. 55. Aulbur, Jönsson, and Wilkins⁵⁶ have related the resulting effective exchange-correlation electric field to the difference between the true and the Kohn-Sham static susceptibilities, and, by using calculated (Kohn-Sham) and measured (i.e., "true") results, determined the prefactor for the long-range component of the kernel for a series of materials. They have found a contribution $\Delta f_{xc}=\gamma/q^{2}$, where $\gamma$ is positive and of the order of 0.25 for several small- and medium-gap semiconductors. The second contribution to the long-range part of the kernel, i.e., that stemming from the electron-hole attraction (which gives rise to the negative $-\alpha/q^{2}$ term discussed in the present paper) is not explicitly considered in these publications. However, since in Ref. 56 $\gamma$ is determined using the experimental susceptibilities, this contribution is of course implicitly included in the resulting values for $\gamma$. The numerical values obtained in Ref. 56 should hence be considered to be the sum of a positive and a negative long-range contribution, stemming from a gap correction and from the electron-hole interaction, respectively. In order to illustrate this point and make the link, we have reported in the last column of Table I, for silicon, the value $\alpha_{ok}^{LDA}$ which one would obtain by fitting the dielectric constant starting from an LDA band structure (instead of that from a GW one, as done in the case of column 7). Consistently with the values reported in Ref. 56, $\alpha$ has now changed sign. Our value is smaller in magnitude than that of Aulbur et al., because we include local-field effects explicitly; if we neglect the latter,

![](./images/812354788615258113_16.jpg)

FIG. 16. Imaginary part of the macroscopic dielectric function for Si. Dots: experiment (Ref. 28); dotted line: RPA; dashed line: GW-RPA calculation; double-dash-dotted line: LRC calculation starting from a KS DFT-LDA electronic structure and using an LRC contribution with $\alpha=-0.1$; double-dot-dashed line: the same as previous but using $\alpha=-0.2$; solid line: using $\alpha=-0.5$.

our fit reproduces the value of Ref. 56. Note that, in this context, also the self-energy contribution can be simulated by a static long-range part only, instead of using the full GW band structure, because bare numbers (static susceptibilities) and not whole parts of the spectrum have to be reproduced. In fact, as we have shown in Fig. 16, a static long-range contribution alone is not able to simulate a quasiparticle shift of the absorption spectrum.

It is at this point worthwhile to comment also on a discussion addressed by Dal Corso, Baroni, and Resta³⁸ and taken up by Aulbur, Jönsson and Wilkins,³⁶ namely, whether the Kohn-Sham "gap problem" has to be solved in order to obtain correct dielectric constants. As pointed out by the authors of Ref. 38, Kohn-Sham eigenvalues do not have a direct physical meaning, and do not necessarily appear explicitly in the calculation of the dielectric constant, which, moreover, is a ground-state quantity. This point of view has however been questioned in Ref. 56, on the basis of the considerations and numerical results in that paper. Also from our present approach, one might get the impression that, as a matter of principle, a quasiparticle band structure has to be used in order to get correct dielectric constants. Therefore, we feel the need to clarify that this is not the case. In fact, we do use a quasiparticle band structure, but for several purely practical reasons: (i) as pointed out above, the exact Kohn-Sham band structure is not known; (ii) starting from a quasiparticle band structure allows for simpler approximations to the remaining part of the kernel; (iii) our derivation is based on the Bethe-Salpeter equation, which relies on the quasiparticle picture; (iv) this way of presenting things allows us to discuss separately the contribution of the electron-hole interaction. However (i) the exact Kohn-Sham band structure might be significantly different from the quasiparticle one, and is nevertheless the correct (fictitious) electronic structure to be used in the framework of TDDFT; (ii) also the exact "electron-hole attraction" contribution to the kernel in the TDDFT framework $f_{xc}$ is most probably very different from the explicit electron-hole attraction (derived from $-W$) of the Bethe-Salpeter equation. In particular, one may expect it to be weaker, because schematically $f_{xc}=\Delta GW-W$, where the contribution $\Delta GW$ from the quasiparticle correction has opposite sign with respect to $-W$. It is the total correction that has to yield the correct dielectric constants, not the quasiparticle shift alone; (iii) as also pointed out above, a total static long-range contribution only simulates the effect of $f_{xc}=\Delta GW-W$ on the dielectric constant, which does not mean that this $f_{xc}$ corresponds to, or even necessarily resembles, the exact exchange-correlation kernel. Therefore, the results of Ref. 56 do not imply that the band gap mismatch between the Kohn-Sham and the quasiparticle band structure is in principle relevant to the problem of calculating the dielectric constant (whereas it can be relevant in practice).

It should be noted that the idea of a polarization contribution is of course not limited to the static case. In fact, de Boeij et al.²¹ have performed calculations of optical spectra of various semiconductors, including silicon, diamond and GaAs, using a polarization-dependent functional derived from current density functional theory.⁵⁷ Their calculations involve two parameters: one (material-dependent) accounting for a positive shift of transition energies, and a second (constant) one, chosen to be 0.4, that multiplies a tensor Y containing the polarization effects. Y is in principle frequency dependent, but a static ($\omega=0$) value, derived from the homogeneous electron gas, is used. This tensor appears in an equation [Eq. (18) in Ref. 21] relating the full susceptibility to a Kohn-Sham one. It is straightforward to show that mathematically this approach is equivalent to ours, if one identifies $0.4Y=\alpha$, and if their shift of transition energies is chosen to be the quasiparticle correction. The fact that the numerical results of Ref. 21 turn out to be in slightly worse agreement with experiment than the present ones can be traced back to several reasons: (i) the authors have visibly chosen the shifts such that peak positions coincide. For example, the shift of 0.6 eV for diamond is significantly smaller than the quasiparticle one (i.e., 1.7 eV); (ii) the use of $\tilde{\chi}$, defined in Eq. (9) of Ref. 21, might have led to some disagreement: in order to be equivalent to our formulation, $\tilde{\chi}$ should in fact not be the Kohn-Sham independent-particle susceptibility, but its macroscopic counterpart, i.e., it should already contain Hartree local-field (microscopic) effects. This point might have been treated differently in Ref. 21 [see the comment before their Eq. (7)]. If $\tilde{\chi}$ is chosen to be the independent-particle Kohn-Sham response function, one can still try to simulate the missing local-field effects through an effective Y (0.4 Y is then of course different from our $\alpha$), but this will most probably lead to worse results than including local-field effects explicitly.

The considerations above are not a criticism to the ansatz used in that work, which constitutes an interesting alternative derivation of such a long-range contribution. If both derivations are correct, the underlying physics must of course be the same. This is in fact the case: when the system responds to the external fields, dipoles are created, which (even in the extreme case where each dipole is atomiclike) in turn give rise to a macroscopic field. The "Kohn-Sham dipoles" have to be calculated self-consistently: the system acting against the applied field, the Hartree term therefore reduces the total potential and hence the net response of the system, leading to a positive long-range contribution (i.e., the term $v$) to the total kernel. Both the self-energy correction and the electron-hole interaction can now change the dipoles: the first contribution will lower the polarizability of the system. Again, a positive long-range contribution will be the consequence. The electron-hole interaction strengthens the dipoles and gives therefore a contribution of opposite sign. The fact that the interaction between electron and hole (which can be understood as intradipole in the above picture) can be shortened, and sometimes can be even described by a contact-exciton model, is hence not in contrast with the fact that $f_{xc}$ gains a long-range component: the latter is in fact the result of the sum of all dipole contributions. Note that the Bethe-Salpeter kernel describes the interaction between a hole and an electron charge density (that can be situated close to each other), whereas the TDDFT kernel yields an interaction between valence-conduction dipoles. It is therefore not surpris-

![](./images/812354788615258113_17.jpg)

FIG. 17. Imaginary part of the macroscopic dielectric function for Si. Dots: experiment (Ref. 28); dashed line: GW-RPA calculation; solid line: TDDFT LRC calculation starting from a GW electronic structure and using an LRC contribution with $\alpha=0.2$; double-dot-dashed line: the same as previous but using $\alpha=0.3$; double-dash-dotted line: using $\alpha=1.0$; dot-dashed line: using $\alpha=1.5$.

ing that the former can sometimes even be modeled by a contact exciton, and still be simulated by a long range $f_{xc}$.

Finally, it is useful to point out the relation between Ref. 14 and the present work on one side, and a recently appeared study by Kim and Görling$^{25}$ on the other side. In that work, the absorption spectrum of bulk silicon was calculated in the framework of a so-called "exact exchange" (EXX) formalism,$^{23,24}$ which in fact could be called density func- tional exact exchange, for it does not correspond to the ordinary definition of the exchange in the Hartree-Fock sense. In that formalism, the authors start from a KS band structure (which happens to be rather close to the $GW$ band structure) obtained through an EXX $v_{x}$ potential and then perform a linear-response TDDFT using an EXX kernel, $f_{x}^{EXX}$. The resulting absorption spectrum of bulk silicon is found to be in good agreement with experiment. Several results of Kim and Goerling are consistent with the findings of Ref. 14: Kim and Goerling show that in their kernel the dynamic dependence can be neglected and, more important, that also their kernel has a $1/q^{2}$ long-range term. However, the weight of the divergence calculated straightforwardly by using the complete $f_{x}^{EXX}$ expression seems to be overestimated, resulting in what the authors call a "collapse of the spectrum." In fact something similar happens in our calculation if we use a very large weight $\alpha$. In Fig. 17 we show the trend for the optical absorption of silicon when $\alpha$ is increased from its best [proportional to the inverse of the dielectric constant, according to Eq. (4)] value of 0.2. At $\alpha=0.3$ most of the oscillator strength is already transferred to low frequency, resulting in an overestimation of the excitonic effects. At $\alpha$ =1.0 the spectrum is appearing only at very low frequency. Finally at $\alpha=1.5$ the spectrum is completely "collapsed," which should reproduce the situation mentioned in Ref. 25. This led Kim and Goerling to introduce an empirical way for reducing the weight by using a recipe to cut off some finite terms. We believe that in fact a parameter-free exact exchange-only formalism is not sufficient to yield good optical spectra because the neglect of the correlation (further order terms of their expansion) might not be justified. In fact the reduction Kim and Görling have applied to the weight of the interactions could come naturally if one sums up also terms coming from the correlation part of their expansion. This should somehow introduce a dependence of the terms on the screening, which is the important information carried by the parameter $\alpha \propto 1/\varepsilon_{\infty}$ of our formulation. This dependence cannot come out from an exchange only term. Further correlation terms should act in such a way to screen the exchange-only contribution.

### III. CONCLUSIONS

In conclusion, we have examined the effects of a static long-range contribution, stemming from the electron-hole interaction, to the exchange-correlation kernel of time-dependent density functional theory. We have shown results for the real and imaginary part of the dielectric function and for the loss function for various semiconductors exhibiting a strong continuum exciton effect. Our calculations demonstrate that this very simple approximation yields excellent agreement between the calculated TDDFT absorption spectra and experiments, as well as for the real part of the dielectric function. We have shown and explained how energy-loss spectra can also be described by this approximation, but not at the same time and with the same parameter as the absorption spectra. More work must hence be done in order to include other terms beyond the static long-range one in that case. However, the breakthrough concerning absorption spectra already allows one to predict the parameter $\alpha$, and hence the optical spectra, for the class of materials considered here, and gives a strong motivation for searching simple ways to extend the limits of validity of the present approach towards more complex systems, without resorting to the significantly more complicated kernels that have been proposed recently.

### ACKNOWLEDGMENTS

This work was supported in part by the European Community Contract No. HPRN-CT-2000-00167, and by the French "Ministère de Recherche" in the framework of the program "ACI Nanostructures" under the Contract No. N52-01. Computer time was granted by IDRIS (Project No. 020544) on the NEC SX5. Ground-state calculations have been done using LSI-CP (http://theory.lsi.polytechnique.fr/ codes/), ABINIT (http://www.abinit.org), and PWSCF (http://www.pwscf.org). All TDDFT, GW, and Bethe- Salpeter calculations have been done using, respectively, the DP, LSI-GW, and EXC codes (http://theory.lsi.

polytechnique.fr/codes/). The LSI-GW code is now freely available in the ABINIT project. A.R. acknowledges support from the École Polytechnique during a sabbatical leave in 2001 where this work was started. A.R. was partially sup- ported by DGES (Grant No. MAT2001-0946) and Basque Country University. We are grateful to A.G. Marinopoulos for useful discussions and we thank Andrea Cucca for his help.

$^{1}$P. Hohenberg and W. Kohn, Phys. Rev. $\mathbf{136}$, B864 (1964).
$^{2}$W. Kohn and L.J. Sham, Phys. Rev. $\mathbf{140}$, A1133 (1965).
$^{3}$R.W. Godby, M. Schlüter, and L. Sham, Phys. Rev. B $\mathbf{35}$, 4170 (1987).
$^{4}$w. Aulbur, L. Jönsson, and J.W. Wilkins, Solid State Phys. $\mathbf{54}$, 1 (1999).
$^{5}$F. Aryasetiawan and O. Gunnarsson, Rep. Prog. Phys. $\mathbf{61}$, 237 (1998).
$^{6}$S. Albrecht, L. Reining, R. Del Sole, and G. Onida, Phys. Rev. Lett. $\mathbf{80}$, 4510 (1998).
$^{7}$E. Runge and E.K.U. Gross, Phys. Rev. Lett. $\mathbf{52}$, 997 (1984).
$^{8}$E.K.U. Gross, F.J. Dobson, and M. Petersilka, *Density Functional Theory* (Springer, New York, 1996).
$^{9}$G. Onida, L. Reining, and A. Rubio, Rev. Mod. Phys. $\mathbf{74}$, 601 (2002).
$^{10}$G. Onida, L. Reining, R.W. Godby, R. Del Sole, and W. Andreoni, Phys. Rev. Lett. $\mathbf{75}$, 818 (1995).
$^{11}$L.X. Benedict, E.L. Shirley, and R.B. Bohn, Phys. Rev. B $\mathbf{57}$, R9385 (1998).
$^{12}$M. Rohlfing and S.G. Louie, Phys. Rev. Lett. $\mathbf{81}$, 2312 (1998).
$^{13}$M. Petersilka, E.K.U. Gross, and K. Burke, Int. J. Quantum Chem. $\mathbf{80}$, 532 (2000).
$^{14}$L. Reining, V. Olevano, A. Rubio, and G. Onida, Phys. Rev. Lett. $\mathbf{88}$, 066404 (2002).
$^{15}$R. Del Sole, G. Adragna, V. Olevano, and L. Reining, Phys. Rev. B $\mathbf{67}$, 045207 (2003).
$^{16}$F. Sottile, V. Olevano, and L. Reining, Phys. Rev. Lett. $\mathbf{91}$, 056402 (2003).
$^{17}$G. Adragna, R. Del Sole, and A. Marini, Phys. Rev. B $\mathbf{68}$, 165108 (2003).
$^{18}$A. Marini, R. Del Sole, and A. Rubio, Phys. Rev. Lett. $\mathbf{91}$, 256402 (2003).
$^{19}$V.I. Gavrilenko and F. Bechstedt, Phys. Rev. B $\mathbf{55}$, 4343 (1997).
$^{20}$I.V. Tokatly and O. Pankratov, Phys. Rev. Lett. $\mathbf{86}$, 2078 (2001).
$^{21}$P. de Boeij, F. Kootstra, J. Berger, R. van Leeuwen, and G. Snijders, J. Chem. Phys. $\mathbf{115}$, 1995 (2002).
$^{22}$I.V. Tokatly, R. Stubner, and O. Pankratov, Phys. Rev. B $\mathbf{65}$, 113107 (2002).
$^{23}$A. Görling, Phys. Rev. A $\mathbf{57}$, 3433 (1998).
$^{24}$Y. Kim and A. Görling, Phys. Rev. B $\mathbf{66}$, 035114 (2002).
$^{25}$Y. Kim and A. Görling, Phys. Rev. Lett. $\mathbf{89}$, 096402 (2002).
$^{26}$K. Tatarczyk, A. Schindlmayer, and M. Scheffler, Phys. Rev. B $\mathbf{63}$, 235106 (2001).
$^{27}$R.W. Godby and R.J. Needs, Phys. Rev. Lett. $\mathbf{62}$, 1169 (1989).
$^{28}$P. Lautenschlager, M. Garriga, L. Viña, and M. Cardona, Phys. Rev. B $\mathbf{36}$, 4821 (1987).
$^{29}$P. Lautenschlager, M. Garriga, S. Logothetidis, and M. Cardona, Phys. Rev. B $\mathbf{35}$, 9174 (1987).
$^{30}$M.K.M. Garriga and K. Ploog, Thin Solid Films $\mathbf{233}$, 122 (1993).
$^{31}$D. Aspnes and A. Studna, Phys. Rev. B $\mathbf{27}$, 985 (1983).
$^{32}$We adopt the most largely used notation in the naming of the structures appearing in the spectra. The reader is invited to refer to Fig. 1(a) for an explication of the convention.

$^{33}$D.M. Roessler and W.C. Walker, Phys. Rev. $\mathbf{159}$, 733 (1967).
$^{34}$D. Edwards and H. Philipp, *Handbook of Optical Constants of Solids*, edited by E.D. Palik (Academic Press, Orlando, 1985).
$^{35}$M. Rohlfing and S. Louie, Phys. Rev. B $\mathbf{62}$, 4927 (2000), and references therein.
$^{36}$B. Arnaud and M. Alouani, Phys. Rev. B $\mathbf{63}$, 085208 (2001).
$^{37}$M. Hybertsen and S. Louie, Phys. Rev. B $\mathbf{35}$, 5585 (1987).
$^{38}$A. Dal Corso, S. Baroni, and R. Resta, Phys. Rev. B $\mathbf{49}$, 5323 (1994).
$^{39}$H.H. Li, J. Phys. Chem. Ref. Data $\mathbf{9}$, 561 (1980).
$^{40}$L. Pavesi and M. Guzzi, J. Appl. Phys. $\mathbf{75}$, 4779 (1994).
$^{41}$T. Ruf, M. Cardona, C.S.S. Pickles, and R. Sussmann, Phys. Rev. B $\mathbf{62}$, 16 578 (2000).
$^{42}$S. Baroni, S. de Gironcoli, A. Dal Corso, and P. Giannozzi, Rev. Mod. Phys. $\mathbf{73}$, 515 (2001).
$^{43}$At $\omega=0$ DFPT and TDDFT are equivalent.
$^{44}$Z.H. Levine and D.C. Allan, Phys. Rev. B $\mathbf{43}$, 4187 (1991).
$^{45}$P. Pavone, K. Karon, O. Schmitt, W. Windl, D. Strandt, P. Gian- nozzi, and S. Baroni, Phys. Rev. B $\mathbf{48}$, 3156 (1993).
$^{46}$J. Stiebling, Z. Phys. B $\mathbf{31}$, 355 (1978).
$^{47}$V. Olevano and L. Reining, Phys. Rev. Lett. $\mathbf{86}$, 5962 (2001).
$^{48}$S. Logothetidis and J. Petalas, J. Appl. Phys. $\mathbf{80}$, 1768 (1996).
$^{49}$E.L. Shirley, Phys. Rev. B $\mathbf{54}$, 7758 (1996).
$^{50}$G. Adragna, Ph.D. thesis, University of Rome "Tor Vergata," 2003.
$^{51}$F. Sottile, K. Karlsson, L. Reining, and F. Aryasetiawan, Phys. Rev. B $\mathbf{68}$, 205112 (2003).
$^{52}$Strictly speaking, it is anyway only this asymptotic part that is rigorously predicted by the derivation of Ref. 14.
$^{53}$To be precise, it has been shown that also a short range $f_{xc}$ can simulate certain features of optical spectra, in particular bound excitons (Ref. 51), provided that the short-range kernel is strong enough and contains enough spatial degrees of freedom. The former condition explains why the relatively weak kernel of TDLDA cannot work, neither on top of a DFT-LDA nor on top of a GW band structure. However, the short-range kernel has been derived from a model, contact, electron-hole interaction $W$ [the true $W$ is of course long-ranged with an asymptotic behavior as $1/(\varepsilon_{\infty}r)$, even in the presence of screening] and should there- fore, as discussed in Ref. 51, just be viewed as a mathematical tool; as a consequence, no prescription has been found how to determine its strength except for a fit to experiment, not even as a tendency.
$^{54}$R.W. Godby and L. Sham, Phys. Rev. B $\mathbf{49}$, 1849 (1994).
$^{55}$X. Gonze, P. Ghosez, and R.W. Godby, Phys. Rev. Lett. $\mathbf{74}$, 4035 (1995).
$^{56}$W.G. Aulbur, L. Jönsson, and J. Wilkins, Phys. Rev. B $\mathbf{54}$, 8540 (1996).
$^{57}$G. Vignale and W. Kohn, in *Electronic Density Functional Theory: Recent Progress and New Directions*, edited by J. Dob- son *et al.* (Plenum, New York, 1998).

155112-14