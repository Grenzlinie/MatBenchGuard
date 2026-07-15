
# Magnetic order and spin excitations in layered Heisenberg antiferromagnets with compass-model anisotropies

A.A. Vladimirov \( ^{a} \) , D. Ihle \( ^{b} \)  and N. M. Plakida \( ^{a} \) 

 \( ^{a} \)  Joint Institute for Nuclear Research, 141980 Dubna, Russia and

 \( ^{b} \)  Institut für Theoretische Physik, Universität Leipzig, D-04109, Leipzig, Germany
(Dated: June 21, 2021)

The spin-wave excitation spectrum, the magnetization, and the Néel temperature for the quasi-two-dimensional spin-1/2 antiferromagnetic Heisenberg model with compass-model interaction in the plane proposed for iridates are calculated in the random phase approximation. The spin-wave spectrum agrees well with data of Lanczos diagonalization. We find that the Néel temperature is enhanced by the compass-model interaction and is close to the experimental value for  \( Ba_{2}IrO_{4} \) .

PACS numbers: 74.72.-h, 75.10.-b, 75.40.Gb

Spin-orbital physics in transition-metal oxides has been extensively studied in recent years. A number of theoretical models was proposed to describe a complicated nature of phase transitions induced by competing spin and orbital interactions as originally was considered in Ref. [1]. Whereas the isotropic spin interaction can be treated within the conventional Heisenberg model, to study the orientation-dependent orbital interaction the compass model is commonly used. The latter reveals a large degeneracy of ground states resulting in a complicated phase diagram. In particular, quantum and thermodynamic phase transitions in the two-dimensional (2D) compass model were studied in Refs. [2–4], where a first-order transition was found for the symmetric compass model. A generalized 2D Compass-Heisenberg (CH) model was introduced in Ref. [5], where an important role of the spin Heisenberg interaction in lifting the high degeneracy of the ground state of the compass model was stressed. In Ref. [6] a phase diagram of the CH model and excitations within Lanczos exact diagonalization for finite clusters on a square lattice were considered in detail. In particular, spin-wave excitations and column-flip excitations in nanoclusters characteristic to the compass model were analyzed.

A strong relativistic spin-orbital coupling reveals a compass-model type interaction in 5d transition metals. In particular, it was shown in Ref. [7], that a strong spin-orbit coupling in such compounds as  \( Sr_{2}IrO_{4} \)  and  \( Ba_{2}IrO_4 \)  results in an effective antiferromagnetic (AF) Heisenberg model for the pseudospins 1/2 with the compass-model anisotropy. The model can be used to explain the AF long-range order (LRO) below the Néel temperature  \( T_{N} = 230 \)  K in  \( Sr_{2}IrO_{4} \)  and  \( T_{N} = 240 \)  K in  \( Ba_{2}IrO_{4} \)  (see, e.g., [8]). The spin-wave spectrum measured by magnetic resonance inelastic x-ray scattering (RIXS) in  \( Sr_{2}IrO_{4} \)  shows a dispersion similar to that one in the undoped cuprate  \( La_{2}CuO_{4} \)  [9].

In the present paper we calculate the spin-wave excitation spectrum and magnetization for a layered AF Heisenberg model with anisotropic compass-model interaction in the plane. To take into account the finite-temperature renormalization of the spectrum and to calculate the Néel temperature  \( T_{N} \) , we employ the equation of motion method for the Green functions (GFs) for spin S = 1/2 using the random phase approximation (RPA) [10]. The results are compared with experimental data for iridates and theoretical studies of the 2D CH model in Ref. [5] and in Refs. [11, 12].

We consider the layered Heisenberg AF with the compass-model interaction in the plane. The Hamiltonian of the model can be written as

 \[ H\;=\;\frac{1}{2}\sum_{i,j}\left\{J_{i j}\mathbf{S}_{i}\mathbf{S}_{j}+\Gamma_{i j}^{x}S_{i}^{x}S_{j}^{x}+\Gamma_{i j}^{y}S_{i}^{y}S_{j}^{y}\right\}. \quad (1) \] 

Here  \( J_{ij} = J(\delta_{r_j,r_i \pm a_x} + \delta_{r_j,r_{i} \pm a_y}) + J_z \delta_{r_j,r_i \pm c} \) , where J is the exchange interaction between the nearest neighbors (NN) in the plane with the lattice constants  \( a_x = a_y = a \) , and  \( J_z \)  is the coupling between the planes with the distance c. The compass model interaction is given by  \( \Gamma_{ij}^{x} = \Gamma_x \delta_{r_j,r_i \pm a_x} \) ,  \( \Gamma_{ij}^{y} = \Gamma_y \delta_{r_j,r_i \pm a_y} \) . The ab initio many-body quantum chemistry calculations give the following parameters for  \( Ba_2IrO_4 \) : J = 65 meV,  \( \Gamma_x = \Gamma_y = \Gamma = 3.4 \)  meV, and  \( J_z \gtrsim 3 - 5 \mu eV \)  [13]. To compare our results with the theoretical studies of the 2D CH model in Ref. [5], we consider also large anisotropic compass-model interactions,  \( \Gamma_x > \Gamma_y > J \) . In Refs. [11, 12] the spin-wave spectrum was calculated for a similar model (1) in the linear spin-wave theory (LSWT), where in addition to the isotropic exchange interaction  \( J_{ij} \)  between the NN in (1) the next-nearest neighbor (NNN) interaction was also taken into account. We consider this more general model in the Appendix.

