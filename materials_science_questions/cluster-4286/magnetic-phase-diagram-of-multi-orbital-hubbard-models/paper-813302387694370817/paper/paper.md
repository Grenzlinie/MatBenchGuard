# Antiferromagnetism in the Hubbard model

G. I. Mironov

Mari State Pedagogical Institute, 424002 Ioshkar-Ola, Russia
(Submitted January 5, 1997)
Fiz. Tverd. Tela (St. Petersburg) **39**, 1594–1599 (September 1997)

The energy spectrum of the two-sublattice Hubbard model is obtained in the static-fluctuation approximation. It is shown how the structure of the energy spectrum is modified as the parameters of the Hubbard model are varied. The ground state of the simple Hubbard model of dimension $d=2$ is the dielectric antiferromagnetic state. The author derives a consistency equation for the magnetization, which has an antiferromagnetic solution. © 1997 American Institute of Physics. [S1063-7834(97)01909-6]

Considerable attention has been devoted to the Hubbard model near half-filling in connection with the subject of high-temperature superconductors. $^{1,2}$ It is especially important to determine the spectrum of elementary excitations, because this information would provide the means for answering questions about which state in the Hubbard model is the ground state, how magnetic crossover actually takes place as the temperature varies, how the temperature and other parameters of the system influence the Mott transition, and how the structure of the electron spectrum changes as the temperature varies. Answers to these questions were obtained almost three decades ago $^{3}$ for the Hubbard model with dimension $d=1$, whereas in the case $d\geqslant 2$ there are virtually no known answers to any of the questions. More recently, the most significant progress has been made in the infinite-dimensional case $d=\infty$ (see, e.g., the survey in Ref. 2), where the Hubbard model essentially reduces to the Anderson model with specially chosen parameters, which has known solutions. However, the extension of the results of the investigation for $d=\infty$ to the case of finite $d\geqslant 2$ is far from trivial. On the other hand, in the limit $d=\infty$ the mean-field theory involves consistency equations that require a large amount of numerical computations. Consequently, there is a pressing need to develop analytical methods for solving the Hubbard model within manageable error limits.

Loskutov *et al.*$^{4}$ have developed a procedure for solving the Hubbard model in the static fluctuation approximation. The objective of the present study is to further elaborate this procedure and apply it to the two-sublattice Hubbard model. From the treatment in Ref. 4 we generalize the Hubbard Hamiltonian$^{5}$ to the case of two sublattices A and C as follows:

$$
H=H_{0}+V, \tag{1}
$$

$$
H_{0}=\sum_{\sigma,f}\varepsilon_{1}n_{f\sigma}+\sum_{\sigma,l}\varepsilon_{2}n_{l\sigma}+\sum_{\sigma,f,l}B_{fl}(a_{f\sigma}^{+}a_{l\sigma}+a_{l\sigma}^{+}a_{f\sigma}), \tag{2}
$$

$$
V=(U_{1}/2)\sum_{\sigma,f}n_{f\sigma}n_{f\overline{\sigma}}+(U_{2}/2)\sum_{\sigma,l}n_{l\sigma}n_{l\overline{\sigma}}, \tag{3}
$$

where the indices $f$ and $l$ refer to sublattices A and C, respectively, $a_{j\sigma}^{+}$ and $a_{j\sigma}$ are the Fermi creation and annihilation operators for electrons at the $j$th lattice site ($j=f,l$) with spin $\sigma$, $n_{f\sigma}=a_{f\sigma}^{+}a_{f\sigma}$, $\varepsilon_{1}$ ($\varepsilon_{2}$) is the self-energy of an electron at a site of sublattice A (C), $U_{1}$ ($U_{2}$) is the energy of Coulomb repulsion of electrons with opposite spins at a single site of sublattice A (C), $B_{fl}=B(f-l)$ is a transport integral describing the hopping of electrons from atom to atom by virtue of their kinetic energy and the crystal field, and $\overline{\sigma}=-\sigma$. If $a_{f\sigma}^{+}$ is interpreted as the hole creation operator, the Hamiltonian (1) represents the Emery Hamiltonian,$^{6}$ which describes the quasi-two-dimensional motion of electrons on $\text{CuO}_{2}$ planes in high-temperature superconductors.

The equations of motion for the electron creation operator in the Heisenberg representation ($j=f,l$)

$$
a_{j\sigma}^{+}(\tau)=\exp(H\tau)a_{j\sigma}^{+}(0)\exp(-H\tau),\quad \tau=it,
$$

have the form

$$
\frac{d}{d\tau}a_{f\sigma}^{+}(\tau)=\varepsilon_{1}a_{f\sigma}^{+}(\tau)+\sum_{l}B_{fl}a_{l\sigma}^{+}(\tau)+U_{1}n_{f\overline{\sigma}}a_{f\sigma}^{+}(\tau), \tag{4}
$$

$$
\frac{d}{d\tau}a_{l\sigma}^{+}(\tau)=\varepsilon_{2}a_{l\sigma}^{+}(\tau)+\sum_{f}B_{fl}a_{f\sigma}^{+}(\tau)+U_{2}n_{l\overline{\sigma}}a_{l\sigma}^{+}(\tau). \tag{5}
$$

The operators $n_{f\overline{\sigma}}$ and $n_{l\overline{\sigma}}$ in Eqs. (4) and (5) are written as follows ($j=f$, $l$) (Ref. 4):

$$
n_{i\overline{\sigma}}=\langle n_{j\overline{\sigma}}\rangle+\Delta n_{j\overline{\sigma}}. \tag{6}
$$

