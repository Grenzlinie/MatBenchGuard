Electron-Hole Asymmetry Driven Surface Charge
Expulsion

Giang H. Bach¹

Received: 6 May 2015 / Accepted: 24 September 2015 / Published online: 1 October 2015
© Springer Science+Business Media New York 2015

Abstract We study an Ising-like dynamic Hubbard (IDHB) model using dynamical mean field theory with an embedding potential. The prominent characteristic of the IDHB model is the broken electron-hole symmetry. Our calculations indicate that the electron-hole asymmetry enhances electron expulsion toward the surface of a semi-infinite bulk. Since correlated hopping amplitude produces the electron-hole asymmetry, it strongly affects the electron expulsion toward the surface.

Keywords Dynamic Hubbard model · Electron-hole asymmetry · Dynamical mean field theory · Negative charge expulsion

## 1 Introduction
Dynamic Hubbard (DHB) models consist of models involving in the modification of atomic orbitals due to double occupancy, which produces the electron-hole asymmetry. A number of various contexts related to the DHB models have been described previously in many papers which were mostly paid attention to the bulk systems [1–3]. Ising-like dynamic Hubbard model (IDHB) is a simple model of which the Hamiltonian is presented by

$$
\begin{aligned}
H= & -\sum_{\langle i, j\rangle \sigma} t\left(c_{i \sigma}^{\dagger} c_{j \sigma}+h . c .\right)-\mu \sum_{i, \sigma} n_{i \sigma} \\
& +\sum_{i}\left(\omega_{0} \sigma_{i}^{x}+g \omega_{0} \sigma_{i}^{z}\right)+\sum_{i}\left(U-2 g \omega_{0} \sigma_{i}^{z}\right) n_{i \uparrow} n_{i \downarrow}.
\end{aligned}
\tag{1}
$$

⊗ Giang H. Bach
gianghuongbach@gmail.com

¹ Computational Material Science Lab, Faculty of Physics, Hanoi University of Science, Vietnam National University, 334 Nguyen Trai, Thanh Xuan, Hanoi, Vietnam

![](./images/814591772352053249_1.jpg)

The first and the second terms are, respectively, the hopping term between nearest neighbor sites and a chemical potential controlling the number of particles of the system in the thermodynamic limit. The last two terms show a competition between electrons paying a cost to have a higher energy level (the third term) and having a Coulomb potential reduction (the fourth term) by residing in the larger orbital. In other words, this model simplifies a two-orbital Hubbard model by considering only one orbital with variation of on-site interaction using an external pseudo-spin field $\sigma_z$ when sites are doubly occupied. IDHB model will then show similar properties of the two-orbital Hubbard model. For example, with both the IDHB and the two- band Hubbard model, it is also that the critical on-site Coulomb interaction $(U_c)$ for a Mott metal-insulator transition is also stronger than that with the single-band Hubbard model.

In the anti-adiabatic limit $\omega_0 \to \infty$, IDHB model modifies the Hubbard model with correlated hopping effective low energy Hamiltonian of which can be represented as follows [4]:

$$
\begin{aligned}
H_{\mathrm{cor}}= & -\sum_{\langle i j\rangle \sigma}\left(t-\mu \delta_{i j}\right)\left[\left(1-n_{i,-\sigma}\right)\left(1-n_{j,-\sigma}\right)+S\left(n_{i,-\sigma}+n_{j,-\sigma}-2 n_{i,-\sigma} n_{j,-\sigma}\right)\right. \\
& \left.+S^{2} n_{i,-\sigma} n_{j,-\sigma}\right]\left(c_{i \sigma}^{\dagger} c_{j \sigma}+h . c .\right)+U \sum_{i} n_{i \uparrow} n_{i \downarrow},
\end{aligned}
$$

where $S=1 / \sqrt{1+g^{2}}$ is the overlap of pseudo-spin background with and without the presence of two electrons on one site. The hopping amplitude in this model depends on the number of electrons on each site, which are $t$, bare hopping amplitude in a nearly empty band, $t S$ in a half-filled band, and $t S^{2}$ in a nearly filled band. It is clearly seen that this model describes the electron's movement under the influence of other electrons. Since it is always hard for holes to move when the lattice is crowded, the effective mass of holes should be greater than that of the electrons (quasi-particle weight of electrons decreases as band filling increases).

The effective Hamiltonian for holes in the nearly full band or in the low hole region is given by [5,6]:

$$
H_{\mathrm{eff}}=-\sum_{i j \sigma}\left[t S^{2}+\Delta t\left(\tilde{n}_{i,-\sigma}+\tilde{n}_{j,-\sigma}\right)\right]\left[\tilde{c}_{i \sigma}^{\dagger} \tilde{c}_{j \sigma}+h . c .\right]+U \sum_{i} \tilde{n}_{i \uparrow} \tilde{n}_{i \downarrow}, \quad(3)
$$

with $\Delta t=t S(1-S)$ and $\tilde{c}(\tilde{c}^{\dagger})$ the destruction (creation) hole operators.

This correlated hopping model supports the "theory of hole superconductivity" where holes superconduct due to kinetic energy lowering mechanism in the nearly full band. The key point of hole superconductors is the basic difference between holes and electrons in their effective mass and charge. This electron-hole asymmetry affects many important behaviors such as the Meissner effect [7] and the London moment which occurs [8] when a normal rotating metal is cooled into the superconducting state. It is shown that electrons move slower near the surface when it is in the superconducting state. Thus, an observation about negative charge expulsion toward the surface in the DHB models is completely consistent with these spontaneous slowing down electrons.

![](./images/814591772352053249_2.jpg)

It is worthy to note that the negative charge expulsion toward the surface is one of several essential features of DHB models.

Recently, Hirsch's paper has shown the existence of negative charge expulsion from the interior to the surface with the correlated hopping models which may cause inhomogeneity in many bulk systems [9]. Using self-consistent mean field theory in finite systems, he showed that the correlated hopping amplitude $\Delta t$ strongly increased the electron expulsion to the surface while Coulomb interaction had a tendency to reduce this effect. With an attempt to indirectly approach the surface of a semi-infinite bulk with this correlated hopping model, this paper examines the IDHB model in the anti-adiabatic limit using dynamical mean field theory (DMFT) with an embedding potential [10]. Through the addition of an embedding potential in the original Hamil- tonian, we succeeded in bringing the effect of the bulk part on the surface. This method leads to a substantial decrease in the time consumed for convergency, and hence, it can be effectively applied in studying the surface of strongly correlated electron models [11,12].

## 2 Model and Method

DMFT brings an opportunity to study the layer systems with strongly correlated inter- actions [13-16]. The common difficulty in the layer problems is that the convergent consuming time increases with the number of layers. Using an embedding potential [10] implying the bulk effects on the surface layers, the convergent time considerably reduces with only few layers. Therefore, the DMFT with an embedding potential is effectively applied to semi-infinite metals or hetero-structures with multi-bands.

In order to demonstrate how DMFT works for layer systems, we consider an IDHB cubic lattice bulk with $N$ surface layers on the top. Figure 1 sketches the structure of the layer system in which the bulk $(R)$ is connected to $N$ layers belonging to the surface part $(\Omega)$. The layer IDHB Hamiltonian is written as

![](./images/814591772352053249_3.jpg)

Fig. 1 A schematic diagram of $N$ top layers $(\Omega)$ connected to a bulk system $(\mathbf{R})$. $n=1$ is considered as the top most layer and $n=N$ is the adjacent layer to the bulk part

![](./images/814591772352053249_4.jpg)

$$
\begin{aligned}
H^{\Omega}= & -\sum_{\langle i \alpha, j \beta\rangle \sigma} t_{i \alpha, j \beta}\left(c_{i \alpha \sigma}^{\dagger} c_{j \beta \sigma}+\text { h.c. }\right)-\mu \sum_{i \alpha, \sigma} n_{i \alpha \sigma} \\
& +\sum_{i \alpha}\left(\omega_{0} \sigma_{i \alpha}^{x}+g \omega_{0} \sigma_{i \alpha}^{z}\right)+\sum_{i \alpha}\left(\mathrm{U}-2 g \omega_{0} \sigma_{i \alpha}^{z}\right) n_{i \alpha \uparrow} n_{i \alpha \downarrow},
\end{aligned}
$$

