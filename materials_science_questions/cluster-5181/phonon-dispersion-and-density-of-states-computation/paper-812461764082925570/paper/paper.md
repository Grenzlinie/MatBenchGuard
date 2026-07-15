Non-local dielectric screening and electric fields associated with optical vibrations in superlattices

This content has been downloaded from IOPscience. Please scroll down to see the full text.

1999 J. Phys.: Condens. Matter 11 2153

(http://iopscience.iop.org/0953-8984/11/9/012)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 132.203.227.63
This content was downloaded on 26/06/2014 at 09:51

Please note that terms and conditions apply.

# Non-local dielectric screening and electric fields associated with optical vibrations in superlattices

V G Tyuterev†

Siberian Physical and Technical Institute, 634050, Novo-Sobornaya Square 1, Tomsk, Russia

Received 15 June 1998, in final form 7 January 1999

**Abstract.** We develop a simple and straightforward technique for extracting information about the electrostatic fields created by optical phonons in superstructures directly from microscopic three-dimensional lattice dynamics calculations. Local fields with a mesoscopic scale of variation associated with long-wavelength phonons in (GaAs)ₙ(AlAs)ₘ [001] superlattices are derived using an 11-parameter rigid-ion force-field model. The classification of local fields, their connection to and distinctions from those obtained from the conventional dielectric continuum approaches is discussed.

We also develop an alternative approach based on spatially dependent non-local microscopic dielectric screening in semiconducting superstructures. The analytical properties of long-wavelength phonon frequencies and associated electric fields find an explanation in terms of an eigenvalue problem for the non-local frequency-dependent microscopic dielectric matrix. Rigorous expressions for eigenfields and eigenpotentials are derived in the exactly solvable model of the dispersionless continuum. A simple and practical approximation with a short-range (elastic) dispersion included shows an excellent agreement with lattice dynamical calculations for (GaAs)ₙ(AlAs)ₘ [001].

## 1. Introduction
The investigation of polar optical vibrations in semiconductor layered structures has been attracting considerable attention in the last decade because they are important as a source of a strong electron-phonon interaction [1–6]. A lot of effort was devoted to the elaboration of a tractable macroscopic model of polar optical phonons. The early continuum theories based on the alternative electrodynamical [7–10] and mechanical [11] approaches did not correlate with each other and were at variance with microscopic lattice dynamics calculations [12–16], and so gave rise to discussion. The subsequent analysis using simplified lattice dynamical models [17–20] and the detailed investigation of the general mathematical properties of continuum solutions [19,21–23] revealed the essence of the problem as an incompatibility of electrodynamical and mechanical boundary conditions. The proper incorporation of the elastic component into the theory in the hydrodynamic limit [24–27] ensures that there is an opportunity for matching the correct boundary conditions and makes it possible to reproduce the microscopic lattice dynamics data, obtaining at the same time closed expressions for the phonon electric fields. These calculations were recently confirmed by experimental investigations of the directional dispersion of phonons in superlattices [28]. The general peculiarities distinguishing the polar optical vibrations in the semiconductor layered structures from the bulk crystal case are well understood both experimentally and theoretically, and are

† E-mail address: vgt@phys.tsu.ru.

characterized by the presence of confined and interface modes. It was established in [25,27,29] that longitudinal and transverse components of vibrations are mixed in an arbitrary direction of phonon propagation.

A grave shortcoming of the aforementioned macroscopic approaches is that they implicitly ignore the difference between the effective (local) and actual (test charge) fields. In fact, they assume that the long-range forces which contribute to an ion's polarization are caused by the test charge field. In our paper we develop a theory of non-local dielectric response which provides a proper macroscopical extension, taking the local field corrections into account.

Thus our theory reveals a picture of phonon electric fields which differs in some essential details from the conventional one. Note in this connection that the aforementioned models to the best of our knowledge have never been checked directly by means of microscopical calculations. The fields derived from the lattice dynamics [3-6] are based on a model expression for the electron-phonon potential which essentially follows from a one-dimensional superlattice model [21]. However, the simplified dipole model [21] itself suffers from the same drawback concerning the local field corrections. In our paper we extend the approach of [21] with the local field corrections included to a realistic three-dimensional lattice dynamics calculation. This method gives information directly and so allows one to verify the models relevant to the phonon electric fields.

The two approaches presented here agree each with other fairly well. Combination of the two methods gives in our opinion the most natural link between microscopic and continuum theories.

The organization of the paper is as follows. In section 2 we develop the generalization of dielectric theory with the local field corrections taken into account. Section 3 describes the methods used for the computing of phonon electric fields directly from lattice dynamics data. In section 4.1 we discuss the results of direct lattice dynamics calculations for the superlattice $(GaAs)_{10}(AlAs)_{10}$ [001] and in section 4.2 we interpret these results from the viewpoint of a non-local dielectric response theory. Section 5 gives our conclusions. The appendix contains an exact solution within a model of a dispersionless inhomogeneous dielectric continuum.

## 2. Non-local microscopic dielectric response in the phonon frequency region

### 2.1. General considerations

The dielectric continuum approaches [7-10,17,21,24,25,27] essentially treat the dielectric response in nano-structures as a local relation between applied and induced fields with spatially and frequency-dependent dielectric constants which are different for each constituent material. Strictly, the dielectric properties of inhomogeneous media should be described in a non- local manner as an integral relation between the applied and induced fields with a spatially and frequency-dependent kernel [30]. It has long been established in the electron theory that the spatially dependent dielectric constant (dielectric function) approximation actually neglects the distinction between the effective (polarizing) and actual (test charge) fields and so is inappropriate. The rigorous dielectric matrix approach describes properly the so-called local field corrections and is adequate for providing an understanding of the response in inhomogeneous media [30-34]. In this section we develop a theory which inherently takes into account the non-local linkage of applied and effective fields and properly incorporates the local field effects for the nano-materials in the infrared frequency region. Similar ideas were developed recently in [35].

We begin with the phenomenological expression for the energy of a crystal in a spatially

slowly varying electric field $\boldsymbol{E}(\boldsymbol{r})$ [36]:

$$
\begin{aligned}
W=\frac{1}{2} \sum_{n n^{\prime}} \boldsymbol{u}^{n} \cdot \widehat{\Phi}^{s r}\left(n n^{\prime}\right) \boldsymbol{u}^{n^{\prime}} & -\sum_{n} \int \boldsymbol{u}^{n} \cdot \widehat{\Psi}(n, \boldsymbol{r}) \boldsymbol{E}(\boldsymbol{r}) \mathrm{d} \boldsymbol{r} \\
& -\frac{1}{8 \pi} \int \boldsymbol{E}(\boldsymbol{r}) \cdot \widehat{\varepsilon}_{\infty}\left(\boldsymbol{r}, \boldsymbol{r}^{\prime}\right) \boldsymbol{E}\left(\boldsymbol{r}^{\prime}\right) \mathrm{d} \boldsymbol{r} \mathrm{d} \boldsymbol{r}^{\prime}.
\end{aligned}
\tag{1}
$$

In this expression, $\boldsymbol{u}^{n}$ denotes the displacement of the $n$th atom, the force-constant matrix $\Phi_{\alpha \alpha^{\prime}}^{s r}(n, n^{\prime})$ describes the short-range part of the interatomic interaction including that associated with electrostatic forces but contains no contribution associated with a macroscopic field, and $\alpha, \alpha^{\prime}$ are Cartesian indexes. The effective transverse charge tensor $\Psi_{\alpha \alpha^{\prime}}(n, \boldsymbol{r})$ gives the $\alpha^{\prime}$-component of the dipole moment induced at the point $\boldsymbol{r}$ when the ion at site $n$ is displaced by unit distance in the $\alpha$-direction. $\widehat{\varepsilon}_{\infty}(\boldsymbol{r}, \boldsymbol{r}^{\prime})$ is the electronic contribution to the dielectric matrix.

The force acting on the atom due to its displacement $\boldsymbol{u}^{n}$ is determined from (1) as $-\partial W / \partial \boldsymbol{u}^{n}$. The electric displacement is defined as $\boldsymbol{D}=-4 \pi \partial W / \partial \boldsymbol{E}$. Then, from the classical equation of motion, assuming the same harmonic time evolution with a frequency $\omega$ for all quantities, we derive

$$
D_{\alpha}(\boldsymbol{r}, \omega)=\sum_{\beta} \int\left\{\varepsilon_{\infty \alpha \beta}\left(\boldsymbol{r}, \boldsymbol{r}^{\prime}\right)+4 \pi N^{-1} \sum_{\lambda q} \frac{G_{\alpha}^{\lambda q}(\boldsymbol{r}) G_{\beta}^{\lambda q *}\left(\boldsymbol{r}^{\prime}\right)}{\Omega_{\lambda}^{2}(\boldsymbol{q})-\omega^{2}}\right\} E_{\beta}\left(\boldsymbol{r}^{\prime}, \omega\right) \mathrm{d} \boldsymbol{r}^{\prime}.
\tag{2}
$$

The expression in the curly brackets describes the non-local frequency-dependent dielectric response of an inhomogeneous medium to an applied field. The quantity $G^{\lambda q}(\boldsymbol{r})$ is defined by the relation

$$
G^{\lambda q}(\boldsymbol{r})=\sum_{l p} m_{p}^{-1 / 2} \mathrm{e}^{\mathrm{i} \boldsymbol{q} \cdot\left(\boldsymbol{r}-\boldsymbol{R}_{l}\right)} \widehat{\Psi}\left(p, \boldsymbol{r}-\boldsymbol{R}_{l}\right) \boldsymbol{f}^{\lambda q}(p).
\tag{3}
$$

Here $\boldsymbol{f}^{\lambda q}(p), \Omega_{\lambda}^{2}(\boldsymbol{q})$ are the solutions of the eigenvalue problem with the dynamical matrix of short-range forces derived from $\Phi_{\alpha \alpha^{\prime}}^{s r}(l p, l^{\prime} p^{\prime})$ in the usual way [36], $l$ is the number of the unit cell and $p$ labels the atom inside it, $\boldsymbol{q}$ is a phonon wave-vector inside the Brillouin zone, and $N$ is the number of unit cells in the crystal.

Having in mind the application to $(\mathrm{GaAs})_{n}(\mathrm{AlAs})_{m}$, we consider the case of a spatially independent electronic contribution $\widehat{\varepsilon}_{\infty}(\boldsymbol{r}, \boldsymbol{r}^{\prime})$ and hereafter approximate it as $\varepsilon_{\infty} \delta_{\alpha \beta} \delta\left(\boldsymbol{r}-\boldsymbol{r}^{\prime}\right)$ for the sake of simplicity. A generalization to the case with the spatial dependence $\widehat{\varepsilon}_{\infty}(\boldsymbol{r}, \boldsymbol{r}^{\prime})$ is straightforward.

Performing the Fourier transformation, neglecting the retardation effects, restricting consideration to the case of longitudinal fields $\boldsymbol{E}(\boldsymbol{k}, \omega)=\boldsymbol{k} E(\boldsymbol{k}, \omega) / k$, and using the translation property $\widehat{\Psi}(l p, \boldsymbol{r})=\widehat{\Psi}(p, \boldsymbol{r}-\boldsymbol{R}_{l})$ where $\boldsymbol{R}_{l}$ is a direct-lattice vector, we find from the Maxwell's equation $\operatorname{div} \boldsymbol{D}=0$

$$
\sum_{\boldsymbol{K}^{\prime}}\left\{\varepsilon_{\infty} \delta_{\boldsymbol{K} \boldsymbol{K}^{\prime}}+4 \pi V_{c} \sum_{\lambda} \frac{g^{\lambda q}(\boldsymbol{K}) g^{* \lambda q}\left(\boldsymbol{K}^{\prime}\right)}{\left(\Omega_{\lambda}^{2}(\boldsymbol{q})-\omega^{2}\right)}\right\} E\left(\boldsymbol{q}+\boldsymbol{K}^{\prime}, \omega\right)=0.
\tag{4}
$$

Here
$$
g^{\lambda q}(\boldsymbol{K})=\left(\boldsymbol{q}+\boldsymbol{K}, G^{\lambda q}(\boldsymbol{K})\right)|\boldsymbol{q}+\boldsymbol{K}|^{-1}.
$$

$\boldsymbol{K}$ is a reciprocal-lattice vector, and $V_{c}$ is the unit-cell volume. Non-trivial solutions of (4) exist if $\Omega_{\lambda}^{2}(\boldsymbol{q})-\omega^{2} \neq 0$. Making the substitution
$$
C^{\lambda q}=\sum_{\boldsymbol{K}} g^{\lambda q}(\boldsymbol{K}) E(\boldsymbol{q}+\boldsymbol{K}, \omega)\left(\Omega_{\lambda}^{2}(\boldsymbol{q})-\omega^{2}\right)^{-1}
$$

reduces (4) to the eigenvalue problem

$$
\sum_{\lambda^{\prime}}\left\{\Omega_{\lambda}^{2}(\boldsymbol{q}) \delta_{\lambda \lambda^{\prime}}+4 \pi V_{c} \varepsilon_{\infty}^{-1} \sum_{\boldsymbol{K}} g^{\lambda q}(\boldsymbol{K}) g^{* \lambda^{\prime} q}(\boldsymbol{K})\right\} C_{i}^{\lambda^{\prime} q}=\omega_{i}^{2}(\boldsymbol{q}) C_{i}^{\lambda q}.
\tag{5}
$$

The irregular term $(\boldsymbol{q}, \bar{G}^{\lambda q})(\boldsymbol{q}, \bar{G}^{\lambda^{\prime} q *}) / q^{2}$ which essentially depends on the direction of $\boldsymbol{q}$ is an important peculiarity of equation (5). Here $\bar{G}^{\lambda q}$ is a space average (zero Fourier component) of $G^{\lambda q}(\boldsymbol{r})$. It is easy to check by direct substitution that the quantities

$$
E_{i}^{i}\left(\boldsymbol{q}+\boldsymbol{K}, \omega_{i}(\boldsymbol{q})\right)=\sum_{\lambda} C_{i}^{\lambda q} g^{\lambda q}(\boldsymbol{K})
\tag{6}
$$

satisfy (4) and consequently should be associated with the longitudinal (eigen)field created by a lattice vibration with a frequency $\omega_{i}(\boldsymbol{q})$.

We regard the fields $\boldsymbol{E}(\boldsymbol{r})$ as slowly varying functions on the interatomic scale. In other words, we believe that $\boldsymbol{E}(\boldsymbol{q}+\boldsymbol{K}) \approx 0$ for any $|\boldsymbol{K}| \gtrsim \pi / a_{0}$ where $a_{0}$ is the interatomic distance. In a bulk crystal where the lattice vectors $|\boldsymbol{R}_{l}| \sim a_{0}$, the only reciprocal-lattice vector which satisfies this condition is $\boldsymbol{K}=0$; hence only a macroscopic component exists, and any microscopic fields with $\boldsymbol{K} \neq 0$ should vanish for a long-wavelength phonon, which is the usual result [36]. In a superstructure geometry, the dimension of the large super-cell $|\boldsymbol{R}_{l}| \gg a_{0}$. Therefore an entire set of reciprocal-lattice vectors exists with $|\boldsymbol{K}| \leqslant \pi / a_{0}$. Then it follows from (6) that components of fields having the period of the super-cell should arise. One is led to conclude that phonons can in some circumstances create microscopic (local) electric fields showing a variation on the scale of the super-cell width, attended with a slow variation on the interatomic scale. They should be distinguished from the macroscopic fields which correspond to $\boldsymbol{K}=0$ and have the crystal dimension as the scale of variation.

### 2.2. The microscopical dielectric matrix for superstructures

For a superstructure $(\mathrm{AC})_{n_{1}}(\mathrm{BC})_{n_{2}}$ constructed from binary sub-cells, it is convenient to introduce the envelope functions $S^{\lambda}(p)$ via the relation

$$
S^{\lambda}(p)=(-1)^{p}\left(m_{p} / \mu_{p}\right)^{1 / 2} \boldsymbol{f}^{\lambda}(p)
\tag{7}
$$

where $\mu_{p}^{-1}=\left(m_{p}^{-1}+m_{p+1}^{-1}\right) / 2$ is a reduced mass. The centre-of-mass displacement in any binary sub-cell will be
$$
\mu_{p}^{-1 / 2} S^{\lambda}(p)-\mu_{p+1}^{-1 / 2} S^{\lambda}(p+1)
$$
and should be close to zero for a long-wavelength optical vibration as long as $\mu_{p}=\mu_{p+1}$. So, unlike the eigenvectors $\boldsymbol{f}^{\lambda}(p)$, the reduced displacements $S^{\lambda}(p)$ should be smooth functions everywhere except possibly in the vicinity of the interface. This observation is readily confirmed in our lattice dynamics calculations (section 3), and was already noted in [12].

Using the relationship

$$
M^{-1} \sum_{m=0}^{M-1} \exp \left(2 \pi \mathrm{i}\left(k-k^{\prime}\right) m / M\right)=\delta_{k k^{\prime}}
\tag{8}
$$

which is valid for any integers $M, m, k, k^{\prime}$ if $0 \leqslant k<M$ and $0 \leqslant k^{\prime}<M$, one can make a formal transformation from 'quasi-continuum' functions into continuum ones [38]:

$$
\begin{aligned}
S^{\lambda}(z)= & \left(2 N_{c}\right)^{-1} \sum_{m, p=0}^{2 N_{c}-1} S^{\lambda}(p) \mathrm{e}^{2 \pi \mathrm{i} m\left(z-p a_{0}\right) / D} \\
\widehat{\boldsymbol{\Psi}}\left(z^{\prime}, z\right)= & \left(2 N_{c}\right)^{-1} \sum_{m, p=0}^{2 N_{c}-1} \int \sum_{l} \widehat{\boldsymbol{\Psi}}\left(p, \boldsymbol{r}-\boldsymbol{R}_{l}\right) \mathrm{e}^{\mathrm{i} \boldsymbol{q} \cdot\left(\boldsymbol{r}-\boldsymbol{R}_{l}\right)} \mathrm{d} x \mathrm{~d} y \\
& \times(-1)^{p} m_{p}^{-1} \sqrt{\mu_{p}} \mathrm{e}^{2 \pi \mathrm{i} m\left(z^{\prime}-p a_{0}\right) / D}
\end{aligned}
\tag{9}
$$
```

The necessary parity properties of (12) are provided if the corresponding integers $k$ are $a=2m$ for $\Gamma_1$, and $s=2m+1$ for $\Gamma_3$. To avoid a possible misunderstanding, let us stress that odd integers correspond to even representations and vice versa. The representation $\Gamma_{5x}$ has both odd and even components. We retain for the integers which correspond to $x$-polarized $\Gamma_{5x}$ the labellings $u=2m$ and $g=2m+1$ in order to distinguish these states from $z$-polarized $\Gamma_1$ and $\Gamma_3$.

One can see a role of $\Psi_{\alpha\alpha'}(z',z)$ in cutting off the components $|K_n|\geqslant\pi/a_0$ from a formally infinite set in the Fourier decompositions of both $E_\alpha(z)$ and $S_\alpha(z)$. Hence we shall consider $\Psi_{\alpha\alpha'}(z',z)$ as a function that is well localized at a distance of the order of a bilayer width $2a_0$. The simplest approximation consists in neglecting its slow dependence in the second argument $\Psi_{\alpha\alpha'}(z,z')=\delta_{\alpha\alpha'}\Psi(z)$ where $\Psi(z)=\xi_L/(\eta V_a\sqrt{\mu_L})$ if $|z|\leqslant\eta$ and zero otherwise, with $\eta\sim2a_0$. $V_a$ is a volume per atom, $\xi_L$ is the modulus of the ion charge and $\mu_L$ is the reduced mass in the $L$th slab. This leads to the expression

$$
G_{\alpha}^{L J k}(z)=n_{L}^{-1 / 2} e_{\alpha}^{(J)} \frac{\xi_{L} d_{L}}{V_{a} \sqrt{\mu_{L}} \pi k \eta} \sin \frac{\pi k \eta}{d_{L}} \sin \left(\pi k \frac{z-\tau_{L}}{d_{L}}\right) \Theta_{L}(z).\qquad(13)
$$

In what follows, we neglect the overlapping of $G_{\alpha}^{L J k}$ in different layers. If also $\xi_L^2(\mu_L V_a^2)^{-1}/(\Omega_{(L)}^2-\Omega_{(L')}^2)\ll1$, we can use perturbation theory and reduce the dimension of problem (5). In a good approximation we can introduce an effective background dielectric constant $\varepsilon_\infty^L$ of any chosen $L$th slab. We just add to (4) the contribution to $\varepsilon_\infty$ from another slab $L'$ with the frequency denominator $\Omega_\lambda^2-\omega^2$ replaced by $\Omega_{L'}^2-\Omega_L^2$. Hereafter all quantities relate to the chosen layer, so the index $L$ can be omitted.

After some algebra one gets
$$
\begin{array}{ll}
\Lambda_{k k^{\prime}}^{(5 y)}=\Omega_{k}^{2} \delta_{k k^{\prime}} \quad \Lambda_{u u^{\prime}}=\Omega_{u}^{2} \delta_{u u^{\prime}} & \Lambda_{a a^{\prime}}=\left(\Omega_{a}^{2}+B_{a}^{2}\right) \delta_{a a^{\prime}} \\
\Lambda_{g g^{\prime}}=\Omega_{g}^{2} \delta_{g g^{\prime}}+h_{g g^{\prime}} q_{x}^{2} / q^{2} & \Lambda_{g s}=h_{g s} q_{x} q_{z} / q^{2} \\
\Lambda_{s s^{\prime}}=\left(\Omega_{s}^{2}+B_{s}^{2}\right) \delta_{s s^{\prime}}-h_{s s^{\prime}}+h_{s s^{\prime}} q_{z}^{2} / q^{2} & q^{2}=q_{x}^{2}+q_{z}^{2}
\end{array}\qquad(14)
$$
where $\Lambda_{k k'}$ stands for the expression inside the curly brackets in (5) and
$$
\begin{aligned}
& B_{k}=\sqrt{4 \pi /\left(\varepsilon_{\infty} V_{a} \mu\right)} \xi d \sin (\pi k \eta / d) /(\pi k \eta) \\
& h_{k k^{\prime}}=2 n\left[1-(-1)^{k}\right]\left[1-(-1)^{k^{\prime}}\right] B_{k} B_{k^{\prime}} /\left(N_{c} \pi^{2} k k^{\prime}\right).
\end{aligned}\qquad(15)
$$

We intend to apply the above theory to the investigation of $(\mathrm{GaAs})_{n_1}(\mathrm{AlAs})_{n_2}$ [001] superlattices in section 4. As the local field corrections produce a noticeable effect, careful verification by an independent method is very desirable. It turns out that there exists an opportunity to make a check by means of a direct calculation. It is commonly accepted that microscopical lattice dynamics calculations cannot give direct knowledge relevant to the phonon electric fields. Actually, a way of extracting this information was already presented in [17,21], and was applied to a simplified one-dimensional dipole superlattice model. In the next section we extend this approach to a realistic three-dimensional lattice dynamics model.

### 3. Electrostatic fields of phonons in a lattice dynamics

Let $u_p=m_p^{-1/2}f^{\lambda q}(p)b_{q\lambda}$ be the displacement of the $p$th ion that is involved in the propagation of the $\lambda$th phonon with the wave-vector $q$ and the amplitude $b_{q\lambda}$. Here we regard the $f^{\lambda q}(p)$ as the eigenvectors of a full lattice dynamical problem which contains both the short-range and the electrostatic part. Then the electric contribution to a force acting at the ion at a lattice position $R_p$ can be derived by definition as

$$
F_{\alpha}^{e l}\left(\boldsymbol{R}_{p}\right)=-\sum_{p^{\prime} \beta} C_{\alpha \beta}\left(p p^{\prime} \mid \boldsymbol{q}\right) u_{\beta}^{p^{\prime}}\qquad(16)
$$


where $C_{\alpha \beta}(p p'|q)$ is the electrostatic contribution to the interatomic interaction derived by Ewald's method [36]. The local electrostatic field at the lattice point $\boldsymbol{R}_p$ can be defined as $\xi_p E_{\alpha}^{\text{local}}(\boldsymbol{R}_p) = F_{\alpha}^{el}(\boldsymbol{R}_p)$ where $\xi_p = (-1)^p \xi$ is the ion's (transverse) charge. The force $F_{\alpha}^{el}(\boldsymbol{R}_p)$ as a function of $\boldsymbol{R}_p$ contains both fast (short-range) and slow components. One can exclude the short-range contribution from (16) using a well known Lorentz relationship between the actual (test charge) field $E_{\alpha}(\boldsymbol{R}_p)$ and the local one:

$$
E_{\alpha}(\boldsymbol{R}_p) = E_{\alpha}^{\text{local}}(\boldsymbol{R}_p) - 4\pi \Pi_{\alpha}(\boldsymbol{R}_p)/3
$$

where $\Pi_{\alpha}(\boldsymbol{R}_p)$ is a lattice polarization at the ion site.

From the definition of a polarization as a density of a dipole moment, one has, in a binary sub-cell, $\boldsymbol{\Pi}(p) = (z_p \boldsymbol{u}_p + z_{p+1} \boldsymbol{u}_{p+1})/(2V_a)$. Here $z_p$ is an effective dynamical charge of an ion which phenomenologically takes into account the electronic contribution to the lattice polarization as $z_p^2 = \xi_p^2/\varepsilon_{\infty}$ [31,32,34]. Using (7), we have, for the polarization produced by the $\lambda$th vibrational mode,

$$
\Pi_{\alpha}(p) \approx (V_a \mu_p)^{-1} z_p m_p^{1/2} f_{\alpha}^{\lambda}(p) b_{\lambda}
$$

as long as the property of the slow variation $|(S_{\alpha}^{\lambda}(p) - S_{\alpha}^{\lambda}(p+1))/S_{\alpha}^{\lambda}(p)| \ll 1$ is valid.

To avoid some convergence problems which arise in the standard Ewald method for layered structures [14], we use a mass-defect approximation presented in [39,40]. Let us consider a superlattice $(\text{GaAs})_{n_1}(\text{AlAs})_{n_2}$ grown along the $z$-axis with a super-cell consisting of two slabs with $n_1$ and $n_2$ bilayer sub-cells respectively. We neglect the difference between the lattice constants and construct a superlattice unit cell, imposing $\boldsymbol{R}_p = \boldsymbol{R}_n + \boldsymbol{r}_s$, $\boldsymbol{R}_n = a_0(0, Y_n, 2n)$, where $n = 0, \dots, N_c - 1$; $s = 1,2$; $\boldsymbol{r}_1 = 0$, $\boldsymbol{r}_2 = a_0(1,1,1)$. Here $a_0 = a/4$ is the monolayer separation, $a$ is a bulk lattice constant, $Y_n = \text{frac}(n/2)$ where $\text{frac}(y)$ means the fractional part of the expression $y$. The positions $s=1$ are occupied by Al if $0 \leqslant n < n_1$ and by Ga if $n_1 \leqslant n < N_c$; $s=2$ is the position of As. If we accept that the interatomic interactions in bulk GaAs and AlAs coincide, then the ion charges of Ga and Al should also be identical (and hence have the opposite sign to that for As). Then, using Ewald's expression [36] and (8), one can prove the relation [41]

$$
C_{\alpha \beta}^{\text{Ewald}}(n s, n' s' | \boldsymbol{q}) = N_c^{-1} \sum_{m=0}^{N_c-1} c_{\alpha \beta}^{\text{Ewald}}(s, s' | \boldsymbol{q} + \boldsymbol{K}) \text{e}^{-\text{i}(\boldsymbol{q}+\boldsymbol{K}) \cdot (\boldsymbol{R}_n - \boldsymbol{R}_{n'})} \tag{17}
$$

where $c_{\alpha \beta}^{\text{Ewald}}(s, s' | \boldsymbol{\varkappa})$ is the Coulomb contribution for bulk GaAs, $\boldsymbol{q}$ belongs to the Brillouin zone of the superlattice, and the $\boldsymbol{K}$ are defined in section 2.2.

An alternative approach to the calculation of the electrostatic fields consists in the replacement of the point ion's interaction matrix $\widehat{\mathbf{C}}$ in (16) by that of interacting Gaussians $\widehat{\mathbf{C}}^{\text{Gauss}}$, and now treating $F_{\alpha}^{el}(\boldsymbol{R}_{lp})$ just as a force acting on a test charge $F_{\alpha}^{el}(\boldsymbol{R}_{lp}) = \xi_p E_{\alpha}(\boldsymbol{R}_{lp})$. This idea was advanced in [21] via an example of a quasi-one-dimensional lattice dynamical model. In three dimensions, we can again avoid the convergence problems by assuming Al and As to have the same charges, considering a superlattice as a superstructure of GaAs and replacing in (16) $C_{\alpha \beta}^{\text{Ewald}}(n s, n' s' | \boldsymbol{q})$ by $C_{\alpha \beta}^{\text{Gauss}}(n s, n' s' | \boldsymbol{q})$ as calculated from (17) with

$$
c_{\alpha \beta}^{\text{Gauss}}(s s' | \boldsymbol{k}) = \frac{4\pi z_s z_{s'}}{V_B} \sum_{\boldsymbol{Q}} \frac{(\boldsymbol{k}+\boldsymbol{Q})_{\alpha} (\boldsymbol{k}+\boldsymbol{Q})_{\beta}}{(\boldsymbol{k}+\boldsymbol{Q})^2} \text{e}^{-(\boldsymbol{k}+\boldsymbol{Q})^2/(4G^2)} \text{e}^{\text{i}\boldsymbol{k} \cdot (\boldsymbol{r}_s - \boldsymbol{r}_{s'})}. \tag{18}
$$

Summation over the reciprocal-lattice vectors $\boldsymbol{Q}$ of bulk GaAs is assumed in equation (18), $\boldsymbol{k}$ belongs to its Brillouin zone, and $V_B = a^3/4$ is the GaAs bulk unit-cell volume. The short-range oscillations in $F_{\alpha}^{el}(\boldsymbol{R}_{lns})$ disappear abruptly in the vicinity of the broadening parameter $G = (0.38)2\pi/a$, implying that any bulk vectors $\boldsymbol{Q}$ longer than $\approx \pi/a_0$ are effectively cut off and the remaining smooth contribution essentially coincides with that computed with $\widehat{\mathbf{C}}^{\text{Ewald}}$.

## 4. Results and discussion

### 4.1. Lattice dynamics

It is convenient to begin our analysis of phonon fields from the lattice dynamics results. Hereafter, we adopt the mass-defect approximation with the 11-parameter rigid-ion model of Kunc et al [42] for bulk GaAs which was earlier applied to (GaAs)ₙ(AlAs)ₘ [001] in [13]. The calculated spectrum and displacement patterns reproduce features which are well established elsewhere [12–16]. The left-hand panel of figure 1 displays a high-frequency part of the long-wavelength optical spectrum which corresponds to the vibrations confined in the AlAs slab of the (GaAs)₁₀(AlAs)₁₀ unit cell. The picture for the GaAs-like vibrations is similar, and we will not discuss it here.

![](./images/812461764082925570_1.jpg)

Figure 1. The directional dependence of the frequencies for AlAs-like long-wavelength phonons in GaAs₁₀AlAs₁₀ [001] as calculated within the 11-parameter rigid-ion model (left-hand panel) and within the non-local dielectric model (right-hand panel). $\theta$ is the angle between the phonon wavevector $q \to 0$ and the superlattice growth direction $z$. The symmetry classifications correspond to those given in [37]. Solid curves correspond to the representations $\Gamma_3$ (even) and $\Gamma_{5x}$ (even). Dashed lines correspond to the full-symmetry representations $\Gamma_1$ (odd). Dotted lines correspond to $\Gamma_{5x}$ (odd).

In the long-wavelength limit $q \to 0$, all of the optical frequencies $\omega(\Gamma_3)$ exhibit directional dependence while the $\omega(\Gamma_1)$ do not. The $\Gamma_5$ phonons can be divided into two groups. Half of them also display directional dependence. It is very pronounced for the most energetic $\Gamma_5$ phonon. For the other $n_1 - 1$ phonons of that group, the angular dispersion is small but definitely exceeds the level of computational error. A survey of the polarization vectors shows that the ion displacements for this group are even with respect to the central plane of the active

slab. The remaining $n_1\ \Gamma_5$ phonons have odd displacement patterns and never show directional dependence. The corresponding frequencies are always doubly degenerate within the limits of computational errors.

![](./images/812461764082925570_2.jpg)

The two approximations discussed in section 3 give the same electric fields. The calculated amplitudes of the fields (16) at the monolayer positions for the long-wavelength optical phonons in the AlAs slab are displayed in figure 2(a). In (16) we have adopted $b_{q\lambda}=(\hbar/2\omega_\lambda(q))^{1/2}$ as the standard value of the classical amplitude, which approximately corresponds to one phonon per super-cell in the quantum case. The results are also qualitatively the same for AlAs- and GaAs-like phonons and we do not discuss the latter here for reasons of space.

In the long-wavelength limit $q\rightarrow0$, the fields associated with any vibrations of symmetry $\Gamma_1$ and phonons of symmetry $\Gamma_3$ that are longitudinal at $q\parallel z$, exhibit a well known picture of confined bulk states which are odd and even functions, respectively, with respect to the central plane of the active slab. The picture of the fields at $q\perp z$ associated with the transverse $\Gamma_3$ phonons is completely different. They contain spatially varying components inside the active AlAs slab but do not vanish in the neighbouring GaAs slabs, and consequently cannot be strictly considered as confined states. One can check that their spatial average is exactly zero. As they are extended throughout the whole crystal, they could be associated with the so-called bulk-like interface phonons of the dielectric continuum approaches. However, they do not visibly display an exponential decay into the conjugated layers which is the conventional result in

the continuum approaches. Another new and important feature of our findings is the intensity dependence of the fields on the frequency. To the best of our knowledge this peculiarity has not been detected in continuum theories. However, it could have been expected because the high-order modes originating from the short-wavelength phonons of the bulk crystals should be less influenced by the contribution of long-range forces.

Representation $\Gamma_{5}$ never creates a $z$-component of the field. The in-plane $x-y$ components of the fields always vanish for the transverse configuration $\boldsymbol{q} \| z$ when $\Gamma_{5}$ phonons propagate along the $z$-axis. Relative to the longitudinal configuration $\boldsymbol{q} \perp z$, all $2 n_{1}$ of the $\Gamma_{5}$ phonons can be divided into two groups. The half of the $\Gamma_{5}$ phonons which have odd displacement patterns never create any electric fields. The other $n_{1}$ of the $\Gamma_{5}$ phonons with even displacement patterns create the fields which lie in the $x y$-plane and have only in-plane macroscopic components. The magnitude of the in-plane macroscopic component of the field achieves its maximal value for the most energetic phonon of this group. It has a small but non-vanishing value for the other $n_{1}-1$ phonons.

An inspection of the results for various ratios of slab widths $n_{1}, n_{2}$ reveals the general rule that the maximal number of electrically active frequencies coincides in each group ( $z$-polarized $\Gamma_{1}, \Gamma_{3}$ and $x y$-polarized $\Gamma_{5}$ ) and is equal to the number of bilayers $n_{L}$ in the active slab, while the minimal wavelength approximately corresponds to the bilayer width.

![](./images/812461764082925570_3.jpg)

Figure 3. Electrostatic potentials associated with long-wavelength $\Gamma_{3}(\widehat{q} \perp z)$ and $\Gamma_{1}$ (any $q \to 0$) AlAs-like phonons. Panels (LD): lattice dynamics calculation; panel (DM): the exact dispersionless continuum solution. Distance along $z$ is in units of the atomic monolayer width.

![](./images/812461764082925570_4.jpg)

Figure 4. Electrostatic potentials associated with long-wavelength $\Gamma_3$ ($\widehat{q} \parallel z$) AlAs-like phonons (full curves) as calculated from the lattice dynamics. Dotted lines represent the macroscopic component. The sequence of curves corresponds to that of the frequencies in figure 1.

![](./images/812461764082925570_5.jpg)

Figure 5. Electrostatic fields associated with two selected $\Gamma_1$- and $\Gamma_3$-originated AlAs-like phonons at wave-vector $(0,0,\pi/D)$.

As one can see from figure 3, panels (LD), the potentials created by AlAs-originated long-wavelength $\Gamma_1$ (odd) phonons vary quickly in the AlAs layer and are constant in the conjugated passive GaAs layers. The in-plane-propagating $(q \perp z)$ $\Gamma_3$ (even) phonons create potentials which vary rapidly inside the AlAs slab (figure 3, panels (LD)) and are linear functions of $z$ in the conjugated GaAs layers. The potentials created by $\Gamma_3$ (even) phonons propagating along the growth direction of the superlattice, $q \parallel z$, display a staircase behaviour (figure 4) which coincides qualitatively with that discussed in reference [43]. They cover the whole crystal with a rapid variation inside the active slab and are also constant inside the conjugated GaAs slabs.

Phonons with finite wave-vectors can be analysed on the same footing. The representative results of lattice dynamical calculations for two selected AlAs-like phonons in $(GaAs)_{10}(AlAs)_{10}$ at the Brillouin-zone edge $(0,0,q)$, $q = \pi/D$, are shown in figure 5.

The calculated fields for in-plane propagation with the wave-vector $(q,0,0)$ for six high-frequency modes are shown in figure 6, panel (LD). The value $q = 2\pi/D = 0.11$ $\mathring{A}^{-1}$ was chosen as a representative one. Each field has a part which is quasi-confined in an active slab and a component penetrating into a passive layer to a greater or lesser extent. One could associate these extended components with the interface modes of the continuum theories. However, the latter should be substantially damped at this value of $q$ inside a passive slab [4,6], while some of modes in figure 6, panel (LD), do not show signs of exponential decay at all and display instead a linear $z$-dependence. All of the modes contain admixtures of extended components,

![](./images/812461764082925570_6.jpg)

Figure 6. Electric forces created by in-plane AlAs-like phonons with the wave-vector $(2\pi/D,0,0)$. Panel (LD): calculated from the lattice dynamics; panel (DM): the dielectric matrix approximation. Dashed curves: Re $E_{z}(z)$; solid curves: Im $E_{x}(z)$; dotted lines: spatial averages of Im $E_{x}$ (macrofields).

while according to reference [25,27] a genuine interface state should not be coupled with the odd fields. One can see that each field has a real $E_{z}$-component and an imaginary $E_{x}$-component, and consequently has a circular polarization. These patterns persist qualitatively for the different widths of layers and various formal ratios $m_{\mathrm{Ga}}/m_{\mathrm{Al}}$ provided that the ratio is far enough from unity. An examination in a more elaborate (bond-charge) model reveals similar results. The picture does not seem to be entirely consistent with the commonly accepted notion and needs an explanation. That is provided by a microscopical dielectric response analysis which is developed in the following subsections.

### 4.2. The non-local dielectric model

#### 4.2.1. The dispersionless continuum.
The general qualitative consequences of local field corrections incorporated into the dielectric theory follow from the exact solution of (5), (14) which is available within the model of a dispersionless continuum and is presented in the appendix. In accordance with the conventional continuum approaches, the greater part of the vibrational states are confined inside an active slab and are dispersionless. There are two selected modes with direction-dependent frequencies, which is also a familiar result. The new

finding is that this angular dispersion originates from the non-local nature of the dielectric response. It appears that the frequencies as functions of the phonon propagation direction (A.3) are different from those obtained from the interface-mode transcendent equation of the continuum theories. The corresponding fields (A.5) and potentials (A.8) are extended into a non-active slab, but their shapes (stepwise and saw-edged, respectively) differ qualitatively from the conventional picture of exponentially evanescent interface states. The remarkable similarity of this result with the lattice dynamics calculations (figure 3, panels (LD), (DM)) attests to these features being representative of the real physical situation.

4.2.2. Long-wavelength phonons in $(GaAs)_{10}(AlAs)_{10}$ [001]. As is established elsewhere [25,27], any realistic approximation should take into account a dispersion of short-range forces. To make the separation of Coulomb forces in (1) into short-range and long-range parts into a somewhat better defined procedure, let us look at the well known Ewald expression for the electrostatic contribution to a dynamical matrix [36]. Usually it is considered as a purely computational trick—rearranging the conditionally converging series into two rapidly converging contributions in the direct and reciprocal spaces respectively. At the same time, one can treat the role of the Ewald breaking parameter as that of cutting off the Coulomb interactions of ions outside the corresponding sphere while the reciprocal sum includes all other interactions. So we can look at this procedure as a method of separation of the short-range forces (direct-lattice summing) and long-range ones (reciprocal-lattice ones). Consequently we have taken the direct-lattice Ewald contribution with the best-converging breaking parameter $G \approx 0.5\pi/a$ and united it with the covalent force contribution of the 11-parameter model [42] to give the overall short-range input. The resulting short-range frequency dispersion in the relevant direction $(2\pi/a)(00\kappa)$ for bulk AlAs and GaAs can be approximated by simple functions:

$$
\Omega_{x, z}^{B}(\kappa)=\Omega-\eta_{x, z}\left(1-\exp \left\{-\left(\kappa / \chi_{x, z}\right)^{R}\right\}\right)
\tag{19}
$$

where $R=4,2$ for $z$- and $x$-polarizations respectively. The values of the adjustable parameters for bulk crystals appear to be: AlAs: $\Omega=362 \mathrm{~cm}^{-1}, \eta_{z}=22 \mathrm{~cm}^{-1}, \eta_{x}=22 \mathrm{~cm}^{-1}$, $\chi_{z}=1.36, \chi_{x}=1.08$; GaAs: $\Omega=268 \mathrm{~cm}^{-1}, \eta_{z}=40 \mathrm{~cm}^{-1}, \eta_{x}=55 \mathrm{~cm}^{-1}, \chi_{z}=1.54$, $\chi_{x}=1.24$.

The application of a dielectric approach to the representative case of $(GaAs)_{10}(AlAs)_{10}$ [001] requires the diagonalization of a $10 \times 10$ matrix (14). In view of the small short-range dispersion (19), it would be a reasonable approximation, at least for the case where $q \rightarrow 0$, to treat (12) as a standing wave of length $2 d_{L} / k$ inside the corresponding layer. Due to the greater dispersion, this approximation is less well founded for $x$-polarized phonons; however, the influence of high-order $g$-modes, except the most energetic one (that with $g=1$ ), is negligible, so in effect the problem reduces to diagonalization of a $6 \times 6$ matrix. So we have taken $\Omega_{k}=\Omega_{z}^{B}\left(Q_{k}\right)$ if $k=a, s$ and $\Omega_{k}=\Omega_{x}^{B}\left(Q_{k}\right)$ if $k=g, u$ where $Q_{k}=a k /\left(2 d_{L}\right)$.

We have found that the results are improved substantially if we introduce an effective width of the layers $d_{L}$ which differs from the actual slab thickness, together with effective positions of the interfaces given by the relations $d_{1}=2 n_{1} a_{0}+2 \delta_{1}, d_{2}=2 n_{2} a_{0}+2 \delta_{2}$, $\tau_{1}=-\delta_{1}, \tau_{2}=2 n_{2} a_{0}-\delta_{2}$, which allow $S_{\alpha}^{L J k}(z)$ to spread a little into the neighbouring layers. The effective parameters are different for $z$ - and $x$-vibrations, and were chosen as $\delta_{1,2}=a_{0}$ for $\Gamma_{1}, \Gamma_{3}$ and $\delta_{1,2}=0$ for $\Gamma_{5}$. We found that the qualitative results depend substantially on these parameters. This dependence correlates with the influence of the spatial charge parameter $\eta$ and works in the same direction—lowering the frequencies of high-order modes and decreasing the amplitudes of the corresponding fields. This fact should be regarded as evidence of the importance of the interface region. The transverse charge parameter is taken as $\xi=z / \sqrt{\varepsilon_{\infty}}$, with the effective dynamical charge of the ion $z$ taken from [42], and with

$\varepsilon_{\infty}=12$ and $\eta=1.7 a_{0}$.

The calculated AlAs-like long-wavelength phonon spectrum for $(GaAs)_{10}(AlAs)_{10}$ [001] is presented in the right-hand panel of figure 1 and shows a good agreement with the angular dispersion obtained from the direct-lattice dynamics computations (left-hand panel). From dimensionality considerations, the solutions of (5) are normalized to a standard amplitude $b_{q \lambda}$ as in section 4.1. As one can see from figure 2(b), the forms of local fields also agree well with those calculated in a lattice dynamical approach (figure 2(a)).

Now the properties of the optical phonons in superstructures and the associated electric fields can be interpreted from the viewpoint of non-local dielectric theory.

The matrix (14) is block diagonalized. The odd phonons with different polarization are not coupled due to vanishing $\bar{G}^{\lambda}$, and their frequencies do not depend on the direction of the wavevector. The even $s$-modes $\Gamma_{3}$ and $x$-polarized $g$-states from the set of $\Gamma_{5}$ are hybridized via the irregular term $h_{g s} q_{x} q_{z} / q^{2}$ into an $n \times n$ block, and so their frequencies are direction dependent. They are decoupled at $q_{x}=0$, with $n$ longitudinal $z$-polarized solutions $\omega_{s}^{2}=\Omega_{s}^{2}+B_{s}^{2}$ and $n$ transverse ones $\omega_{g}^{2}=\Omega_{g}^{2}$ with $x$-polarization. As the block $\Lambda_{s s^{\prime}}$ in (14) is diagonal, the $z$-polarized solutions coincide with the initial basis (13). They create both macro-fields and local fields which are directed along $z$, the latter being well confined inside the corresponding layer. For the in-plane configuration, $s$ - and $g$-phonons are also decoupled, but the block $\Lambda_{s s^{\prime}}$ now needs diagonalization and its eigenvectors differ from the initial basis. According to (11), they contribute only to the local fields directed along the growth axis. The $x$-polarized $g$-states never create local fields. Propagating in the $x y$-plane, they produce in-plane macro-fields, as $\bar{G}_{x}^{g} \neq 0$. When these phonons propagate along $z$, their macro-fields vanish.

Next, there are $n$ odd $a$-states $\Gamma_{1}$ with $\omega_{a}^{2}=(\Omega_{a}^{2}+B_{a}^{2})$. As $\bar{G}_{z}^{a}=0$, these $z$-polarized solutions create the purely local electrostatic fields which are confined inside the corresponding layer.

There also exist $n$ odd $x$-polarized $u$-states from the set of $\Gamma_{5}$ with frequencies $\omega_{u}^{2}=\Omega_{u}^{2}$. According to (11), they never create any electric fields.

And, finally, there are $2 n$ trivial solutions with transverse $y$-polarization $(\Gamma_{5 y})$ for both even and odd $k=g, u$, with doubly degenerate frequencies $\omega_{k}^{2}=\Omega_{k}^{2}$.

4.2.3. Finite-wave-vector phonons in $(GaAs)_{10}(AlAs)_{10}$ [001]. The simple approximation (19) is not appropriate for the case of finite wave-vectors. However, some qualitative conclusions can be made on the basis of long-wavelength results as follows. First, for the case of cross-layer propagation, $(0,0, q)$ with $q=\pi / D$, it is easy to see from the comparison of figure 2 and figure 5 that the approximation $E_{z}^{q}(x, z)=\mathrm{e}^{\mathrm{i} q z} E_{z}^{0}(z)$ is a fairly good one. Next, the numerical analysis shows that for the in-plane propagation, $(q, 0,0)$, the relationship $\mathrm{d} E_{x}(z) / \mathrm{d} z=\mathrm{i} q E_{z}(z)$ describes the lattice dynamics data (figure 6, panel (LD)) with a great degree of accuracy. This means that the relevant fields are longitudinal ones, $E(x, z)=-\nabla\{\mathrm{e}^{\mathrm{i} q x} \phi^{q}(z)\}$, as they should be, because the lattice dynamics calculations neglect retardation effects. Consequently, the $x$-components of the fields shown in figure 6, panel (LD), by solid curves are in fact quantities proportional to the electric potentials induced by the in-plane-propagating phonons. Assuming a weak $q$-dependence of the periodic part
$$
\phi^{q}(z) \approx \lim _{q \rightarrow 0} \phi^{q}(z)+\Phi_{q}
$$
we get a good qualitative agreement (figure 6, panels (LD), (DM)) between the lattice dynamics and the dielectric model up to an unknown constant $\Phi_{q}$.

This approximation says nothing about the macroscopic component $\Phi_{q}$, and quantitative analysis for the finite-wave-vector propagation demands a closer investigation of the shortrange problem, which is the subject of a forthcoming paper. A comparison of the numerical data

within the rigid-ion and bond-charge models shows that the radius of action of the mechanical forces is qualitatively important. It is interesting that a central-force approximation destroys the above picture entirely, which indicates the crucial role of shear forces in the formation of polarization fields.

## 5. Conclusions
We present the lattice dynamical calculations of the local electrostatic fields with a mesoscopic scale of variation created by the optical phonons in the $(GaAs)_n(AlAs)_m$ [001] superlattices. Next we present an alternative model-independent approach based on non-local dielectric screening, which provides an apparatus for calculating both the optical phonon frequencies and their local fields within the electrostatic approximation. This dielectric theory treats the mechanical (short-range) part of the interaction on an equal footing with the long-range contribution, and is in this sense in the spirit of generalized continuum theories [25,27], but in addition takes into account the local field effects. The properties of the electric fields are in overall agreement with our lattice dynamical data as well as with those obtained in the existing continuum theories, and can be well understood in terms of eigenpotentials of a microscopical dielectric matrix. The local field corrections are of fundamental importance, and change qualitatively the shapes of the direction-dependent modes. A closed analytic form for the fields and potentials derived in a dispersionless continuum approximation may be of practical use for the investigation of carrier scattering processes. We believe that the relative simplicity of the dielectric matrix approach could make it useful in further applications to other types of nano-structure.

## Appendix. The exactly solvable model: non-local dielectric screening in the dispersionless continuum
The dispersionless continuum approximation is equivalent to the assumptions $\Omega_k^2 = \Omega^2$, $k = 1, ..., \infty$, $\eta \to 0$, $B_k \to B = \xi[4\pi/(\varepsilon_\infty V_a \mu)]^{1/2}$. We put $\tau = 0$, thus assuming the left-hand slab to be the active one. $d$ is its width, and $\bar{\mu} = \mu/a_0$ is a reduced mass density. We retain the labelling $s = 2m+1$, $a = 2m$ and $g = 2m+1$, $u = 2m$ for the even and odd $z$- and $x$-polarized states respectively. The solutions of (5) are normalized to a standard amplitude $b = (\hbar/2\Omega)^{1/2}$ as $C_\lambda = b\bar{C}_\lambda$. One deduces from (6), (14) the following results:

(a) Direction-independent (trivial) solutions $\omega_u^2(\Gamma_{5x}) = \Omega^2$.
(b) Direction-independent symmetric solutions $\omega_g^2(\Gamma_{5x}) = \Omega^2$ with non-vanishing $\bar{C}_g$ satisfying the orthogonality condition $\sum_g \bar{C}_g/g = 0$.
(c) Antisymmetric solutions with direction-independent frequencies $\omega_a^2(\Gamma_1) = \Omega^2 + \Delta$. The corresponding local fields are directed along $z$:
$$E_z^a(z) = E_0 \sin(\pi z/d)\Theta(z).$$
Here $\Theta(z)$ is the stepwise function introduced in (12), and
$$\Delta = 4\pi\xi^2/(\varepsilon_\infty V_a \mu) \quad E_0 = b\xi/(V_a\sqrt{\bar{\mu}d}).$$
(d) Taking all coefficients $\bar{C}_\lambda = 0$, except the $\bar{C}_s$ which satisfy the orthogonality condition $\sum_s \bar{C}_s/s = 0$, one get the direction-independent symmetric solutions $\omega_s^2 = \Omega^2+\Delta$ which originate from $\Gamma_3$ representations. We can use the multiple degeneracy of the solutions, and choose $\bar{C}_s = -s\bar{C}_1$. Taking into account the fact that $\sum_\lambda |\bar{C}_\lambda|^2 = 1$, we derive the fields
$$E_z^s(z) = E_0(s^2+1)^{-1/2}\Theta(z)\{\sin(\pi z/d)-s\sin(\pi s z/d)\} \tag{A.1}$$

with eigenpotentials which are continuous at the interfaces:

$$
\phi^{s}(z)=-d e_{0} E_{0} \pi^{-1}\left(s^{2}+1\right)^{-1 / 2} \Theta(z)\{\cos (\pi z / d)-\cos (\pi s z / d)\}. \tag{A.2}
$$

The average Fourier component of (A.1) and consequently also the macroscopic field $\bar{E}_{z}^{s}$ vanish, so these solutions are purely local ones.
(e) Taking $\bar{C}_{s}^{( \pm)}=2 \alpha^{( \pm)} /(\pi s)$ and $\bar{C}_{g}^{( \pm)}=2 \alpha^{(\mp)} /(\pi g)$, we get two direction-dependent solutions:

$$
\omega_{( \pm)}^{2}=\Omega^{2}+\frac{1}{2} \Delta\{1 \pm H\} \quad \alpha^{( \pm)}=(1 \pm\left(1-2 d \sin ^{2} \vartheta / D\right) / H)^{1 / 2} \tag{A.3}
$$

where
$$
H(\vartheta)=\left(\cos ^{2} \vartheta+\left(\sin ^{2} \vartheta\right)(D-2 d)^{2} / D^{2}\right)^{1 / 2}
$$

and $\theta$ is the angle that the phonon propagation vector $q$ makes with the growth axis $z$.
Using the relations

$$
\sum_{m=0}^{\infty} \frac{1}{(2 m+1)^{2}}=\frac{1}{8} \pi^{2} \quad \sum_{m=0}^{\infty} \frac{\sin (2 m+1) x}{(2 m+1)}=\frac{\pi}{4} \quad 0<x<\pi \tag{A.4}
$$

one has, from (11),
$$
E_{z}^{( \pm)}(z, \vartheta)=E_{z}^{( \pm) \text {macr }}(\vartheta)+E_{z}^{( \pm) \text {local }}(z, \vartheta)
$$

with a periodic part (local field) written as
$$
E_{z}^{( \pm) \text {local }}(z, \vartheta)=E_{0} \alpha^{( \pm)}[\Theta(z)-d / D]. \tag{A.5}
$$

These solutions create the macroscopic components of the field:
$$
E_{x}^{( \pm) \text {macr }}(\vartheta)=\beta^{( \pm)} q_{x} / q \quad E_{z}^{( \pm) \text {macr }}(\vartheta)=\beta^{( \pm)} q_{z} / q \tag{A.6}
$$
$$
\beta^{( \pm)}=\left[\alpha^{( \pm)} \cos \vartheta+\alpha^{(\mp)} \sin \vartheta\right] d / D. \tag{A.7}
$$

The local fields (A.5) correspond to the periodic potentials
$$
\phi^{( \pm) \text {local }}(z, \vartheta)=E_{0} e_{0} \alpha^{( \pm)}\{(D-d)(2 z-d) \Theta(z)+d(D+d-z)[1-\Theta(z)]\} /(2 D). \tag{A.8}
$$

We have arrived at the simple result that the irregular solution (A.3) for arbitrary direction of the phonon wave-vector $q \to 0$ constitutes a mixture of a periodic stepwise local field (A.5) directed along the superlattice's growth direction $z$ with a homogeneous electric field directed along the direction of the phonon propagation vector $q$ with components (A.6), (A.7). It is easy to check that (A.3), (A.6), (A.7) reduce to the ordinary bulk crystal angle-independent solutions [36] when the width of the active layer coincides with the super-cell dimension $d=D$. A number of first modes (A.2) and mode (A.8) are shown in figure 3, panel (DM).

## Acknowledgments
I thank Professor Gianni Mula for stimulating discussions. This work was supported in part by INTAS Foundation, under Grant No 93-1707 ext.

## References
[1] Jusserand B and Cardona M 1989 *Light Scattering in Solids* (Berlin: Springer) pp 49–152
[2] Menendez J 1989 *J. Lumin.* **44** 285
[3] Rücker H, Molinari E and Lugli P 1991 *Phys. Rev. B* **44** 3463
[4] Rücker H, Molinari E and Lugli P 1992 *Phys. Rev. B* **45** 6747
[5] Molinari E, Bungaro C, Gulia M, Lugli P and Rücker H 1992 *Semicond. Sci. Technol.* **7** B67

[6] Lee I, Goodnick S M, Gulia M, Molinari E and Lugli P 1995 *Phys. Rev.* B **51** 7046

[7] Wendler L and Haupt R 1987 *Phys. Status Solidi* b **143** 487

[8] Nkoma J S 1987 *Surf. Sci.* **191** 595

[9] Babiker M 1986 *J. Phys. C: Solid State Phys.* **19** L339

[10] Trallero-Giner C and Comas F 1988 *Phys. Rev.* B **37** 4583

[11] Ridley B K 1989 *Phys. Rev.* B **39** 5282

[12] Richter E and Strauch D 1987 *Solid State Commun.* **64** 867

[13] Ren Shang-Fen, Chu Hanyou and Chang Yia-Chung 1988 *Phys. Rev.* B **37** 8911

[14] Yip Sung-kit and Chang Yia-Chung 1984 *Phys. Rev.* B **30** 7037

[15] Tsuchiya T, Akera H and Ando T 1989 *Phys. Rev.* B **39** 6025

[16] Baroni S, Gianozzi P and Molinari E 1990 *Phys. Rev.* B **41** 3870

[17] Huang Kun and Zhu Bangfen 1988 *Phys. Rev. B* **38** 2083

[18] Liu Y and Inkson J C 1991 *Semicond. Sci. Technol.* **6** 335

[19] Weber G 1992 *Phys. Rev.* B **46** 16 171

[20] Bhatt A R, Kim K W, Stroscio M A and Higman J M 1993 *Phys. Rev.* B **48** 14 671

[21] Huang Kun and Zhu Bangfen 1988 *Phys. Rev. B* **38** 13 377

[22] Nash K J 1992 *Phys. Rev.* B **46** 7723

[23] Zhu Bangfen 1988 *Phys. Rev.* B **38** 7694

[24] Comas F and Trallero-Giner C 1993 *Physica* B **192** 394

[25] Chamberlain M P, Cardona M and Ridley B K 1993 *Phys. Rev.* B **48** 14 356

[26] Trallero-Giner C, Comas F and Garcia-Moliner F 1994 *Phys. Rev.* B **50** 1755

[27] Ridley B K, Al-Dossary O, Constantinou N C and Babiker M 1996 *Phys. Rev.* B **50** 11 701

[28] Zunke M, Schorer R, Abstreiter G, Klein W, Weimann G and Chamberlain M P 1995 *Solid State Commun.* **91** 847

[29] Enderlain R 1988 *Phys. Status Solidi* b **150** 85

[30] Hanke W 1978 *Adv. Phys.* **27** 287

[31] Sham L J 1969 *Phys. Rev.* B **188** 1431

[32] Vogl P 1978 *J. Phys. C: Solid State Phys.* **11** 251

[33] Balderschi A and Tosatti E 1979 *Solid State Commun.* **29** 131

[34] Tyuterev V G 1975 *Sov. Phys.–JETP* **40** 773

[35] Dimelow T and Smith S R P 1998 *Phys. Rev.* B **57** 3978

[36] Maradudin A A 1974 *Dynamical Properties of Solids* ed G K Horton and A A Maradudin (North-Holland: Amsterdam) pp 1–82

[37] Kovalev O V 1984 *Irreducible and Induced Representations and Co-Representations of Fedorov's Groups* (Moscow: Nauka)

[38] Foreman B A 1995 *Phys. Rev.* B **52** 12 241

[39] Kannelis G 1987 *Phys. Rev.* B **35** 746

[40] Miglio L and Colombo L 1990 *Superlatt. Microstruct.* **7** 139

[41] Grinyaev S N, Karavaev G F and Tyuterev V G 1996 *Physica* B **228** 319

[42] Kunc K, Balkanski M and Nusimovici M A 1975 *Phys. Status Solidi* b **72** 229

[43] Bechstedt F and Gerecke H 1989 *Phys. Status Solidi* b **156** 151