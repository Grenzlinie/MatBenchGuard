# Electrocaloric effect in PbZrO₃ thin films with antiferroelectric-ferroelectric phase competition

E. Glazkova-Swedberg, J. Cuozzo, S. Lisenkov *, I. Ponomareva

Department of Physics, University of South Florida, Tampa, FL 33620, USA

---

## ARTICLE INFO

**Article history:**
Received 9 September 2016
Received in revised form 25 October 2016
Accepted 4 December 2016

**Keywords:**
Electrocaloric effect
Ferroelectric-antiferroelectric transitions
First-principle-based methods

## ABSTRACT

Electrocaloric effect in antiferroelectric PbZrO₃ thin films that undergo antiferroelectric-ferroelectric phase transition upon cooling down is investigated using atomistic first-principles-based simulations. It is found that such a phase transition is associated with a large positive electrocaloric response that can reach 13 K under electric field of 500 kV/cm. High tunability of the phase transition by the electric field leads to a wide range of temperatures associated with strong electrocaloric response. Epitaxial strain was found to provide further tunability to the electrocaloric properties. Large intrinsic electrocaloric effect at the antiferroelectric-ferroelectric phase transition and its high tunability by the electric field offer promising technological applications.

© 2016 Elsevier B.V. All rights reserved.

---

Electrocaloric effect (ECE) is defined as a reversible change in temperature under adiabatic application of an electric field. Alternatively, the effect can be quantified by an isothermal entropy change. The effect has received much attention in the recent years owing to its potential promise for room temperature cooling applications [1–3]. The ECE can be both positive and negative. The positive effect is associated with an increase in temperature under adiabatic application of the electric field, while the negative effect results in a decrease in temperature when the electric field increases. Positive effect typically occurs in paraelectric and ferroelectric phases [4]. Note, however, that in ferroelectric (FE) phase the effect can be negative if the electric field is non-collinear with the polarization [5] or in the presence of defects [6]. On the other hand, antiferroelectric (AFE) phases are associated with negative ECE [7–9]. One interesting question that has not received much attention in the literature is the ECE in materials that exhibit an AFE-FE phase transition and/or phase competition in the absence of an electric field [10]. Such transitions occur, for example, in Zr rich Pb(ZrₓTi₁₋ₓ)O₃ alloys [11], PbZrO₃ with defects [12,13] and in thin PbZrO₃ films [14–19]. From one point of view, a phase competition can make a material very susceptible to the electric field and, therefore, may lead to the enhancement of the ECE. Indeed, paraelectric-FE as well as FE-FE phase transitions are usually associated with enhanced ECE. Recently, it was proposed that AFE-FE phase competition could be responsible for the giant ECE in a relaxor Pb₀.₈Ba₀.₂ZrO₃ film at room temperature [20]. A giant ECE was estimated at the electric field induced AFE-FE phase transition [21]. On the other hand, the ECE in AFE and FE phases exhibits opposite signs [8,10,22], which may potentially lead to a reduction of the electrocaloric response at the AFE-FE phase transition. Similarly, it is presently unknown what contribution the AFE-FE phase competition makes to the isothermal entropy change. Could such a transition be responsible for the giant value of 46.9 J/K kg reported experimentally [20]?

Motivated by seeking an answer to these questions we use the first-principles-based atomistic simulations to study PbZrO₃ thin films that exhibit AFE-FE phase transition upon cooling down. Experimentally (001)₀-oriented 200 nm thick PbZrO₃ films exhibit FE behavior up to a temperature of about 60 K [19]. Above this temperature the films show AFE behavior. In the same experiment it was found that (120)₀-oriented 120 nm thick PbZrO₃ films show a mixed FE and AFE phases with the FE phases being more stable at low temperatures and AFE phase becoming dominant above the room temperature. Computationally, the AFE-FE phase transition in a 5 nm thick film was predicted to occur at 380 K [23]. At present it is not possible to simulate 200 nm thick film atomistically. So we model an ultrathin PbZrO₃ film of 5 nm thickness grown along the [001] pseudocubic direction. Periodic boundary conditions are applied along the film's in-plane directions, while no periodic boundary conditions are simulated along the film's growth direction. The total energy of the film modeled by 12 × 12 × 12 supercell is given by the first-principles effective Hamiltonian for PbZrO₃[24] whose degrees of freedom are local modes, $\mathbf{u}_i$, that are proportional to the dipole moment of the unit cell i, local