We adopt a two-sublattice \((A,B)\) representation for the AF LRO below the Néel temperature. Then the Hamiltonian (1) with \(\Gamma_{x}=\Gamma_{y}>0\) is an easy-plane AF, where the direction of the AF order parameter (OP) – the magnetization of one sublattice in the \((x,y)\) plane – is degenerate. To lift the degeneracy, we assume anisotropic compass-model interactions \(\Gamma_{x}>\Gamma_{y}>0\). In this case the model (1) describes an easy-axis AF with the OP \(\langle S_{xC_{A}}^{x}\rangle=-\langle S_{yC_{B}}^{x}\rangle\) fixed along the \(x\) axis. We can consider also the limiting case, \(\Gamma_{x}=\Gamma_{y}\). The AF LRO can be described by the AF wave vector \(\mathbf{Q}=(\pi/a,\pi/a,\pi/c)\).

It is convenient to write the Hamiltonian (1) in terms
 

of the circular components  \( S_{i}^{\pm}=S_{i}^{y}\pm iS_{i}^{z} \)  in the form

 \[ \begin{align*}H~&=~\frac{1}{2}\sum_{\langle i,j\rangle}\left\{J_{ij}^{x}S_{i}^{x}S_{j}^{x}+J_{ij}^{y}\frac{1}{2}\left[S_{i}^{+}S_{j}^{-}+S_{i}^{-}S_{j}^{+}\right]\right.\\&\left.~+~\frac{1}{4}\Gamma_{ij}^{y}\left[S_{i}^{+}S_{j}^{+}+S_{i}^{-}S_{j}^{-}\right]\right\},\end{align*} \quad (2) \] 

where  \( J_{ij}^{x}=J_{ij}+\Gamma_{ij}^{x} \) ,  \( J_{ij}^{y}=J_{ij}+(1/2)\Gamma_{ij}^{y} \) .

To calculate the spin-wave spectrum of transverse spin excitations, we introduce the retarded two-time commutator GFs [14]:

 \[ \begin{align*}G_{nm}^{\alpha,\beta}(t-t^{\prime})~&=~-i\theta(t-t^{\prime})\langle[S_{n}^{\alpha}(t),S_{m}^{\beta}(t^{\prime})]\rangle\\~&=~\int_{-\infty}^{+\infty}\frac{d\omega}{2\pi}e^{-i\omega(t-t^{\prime})}\langle[S_{n}^{\alpha}|S_{m}^{\beta}\rangle_{\omega}],\end{align*} \quad (3) \] 

where  \( \alpha,\beta=(\pm) \) , and  \( \langle\ldots\rangle \)  is the statistical average. The indexes n,m run over N/2 lattice sites i (j) in the sublattice A (B).

There are four types of the GFs due to the two-sublattice representation for normal and anomalous GFs which can be written as  \( 4 \times 4 \)  matrix GF

 \[ \hat{G}(\omega)=\langle\left(\begin{array}{c}S_{i}^{+}\\ S_{i}^{-}\\ S_{j}^{+}\\ S_{j}^{-}\end{array}\right)\mid\left(S_{i}^{x}S_{i}^{y}S_{j}^{+}S_{j}^{-}\right)\rangle_{\omega}. \quad (4) \] 

Here the lattice sites \(i, i'\) refer to the sublattice \(A\) while the lattice sites \(j, j'\) refer to the sublattice \(B\).

Using equations of motion for spin operators,  \( i(d/dt)S_{i}^{\pm}(t)=[S_{i}^{\pm},H]=\mp\sum_{n}J_{in}^{x}S_{i}^{\pm}S_{n}^{\pm}\pm\sum_{n}[J_{in}^{y}S_{i}^{x}S_{n}^{\pm}+(1/2)\Gamma_{in}^{y}S_{i}^{x}S_{n}^{\mp}] \) , we obtain a system of equations for the matrix components of the GF (4). In particular,

 \[ \begin{align*}&\omega\langle\langle S_{i}^{+}|S_{i}^{-}\rangle\rangle_{\omega}=2\langle S_{i}^{x}\rangle\delta_{i,i^{\prime}}-\sum_{n}J_{in}^{x}\langle\langle S_{i}^{+}S_{n}^{x}|S_{i}^{-}\rangle\rangle_{\omega}\\&+\sum_{n}[J_{in}^{y}\langle\langle S_{i}^{x}S_{n}^{+}|S_{i}^{-}\rangle\rangle_{\omega}+(1/2)\Gamma_{in}^{y}\langle\langle S_{i}^{x}S_{n}^{-}|S_{i}^{-}\rangle\rangle_{\omega}],\\&\omega\langle\langle S_{j}^{-}|S_{j}^{+}\rangle\rangle_{\omega}=-2\langle S_{j}^{x}\rangle\delta_{j,j^{\prime}}+\sum_{m}J_{jm}^{x}\langle\langle S_{j}^{-}S_{m}^{+}|S_{j}^{+}\rangle\rangle_{\omega}\\&-\sum_{m}[J_{jm}^{y}\langle\langle S_{j}^{x}S_{m}^{-}|S_{j^{+}}^{\prime}\rangle\rangle_{\omega}+(1/2)\Gamma_{jm}^{y}\langle\langle S_{j}^{x}S_{m}^{+}|S_{j^{+}}^{\prime}\rangle\rangle_{\omega}].\end{align*} \] 

