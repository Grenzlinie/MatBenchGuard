Accepted manuscript. The final version was published in:
Journal of Magnetism and Magnetic Materials **527**, 167767 (2021),
DOI:10.1016/j.jmmm.2021.167767

# Magnetocaloric and electrocaloric properties of the Hubbard pair cluster

K. Szałowski$^{a,*}$, T. Balcerzak$^{a}$

$^{a}$Department of Solid State Physics, Faculty of Physics and Applied Informatics,
University of Łódź, ulica Pomorska 149/153, 90-236 Łódź, Poland

## Abstract
The paper contains the discussion of the magnetocaloric and electrocaloric effect in a model dimer (pair cluster). The system of interest is modelled with a Hubbard Hamiltonian including the external electric and magnetic field. The thermodynamics of such pair is described exactly, on the grounds of the grand canonical ensemble, focusing on the half-filling of energy states. The quantities of interest, such as magnetic entropy, magnetic specific heat as well as isothermal entropy change resulting from the variation of either electric or magnetic field and appropriate Grüneisen ratios are calculated and discussed in a wide range of external fields. The importance of singlet to triplet transition for the observed behaviour is emphasized. The ranges of direct and inverse caloric effects are found and the manifestations of the magnetoelectric phenomena are described. In particular, the tunability of the magnetocaloric effect with electric field as well as tunability of the electrocaloric effect with magnetic field are demonstrated.

Keywords: magnetocaloric effect, electrocaloric effect, Hubbard model, exact diagonalization, dimer

## 1. Introduction
The search for nanodevices stimulates strongly the search for novel approaches to refrigeration in relevant scale, ranging from nano- to mesoscale, exploiting a plethora of physical phenomena [1, 2, 3]. Among various strategies adopted to achieve the goal of on-chip cooling, one of the successful approaches is based on magnetocaloric effect (MCE)[4, 5], manifesting itself for example in a form of temperature drop during adiabatic demagnetization [6]. This principle has been demonstrated and used for effective on-chip cooling on the basis of such subsystems as single magnetic ions [7], thin magnetic films [8] or nuclear magnetic moments [9, 10, 11]. Analogous mechanism has already been observed in molecular nanomagnets [12]. Another, less frequently investigated caloric effect connected with the variability of the external electric fieldis electrocaloric effect (ECE) [13, 14]. Both effects give hopes for efficient solid state-based cooling [15] and motivate constant quest for novel materials and concepts, including especially quantum materials [16].

The finite cluster nanosystems exhibit typically quantum level crossings [17, 18] - the points in which the ground state of the system changes when some control parameter (like the external electric or magnetic field) is varied. Their presence manifests itself in the experiment, for example, as a rapid change of the total magnetization of the system at a certain critical value of the field. However, the accidental state degeneracy at the quantum level crossing point causes also a residual entropy to emerge exactly for the critical field. This entropy has necessarily different value than the entropy at each side of the quantum level crossing point (which may be either zero when the ground state is non-degenerate or positive if it is degenerate). As a consequence, the ground-state (residual) entropy exhibits a discontinuous behaviour as a function of the field at the quantum level crossing point. The temperature would tend to smear that dependence, nevertheless, such a behaviour of the entropy makes it particularly sensitive to the external field in the vicinity of the quantum level crossing. This behaviour can be utilized to maximize the caloric effect corresponding to the external field causing the quantum level crossing.

The simplest magnetic systems with spin-spin coupling are spin dimers. In case of antiferromagnetic coupling, they exhibit a singlet-to-triplet transition (quantum level crossing) when the magnetic field is increased.

*Corresponding author
Email addresses: karol.szalowski@uni.lodz.pl (K. Szałowski), tadeusz.balcerzak@uni.lodz.pl (T. Balcerzak)
URL: https://orcid.org/0000-0002-3204-1849 (K. Szałowski), https://orcid.org/0000-0001-7267-992X (T. Balcerzak)
1

Accepted manuscript. The final version was published in:
Journal of Magnetism and Magnetic Materials 527, 167767 (2021),
DOI:10.1016/j.jmmm.2021.167767

The dimer structure can arise naturally in molecular magnets, making them a highly interesting class of materials. The mentioned phenomenon has been studied in the context of the magnetocaloric effect, for example in (coupled) Cu-based dimers with spin 1/2 [19, 20, 21] or Ni-based dimers with spin 1 [22]. It can be mentioned that also rotational magnetocaloric effect utilizing magnetic anisotropy has been studied in dimer systems based on Dy and Gd ions [23]. The phenomenon has been also found and discussed theoretically in various magnetic cluster systems, to mention such examples as the calculations for anisotropic Heisenberg polyhedra [24], Ising tetrahedra [25], edge-sharing tetrahedra and octahedra [26] or triangular lattice-based Ising nanoclusters [27, 28] and other clusters [29].

In order to enrich the number of degrees of freedom in the studied system and include two external fields - the magnetic and electric one - a natural choice is focusing the interest on a Hubbard dimer (pair). Such nanosystem exhibits an interplay between charge and spin response to the external fields, being a natural candidate system to exhibit pronounced magnetoelectric phenomena. Some properties of the system, like the chemical potential, magnetic and electric polarization and susceptibilities were studied by us in Refs. [30, 31, 32] It should be mentioned that the thermodynamics of such system can be described exactly. The Hubbard dimer has been studied also in the context of symmetries [33], density functional theory [34, 35], spectral function [36], integrals of motion [37], two-orbital model [38], orbital degeneracy [39] or the extended version of the Hubbard model [40, 41] including the electron-phonon couplings within Hubbard-Holstein model on a dimer [42]. Other cluster-based Hubbard nanostructures have also been studied [43, 44, 45], to mention especially those like cube [46, 47, 48], triangle [49, 50] and tetrahedron [49] or a finite chain [51, 52, 53].

In the paper we characterize exactly the magnetocaloric and electrocaloric effect in Hubbard dimer (pair), exploiting the plethora of phenomena caused by the simultaneous presence of electric and magnetic field. In the next section 2 we sketch the theoretical formalism used to characterize the thermodynamics of the Hubbard dimer, based on the grand canonical ensemble. In the following part 3 we present and discuss the results of the extensive numerical calculations focused on the magneto- and electrocaloric effect. The final remarks are drawn in the section 4.

## 2. Theoretical model

The Hubbard Hamiltonian for the pair of atoms (a, b) embedded in the external magnetic and electric fields is of the form:

$$
\begin{aligned}
\mathcal{H}_{a, b}= & -t \sum_{\sigma=\uparrow, \downarrow}\left(c_{a, \sigma}^{+} c_{b, \sigma}+c_{b, \sigma}^{+} c_{a, \sigma}\right) \\
& +U\left(n_{a, \uparrow} n_{a, \downarrow}+n_{b, \uparrow} n_{b, \downarrow}\right) \\
& -H\left(S_{a}^{z}+S_{b}^{z}\right)-V\left(n_{a}-n_{b}\right),
\end{aligned}
$$

where $t>0$ is the hopping integral, and $U \geq 0$ is on-site Coulomb repulsion energy. The external uniform magnetic field with magnitude $H^{z}$ is introduced by the parameter $H$, namely $H=-g \mu_{\mathrm{B}} H^{z}$. The parameter $V$ stands for the electrostatic potential of the uniform electric field oriented along the line joining both atoms, in such a way that $V=V_{a}=-V_{b}$. It is related to the electric field $E$ by the formula $V=E|e| d / 2$, where $d$ is the interatomic distance and $e$ is the electron charge.

The creation $(c_{\gamma, \sigma}^{+})$ and annihilation $(c_{\gamma, \sigma})$ operators for site $\gamma=a, b$ and spin state $\sigma=\uparrow, \downarrow$ can be used to define the corresponding occupation number operators $n_{\gamma, \sigma}$, namely:

$$
n_{\gamma, \sigma}=c_{\gamma, \sigma}^{+} c_{\gamma, \sigma}.
$$

With the help of $n_{\gamma, \sigma}$ the total occupation number operators at the site $\gamma=a, b$ are given by:

$$
n_{\gamma}=n_{\gamma, \uparrow}+n_{\gamma, \downarrow}.
$$

Moreover, the spin operators $S_{\gamma}^{z}$ in Eq.(1) are defined as follows:

$$
S_{\gamma}^{z}=\left(n_{\gamma, \uparrow}-n_{\gamma, \downarrow}\right) / 2.
$$

We consider the Hubbard pair as an open system, being able to exchange the electrons with its neighbourhood. For instance, this could be a situation where the pair cluster is placed on the metallic substrate serving as the electronic reservoir or a situation where the pair is coupled to the electrodes (gates). Taking into account the possible fluctuations of the number of electrons, the equilibrium thermodynamics of such open system is properly described by the grand canonical ensemble. In this formalism the Hamiltonian (1) is extended by adding the term $-\mu\left(n_{a}+n_{b}\right)$, where $\mu$ is the chemical potential.