---

* Corresponding author.
E-mail address: slisenk@usf.edu (S. Lisenkov).

http://dx.doi.org/10.1016/j.commatsci.2016.12.002
0927-0256/© 2016 Elsevier B.V. All rights reserved.

strains, $\boldsymbol{\eta}_{i}$, and antiferrodistortive rotation of oxygen octahedra, $\boldsymbol{\omega}_{i}$.
The effective Hamiltonian is expanded as [24]

$$
\begin{aligned}
E^{\mathrm{tot}} & =E^{\mathrm{AFE}}\left(\left\{\mathbf{u}_{i}\right\}\right)+E^{\mathrm{AFD}}\left(\left\{\boldsymbol{\omega}_{i}\right\}\right)+E^{\mathrm{elas}}\left(\left\{\boldsymbol{\eta}_{i}\right\}\right)+E^{\mathrm{AFE}-\mathrm{elas}}\left(\left\{\mathbf{u}_{i}, \boldsymbol{\eta}_{i}\right\}\right) \\
& +E^{\mathrm{AFD}-\mathrm{elas}}\left(\left\{\boldsymbol{\omega}_{i}, \boldsymbol{\eta}_{i}\right\}\right)+E^{\mathrm{AFE}-\mathrm{AFD}}\left(\left\{\mathbf{u}_{i}, \boldsymbol{\omega}_{i}\right\}\right),
\end{aligned}
\tag{1}
$$

where $E^{\mathrm{AFE}}$ is the energy associated with the antiferroelectric $\Sigma_{2}$
mode and includes contributions from the dipole-dipole interac-
tions, short-range interaction, and on-site self energy. $E^{\mathrm{AFD}}$ gives
the energy due to the antiferrodistortive mode that is similar to
$E^{\mathrm{AFE}}$ but excludes the dipole-dipole interactions as antiferrodis-
tortive local modes are nonpolar. The third term, $E^{\mathrm{elas}}$, is the elastic
energy associated with the unit cell deformation. The terms
$E^{\mathrm{AFE}-\mathrm{elas}}, E^{\mathrm{AFD}-\mathrm{elas}}$, and $E^{\mathrm{AFE}-\mathrm{AFD}}$ are the energy contributions due the
interactions between the AFE mode and the strain, the antiferrodis-
tortive mode and the strain, and the AFE and antiferrodistortive
modes, respectively.

The Hamiltonian correctly reproduces many electrical and ther-
modynamical properties of $\mathrm{PbZrO}_{3}$. In particular, it accurately pre-
dicts the AFE-FE phase transition and the dipole pattern associated
with it, electric hysteresis loops and $\mathrm{PbZrO}_{3}$ behavior under pres-
sure. The Curie point of 946 K, however, overestimates the experi-
mental value of 503 K. Previously, this Hamiltonian was used to
explain stabilization of the FE phases in $\mathrm{PbZrO}_{3}$ films [23] and pre-
dict the emergence of the FE phases in other low-dimensional struc-
tures of $\mathrm{PbZrO}_{3}$ [25]. The FE phases in $\mathrm{PbZrO}_{3}$ films are very
sensitive to the surface charge compensation [23,25,26]. In partic-
ular, the FE phases can only develop if the polarization surface
charge is well screened by free carriers [23,25]. To simulate the
surface charge screening we apply a compensating field
$\mathbf{E}_{\text{comp}}=-\beta \mathbf{E}_{\text{dep}}$ that opposes the depolarizing field, $\mathbf{E}_{\text{dep}}$, associated
with the polarization surface charge [25,27]. The screening param-
eter $\beta$ can vary from 0 to 1 which correspond to $0 \%$ and $100 \%$ of the
surface charge screened, respectively. Realistic surface charge com-
pensation is associated with $\beta$ in between these limiting values. To
equilibrate films at different temperatures we use the simulated
annealing technique. The annealing starts at 955 K and proceeds
in decrements of 25 K until the temperature reaches 5 K. At each
temperature the film is equilibrated using 40,000 Metropolis
Monte Carlo sweeps with interactions modeled by the effective
Hamiltonian. To model the response of the film to the electric field,
$\mathbf{E}$, we apply the field along the film's growth direction. Previously, a
similar computational approach was used to explain emergence of
the FE phases in $\mathrm{PbZrO}_{3}$ ultrathin films and predict the onset of fer-
roelectricity in other $\mathrm{PbZrO}_{3}$ nanostructures [23,25,26].