We assume that the fluctuation operator of the number of particles $\Delta n_{j\overline{\sigma}}$ does not depend on $\tau$ (Refs. 4 and 7). In the simple Hubbard model$^{5}$ this assumption corresponds to the situation where the fluctuation operator $\Delta n_{j\overline{\sigma}}$ represents a homogeneous-fluctuation operator that is an integral of motion. The thermodynamic averages $\langle n_{j\overline{\sigma}}\rangle=\text{Tr}\{n_{f\overline{\sigma}}\exp(-\beta H)\}$ are assumed to be independent of the site index $j$ in each sublattice. We express the spin $S$ and the number density $n$ as follows:

$$
\langle n_{f\overline{\sigma}}\rangle+\langle n_{f\sigma}\rangle=n, \tag{7}
$$

$$
\langle n_{f\overline{\sigma}}\rangle-\langle n_{f\sigma}\rangle=2\langle S_{f}^{z}\rangle=2S. \tag{8}
$$

For $n=1$ it follows from (7) and (8) that

$$
\langle n_{f\overline{\sigma}}\rangle=(1/2)+S, \tag{9}
$$

$$
\langle n_{f\sigma}\rangle=(1/2)-S, \tag{10}
$$

where $S=\langle S_{f}^{z}\rangle=-\langle S_{f+\Delta}^{z}\rangle$, and the vector $\boldsymbol{\Delta}$ connects neighboring atoms. Consequently,
$$
\left\langle n_{l \overline{\sigma}}\right\rangle=(1 / 2)-S,\qquad(11)
$$

$$
\left\langle n_{l \sigma}\right\rangle=(1 / 2)+S.\qquad(12)
$$

Taking Eqs. (9) and (11) into account, we rewrite the differential equations (4) and (5) in the form
$$
\begin{aligned}
\frac{d}{d \tau} a_{f \sigma}^{+}(\tau)=\varepsilon_{1}^{\prime} a_{f \sigma}^{+}(\tau)+\sum_{l} B_{f l} a_{l \sigma}^{+}(\tau)+U_{1} \Delta n_{f \overline{\sigma}} a_{f \sigma}^{+}(\tau), \\
(13)
\end{aligned}
$$

$$
\begin{aligned}
\frac{d}{d \tau} a_{l \sigma}^{+}(\tau)=\varepsilon_{2}^{\prime} a_{l \sigma}^{+}(\tau)+\sum_{f} B_{f l} a_{f \sigma}^{+}(\tau)+U_{2} \Delta n_{l \overline{\sigma}} a_{l \sigma}^{+}(\tau), \\
(14)
\end{aligned}
$$
where $\varepsilon_{1}^{\prime}=\varepsilon_{1}+(U_{1} / 2)+S U_{1}$, and $\varepsilon_{2}^{\prime}=\varepsilon_{2}+(U_{2} / 2)-S U_{2}$.

We write the Heisenberg operators in the form
$$
a_{j \sigma}^{+}(\tau)=\exp \left(H_{0} \tau\right) \widetilde{a}_{j \sigma}^{+}(\tau) \exp \left(-H_{0} \tau\right),\qquad(15)
$$
where $H_{0}$ is the Hamiltonian appearing in Eq. (1) with allowance for renormalization of the electron self-energies (the substitutions $\varepsilon_{1} \to \varepsilon_{1}^{\prime}$ and $\varepsilon_{2} \to \varepsilon_{2}^{\prime}$). In this case we have two equations for the unknown operators:
$$
\frac{d}{d \tau} \widetilde{a}_{f \sigma}^{+}(\tau)=U_{1} \Delta n_{f \overline{\sigma}} \widetilde{a}_{f \sigma}^{+}(\tau),\qquad(16)
$$

$$
\frac{d}{d \tau} \widetilde{a}_{l \sigma}^{+}(\tau)=U_{2} \Delta n_{l \overline{\sigma}} \widetilde{a}_{l \sigma}^{+}(\tau).\qquad(17)
$$

To close the system of differential equations, we multiply Eq. (16) by the fluctuation operator $\Delta n_{f \overline{\sigma}}=\Delta n_{f \overline{\sigma}}(0)$, multiply Eq. (17) by $\Delta n_{l \overline{\sigma}}=\Delta n_{l \overline{\sigma}}(0)$, and make use of the fact that the operators $\Delta n_{f \overline{\sigma}}^{2}$ and $\Delta n_{l \overline{\sigma}}^{2}$ are $c$-numbers in the half-filling case $^{4}$:
$$
\Delta n_{f \overline{\sigma}}^{2}=\left\langle\Delta n_{f \overline{\sigma}}^{2}\right\rangle,\qquad(18)
$$

$$
\Delta n_{l \overline{\sigma}}^{2}=\left\langle\Delta n_{l \overline{\sigma}}^{2}\right\rangle.\qquad(19)
$$

We obtain
$$
\frac{d}{d \tau} \Delta n_{f \overline{\sigma}} \widetilde{a}_{f \sigma}^{+}(\tau)=U_{1}\left\langle\Delta n_{f \overline{\sigma}}^{2}\right\rangle \widetilde{a}_{f \sigma}^{+}(\tau),\qquad(20)
$$

$$
\frac{d}{d \tau} \Delta n_{l \overline{\sigma}} \widetilde{a}_{l \sigma}^{+}(\tau)=U_{2}\left\langle\Delta n_{l \overline{\sigma}}^{2}\right\rangle \widetilde{a}_{l \sigma}^{+}(\tau).\qquad(21)
$$