The exact analytical diagonalization of the extended Hamiltonian has been performed in Ref. [30]. As a result, a set of 16 eigenenergies and corresponding eigenstates has been found, which enabled determination of

Accepted manuscript. The final version was published in:
Journal of Magnetism and Magnetic Materials 527, 167767 (2021),
DOI:10.1016/j.jmmm.2021.167767

the grand partition function $\mathcal{Z}_{a,b}$:
$$
\begin{aligned}
\mathcal{Z}_{a,b} &= \mathrm{Tr}_{a,b} \exp\{-\beta\left[\mathcal{H}_{a,b} - \mu\left(n_a + n_b\right)\right]\} \\
&= \sum_{i=1}^{16} \exp\left(-\frac{t}{k_{\mathrm{B}} T} E_i\right),
\end{aligned} \tag{5}
$$
where $E_i$ are the normalized energy eigenvalues given in the Appendix B of Ref. [30]. The grand potential, $\Omega_{a,b}$, of the open system is then given by:
$$
\Omega_{a,b} = -k_{\mathrm{B}} T \ln \mathcal{Z}_{a,b}, \tag{6}
$$
and it enables the calculation of all thermodynamic properties in equilibrium.

On the other hand, the statistical properties can be found from the statistical operator $\rho_{a,b}$:
$$
\rho_{a,b} = \frac{1}{\mathcal{Z}_{a,b}} \exp\{-\beta\left[\mathcal{H}_{a,b} - \mu\left(n_a + n_b\right)\right]\}, \tag{7}
$$
which can be constructed in a diagonal form on the basis of the diagonalized pair Hamiltonian $\mathcal{H}_{a,b}$. With the help of $\rho_{a,b}$ the statistical averages of arbitrary quantum mechanical operators can be calculated. In particular, averaging of operators $n_\gamma$, and $S_\gamma^z$, which are defined by Eqs. (3) and (4), respectively, can be performed. Namely:
$$
\left\langle n_\gamma \right\rangle = \mathrm{Tr}_{a,b} \left[ \left(n_{\gamma,\uparrow} + n_{\gamma,\downarrow}\right) \rho_{a,b} \right], \tag{8}
$$
and
$$
\left\langle S_\gamma^z \right\rangle = \mathrm{Tr}_{a,b} \left[ \frac{1}{2} \left(n_{\gamma,\uparrow} - n_{\gamma,\downarrow}\right) \rho_{a,b} \right]. \tag{9}
$$

For completeness of the method, the chemical potential $\mu$ can be self-consistently determined from the relationship:
$$
\left\langle n_a \right\rangle + \left\langle n_b \right\rangle = -\left( \frac{\partial \Omega_{a,b}}{\partial \mu} \right)_{T,H,V}. \tag{10}
$$

For studies of the magnetocaloric and electrocaloric effects the entropy $S$ of the system is a crucial quantity. The entropy as a function of $T$, $H$ and $E$ is defined by:
$$
S\left(T,H,E\right) = -\left( \frac{\partial \Omega_{a,b}}{\partial T} \right)_{H,E}, \tag{11}
$$
where the external field parameters $H$ and $E$ are constant.

Alternatively, the entropy can be expressed as:
$$
S\left(T,H,E\right) = \frac{\left\langle \mathcal{H}_{a,b} - \mu\left(n_a + n_b\right) \right\rangle - \Omega_{a,b}}{T}. \tag{12}
$$

The caloric effects, which can manifest themselves by the heat flow between the system and its environment under the external field change can be quantified with the help of the isothermal entropy changes $\Delta S_T$. For the magnetocaloric effect we define
$$
\Delta S_T^{MCE} = S(T,H=0,E) - S(T,H,E), \tag{13}
$$
i.e., $\Delta S_T$ is the isothermal change of the entropy corresponding to the jump of magnetic field from $H=0$ to $H>0$, whereas the electric field parameter $E$ is constant. Analogously, the electrocaloric effect is described by
$$
\Delta S_T^{ECE} = S(T,H,E=0) - S(T,H,E), \tag{14}
$$
where the isothermal entropy change corresponds to the jump of the electric field from $E=0$ to $E>0$, whereas the magnetic field is constant.

The known entropy of the system can also be exploited for calculation of the heat capacity, $C_{H,E}$. For the constant external field parameters $H$ and $E$, the heat capacity of the Hubbard pair cluster (dimer) is then given by:
$$
C_{H,E} = T \left( \frac{\partial S\left(T,H,E\right)}{\partial T} \right)_{H,E} = -T \left( \frac{\partial^2 \Omega_{a,b}}{\partial T^2} \right)_{H,E}. \tag{15}
$$

Applying the fluctuation-dissipation theorem, an alternative formula, particularly convenient for numerical calculations, can be derived in the following form:
$$
C_{H,E} = \frac{\left\langle \left[ \mathcal{H}_{a,b} - \mu\left(n_a + n_b\right) \right]^2 \right\rangle - \left\langle \mathcal{H}_{a,b} - \mu\left(n_a + n_b\right) \right\rangle^2}{k_{\mathrm{B}} T^2}. \tag{16}
$$

Potentially interesting parameters quantifying the response of the system to the external field are Grüneisen ratios. For the system embedded in external magnetic field $H$ and electric field $E$ two such parameters can be defined. Namely, a magnetic Grüneisen ratio can be defined as [54, 56]:
$$
\Gamma_H = -\frac{1}{C_{H,E}} \left( \frac{\partial M}{\partial T} \right)_{H,E}, \tag{17}
$$
where $M = \left\langle S_a^z \right\rangle + \left\langle S_b^z \right\rangle$ is the total magnetization of the cluster. This quantity can be further expressed in the following forms:
$$
\Gamma_H = \frac{1}{T} \left( \frac{\partial T}{\partial H} \right)_{S,E} = -\frac{1}{C_{H,E}} \left( \frac{\partial S}{\partial H} \right)_{T,E}. \tag{18}
$$

Moreover, in an analogous manner, an electric Grüneisen ratio can be defined as follows:
$$
\Gamma_E = -\frac{1}{C_{H,E}} \left( \frac{\partial P}{\partial T} \right)_{H,E}. \tag{19}
$$

Accepted manuscript. The final version was published in:
Journal of Magnetism and Magnetic Materials 527, 167767 (2021),
DOI:10.1016/j.jmmm.2021.167767

where $P$ is the total electric polarization of the pair. Alternatively, it can be expressed as:

$$
\Gamma_{E}=\frac{1}{T}\left(\frac{\partial T}{\partial E}\right)_{S, H}=-\frac{1}{C_{H, E}}\left(\frac{\partial S}{\partial E}\right)_{T, H}. \tag{20}
$$

The formulas given by Eq. 18 and 20 show a direct relation of Grüneisen ratios both to the differential temperature change under adiabatic conditions and to the differential entropy change under isothermal conditions, thus proving the importance of these quantities for description of the caloric effects. Interestingly, the Grüneisen ratio is expected to diverge at quantum phase transition points [54, 55] and presents an experimentally measurable quantity.

The numerical calculations based on the above formalism and aimed at description of the magneto- and electrocaloric effects for the Hubbard dimer will be presented in the next Section 3.

### 3. Numerical results and discussion

The numerical results have been obtained on the basis of formalism outlined in previous section and are based on the exact diagonalization of the model. For most of the figures, the mean number of electrons in the cluster has been assumed as $x=(\langle n_{a}\rangle+\langle n_{b}\rangle) / 2=1$, which corresponds to the half-filling condition for the energy states of the system. For such electron concentration, the chemical potential is independent on the external fields and temperature and equal to $\mu=U / 2$. However, two figures were prepared to demonstrate the influence of the electron concentration $x$ on the thermodynamic parameters.

We commence the discussion of the results from the most fundamental quantity for the caloric properties - the entropy of the system. In Fig.1, the normalized entropy $S / k_{\mathrm{B}}$ is presented in the normalized magnetic field $H / t$ - normalized temperature $k_{\mathrm{B}} T / t$ coordinates as a density plot with contours. The electric field is absent in this case. The isentropes with increasing values correspond typically to increasing temperatures. For zero temperature, a characteristic point is seen, in which the isolines are concentrated. This point corresponds to the magnetic critical field $H_{c}$ in which the quantum level crossing takes place, as the system switches from a singlet state (occurring in lower magnetic fields) to a triplet state (occurring in higher magnetic fields) at zero temperature. The value of the critical field $H_{c}$, seen in Fig.1 for the normalized electric field $E|e| d / t=0$ and Hubbard on-site energy $U / t=2$, is in agreement with the phase diagram constructed by us in Ref. [32] (see Fig. 1 in Ref. [32]).