Fig. 1(a) shows polarization vs electric field loops ($P(E)$ loops)
computed for the $\mathrm{PbZrO}_{3}$ film at different temperatures. The film
has $97.5 \%$ of its polarization surface charge compensated by free
carriers. At the highest temperature the film exhibits paraelectric
behavior, while at 500 K it shows typical AFE behavior. For the low-
est temperature reported in Fig. 1(a) the film exhibits a sponta-
neous reversible polarization associated with a FE behavior.
Hysteresis loops were computed in the temperature range of 5-
955 K in steps of 25 K. For each temperature the zero field positive
value of polarization was used to plot the polarization, $\mathbf{P}$, as a func-
tion of temperature in Fig. 1(b). In addition, we also report the AFE
order parameter as a function of temperature in the same figure.
The AFE order parameter is computed by averaging the local modes
in the $\Sigma_{2}$ point of the Brillouin zone. The components of the strain
tensor as a function of temperature are given in Fig. 1(c). Under the
chosen boundary conditions the film exhibits an AFE to FE phase
transition at 293 K. The temperature of the AFE-FE phase transi-
tion, $T_{A-F}$, is very sensitive to surface charge compensation. Fig. 1
(d) shows the dependence of transition temperature on the screen-
ing parameter, $\beta$. Since our simulations correspond to a film sandwiched between two electrodes we can use the model of imperfect
screening to relate screening parameter to the effective screening
length of the electrodes [28]. In such a model the finite screening
length of the electrodes, $\lambda_{\text{eff}}$, leads to the appearance of the residual
depolarizing field in a polar film sandwiched between two elec-
trodes. The compensating electric field due to the electrodes,
$\mathbf{E}_{\text{comp}}$, is related to the residual depolarizing field in the polar film,
$\mathbf{E}_{\text{dep}}$, as

$$
\mathbf{E}_{\text{comp}}=-\frac{\mathbf{E}_{\text{dep}} d}{d+2 \lambda_{\text{eff}}}
\tag{2}
$$

where $d$ is the film's thickness. Since in our model the compensating
field is given by $\mathbf{E}_{\text{comp}}=-\beta \mathbf{E}_{\text{dep}}$ we obtain

$$
\lambda_{\text{eff}}=\frac{d(1-\beta)}{2 \beta}
\tag{3}
$$

The screening parameter of $97.5 \%$ corresponds to the effective
screening length of $0.6 \mathring{A}$. For metals the screening length ranges
from 0.23 to $0.6 \mathring{A}$ [28-30].

Next we turn to the investigation of the ECE using the compu-
tational technique that models the experimental indirect approach
[8,20,22]. In such an approach the $P(E)$ loops obtained for temper-
atures ranging from 5 to 955 K in steps of 25 K are used to compute
the dependence of polarization on temperature for different values
of an electric field. More precisely, the upper branches of $P(E>0)$
loops (see Fig. 1(a) for an example) were used to obtain $P(T)$ curves
plotted in Fig. 2(a). The most notable feature of these curves is a
significant shift in the AFE-FE transition temperature under applied
electric field. The data plotted in Fig. 2(a) are then used to estimate
the electrocaloric temperature change, $\Delta T$, and isothermal entropy
change, $\Delta S$, from Maxwell relations

$$
\Delta T=-\frac{1}{\rho} \int_{0}^{E} \frac{T}{C}\left(\frac{\partial P}{\partial T}\right)_{E} d E
\tag{4}
$$

