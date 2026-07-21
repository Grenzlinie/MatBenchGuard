# Electrohydrodynamic Stresses from Hydrogen-Bond Network Dynamics in Water

Pramodt Srinivasula*
Electrosoft labs LLP, Mumbai, India

The resistance of hydrogen-bond networks to ambient flow in water produces viscoelectric stresses and contributes to electrostrictive pressure. Within Onsager's nonequilibrium thermodynamic framework, a lattice-gas description of aqueous electrolytes is combined with a coarse-grained hydrodynamic representation of hydrogen-bonded molecular networks, where viscous dissipation is modeled through energetically equivalent Brownian entities. This formulation connects molecular structural information from experiments and molecular dynamics to a unified dipolar Poisson-Nernst-Planck-Stokes (dPNP-S) continuum theory, quantitatively reproducing the measured viscoelectric coefficient of Jin *et al.* [1] and contributions to electrostrictive pressure. These results identify a microscopic mechanism by which hydrogen-bond dynamics influence electrohydrodynamic flow.

*Motivation*– Water, though seemingly simple at the macroscale, exhibits complex behavior that reflects its intricate molecular structure. The hydrogen-bonding and dipolar interactions among the water molecules play a pivotal role in governing both dielectric and hydrodynamic responses, particularly under an external electric field, manifesting in phenomena such as dielectric saturation [2], viscoelectric effect (VE) [1, 3] and electrostrictive (ES) pressure[4, 5].

The dielectric saturation influences electric double layer (EDL) behaviour via reducing permittivity from 80 to as low as 2[6] during its evolution [7] upto several micrometer distances from the electrode surface through hydrogen bonded (HB) networks [8]. VE and ES are interpreted using the decades-old empirical formulations[5, 9] beyond the scope of their original experimental settings. For example, the VE coefficient value $10^{-15}\ \text{m}^2\text{V}^{-2}$ for water is widely used in modelling, where it significantly influences the nanoscale hydrodynamics across a different range of temperature and salt concentration[10–12].

Modern MD studies indicate that hydrogen-bonded water clusters associated with viscous behaviour comprise roughly 25 molecules at low shear, which gives an effective water cluster structural radius ($R_{\text{wc}}$) of approximately $0.5\pm0.1\ \text{nm}$ [13–15]. Whereas HB correlation dynamics can extend further over a distance $l_d=1.75\pm0.25\ \text{nm}$ in the network [16] and manifest as a slower Debye-like timescale [17]. Beyond viscosity changes, Zong *et al.* [14] observed an approximately linear increase in activation free energy, $\delta(\Delta G)\sim600\ \text{J/mol}$ at 298 K for strong electric field variations $\delta|\text{E}|\sim1\ \text{V/nm}$, attributed to hydrogen-bond network reorganization in a background medium of relative permittivity 80.

Similarly, light- and neutron-scattering measurements [18] further showed that although no persistent molecular structures exist beyond a few molecular diameters, water exhibits a slower Debye-like relaxation over nanometer length scales. Similar observations were made in other polar liquids as well [19]. These observations are consistent with the dielectric spectrometry results of Jansson *et al.* [20], which identified a 4-5 orders slower Debye-like relaxation in pure water due to HB networks (despite some initial concerns regarding electrode insulation effects masking the results).

Despite these advances, a mechanistic continuum description of hydrogen-bond network dynamics in nanofluidic systems remains limited, particularly for realistic nanopores with lateral dimensions up to hundreds of nanometers involving transient electrokinetic processes [21,22]. This work introduces a coarse-grained hydrodynamic theory and captures the additional hydrodynamic stress contributions in the Stokes equation arising from the collective dynamics of the hydrogen-bond network.

*Theory*– Guided by molecular dynamics simulations and experiments, the slow collective dynamics of hydrogen-bond network segments are modeled as orientable Brownian entities embedded within the molecular lattice-gas description of the electrolyte. These entities represent coarse-grained segments of the hydrogen-bond network whose orientational dynamics generate

![](./images/1240245403585085443_1.jpg)

FIG. 1. Schematics: (a) Electric-field-induced hydrogen-bond restructuring across molecular, cluster, and network scales. Colored spheres denote oxygen (red), hydrogen (light gray), and water clusters (dark gray); solid and dashed bonds indicate covalent and HB correlations. Arrows indicate structural orientation (black) electric field & induced rotation (blue), ambient flow (orange), and rotational diffusion (grey). (b) Coarse-grained Brownian-particle representation of the HB network embedded in a molecular lattice; sticks denote structural correlations between molecules (spheres). (Color online.)

---
* Previously at Department of Mechanical Engineering, TU Darmstadt,
where part of this research was conducted.

additional dielectric and hydrodynamic stresses dur- ing electrical double-layer evolution in nanochannels of width 10–100 nm. Viscous dissipation associated with hydrogen-bond network dynamics is represented by identical Brownian particles with an equivalent coarse- graining radius $R_{B}=R_{wc}+l_{d}=2.25$ nm, uniformly filling the space with a concentration $c_{B}=R_{B}^{-3} ~m^{-3}$. Hence, for water with molecular density $c_{s 0}=55000 N_{A} ~m^{-3}$ at 298 K (for density $990 ~kg / m^{3}$, Avogadro number $N_{A}$ ), each HB network segment analogous to a Brownian particle consists of $n_{B} \approx 3020$ molecules. The reorganization of water clusters, due to electric-field-induced realignment of dipolar molecules and the associated restructuring of the HB network, results in an effective reorientation of the virtual Brownian particles, as illustrated in Fig. 1(a).

Consider an electric field $\mathbf{E}=|\mathbf{E}| \hat{\mathbf{E}}=-\nabla \psi$ imposed on the aqueous electrolyte. Based on the above data fromZong et al. [14], reorientation of the representative Brown- ian particles along a strong electric field is interpreted as a linear field-energy coupling, $\delta(\Delta G)(n_{B} / N_{A}) \approx$ $p_{0 B} \delta(E)$ . This defines a virtual, energetically equiva lent Brownian particles dipole of moment $p_{B}=p_{0 B} \hat{p}_{B}$ of constant magnitude $p_{0 B} \simeq 633 D$ , characterized by a spatiotemporal mean-field orientation probability f_B(p0B, E, κ, x, t). This decouples hydrogen-bond net- work energetics from the intrinsic molecular dipole con- tribution $\overline{p}$ , arising from individual dipoles and their in teractions (per molecule), which determines the effective dipole moment per molecule $p_{e}$ consistent with the zero field relative permittivity $\varepsilon_{r 0}$ . Hence, $\overline{p}=p_{e}-p_{B} / n_{B}$ . Numerically, $p_{0 B}$ is about one order of magnitude smaller than the summed molecular dipole moment of water within the corresponding hydrogen-bond network seg- ment, with $|\overline{p}| \sim 1.85-3 D[14])$ within the correspond ing HB network segment. Thus a relevant parameter is identified as $\alpha_{1}=p_{0 B} /(n_{B}|\overline{p}|) \sim 0.1$ .