![](./images/867768465031692568_1.jpg)

Figure 1: Density plot of normalized entropy as a function of the normalized temperature and magnetic field, for electric field $E|e| d / t=0.0$ and $U / t=2.0$. Isentropes are marked with solid lines.

To complement the picture presented in Fig. 1, in Fig.2 the normalized entropy $S / k_{\mathrm{B}}$ is presented in the normalized electric field $E|e| d / t$ - normalized temperature $k_{\mathrm{B}} T / t$ coordinates as a density plot with contours. The magnetic field is set to $H / t=1.5$. As before, the isentropes with increasing values correspond normally to increasing temperatures. Again, for zero temperature, a characteristic point is seen, in which the isolines are concentrated. This point corresponds to the electric critical field $E_{c}$ in which the quantum level crossing takes place and the system switches from triplet state (occurring in lower electric fields) to singlet state (occurring in higher electric fields). It can be verified that the value of the critical field $E_{c}$ presented in Fig.2 for the normalized magnetic field $H / t=1.5$ and Hubbard on-site energy $U / t=2$ is in agreement with the phase diagram found by us in Ref. [32].

It can already be noted that in the vicinity of the quantum level crossing the entropy becomes particularly sensitive to the external field - either magnetic or electric one. This fact is connected with the possibility of generating a significant entropy change with a limited change in the field, thus maximizing the caloric effects. Such a conclusion has been drawn, for example, in Ref. [21] for the magnetocaloric effect in Heisenberg dimer, undergoing the singlet-triplet transition.

The cross-sections of the density plots permit the detailed tracking of the entropy variability as a function of a single control parameter. An example of such plot is

Accepted manuscript. The final version was published in:
Journal of Magnetism and Magnetic Materials 527, 167767 (2021),
DOI:10.1016/j.jmmm.2021.167767

![](./images/867768465031692568_2.jpg)

Figure 2: Density plot of normalized entropy as a function of the normalized temperature and electric field, for magnetic field $H/t=1.5$ and $U/t=2.0$. Isentropes are marked with solid lines.

![](./images/867768465031692568_3.jpg)

Figure 3: Dependence of the normalized entropy on the normalized temperature, for $U/t=2.0$ for various electric fields, for normalized magnetic field $H/t=2.0$ (main panel) and for $H/t=0.0$ (inset).

Fig. 3, where the entropy, $S/k_\mathrm{B}$, is plotted vs. dimensionless temperature $k_\mathrm{B}T/t$ for several electric fields $E|e|d/t$ and for $U/t=2$. In the main panel the magnetic field is fixed at $H/t=2$, whereas in the inset the magnetic field is absent. In general, the entropy is an increasing function of temperature, and when $T\rightarrow\infty$ the entropy reaches the limit $S/k_\mathrm{B}=\ln 16\approx 2.7726$. It means that all the 16 states of the Hubbard pair cluster, which have been specified in Ref. [30], are occupied with equal probability. The electric field causes that approaching this limit is slightly harder. On the other hand, for $T\rightarrow 0$, when the system is in a pure ground state, either singlet or triplet one, the entropy goes to zero. However, for the electric critical field (the green curve labelled by $E_c|e|d/t=2.828$), i.e., when the quantum level crossing takes place, the residual entropy remains. It results from degeneracy of two states (singlet and triplet) exactly at the phase transition point, and its value is $S/k_\mathrm{B}=\ln 2\approx 0.6931$. In general, the residual entropy, $S/k_\mathrm{B}$ amounts to $\ln n$, where $n$ is a number of degenerate states occurring with the same ground state energy. In our case $n=2$, which corresponds to equilibrium coexistence of the singlet and triplet state exactly at the critical electric field. For $H/t=0$, in the inset, the system is in pure singlet state for all considered values of the electric field and the residual entropy does not emerge. It should also be noted that for $T\rightarrow 0$ the entropy curves exhibit a vanishing slope, thus not depending on the temperature, which reflects the 3rd law of thermodynamics.

Fig. 4 and Fig. 5 present the density and contour plots of the normalized specific heat, $C_{H,E}/k_\mathrm{B}$, for the same parameters $E|e|d/t$, $H/t$ and $U/t$ as in Fig. 1 and Fig. 2, respectively. The isolines, representing the constant values of the specific heat, show a quite complex behaviour. The specific heat for $T\rightarrow 0$ tends to zero, in agreement with the 3rd law of thermodynamics, in this way reflecting the flattening of the entropy curves from Fig. 3. The quantum level crossings at $T=0$ are seen in the points where the isolines are concentrating and even forming a loop structure. As the entropy in the vicinity of the level crossing presents a local maximum as a function of the field, the specific heat $C=T(\partial S/\partial T)$ shows a double peak (with the peaks located at two inflection points of the field dependence of the entropy). With an increase in temperature, in both figures the specific heat increases, then reaches some maximum at intermediate temperatures and finally tends to zero when the temperature is very high. The areas where the specific heat is large, i.e., $C_{H,E}/k_\mathrm{B}>1$, have been distinguished by various shades of yellow and red colours. It can be deduced from Fig. 4 that the highest maximum of the specific heat occurs at $H/t\rightarrow 0$, near the temperature of $k_\mathrm{B}T/t\approx 0.4$. On the other hand, in Fig. 5, the highest maximum will occur at the largest electric field ($E|e|d/t\approx 5$ in this figure), and for the temperature about $k_\mathrm{B}T/t\approx 0.7$. Moreover, it can be seen in Fig. 5 that for some electric fields, for instance near $E|e|d/t\approx 2.5$, the double-maximum structure of the specific heat can be predicted when temperature increases. Such an interesting behaviour of the specific heat results from a complicated interplay between the magnetic and electric energy terms. It should be noticed that the spe-
5

Accepted manuscript. The final version was published in:
Journal of Magnetism and Magnetic Materials 527, 167767 (2021),
DOI:10.1016/j.jmmm.2021.167767

![](./images/867768465031692568_4.jpg)

Figure 4: Density plot of normalized specific heat as a function of the normalized temperature and magnetic field, for electric field E|e|d/t = 0.0 and U/t = 2.0. Lines of constant specific heat are marked with solid lines.

![](./images/867768465031692568_5.jpg)

Figure 5: Density plot of normalized specific heat as a function of the normalized temperature and electric field, for magnetic field H/t = 1.5 and U/t = 2.0. Lines of constant specific heat are marked with solid lines.

cific heat fulfils the inequality $C_{H,E} \geq 0$ for any point in $(H,E,T)$-space, which evidences that the system remains in a stable thermal equilibrium.

Further illustration of the entropy behaviour is shown in the Fig. 6 to Fig. 10. In Fig.6 the normalized entropy, $S/k_{\rm B}$, is plotted vs. normalized magnetic field $H/t$. The on-site Coulomb energy amounts to $U/t=5$, whereas the electric field is absent. Various curves correspond to different temperatures. For very low temperatures a peak of residual entropy is seen at the critical magnetic field $H_c$ corresponding to the quantum level crossing of singlet and triplet states. As before, this transition has been predicted by the phase diagram obtained by us in Ref. [32] and the entropy in this doubly-degenerated point for $T \to 0$ amounts to $S/k_{\rm B} = \ln 2$ (see also the discussion of Fig. 3). The entropy peak disappears in large temperatures, where the curves become monotonously decreasing functions of the field. This result can be intuitively understood, since the increasing magnetic field orders the system and thus diminishes the entropy. Moreover, in the context of Maxwell relation $(\partial S/\partial H)_{T,E} = (\partial M/\partial T)_{H,E}$, it means that the magnetization $M$ of the system decreases with the temperature. By the same token, in the region of low temperatures, for the magnetic fields below the quantum level crossing point (in singlet state), the behaviour of magnetization should be anomalous, with the derivative $(\partial M/\partial T)_{H,E} > 0$. Such anomalous behaviour is in agreement with the predictions of our previous paper Ref. [31].