$$
\Delta S=-\frac{1}{\rho} \int_{0}^{E}\left(\frac{\partial P}{\partial T}\right)_{E} d E
\tag{5}
$$

Here we used $C=302 \mathrm{~J} \times \mathrm{kg} / \mathrm{K}$ [31] and $\rho=8.3 \mathrm{~g} / \mathrm{cm}^{3}$ [22]. For
numerical integration of Eqs. (4) and (5) the computational depen-
dencies $P(T)$ obtained for different electric fields and shown in
Figs. 2(a) and 3(b) were smoothed using Bezier interpolation
scheme before computing the derivatives $\left(\frac{\partial P}{\partial T}\right)_{E}$ numerically. We
use computational data in the temperature interval [5:955] K col-
lected with steps of 25 K and for electric fields 50 kV/cm and
[100:600] kV/cm with steps of 100 kV/cm. Interpolation of compu-
tational data for $P(T)$ smooths features of the electrocaloric $\Delta T$.

Fig. 2(b) and (c) give the electrocaloric change in temperature
and isothermal entropy change, respectively, as a function of tem-
perature. The data indicate that the ECE is mostly positive reaching
negative values in the AFE phase in the vicinity of the Curie point.
The coexistence of positive and negative ECE similar to the one
found in computations has been observed experimentally in (Pb,
La) $(\mathrm{Zr}, \mathrm{Sn}, \mathrm{Ti}) \mathrm{O}_{3}$ single crystal [10]. Under an electric field of
500 kV/cm the maximum $\Delta T$ value reaches 13 K which compares
well with the experimental value of 12 K obtained in $\mathrm{PbZr}_{0.95} \mathrm{Ti}_{0.05^{-}}$
$\mathrm{O}_{3}$ films under similar electric field [22]. A notable feature of the
electrocaloric response is the broadness of $\Delta T(T)$. The FWHM of
$\Delta T(T)$ under 500 kV/cm electric field is 317 K which compares
favorably to 120 K in $\mathrm{PbZr}_{0.95} \mathrm{Ti}_{0.05} \mathrm{O}_{3}$ films [22]. The room temper-
ature is within the half maximum range of $\Delta T$. More precisely, at
room temperature $\Delta T$ reaches 7 K under the field of 500 kV/cm.
It should be noted that the room temperature in computations is
$0.3 T_{C}$, while experimentally it is $0.6 T_{C}$, where $T_{C}$ is the Curie tem-
perature of $\mathrm{PbZrO}_{3}$. This difference is due to the overestimation
of $T_{C}$ by the effective Hamiltonian. Nevertheless given that in both

![](./images/811093180815507457_1.jpg)

Fig. 1. (a) Hysteresis loops in PbZrO₃ film at different temperatures. The polarization is along the growth direction. (b) Cartesian components of polarization and AFE order parameter as a function of temperature. AFE order parameter is reported relative to the computational lattice constant of cubic PbZrO₃. (c) Temperature dependence of the largest (ηᵢ), medium (ηⱼ) and smallest (ηₖ) components of the strain tensor in Voigt notations. (d) Dependence of the AFE-FE transition temperature on the screening parameter β.

![](./images/811093180815507457_2.jpg)

Fig. 2. (a) Temperature dependence of the polarization under different electric fields for the PbZrO₃ film. Electrocaloric ΔT (b) and isothermal entropy change (c) as a function of temperature for different values of the applied electric field. Data correspond to β = 0.975.

computations and experiments the room temperature is signifi- cantly below the Curie point we expect accurate qualitative predic- tions. We find that ECE is positive at the AFE-FE phase transition which is attributed to the negative slope of $\frac{dP}{dT}$ (see Fig. 2(a)). The largest ΔS under the electric field of 500 kV/cm reaches 9 J/kg K, which compares well with the experimental value of 8 J/kg K for PbZr₀.₉₅Ti₀.₀₅O₃ films [22] and is within the range of the values reported in the literature [20].