The electric-field-induced reorientation of hydrogen- bond network segments is additionally modulated by ther- mal fluctuations, represented as orientational diffusion of the equivalent Brownian particles, and by hydrodynamic deformation through the local velocity-gradient tensor $\kappa=\nabla v$ and fluid viscosity $\eta$ . Viscosity at zero electric field is $\eta_{0} \cong 8.9 ×10^{-4} ~Pa$ s at 298 K [23]. Consider a Jeffery's prolate spheroidal Brownian particle with as- pect ratio (of major to minor axes lengths) $\Theta_{B}$ . For weak geometric anisotropy, $\delta_{B}=(\Phi_{B}-1) \ll 1$ , the difference in axial and equatorial rotational resistance coefficients scales linearly as $\sim 0.3 \delta_{B}$ [24]. This correction is there fore subleading, and the rotational friction may be taken isotropic to leading order as, $\zeta_{B}^{r}=8 \pi \eta_{0} R_{B}^{3} F_{eq } / \Theta_{B}^{2}$ .

$$
F_{\mathrm{eq}}=\frac{4}{6} \frac{\left(1 / \Theta_{B}\right)^{2}-\Theta_{B}^{2}}{1-\left[\tanh ^{-1}\left(\sqrt{1-\frac{1}{\Theta_{B}^{2}}}\right) / \sqrt{1-\frac{1}{\Theta_{B}^{2}}}\right]\left(2-\frac{1}{\Theta_{B}^{2}}\right)} \quad(1)
$$

is Perrin's rotational friction factor [25]. Approximating its rotational diffusivity $D_{r, B}$ from the Stokes-Einstein relation $\beta D_{r, B} \zeta_{B}^{r}=1$ , the first-order rotational relaxation time is $\tau_{r, B}=\zeta_{r, B} \beta / 2$ . Here $\beta$ is the inverse temperature parameter. Matching this to the experimentally observed Debye-like timescale of 29.5 ns for pure water at 298 K [20], we obtain a small anisotropy $\delta_{B}=0.0273$ .

The coarse-grained representation is combined with the standard uniform molecular lattice gas model (Fig.1(b)), where they capture different degrees of freedom, at the network and molecular levels, respectively. Water molecules are modeled as spherical dipoles of constant magnitude moments $\overline{p}=\overline{p}_{0} \hat{p}$ with a mean-field orien tational distribution $f(\overline{p}_{0}, E, x, t)$ . The mean-field free energy functional $F$ for a lattice representing a dilute to moderately concentrated aqueous electrolyte (inter- ion, ion-water cluster interactions ignored) can be ex- pressed in terms of spatio-temporal ion concentrations $c_{ \pm}(x, t)$ with valencies $z_{ \pm}$ , solvent concentration $c_{s}(x, t)$ ,weighted angular averages $<(\cdot)>=(\int d \hat{p} f(\cdot)) / \int d \hat{p}$  over the orientational degrees of freedom of the dipoles, $<(\cdot)>_{B}=(\int d \hat{p}_{B} f_{B}(\cdot)) / \int d \hat{p}_{B}$ for Brownian clusters:

$$
\begin{aligned}
\mathcal{F}= & \int d \mathbf{x}\left[\left(\psi \rho_{i}-\frac{\varepsilon_{0}}{2}|\nabla \psi|^{2}\right)+\frac{1}{\beta}\left(c_{+} \ln \left(\frac{c_{+}}{c_{0}}\right)+c_{-} \ln \left(\frac{c_{-}}{c_{0}}\right)+c_{s} \ln \left(\frac{c_{s}}{c_{s 0}}\right)\right)+\lambda_{1}\left(c_{+} c_{-}+c_{s}-c_{L}\right)\right]-\int d \mathbf{x} c_{s}\left[g \overline{p}_{0}^{2}\right. \\
& \left.+\gamma_{c}\langle\overline{\mathbf{p}} \cdot \nabla \psi\rangle+\left(\frac{<\ln f>-\lambda_{2}(<f>-1)}{\beta}\right)\right]+\int d \mathbf{x} c_{B}\left[\left\langle\mathbf{p}_{B} \cdot \nabla \psi\right\rangle_{B}+\left(\frac{<\ln f_{B}>_{B}-\lambda_{2 B}\left(<f_{B}>_{B}-1\right)}{\beta}\right)\right].
\end{aligned}
$$

Here, $\varepsilon_{0}, e_{0}$ denote the permittivity of free space and the elementary charge; $g, \gamma_{c}$ are the solvent dipolar reaction field and cavity parameters; $c_{0}, c_{s 0}$ are the bulk concentra tions of ions and solvent; and $\rho_{i}=e_{0}(z_{+} c_{+}+z_{-} c_{-})$ is the ionic charge density. The first two integrals correspond to finite ion effects [26], and dipolar solvent effects [27, 28] from the molecular lattice model, respectively. These represent electrostatic field interaction with the ions and the field's self energy; translational entropy of molec- ular species (crowding effects) with lattice-occupation constraint of constant total lattice space concentration $c_{L}=c_{s 0}+2 c_{0}$ enforced by Lagrange multiplier $\lambda_{1}(x)$ ; solvent dipolar interactions energy with reaction field, dipole-field coupling with cavity effect; and orientational entropy with normalization via $\lambda_{2}(x)$ , in the order. The last integral corresponds to the equivalent Brownian HB network clusters incorporating the field-induced energy and orientational entropy with normalization via $\lambda_{2 B}(x)$ .

The standard Langevin-Boltzmann distribution of molecular dipole orientations subjected to an exter-