where $c_{i \alpha \sigma}^{\dagger}$ and $c_{i \alpha \sigma}$ are, respectively, creation and annihilation operators for an electron with spin $\sigma$ at site $\mathrm{i}$ in the $\alpha$ th layer. The hopping integral $t_{i \alpha, j \beta}$ between two nearest neighbor sites $\langle i, j\rangle$ on two adjacent layers $\langle\alpha, \beta\rangle$ is allowed to modify due to surface relaxation effects. The second term controls the filling number of the systems through the chemical potential $\mu$, and the free pseudo-spin energy in each layer is included in the third term. The electron-hole symmetry is broken by adding a pseudo-spin $\sigma_{i \alpha}^{z}$ to control the on-site Coulomb interaction in the $\alpha$ th layer . For further understanding the DHB models, the reader is referred to the previous work [17].

The Green function for the layer system is given by

$$
\mathbf{G}^{\Omega}\left(\mathbf{k}, i \omega_{n}\right)=\left[\left(i \omega_{n}+\mu\right) \mathbf{1}-\epsilon(\mathbf{k})-\mathbf{S}\left(\mathbf{k}, i \omega_{n}\right)-\Sigma^{\Omega}\left(i \omega_{n}\right)\right]^{-1},
$$

where $\mathbf{G}^{\Omega}\left(\mathbf{k}, i \omega_{n}\right)$ is a $N \times N$ square matrix; $\Sigma^{\Omega}\left(i \omega_{n}\right)$ is the layer self-energy matrix which does not depend on $\mathbf{k}$ in the frame work of single-site DMFT [18]. $\epsilon(\mathbf{k})$ is a $N \times N$ hopping matrix describing the translational symmetry in each layer perpendicular to $\mathrm{Oz}$ axis $\left(\epsilon_{\|}(\mathbf{k})\right)$ and the breaking translational symmetry along to $\mathrm{Oz}$ axis $\left(\epsilon_{\perp}\right)$. If we only consider the nearest inter-plane hopping and the nearest intra-plane hopping, $\epsilon(\mathbf{k})$ has a form of the tri-diagonal matrix which is [11,13]

$$
\epsilon(\mathbf{k})=\left(\begin{array}{ccccc}
t_{11} \epsilon_{\|}(\mathbf{k}) & t_{12} \epsilon_{\perp}(\mathbf{k}) & 0 & 0 & \ldots \\
t_{21} \epsilon_{\perp}(\mathbf{k}) & t_{22} \epsilon_{\|}(\mathbf{k}) & t_{23} \epsilon_{\perp}(\mathbf{k}) & 0 & \ldots \\
0 & t_{32} \epsilon_{\perp}(\mathbf{k}) & t_{33} \epsilon_{\|}(\mathbf{k}) & t_{34} \epsilon_{\perp}(\mathbf{k}) & \ldots \\
0 & 0 & \ldots & \ldots & \ldots,
\end{array}\right) .
$$

where $\epsilon_{\|}(\mathbf{k})=-2\left[\cos \left(\mathrm{k}_{\mathrm{x}}\right)+\cos \left(\mathrm{k}_{\mathrm{y}}\right)\right]$ and $\mid \epsilon_{\perp}(\mathbf{k}) \mid=1$. For simplicity, we take $t_{\alpha \alpha}=t_{\|}$and $t_{\alpha \beta}=t_{\perp}$ if $\alpha=\beta \pm 1$ The effect of the substrate on the surface is presented by an embedding potential matrix $\mathbf{S}(\mathbf{k}, i \omega)$, which is

$$
\mathbf{S}\left(\mathbf{k}, i \omega_{n}\right)=\mathbf{t}_{\mathbf{R}}^{\Omega} \mathbf{G}^{\mathbf{R}}(\mathbf{k}, i \omega) \mathbf{t}_{\mathbf{R}}^{\Omega},
$$

where $\mathbf{t}_{\mathbf{R}}^{\Omega}$ is a hopping matrix between $N$ surface layers and the substrate; $\mathbf{G}^{\mathbf{R}}(\mathbf{k}, i \omega)$ is the semi-infinite bulk Green function which is calculated as

$$
\mathbf{G}^{\mathbf{R}}\left(\mathbf{k}, i \omega_{n}\right)=\left[\left(i \omega_{n}+\mu\right) \mathbf{1}-\epsilon(\mathbf{k})-\Sigma^{\mathbf{R}}\left(i \omega_{n}\right)\right]^{-1},
$$

with $\Sigma^{R}\left(i \omega_{n}\right)$ the bulk self-energy. Since nearest neighbor hopping is taken into account in formula (7), only hopping amplitude between the last layer of the surface part ( $N$ th) and the substrate is non-zero, which is $t_{\perp}$. Therefore, the only non-vanishing element of the embedding potential is