In the RPA [10] for all GFs the following approximation is used for the lattice sites  \( n \neq i \) ,  \( m \neq j \) , as e.g.,

 \[ \begin{align*}\langle\langle S_{i}^{x}S_{n}^{\alpha}|S_{i^{\prime}}^{\beta}\rangle\rangle_{\omega}&=\langle S_{i}^{x}\rangle\langle\langle S_{n}^{\alpha}|S_{i^{\prime}}^{\beta}\rangle\rangle_{\omega}=\sigma\langle\langle S_{n}^{\alpha}|S_{i^{\prime}}^{\beta}\rangle\rangle_{\omega},\\\langle\langle S_{n}^{x}S_{i}^{\alpha}|S_{i^{\prime}}^{\beta}\rangle\rangle_{\omega}&=\langle S_{n}^{x}\rangle\langle\langle S_{i}^{\alpha}|S_{i^{\prime}}^{\beta}\rangle\rangle_{\omega}=-\sigma\langle\langle S_{i}^{\alpha}|S_{i^{\prime}}^{\beta}\rangle\rangle_{\omega},\end{align*} \quad (5) \] 

where  \( \langle S_{i}^{x}\rangle = \sigma \)  for  \( i \in A \)  while  \( \langle S_{n}^{x}\rangle = -\sigma \)  for  \( n \in B \) . A similar approximation is used for the B sublattice, where  \( \langle S_{j}^{x}\rangle = -\sigma \)  for  \( j \in B \)  while  \( \langle S_{m}^{x}\rangle = \sigma \)  for  \( m \in A \) . The RPA results in a closed system of equations for the components of the matrix GF (4).
To solve the obtained system of equations we introduce the Fourier representation of spin operators for N/2 lattice sites in two sublattices,  \( S_{i}^{\pm} = \sqrt{2/N}\sum_{q} S_{q}^{\pm} \exp(\pm i\mathbf{q}\mathbf{r}_{i}) \)  and  \( S_{j}^{\pm} = \sqrt{2/N}\sum_{q'} S_{q'}^{\pm} \exp(\pm i\mathbf{q'}\mathbf{r}_{j}) \) , where  \( q \)  and  \( q' \)  run over  \( (N/2) \)  wave vectors in the reduced BZ of each sublattice. Using this transformation the equation for the Fourier representation of the matrix GF (4) can be written in the from

 \[ \hat{G}(\mathbf{q},\omega)=\{\omega\hat{I}-\hat{V}(\mathbf{q})\}^{-1}\times2\sigma\hat{I}_{1}, \quad (6) \] 

where  \( \hat{I} \)  is the unity matrix,  \( \hat{I}_{1} \)  is a diagonal matrix with the elements  \( d_{11} = d_{33} = 1 \)  and  \( d_{22} = d_{44} = -1 \) , and the interaction matrix is given by

 \[ \hat{V}(\mathbf{q})=\begin{pmatrix}A&0&B(\mathbf{q})&C(\mathbf{q})\\ 0&-A&-C(\mathbf{q})&-B(\mathbf{q})\\ B(\mathbf{q})&C(\mathbf{q})&A&0\\ -C(\mathbf{q})&-B(\mathbf{q})&0&-A\end{pmatrix}. \quad (7) \] 

Here the interaction parameters are:

 \[ \begin{aligned}A&=\sigma J^{x}(0)=\sigma[J(0)+2\Gamma_{x}],\\J(\mathbf{q})&=2J\left(\cos q_{x}+\cos q_{y}\right)+2J_{z}\cos q_{z},\\B(\mathbf{q})&=\sigma\Gamma_{y}\cos q_{y},\quad C(\mathbf{q})=\sigma\left[J(\mathbf{q})+\Gamma_{y}\cos q_{y}\right].\end{aligned} \quad (8) \] 

The spectrum of spin waves is determined from the equation

 \[ \mathrm{D e t}|\omega\hat{I}-\hat{V}(\mathbf{q})|=0. \quad (9) \] 

After some algebra we obtain the biquadratic equation for the frequency \(\omega\) of spin-wave excitations:

 \[ \begin{aligned}&\omega^{4}-2\omega^{2}[A^{2}+B^{2}(\mathbf{q})-C^{2}(\mathbf{q})]+[B^{2}(\mathbf{q})-C^{2}(\mathbf{q})]^{2}\\&-2A^{2}[C^{2}(\mathbf{q})+B^{2}(\mathbf{q})]+A^{4}=0.\\ \end{aligned} \] 

The solution of this equation reads

 \[ \begin{aligned}\omega_{\nu}(\mathbf{q})~&=~\pm\{A^{2}+B^{2}(\mathbf{q})-C^{2}(\mathbf{q})+2\nu A B(\mathbf{q})\}^{1/2}\\&\equiv~\pm\sigma\varepsilon_{\nu}(\mathbf{q}),\end{aligned} \quad (10) \] 

where \(\nu=\pm1\). The energy of excitations for “acoustic” \(\varepsilon_{-}(\mathbf{q})\) and “optic” \(\varepsilon_{+}(\mathbf{q})\) modes are

 \[ \begin{align*}\varepsilon_{-}(\mathbf{q})~&=~\Big\{J^{2}(0)-J^{2}(\mathbf{q})+4\Gamma_{x}[J(0)+\Gamma_{x}]-\Big.\\&\quad-2\Gamma_{y}\left[J(0)+J(\mathbf{q})+2\Gamma_{x}\right]\cos q_{y}\Big\}^{1/2},\\ \varepsilon_{+}(\mathbf{q})~&=~\Big\{J^{2}(0)-J^{2}(\mathbf{q})+4\Gamma_{x}[J(0)+\Gamma_{x}]+\Big.\\&\quad+2\Gamma_{y}[J(0)-J(\mathbf{q})+2\Gamma_{x}]\left.\cos q_{y}\right\}^{1/2}.\end{align*} \quad (11) \] 

These two branches are coupled by the relation \(\varepsilon_{-}(\mathbf{q}+\mathbf{Q})=\varepsilon_{+}(\mathbf{q})\) for the AF wave vector \(\mathbf{Q}\).

For the symmetric compass-model interaction, \(\Gamma_{x} = \Gamma_{y} = \Gamma\), for \(\mathbf{q} = 0\) we have the gapless acoustic mode while the optic mode has a gap:

 \[ \varepsilon_{-}(0)=0,\quad\varepsilon_{+}(0)=2\sqrt{\Gamma J(0)+2\Gamma^{2}}>0. \quad (13) \]
 

For the wave vector \(\mathbf{q} = \mathbf{Q}\) we have the opposite results: \(\varepsilon_{-}(\mathbf{Q}) = \varepsilon_{+}(0) > 0\), \(\varepsilon_{+}(\mathbf{Q}) = \varepsilon_{-}(0) = 0\). In the anisotropic case \(\Gamma_{x} > \Gamma_{y}\) the spectrum of excitations has gaps both at \(\mathbf{q} = 0\) and \(\mathbf{q} = \mathbf{Q}\):

 \[ \varepsilon_{-}(0)=\varepsilon_{+}(\mathbf{Q})=2\sqrt{(\Gamma_{x}-\Gamma_{y})\left(J(0)+\Gamma_{x}\right)}. \quad (14) \] 

For a conventional AF Heisenberg model with \(\Gamma_{x} = \Gamma_{y} = 0\) we have only one branch with the dispersion \(\varepsilon_{-}(\mathbf{q}) = \varepsilon_{+}(\mathbf{q}) = {\sqrt{J^{2}(0) - J^{2}(\mathbf{q})}}\) which is gapless both at \(\mathbf{q} = 0\) and \(\mathbf{q} = \mathbf{Q}\).

A similar equation of motion method for the matrix GF (4) can be employed in the LSWT using the transformation \(S_{i}^{+} = \sqrt{2S} a_{i}\), \(S_{i}^{-} = \sqrt{2S} a_{i}^{\dagger}\), \(S_{i}^{x} = S - a_{i}^{\dagger} a_{i}\) for the sublattice \(A\) and the similar transformation for the sublattice \(B\) (\(a_{i} \to b_{i}^{\dagger}\)). Then keeping only linear terms in the bose-like operators \((a_{i}, a_{i}^{\dagger})\) and \((b_{i}, b_{i}^{\dagger})\) we obtain Eqs. (10), (11), (12) for the spin-wave spectrum in LSWT with the sublattice magnetization \(\sigma\) substituted by spin \(S\). The same spectrum in LSWT was obtained in Refs. [5, 6]. Note that in the RPA the energy of spin excitations \(\omega_{\pm}(\mathbf{q})\), Eq. (10), is reduced in comparison with the LSWT since \(\sigma < S\) even at zero temperature due to zero-point fluctuations in the AF state. The spectrum (10) for the symmetric compass model, \(\Gamma_{x} = \Gamma_{y}\), is similar to the spectrum of the anisotropic AF Heisenberg model considered in Ref. [15] and Refs. [11, 12].

In Figure 1 the spectrum of spin waves  \( \omega_{\pm}(\mathbf{q}) \)  in the plane in RPA for the parameters J = 65 meV,  \( \Gamma = 3.4 \)  meV found for  \( Ba_{2}IrO_{4} \)  [13] is shown at T = 0. The spectrum  \( \omega_{-}(\mathbf{q}) \)  shows a gap at the wave vector Q given by  \( \omega_{-}(\mathbf{Q}) = 2\sigma\sqrt{\Gamma J(0) + 2\Gamma^{2}} \approx 1.48 J\sqrt{\Gamma J} \approx 22 \)  meV for  \( \sigma = 0.37 \) . This value is comparable with the maximum energy of excitations  \( \omega_{\pm}^{\text{max}}(\mathbf{Q}/2) = 4\sigma J\sqrt{1 + \Gamma J} \approx 1.5 J \)  that gives  \( \omega_{-}(\mathbf{Q})/\omega_{\pm}^{\text{max}}(\mathbf{Q}/2) \approx 0.22 \) . We can suggest that the spin-wave spectrum in  \( Ba_{2}IrO_{4} \)  should be similar to that one measured by RIXS in  \( Sr_{2}IrO_{4} \)  [9]. The latter was fitted by a one-branch phenomenological  \( J - J' - J'' \)  model with J = 60 meV,  \( J' = -20 \)  meV, and  \( J'' = 15 \)  meV. The spectrum does not reveal a gap in the acoustic branch  \( \omega_{-}(\mathbf{q}) \)  at Q as for  \( Ba_{2}IrO_{4} \) . However, since the intensity of scattering on magnons is proportional to  \( 1/\omega(\mathbf{q}) \) , strong scattering on the gapless branch  \( \omega_{+}(\mathbf{q}) \to 0 \)  for  \( q \to Q \)  completely suppresses scattering on the gapped  \( \omega_{-}(\mathbf{q}) \)  branch. To distinguish scattering on the two branches, high-resolution studies are necessary. A possibility of observation of a two-peak structure in the RIXS experiments caused by the two-branch spectrum of spin waves is discussed in Refs. [12, 16, 17]. For the model (1) with the exchange interaction  \( J_{ij} \)  only between nearest neighbors the energy of excitations at  \( \mathbf{q}_{1} = (\pi/2, \pi/2) \) ,  \( \omega_{-}(\mathbf{q}_{1}) = \omega_{+}(\mathbf{q}_{1} \) , is nearly equal to  \( \omega_{\pm}(\mathbf{q} = \pi, 0) \)  (up to  \( \pm\Gamma/J \) ), while in the RIXS experiment  \( \omega(\mathbf{q}_{1}) \approx (1/2)\omega(\mathbf{q} = \pi, 0) \)  was found. By taking into account the exchange interactions also between the NNN in the plane the spectrum can be fitted to the experimentally observed one as discussed in the Appendix.

![](./images/867749295023980814_1.jpg)

FIG. 1: Spectrum of spin-wave excitations \(\omega_{-}(\mathbf{q})\) (bold line) and \(\omega_{+}(\mathbf{q})\) (dashed line) along the symmetry directions in the BZ for the symmetric compass model with \(\Gamma_{x} = \Gamma_{y} = \Gamma = 0.052 J\) and \(J_{z} = 0\).

![](./images/867749295023980814_2.jpg)

FIG. 2: Spectrum of spin-wave excitations \(\omega_{-}(\mathbf{q})\) (bold line) and \(\omega_{+}(\mathbf{q})\) (dashed line) along the symmetry directions in the BZ for the anisotropic compass model with \(\Gamma_{x}=8.9J\), \(\Gamma_{y}=4.5J\), \(J_{z}=0\). Circles are numerical results from Ref. [5].

Figure 2 shows the spin-wave dispersion for large anisotropic interaction, \(\Gamma_{x} = 8.9 J\), \(\Gamma_{y} = 4.5 J\) used in Ref. [5] in numerical calculations with Lanczos exact diagonalization. Our RPA calculations give a similar formula for the spectrum as in LSWT except for the prefactor \(\sigma = 0.44\) instead of \(S = 1/2\) in LSWT. The dispersion curves are in good agreement with numerical ones shown by circles which were multiplied by the factor \(10/4\), since in Ref. [5], instead of spin \(1/2\) operators, the Pauli matrices are used so that the exchange integral \(I\) corresponds to our \((1/4) J\) in Eq. (1), and in Fig. (4) of Ref. [5] the energy unit is \(J_{c} = 10 I\). The spectrum reveals a large gap at all wave vectors caused by the large value of \(\Gamma_{x}\) and a noticeable dispersion only along the \(\Gamma(0, 0) \to Y(0, \pi)\) direction due to a large, in comparison with \(J\), interaction \(Y_{y} = 4.5 J\).

To calculate the sublattice magnetization \(\sigma = \langle S_{i}^{x} \rangle\) in RPA, we use the kinematic relation \(S_{i}^{x} = (1/2) - S_{i}^{-} S_{i}^{+}\) for spin \(S = 1/2\) which results in the self-consistent equa-
 

tion

 \[ \sigma=\frac{1}{2}-\frac{1}{N/2}\sum_{\mathbf{q}}\left\langle S_{\mathbf{q}}^{-}S_{\mathbf{q}}^{+}\right\rangle. \quad (15) \] 

The spin correlation function  \( \langle S_{\mathbf{q}}^{-}S_{\mathbf{q}}^{+}\rangle \)  can be calculated from the GF  \( \langle S_{\mathbf{q}}^{+}|S_{\mathbf{q}}^{-}\rangle_{\omega} \)  which follows from the GF (6):

 \[ \langle S_{\mathbf{q}}^{+}|S_{\mathbf{q}}^{-}\rangle_{\omega}=2\sigma\frac{a_{\mathbf{q}}(\omega)}{[\omega^{2}-\omega_{z}^{2}(\mathbf{q})][\omega^{2}-\omega_{+}^{2}(\mathbf{q)}]}, \quad (16) \] 

 \[ \begin{align*}a_{\mathbf{q}}(\omega)&=\omega^{3}+A\omega^{2}-[A^{2}+B^{2}(\mathbf{q})-C^{2}(\mathbf{q})]\omega-\\&-A^{3}+A[B^{2}(\mathbf{q})+C^{2}(\mathbf{q})].\end{align*} \] 

Using the spectral representation for GFs, for the correlation function we obtain

 \[ \langle S_{\mathbf{q}}^{-}S_{\mathbf{q}}^{+}\rangle=2\sigma\sum_{\mu,\nu=\pm1}I_{\mu\nu}(\mathbf{q})N(\mu\omega_{\nu}(\mathbf{q})), \quad (17) \] 

where  \( N(\omega) = [\exp(\omega/T) - 1]^{-1} \) , and the contribution from the four poles of the GF (16) is given by

 \[ I_{\mu\nu}(\mathbf{q})=\frac{a_{\mathbf{q}}(\mu\omega_{\nu}(\mathbf{q}))}{8\mu\nu\omega_{\nu}(\mathbf{\mathbf{q}})A B(\mathbf{\mathbf{q}})}. \quad (18) \] 

Note that  \( I_{\mu\nu}(\mathbf{q}) \)  does not depend on  \( \sigma \) .

Using relation (17) we perform the self-consistent solution of Eq. (15) for the magnetization  \( \sigma \) . Figure 3 shows

![](./images/867749295023980814_3.jpg)

FIG. 3: Sublattice magnetization \(\sigma = \langle S_{y}^{z} \rangle\) for the parameters \(J_{x} = 5 \cdot 10^{-5} J\), \(\Gamma_{xy} = 0.052 J\) for \(\Gamma_{y}/\Gamma_{x} = 1\) (solid line), 0.95 (dashed line), 0.5 (dotted), and for \(\Gamma_{y}/\Gamma_{x} \leqslant 0.1\) (dash-dotted).

the sublattice magnetization for  \( J_{z} = 5 \cdot 10^{-5} J \) ,  \( \Gamma_{x} = 0.052 J \)  for various  \( \Gamma_{y}/\Gamma_{x} \) . For the symmetric compass model,  \( \Gamma_{x} = \Gamma_{y} = 0.052 J \) , the Néel temperature  \( T_{N} = 0.365 J = 275 K \)  is close to  \( T_{N} = 240 K \)  observed in experiment for  \( Ba_{2}IrO_{4} \) . We stress that the anisotropy of the compass-model interaction,  \( \Gamma_{y}/\Gamma_{x} < 1 \) , enhances  \( T_{N} \) .

To study the  \( T_{N} \)  dependence on the parameters of the model, we consider Eq. (15) in the limit  \( \sigma \rightarrow 0 \) . In this limit  \( N(\omega_{\nu}) \approx (T/\sigma\varepsilon_{\nu}) \) , and for the Néel temperature we have the equation:

 \[ \frac{1}{2}=\frac{1}{N/2}\sum_{\mathbf{q}}\sum_{\mu,\nu=\pm1}I_{\mu\nu}(\mathbf{q})\frac{2T_{N}}{\mu\varepsilon_{\nu}(\mathbf{q})}. \quad (19) \] 

![](./images/867749295023980814_4.jpg)

FIG. 4: Néel temperature  \( T_{N} \)  as a function of  \( J_{z} \)  with  \( \Gamma_{x} = \Gamma_{y} = 0.052 J \)  (solid line) and  \( \Gamma_{x} = \Gamma_{y} = 0 \)  (dashed line).

Therefore,

 \[ T_{N}=\frac{1}{4C},\quad C=\frac{1}{N/2}\sum_{\mathbf{q}}\sum_{\mu,\nu}\frac{I_{\mu\nu}(\mathbf{q})}{\mu\varepsilon_{\nu}(\mathbf{q})}. \quad (20) \] 

Let us study in which cases the integral over q in (20) has a finite value that results in a finite  \( T_{N} \) .

At first we consider the symmetric compass model,  \( \Gamma_{x} = \Gamma_{y} = \Gamma \) . In this case  \( \varepsilon_{-}(\mathbf{q}) = 0 \)  at q = 0 and  \( \varepsilon_{+}(\mathbf{q}) = 0 \)  at q = Q. Since these two branches are symmetric, we can consider only the divergency of the integral in (20) at q = 0 for  \( \varepsilon_{-}(\mathbf{q}) \)  given around q = 0 by

 \[ \begin{align*}\varepsilon_{-}^{2}(\mathbf{q})~&=~2(J(0)+\Gamma)\{J q_{x}^{2}\\&~+~[J+\Gamma^{2}/(J(0)+\Gamma)]q_{y}^{2}+J_{z}q_{z}^{2}\}.\end{align*} \quad (21) \] 

The integral in (20) diverges as \(\int d^{3}\mathbf{q}/\varepsilon_{-}^{2}(\mathbf{q})\) if any coefficient before \(q_{x}\), \(q_{y}\) or \(q_{z}\) in (21) is zero. In particular, for nonzero \(J(0)\) there is no LRO at finite \(T\) for \(J_{z}=0\).

In the limiting case  \( \Gamma \rightarrow 0 \)  we have  \( \lim_{J \to 0} J(\mathbf{q}) = (A + \mu\omega_{\mathbf{q}})/(4\mu\omega_{\mathbf{q}}) \)  with  \( \omega_{\mathbf{q}} = \sqrt{A^{2} - C^{2}(\mathbf{q})} \) . From Eq. (20) we get the conventional formula for  \( T_{N} \)  of the AF Heisenberg model (c.f. Ref. [18]) :

 \[ T_{N}(\Gamma=0)=\left\{\frac{8J(0)}{N}\sum_{\mathbf{q}}\frac{1}{J(0)^{2}-J^{2}(\mathbf{q})}\right\}^{-1}. \quad (22) \] 

Thus, for a symmetric 2D compass model we have no LRO at finite T. To obtain LRO, we must have finite values of both J and  \( J_{z} \) . The Néel temperature  \( T_{N} \)  as a function of the interplane coupling  \( J_{z} \)  is shown in fig. 4 for the interaction  \( \Gamma_{x} = \Gamma_{y} = 0.052 J \)  and for  \( \Gamma_{x} = \Gamma_{y} = 0 \) . We can conclude that the compass-model interaction enhances the Néel temperature and, in particular, the anisotropy of the compass-model interaction results in a further increase of  \( T_{N} \)  as shown in Fig. 3. In the anisotropic case  \( \Gamma_{x} > \Gamma_{y} \)  the spectrum of excitations has a gap at q = 0, Eq. (14), and therefore neither branch of this spectrum ever reaches zero, so that we have a finite  \( T_{N} \)  even for  \( J_{z} = 0 \) . Figure 5 demonstrates
 
![](./images/867749295023980814_5.jpg)

FIG. 5: Néel temperature  \( T_{N} \)  as a function of  \( \Gamma_{x} \)  for  \( J_{z}=0 \) ,  \( \Gamma_{y}=0.1\Gamma_{x} \)  (solid line) and  \( \Gamma_{y}=0.9\Gamma_{x} \)  (dashed line). In the inset the  \( 1/T_{N} \)  dependence is shown in the logarithmic scale for small  \( \Gamma_{x} \) .

the dependence of  \( T_{N} \)  on  \( \Gamma_{x} \)  for  \( J_{z}=0 \) ,  \( \Gamma_{y}=0.1\Gamma_{x} \)  and  \( \Gamma_{y}=0.9\Gamma_{x} \) . For  \( \Gamma_{x}\to0 \)  the Néel temperature goes to zero as shown in the inset.

To summarize, we have studied the spin-wave spectrum for the Heisenberg model with anisotropic compass-model interaction within the RPA. The spectrum has gaps at q = 0 or at the AF wave vector Q for nonzero compass-model interactions. The calculation of the Néel temperature  \( T_{N} \)  shows that for the symmetric compass-model interaction,  \( \Gamma_{x} = \Gamma_{y} \) , and a nonzero exchange interaction J, the AF LRO at finite T can exist only for a finite coupling  \( J_{z} \)  between the planes. For the anisotropic compass-model interaction,  \( \Gamma_{x} > \Gamma_{y} \) , and a finite exchange interaction J in the plane, the AF LRO with finite Néel temperature emerges even in the 2D case as observed in finite cluster calculations [5, 6]. In any case,  \( T_{N} \)  is enhanced by the compass-model interaction.

The authors would like to thank G. Jackeli, A. M. Oles, J. Richter, Yu. G. Rudoy, and V. Yushankhai for valuable discussions. We thank T. Nagao who drew our attention to Refs. [11, 12, 16, 17] for comments on the first version of our paper [19]. A financial support by the Heisenberg-Landau Program of JINR is acknowledged.

## Appendix A: Further distant neighbors

To fit the spin-excitation spectrum observed by RIXS in  \( Sr_{2}IrO_{4} \)  in Ref. [9] we consider a more general exchange interaction which includes the NNN interaction  \( J_{ij}^{nn} = J_{ij}^{\prime} + J_{ij}^{\prime\prime} \) , where  \( J_{ij}^{\prime} = J^{\prime}[\delta_{r_{j},r_{i} \pm (a_{x} + a_{y})} + \delta_{r_{j},r_{i} \pm (a_{x} - a_{y})}] \)  and  \( J_{ij}^{\prime\prime} = J^{\prime\prime}(\delta_{r_{j},r_{i} \pm 2a_{x}} + \delta_{r_{j},r_{i} \pm 2a_{y}}) \) . Note that in the two-sublattice model for the Hamiltonian (1) the in-plane exchange interaction  \( J_{ij} \)  acts between the NN on the two sublattices, while for the NNN exchange interaction  \( J_{ij}^{nn} \)  the lattice sites i and j refer to the same sublattice. Therefore, in the equation for the GF (6) the exchange interaction  \( J_{ij}^{nn} \)  gives a contribution only for the diagonal terms in the interaction matrix (7). This results in the transformation of the parameter  \( A = \sigma J^{x}(0) \)  to the function  \( A(\mathbf{q}) = \sigma [J^{x}(0) - J^{nn}(0) + J^{nn}(\mathbf{q})] \) , where  \( J^{nn}(\mathbf{\mathbf{q}}) = 4J^{\prime} \cos q_{x} \cos q_{y} + 2J^{\prime\prime}(\cos 2q_{x} + \cos 2q_{y}) \) . The solution of Eq. (9) yields the same spectrum of spin excitations (10) with the parameter A substituted by  \( A(\mathbf{q}) \) . The energy of excitations for “acoustic”  \( \varepsilon_{-}(\mathbf{q}) \)  and “optic”  \( \varepsilon_{+}(\mathbf{q}) \)   \( \varepsilon_{+}(\theta) \)  modes is given by Eqs. (11) and (12), where instead of  \( J(0) \)  we have to use the function  \( [J(0) - J^{nn}(0) + J^{nn}(\mathbf{q})] \) . If we take  \( \Gamma_{x} = \Gamma_{y} = 0 \) , the spectrum of spin waves transforms to  \( \varepsilon(\mathbf{q}) = \{[J(0) - J^{nn}(0) + J^{nn}(\mathbf{q})]^{2} - J^{2}(\mathbf{q})\}^{1/2} \)  which is gapless both at  \( \mathbf{q} = 0 \)  and  \( \mathbf{q}=(\pi, \pi) \) .

![](./images/867749295023980814_6.jpg)

FIG. 6: Spectrum of spin-wave excitations  \( \omega_{-}(\mathbf{q}) \)  (bold line) and  \( \omega_{+}(\mathbf{q}) \)  (dashed line) along the symmetry directions in the BZ for the model with  \( \Gamma_{x} = \Gamma_{y} = \Gamma = 0.052 J \) ,  \( J_{z} = 0 \) , and NNN interactions  \( J' = -(1/3)J \) ,  \( J'' = (1/4)J \) .

Taking into account the  \( J^{nn}(\mathbf{q}) \)  term with  \( J' = -(1/3)J \)  and  \( J'' = (1/4)J \)  as suggested in experiment [9] and in Refs. [11, 12] we obtain the spin-wave spectrum in RPA shown in Fig. 6. In comparison with Fig. 1 on the excitation energy  \( \omega(\pi/2, \pi/2) \approx (1/2)\omega(\pi, 0) \) , as observed in the RIXS experiment and in the LSWT in Refs. [11, 12]. The maximum energy of excitation  \( \omega(\pi, 0) = 2.5J \)  is larger than in Fig. 1, where  \( \omega(\pi, 0) \approx 1.6J \) , but it is still smaller than the experimental value of 200 meV [9] due to the renormalization of the spin-excitation energy in RPA given by the reduced magnetization  \( \sigma = 0.36 \)  in comparison with  \( \sigma = S = 1/2 \)  in the LSWT. Large values of  \( J' = -(1/3)J \)  and  \( J'' = (1/4)J \)  in comparison with  \( J' \approx -0.1J \)  found in  \( La_{2}CuO_{4} \)  [20] may be explained by a mixing of the  \( j_{eff} = 1/2 \)  states with higher energy  \( j_{eff} = 3/2 \)  states as suggested in Refs. [16, 17], where an itinerant-electron multi-orbital model was considered.

The NNN interaction also results in the lowering of the Néel temperature,  \( T_{N} = 0.3J = 220 K \)  (for J = 65 meV), in comparison with  \( T_{N} = 0.365J = 275 K \)  found for  \( J_{ij}^{nn} = 0 \)  and is close to  \( T_{N} = 240 K \)  observed in experiment for  \( Ba_{2}IrO_{4} \) .
 

[1] K. Kugel and D. Khomskii, Uspekhi Fiz. Nauk 136, 621 (1982) [translated in Sov. Phys. Usp. 25, 231 (1982)].

[2] R. Orús, A. C. Doherty, and G. Vidal, Phys. Rev. Lett. 102, 077203 (2009).

[3] S. Wenzel and W. Janke, Phys. Rev. B 78, 064402 (2008).

[4] S. Wenzel, W. Janke, and A. M. Läuchli, Phys. Rev. E 78, 066702(2010).

[5] F. Trousselet, A. M. Oleś, and P. Horsch, Europhys. Lett. 91, 40005 (2010),

[6] F. Trousselet, A. M. Oleś, and P. Horsch, Phys. Rev. B 86, 134412 (2012).

[7] G. Jackeli and G. Khaliullin, Phys. Rev. Lett. 102, 017205 (2009).

[8] S. Boseggia, R. Springell, H. C. Walker, H. M. Rønnow, Ch. Rüegg, H. Okabe, M. Isobe, R. S. Perry, S. P. Collins, and D. F. McMorrow, Phys. Rev. Lett. 110, 117207 (2013).

[9] J. Kim, D. Casa, M. H. Upton, T. Gog, Y.-J. Kim, J. F. Mitchell, M. van Veenendaal, M. Daghofer, J. van den Brink, G. Khaliullin, and B. J. Kim, Phys. Rev. Lett. 108, 177003 (2012).

[10] S. V. Tyablikov, Methods in the Quantum Theory of Magnetism, Plenum, New York, 1967 (2-nd Edition:

“Nauka”, Moscow, 1975).

[11] J. I. Igarashi and T. Nagao, Phys. Rev. B 88, 104406 (2013).

[12] J. I. Igarashi and T. Nagao, Phys. Rev. B 89, 064410 (2014).

[13] V. M. Katukuri, V. Yushankhai, L. Siurakshina, J. van den Brink, L. Hozoi, and I. Rousochatzakis, Phys. Rev. X 4, 021051 (2014).

[14] D. N. Zubarev, Usp. Phys. Nauk, 71, 71 (1960) [translated in Sov. Phys. Usp. 3, 320 (1960)].

[15] V. I. Lymar' and Yu. G. Rudoy, Theor. Math. Phys. 21, 86 (1974).

[16] J. I. Igarashi and T. Nagao, J. Phys. Soc. Jpn. B 83, 053709 (2014).

[17] J. I. Igarashi and T. Nagao, Phys. Rev. B 90, 064402 (2014).

[18] A. A. Vladimirov, D. Ihle, and N. M. Plakida, Theor. Math. Phys. 177, 1540 (2013).

[19] A. A. Vladimirov, D. Ihle, and N. M. Plakida, JETP Letters 100, 780 (2014).

[20] R. Coldea, S.M. Hayden, G.Aeppli, T.G. Perring, C.D Frost, T.E. Mason, S.-W. Cheong, Z. Fisk, Phys. Rev. Lett. 86, 5377 (2001).
 