In order to give a flavour of the importance of electronic concentration on the dimer entropy away from half-filling of the energy levels (i.e. for $x \neq 1$), Fig. 7 is presented. It permits tracking of the entropy dependence on the electronic concentration $x$ for the same parameters as those used for preparing Fig. 6, with some values of the external magnetic field selected. In part Fig. 7(a) the lower magnetic fields are considered. It is evident that the entropy shows pronounced dependence on the electronic concentration $x$ with full electron-hole symmetry (i.e. the values remain the same for $x$ and $1-x$). In the absence of the magnetic field the entropy is low (close to zero) at half-filling ($x=1$), and if the dimer is charge doped, the entropy rises significantly. The maximum values are taken at $|x-1|=1/3$ and if the system is doped stronger, minimum are reached at $|x-1|=1/2$. Further doping results in reaching another maxima of entropy at $|x-1|=2/3$ and then the entropy tends to zero if the limit of $|x-1|=1$ is achieved (system is empty or completely filled with electrons). A similar behaviour can be observed for the presence of the external field $H/t \lesssim 0.3$, but the entropy value at $x=1$ rises whereas the value at the maxima is reduced. Moreover, the first maximum is shifted towards $x=1$ and the second one shows quite the opposite tendency. If the magnetic field exceeds $H/t \simeq 0.3$, as shown in Fig. 7(b), the maxima continue to shift in the directions described above. However, this time the maxima close to $|x-1| \simeq 1/3$ become gradually more pronounced. The largest entropy value at the maxima is achieved at the critical magnetic field $H/t = 0.702$. After crossing this field value, the maxima tend to flatten. On the
6

Accepted manuscript. The final version was published in:
Journal of Magnetism and Magnetic Materials **527**, 167767 (2021),
DOI:10.1016/j.jmmm.2021.167767

![](./images/867768465031692568_6.jpg)

Figure 6: Dependence of the normalized entropy on the normalized magnetic field, for $U/t = 5.0$ and electric field $E|e|d/t = 0.0$, for various temperatures.

contrary the maxima close to $|x-1| \simeq 2/3$ exhibit the entropy magnitude much less sensitive to the magnetic field for $H/t \gtrsim 0.3$; when it increases, the value tends to $k_{\text{B}} \ln 2$ for strong fields and the position of maxima shifts to $|x-1| = 3/4$.

Behaviour of the entropy analogous to one discussed in Fig. 6 can be seen in Fig. 8, where it is plotted vs. the electric field $E|e|d/t$, for Coulomb on-site energy $U/t = 2$ and the magnetic field fixed at $H/t = 2$. Various curves correspond to different temperatures. Again, in the low temperature region, the residual entropy peak is seen, corresponding to quantum level crossing between the triplet and the singlet state. The value of the entropy in the peak for $T \to 0$ is the same as in Fig. 6, $S/k_{\text{B}} = \ln 2$. The peak disappears as the temperature increases. The analysis of the entropy vs. electric field can be connected with the behaviour of electric polarization $P$ vs. temperature. With the help of Maxwell relation $(\partial S/\partial E)_{H,T} = (\partial P/\partial T)_{H,E}$, we can conclude that the electric polarization $P$ should behave similarly to magnetization $M$. Namely, it decreases with increase in temperature for sufficiently large temperatures. However, in the low temperatures, below the quantum level crossing (in triplet state) the behaviour of $P$ is anomalous, with the derivative $(\partial P/\partial T)_{H,E} > 0$. Such a behaviour has also been predicted in Ref. [31].

Like in the case of Fig. 7, it is instructive to sketch the entropy behaviour as a function of the electron concentration to demonstrate the effect of charge doping of the system. Such data can be tracked in Fig. 9, prepared for the same parameters as Fig. 8, for selected values of the electric field. In the absence of the electric and magnetic field, the entropy shows four symmetric maxima at $|x-1| = 1/3$ and $|x-1| = 2/3$, with the entropy value of $k_{\text{B}} \ln 2$. At $|x-1| = 1/2$ the entropy has deep local minima. The maxima at $|x-1| = 2/3$ remain completely insensitive to the changes in the electric field. On the contrary, the maxima at $|x-1| = 1/3$ build up when the electric field is applied; their position is shifted towards $x = 1$. Also the minimum at $x = 1$ is lifted up. The maximum entropy is reached at the critical electric field value $E|e|d/t = 2.828$. Further increase in the field results in flattening of the maxima.

![](./images/867768465031692568_7.jpg)

Figure 7: Dependence of the normalized entropy on the electron concentration, for $U/t = 5.0$ electric field $E|e|d/t = 0.0$ and normalized temperature $k_{\text{B}}T/t = 0.1$, for various magnetic fields.

Both Fig. 7 and Fig. 9 demonstrate the crucial influence of the electronic concentration on the entropy behaviour in the dimer. However, the case of $x = 1$ (i.e. half filling), indicates the most pronounced sensitivity of the entropy to the external electric field. Therefore, we return in all the further discussion to the case of $x = 1$.

Accepted manuscript. The final version was published in:
Journal of Magnetism and Magnetic Materials 527, 167767 (2021),
DOI:10.1016/j.jmmm.2021.167767

![](./images/867768465031692568_8.jpg)

Figure 8: Dependence of the normalized entropy on the normalized electric field, for $U/t = 2.0$ and magnetic field $H/t = 2.0$, for various temperatures.

![](./images/867768465031692568_9.jpg)

Figure 9: Dependence of the normalized entropy on the electron concentration, for $U/t = 2.0$ magnetic field $H/t = 2.0$ and normalized temperature $k_\text{B}T/t = 0.1$, for various electric fields.

The observation that maximum value of the entropy in the low-temperature peak is constant, $S/k_\text{B} = \ln 2$, has been confirmed in Fig.10. It this figure the normalized entropy, showing a pronounced peak, is presented vs. normalized magnetic field $H/t$, for $U/t = 5$, whereas the temperature is low and constant, $k_\text{B}T/t = 0.1$. Various curves in Fig.10 correspond to different magnitudes of the electric field $E|e|d/t$. An increase in the electric field causes the increase in the critical magnetic field $H_c$, thus shifting the position of the entropy peak. Such a shift is non-linear vs. electric field $E|e|d/t$, which is in agreement with the phase diagram presented in Ref. [32].

The response of the entropy to the external fields is quantified by the appropriate Grüneisen ratios. In Fig. 11 the magnetic Grüneisen ratio $\Gamma_H t$ is shown in dimensionless units, as a function of the normalized magnetic field $H/t$. Various curves correspond to different temperatures $k_\text{B}T/t$. The Coulombic on-site energy amounts to $U/t = 5$, and the electric field is absent. It is demonstrated that for very low temperatures the parameter $\Gamma_H$ diverges at the quantum level crossing, i.e., for the critical field $H_c$. With an increase in temperature, the divergence disappears and the curves flatten. The magnetic Grüneisen ratio is negative in the range of the singlet ground state, i.e., below $H_c$, and positive in the range of the triplet ground state, above $H_c$. The divergence of $\Gamma_H$ at $H_c$, when $T \to 0$, is predisposing this parameter for a good indicator of the quantum level crossing.

In Fig. 12 the electric Grüneisen ratio, $\Gamma_E t/(|e|d)$, is shown in dimensionless units, vs. normalized electric field $E|e|d/t$. Various curves correspond to different temperatures $k_\text{B}T/t$. The Coulombic on-site energy amounts to $U/t = 5$, and the magnetic field is $H/t = 2$. One can see in Fig. 12 that for very low temperatures the parameter $\Gamma_E$ diverges at the quantum level crossing point, at the critical field $E_c$. With an increase in temperature this divergence disappears and the curves flatten, similarly to the behaviour of $\Gamma_H$ demonstrated in the previous figure. However, here the electric Grüneisen ratio is negative in the range of the triplet ground state, i.e., below $E_c$, and is positive in the range of the singlet ground state, above $E_c$. The divergence of $\Gamma_E$ at $E_c$, when $T \to 0$, can be also a useful property, analogously to $\Gamma_H$, for uncovering the presence of the quantum level crossing. Moreover, this divergence proves the sensitivity of the entropy to the changes of the external field, marking the regions of interest for maximising the entropy change in the caloric effects.

The behaviour of the entropy as a function of the external field is crucial for the description of magnetocaloric (MCE) and electrocaloric (ECE) effects. The appropriate quantity is the isothermal entropy change when the external field is varied between the initial value of 0 to the non-zero final value. First let us discuss the MCE in the Hubbard dimer system. In Fig. 13 and Fig. 14 the isothermal entropy change in MCE (defined by Eq. 13) is presented vs. normalized temperature $k_\text{B}T/t$. Various curves in these figures correspond to different constant external electric fields $E|e|d/t$. Fig. 13 is prepared for $U/t = 2$ and the external magnetic field is switched from $H/t = 0$ to $H/t = 0.1$. The final value, according to the phase diagram (Ref. [32]), cor-

8

Accepted manuscript. The final version was published in:
Journal of Magnetism and Magnetic Materials **527**, 167767 (2021),
DOI:10.1016/j.jmmm.2021.167767

![](./images/867768465031692568_10.jpg)

Figure 10: Dependence of the normalized entropy on the normalized magnetic field, for $U/t = 5.0$ and normalized temperature $k_\text{B}T/t = 0.1$, for various electric fields.