Taking Eqs. (6), (9), and (11) into account, along with the properties of the Fermi operators $n_{j \overline{\sigma}}^{2}=n_{j \overline{\sigma}}$, we obtain
$$
\Phi^{2}=\left\langle\Delta n_{f \overline{\sigma}}^{2}\right\rangle=\left\langle\Delta n_{l \overline{\sigma}}^{2}\right\rangle=(1 / 4)-S^{2}.\qquad(22)
$$

The solutions of the system of equations (16), (20) have the form $\left[\widetilde{a}_{f \sigma}^{+}(0)=a_{f \sigma}^{+}(0)\right]$
$$
\begin{aligned}
\widetilde{a}_{f \sigma}^{+}(\tau)= & a_{f \sigma}^{+}(0) \cosh \left(U_{1} \Phi \tau\right) \\
& +\Delta n_{f \overline{\sigma}} a_{f \sigma}^{+}(0) \sinh \left(U_{1} \Phi \tau\right) / \Phi,
\end{aligned}\qquad(23)
$$

$$
\begin{aligned}
\Delta n_{f \overline{\sigma}} \widetilde{a}_{f \sigma}^{+}(\tau)= & \Delta n_{f \overline{\sigma}} a_{f \sigma}^{+}(0) \cosh \left(U_{1} \Phi \tau\right) \\
& +\Phi a_{f \sigma}^{+}(0) \sinh \left(U_{1} \Phi \tau\right).
\end{aligned}\qquad(24)
$$

The system of differential equations (17), (21) have the solutions
$$
\begin{aligned}
\widetilde{a}_{l \sigma}^{+}(\tau)= & a_{l \sigma}^{+}(0) \cosh \left(U_{2} \Phi \tau\right) \\
& +\Delta n_{l \overline{\sigma}} a_{l \sigma}^{+}(0) \sinh \left(U_{2} \Phi \tau\right) / \Phi,
\end{aligned}\qquad(25)
$$

$$
\begin{aligned}
\Delta n_{l \overline{\sigma}} \widetilde{a}_{l \sigma}^{+}(\tau)= & \Delta n_{l \overline{\sigma}} a_{l \sigma}^{+}(0) \cosh \left(U_{2} \Phi \tau\right) \\
& +\Phi a_{l \sigma}^{+}(0) \sinh \left(U_{2} \Phi \tau\right).
\end{aligned}\qquad(26)
$$

The general solution (15) then has the form
$$
\begin{aligned}
a_{f \sigma}^{+}(\tau)= & \exp \left(H_{0} \tau\right) a_{f \sigma}^{+}(0) \exp \left(-H_{0} \tau\right) \cosh \left(U_{1} \Phi \tau\right) \\
& +\Delta n_{f \overline{\sigma}} \exp \left(H_{0} \tau\right) a_{f \sigma}^{+}(0) \\
& \times \exp \left(-H_{0} \tau\right) \sinh \left(U_{1} \Phi \tau\right) / \Phi.
\end{aligned}\qquad(27)
$$

Next we calculate $\overline{a_{f \sigma}^{+}(\tau)}=\exp (H_{0} \tau) a_{f \sigma}^{+}(0) \exp (-H_{0} \tau)$. The operator $\overline{a_{f \sigma}^{+}(\tau)}$ obeys the equation [see Eq. (13)]
$$
\frac{d}{d \tau} \overline{a_{f \sigma}^{+}(\tau)}=\varepsilon_{1}^{\prime} \overline{a_{f \sigma}^{+}(\tau)}+\sum_{l} B_{f l} \overline{a_{l \sigma}^{+}(\tau)}.\qquad(28)
$$

Analogously,
$$
\frac{d}{d \tau} \overline{a_{l \sigma}^{+}(\tau)}=\varepsilon_{2}^{\prime} \overline{a_{l \sigma}^{+}(\tau)}+\sum_{f} B_{f l} \overline{a_{f \sigma}^{+}(\tau)}.\qquad(29)
$$

After the Fourier transformations $^{8}$
$$
a_{f \sigma}^{+}=(2 / N)^{1 / 2} \sum_{\mathbf{k}} a_{\mathbf{k} \sigma}^{+} \exp \left(-i \mathbf{k} \cdot \mathbf{r}_{f}\right),
$$

$$
a_{l \sigma}^{+}=(2 / N)^{1 / 2} \sum_{\mathbf{k}} b_{\mathbf{k} \sigma}^{+} \exp \left(-i \mathbf{k} \cdot \mathbf{r}_{l}\right)
$$
from Eqs. (28) and (29) we obtain
$$
\frac{d}{d \tau} \overline{a_{\mathbf{k} \sigma}^{+}(\tau)}=\varepsilon_{1}^{\prime} \overline{a_{\mathbf{k} \sigma}^{+}(\tau)}+B_{\mathbf{k}} \overline{b_{\mathbf{k} \sigma}^{+}(\tau)},\qquad(30)
$$

$$
\frac{d}{d \tau} \overline{b_{\mathbf{k} \sigma}^{+}(\tau)}=\varepsilon_{2}^{\prime} \overline{b_{\mathbf{k} \sigma}^{+}(\tau)}+B_{\mathbf{k}} \overline{a_{\mathbf{k} \sigma}^{+}(\tau)},\qquad(31)
$$
where $B_{\mathbf{k}}$ is defined by the equation (here $d=2$)
$$
B_{\mathbf{k}}=-2|B|\left[\cos \left(k_{x} a\right)+\cos \left(k_{y} a\right)\right].
$$

