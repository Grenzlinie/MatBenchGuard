**MICROSCOPIC THEORY OF SURFACE DIELECTRIC RESPONSE IN A LOCAL REPRESENTATION**

C.H. Wu and W. Hanke

Max-Planck-Institut für Festkörperforschung, Stuttgart, BRD

(Received 10 May 1977 by M. Cardona)

We give a formulation of surface dielectric response in a local LCAO or Wannier representation. It is shown that this representation allows for a practical solution of the response integral equation and thus makes possible an explicit and self-consistent calculation of the nonlocal RPA response function $\epsilon^{-1}$. The formulation takes into account lattice potential effects and is therefore particularly suited for investigations of surface dielectric response and screening in transition metals, semiconductors and insulators. We present model calculations of charge densities induced in a metal thin film by localized perturbations in the surface region. It is demonstrated that "surface effects", resulting from differences in the effective atomic potential for different layers, must be included in the calculations of surface response in systems with tightly bound electrons.

THE DIELECTRIC RESPONSE of a surface to some perturbing potential plays an important role in a number of surface phenomena. Thus the interaction energy between an ion a short distance outside the surface and the induced charge density contributes to the energy of ionic and polar chemisorption and enters the energetics of field evaporation and desorption [1]. The adsorbate ions and their induced charge constitute a dipole layer which produces a change in work function [2]. From the poles of the response function one gains information about surface elementary excitations. The density-response function is also a key quantity for calculating exchange and correlation and is therefore of importance for the surface energy [3].

There exist already numerous calculations of the screening properties of metal surfaces, practically all assuming the "jellium" model [4]. Due to the neglect of lattice-potential effects this model is justified only for surfaces of simple metals.

In the present manuscript the wavevector- and frequency-dependent dielectric response of two plane parallel surfaces is formulated with emphasis on systems for which the localization properties of electronic wavefunctions become important, like transition-metal and semiconductor surfaces. A few attempts have already been directed towards a calculation of the surface polarizability $\tilde{\chi}$ including lattice-potential effects [5,6], but here the self-consistency problem, i.e. the inversion problem of the nonlocal dielectric function $\epsilon$, has not been solved. In the following it is shown that an LCAO or Wannier representation allows for a practical solution of the RPA response integral equation and thus makes possible an explicit calculation of the surface response function $\epsilon^{-1}$, fully including lattice-potential effects, i.e. local-field and surface-state effects. We present a model tight-binding calculation of the density-response function in a metal with $s$-type electrons. On the basis of this simple model we investigate in particular the influence of surface-state effects on the profiles of charge distributions induced by various external potentials. These effects, which are not included in the jellium model, are shown to play a significant role in the surface dielectric response of systems with more or less tightly bound electrons.

The inverse dielectric function $\epsilon^{-1}$ is determined by the integral equation
$$
\epsilon^{-1}=\delta+v \tilde{\chi} \epsilon^{-1} \tag{1}
$$
where $\delta$ is the Dirac-delta function, $v$ the Coulomb interaction and $\tilde{\chi}$ the proper polarization part. The term $v \tilde{\chi} \epsilon^{-1}$ is understood to be integrated over coordinates.

In a system with a surface which we take parallel to the $(x,y)$-plane, the non-local polarizability in the time-dependent Hartree or random-phase approximation (RPA) can be written as [7]
$$
\begin{aligned}
\tilde{\chi}_{\omega} & (\mathbf{q}+\mathbf{G}, \mathbf{q}+\mathbf{G}^{\prime} ; z, z^{\prime}) \\
& =\frac{1}{V} \sum_{\mathbf{k}, k_{Z}, k_{Z}^{\prime}} \frac{f\left(\mathbf{k}, k_{Z}\right)-f\left(\mathbf{k}+\mathbf{q}, k_{Z}^{\prime}\right)}{E\left(\mathbf{k}, k_{Z}\right)-E\left(\mathbf{k}+\mathbf{q}, k_{Z}^{\prime}\right)+\omega} \\
& \times \int \psi_{\mathbf{k}, k_{Z}}^{*}(r) e^{-i(\mathbf{q}+\mathbf{G}) \mathbf{r}} \psi_{\mathbf{k}+\mathbf{q}, k_{Z}^{\prime}}(r) \mathrm{d}^{2} r \\
& \times \int \psi_{\mathbf{k}+\mathbf{q}, k_{Z}}^{*}\left(r^{\prime}\right) e^{i\left(\mathbf{q}+\mathbf{G}^{\prime}\right) \mathbf{r}^{\prime}} \psi_{\mathbf{k}, k_{Z}^{\prime}}\left(r^{\prime}\right) \mathrm{d}^{2} r^{\prime}
\end{aligned} \tag{2}
$$