![](./images/867768465031692568_11.jpg)

Figure 11: Dependence of the normalized magnetic Grüneisen ratio on the normalized magnetic field, for $U/t = 5.0$ and normalized electric field $E|e|d/t = 0.0$, for various temperatures.

responds to the region of the singlet ground state for all the values of the electric field. On the other hand, Fig. 14 is prepared for $U/t = 5$ with the magnetic field switched from $H/t = 0$ to $H/t = 1.5$, where such a final value corresponds to the triplet ground state for the values of electric fields specified in the figure legend. It can also be mentioned that for the electric field higher than about $E|e|d/t \approx 5$ the system with the parameters from Fig. 14 should undergo the transition to the singlet ground state. One can see that behaviour of the MCE curves vs. temperature is completely different for both figures. In Fig. 13, starting from the singlet ground state, the strong inverse MCE can be observed in the low temperature region. Then, for higher temperatures the MCE becomes direct, i.e., entropy change is positive, but relatively weak, and it further weakens with an increase in temperature. The inset in Fig. 13 shows this behaviour in the logarithmic temperature scale. On the other hand, in Fig. 14, starting from the triplet ground state, a strong direct MCE can be observed, provided the electric field is not very large. When $E|e|d/t$ increases, that is, approaching a phase boundary with the singlet ground state, the inverse MCE appears in the low temperatures and the curves noticeably tend to the shape demonstrated in the previous figure. The common characteristic of both figures, Fig. 13 and Fig. 14, is a shift of the minimum and maximum position of the curves towards higher temperatures, as the electric field increases. The strengthening of the electric field makes the curves more flat in Fig. 13, but in Fig. 14 such conclusion can be drawn only for the positive (direct) MCE. It can be seen that the magnitude of the external constant electric field exerts a noticeable effect on the entropy change under variation of the magnetic field, being a clear manifestation of the magnetoelectric phenomena in Hubbard dimer.

An effect complementary to MCE is ECE, quantified conveniently by the isothermal entropy change defined by Eq. 14. In Fig. 15 and Fig. 16, the isothermal entropy change in ECE is presented vs. normalized temperature $k_\text{B}T/t$. Various curves in these figures correspond to different magnitudes of the constant external magnetic field $H/t$. Fig. 15 is prepared for $U/t = 2$ and the electric field is switched from $E|e|d/t = 0$ to $E|e|d/t = 0.5$, where the final value corresponds to the region with the singlet ground state, since all values of the magnetic field labelled in this figure fulfil the condition $H < H_c$. On the other hand, Fig. 16 is prepared for $U/t = 5$ and the electric field is also switched from $E|e/t = 0$ to $E|e|d/t = 0.5$. Therefore, the final value of $E$ corresponds to the singlet ground state for $H/t =$0.0, 0.4, 0.5 and 0.6, according to the phase diagram presented in Ref. [32]. However, for higher fields, i.e., for $H/t =$0.8, 0.9 and 1.0, the triplet ground state occurs at the final value of $E$. Therefore, it is interesting to compare ECE in both these figures. In Fig. 15 the curves present two positive maxima showing a direct ECE. In the low temperature region the maximum is sharp and it builds up with an increase in the magnetic field. On the other hand, the second, high-temperature maximum is less pronounced and slowly flattens with an increase in the magnetic field. At the same time, the minimum between these maxima becomes deeper as the field increases. In particular, for $H/t = 1$ an inverse

Accepted manuscript. The final version was published in:
Journal of Magnetism and Magnetic Materials 527, 167767 (2021),
DOI:10.1016/j.jmmm.2021.167767

![](./images/867768465031692568_12.jpg)

Figure 12: Dependence of the normalized electric Grüneisen ratio on the normalized electric field, for $U/t = 5.0$ and normalized magnetic field $H/t = 2.0$, for various temperatures.

![](./images/867768465031692568_13.jpg)

Figure 13: Dependence of the normalized isothermal entropy change in magnetocaloric effect on the normalized temperature, for magnetic field variation between $H/t = 0.0$ and $0.1$, for $U/t = 2.0$ and various normalized electric field values. The inset shows selected data from the main panel in logarithmic scale for temperature.

ECE can be found, corresponding to the minimum of $\Delta S_{T}^{ECE}$, which then extends down to negative values. In Fig. 16, the ECE curves corresponding to $H/t \leq 0.6$, i.e., for the singlet ground state, are of similar character as those in Fig. 15, with the reservation that the negative minima are much deeper. However, the curves for $H/t \geq 0.8$, i.e., for the triplet ground state, are totally different. They present a strong inverse ECE in the low-temperature minimum. Also the second negative minimum, which is more shallow, can be seen for larger temperatures. The minimum at the low temperature is especially pronounced for $H/t = 0.8$, i.e., for the smallest considered field in the range of the triplet ground state. Evidently, the rapid change from positive to negative ECE is connected with the quantum phase transition in the ground state, from singlet to triplet state. The insets in Figs.15 and 16 are to inspect the effect in the logarithmic temperature scale for some representative values of $H/t$ chosen from the main figures, to facilitate tracking the low-temperature behaviour.

## 4. Summary and conclusion
In the paper we report a theoretical study of the caloric effects - MCE and ECE - in a model Hubbard dimer (pair cluster) immersed in external electric and magnetic field.

The formalism of the grand canonical ensemble has been used [30], in which the system can exchange electrons with its environment, whereas the average electron concentration, $x = (\langle n_{a}\rangle+\langle n_{b}\rangle)/2$, amounts to $0 \leq x \leq 2$. This general formalism enables the studies of the influence of electron concentration $x$ on the thermodynamic properties of such cluster. However, in the numerical application of the method, the most interesting value of concentration has been exploited, namely $x = 1$, which corresponds to the half-filling of the energy levels of the system. For $x = 1$ the sensitivity of the system entropy to the external fields was found to be maximized, thus corresponding to the most pronounced caloric effects exhibited by the system in question.

For investigation of the caloric effects, a crucial quantity is the entropy with its dependence on the external fields. The numerically exact results for the entropy of the Hubbard dimer have been analysed in relation to the phase diagram obtained by us previously in Ref. [32], and they are in agreement with other thermodynamic properties, for instance, those calculated in our work Ref. [31]. One of the most interesting results is the residual entropy in the ground state exactly at the quantum level crossing point (corresponding to a transition between the singlet and triplet state and controlled with the electric or magnetic field). This particular feature is manifested as the finite-width entropy peak at the finite temperature when the critical field value is crossed. Moreover, in the vicinity of this critical field the entropy is particularly sensitive to the external field, thus maximizing the caloric effect magnitude. It might be mentioned that the effect of maximization of the field dependence of the entropy has been pointed out in the context of spin dimers [12, 21] and the singlet-triplet transition in this system focused the attention in Ref. [19].

10

Accepted manuscript. The final version was published in:
Journal of Magnetism and Magnetic Materials 527, 167767 (2021),
DOI:10.1016/j.jmmm.2021.167767

![](./images/867768465031692568_14.jpg)

Figure 14: Dependence of the normalized isothermal entropy change
in magnetocaloric effect on the normalized temperature, for magnetic
field variation between H/t = 0.0 and 1.5, for U/t = 5.0 and various
normalized electric field values.

![](./images/867768465031692568_15.jpg)

Figure 15: Dependence of the normalized isothermal entropy change
in electrocaloric effect on the normalized temperature, for electric
field variation between E|e|d/t = 0.0 and 0.5, for U/t = 2.0 and var-
ious normalized magnetic field values. The inset shows selected data
from the main panel in logarithmic scale for temperature.

The numerical calculations concerned first measures
of MCE and ECE such as the isothermal entropy
changes $\Delta S_{T}^{MCE}$ and $\Delta S_{T}^{ECE}$, respectively. The inves-
tigations spanned of the wide range of temperatures as
well as magnitudes of the magnetic field and electric
field change, to identify the most interesting cases. In
general, the significant ranges of both direct and inverse
caloric effects were found.

It has also been found that the caloric effects are es-
pecially pronounced in the low temperature region, in
the vicinity of the critical fields responsible for quan-
tum level crossing. This fact could be potentially used in
practice, for the magnetic or electric field change-based
cooling in the range of low temperatures.

In the theoretical part, the electric Grüneisen ratio,
$\Gamma_{E}$, has been defined as a new quantity, being an ana-
logue of the magnetic Grüneisen ratio, $\Gamma_{H}$. It has been
shown that both parameters reveal singularities at the
quantum critical points, when $T \to 0$. Thus, both these
Grüneisen ratios can be useful for determination of the
quantum phase transitions.