Next we investigate the effect of epitaxial strain on the elec- trocaloric properties of the film. Fig. 3(a) gives the dependence of the AFE-FE transition temperature on the epitaxial strain for the case of good surface charge compensation, namely β = 0.98. The epitaxial strain is defined with respect to zero Kelvin computa- tional lattice constant of cubic PbZrO₃ of 4.1 Å. For the epitaxial strain in the range of −1% to 2% we do not observe the AFE-FE phase transition. To understand why the stabilization of the FE tetragonal phase requires relatively large compressive strain we notice that the FE phase is associated with the in-plane sponta- neous strain of −2% (see Fig. 1(c)). Therefore, strains greater than −1.5% are too weak to stabilize the FE phase. It should be noted that first-principles zero Kelvin calculations suggest that the FE rhombohedral phase is stable for the entire range of compressively

![](./images/811093180815507457_3.jpg)

Fig. 3. (a) Phase diagram for the AFE-FE phase transition in $PbZrO_3$ film with 98% of its surface charge compensated. (b) Temperature dependence of the polarization under different electric fields in $PbZrO_3$ film under a compressive strain of $-1.5\%$ and $\beta=0.98$. Electrocaloric $\Delta T$ (c) and isothermal entropy change (d) as a function of temperature for different values of applied electric field. Data correspond to $\beta=0.98$ and an epitaxial strain of $-1.5\%$.

strained $PbZrO_3$ bulk [18]. A notable feature of the phase diagram in Fig. 3(a) is the tunability of $T_{A-F}$ by the epitaxial strain. Indeed, $T_{A-F}$ increases very rapidly as the compressive strain increases in magnitude. To investigate the role of epitaxial strain on the electrocaloric properties we focus on the compressive strain of $-1.5\%$ since for this case $T_{A-F}$ is below the room temperature and our computations suggest that maximum ECE occurs above $T_{A-F}$ (see Fig. 2(b)). The $P(T)$ curves for this case are given in Fig. 3(b) and reveal that, just as in the stress-free case, the electric field has a pronounced effect on $T_{A-F}$. One feature that differentiates these curves from the ones obtained for the stress-free films is the relatively weak response to the lower electric fields for the temperatures below 200 K. The origin of this feature is the formation of a monoclinic phase associated with significantly smaller $\eta_3$ strain component, or elastic deformation along the growth direction. As the temperature is lowered below 200 K the spontaneous strain associated with tetragonal FE phase ($\eta_1$ and $\eta_2$ components of the strain tensor) decreases significantly below the value of epitaxial compressive strain of $-1.5\%$ (see Fig. 1(c) for the spontaneous strain in the stress-free film). The structure's response to this new unfavorable condition is the formation of a new low symmetry phase that is associated with a weaker response to the electric field as compared to the FE tetragonal phase. The electrocaloric $\Delta T$ and $\Delta S$ are given in Fig. 3(c) and (d), respectively. The maximum electrocaloric $\Delta T$ in this case is smaller than that for the stress-free film. However, the range of the temperatures with significant $\Delta T$ is much wider. Similar observation holds for $\Delta S(T)$. This is in agreement with the findings for ferroelectric thin films [32-34].

At the same time effective Hamiltonian simulations of strained $BaTiO_3$ [34] predicted the enhancement of the electrocaloric $\Delta T$ as compared to the stress-free value below compressive strain of $-0.75\%$. In our case the origin of the widening of electrocaloric $\Delta T$ is in the high tunability of the AFE-FE phase transition by the electric field. Indeed, the electric field can significantly shift $T_{A-F}$ as seen from Fig. 3(b). Since $T_{A-F}$ is associated with the largest values of $\frac{dP}{dT}$ and, consequently, $\Delta T$ and $\Delta S$ the shift leads to the broadening of $\Delta T(T)$ and $\Delta S(T)$ curves.