where, $V$ is the area in $(x,y)$ plane, $\psi$, $E$, and $f$ denote wave functions energies and occupation numbers of electronic states. $r$ with $r=(r,z)$, $\mathbf{K}$, $\mathbf{q}$ and $\mathbf{G}$ are two-dimensional vectors with $\mathbf{G}$ being a reciprocal lattice vector. Assuming translational invariance in the surface plane, i.e. neglecting local-field or lattice-periodicity effects, corresponds to diagonal $\mathbf{G}=\mathbf{G}'$ in equation (2).

In the representation of the two-dimensional Fourier transform, of equation (2), we are left with an extremely complicated mixed infinitesimal matrix (in $\mathbf{G}$ and $\mathbf{G}'$) and integral (in $z$ and $z'$) equation (1). We tackle the difficult problem of solving this integral equation in a tight-binding or Wannier representation, like we did in the bulk case [8]. For simplicity of notation let us take a one-orbital model. The multi-orbital case appropriate to a transition metal or to a semiconductor is a straightforward extension. We then expand the wave functions of a film with $N$ layers in LCAO's or Wannier functions $a$ as

$$
\psi_{\mathbf{k}, k_{Z}}(r)=\frac{1}{(N M)^{1 / 2}} \sum_{n=0}^{N-1} \sum_{\boldsymbol{R}} c_{n}\left(\mathbf{k}, k_{Z}\right) \mathrm{e}^{i \mathbf{k} \cdot \mathbf{R}} a(r-R)
\tag{3}
$$

where $\mathbf{R}=[\mathbf{R}, R_{Z}(n)]$. $M$ is the number of two-dimensional unit cells. With the help of this expansion, the polarizability can be written in the factorized form

$$
\begin{aligned}
& \tilde{\chi}_{\omega}\left(\mathbf{q}+\mathbf{G}, \mathbf{q}+\mathbf{G}^{\prime} ; z, z^{\prime}\right) \\
& \quad=\sum_{\boldsymbol{s} \boldsymbol{s}^{\prime}} A_{\boldsymbol{s}}(\mathbf{q}+\mathbf{G} ; z) N_{\boldsymbol{s} \boldsymbol{s}^{\prime}}(\mathbf{q} ; \omega) A_{\boldsymbol{s}^{\prime}}^{*}\left(\mathbf{q}+\mathbf{G}^{\prime} ; z^{\prime}\right)
\tag{4}
\end{aligned}
$$

where $A_{s}$ is a form factor for a generalized density wave, defined as

$$
\begin{aligned}
& A_{\boldsymbol{s}}(\mathbf{q}+\mathbf{G} ; z)=\int a^{*}\left(\mathbf{r} ; z-\tilde{R}_{Z}\right) \mathrm{e}^{-i(\mathbf{q}+\mathbf{G}) \mathbf{r}} \\
& \quad \times a\left(\mathbf{r}-\mathbf{R} ; z-R_{Z}\right) \mathrm{d}^{2} \mathbf{r}
\tag{5}
\end{aligned}
$$