The solutions of Eqs. (30) and (31) have the form
$$
\begin{aligned}
\overline{a_{\mathbf{k} \sigma}^{+}(\tau)}= & a_{\mathbf{k} \sigma}^{+}(0)\left[\left(\left(\varepsilon_{1}^{\prime}-\varepsilon_{2}^{\prime}\right) / 2 t_{\mathbf{k}}\right) \sinh \left(t_{\mathbf{k}} \tau\right)\right. \\
& \left.+\cosh \left(t_{\mathbf{k}} \tau\right)\right] \exp \left(\tau\left(\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}\right) / 2\right) \\
& +b_{\mathbf{k} \sigma}^{+}(0) \sinh \left(t_{\mathbf{k}} \tau\right) \\
& \times \exp \left(\tau\left(\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}\right) / 2\right) B_{\mathbf{k}} / t_{\mathbf{k}},
\end{aligned}\qquad(32)
$$

$$
\begin{aligned}
\overline{b_{\mathbf{k} \sigma}^{+}(\tau)}= & b_{\mathbf{k} \sigma}^{+}(0)\left[\left(\left(\varepsilon_{2}^{\prime}-\varepsilon_{1}^{\prime}\right) / 2 t_{\mathbf{k}}\right) \sinh \left(t_{\mathbf{k}} \tau\right)\right. \\
& \left.+\cosh \left(t_{\mathbf{k}} \tau\right)\right] \exp \left(\tau\left(\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}\right) / 2\right) \\
& +a_{\mathbf{k} \sigma}^{+}(0) \sinh \left(t_{\mathbf{k}} \tau\right) \\
& \times \exp \left(\tau\left(\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}\right) / 2\right) B_{\mathbf{k}} / t_{\mathbf{k}},
\end{aligned}\qquad(33)
$$
where

$$t_{\mathbf{k}}=\left[\left(\left(\varepsilon_{2}^{\prime}-\varepsilon_{1}^{\prime}\right) / 2\right)^{2}+B_{\mathbf{k}}^{2}\right]^{1 / 2},$$

$$\overline{a_{\mathbf{k} \sigma}^{+}(0)}=a_{\mathbf{k} \sigma}^{+}(0), \quad \overline{b_{\mathbf{k} \sigma}^{+}(0)}=b_{\mathbf{k} \sigma}^{+}(0).$$

Using Eqs. (32) and (33) and carrying out a Fourier transformation, we obtain for the solution, Eq. (27)

$$
\begin{aligned}
a_{\mathbf{k} \sigma}^{+}(\tau)= & \left\{\left[a_{\mathbf{k} \sigma}^{+}(0)\left[\left(\left(\varepsilon_{1}^{\prime}-\varepsilon_{2}^{\prime}\right) / 2 t_{\mathbf{k}}\right) \sinh \left(t_{\mathbf{k}} \tau\right)+\cosh \left(t_{\mathbf{k}} \tau\right)\right]\right.\right. \\
& +b_{\mathbf{k} \sigma}^{+}(0) \sinh \left(t_{\mathbf{k}} \tau\right) B_{\mathbf{k}} / t_{\mathbf{k}}] \cosh \left(U_{1} \Phi \tau\right) \\
& +\left[\Delta n_{1 \bar{\sigma}} a_{\mathbf{k} \sigma}^{+}(0)\left[\left(\left(\varepsilon_{1}^{\prime}-\varepsilon_{2}^{\prime}\right) / 2 t_{\mathbf{k}}\right) \sinh \left(t_{\mathbf{k}} \tau\right)\right.\right. \\
& \left.\left.+\cosh \left(t_{\mathbf{k}} \tau\right)\right]+\Delta n_{1 \bar{\sigma}} b_{\mathbf{k} \sigma}^{+}(0) \sinh \left(t_{\mathbf{k}} \tau\right)\left(B_{\mathbf{k}} / t_{\mathbf{k}}\right)\right] \\
& \left.\times \sinh \left(U_{1} \Phi \tau\right) / \Phi\right\} \exp \left(\tau\left(\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}\right) / 2\right), \quad (34)
\end{aligned}
$$

where $\Delta n_{1 \bar{\sigma}}=(2 / N) \sum_{\mathbf{p}}(n_{\mathbf{p} \bar{\sigma}}-\langle n_{\mathbf{p} \bar{\sigma}}\rangle)$ is the operator of the homogeneous fluctuation of the number of particles in sublattice A. For electrons of the other subsystem we can write the analogous equation

$$
\begin{aligned}
b_{\mathbf{k} \sigma}^{+}(\tau)= & \left\{\left[b_{\mathbf{k} \sigma}^{+}(0)\left[\left(\left(\varepsilon_{2}^{\prime}-\varepsilon_{1}^{\prime}\right) / 2 t_{\mathbf{k}}\right) \sinh \left(t_{\mathbf{k}} \tau\right)+\cosh \left(t_{\mathbf{k}} \tau\right)\right]\right.\right. \\
& +a_{\mathbf{k} \sigma}^{+}(0) \sinh \left(t_{\mathbf{k}} \tau\right) B_{\mathbf{k}} / t_{\mathbf{k}}] \cosh \left(U_{2} \Phi \tau\right) \\
& +\left[\Delta n_{2 \bar{\sigma}} b_{\mathbf{k} \sigma}^{+}(0)\left[\left(\left(\varepsilon_{2}^{\prime}-\varepsilon_{1}^{\prime}\right) / 2 t_{\mathbf{k}}\right) \sinh \left(t_{\mathbf{k}} \tau\right)\right.\right. \\
& \left.\left.+\cosh \left(t_{\mathbf{k}} \tau\right)\right]+\Delta n_{2 \bar{\sigma}} a_{\mathbf{k} \sigma}^{+}(0) \sinh \left(t_{\mathbf{k}} \tau\right)\left(B_{\mathbf{k}} / t_{\mathbf{k}}\right)\right] \\
& \left.\times \sinh \left(U_{2} \Phi \tau\right) / \Phi\right\} \exp \left(\tau\left(\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}\right) / 2\right). \quad (35)
\end{aligned}
$$