![](./images/814591772352053249_5.jpg)

$$
S_{11}(\mathbf{k}, i \omega_{n})=t_{\perp}^{2} G_{11}^{R}(\mathbf{k}, i \omega_{n}), \tag{9}
$$

with $G_{11}^{R}(\mathbf{k}, i \omega_{n})$ the Green function of the top layer of the substrate, which is calculated using a recursive relation [19].

A standard layer-DMFT routine is carried out in the following steps: (i) perform a normal single-site DMFT process for the bulk substrate in order to get the bulk self-energy, which is used to define the embedding potential $S_{11}(\mathbf{k}, i \omega_{n})$; (ii) build an single-site Anderson impurity model for each layer in the $\Omega$ part, solve them by exact diagonalization and from that, obtain the layer self-energy elements $\Sigma_{\alpha \beta}(i \omega_{n}) = \Sigma_{\alpha}(i \omega_{n}) \delta_{\alpha \beta}$ of the matrix $\Sigma^{\Omega}(i \omega_{n})$, which is diagonal; (iii) put $S_{11}(\mathbf{k}, i \omega_{n})$, $\Sigma^{\Omega}(i \omega_{n})$ into formula (5) to find the $\mathbf{k}$-dependent layer Green function $\mathbf{G}^{\Omega}(\mathbf{k}, i \omega_{n})$ and the on-site layer Green function can be found by $G_{\alpha}(i \omega_{n}) = \sum_{\mathbf{k}} G_{\alpha \alpha}(\mathbf{k}, i \omega_{n})$; (iv) the DMFT self-consistency conditions imply a new choice for bath parameters which should satisfy $G_{\alpha}^{0}(i \omega_{n}) = [G_{\alpha}^{-1}(i \omega_{n})+\Sigma_{\alpha}(i \omega_{n})]^{-1}$. This routine is repeated until self-consistency is achieved. The following calculations have been performed for $n_{s}=6$ sites, where $n_{s}$ is the number of bath sites in the mapped single Anderson impurity Hamiltonian in the DMFT self-consistent routine. Our previous results have confirmed that $n_{s}=6$ is sufficient to produce self-consistent results [20].

## 3 Results and Discussion

### 3.1 Quasi-Particle Weight for a Bethe Lattice

Firstly, Fig. 2 shows the quasi-particle weight $Z$ as the function of electron filling n in the IDHB model in the anti-adiabatic limit $\omega_{0} \to \infty$ and in the Hubbard model with correlated hopping of which the quasi-particle weight is approximately described as follows [21]:

$$
Z=\left[1+(S-1) \frac{n}{2}\right]^{2}. \tag{10}
$$

We can see that the DMFT values precisely agree with the analytical results for $U=0$ at weak $g$ coupling, where the quasi-particle weight monotonically decreases

Fig. 2 Quasi-particle weight $Z$ dependence on electron filling for a Bethe lattice with different $g$ coupling values. Here we take $U=0, \omega_{0}=50$. The DMFT result (presented by points) is expectantly followed by the analytical ones (presented by lines) at small $g$ coupling constant or at low electron filling
(Color figure online)

![](./images/814591772352053249_6.jpg)

![](./images/814591772352053249_7.jpg)

with increasing number filling. Since the coupling constant $g$ is characteristic for the "quasi-particle dressing" effect caused by a pseudo-spin field, the larger the coupling constant, the smaller the quasi-particle weight. We can also see that because the quasi-particle weight is inversely proportional to the effective mass, holes are much heavier than electrons as suggested in the DHB models. Even though two-site DMFT is good enough to qualitatively produce the quasi-particle weight as confirmed in previous works [17], the increase of the number of bath sites leads to better quantitative results at stronger coupling ($g=1.5$), where the numerical calculation (circle dot) approaches to the appropriate value ($Z=S^{2}$ at $n=2$).

### 3.2 Surface Charge Occupation

In the following part, the surface calculations have been carried out with $N=5$ layers in the $\Sigma$ part. For simplicity, we take $t_{\perp}=t_{\|}=t$. In order to put the system into the anti-adiabatic limit, $\omega_{0}=50$ is taken below. It is worthwhile to mention that for a conventional Hubbard model, the charge density increases in the surface for all electron fillings above half-filling and behave oppositely below half-filling due to electron-hole symmetry [22], which refers to the charge transfer effect. Since the thermodynamic equilibrium requires a common chemical potential for both the surface and the bulk, above half-filling electrons will accumulate on the surface due to a narrower bandwidth of the surface. However, the DHB models describe different physics where the electron expulsion physics is associated with kinetic energy lowering.