nal electric field of nominal magnitude $E_0$, $f = (\alpha_2\tilde{E}/sinh(\alpha_2\tilde{E}))e^{\alpha_2\hat{\mathbf{p}}\cdot\tilde{\mathbf{E}}}$, is obtained from $\partial\mathcal{F}/\partial f = 0$ [27]. Here $\tilde{\mathbf{E}} = \tilde{E}\hat{\mathbf{E}}$ is a normalized electric field with magnitude $\tilde{E} = |\mathbf{E}|/E_0$ and $\alpha_2 = \gamma_c\overline{p}_0E_0\beta$ is a dimensionless number indicating relative magnitude of electric field influence on the molecular dipolar orientation. The standard Onsager's non equilibrium thermodynamic principles for electrostatics $\delta\mathcal{F}/\delta\psi = 0$, and species chemical potentials $\mu_{\pm,s} = M_{\pm,s}+\lambda_1 = \delta\mathcal{F}/\delta c_{\pm,s}$ with ion fluxes $J_{\pm,s} = -\beta D_{\pm,s}c_{\pm,s}\nabla\mu_{\pm,s}$ [26], gives the Poisson and advective Nernst-Planck equations,

$$
-\varepsilon_0\nabla^2\psi=\rho_i+\rho_s,\quad \rho_s=-\nabla\cdot\left(\mathbf{P}\left(1+\frac{\alpha_1<\hat{\mathbf{p}}_B>B}{\gamma_c\ <\hat{\mathbf{p}}>}\right)\right) \tag{3}
$$

$$
\begin{aligned}
\dot{c}_{\pm}=&D_{\pm}\bigg[z_{\pm}e_0\beta\nabla\cdot(c_{\pm}\nabla\psi)+\nabla^2c_{\pm}+\nabla\cdot\left(\frac{c_{\pm}\nabla c}{c_L - c}\right)\\
&+\alpha_2\nabla\cdot\left(c_{\pm}(\nabla\tilde{E})\mathcal{L}\right)+\beta\nabla\cdot\left(c_{\pm}\nabla\mu_s\right)\bigg]-\nabla\cdot(c_{\pm}\mathbf{v}), \tag{4}
\end{aligned}
$$

where overdot denote time derivative. The solvent molecular and HB network effects reflect as the additional dipolar charge $\rho_s$ and the dipolar solvent-induced ionic flux (second line of Eq. (4)). Here $\mathcal{L}=<\hat{\mathbf{p}}\cdot\tilde{\mathbf{E}}> = coth(\alpha_2\tilde{E})-(\alpha_2\tilde{E})^{-1}$ is the Langevin function and $\mathbf{P} = \gamma_c c_s<\overline{\mathbf{p}}>$ is the polarization density vector with $\langle\overline{\mathbf{p}}\rangle=p_0\mathcal{L}\hat{\mathbf{E}}$, parallel to $\tilde{\mathbf{E}}$.

The molecular level degrees of freedom in the lattice model equilibrate into fixed material parameters, such as a contribution towards the solvent viscosity $\eta_f$ (excluding HB effects). However, the contributions arising from the slower, collective dynamics of HB-network segments remain to be evaluated. The Onsager's variational functional (or Rayleighian) $\mathcal{R}$ incorporating both molecular transport and mesoscale hydrogen-bond network dynamics is constructed as the sum of a dissipation functional $\Phi$ and the rate of change of free energy $\dot{\mathcal{F}}$ [29].

$$
\mathcal{R}=\Phi+\dot{\mathcal{F}}-\iint d\mathbf{x}d\hat{\mathbf{p}}_B\lambda_3(\dot{\hat{\mathbf{p}}}_B\cdot\hat{\mathbf{p}}_B)+\int d\mathbf{x}\lambda_4(\nabla\cdot\mathbf{v}) \tag{5}
$$

$$
\begin{aligned}
\Phi=&\int d\mathbf{x}\bigg[\frac{\eta_f}{4}\left(\boldsymbol{\kappa}+\boldsymbol{\kappa}^T\right)^2\\
&+\frac{c_B\zeta_B^r}{4}\left\langle2(\dot{\hat{\mathbf{p}}}_B-\dot{\hat{\mathbf{p}}}_{f,B})^2+\overline{\chi}(\hat{\mathbf{p}}_B\cdot\boldsymbol{\kappa}\cdot\hat{\mathbf{p}}_B)^2\right\rangle_B\bigg] \tag{6}
\end{aligned}
$$

$$
\dot{\mathcal{F}}=\int d\mathbf{x}\left(\mu_+\dot{c}_++\mu_-\dot{c}_-+\mu_s\dot{c}_s+\frac{\delta\mathcal{F}}{\delta f}\dot{f}+\frac{\delta\mathcal{F}}{\delta f_B}\dot{f}_B\right) \tag{7}
$$

Lagrange multipliers $\lambda_3(\hat{\mathbf{p}}_B)$ and $\lambda_4(\mathbf{x})$ enforce fixed dipole magnitude $(\dot{\hat{\mathbf{p}}}_B\cdot\hat{\mathbf{p}}_B = 0)$ and continuum level incompressibility $(\nabla\cdot\mathbf{v}=0)$, respectively.

The flow-induced rate of the dipole orientation of a Brownian particle is $\dot{\hat{\mathbf{p}}}_{f,B}=\hat{\mathbf{p}}_B^\perp\cdot(\mathbf{R}+\chi\mathbf{D})\cdot\hat{\mathbf{p}}_B$, where, $\mathbf{R}$ and $\mathbf{D}$ are the antisymmetric and symmetric parts of the velocity gradient tensor $\boldsymbol{\kappa}$, respectively, and $\hat{\mathbf{p}}_B^\perp=\mathbf{I}-\hat{\mathbf{p}}_B\hat{\mathbf{p}}_B$ is the transverse projection operator [30]. The shape factor $\chi=(\Theta_B^2-1)/(\Theta_B^2+1)$ reduces to $\chi\simeq\delta_B$ in the small anisotropy limit. The dissipation function $\Phi$ (Eq. (6)) accounts for molecular lattice viscous contribution $(\eta_f)$ to ambient flow and hydrodynamic torques on Brownian particle arising from relative angular motion and anisotropic extensional coupling, respectively. Here, for weak anisotropy, the torque-flow coupling coefficient based on resistance tensors is $\overline{\chi}\simeq\delta_B/2$ [24, 30].