The Hubbard dimer (pair cluster) turned out to be a
very interesting model system, in which the thermody-
namics of the caloric effects - MCE and ECE - can be
simultaneously studied by the exact method. The mag-
netic and electric fields are found to exert opposite ef-
fects on the induced magnetism in the studied system,
therefore, using the exact approach is particularly im-
portant for studying the interplay of both fields.

It can be noted that in the light of the paper [57],
where the magnetoelastic properties of the Hubbard pair
cluster have been investigated, it would be interesting to
study the caloric effects in the presence of the external
elastic forces, leading to the emergence of multicaloric
effects [58, 59, 60]. These forces, being able to deform
interatomic distance, influence both the hopping inte-
gral and the interatomic Coulomb potential. However,
such problem exceeds the frame of the present paper
and should be considered elsewhere.

Having found the entropy, the specific heat has been
determined for the system embedded simultaneously in
the magnetic and electric fields. An interesting result is
a possibility of occurrence of double maximum of the
specific heat in some regions of the density diagrams
(Figs. 4 and 5), when corresponding temperature depen-
dence is analysed.

The dimer with electron hopping has also been dis-
cussed in the literature as a part of Ising Hamiltonian-
based more elaborate magnetic model [61, 62, 63] in
the simultaneous presence of the electric and magnetic
field. In this case, non-trivial phase diagrams were
found as a result of the interplay of the charge doping
(controlled with the chemical potential) and the influ-
ence of the external fields in the infinite planar system.
This might motivate further studies of Hubbard dimers
embedded in localized-spin magnetic model in the ex-
ternal fields.

Last but not least, let us mention the applicabil-
ity of the Hubbard dimer model to experimental sys-
tems in condensed matter physics. In this context,
we can point out the layered charge transfer salts of
Mott insulator type, for which Hubbard dimer can
serve as a minimum model [64]. For example, the

11

Accepted manuscript. The final version was published in:
Journal of Magnetism and Magnetic Materials 527, 167767 (2021),
DOI:10.1016/j.jmmm.2021.167767

![](./images/867768465031692568_16.jpg)

Figure 16: Dependence of the normalized isothermal entropy change in electrocaloric effect on the normalized temperature, for electric field variation between $E|e|d/t = 0.0$ and $0.5$, for $U/t = 5.0$ and various normalized magnetic field values. The inset shows selected data from the main panel in logarithmic scale for temperature.

extended Hubbard model for two sites was investi- gated to capture physics of $\beta$ and $\kappa$ polymorphs of $(ET)_2X$ or $(BEDT-TTF)_2X$, where (ET) or (BEDT-TTF) is bis(ethylenedithio)tetrathiafulvalene and X is mono- valent anion, like $Cu_2(CN)_3$, constituting half-filled systems composed of effective dimers [65]. Similar goals was addressed in calculations performed in Ref. [66]. The mentioned materials motivate also the interest in development of more elaborate models based on dimer- ized Hubbard Hamiltonian with interacting dimers [67] for a complex group of BEDT-TTF charge transfer salts [68]. A somehow similar kind of model has been ap- plied to description of metal-insulator transition in $VO_2$ [69]. In this context, it is worth mentioning that the pronounced electrocaloric effect associated with metal- insulator transition has been measured in $VO_2$ [70]. In addition, etracyanoquinodimethane (TCNQ)-based charge transfer salts were also modelled using the dimer Hubbard model [71]. Also, the applications of two site Hubbard model to description of diradicals can be men- tioned [72, 73, 74]. Hubbard model on small clusters has been also invoked for prediction of selected proper- ties of transition metal nanostructures [45, 75].

The present results, concerning an ensemble of non- interacting Hubbard dimers, may serve as a starting point for the studies of electro- and magnetocaloric phe- nomena in extended model with, for example, inter- dimer interactions included (see for example the study in Ref. [76]). Moreover, larger clusters can be studied using the identical model, to mention for example our work on the cubic cluster Ref. [48]. The influence of the cluster geometry on the thermodynamic properties is expected to be crucial (in particular, linear or closed geometry can lead to different sort of behaviour, as it can be followed for the case of Hubbard trimer in Ref. [50]). Therefore, each shape and size of cluster requires a sep- arate computation. In the context of exact studies, the works for various tetramers can be noticed [77, 49, 78]. However, in relation to the external electric field applied to the Hubbard model for large clusters or even infinite lattice of any dimensionality, it should be mentioned that screening effects would limit the field influence on the model properties. This facts focuses the interest in electric field-related phenomena rather on small clus- ters.

## References

[1] F. Giazotto, T. T. Heikkilä, A. Luukanen, A. M. Savin, J. P. Pekola, Opportunities for mesoscopics in ther- mometry and refrigeration: Physics and applications, Reviews of Modern Physics 78 (1) (2006) 217-274. doi:10.1103/RevModPhys.78.217.

[2] J. T. Muhonen, M. Meschke, J. P. Pekola, Micrometre-scale refrigerators, Reports on Progress in Physics 75 (4) (2012) 046501. doi:10.1088/0034-4885/75/4/046501.

[3] A. Ziabari, M. Zebarjadi, D. Vashaee, A. Shak- ouri, Nanoscale solid-state cooling: A review, Re- ports on Progress in Physics 79 (9) (2016) 095901. doi:10.1088/0034-4885/79/9/095901.

[4] V. K. Pecharsky, K. A. Gschneidner, A. O. Pecharsky, A. M. Tishin, Thermodynamics of the magnetocaloric effect, Physical Review B 64 (14) (2001) 144406. doi:10.1103/PhysRevB.64.144406.

[5] V. Franco, J. S. Blázquez, J. J. Ipus, J. Y. Law, L. M. Moreno- Ramírez, A. Conde, Magnetocaloric effect: From materials re- search to refrigeration devices, Progress in Materials Science 93 (2018) 112-232. doi:10.1016/j.pmatsci.2017.10.005.

[6] J. H. Belo, A. L. Pires, J. P. Araújo, A. M. Pereira, Magnetocaloric materials: From micro- to nanoscale, Journal of Materials Research 34 (1) (2019) 134-157. doi:10.1557/jmr.2018.352.

[7] C. Ciccarelli, R. P. Campion, B. L. Gallagher, A. J. Fer- guson, Intrinsic magnetic refrigeration of a single electron transistor, Applied Physics Letters 108 (5) (2016) 053103. doi:10.1063/1.4941289.

[8] D. I. Bradley, A. M. Guénault, D. Gunnarsson, R. P. Ha- ley, S. Holt, A. T. Jones, Y. A. Pashkin, J. Penttilä, J. R. Prance, M. Prunnila, L. Roschier, On-chip magnetic cooling of a nanoelectronic device, Scientific Reports 7 (1) (2017) 1-9. doi:10.1038/srep45566.

[9] M. Palma, C. P. Scheller, D. Maradan, A. V. Fes- hchenko, M. Meschke, D. M. Zumbühl, On-and-off chip cooling of a Coulomb blockade thermometer down to 2.8 mK, Applied Physics Letters 111 (25) (2017) 253105. doi:10.1063/1.5002565.

[10] N. Yurttagül, M. Sarsby, A. Geresdi, Indium as a High- Cooling-Power Nuclear Refrigerant for Quantum Nanoelec- tronics, Physical Review Applied 12 (1) (2019) 011005. doi:10.1103/PhysRevApplied.12.011005.

Accepted manuscript. The final version was published in:
Journal of Magnetism and Magnetic Materials 527, 167767 (2021),
DOI:10.1016/j.jmmm.2021.167767

[11] M. Sarsby, N. Yurttagül, A. Geresdi, 500 microkelvin nanoelectronics, Nature Communications 11 (1) (2020) 1-7. doi:10.1038/s41467-020-15201-3.

[12] J. W. Sharples, D. Collison, E. J. L. McInnes, J. Schnack, E. Palacios, M. Evangelisti, Quantum signatures of a molecular nanomagnet in direct magnetocaloric measurements, Nature Communications 5 (1) (2014) 1-6. doi:10.1038/ncomms6321.

[13] Z. Kutnjak, B. Rožič, R. Pirc, J. G. Webster, Electrocaloric Effect: Theory, Measurements, and Applications, in: Wiley Encyclopedia of Electrical and Electronics Engineering, John Wiley & Sons, Inc., 1999.

[14] M. Ožbolt, A. Kitanovski, J. Tušek, A. Poredoš, Electrocaloric refrigeration: Thermodynamics, state of the art and future perspectives, International Journal of Refrigeration 40 (2014) 174-188. doi:10.1016/j.ijrefrig.2013.11.007.

[15] L. Mañosa, A. Planes, M. Acet, Advanced materials for solid-state refrigeration, Journal of Materials Chemistry A 1 (16) (2013) 4925-4936. doi:10.1039/C3TA01289A.