Figure 3 shows the electron occupation in $N$ surface layers with different on-site Coulomb U in the case of bulk filling $n_{\mathrm{b}}=1.8$ (corresponding to 0.2 hole filling). We can see that the electron density mostly changes in the top layer and quickly converges to the bulk filling. It is also mentioned that Friedel oscillations observed in a finite system [9] are not clearly shown in our calculations. In fact, Friedel oscillations have been found in the DMFT calculations for a layer system without using an embedding potential. However, the number of layers is pretty large in order to get convergence ($N\approx25$) [23]. Using an embedding potential, we need fewer layers ($N=5$) to describe a semi-infinite layered system and thus, it is quite hard to observe surface oscillations.

Fig. 3 Electron density n as a function of layer index $j$ with different on-site Coulomb potential $U$. Here the bulk filling is $n_{\mathrm{b}}=1.8, g=1.5$ (Color figure online)

![](./images/814591772352053249_8.jpg)

![](./images/814591772352053249_9.jpg)

![](./images/814591772352053249_10.jpg)

Fig. 4 Kinetic energy (K.E.), potential energy (P.E.), pseudo-spin energy (Ps.E.), and total energy (T.E.) of the surface layers with $U=2$, $g=1.5$. Here the bulk filling is $n_{\text{b}}=1.8$ (Color figure online)

The effect of Coulomb interaction on compressing the electron density on the surface is consistent with previous calculations for the Hubbard models [10] as well as for the DHB models (see Fig. 6 in Ref. [1]) where double occupancy competes with hopping process. Obviously increasing the electron density on the surface above half-filling implies increasing surface double occupancy which must cost a Coulomb on-site energy.

The physics in the correlated hopping models emphasize the dependence of hop- ping amplitude on the number of electrons on that site where the hopping terms are correspondingly $t$, $tS$, and $tS^{2}$ if there are zero, one, or two electrons. In the nearly filled band, the hopping amplitude is much smaller than the one in the empty band due to $S<1$. When holes increase, kinetic energy will decrease. Thus, holes can take benefit from lowering kinetic energy in the bulk by pushing electrons to the surface, hence increasing kinetic energy in the surface. This argument is confirmed by Fig. 4, where the kinetic energy (K.E.), potential energy (P.E.), pseudo-spin energy (Ps.E.), and total energy (T.E.) of the surface layers are plotted in the case of $U=2$, $g=1.5$. Remember that K.E, P.E, Ps.E, and T.E are obtained as follows:

$$
\text{T.E.} = \text{K.E.} + \text{P.E.} + \text{Ps.E.} \tag{11}
$$

$$
\text{K.E.} = \sum_{\sigma,k=2}^{n_{s}} V_{k} \left\langle \psi_{0} | d_{\sigma}^{\dagger}a_{k\sigma} + h.c. | \psi_{0} \right\rangle \tag{12}
$$

$$
\text{P.E.} = \left\langle \psi_{0} | (U - 2g\omega_{0}\sigma_{z})n_{d\uparrow}n_{d\downarrow} | \psi_{0} \right\rangle \tag{13}
$$

$$
\text{Ps.E.} = \omega_{0} \left\langle \psi_{0} | \sigma_{x} | \psi_{0} \right\rangle + g\omega_{0} \left\langle \psi_{0} | \sigma_{z} | \psi_{0} \right\rangle, \tag{14}
$$

where these expectation values of energy are taken on the ground state $|\psi_{0}>$ of the mapped single-impurity Anderson model in the normal convergency DMFT routine [20]. It is worthy to note that the variation with electron filling of pseudo-spin energy and potential energy is oppositely behaved. This reflects the two-band physics of the

![](./images/814591772352053249_11.jpg)

Fig. 5 Electron density as a
function of layer index $j$ with
different $g$ coupling constant.
Here the bulk filling $n_{\mathrm{b}}=1.8$,
$U=0$ (Color figure online)

![](./images/814591772352053249_12.jpg)

Table 1 The $g$-dependence of
$\Delta t$, $\Delta t_{\mathrm{c}}$ in the anti-adiabatic
limit