The unified hydrodynamics across scales follow from the Rayleighian variational principle. Introducing a characteristic velocity-gradient magnitude $\dot{\gamma}$ (identified with the shear rate for general shear flows), we can write, $(\mathbf{R}+\chi\mathbf{D})=\dot{\gamma}(\boldsymbol{\kappa}(1+\chi)-\boldsymbol{\kappa}^T(1-\chi))$. Dimensionless numbers $\alpha_{2B}=p_{0B}E_0\beta$, and $\alpha_3=\dot{\gamma}/D_{r,B}$ with the rotational diffusivity of Brownian particle model $(D_{r,B}\sim R_B^{-3})$ indicate magnitudes of the electric and flow field influences on the Brownian particle dynamics. Imposing the conservation of orientation probability $\dot{f}_B=-\nabla_{\hat{\mathbf{p}}_B}\cdot(f_B\dot{\hat{\mathbf{p}}}_B)$ (with notation $\nabla_{\hat{\mathbf{p}}_B}=\partial/\partial\hat{\mathbf{p}}_B$) in the weak flow limit $\alpha_3\ll1$, Onsager's principle $\delta\mathcal{R}/\delta\hat{\mathbf{p}}_B=0$ reduces to $f_{0B}=(\alpha_{2B}/sinh(\alpha_{2B}))e^{\alpha_{2B}\hat{\mathbf{p}}_B\cdot\tilde{\mathbf{E}}}(1+O(\alpha_3))$, and hence $\rho_s\approx-\nabla\cdot(\mathbf{P}(1+\alpha_1\alpha_2/\alpha_{2B}))$, for small $\alpha_2$ and $\alpha_{2B}$, as detailed in Appendix A.

Variation of the Rayleighian with respect to the velocity field, $\delta\mathcal{R}/\delta\mathbf{v}=0$, yields the Stokes equation [29]. Upon evaluating the required orientation-weighted integrals involving $f,f_{0B}$ and following mathematical simplifications for the case of simple shear, at small $\alpha_2$ and $\alpha_{2B}$ one obtains the following with VE and ES terms as shear and isotropic stress corrections (see Appendix B).

$$
\begin{aligned}
&\left[-\nabla\cdot(\eta_0\nabla\mathbf{v})-\nabla\cdot\left(\frac{c_B\zeta_B^r\overline{\chi}\alpha_{2B}^2}{315}\tilde{E}^2\nabla\mathbf{v}\right)\right]+\left[\rho_i\nabla\psi+\nabla(\mathbf{P}\cdot\nabla\psi)\right.\\
&\left.+\frac{\alpha_2^2}{6}\nabla\left(c_s\tilde{E}^2\right)\right]-\nabla\cdot\left[\lambda_4+c_L\lambda_1+\frac{4\Theta_B\alpha_{2B}^2}{15\beta}(c_B\tilde{E}^2)\right]\mathbf{I}=0 \tag{8}
\end{aligned}
$$

Here, the three square-bracketed groups of terms correspond to shear, body force and pressure, respectively.

Molecular-scale contributions from $\delta\dot{\mathcal{F}}/\delta\mathbf{v}$ enter as a Maxwell body force, comprising Coulombic and dielectrophoretic components, together with solvent dipolar orientation variation dependent osmotic force, respectively. A pressure correction additionally emerges from the Lagrange multiplier $\lambda_1$, enforcing the lattice-level constraint on molecular compressibility, thereby renormalizing the continuum pressure $\lambda_4$.

The HB-network contribution generates multiple stress components. The extensional-rotational coupling in the dissipation function $\Phi$ (last term of Eq. 6) produces a shear stress contributing along with the ambient fluid dissipation (first term of Eq. 6). Put together, the leading-order term yields the zero-field viscosity, $\eta_0=\eta_f+c_B\zeta_B^r\overline{\chi}/15$, while higher-order term $O(\alpha_{2B})$ give rise to the viscoelectric correction. In addition, dissipation associated with relative angular motion (second term of Eq. 6) for the anisotropic (slender) component in a deformational flow produces an isotropic stress, recognized as a contribution to the well-known electrostrictive

pressure ($\Pi_{e_s}$); While the spherical rotational component generates no stress.

Application– Eq. (3), (4) and (8) comprise dipolar Poisson–Nernst–Planck–Stokes (dPNP–S) framework, applicable to a broad range of practical scenarios. The standard spatiotemporal anisotropic nonlinear relative permittivity is defined in terms of polarization density $\mathbf{P}$ as, $\varepsilon_{r}=\mathbf{I}+\varepsilon_{0}^{-1} \nabla_{\mathbf{E}} \mathbf{P}$ (with $(\nabla_{\mathbf{E}} \mathbf{P})_{i j}=\partial P_{i} / \partial E_{j}$ in index notation) [5]. In the limits $\alpha_{2} \ll 1, \alpha_{1} \ll 1$, the leading order isotropic approximation $\varepsilon_{r} \approx \varepsilon_{r 0}=1+c_{s} \gamma_{c} p_{0}^{2} \beta \varepsilon_{0}^{-1} / 3$ yields the field-independent estimate implying $p_{0} \approx\left|\mathbf{p}_{e}\right|$. Enforcing the lattice-occupation constraint on the species fluxes yields $\nabla \lambda_{1}=-\left(\sum_{i= \pm, s} D_{i} c_{i} \nabla M_{i}\right) / \sum_{i= \pm, s} D_{i} c_{i}$. For the equal size of molecules occupying the uniform lattice, the species diffusivities $D_{\pm,s}$ are comparable in magnitudes, which is a reasonable approximate for typical monovalent electrolytes. For dilute-electrolytes $(c_{0}/c_{L}\ll1)$ the weak dipolar effect $(\alpha_{2} \ll 1)$, implies $\lambda_{1} \rightarrow-M_{s}$, so that the effective solvent chemical potential in Eq. (4) vanishes, $\mu_{s} \rightarrow 0$, and the molecular pressure correction in Eq: (8) approaches: $c_{L} \nabla \lambda_{2} \rightarrow c_{L} \alpha_{2} \mathcal{L} \nabla \tilde{E}$. In appropriate asymptotic limits, the dPNP–S model recovers several established descriptions: the MLB model [28] at steady state and further the LB model for $\alpha_{2} \ll 1, \gamma_{c}=1$ with appropriate $|\mathbf{p}_{e}|$; the modified PNP (mPNP) model [26] for $\alpha_{2} \epsilon_{D}^{2} \ll 1$, and further, the classical PNP model for $c_{0}/c_{s0} \ll 1$; and the macroscopic Stokes equation with Maxwell stress for $\alpha_{1} \ll 1, \alpha_{2} \ll 1, \alpha_{2B} \ll 1$. Here, $\epsilon_{D}=\lambda_{D}/L$ is the dimensionless Debye length.

The empirical viscoelectric coefficient for quadratic field dependence, estimated using the nominal electric field $E_{0}$ and Poisson-Boltzmann theory for the experimental conditions of Jin *et al.* [1], is obtained from Eq. 8 (see Appendix C) as $f_{v}=(0.96 \pm 0.4) \times 10^{-15} \ (\text{m/V})^{2}$, in quantitative agreement with the reported value. Similarly, the prefactor of the electrostrictive pressure arising from HB network effects is of comparable magnitude, though slightly larger, than the statistical Kirkwood correlation factor $g_{k}$ (see Appendix C).