[16] M. S. Reis, N. Ma, Caloric effects of quantum materials: An outlook, Physics Open 4 (2020) 100028. doi:10.1016/j.physo.2020.100028.

[17] O. Waldmann, Field-induced level crossings in spin clusters: Thermodynamics and magnetoelastic instability, Physical Review B 75 (17) (2007) 174440. doi:10.1103/PhysRevB.75.174440.

[18] A. Furrer, O. Waldmann, Magnetic cluster excitations, Reviews of Modern Physics 85 (1) (2013) 367-420. doi:10.1103/RevModPhys.85.367.

[19] T. Chakraborty, H. Singh, C. Mitra, Experimental evidences of singlet to triplet transition in a spin cluster compound, Journal of Magnetism and Magnetic Materials 396 (2015) 247-253. doi:10.1016/j.jmmm.2015.08.053.

[20] J. Brambleby, P. A. Goddard, J. Singleton, M. Jaime, T. Lancaster, L. Huang, J. Wosnitza, C. V. Topping, K. E. Carreiro, H. E. Tran, Z. E. Manson, J. L. Manson, Adiabatic physics of an exchange-coupled spin-dimer system: Magnetocaloric effect, zero-point fluctuations, and possible two-dimensional universal behavior, Physical Review B 95 (2) (2017) 024404. doi:10.1103/PhysRevB.95.024404.

[21] T. Chakraborty, C. Mitra, Magnetocaloric effect as a signature of quantum level-crossing for a spin-gapped system, Journal of Physics: Condensed Matter 31 (47) (2019) 475802. doi:10.1088/1361-648X/ab3962.

[22] R. Tarasenko, P. Danylchenko, V. Tkáč, A. Orendáčová, E. Čižmár, M. Orendáč, A. Feher, Experimental study of the magnetocaloric effect in [Ni(fum)(phen)] - The ferromagnetic dimer with spin 1, Physica B: Condensed Matter 576 (2020) 411671. doi:10.1016/j.physb.2019.411671.

[23] G. Lorusso, O. Roubeau, M. Evangelisti, Rotating Magnetocaloric Effect in an Anisotropic Molecular Dimer, Angewandte Chemie International Edition 55 (10) (2016) 3360-3363. doi:10.1002/anie.201510468.

[24] K. Karl'ová, J. Strečka, J. Richter, Enhanced magnetocaloric effect in the proximity of magnetization steps and jumps of spin-1/2 XXZ Heisenberg regular polyhedra, Journal of Physics: Condensed Matter 29 (12) (2017) 125802. doi:10.1088/1361-648X/aa53ab.

[25] M. Mohylna, M. Žuković, Magnetocaloric properties of frustrated tetrahedra-based spin nanoclusters, Physics Letters A 383 (21) (2019) 2525-2534. doi:10.1016/j.physleta.2019.05.015.

[26] H. A. Zad, M. Sabeti, A. Zoshki, N. Ananikian, Electrocaloric effect in the two spin-1/2 XXZ Heisenberg edge-shared tetrahedra and spin-1/2 XXZ Heisenberg octahedron with Dzyaloshinskii-Moriya interaction, Journal of Physics: Condensed Matter 31 (42) (2019) 425801. doi:10.1088/1361-648X/ab2854.

[27] M. Žuković, Thermodynamic and magnetocaloric properties of geometrically frustrated Ising nanoclusters, Journal of Magnetism and Magnetic Materials 374 (2015) 22-35. doi:10.1016/j.jmmm.2014.08.017.

[28] M. Mohylna, M. Žuković, Effect of Single-Ion Anisotropy on Magnetocaloric Properties of Frustrated Spin-s Ising Nanoclusters, Magnetochemistry 6 (4) (2020) 56. doi:10.3390/magnetochemistry6040056.

[29] S. Haldar, S. Ramasesha, Magnetocaloric effect in molecular spin clusters and their assemblies: Exact and Monte Carlo studies using exact cluster eigenstates, Journal of Magnetism and Magnetic Materials 500 (2020) 166424. doi:10.1016/j.jmmm.2020.166424.

[30] T. Balcerzak, K. Szalowski, Hubbard pair cluster in the external fields. Studies of the chemical potential, Physica A: Statistical Mechanics and its Applications 468 (2017) 252-266. doi:10.1016/j.physa.2016.11.004.

[31] T. Balcerzak, K. Szalowski, Hubbard pair cluster in the external fields. Studies of the polarization and susceptibility, Physica A: Statistical Mechanics and its Applications 512 (2018) 1069-1084. doi:10.1016/j.physa.2018.08.152.

[32] T. Balcerzak, K. Szalowski, Hubbard pair cluster in the external fields. Studies of the magnetic properties, Physica A: Statistical Mechanics and its Applications 499 (2018) 395-406. doi:10.1016/j.physa.2018.02.017.

[33] N. Cerrato, C. Noce, Complete set of commuting observables for a two-site Hubbard model, European Journal of Physics 40 (5) (2019) 055403. doi:10.1088/1361-6404/ab2004.

[34] D. J. Carrascal, J. Ferrer, J. C. Smith, K. Burke, The Hubbard dimer: A density functional case study of a many-body problem, Journal of Physics: Condensed Matter 27 (39) (2015) 393001. doi:10.1088/0953-8984/27/39/393001.

[35] C. A. Ullrich, Density-functional theory for systems with noncollinear spin: Orbital-dependent exchange-correlation functionals and their application to the Hubbard dimer, Physical Review B 98 (3) (2018) 035140. doi:10.1103/PhysRevB.98.035140.

[36] M. Vanzini, L. Reining, M. Gatti, Spectroscopy of the Hubbard dimer: The spectral potential, The European Physical Journal B 91 (8) (2018) 192. doi:10.1140/epjb/e2018-90277-3.

[37] R. Wortis, M. P. Kennett, Local integrals of motion in the two-site Anderson-Hubbard model, Journal of Physics: Condensed Matter 29 (40) (2017) 405602. doi:10.1088/1361-648X/aa818e.

[38] M. E. Amendola, A. Romano, C. Noce, Analytical diagonalization study of a two-orbital Hubbard model on a two-site molecule, Physica B: Condensed Matter 479 (2015) 121-129. doi:10.1016/j.physb.2015.10.003.

[39] J. Spalek, A. M. Oleś, K. A. Chao, Thermodynamic properties of a two-site Hubbard model with orbital degeneracy, Physica A: Statistical Mechanics and its Applications 97 (3) (1979) 552-564. doi:10.1016/0378-4371(79)90095-5.

[40] S.-H. Chen, Y.-C. Cheng, Magnetic susceptibility of a two-site extended Hubbard Hamiltonian with arbitrary electron density, Physical Review B 18 (7) (1978) 3465-3469. doi:10.1103/PhysRevB.18.3465.

[41] J. R. Iglesias, M. A. Gusmão, M. Acquarone, A. Romano, C. Noce, Model calculation of the interaction terms and ground states of the extended Hubbard model on a dimer, Physica B: Condensed Matter 230-232 (1997) 1047-1049. doi:10.1016/S0921-4526(96)00805-8.

[42] M. Acquarone, J. R. Iglesias, M. A. Gusmão, C. Noce, A. Romano, Electronic and phononic states of the Holstein-Hubbard

Accepted manuscript. The final version was published in:
Journal of Magnetism and Magnetic Materials $\boldsymbol{527}$, 167767 (2021),
DOI:10.1016/j.jmmm.2021.167767

dimer of variable length, Physical Review B 58 (12) (1998) 7626-7636. doi:10.1103/PhysRevB.58.7626.

[43] J. Callaway, D. P. Chen, D. G. Kanhere, Q. Li, Small-cluster calculations for the simple and extended Hubbard models, Physical Review B 42 (1) (1990) 465-474. doi:10.1103/PhysRevB.42.465.

[44] G. M. Pastor, R. Hirsch, B. Mühlschlegel, Electron correlations, magnetism, and structure of small clusters, Physical Review Letters 72 (24) (1994) 3879-3882. doi:10.1103/PhysRevLett.72.3879.

[45] F. López-Urías, G. M. Pastor, Thermodynamic properties of antiferromagnetic clusters, Journal of Magnetism and Magnetic Materials 294 (2) (2005) e27-e31. doi:10.1016/j.jmmm.2005.03.048.

[46] J. Callaway, D. P. Chen, Y. Zhang, Hubbard model for a cubic cluster, Physical Review B 36 (4) (1987) 2084-2091. doi:10.1103/PhysRevB.36.2084.

[47] R. Schumann, D. Zwicker, The Hubbard model extended by nearest-neighbor Coulomb and exchange interaction on a cubic cluster - rigorous and exact results, Annalen der Physik 522 (6) (2010) 419-439. doi:10.1002/andp.201010452.