<table>
<thead>
<tr>
<th>$g$</th>
<th>$tS^{2}$</th>
<th>$\Delta t=t(S-S^{2})$</th>
<th>$\Delta t/tS^{2}$</th>
<th>$\Delta t_{\mathrm{c}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.5</td>
<td>0.8</td>
<td>0.09</td>
<td>0.11</td>
<td>0.57</td>
</tr>
<tr>
<td>1.0</td>
<td>0.5</td>
<td>0.21</td>
<td>0.42</td>
<td>0.35</td>
</tr>
<tr>
<td>1.5</td>
<td>0.31</td>
<td>0.25</td>
<td>0.81</td>
<td>0.22</td>
</tr>
</tbody>
</table>

systems, which means that in order to reduce the potential on the same site, electrons need energy for transitions to higher bands here modeled by an excitation correspond- ing to the pseudo-spin energy. The other remark as expected is that the variation of total energy has the same form as the layer dependence of kinetic energy, where kinetic energy of the layers close to the bulk is lower than that of the top most layer.

Figure 5 shows the effect of coupling constant $g$ on the electron density of each surface layer with $U=0$. The increase of electron concentration in the top most layer is observed for all coupling $g$. Table 1 shows that when $g$ increases from 0.5 to $1.5, tS^{2}$ decreases and $\Delta t$ increases. The larger $\Delta t$ seemingly enhances electron expulsion from the interior to the top surface, whereas the reduced $tS^{2}$ partly prevents this expulsion. However, the proportional dependence of the ratio of $\Delta t/tS^{2}$ (see Table 1) on coupling constant $g$ emphasizes the key role of $\Delta t$ on enhancing electron expulsion toward the surface which agrees well with Ref. [9] (see Fig. 3). We observe that a small increase of $\Delta t/tS^{2}$ can strongly affect this process. It is also suggested that $\Delta t$ can drive a phase separation into hole-rich and hole-poor regions due to surface charge expulsion if the correlated hopping amplitude approaches a critical value $\Delta t_{c}$:

$$
\Delta t_{\mathrm{c}}=\frac{t S^{2}+U /(2 z)}{2\left(1-\frac{3}{2} n_{\mathrm{h}}\right)} \tag{15}
$$

with $z$ the number of nearest neighbors, $n_{\mathrm{h}}$ the hole density. For the parameters in Fig. $5, n_{\mathrm{h}}=0.2$, the critical correlated hopping amplitude $\Delta t_{c}$ is proportional to $t S^{2}$, and thus, negative charge expulsion is strongly observed in the top surface with the larger $\Delta t$.

The effect of $g$ coupling on the surface charge expulsion is also examined with different bulk fillings as shown in Fig. 6, where difference between electron density

![](./images/814591772352053249_13.jpg)

Fig. 6 Electron density
difference between the top most
layer $n_1$ and the bulk with
different bulk fillings $n_{\rm b}$ in the
cases of $g=0.5$ (solid line) and
$g=1.5$ (dot line) (Color figure
online)

![](./images/814591772352053249_14.jpg)

on the top most layer and the bulk is drawn versus bulk filling. It is clearly seen that
the effect is more pronounced with stronger coupling in all bulk filling cases and the
maximum of $\delta n_1$ occurs at a lower bulk filling in the stronger coupling case.

## 4 Conclusions

IDHB model is the simplest version of dynamic Hubbard models where an auxiliary
spin-$\frac{1}{2}$ degree of freedom is coupled to electronic states to switch between two orbitals
with and without doubly occupied electrons. As a member of DHB models, this model
also emphasizes on electron–hole asymmetry where holes are much heavier than elec-
trons so that in the low hole concentration region, holes are expected to bind as Cooper
pairs to lower their kinetic energy then superconduct (theory of hole superconductors).
With this expectation, holes will tend to concentrate in the interior in contrast with
larger electron concentration in the surface because hole will take benefit of lowering
the kinetic energy in the inner part with more degrees of freedom than that of the
surface. It is straight forward to understand that the kinetic energy decreases when
the hole concentration increases in the correlated hopping model where the hopping
amplitude depends on site occupation number. Fortunately, the IDHB model can give
rise to the correlated hopping model in the anti-adiabatic limit $\omega_0 \to \infty$.

In summary, our results showed that electrons are expelled from the interior onto
the top most layer of the surface, which is consistent with remarks concluded in the
correlated hopping model [9] for a finite system. The correlated hopping term $\Delta t$ can
strongly enhance this electron expulsion process and this observation is one of the key
features of the DHB models.

Acknowledgments The author thank Dr. Reza Nourafkan and Dr. Frank Marsiglio for their useful
advice. This work is funded by the Vietnam National Foundation for Science and Technology Development
(NAFOSTED) under the Grant Number 103.02-2012.73

## References

1. J.E. Hirsch, Dynamic Hubbard model. Phys. Rev. Lett. 87, 206402–4 (2001)
2. J.E. Hirsch, Why holes are not like electrons: a microscopic analysis of the differences between holes
and electrons in condensed matter. Phys. Rev. B 65, 184502–184520 (2002)

![](./images/814591772352053249_15.jpg)

3. J.E. Hirsch, Dynamic Hubbard model for solid with hydrogen-like atoms. Phys. Rev. B **90**, 104501–104509 (2014)

4. J.E. Hirsch, Quantum Monte Carlo and exact diagonalization study of a dynamic Hubbard model. Phys. Rev. B **65**, 214510–214516 (2002)

5. J.E. Hirsch, F. Marsiglio, Superconducting state in an oxygen hole metal. Phys. Rev. B **39**, 11515–11525 (1989)

6. J.E. Hirsch, F. Marsiglio, Hole superconductivity: review and some new results. Phys. C **162–164**, 591 (1989)

7. J.E. Hirsch, The origin of the Meissner effect in new and old superconductor. Phys. Scr. **85**, 035704 (2012)

8. J.E. Hirsch, The London moment: what a rotating superconductor reveals about superconductivity. Phys. Scr. **89**, 015806–015810 (2014)

9. J.E. Hirsch, Charge expulsion, charge inhomogeneity and phase separation in dynamic Hubbard mod- els. Phys. Rev. B **87**, 184506–184512 (2013)

10. H. Ishida, A. Liebsch, Embedding approach for dynamical mean field theory of strongly correlated heterostructures. Phys. Rev. B **79**, 045130–045138 (2009)

11. R. Nourafkan, F. Marsiglio, M. Capone, Metallic surface of a bipolaronic insulator. Phys. Rev. B **82**, 115127–115136 (2010)

12. R. Nourafkan, F. Marsiglio, Competition between reduced delocalization and charge transfer effects for a two-band Hubbard model. Phys. Rev. B **84**, 075133–075135 (2011)

13. M. Potthoff, W. Nolting, Surface metal-insulator transition in the Hubbard model. Phys. Rev. B **59**, 2549–2555 (1999)

14. M. Potthoff, W. Nolting, Metallic surface of a Mott insulator-Mott insulating surface of a metal. Phys. Rev. B **60**, 7834–7849 (1999)

15. S. Schwieger, M. Potthoff, W. Nolting, Correlation and surface effect in vanadium oxides. Phys. Rev. B **67**, 165408–165417 (2003)

16. J.K. Freericks, Dynamical mean field theory for strongly correlated inhomogeneous multilayered nanostructures. Phys. Rev. B **70**, 195342–195414 (2004)

17. G.H. Bach, J.E. Hirsch, F. Marsiglio, Two-site dynamical mean field theory for the dynamic Hubbard model. Phys. Rev. B **82**, 155122–155213 (2010)

18. G. Georges, G. Kotliar, K. Krauth, M.J. Rozenberg, Dynamical mean field theory of strongly correlated fermion systems and the limit of infinite dimensions. Rev. Mod. Phys. **68**, 13 (1996)

19. D. Kalkstein, P. Soven, A Green’s function theory of surface states. Surf. Sci. **26**, 85 (1971)

20. B. Giang, Dynamical mean field theory for the dynamic Hubbard model, Ph.D. thesis, chapter 6, 2011

21. J.E. Hirsch, Quasiparticle undressing in a dynamic Hubbard model: exact diagonalization study. Phys. Rev. B **66**, 064507–064512 (2002)

22. R. Nourafkan, F. Marsiglio, Surface effects in doping a Mott insulator. Phys. Rev. B **83**, 155116–155117 (2001)

23. M. Potthoff, W. Nolting, Metallic surface of a Mott insulator-Mott insulating surface of a metal. Phys. Rev. B **60**, 7834–7849 (1999)

![](./images/814591772352053249_16.jpg)