Since the ECE explored in this study involves AFE-FE phase transition the validity of the computational approach based on integration of Maxwell equations should be addressed. In Ref. [35] direct first-principles-based simulations were used to study ECE in bulk $PbZrO_3$. It was found that the AFE-FE phase transition induced by the electric field is associated with some irreversible heating due to first-order-like character of this transition. More precisely, at 800 K the irreversible heating due to both AFE-FE and reverse FE-AFE phase transition was 2 K, which is approximately 1 K per a single transition. In the films studied here the AFE-FE phase transition occurs in the temperature range of 400-600 K where the ECE ranges from 15 to 5 K, respectively, under the application of the electric field of 500 kV/cm. Taking into account the irreversible heating due to the AFE-FE phase transition is likely to slightly decrease the reported values of $\Delta T$, however, will not change the qualitative conclusions of this study. Another potential source of inaccuracy in predicted $\Delta T$ is the use of constant heat capacity in integrating Eq. (4). Debye temperature for $PbZrO_3$ is 396 K [36]. At half Debye temperature the heat capacity is reduced from the

classical Dulong-Petit value by 18%. Therefore, for temperatures below 200 K the computational data for ECE provide the lower esti- mate for the effect. At the same time this temperature range is of less practical importance. Approximation of constant heat capacity is likely to be crude in the vicinity of first-order phase transition. However, given that the range of fast variation of heat capacity is typically very narrow [37] this approximation is not expected to significantly affect our findings. Nevertheless, direct computational and experimental studies are needed to confirm the potential of AFE thin films to exhibit large ECE.

In summary, we have used atomistic first-principles-based sim- ulations to predict a significant electrocaloric effect in antiferro- electric $PbZrO_{3}$ films that undergo transition into a FE phase upon cooling down. The notable feature of the effect is the wide range of temperatures associated with strong electrocaloric response. This features derives its origin in the high tunability of the AFE-FE phase transition temperature by the applied electric field. Epitaxial compressive strain was found to critically affect $T_{A-F}$ and, therefore, could be used to tune the electrocaloric response in $PbZrO_{3}$ films. In particular, we found that an epitaxial compressive strain of $-1.5\%$ decreases $T_{A-F}$ as compared to the stress-free case and leads to the reduction of the maximum elec- trocaloric $\Delta T$. On the other hand, the same strain results in signif- icant widening of $\Delta T(T)$ and $\Delta S(T)$ curves which we attribute to the increased tunability of AFE-FE by the applied electric field. Our findings suggest that AFE films that exhibits FE phases could be promising candidates for applications that utilize ECE. This conclu- sion is likely to hold for a wider class of materials that exhibit AFE- FE phase transition and competition.

Financial support for this work provided by the National Science Foundation Grant No. DMR-1250492 and MRI CHE-1531590. The authors would like to acknowledge the use of the services provided by Research Computing at the University of South Florida.

## References

[1] S.-G. Lu, Q. Zhang, Adv. Mater. 21 (2009) 1983.
[2] J.F. Scott, Ann. Rev. Mater. Sci. 41 (2011) 229.
[3] X. Moya, S. Kar-Narayan, N.D. Mathur, Nat. Mater. 13 (2014) 439.
[4] J. Peräntie, J. Hagberg, A. Uusimäki, H. Jantunen, Phys. Rev. B 82 (2010) 134119.
[5] I. Ponomareva, S. Lisenkov, Phys. Rev. Lett. 108 (2012) 167604.