The definition of the operator $\Delta n_{2 \bar{\sigma}}$ of the homogeneous fluctuation of the number of particles in sublattice C is analogous to the definition of the operator $\Delta n_{1 \bar{\sigma}}$.

All the information about the physical properties of the Hubbard model in the given approximation is contained in Eqs. (34) and (35). Our primary concern is the energy spectrum of the system. We therefore calculate the anticommutator Green's function. It follows from (34) and (35) that

$$
\begin{aligned}
&\left\langle\left\langle a_{\mathbf{k} \sigma}^{+}(\tau) \mid a_{\mathbf{k} \sigma}(0)\right\rangle\right\rangle \\
&= \operatorname{Tr}\left\{\left[a_{\mathbf{k} \sigma}^{+}(\tau) a_{\mathbf{k} \sigma}(0)+a_{\mathbf{k} \sigma}(0) a_{\mathbf{k} \sigma}^{+}(\tau)\right] \exp (-\beta H)\right\} \\
&= \frac{1}{4}\left\{\left(1+\frac{\varepsilon_{1}^{\prime}-\varepsilon_{2}^{\prime}}{2 t_{\mathbf{k}}}\right)\left[\exp \left(\left(\frac{\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}}{2}+U_{1} \Phi+t_{\mathbf{k}}\right) \tau\right)\right.\right. \\
&\left.+\exp \left(\left(\frac{\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}}{2}-U_{1} \Phi+t_{\mathbf{k}}\right) \tau\right)\right]+\left(1-\frac{\varepsilon_{1}^{\prime}-\varepsilon_{2}^{\prime}}{2 t_{\mathbf{k}}}\right) \\
& \times\left[\exp \left(\left(\frac{\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}}{2}+U_{1} \Phi-t_{\mathbf{k}}\right) \tau\right)\right. \\
&\left.\left.+\exp \left(\left(\frac{\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}}{2}-U_{1} \Phi-t_{\mathbf{k}}\right) \tau\right)\right]\right\}, \quad (36)
\end{aligned}
$$

$$
\begin{aligned}
&\left\langle\left\langle b_{\mathbf{k} \sigma}^{+}(\tau) \mid b_{\mathbf{k} \sigma}(0)\right\rangle\right\rangle \\
&= \operatorname{Tr}\left\{\left[b_{\mathbf{k} \sigma}^{+}(\tau) b_{\mathbf{k} \sigma}(0)+b_{\mathbf{k} \sigma}(0) b_{\mathbf{k} \sigma}^{+}(\tau)\right] \exp (-\beta H)\right\} \\
&= \frac{1}{4}\left\{\left(1-\frac{\varepsilon_{1}^{\prime}-\varepsilon_{2}^{\prime}}{2 t_{\mathbf{k}}}\right)\left[\exp \left(\left(\frac{\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}}{2}+U_{2} \Phi+t_{\mathbf{k}}\right) \tau\right)\right.\right. \\
&\left.+\exp \left(\left(\frac{\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}}{2}-U_{2} \Phi+t_{\mathbf{k}}\right) \tau\right)\right]+\left(1+\frac{\varepsilon_{1}^{\prime}-\varepsilon_{2}^{\prime}}{2 t_{\mathbf{k}}}\right) \\
& \times\left[\exp \left(\left(\frac{\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}}{2}+U_{2} \Phi-t_{\mathbf{k}}\right) \tau\right)\right. \\
&\left.\left.+\exp \left(\left(\frac{\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}}{2}-U_{2} \Phi-t_{\mathbf{k}}\right) \tau\right)\right]\right\}. \quad (37)
\end{aligned}
$$

The Fourier transforms of the anticommutator Green's functions (36) and (37) are

$$
\begin{aligned}
\left\langle\left\langle a_{\mathbf{k} \sigma}^{+} \mid a_{\mathbf{k} \sigma}\right\rangle\right\rangle_{E}= & \frac{i}{2 \pi} \frac{1}{4}\left\{\frac{1+\left(\varepsilon_{1}^{\prime}-\varepsilon_{2}^{\prime}\right) / 2 t_{\mathbf{k}}}{E-U_{1} \Phi-t_{\mathbf{k}}-\left(\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}\right) / 2}\right. \\
& +\frac{1+\left(\varepsilon_{1}^{\prime}-\varepsilon_{2}^{\prime}\right) / 2 t_{\mathbf{k}}}{E+U_{1} \Phi-t_{\mathbf{k}}-\left(\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}\right) / 2} \\
& +\frac{1-\left(\varepsilon_{1}^{\prime}-\varepsilon_{2}^{\prime}\right) / 2 t_{\mathbf{k}}}{E-U_{1} \Phi+t_{\mathbf{k}}-\left(\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}\right) / 2} \\
& \left.+\frac{1-\left(\varepsilon_{1}^{\prime}-\varepsilon_{2}^{\prime}\right) / 2 t_{\mathbf{k}}}{E+U_{1} \Phi+t_{\mathbf{k}}-\left(\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}\right) / 2}\right\}, \quad (38)
\end{aligned}
$$