with the index $s$ short for $(\mathbf{R}, \tilde{R}_{Z}, R_{Z})$. $N$ is the polarizability of the charge-density wave $s$ induced by the wave wave $s'$. The separable form both in $(\mathbf{G}, \mathbf{G}')$ and in $(z,z')$ of $\tilde{\chi}$, and therefore of the kernel in equation (1), enables this equation to be solved

$$
\begin{aligned}
& \epsilon_{\omega}^{-1}\left(\mathbf{q}+\mathbf{G}, \mathbf{q}+\mathbf{G}^{\prime} ; z, z^{\prime}\right)=\delta_{\mathbf{G G}^{\prime}} \delta\left(z-z^{\prime}\right) \\
& +\int v\left(\mathbf{q}+\mathbf{G} ;\left|z-z^{\prime \prime}\right|\right) \chi_{\omega}\left(\mathbf{q}+\mathbf{G}, \mathbf{q}+\mathbf{G}^{\prime} ; z^{\prime \prime}-z^{\prime}\right) \mathrm{d} z^{\prime \prime} .(6)
\end{aligned}
$$

With the density-response function $\chi$ given by

$$
\begin{aligned}
& \chi_{\omega}\left(\mathbf{q}+\mathbf{G}, \mathbf{q}+\mathbf{G}^{\prime} ; z, z^{\prime}\right) \\
& \quad=\sum_{\boldsymbol{s} \boldsymbol{s}^{\prime}} A_{\boldsymbol{s}}(\mathbf{q}+\mathbf{G} ; z) S_{\boldsymbol{s} \boldsymbol{s}^{\prime}}^{-1}(\mathbf{q} ; \omega) A_{\boldsymbol{s}^{\prime}}^{*}\left(\mathbf{q}+\mathbf{G}^{\prime} ; z^{\prime}\right)
\tag{7}
\end{aligned}
$$

where $S^{-1}=(N^{-1}-V)=N(1-V N)^{-1}$, and

$$
\begin{aligned}
& V_{\boldsymbol{s} \boldsymbol{s}^{\prime}}(\mathbf{q})=\sum_{\mathbf{G}} \iint A_{\boldsymbol{s}}^{*}(\mathbf{q}+\mathbf{G} ; z) v\left(\mathbf{q}+\mathbf{G} ;\left|z-z^{\prime}\right|\right) \\
& \quad \times A_{\boldsymbol{s}^{\prime}}\left(\mathbf{q}+\mathbf{G} ; z^{\prime}\right) \mathrm{d} z \mathrm{~d} z^{\prime}
\tag{8}
\end{aligned}
$$

$v(\mathbf{q}+\mathbf{G},|z-z'|)$ is the two-dimensional Fourier transform of the Coulomb interaction.

Equations (6) and (7) fully take into account the nonlocality introduced by the surface as well as the periodicity (local-field) effects in the surface plane. The iterative summation over the Coulomb interaction between electron-hole pairs in the self-consistent response problem is performed explicitly in the density-interaction matrix $V_{\boldsymbol{s s}'}$ of equation (8). The nonlocality due to the surface manifests itself in the $\tilde{R}_{z}$ - and $R_{z}$ - dependence of the matrix index $s$ which determines the size of the matrix $S_{ss'}$ to be inverted. If the Wannier functions are well-localized it is clear that the number of components $\tilde{R}_{z}$ being different from the components $R_{z}$ as well as the number of vectors $\mathbf{R}$ generating the index $s$ are greatly reduced. Thus, in this case, the dimension of the matrix $S$ is essentially determined by the number of layers $N$ times a small overlap factor. Since we expect the surface dielectric response of thin films to rapidly approach the response of the semi-infinite system (this is also demonstrated in the following 8- and 16-layer model calculation) we have a practical scheme for calculating the density response of a general surface system.

In order to demonstrate the characteristic features of the surface dielectric response in a system with localized electronic states we choose a simple model of a (001) surface of an f.c.c. metal. We take a one-orbital model of $s$-type symmetry and assume the overlap in the Hamiltonian matrix elements to be confined to nearest neighbors. The Wannier functions $a_{s}=a_{s}\{r-[\mathbf{R}, R(n)]\}$ of the surface layers $n=0$ and $n=N-1$, are allowed to be different from the rest, denoted by $a$.

To determine the coefficients $c$ and the energies $E$ we substitute the expansion, equation (3), into the one-particle Schrödinger equation, and write the resulting $N$ linear equations as

$$
\sum_{n^{\prime}=0}^{N-1} M_{n n^{\prime}} c_{n^{\prime}}\left(\mathbf{k}, \mathbf{k}_{Z}\right)=0.
\tag{8}
$$

In the spirit of the so-called defect-matrix method [9] the $(N \times N)$ matrix $M$ is decomposed into $M=M_{0}+\delta M$. $M_{0}$ corresponds to the $N$-layer system with periodic boundary conditions, and $\delta M$ to the perturbation introduced by (a) the change of the number of nearest-neighbor overlap matrix elements involving Wannier functions of the $n=0$ and $n=N-1$ layers and (b) the deviation of these surface matrix elements from the bulk matrix elements. The energies $E(\mathbf{k}, k_{Z})$ and expansion

![](./images/812446750798249984_1.jpg)

Fig. 1. Charge density $\rho^{\text{ind}}(\mathbf{q}, z)=\rho^{\text{ind}}(z)$, for fixed $\mathbf{q}(q_{x}=\pi/32)$ induced by $V_{\text{ext}}(r)=\delta[z-R_{Z}(n)]\text{e}^{-i\boldsymbol{q}\cdot\boldsymbol{r}}$ for (a) $n=0$; i.e. perturbation localized in first surface layer and (b) $n=1$; i.e. perturbation in second layer. The dashed curves denote the calculations with geometrical effect only. Full curves correspond to geometrical plus surface effect.

coefficients $c_{n}(\mathbf{k}, k_{Z})$ are determined by the corresponding secular equation. In our model the perturbation $\delta M$ can be expressed in terms of two-dimensionaless parameters $\eta$ and $\zeta$ which are a measure for the deviation of surface overlap from bulk overlap and which are defined as
$$\zeta=1-\left\langle a_{s}|H| a^{\prime}\right\rangle /\left\langle a|H| a^{\prime}\right\rangle,\qquad(9)$$
and
$$\begin{aligned}
\eta & =\frac{\langle a|H| a\rangle-E+4\left\langle a|H| a^{\prime}\right\rangle \cos \left(k_{x}\right) \cos \left(k_{y}\right)}{\left\langle a|H| a^{\prime}\right\rangle\left[2 \cos \left(k_{x}\right)+2 \cos \left(k_{y}\right)\right]} \\
& -\frac{\left\langle a_{s}|H| a_{s}\right\rangle-E+4\left\langle a_{s}|H| a_{s}^{\prime}\right\rangle \cos \left(k_{x}\right) \cos \left(k_{y}\right)}{\left\langle a_{s}|H| a^{\prime}\right\rangle\left[2 \cos \left(k_{x}\right)+2 \cos \left(k_{y}\right)\right]}. \quad(10)
\end{aligned}$$

The prime in the overlap matrix elements denotes nearest-neighbor interactions. The coefficients $c_{n}(n=1,\dots,N-2)$, then can be found to be
$$\begin{aligned}
c_{n} & =c_{n=0}\left\{\sin \left[k_{Z}(n+1)\right]+\eta \sin \left(k_{Z} n\right)\right. \\
& \left.+\zeta \sin \left[k_{Z}(n-1)\right]\right\} \sin k_{Z}
\end{aligned}\qquad(11)$$
where $c_{n=0}=\pm c_{n=N-1}$. The possible $N$ values of $k_{Z}$ are determined by
$$\begin{gathered}
\exp \left[i\left(\frac{N+1}{2}\right) k_{Z}\right]+\eta \exp \left[i\left(\frac{N-1}{2}\right) k_{Z}\right] \\
+\zeta \exp \left[i\left(\frac{N-3}{2}\right) k_{Z}\right]=0.
\end{gathered}\qquad(12)$$

Thus, if the "surface-state" parameters $\eta$ and $\zeta$ are different from zero, $k_{Z}$ can be imaginary and the coefficients $c_{n}$ take an exponential decaying form corresponding to a surface state. In the $N\to\infty$ limit the $(N-2)$ energy roots $E(k_{Z})$ contained in (12) differ from that of the $N$ layer periodic system by $O(1/N)$. The other two energy roots become identical and have imaginary $k_{Z}$.

We use the energies and wave functions of this tight-binding description to calculate the density response of a metal thin film. To get some insight into the role played by localized electronic states, and to simultaneously keep the computational effort under control, a simplified model of a transition metal is assumed where only $d$-band effects are taken into account in evaluating $\tilde{\chi}$ of equation (4). The angular dependence is neglected and the five $d$ wave functions are linearly combined so as to form an $(m=0)$ $s$ state. The lattice constant, overlap and atomic orbital parameters are adjusted to simulate the surface and bulk situation encountered in Ni. We consider a half-filled band of width $W=4.35$ (eV) [10] which results in the value for $\langle a|H| a^{\prime}\rangle=-0.272$ (eV). (The zero of energy is taken such that $\langle a|H| a\rangle=0$.) For the localized atomic orbitals $a(r-R)$ a one-Gaussian model is used with a decay parameter $\alpha=0.27$. The surface effect, i.e. change of atomic potential and orbital behaviour in the surface layers, is rather difficult to estimate without detailed information from first-principle calculations [10]. We presume, following the renormalized atom picture for metal surfaces [11], less compression of charge and therefore a smaller decay parameter $\alpha$ for orbitals of the surface layers: the approximate value of one-third of the surface of the atomic cell that encounters no neighbors, and thus suffers no charge compression across it, gives an estimate for $\alpha_{s}$ with $\alpha_{s}=0.21$ in a.u. In the parameters $\zeta$ and $\eta$ we take only "diagonal" surface effects into account, i.e. we assume only the on-site matrix element $\langle a_{s}|H| a_{s}\rangle$ changed from its bulk value. Following again the renormalized-atom approach we expect for the $m=0$ combination of $d$-type electronic wave functions, a reduction of $\langle a|H| a\rangle$ on the surface site by somewhat less than one-third the difference between the bulk mean $d$-band position and the atomic $d$-level, resulting (for the special case of Ni) in $\langle a_{s}|H| a_{s}\rangle=\langle a|H| a\rangle-0.68$ (eV) [10]. In the calculation of the density matrix elements $A_{s}$ only one-site overlap

is included, having found nearest-neighbor contribution (with the above $\alpha$ and $\alpha_{s}$) to give $\sim 10\%$ corrections to $\epsilon^{-1}$.

The dimension of the matrices $N$, $V$ and $S$ is then identical with the number of layers. The $\mathbf{k}$-summation in the polarizability matrix $N$ was done by numerical integration, dividing the 2-D Brillouin zone in small squares of width $1/256$ in reduced units.

The results of our calculation of the profiles of the charge density $\rho^{\text{ind}}$ induced in an 8-layer film by an external perturbation of the form
$$
V_{\text{ext}}(r)=V_{\text{ext}}(z) e^{i \mathbf{q} \cdot \mathbf{r}} \tag{13}
$$
which is localized in the $z$-direction [$V_{\text{ext}}(z)=$ $\delta(z-R_{z})$] are plotted in Fig. 1(a) corresponds to $R_{z}(n=0)$, i.e. localization in the first surface plane and (b) to $R_{z}(n=1)$, i.e. localization in the second plane. The dashed curve gives the results $\rho^{\text{ind}}$ when only geometrical effects due to cut-off of overlap matrix elements are considered while the full curve gives $\rho^{\text{ind}}$ for geometrical plus surface effects. We have also calculated the corresponding $\rho^{\text{ind}}$ in a 16-layer film. On the scale of Fig. 1. the results are practically identical with the 8-layer results. This demonstrates that there is in fact a rapid convergence of the response of thin films to that of the semi-infinite limit, at least for a localized electronic system. Figure 1 shows that the induced density for the geometrical case is reduced to a large extent in the surface region when the localized perturbation moves from the $(n=1)$ plane to the surface layer $(n=0)$.

Thus, as one expects, the screening is reduced in the surface region. It is important to note that $\rho^{\text{ind}}$ is even more reduced when surface-state effects are taken additionally into account. The quite significant change in the surface density profiles due to the inclusion of these effects becomes of course smaller for positions inside the film. In view of our simple model we certainly cannot claim to have calculated the absolute magnitude of this change. Nevertheless we believe that our results quite generally demonstrate the importance of the surface effect in the density response of a surface system with localized electrons. This effect should for example, be of similar importance for the screening of point-charges in the surface region. It should also affect the interaction energy between an ion a short distance outside the surface and its induced charge density, and thus questions of chemisorption.

In summary, we have given a formulation of the surface dielectric response in a local representation. It has been shown that this representation allows for an explicit and self-consistent calculation of the non-local RPA response function $\epsilon^{-1}$, fully taking into account lattice-potential effects. Thus the formulation is particularly suited for investigations of surface response and screening properties in transition metals, semiconductors and insulators. A simple model calculation of the charge density induced by a localized external perturbation has shown the importance of surface-state effects.

## REFERENCES

1. See, for example, "Interaction on Metal Surfaces" in *Topics in Applied Physics* (Edited by GOMER R.). Springer, Berlin (1975).

2. LANG N.D., *Phys. Rev.* B4, 4234 (1971).

3. HARRIS J. & JONES R.O., *J. Phys. F: Metal Phys.* 4, 1170 (1974).

4. YING S.C., SMITH J.R. & KOHN W., *Phys. Rev.* B11, 1483 (1975) and references therein.

5. ZEYHER R., BIRMAN J.L. & BRENIG W., *Phys. Rev.* B6, 4613 (1972).

6. HYZHNYAKOV V.V., MARADUDIN A.A. & MILLS D.L., *Phys. Rev.* B11, 3149 (1975).

7. NEWNS D.M., *Phys. Rev.* B1, 3304 (1970).

8. HANKE W. & SHAM L.J., *Phys. Rev.* B12, 4501 (1975).

9. MONTROLL E.W., *J. Phys. Chem. Solids* 34, 567 (1973).

10. BOHNEN K.P. & GASPARD J.P., *Z. Phys.* (to be published).

11. FULDE P., LUTHER A. & WATSON R.E., *Phys. Rev.* B8, 440 (1973).