[6] Y.-B. Ma, A. Grünebohm, K.-C. Meyer, K. Albe, B.-X. Xu, Phys. Rev. B 94 (2016) 094113.
[7] R. Pirc, B. Roi, J. Koruza, B. Mali, Z. Kutnjak, Europhys. Lett. 107 (2014) 17002.
[8] W. Geng, Y. Liu, X. Meng, L. Bellaiche, J.F. Scott, B. Dkhil, A. Jiang, Adv. Mater. 27 (2015) 3165.
[9] S. Lisenkov, B.K. Mani, E. Glazkova, C.W. Miller, I. Ponomareva, Sci. Rep. 6 (2016) 19590.
[10] F. Zhuo, Q. Li, J. Gao, Y. Wang, Q. Yan, Y. Zhang, X. Xi, X. Chu, W. Cao, Appl. Phys. Lett. 108 (2016).
[11] X. Tan, C. Ma, J. Frederick, S. Beckman, K.G. Webber, J. Am. Ceram. Soc. 94 (2011) 4091.
[12] G. Shirane, S. Hoshino, Acta Crystallogr. 7 (1954) 203.
[13] L. Benguigui, J. Solid State Chem. 3 (1971) 381.
[14] P. Ayyub, S. Chattopadhyay, R. Pinto, M.S. Multani, Phys. Rev. B 57 (1998) R5559.
[15] J. Zhai, Y. Yao, X. Li, T.F. Hung, Z.K. Xu, H. Chen, E.V. Colla, T.B. Wu, J. Appl. Phys. 92 (2002) 3990.
[16] A. Roy Chaudhuri, M. Arredondo, A. Hähnel, A. Morelli, M. Becker, M. Alexe, I. Vrejoiu, Phys. Rev. B 84 (2011) 054112.
[17] K. Boldyreva, L. Pintilie, A. Lotnyk, I.B. Misirlioglu, M. Alexe, D. Hesse, Appl. Phys. Lett. 91 (2007) 122915.
[18] S.E. Reyes-Lillo, K.M. Rabe, Phys. Rev. B 88 (2013) 180102.
[19] L. Pintilie, K. Boldyreva, M. Alexe, D. Hesse, J. Appl. Phys. 103 (2008).
[20] B. Peng, H. Fan, Q. Zhang, Adv. Funct. Mater. 23 (2013) 2987.
[21] Y. Zhao, X. Hao, Q. Zhang, J. Mater. Chem. C 3 (2015) 1694.
[22] A.S. Mischenko, Q. Zhang, J.F. Scott, R.W. Whatmore, N.D. Mathur, Science 311 (2006) 1270.
[23] B.K. Mani, C.-M. Chang, S. Lisenkov, I. Ponomareva, Phys. Rev. Lett. 115 (2015) 097601.
[24] B.K. Mani, S. Lisenkov, I. Ponomareva, Phys. Rev. B 91 (2015) 134112.
[25] B.K. Mani, R. Herchig, E. Glazkova, S. Lisenkov, I. Ponomareva, Nanotechnology 27 (2016) 195705.
[26] R. Herchig, B. Mani, S. Lisenkov, I. Ponomareva, Comput. Mater. Sci. 117 (2016) 468.
[27] I. Ponomareva, I.I. Naumov, I. Kornev, H. Fu, L. Bellaiche, Phys. Rev. B 72 (2005) 140102.
[28] P. Ghosez, J. Junquera, Handbook of Theoretical and Computational Nanotechnology, vol. 9, American Scientific Publishers, Stevenson Ranch, CA, 2006, pp. 623-728.
[29] M. Dawber, P. Chandra, P.B. Littlewood, J.F. Scott, J. Phys.: Cond. Matt. 15 (2003) L393.
[30] R.R. Mehta, B.D. Silverman, J.T. Jacobs, J. Appl. Phys. 44 (1973) 3379.
[31] E. Sawaguchi, G. Shirane, Y. Takagi, J. Phys. Soc. Jpn. 6 (1951) 333.
[32] G. Akcay, S.P. Alpay, J.V. Mantese, G.A. Rossetti, Appl. Phys. Lett. 90 (2007) 252909.
[33] J. Zhang, A.A. Heitmann, S.P. Alpay, G.A. Rossetti, J. Mater. Sci. 44 (2009) 5263.
[34] M. Marathe, C. Ederer, Appl. Phys. Lett. 104 (2014) 212902, http://dx.doi.org/10.1063/1.4879840.
[35] S. Lisenkov, B.K. Mani, E. Glazkova, C.W. Miller, I. Ponomareva, Sci. Rep. 6 (2016) 19590.
[36] W.N. Lawless, Phys. Rev. B 30 (1984) 6555.
[37] E.A. Mikhaleva, I.N. Flerov, M.V. Gorev, M.S. Molokeev, A.V. Cherepakhin, A.V. Kartashev, N.V. Mikhashenok, K.A. Sablina, Phys. Solid State 54 (2012) 1832.