$$
\begin{aligned}
\left\langle\left\langle b_{\mathbf{k} \sigma}^{+} \mid b_{\mathbf{k} \sigma}\right\rangle\right\rangle_{E}= & \frac{i}{2 \pi} \frac{1}{4}\left\{\frac{1-\left(\varepsilon_{1}^{\prime}-\varepsilon_{2}^{\prime}\right) / 2 t_{\mathbf{k}}}{E-U_{2} \Phi-t_{\mathbf{k}}-\left(\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}\right) / 2}\right. \\
& +\frac{1-\left(\varepsilon_{1}^{\prime}-\varepsilon_{2}^{\prime}\right) / 2 t_{\mathbf{k}}}{E+U_{2} \Phi-t_{\mathbf{k}}-\left(\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}\right) / 2} \\
& +\frac{1+\left(\varepsilon_{1}^{\prime}-\varepsilon_{2}^{\prime}\right) / 2 t_{\mathbf{k}}}{E-U_{2} \Phi+t_{\mathbf{k}}-\left(\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}\right) / 2} \\
& \left.+\frac{1+\left(\varepsilon_{1}^{\prime}-\varepsilon_{2}^{\prime}\right) / 2 t_{\mathbf{k}}}{E+U_{2} \Phi+t_{\mathbf{k}}-\left(\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}\right) / 2}\right\}, \quad (39)
\end{aligned}
$$

where

$$
\begin{aligned}
& \varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}=\varepsilon_{1}+\varepsilon_{2}+\left(\left(U_{1}+U_{2}\right) / 2\right)+S\left(U_{1}-U_{2}\right), \\
& \varepsilon_{1}^{\prime}-\varepsilon_{2}^{\prime}=\varepsilon_{1}-\varepsilon_{2}+\left(\left(U_{1}-U_{2}\right) / 2\right)+S\left(U_{1}+U_{2}\right), \\
& \Phi=\left(1 / 4-S^{2}\right)^{1 / 2}, \quad t_{\mathbf{k}}=\left[\left(\left(\varepsilon_{1}^{\prime}-\varepsilon_{2}^{\prime}\right) / 2\right)^{2}+B_{\mathbf{k}}^{2}\right]^{1 / 2}.
\end{aligned}
$$

The poles of the Green's functions (38) and (39) determine the energy spectrum of the system

$$
E_{1-4}=\left(\left(\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}\right) / 2\right) \pm U_{1} \Phi \pm t_{\mathbf{k}}, \quad(40)
$$

$$
E_{5-8}=\left(\left(\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}\right) / 2\right) \pm U_{2} \Phi \pm t_{\mathbf{k}}. \quad(41)
$$

An analysis of the spectrum, Eqs. (40), (41) in the case of a half-filled band $(n=1)$ shows that the bands associated with antiferromagnetic interaction become narrower when the temperature drops below the Néel temperature. The system characterized by the Hamiltonian (1) is conducting above the Néel point for parameters corresponding to $\mathrm{Cu}$ and $\mathrm{O}$. At temperatures below the Néel temperature the substance can exist either in the conducting (semiconductor or metal type) state or (for smaller values of $B$) in the insulating state. The bands become narrower as the temperature decreases (the bands are formed from intersecting or nonintersecting subbands) until, as a result, two narrow bands are left at $T=0$ (Figs. 1-3). If we set $\varepsilon_{1}=\varepsilon_{2}=\varepsilon$ and $U_{1}=U_{2}=U$, we can

![](./images/813302387694370817_1.jpg)

FIG. 1. Energy spectrum of the Hubbard model for the following values of
the parameters: $\varepsilon_1=-4$ eV, $\varepsilon_2=-1$ eV, $U_1=8$ eV, $U_2=2$ eV, $B=1.5$ eV,
$S=0.1$.

then revert to the simple Hubbard model. The spectrum of
elementary excitations in this case is described by the sim-
pler equation $(n=1, S=1/2)$

$$
E(\mathbf{k})= \pm\left[(U / 2)^{2}+4 B^{2}\left[\cos (k_{x} a)+\cos (k_{y} a)\right]^{2}\right]^{1 / 2}.
\tag{42}
$$

We emphasize that Eq. (42) for the energy spectrum at fixed
values of $U$ and $2B$ corresponds to the energy spectrum at a
finite temperature, which is determined from Eq. (45). The
resulting form of the energy spectrum Eq. (42) (Fig. 4), is
typical of the antiferromagnetic insulating state. $^{9}$ Indeed, an
analysis of the spectrum in this case shows that for $n=1$ the
energy of the ground state in the presence of antiferromag-
netic ordering is significantly lower than the energy of the
ground state in the case of paramagnetism or ferromag-
netism. Consequently the ground state of the Hubbard model
in the approximation used here is antiferromagnetic and in-
sulating at $T=0$ and $n=1$.

We now derive a consistency equation for $S$. From Eq.
(38), on the basis of the spectral theorem, $^{10}$ we obtain

![](./images/813302387694370817_2.jpg)

FIG. 2. Energy spectrum of the Hubbard model for the following values of
the parameters: $\varepsilon_1=-4$ eV, $\varepsilon_2=-1$ eV, $U_1=8$ eV, $U_2=2$ eV, $B=1.5$ eV,
$S=0.49$.

![](./images/813302387694370817_3.jpg)

FIG. 3. Energy spectrum of the Hubbard model for the following values of
the parameters: $\varepsilon_1=-4$ eV, $\varepsilon_2=-1$ eV, $U_1=8$ eV, $U_2=2$ eV, $B=1.5$ eV.
The solid curves correspond to $S=1/2$ (antiferromagnetic state), and the
dashed curves correspond to $S=0$ (paramagnetism or ferromagnetism).