[48] K. Szałowski, T. Balcerzak, Electrocaloric effect in cubic Hubbard nanoclusters, Scientific Reports 8 (1) (2018) 1-10. doi:10.1038/s41598-018-23443-x.

[49] R. Schumann, Analytical solution of extended Hubbard models on three- and four-site clusters, Physica C: Superconductivity 460 (2007) 1015-1017. doi:10.1016/j.physc.2007.03.203.

[50] R. C. Juliano, E. G. Santos, M. A. Gusmão, Thermodynamic signatures of geometrical frustration in clusters, Journal of Physics: Condensed Matter 32 (7) (2019) 075602. doi:10.1088/1361-648X/ab5347.

[51] C. Noce, M. Cuoco, A. Romano, Thermodynamical properties of the Hubbard model on finite-size clusters, Physica C: Superconductivity 282 (1997) 1705-1706. doi:10.1016/S0921-4534(97)00972-6.

[52] Y. Hancock, Quasi-zero-dimensional quantum spin-switching system, Physical Review B 71 (22) (2005) 224428. doi:10.1103/PhysRevB.71.224428.

[53] Y. Hancock, A family of spin-switching, inhomogeneous Hubbard chains, Physica E: Low-dimensional Systems and Nanostructures 56 (2014) 141-150. doi:10.1016/j.physe.2013.08.021.

[54] L. Zhu, M. Garst, A. Rosch, Q. Si, Universally Diverging Grüneisen Parameter and the Magnetocaloric Effect Close to Quantum Critical Points, Physical Review Letters 91 (6) (2003) 066404. doi:10.1038/PhysRevLett.91.066404.

[55] R. Jafari, Thermodynamic properties of the one-dimensional extended quantum compass model in the presence of a transverse field, The European Physical Journal B 85 (2012) 167. doi:10.1140/epjb/e2012-20682-5.

[56] K. Szałowski, T. Balcerzak, A. Bobák, Thermodynamic properties of a diluted Heisenberg ferromagnet with interaction anisotropy-Magnetocaloric point of view, Journal of Magnetism and Magnetic Materials 323 (15) (2011) 2095-2102. doi:10.1016/j.jmmm.2011.03.020.

[57] T. Balcerzak, K. Szałowski, Hubbard pair cluster with elastic interactions. Studies of thermal expansion, magnetostriction and electrostriction, Physica A: Statistical Mechanics and its Applications 531 (2019) 121740. doi:10.1016/j.physa.2019.121740.

[58] H. Ursic, V. Bobnar, B. Malic, C. Filipic, M. Vrabelj, S. Drnovsek, Y. Jo, M. Wencka, Z. Kutnjak, A multicaloric material as a link between electrocaloric and magnetocaloric refrigeration, Scientific Reports 6 (1) (2016) 26629. doi:10.1038/srep26629.

[59] E. Stern-Taulats, T. Castán, L. Mañosa, A. Planes, N. D. Mathur, X. Moya, Multicaloric materials and effects, MRS Bulletin 43 (4) (2018) 295-299. doi:10.1557/mrs.2018.72.

[60] J.-Z. Hao, F.-X. Hu, Z.-B. Yu, F.-R. Shen, H.-B. Zhou, Y.-H. Gao, K.-M. Qiao, J. Li, C. Zhang, W.-H. Liang, J. Wang, J. He, J.-R. Sun, B.-G. Shen, Multicaloric and coupled-caloric effects, Chinese Physics B 29 (4) (2020) 047504. doi:10.1088/1674-1056/ab7da7.

[61] H. Čenčariková, J. Strečka, Enhanced magnetoelectric effect of the exactly solved spin-electron model on a doubly decorated square lattice in the vicinity of a continuous phase transition, Physical Review E 98 (6) (2018) 062129. doi:10.1103/PhysRevE.98.062129.

[62] H. Čenčariková, J. Strečka, Conventional and rotating magnetoelectric effect of a half-filled spin-electron model on a doubly decorated square lattice, Physics Letters A 383 (33) (2019) 125957. doi:10.1016/j.physleta.2019.125957.

[63] H. Čenčariková, J. Strečka, A. Gendiar, Influence of applied electric and magnetic fields on a thermally-induced reentrance of a coupled spin-electron model on a decorated square lattice, Physica E: Low-dimensional Systems and Nanostructures 115 (2020) 113717. doi:10.1016/j.physe.2019.113717.

[64] R. H. McKenzie, A strongly correlated electron model for the layered organic superconductors $\kappa$-(BEDT-TTF)$_2$X, Comments on Condensed Matter Physics 18 (1998) 309. arXiv:cond-mat/9802198.

[65] E. Scriven, B. J. Powell, Effective Coulomb interactions within BEDT-TTF dimers, Physical Review B 80 (20) (2009) 205107. doi:10.1103/PhysRevB.80.205107.

[66] T. Koretsune, C. Hotta, Evaluating model parameters of the $\kappa$- and $\beta'$-type Mott insulating organic solids, Physical Review B 89 (4) (2014) 045102. doi:10.1103/PhysRevB.89.045102.

[67] A. C. Jacko, E. P. Kenny, B. J. Powell, Interplay of dipoles and spins in $\kappa$-(BEFT-TTF)$_2$X, where X=Hg(SCN)$_2$Cl, Hg(SCN)$_2$Br, Cu[N(CN)$_2$]Cl, Cu[N(CN)$_2$]Br and Ag$_2$(CN)$_3$, Physical Review B 101 (12) (2020) 125110. doi:10.1103/PhysRevB.101.125110.

[68] M. Dressel, S. Tomić, Molecular quantum materials: Electronic phases and charge dynamics in two-dimensional organic solids, Advances in Physics 69 (1) (2020) 1-120. doi:10.1080/00018732.2020.1837833.

[69] O. Nájera, M. Civelli, V. Dobrosavljević, M. J. Rozenberg, Resolving the VO$_2$ controversy: Mott mechanism dominates the insulator-to-metal transition, Physical Review B 95 (3) (2017) 035113. doi:10.1103/PhysRevB.95.035113.

[70] D. Matsunami, A. Fujita, Electrocaloric effect of metal-insulator transition in VO$_2$, Applied Physics Letters 106 (4) (2015) 042901. doi:10.1063/1.4906801.

[71] K. Král, J. Málek, B. Hejda, S. Záliš, Supermolecular CNDO/S calculation of parameters for extended Hubbard hamiltonian of TCNQ dimers, Chemical Physics 45 (1) (1980) 101-108. doi:10.1016/0301-0104(80)85172-X.

[72] C. J. Calzado, J. Cabrero, J. P. Malrieu, R. Caballol, Analysis of the magnetic coupling in binuclear complexes. I. Physics of the coupling, The Journal of Chemical Physics 116 (7) (2002) 2728-2747. doi:10.1063/1.1430740.

[73] M. Nakano, R. Kishi, S. Ohta, H. Takahashi, T. Kubo, K. Kamada, K. Ohta, E. Botek, B. Champagne, Relationship between Third-Order Nonlinear Optical Properties and Magnetic Interactions in Open-Shell Systems: A New Paradigm for Nonlinear Optics, Physical Review Letters 99 (3) (2007) 033001. doi:10.1103/PhysRevLett.99.033001.

[74] K. Kamada, K. Ohta, A. Shimizu, T. Kubo, R. Kishi, H. Takahashi, E. Botek, B. Champagne, M. Nakano, Singlet Diradical

Accepted manuscript. The final version was published in:
Journal of Magnetism and Magnetic Materials 527, 167767 (2021),
DOI:10.1016/j.jmmm.2021.167767

Character from Experiment, The Journal of Physical Chemistry
Letters 1 (6) (2010) 937-940. doi:10.1021/jz100155s.

[75] F. López-Urías, G. M. Pastor, Exact diagonalization of Hubbard
clusters at finite temperatures, The European Physical Journal D
52 (1) (2009) 159. doi:10.1140/epjd/e2009-00009-9.

[76] R. M. Fye, D. J. Scalapino, R. T. Scalettar, Enhance-
ment of binding energies in linked Hubbard clus-
ters, Physical Review B 46 (13) (1992) 8667-8670.
doi:10.1103/PhysRevB.46.8667.

[77] R. Schumann, Thermodynamics of a 4-site
Hubbard model by analytical diagonalization,
Annalen der Physik 11 (1) (2002) 49-88.
doi:10.1002/1521-3889(200201)11:1<49::AID-ANDP49>3.0.CO;2-7.

[78] R. Schumann, Rigorous solution of a Hubbard model extended
by nearest-neighbour Coulomb and exchange interaction on a
triangle and tetrahedron, Annalen der Physik 17 (4) (2008) 221-
259. doi:10.1002/andp.200710281.