The dPNP–S equations are solved numerically for electroosmotic flow in a nanofluidic electrolytic cell with surface potential, Stern layer, and no-slip boundaries, using experimentally relevant parameters in the limit $\alpha_{1} \ll 1$. Hydrogen-bond (HB) network dynamics introduce spatiotemporal variations in the effective permittivity and viscoelectric (VE) coefficient during electric double-layer evolution, differing from simpler transient implementations based on a constant empirical VE coefficient (noted *LBFT–VE* in the *joint PRF submission*). To isolate these effects, dPNP–S predictions obtained by neglecting the electrostrictive pressure and dipolar orientational osmotic contributions in Eq. 8 are compared with the LBFT–VE model. Figure 2(a) shows that HB-network dynamics produce pronounced deviations in the evolution of the normalized permittivity $\varepsilon_{r}/\varepsilon_{r0}$ and VE coefficient $f_{v}/f_{v0}$ near the electrode surface. These variations propagate into measurable corrections in the electroosmotic mobility of the induced flow, $\mu_{eo}=\int_{0}^{l} dx\ v/(lE_{0})$, relative to the classical PNP–Stokes prediction, as shown in Fig. 2(b) for representative parameter sets (Cases I and IV of the *joint PRF submission*).For weak dipolar coupling (Case IV, $\alpha_{2} \epsilon_{D}^{2} \sim 10^{-5}$), dPNP–S converges to mPNP, while for stronger coupling (Case I, $\alpha_{2} \epsilon_{D}^{2}=0.37$) it departs significantly. In both regimes, it differs from LBFT–VE, demonstrating the hydrodynamic impact of HB-network dynamics.

![](./images/1240245403585085443_2.jpg)

FIG. 2. (a) Evolution of $\varepsilon_{r}/\varepsilon_{r0}$ and $f_{v}/f_{v0}$ from dPNP-S compared to LB-fitted transient viscoelastic models (LBFT-VE). Black arrows indicate the evolution from time 0.5 to 5 times of Debye timescale $(\tau_{D})$. (b) Electroosmotic mobility correction factor over PNP for different parametric cases (refer to the *joint PRF submission*), using different models. (Color online.)

Insights– The weak anisotropy of the Brownian-particle representation $(\delta_{B} \ll 1)$ reflects the strong resistance of the hydrogen-bond (HB) network to shear deformation. Unlike prior treatments assuming a constant viscoelectric coefficient $f_{v}$, the present theory resolves its intrinsic spatiotemporal dependence on ion concentration and electric-field strength, allowing direct implementation in continuum models. Electrostrictive pressure macroscopically associated with dielectric variations under strain is correlated to the underlying HB network dynamics. Fundamentally, this theory provides a molecular-to-continuum multiscale connection between HB-network structure, its characteristic scales, and the resulting observable phenomena. Future nanofluidic measurements of EOF mobility under periodic electric fields, combined with molecular dynamics simulations, could help validate and refine the model.

Conclusion– To represent the collective dynamics of the hydrogen-bond network, transient clusters are modeled as orientable Brownian particles, consistent with molecular dynamics and experimental observations [13, 14, 16, 20]. Within Onsager's variational framework, this coarse-grained description leads to a dipolar Poisson–Nernst–Planck–Stokes (dPNP–S) continuum theory for coupled ion and fluid transport. In this formulation, the hydrogen-bond network contributes as a particle-like component distinct from the background solvent response, represented by orientable dipolar entities whose rotational dynamics generate stresses reminiscent of dipolar suspensions. The resulting framework quan-

titatively predicts transient dielectric saturation, visco- electric responses, and electrostrictive contributions, en- abling a physically grounded solvent-enriched continuum electrohydrodynamics beyond empirical closures.

Declarations- No data were created or used in this study. This research received no specific grant from any funding agency. The author declares no competing inter- ests.

[1] D. Jin, Y. Hwang, L. Chai, N. Kampf, and J. Klein, Direct measurement of the viscoelectric effect in water, Proceedings of the National Academy of Sciences 119, e2113690119 (2022).

[2] F. Alvarez, A. Arbe, and J. Colmenero, The debye's model for the dielectric relaxation of liquid water and the role of cross-dipolar correlations. a md-simulations study, The Journal of Chemical Physics 159 (2023).

[3] A. Baer, Z. Miličević, D. M. Smith, and A.-S. Smith, Water in an electric field does not dance alone: The relation between equilibrium structure, time dependent viscosity and molecular motions, Journal of molecular liquids 282, 303 (2019).

[4] P. Drude and W. Nernst, Über elektrostriktion durch freie ionen, Zeitschrift für physikalische Chemie 15, 79 (1894).

[5] L. D. Landau, J. S. Bell, M. Kearsley, L. Pitaevskii, E. Lif- shitz, and J. Sykes, Electrodynamics of continuous media, Vol. 8 (elsevier, 2013).

[6] L. Fumagalli et.al., Anomalously low dielectric constant of confined water, Science 360, 1339 (2018).

[7] C. Colosi, M. Costantini, A. Barbetta, C. Cametti, and M. Dentini, Anomalous debye-like dielectric relaxation of water in micro-sized confined polymeric systems, Physical Chemistry Chemical Physics 15, 20153 (2013).

[8] J.-m. Zheng, W.-C. Chin, E. Khijniak, E. Khijniak Jr, and G. H. Pollack, Surfaces and interfacial water: evidence that hydrophilic surfaces have long-range impact, Advances in colloid and interface science 127, 19 (2006).

[9] J. Lyklema and J. T. G. Overbeek, On the interpretation of electrokinetic potentials, Journal of Colloid Science 16, 501 (1961).

[10] W. Hsu, Daiguji, Dunstan, M. Davidson, and D. Harvie, Electrokinetics of the silica and aqueous electrolyte solu- tion interface: Viscoelectric effect, ACIS 234, 108 (2016).

[11] K. Saurabh and M. Solovchuk, Mathematical and com- putational modeling of electrohydrodynamics through a nanochannel, AIP Advances 13 (2023).

[12] S. K. Mehta, G. Biswas, and P. K. Mondal, Arresting of viscoelectric effect modulated flow reduction in nanochan- nels with imposed temperature gradients, Langmuir 41, 19754 (2025).