$$
\begin{aligned}
\left\langle n_{\mathbf{k} \sigma}\right\rangle= & \frac{1}{4}\left\{\left(1+\frac{\varepsilon_{1}^{\prime}-\varepsilon_{2}^{\prime}}{2 t_{\mathbf{k}}}\right)\left[f^{+}\left(\frac{\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}}{2}+U_{1} \Phi+t_{\mathbf{k}}\right)\right.\right. \\
& \left.+f^{+}\left(\frac{\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}}{2}-U_{1} \Phi+t_{\mathbf{k}}\right)\right]+\left(1-\frac{\varepsilon_{1}^{\prime}-\varepsilon_{2}^{\prime}}{2 t_{\mathbf{k}}}\right) \\
& \times\left[f^{+}\left(\frac{\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}}{2}+U_{1} \Phi-t_{\mathbf{k}}\right)\right. \\
& \left.\left.+f^{+}\left(\frac{\varepsilon_{1}^{\prime}+\varepsilon_{2}^{\prime}}{2}-U_{1} \Phi-t_{\mathbf{k}}\right)\right]\right\},
\end{aligned}
\tag{43}
$$

where
$$
f^{+}(x)=1 /(1+\exp (\beta x)).
$$

![](./images/813302387694370817_4.jpg)

FIG. 4. Energy spectrum of the Hubbard model for the following values of
the parameters: $\varepsilon_1=\varepsilon_2=-4$ eV, $U_1=U_2=8$ eV, $B=1.5$ eV. The solid
curves correspond to $S=1/2$ (antiferromagnetic state), and the dashed
curves correspond to $S=0$ (paramagnetism or ferromagnetism).


The following equation can be obtained for electrons with opposite orientation of the spin projection by analogy with Eqs. (13)-(43):

$$
\begin{aligned}
\left\langle n_{\mathbf{k} \bar{\sigma}}\right\rangle= & \frac{1}{4}\left\{\left(1+\frac{\varepsilon_{1}^{\prime \prime}-\varepsilon_{2}^{\prime \prime}}{2 t_{\mathbf{k}}^{\prime}}\right)\left[f^{+}\left(\frac{\varepsilon_{1}^{\prime \prime}+\varepsilon_{2}^{\prime \prime}}{2}+U_{1} \Phi+t_{\mathbf{k}}^{\prime}\right)\right.\right. \\
& \left.+f^{+}\left(\frac{\varepsilon_{1}^{\prime \prime}+\varepsilon_{2}^{\prime \prime}}{2}-U_{1} \Phi+t_{\mathbf{k}}^{\prime}\right)\right]+\left(1-\frac{\varepsilon_{1}^{\prime \prime}-\varepsilon_{2}^{\prime \prime}}{2 t_{\mathbf{k}}^{\prime}}\right) \\
& \times\left[f^{+}\left(\frac{\varepsilon_{1}^{\prime \prime}+\varepsilon_{2}^{\prime \prime}}{2}+U_{1} \Phi-t_{\mathbf{k}}^{\prime}\right)\right. \\
& \left.\left.+f^{+}\left(\frac{\varepsilon_{1}^{\prime \prime}+\varepsilon_{2}^{\prime \prime}}{2}-U_{1} \Phi-t_{\mathbf{k}}\right)\right]\right\},
\end{aligned}
$$

where

$$
\begin{aligned}
& \varepsilon_{1}^{\prime \prime}+\varepsilon_{2}^{\prime \prime}=\varepsilon_{1}+\varepsilon_{2}+\left(\left(U_{1}+U_{2}\right) / 2\right)-S\left(U_{1}-U_{2}\right), \\
& \varepsilon_{1}^{\prime \prime}-\varepsilon_{2}^{\prime \prime}=\varepsilon_{1}-\varepsilon_{2}+\left(\left(U_{1}-U_{2}\right) / 2\right)-S\left(U_{1}+U_{2}\right), \\
& t_{\mathbf{k}}^{\prime}=\left[\left(\left(\varepsilon_{1}^{\prime \prime}-\varepsilon_{2}^{\prime \prime}\right) / 2\right)^{2}+B_{\mathbf{k}}^{2}\right]^{1 / 2}.
\end{aligned}
$$