[13] Y. Gao, J. Wu, Y. Feng, J. Han, and H. Fang, Structural effects of water clusters on viscosity at high shear rates, The Journal of Chemical Physics 160 (2024).

[14] D. Zong, H. Hu, Y. Duan, and Y. Sun, Viscosity of water under electric field: Anisotropy induced by redistribution of hydrogen bonds, The Journal of Physical Chemistry B 120, 4818 (2016).

[15] S. Maheshwary, N. Patel, N. Sathyamurthy, A. D. Kulka- rni, and S. R. Gadre, Structure and stability of water clus- ters (h2o) n, n= 8- 20, JPC A 105, 10525 (2001).

[16] D. C. Elton, The origin of the debye relaxation in liq- uid water and fitting the high frequency excess response, Physical Chemistry Chemical Physics 19, 18739 (2017).

[17] I. Popov, P. B. Ishai, A. Khamzin, and Y. Feldman, The mechanism of the dielectric relaxation in water, Physical Chemistry Chemical Physics 18, 13941 (2016).

[18] K. Elamin, S. Cazzato, J. Sjostrom, S. M. King, and J. Swenson, Long-range diffusion in xylitol-water mix- tures, The Journal of Physical Chemistry B 117, 7363 (2013).

[19] Y. Wang, P. J. Griffin, A. Holt, F. Fan, and A. P. Sokolov, Observation of the slow, debye-like relaxation in hydrogen-bonded liquids by dynamic light scattering, The Journal of Chemical Physics 140 (2014).

[20] H. Jansson, R. Bergman, and J. Swenson, Hidden slow dynamics in water, Physical Review Letters 104, 017802 (2010).

[21] Y. He, M. Tsutsui, C. Fan, M. Taniguchi, and T. Kawai, Gate manipulation of dna capture into nanopores, ACS nano 5, 8391 (2011).

[22] T. Emmerich, Y. Teng, N. Ronceray, E. Lopriore, R. Chiesa, A. Chernev, V. Artemov, M. Di Ventra, A. Kis, and A. Radenovic, Nanofluidic logic with mechano-ionic memristive switches, Nature Electronics 7, 271 (2024).

[23] U. Kaatze, Complex permittivity of water as a function of frequency and temperature, Journal of Chemical and Engineering Data 34, 371 (1989).

[24] A. Satoh, Introduction to molecular-microsimulation for colloidal dispersions, Chapter-5, Vol. 17 (Elsevier, 2003).

[25] S. H. Koenig, Brownian motion of an ellipsoid. a correc- tion to perrin's results, Biopolymers: Original Research on Biomolecules 14, 2421 (1975).

[26] M. S. Kilic, M. Z. Bazant, and A. Ajdari, Steric effects in the dynamics of electrolytes at large applied voltages. ii. modified poisson-nernst-planck equations, Physical Re- view E—Statistical, Nonlinear, and Soft Matter Physics 75, 021503 (2007).

[27] A. Iglič, E. Gongadze, and K. Bohinc, Excluded volume effect and orientational ordering near charged surface in solution of ions and langevin dipoles, Bioelectrochemistry 79, 223 (2010).

[28] E. Gongadze and A. Iglič, Decrease of permittivity of an electrolyte solution near a charged surface due to saturation and excluded volume effects, Bioelectrochemistry 87, 199 (2012).

[29] M. Doi, Onsager's variational principle in soft matter, Jour- nal of Physics: Condensed Matter 23, 284118 (2011).

[30] S. Kim and S. J. Karrila, Microhydrodynamics: princi- ples and selected applications (Butterworth-Heinemann, 2013).

END MATTER

Appendix A.- The Onsager's principle $\delta \mathcal{R}/\delta \hat{\mathbf{p}}_{B}=0$ reduces to the Fokker-Planck type equation for the re-

orientation dynamics of the Brownian clusters $f_{B}$.

$$
\dot{f}_{B}=\nabla_{\hat{\mathbf{p}}_{B}} \cdot\left(D_{r}\left(\gamma_{c} \beta p_{0 B} f_{B} \nabla \psi+\nabla_{\hat{\mathbf{p}}_{B}} f_{B}\right) \cdot \hat{\mathbf{p}}_{B}^{\perp}-f_{B} \dot{\hat{\mathbf{p}}}_{f, B}\right) \quad(9)
$$

For the dilute-mild aqueous electrolytes $(c_{0} \sim 0.01-1$ mM) the EDL evolves at micro to submicro second time scale $\tau_{E D L}=\lambda_{D} L / D$ depending on the translational diffusivity of ions $D_{\pm, s} \sim 1 /(6 \pi \eta_{0} \beta a)$ with lattice element size $a=c_{L}^{-1 / 3}$ and Debye length $\lambda_{D}=$ √ε₀εᵣ₀/(2c₀z²e₀β) ~ 10 - 100 nm. Hence the Brown-ian cluster rotation can be considered quasistatic during EDL evolution. Integrating the above equation in Einstein's indices $(i, j, k)$ format, we get the following with an integration constant $c_{1}$.

$$
\begin{aligned}
f_{B}= & c_{1} e^{\frac{\alpha_{3}}{2} \tilde{\kappa}_{j k} \hat{p}_{B j} \hat{p}_{B k}-\alpha_{2 B} \hat{p}_{B i} \partial_{i} \psi} \\
& \int_{0}^{\pi} d \theta \sin \theta e^{\left(\alpha_{2 B} \cos \theta\left|\partial_{i} \psi\right|+\Lambda\right)} I_{0}\left(v_{1}\right) I_{0}\left(v_{2}\right) I_{0}\left(\frac{v_{3}}{2}\right) \quad(10)
\end{aligned}
$$

Here $I_{0}$ is the modified Bessel's function of first-kind in terms of functions of the angle $\theta$ between $\hat{\mathbf{p}}_{B}$ and $\mathbf{E}, v_{1}=$ (κ̃_xy + κ̃_yx) (α₃/2) cosθ sinθ, v₂ = (κ̃_xz + κ̃_zx) (α₃/2) cosθ sinθ and $v_{3}=(\tilde{\kappa}_{y z}+\tilde{\kappa}_{z y}) \frac{\alpha_{3}}{2} sin ^{2} \theta. \quad \Lambda=\tilde{\kappa}_{x x} cos ^{2}(\theta)+$ κ̃_yy sin²(θ)cos²(φ)+κ̃_zz sin²(θ)sin²(φ) consists of only the extensional terms of the velocity gradient. For a general shear flow (i.e., $\Lambda=0$) with small advection $\alpha_{3} \ll 1$, this approximates using the condition $\langle f_{B}\rangle=1$ to:

$$
f_{B}=f_{0 B}\left(1+\alpha_{3}\left(2 \overline{\chi} \hat{\mathbf{p}}_{B} \cdot \mathbf{D} \cdot \hat{\mathbf{p}}_{B}\right)+O\left(\alpha^{2}\right)\right), \quad(11)
$$

$$
f_{0 B}=\left(\alpha_{2 B} e^{\alpha_{2 B} \hat{\mathbf{p}}_{B} \cdot \tilde{\mathbf{E}}}\right) / \sinh \left(\alpha_{2 B}\right).
$$

Appendix B.- Useful Integrals: since $f_{0}$ is axisymmetric about the perturbing electric field $\mathbf{E}$, any tensorial moment of $f_{0}$ shall be constructed from the available invariant tensors under rotation of $\mathbf{E}$, such as δᵢⱼ, ÊᵢÊⱼ, δᵢⱼÊₖÊₗ, ÊᵢÊⱼÊₖÊₗ. Integrals below are evaluated using such an ansatz, when required.

$$
\frac{\mathbf{I}_{1}}{4 \pi}=\frac{\int d \hat{\mathbf{p}}_{B} f_{0} \hat{\mathbf{p}}_{B}}{4 \pi}=\mathcal{L}_{B} \tilde{\mathbf{E}}, \mathcal{L}_{B}=\operatorname{coth}\left(\alpha_{2 B} \tilde{E}\right)-\left(\alpha_{2 B} \tilde{E}\right)^{-1}(12)
$$

$$
\int d \hat{\mathbf{p}}_{B} f_{0} \ln \left(f_{0}\right)=4 \pi\left(\ln \left(\alpha_{2 B} \tilde{E} / \sinh \left(\alpha_{2 B} \tilde{E}\right)\right)+\alpha_{2 B} \tilde{E} \mathcal{L}_{B}\right)(13)
$$

$$
\int d \hat{\mathbf{p}}_{B} f_{0}\left(-\hat{\mathbf{p}}_{B} \cdot \nabla \psi\right)^{k}=\frac{4 \pi}{\alpha_{2 B}^{k}} \frac{\mathrm{d}^{k} Z}{Z \mathrm{~d} \tilde{E}^{k}}, Z=\frac{2 \sinh \left(\alpha_{2 B} \tilde{E}\right)}{\alpha_{2 B} \tilde{E}} \quad(14)
$$

$$
\mathbf{I}_{2}=\int d \hat{\mathbf{p}}_{B} f_{0}\left(\hat{\mathbf{p}}_{B} \hat{\mathbf{p}}_{B}-\frac{\mathbf{I}}{3}\right)=4 \pi\left(\left(\frac{\mathcal{L}_{B}}{\alpha_{2 B} \tilde{E}}-\frac{1}{3}\right) \mathbf{I}+\left(1-\frac{3 \mathcal{L}_{B}}{\alpha_{2 B} \tilde{E}}\right) \hat{\mathbf{E}} \hat{\mathbf{E}}\right),
$$

$$
\begin{aligned}
\mathbf{I}_{3}= & \int d \hat{\mathbf{p}}_{B} f_{0} \hat{\mathbf{p}}_{B} \hat{\mathbf{p}}_{B}\left(\hat{\mathbf{p}}_{B} \cdot \nabla \psi\right) \\
= & -4 \pi|\nabla \psi|\left[\left(\left(1+15 /\left(\alpha_{2 B} \tilde{E}\right)^{2}\right) \mathcal{L}_{B}-5 /\left(\alpha_{2 B} \tilde{E}\right)\right) \hat{\mathbf{E}} \hat{\mathbf{E}}\right. \\
& \left.+\left(1 /\left(\alpha_{2 B} \tilde{E}\right)-3 \mathcal{L}_{B} /\left(\alpha_{2 B} \tilde{E}\right)^{2}\right)\left(\hat{\mathbf{E}} \hat{\mathbf{E}}+(\hat{\mathbf{E}} \hat{\mathbf{E}})^{T}-\mathbf{I}\right)\right] \quad(15)
\end{aligned}
$$

$$
\int d \hat{\mathbf{p}}_{B} f_{0} \hat{\mathbf{p}}_{B}\left(\hat{\mathbf{p}}_{B} \cdot \nabla \psi\right)=4 \pi \nabla \psi\left(1-2 \mathcal{L}_{B} /\left(\alpha_{2 B} \tilde{E}\right)\right) \quad(16)
$$

$$
\int d \hat{\mathbf{p}}_{B} f_{0} \hat{\mathbf{p}}_{B}\left(\hat{\mathbf{p}}_{B} \cdot \nabla \psi\right)=4 \pi \nabla \psi\left(1-2 \mathcal{L}_{B} /\left(\alpha_{2 B} \tilde{E}\right)\right) \quad(17)
$$

Also, define a symmetric tensor $\mathbf{I}_{4}=p_{0 B} \beta\left(\mathbf{I}_{1} \nabla \psi-\mathbf{I}_{3}\right)+$ $3 \mathbf{I}_{2}=-8 \pi \mathbf{I}\left(1-3 \mathcal{L}_{B} / \alpha_{2 B} \tilde{E}\right)$.

Using these integrals, we get $\delta \Phi / \delta \mathbf{v}=-\nabla \cdot$ $(\eta_{f} \boldsymbol{\kappa}+\boldsymbol{\sigma}_{1}+\boldsymbol{\sigma}_{2}+\boldsymbol{\sigma}_{3})$ with $4 \pi \boldsymbol{\sigma}_{1}=-c_{B}\left(\mathbf{I}_{4}-\mathbf{I}_{4}^{T}\right)=0$, $4 \pi \boldsymbol{\sigma}_{2}=\chi c_{B}\left(\mathbf{I}_{4}+\mathbf{I}_{4}^{T}\right)$. For a small HB energetic effect, $\alpha_{2 B} \ll 1$, approximating $3 \mathcal{L}_{B} / \alpha_{2 B} \tilde{E}=1-\alpha_{2 B}^{2} / 15+$ $O\left(\alpha_{2 B}^{4}\right)$, the isotropic stress $\boldsymbol{\sigma}_{2}=4 \chi c_{B} \alpha_{2 B}^{2} \tilde{E}^{2} \mathbf{I} / 15 \beta$, recovers a local field-dependent pressure correction, which is recognized with the classical electrostrictive pressure. Similarly, the stress component,

$$
\begin{aligned}
\boldsymbol{\sigma}_{3}= & c_{B} \zeta_{B}^{r} \frac{\overline{\chi}}{4 \pi}\left[C_{1}(\hat{\mathbf{E}} \cdot \kappa \cdot \hat{\mathbf{E}}) \hat{\mathbf{E}} \hat{\mathbf{E}}\right. \\
& +C_{2}(\operatorname{Tr}(\kappa) \hat{\mathbf{E}} \hat{\mathbf{E}}+\hat{\mathbf{E}} \hat{\mathbf{E}} \cdot \kappa+(\kappa \cdot \hat{\mathbf{E}} \hat{\mathbf{E}})^{T}+\hat{\mathbf{E}} \cdot \kappa \hat{\mathbf{E}}+\kappa \cdot \hat{\mathbf{E}} \hat{\mathbf{E}} \\
& \left.+\hat{\mathbf{E}} \cdot \kappa \cdot \hat{\mathbf{E}} \mathbf{I})+C_{3}\left(\operatorname{Tr}(\kappa) \mathbf{I}+\kappa+(\kappa)^{T}\right)\right],
\end{aligned}
$$

Also, another integral $\mathbf{I}_{5}=\int d \hat{\mathbf{p}}_{B} f_{0} \hat{p}_{i} \hat{p}_{j} \hat{p}_{\mu} \hat{p}_{v}$ is useful for evaluating $8 \pi \boldsymbol{\sigma}_{3}=c_{B} \zeta_{B}^{r} \overline{\boldsymbol{\chi}}\left(\boldsymbol{\kappa}+\boldsymbol{\kappa}^{T}\right): \mathbf{I}_{5}$. Owing to the orientation probability about $\hat{\mathbf{E}}$, this integral can be expanded in fourth order moments $\boldsymbol{\Gamma}_{1}=\hat{\mathbf{E}}^{\otimes 4}, \boldsymbol{\Gamma}_{2}=$ $\hat{\mathbf{E}} \hat{\mathbf{E}} \otimes \mathbf{I}+\mathbf{I} \otimes \hat{\mathbf{E}} \hat{\mathbf{E}}+\mathcal{P}(\hat{\mathbf{E}} \otimes \mathbf{I} \otimes \hat{\mathbf{E}})$ and $\boldsymbol{\Gamma}_{3}=\mathbf{I} \otimes \mathbf{I}+\mathcal{P}(\mathbf{I} \otimes \mathbf{I})$ (where $\otimes$ and $\mathcal{P}$ represents tensor products, and indices permutations, respectively) as, $\mathbf{I}_{5}=\sum_{i} C_{i} \boldsymbol{\Gamma}_{i}$. The coefficients are identified using contraction of $\mathbf{I}_{5}$ with $\boldsymbol{\Gamma}_{i}$ as, $C_{i}=\frac{\pi}{2}\left(Q_{i}+\frac{U_{i}}{\left(\alpha_{2 B} \tilde{E}\right)^{2}}-\left(\frac{V_{i}}{\alpha_{2 B} \tilde{E}}+\frac{W_{i}}{\left(\alpha_{2 B} \tilde{E}\right)^{3}}\right) \mathcal{L}_{B}\right)$, with $(Q_{i}, U_{i}, V_{i}, W_{i})=(8,280,80,840),(0,-40,-8,-120)$, $(0,8,0,24)$ for $i=1,2,3$ respectively. The case of simple shear flow (say, having $\kappa_{y x}=\dot{\gamma}$, while other components are zero) perpendicular to the field $(\mathbf{E}=E \hat{\mathbf{x}})$ can be used to simplify the stress to $\boldsymbol{\sigma}_{3}=\dot{\gamma}\left(C_{2}+C_{3}\right)$, which is $\sigma_{y x}=c_{B} \zeta_{B}^{r} \bar{\chi} \dot{\gamma}\left(1+\alpha_{2 B}^{2} \tilde{E}^{2} / 21\right) / 15$ for $\alpha_{2 B} \ll 1$. Hence, this contributes to the field-dependent strain rate-based viscous shear stress.

Appendix C.-Jin et al. [1]'s experimental conditions include $T=298 \mathrm{~K}, c_{0}=0.08 \mathrm{mM}, E_{0}=\left(V_{1}-\right.$ $V_{2}) / L, V_{1}=-150 \mathrm{mV}, V_{2}=100 \mathrm{mV}, L=57.5 \pm 17.5 \mathrm{~nm}$, while using PB theory. Hence, $f_{v 0}=L_{E} L_{m} f_{v B}$, $f_{v B}=c_{B} \zeta_{r} \bar{\chi} \beta^{2} p_{0 B}^{2} / 315 \eta_{0}$ comes from the HB network segment, while $L_{E}=\left(E_{s} / E_{0}\right)^{2}$ and $L_{m}=$ $\left(\frac{\left(1-A_{1} E_{s}^{2}-A_{2} \psi_{s}^{2}\right) \epsilon_{D}\left(1-e^{-1 / \epsilon_{D}}\right)}{1-\left(A_{1} E_{s}^{2}-A_{2} \psi_{s}^{2}\right) \epsilon_{D}\left(1-e^{-1 / \epsilon_{D}}\right)}\right)$ are prefactors for the nominal field to surface field and surface value of to mean value conversions. Here $E_{s}\left(c_{0}, V_{0}, L\right)$ is the electric field at the electrode surface of constant potential, estimated iteratively, and $A_{i}$ are the coefficients from MLB model [28], $A_{1} A_{3}=2 c_{s 0} \alpha_{2}^{4} /\left(135 \varepsilon_{0} E^{2} \beta\right)$ and $A_{2} A_{3}=2 c_{0} \alpha_{2}^{2}\left(e_{0} \beta \psi\right)^{2} /\left(9 \varepsilon_{0} E^{2} \beta\right)$, with $A_{1}=$ $n^{2}+2 \alpha_{2}^{2} c_{s 0} /\left(9 \varepsilon_{0} \beta E^{2}\right)$. Similarly, electrostrictive pressure $\Pi_{e s}=L_{p} \Pi_{0, e s}$, with the traditional expression $\Pi_{0, e s}=c_{s 0}\left|\mathbf{p}_{e}\right|^{2} \beta E^{2} / 6$ and the HB network prefactor $L_{p}=\left(\frac{8}{5} \Theta_{B} \alpha_{1}^{2} n_{B}\right)\left(\frac{c_{s} \bar{P}_{0}^{2}}{c_{s 0}\left|\mathbf{p}_{e}\right|^{2}}\right).$