Summing Eqs. (43) and (44), we obtain an equation for the chemical potential. This expression is too cumbersome to write out here, and we merely note that a half-filled band ($n=1$) corresponds to the conditions $\varepsilon_{1}=-U_{1}/2$ and $\varepsilon_{2}=-U_{2}/2$. We set $\varepsilon_{1}=-U_{1}/2$ and $\varepsilon_{2}=-U_{2}/2$ in Eqs. (43) and (44) for the case $n=1$ and bearing in mind that $2S=\langle n_{f\bar{\sigma}}\rangle-\langle n_{f\sigma}\rangle=(2/N)\sum_{\mathbf{k}}(\langle n_{\mathbf{k}\bar{\sigma}}\rangle-\langle n_{\mathbf{k}\sigma}\rangle$ we obtain an equation for $S$,

$$
\begin{aligned}
2 S= & \frac{1}{2 N} \sum_{\mathbf{k}}\left\{\left(1-S \frac{U_{1}+U_{2}}{2 t_{\mathbf{k}}}\right)\left[\tanh \left(\frac{\beta}{2}\left(S \frac{U_{1}-U_{2}}{2}\right.\right.\right.\right. \\
& \left.\left.\left.+U_{1} \Phi-t_{\mathbf{k}}\right)\right)+\tanh \left(\frac{\beta}{2}\left(S \frac{U_{1}-U_{2}}{2}-U_{1} \Phi-t_{\mathbf{k}}\right)\right)\right] \\
& +\left(1+S \frac{U_{1}+U_{2}}{2 t_{\mathbf{k}}}\right)\left[\tanh \left(\frac{\beta}{2}\left(S \frac{U_{1}-U_{2}}{2}-U_{1} \Phi+t_{\mathbf{k}}\right)\right)\right. \\
& \left.\left.+\tanh \left(\frac{\beta}{2}\left(S \frac{U_{1}-U_{2}}{2}+U_{1} \Phi+t_{\mathbf{k}}\right)\right)\right]\right\}.
\end{aligned}
$$

The magnitude of the spin (magnetization) $S$ depends on the temperature. In the general case, most likely, Eq. (45) can be used to investigate the magnetization only by numerical analysis. Let us consider the simplest case $T=0$. Near spin $S \approx 1 / 2$ we have $t_{\mathbf{k}}>\left[S\left(U_{1}-U_{2}\right) / 2\right] \pm U_{1} \Phi$. In this case, therefore, we infer that (for $d=1$)

$$
\frac{4}{U_{1}+U_{2}}=\frac{2}{N} \sum_{\mathbf{k}}\left[S^{2}\left(U_{1}+U_{2}\right) / 4+4 B^{2} \cos ^{2}\left(k_{x} a\right)\right]^{-1 / 2}.
$$

Changing from summation on $\mathbf{k}$ to integration over $\theta=k_{x} a$ ($\pi/2\geqslant\theta\geqslant\pi/2$), we obtain

$$
\begin{aligned}
\frac{4}{U_{1}+U_{2}}= & \frac{2}{\pi}\left[S^{2}\left(U_{1}+U_{2}\right) / 4+4 B^{2}\right]^{-1 / 2} K \\
& \times\left(4 B^{2} /\left(S^{2}\left(U_{1}+U_{2}\right) / 4+4 B^{2}\right)\right),
\end{aligned}
$$

where

$$
K(m)=\frac{\pi}{2}\left[1+\left(\frac{1}{2}\right)^{2} m+\left(\frac{1 \cdot 3}{2 \cdot 4}\right)^{2} m^{2}\left(\frac{1 \cdot 3 \cdot 5}{2 \cdot 4 \cdot 6}\right)^{2} m^{3}+\ldots\right]
$$

is a complete elliptic integral of the first kind $(m<1).^{11}$ We confine our discussion to the case $4 B \ll U_{1}+U_{2}$ so that we can set $K(m)=\pi / 2$. In this case it follows from Eq. (47) that $S=1/2$. The exact values of the complete elliptic integral of the first kind $K(m)$ are needed in more general cases [see Table 17.1 on p. 608 in Ref. 11]. Now the spin $S$ depends on the ratio between $U_{1}+U_{2}$ and $2 B$, and a nontrivial solution always exists for $S$. For example, in the case $4 B /\left(U_{1}+U_{2}\right)=0.2$ the spin $S=0.48$; if $4 B /\left(U_{1}+U_{2}\right)=0.8$, then the spin $S=0.25$, etc. Consequently, the consistency equation for $S$, Eq. (45) always has a nontrivial antiferromagnetic solution, which was predicted in an earlier paper. $^{12}$ The behavior of the curve of $S$ as a function of the ratio $\left(U_{1}+U_{2}\right)/4B$ agrees with the results of a numerical analysis. $^{13,14}$

In summary, the above-proposed procedure for calculating the anticommutator Green's function can be used not only to determine the spectrum of elementary excitations, but also to derive a consistency equation for the spin (magnetization) $S$ with a nontrivial antiferromagnetic solution.

The author is grateful to R. R. Nigmatullin for helpful discussions of the results and for valuable consultations.

$^{1}$ Yu. A. Izyumov, M. I. Katsnel'son, and Yu. N. Skryabin, *Magnetism of Localized Electrons* [in Russian], Moscow (1994).
$^{2}$ Yu. A. Izyumov, Usp. Fiz. Nauk **165**, 403 (1995).
$^{3}$ E. Lieb and F. Y. Wu, Phys. Rev. Lett. **20**, 1445 (1968).
$^{4}$ V. V. Loskutov, G. I. Mironov, and R. R. Nigmatullin, Fiz. Nizk. Temp. **22**, 282 (1996) [Low Temp. Phys. **22**, 220 (1996)].
$^{5}$ J. Hubbard, Proc. R. Soc. London Ser. A **276**, 238 (1963).
$^{6}$ V. J. Emery, Phys. Rev. Lett. **58**, 2794 (1987).
$^{7}$ R. R. Nigmatullin and V. A. Toboev, Teor. Mat. Fiz. **68**, 88 (1986).
$^{8}$ T. Moriya, *Spin Fluctuations in Itinerant Electron Magnetism* (Springer-Verlag, Berlin-New York, 1985) [Russian trans., Moscow, 1988].
$^{9}$ S. L. Malyshev and V. N. Popov, Teor. Mat. Fiz. **105**, 149 (1995).
$^{10}$ S. V. Tyablikov, *Methods in the Quantum Theory of Magnetism* (Plenum Press, New York, 1967) [Russian original, 2nd ed., Nauka, Moscow, 1975].
$^{11}$ M. Abramowitz and I. A. Stegun, *Handbook of Mathematical Functions*, U. S. Govt. Printing Office, Washington, DC (1964) [Russian trans., Nauka, Moscow 1979].
$^{12}$ D. I. Khomskii, Fiz. Met. Metalloved. **29**(1), 31 (1970).
$^{13}$ Y. Kakehashi and H. Hasegawa, Phys. Rev. B **37**, 7777 (1988).
$^{14}$ Y. Kakehashi and P. Fulde, Phys. Rev. B **32**, 1595 (1985).

Translated by James S. Wood