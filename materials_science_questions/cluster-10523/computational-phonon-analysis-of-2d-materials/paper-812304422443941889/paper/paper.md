# Phonon Dispersion Relations in Two-dimensional Peierls Phase
Shutaro CHIBA* and Yoshiyuki ONO†

Department of Physics, Toho University, 2-2-1 Miyama, Funabashi, Chiba 274-8510
(Received January 15, 2004)

The phonon dispersion relations in the two-dimensional Peierls phase (Peierls insulator) are studied numerically, focusing on a two-dimensional SSH (Su-Shrieffer-Heeger) model having a half-filled electronic band, in which the ground state has multimode lattice distortions with the nesting wave vector $\boldsymbol{Q}=(\pi,\pi)$ and various other wave vectors parallel to $\boldsymbol{Q}$. In addition it has been shown that there are a large number of degeneracy in the ground state, with different patterns of lattice distortions. We consider the phonon dispersion relations in the two-dimensional Peierls phase at temperatures lower than the critical temperature of Peierls transition $T_{\rm c}$. When the temperature is raised from the region lower than $T_{\rm c}$, we confirm the softening of phonon modes whose wave vectors are $\boldsymbol{Q}$ and those parallel to $\boldsymbol{Q}$, similarly as reported in our previous paper [J. Phys. Soc. Jpn. 72 (2003) 1995] where we dealt with phonon dispersion relations at temperatures higher than $T_{\rm c}$. The dependence of phonon dispersion relations on the patterns of lattice distortions is also discussed.

KEYWORDS: two-dimensional Peierls phase, multimode lattice distortions, phonon dispersion relations, phonon softening, SSH model
DOI: 10.1143/JPSJ.73.2473

## 1. Introduction
A theoretical model based on the two-dimensional (2D) square-lattice version of Su-Schrieffer-Heeger (SSH) model,¹) which was originally proposed for studying one-dimensional (1D) electron–lattice systems such as polymers, and extended to include on-site electron–electron repulsive interaction, is extensively used in investigating the electronic and lattice properties of 2D systems,²⁻⁵) and often called as the 2D Peierls–Hubbard (PH) model. When the electronic band is just half-filled, the square shape of the Fermi surface makes us speculate the Peierls instability due to lattice distortions with the nesting vector $\boldsymbol{Q}=(\pi,\pi)$; here and hereafter the lattice constant is set to be unity. Then this 2D PH model is expected to be the minimal theoretical model for studying layered substances such as organic compounds which show the BOW (bond order wave) and the SDW (spin density wave) states.⁵) In fact Yuan and Kopp⁵) suggested the possibility to explain the occurrence (including the coexistence) of the BOW and the SDW in some organic compounds⁶,⁷) by this model. Although previous works based on this 2D PH model considered only the lattice distortions with the nesting vector $\boldsymbol{Q}$, recent investigations by our group⁸,¹⁰) have revealed that the true ground state of the 2D SSH model without the electron–electron interaction involves lattice distortions not only with $\boldsymbol{Q}$ but also with those wave vectors parallel to $\boldsymbol{Q}$. In fact it has been shown that this multimode Peierls state has a lower energy than the traditional single-mode ($\boldsymbol{Q}$-mode) Peierls state as treated by Tang and Hirsch.²) Therefore, before discussing rather sophisticated problems such as the coexistence of the BOW and the SDW, we should understand more deeply the ground state of the 2D SSH model in the absence of electron–electron interactions.

What are known concerning this multimode Peierls state are summarized as follows: (1) The lattice distortions consist of the longitudinal $\boldsymbol{Q}$-mode and of the transverse modes with wave vectors parallel to $\boldsymbol{Q}$.⁸,⁹) (2) The number of nonequivalent distortion patterns with the same degenerate ground state energy is given by $_{N/2}{\rm C}_{N/4}$ ($\sim2^{N/2}$ for large $N$) for the system size $N\times N$.¹⁰,¹¹) (3) The critical temperature $T_{\rm c}$, below which the multimode Peierls phase is the most stable state, is independent of the distortion pattern, and so is the temperature dependent free energy which is always lower than that of the single-mode ($\boldsymbol{Q}$-mode) Peierls phase; by the way, the critical temperature (scaled by $t_0$ the electronic nearest neighbor transfer integral) of the multimode Peierls transition is determined only by the dimensionless coupling constant (see next section for its definition) and is higher than that of the single-mode Peierls transition.¹²) (4) In accordance with the low temperature behaviors of the distortions, the longitudinal phonon mode with the wave vector $\boldsymbol{Q}$ and the transverse phonon modes with the wave vectors parallel to $\boldsymbol{Q}$ are found to soften when the temperature approaches to $T_{\rm c}$ from above, all vanishing at $T_{\rm c}$.⁹) Although there is no distortion component of the transverse mode with $\boldsymbol{Q}$ below $T_{\rm c}$, we find the softening of this phonon mode at the same $T_{\rm c}$.⁹)

In the present work, we discuss the phonon dispersion relations in the multimode Peierls phase, i.e., at temperatures lower than $T_{\rm c}$, based on the 2D version of the SSH model. Particularly the temperature and distortion-pattern dependences of the dispersion relations are considered. In the presence of Peierls distortions, the calculation of the phonon dispersion is not as simple as that in the high temperature region ($T>T_{\rm c}$) where the eigenmode calculation reduces to eigenvalue problems of $2\times2$ matrices. Furthermore we argue the possibility to lift the degeneracy by virtue of the pattern-dependent quantum correction of the ground state energy.

The paper is organized as follows. In the next section we present the model and formulations to obtain phonon dispersion relations in the presence of the multimode Peierls distortions. In §3 the results of calculations are shown. The last section is devoted to summary and discussion. Some preliminary results of the present work have been published in ref. 13.

*E-mail: shutaroc@ph.sci.toho-u.ac.jp
†E-mail: ono@ph.sci.toho-u.ac.jp

## 2. Model and Formulation

In this paper we focus on the 2D square-lattice SSH model with a half-filled electronic band, described as follows,

$$
\begin{aligned}
H= & -\sum_{i, j, s}\left\{\left[t_{0}-\alpha\left(u_{x}(i+1, j)-u_{x}(i, j)\right)\right]\right. \\
& \times\left(c_{i+1, j, s}^{\dagger} c_{i, j, s}+c_{i, j, s}^{\dagger} c_{i+1, j, s}\right) \\
& +\left[t_{0}-\alpha\left(u_{y}(i, j+1)-u_{y}(i, j)\right)\right] \\
& \times\left(c_{i, j+1, s}^{\dagger} c_{i, j, s}+c_{i, j, s}^{\dagger} c_{i, j+1, s}\right) \\
& +\frac{K}{2} \sum_{i, j}\left[\left(u_{x}(i+1, j)-u_{x}(i, j)\right)^{2}\right. \\
& \left.+\left(u_{y}(i, j+1)-u_{y}(i, j)\right)^{2}\right] \\
& +\frac{M}{2} \sum_{i, j}\left[\left(\dot{u}_{x}(i, j)\right)^{2}+\left(\dot{u}_{y}(i, j)\right)^{2}\right],
\end{aligned}
$$

where the field operators $c_{i, j, s}$ and $c_{i, j, s}^{\dagger}$ annihilate and create an electron with spin $s$ at the site $(i, j)$, respectively, and $t_{0}$ is the transfer integral for the equidistant lattice, $\alpha$ the electron-lattice coupling constant, $\boldsymbol{u}(i, j)$ the lattice displacement vector whose $x$ - and $y$-components are denoted as $u_{x}(i, j)$ and $u_{y}(i, j)$, respectively, $K$ the force constant describing the ionic coupling strength in the lattice system, $M$ the mass of an ion unit at a site. Through out this paper, we assume the periodic boundary conditions for both directions.

Before describing linear mode equations for the multimode Peierls phase, let us discuss phonon dispersion in the temperature region higher than the critical temperature $T_{\mathrm{c}}$ of the Peierls transition as a supplement to our previous paper. $^{9)}$ In this temperature region we have numerically confirmed that the longitudinal $\boldsymbol{Q}$-mode and all of transverse modes with wave vectors parallel to $\boldsymbol{Q}$ including $\boldsymbol{Q}$ itself are softened when the temperature is lowered to $T_{\mathrm{c}}$. Furthermore it has been confirmed again numerically that the eigenfrequencies for transverse modes with wave vectors $q_{x}=q_{y}=$ $q$ have the same $q$-dependence as that of the free phonon $\omega_{0}(q)[=\sqrt{2(K / M)(1-\cos q)}]$. Therefore their temperature dependent prefactor is independent of the phonon wave number $q$. After the publication of the previous paper, ${ }^{9)}$ we have noticed that this fact can be proven even analytically. As described in ref. 9, the normal mode analysis in the temperature region higher than $T_{\mathrm{c}}$ reduces to the eigenvalue problem of $2 \times 2$ matrices, whose elements are given by sums over the electronic wave number. When the wave number of the linear mode is given as $q_{x}=q_{y}=q$ and if we restrict ourselves to the transverse mode, the square of the eigenfrequency is found to be expressed in the following form after some tedious manipulations of trigonometric functions,

$$
\omega^{2}=(1-\cos q)\left\{\frac{2 K}{M}-\frac{8 \alpha^{2}}{M N^{2} t_{0}} \sum_{\boldsymbol{k}} f\left(\epsilon_{\boldsymbol{k}}\right) \frac{\cos \left[\frac{1}{2}\left(k_{x}+k_{y}\right)\right] \sin ^{2}\left[\frac{1}{2}\left(k_{x}-k_{y}\right)\right]}{\cos \left[\frac{1}{2}\left(k_{x}-k_{y}\right)\right]}\right\} .
$$

We have confirmed that the above expression precisely reproduces the numerically obtained temperature dependence of dispersion curves in the case of the transverse modes with $q_{x}=q_{y}=q$ at temperatures higher than $T_{\mathrm{c}}$ [see Fig. 2(a) of ref. 9]. It is also clear that the critical temperature $T_{\mathrm{c}}$ (scaled by $t_{0}$ ) at which the right hand side of eq. (2.2) vanishes depends only on the dimensionless coupling constant $\lambda\left(\equiv \alpha^{2} / K t_{0}\right)$.

In the temperature region lower than $T_{\mathrm{c}}$, the linear mode analysis takes much more complicated form than that in the higher temperature region, due to the presence of Peierls distortions. In the previous paper, ${ }^{9)}$ we have presented the formulation of linear mode analysis in the site representation, where the normal mode analysis is expressed as the eigenvalue problem of a $2 N^{2} \times 2 N^{2}$ matrix for the system size $N \times N$. However if we notice that the Peierls distortions involve only the Fourier components with $\boldsymbol{Q}=(\pi, \pi)$ and those wave vectors parallel to it. the problem can be reduced to eigenvalue problems of smaller matrices by introducing the momentum representation for the Hamitonian as was done in the study of the static distortions. ${ }^{8)}$ In fact, the lattice distortions can be written in the following form,

$$
x_{r}=x_{Q}(-1)^{i+j}+\sum_{\substack{0<q<\pi \\\left(q_{x}=q_{y}=q\right)}}\left[x_{q} \mathrm{e}^{\mathrm{i} \boldsymbol{q} \cdot \boldsymbol{r}}+\text { c.c. }\right],
$$

$$
y_{r}=y_{Q}(-1)^{i+j}+\sum_{\substack{0<q<\pi \\\left(q_{x}=q_{y}=q\right)}}\left[y_{q} \mathrm{e}^{\mathrm{i} \boldsymbol{q} \cdot \boldsymbol{r}}+\text { c.c. }\right],
$$

where $\boldsymbol{r}$ stands for the lattice site $(i, j), x_{r}=u_{x}\left(\boldsymbol{r}+\boldsymbol{e}_{x}\right)-$ $u_{x}(\boldsymbol{r}), y_{r}=u_{y}\left(\boldsymbol{r}+\boldsymbol{e}_{y}\right)-u_{y}(\boldsymbol{r})$, with $\boldsymbol{e}_{x}=(1,0)$ and $\boldsymbol{e}_{y}=$ $(0,1)$, and $x_{q}, y_{q}, x_{Q}$ and $y_{Q}$ are Fourier amplitudes of lattice distortions with corresponding wave vectors $\boldsymbol{q}=(q, q)$ and $\boldsymbol{Q}$ respectively. Substituting the above expressions for the lattice distortions into the static part of the Hamiltonian eq. (2.1), we obtain the following expression,

$$
\begin{aligned}
H= & \sum_{\boldsymbol{k}, s} \epsilon_{\boldsymbol{k}} c_{\boldsymbol{k}, s}^{\dagger} c_{\boldsymbol{k}, s} \\
& +\alpha \sum_{\boldsymbol{k}, s} 2 \mathrm{i}\left(x_{Q} \sin k_{x} a+y_{Q} \sin k_{y} a\right) c_{\boldsymbol{k}+\boldsymbol{Q}, s}^{\dagger} c_{\boldsymbol{k}, s} \\
& +\alpha \sum_{0<q<\pi} \sum_{\boldsymbol{k}, s} 2\left\{\mathrm{e}^{-\mathrm{i} q / 2}\left[x_{q} \cos \left(k_{x}+\frac{q}{2}\right)\right.\right. \\
& \left.+y_{q} \cos \left(k_{y}+\frac{q}{2}\right)\right] c_{\boldsymbol{k}+\boldsymbol{q}, s}^{\dagger} c_{\boldsymbol{k}, s} \\
& \left.+\mathrm{e}^{\mathrm{i} q / 2}\left[x_{q}^{*} \cos \left(k_{x}-\frac{q}{2}\right)+y_{q}^{*} \cos \left(k_{y}-\frac{q}{2}\right)\right] c_{\boldsymbol{k}-\boldsymbol{q}, s}^{\dagger} c_{\boldsymbol{k}, s}\right\} \\
& +N^{2} \frac{K}{2}\left(x_{Q}^{2}+y_{Q}^{2}\right)+N^{2} K \sum_{0<q<\pi}\left(\left|x_{q}\right|^{2}+\left|y_{q}\right|^{2}\right),
\end{aligned}
$$

J. Phys. Soc. Jpn., Vol. 73, No. 9, September, 2004
S. CHIBA and Y. ONO

![](./images/812304422443941889_1.jpg)

Fig. 1. (a) indicates the structures of the electronic states in the presence of multimode Peierls distortions. The wave vectors on the thick line are entangled due to Peierls distortions composed of Fourier components with $\boldsymbol{Q}$ and those wave vectors parallel to $\boldsymbol{Q}$. The electronic states can be divided into $N$ groups with $N$ the linear system size, the off-set wave number $p$ playing the role of the group index. (b) shows the similar structures of the phonon modes. The phonon modes can also be divided into $N$ groups. For example, the thick line shows the wave vectors involved in phonon modes belonging to the group indicated by $q'=0$, and the dotted line the group indicated by $q'=2\times2\pi/N$, respectively.

with $\epsilon_{\boldsymbol{k}}=-2t_{0}(\cos k_{x}+\cos k_{y})$. This is the same as was given in ref. 8. Nevertheless we have reproduced it here for clarifying the notations and for later use in the present paper.

The electronic wave functions $\{\phi_{v}(\boldsymbol{r})\}$ and the Fourier amplitudes of the static distortions are determined self-consistently so as to minimize the total energy (or free energy at finite temperatures).

As is seen from the above expression of the Hamiltonian, the electronic eigenstates in the presence of the multimode Peierls distortions can be classified into $N$ groups ($N$ the linear system dimension), the states in each group given by superpositions of plane waves with wave vectors $(k,k+p)$ $[k=2\pi n/N,\ n=-(N/2-1),\dots,N/2]$ where the off-set wave number $p$ plays the role of the group index and takes one of the values in the region $0\leq p<2\pi$ [see Fig. 1(a)]; note that all the wave vectors should be considered within the first Brillouin zone. Thus the electronic eigenstates are expressed in the form,
$$
\phi_{v}(\boldsymbol{r})\equiv\phi_{u,p}(\boldsymbol{r})=\frac{1}{N}\sum_{n}A_{u,p}(k_{n})\mathrm{e}^{\mathrm{i}\boldsymbol{k}_{n,p}\cdot\boldsymbol{r}},\tag{2.6}
$$
where $u$ is the energy index within each group, $p$ the group index and $A_{u,p}(n)$ corresponding to a wave function in the wave number representation; the wave vector $\boldsymbol{k}_{n,p}$ is given by $(k_{n},k_{n}+p)$ with $k_{n}=2\pi n/N$.

In the previous paper we have presented a general formulation for obtaining the linear normal modes, according to which the normal mode equations for the linear dynamical deviations of lattice displacements from their static stationary values are given by
$$
M\omega^{2}\delta\boldsymbol{u}(\boldsymbol{r};\omega)=\sum_{\boldsymbol{R}}\mathcal{W}(\boldsymbol{r};\boldsymbol{R})\delta\boldsymbol{u}(\boldsymbol{R};\omega),\tag{2.7}
$$
where the $2\times2$ matrices $\mathcal{W}(\boldsymbol{r};\boldsymbol{R})$ are defined in terms of electronic wave functions $\{\phi_{v}\}$ and eigenenergies $\{\varepsilon_{v}\}$ in the absence of phonon excitations as follows,
$$
\begin{aligned}
\mathcal{W}_{a,b}(\boldsymbol{r};\boldsymbol{R})=&2\alpha^{2}\sum_{v}\sum_{\mu(\neq v)}\frac{f(\varepsilon_{v})}{\varepsilon_{v}-\varepsilon_{\mu}}\\
&\times\left[\phi_{\mu}(\boldsymbol{r})\left(\phi_{v}(\boldsymbol{r}+\boldsymbol{e}_{a})-\phi_{v}(\boldsymbol{r}-\boldsymbol{e}_{a})\right)\right.\\
&\left.+\phi_{v}(\boldsymbol{r})\left(\phi_{\mu}(\boldsymbol{r}+\boldsymbol{e}_{a})-\phi_{\mu}(\boldsymbol{r}-\boldsymbol{e}_{a})\right)\right]\\
&\times\left[\phi_{\mu}(\boldsymbol{R})\left(\phi_{v}(\boldsymbol{R}+\boldsymbol{e}_{b})-\phi_{v}(\boldsymbol{R}-\boldsymbol{e}_{b})\right)\right.\\
&\left.+\phi_{v}(\boldsymbol{R})\left(\phi_{\mu}(\boldsymbol{R}+\boldsymbol{e}_{b})-\phi_{\mu}(\boldsymbol{R}-\boldsymbol{e}_{b})\right)\right]\\
&+K\delta_{a,b}\left(-\delta_{\boldsymbol{r}+\boldsymbol{e}_{a},\boldsymbol{R}}+2\delta_{\boldsymbol{r},\boldsymbol{R}}-\delta_{\boldsymbol{r}-\boldsymbol{e}_{a},\boldsymbol{R}}\right).\quad(2.8)
\end{aligned}
$$

Here $a$ and $b$ stand for $x$ or $y$, $f(\varepsilon_{v})$ being the Fermi distribution function with zero chemical potential due to the electron–hole symmetry of the system. If we note the form of the electronic wave functions eq. (2.6), it is straightforward to conclude that the linear modes are also classified into $N$ groups, each of which involves only the wave vectors of the form $(q,q+q')$ $[q=2\pi n/N,\ n=-(N/2-1),\dots,$ $N/2]$, $q'$ being the group index and given by $q'=2\pi n'/N$ with an integer $n'$ $[0\leq n'<N]$ [see Fig. 1(b)].

Therefore the normal mode amplitudes can be expressed in the following form,
$$
\begin{aligned}
\delta u_{a}(\boldsymbol{r};q',\omega)=&\sum_{q}\mathcal{g}_{a}(q;q',\omega)\\
&\times\exp\left[\mathrm{i}(q\boldsymbol{e}_{x}+(q+q')\boldsymbol{e}_{y})\cdot\boldsymbol{r}\right],\tag{2.9}
\end{aligned}
$$
for a group indicated by $q'$, where $a$ is $x$ or $y$ and the coefficients $\mathcal{g}_{a}(q;q',\omega)$ are calculated from the following eigenvalue equations,
$$
\begin{aligned}
&\omega^{2}\mathcal{g}_{a}(q_{1};q',\omega)\\
&\quad=\sum_{b=x,y}\sum_{q_{2}}\mathcal{K}_{a,b}(q_{1},q_{2};q')\mathcal{g}_{b}(q_{2};q',\omega).\tag{2.10}
\end{aligned}
$$

Here $\mathcal{K}_{a,b}(q_{1},q_{2};q')$ are $2N\times2N$ matrices, the explicit form of which is given by
$$
\begin{aligned}
\mathcal{K}^{a,b}(q_{1},q_{2},q')=&\frac{4\alpha^{2}}{MN^{2}}\sum_{u_{1},u_{2},p}\sum_{n_{1},n_{2}}\left\{\frac{f(\varepsilon_{u_{1},p})-f(\varepsilon_{u_{2},p+q'})}{\varepsilon_{u_{1},p}-\varepsilon_{u_{2},p+q'}}\right.\\
&\times A_{u_{1},p}^{*}(k_{n_{1}})A_{u_{2},p+q'}(k_{n_{1}}+q_{1})\\
&\times\left[\sin(\boldsymbol{k}_{n_{1},p}\cdot\boldsymbol{e}_{a})-\sin(\boldsymbol{k}_{n_{1},p}\cdot\boldsymbol{e}_{a}+q_{1})\right]\\
&\left.\times A_{u_{1},p}(k_{n_{2}})A_{u_{2},p+q'}^{*}(k_{n_{2}}+q_{2})\right.
\end{aligned}
$$

![](./images/812304422443941889_2.jpg)

Fig. 2. The temperature dependence of eigenvalues $\omega^{2}$ for the group with $q'=0$, i.e., for those modes involving only the wave numbers satisfying $q_{x}=q_{y}$, around $T_{c}$. The system size is $8 \times 8$, and the dimensionless coupling constant $\lambda=0.65$, for which the transition temperature is given by $k_{\mathrm{B}} T_{\mathrm{c}} / t_{0}=0.362$. Below $T_{\mathrm{c}}$ there are multimode lattice distortions; as typical examples we treat the distortion patterns with wave vectors (a) $\boldsymbol{Q}$ and $\boldsymbol{Q} / 2$ and (b) $\boldsymbol{Q}, \boldsymbol{Q} / 4$ and $3 \boldsymbol{Q} / 4$, respectively. The data for $T>T_{\mathrm{c}}$ are also plotted for reference. The continuous curves are obtained by putting $\omega^{2}$ in increasing order at each temperature.

$$
\begin{aligned}
& \times\left[\sin \left(\boldsymbol{k}_{n_{2}, p} \cdot \boldsymbol{e}_{b}\right)-\sin \left(\boldsymbol{k}_{n_{2}, p} \cdot \boldsymbol{e}_{b}+q_{2}\right)\right] \\
& +\frac{f\left(\varepsilon_{u_{1}, p}\right)-f\left(\varepsilon_{u_{2}, p-q^{\prime}}\right)}{\varepsilon_{u_{1}, p}-\varepsilon_{u_{2}, p-q^{\prime}}} \\
& \times A_{u_{1}, p}\left(k_{n_{1}}\right) A_{u_{2}, p-q^{\prime}}^{*}\left(k_{n_{1}}-q_{1}\right) \\
& \times\left[\sin \left(\boldsymbol{k}_{n_{1}, p} \cdot \boldsymbol{e}_{a}\right)-\sin \left(\boldsymbol{k}_{n_{1}, p} \cdot \boldsymbol{e}_{a}-q_{1}\right)\right] \\
& \times A_{u_{1}, p}^{*}\left(k_{n_{2}}\right) A_{u_{2}, p-q^{\prime}}\left(k_{n_{2}}-q_{2}\right) \\
& \left.\times\left[\sin \left(\boldsymbol{k}_{n_{2}, p} \cdot \boldsymbol{e}_{b}\right)-\sin \left(\boldsymbol{k}_{n_{2}, p} \cdot \boldsymbol{e}_{b}-q_{2}\right)\right]\right\} \\
& +\frac{K}{M}\left[1-\cos q_{1}\right] \delta_{b, x} \delta_{q_{1}, q_{2}} \\
& +\frac{K}{M}\left[1-\cos \left(q_{1}+q^{\prime}\right)\right] \delta_{b, y} \delta_{q_{1}, q_{2}}. \quad(2.11)
\end{aligned}
$$

The derivation of the above matrix elements is rather tedious but straightforward if we notice the structure of the electronic wave functions eq. (2.6). The eigenvalue $\omega^{2}$ and the eigenvector $\left\{g_{a}(q ; q', \omega)\right\}$ can be obtained by diagonalizing these $2 N \times 2 N$ matrices for each fixed value of $q'$.

## 3. Results

As described in the previous section, we have to obtain the static lattice distortions and corresponding electronic wave functions. Since there are many different patterns of lattice distortions in the temperature region below $T_{\mathrm{c}}$, it is also necessary to fix the pattern. The self-consistent equations for the lattice distortions and the electronic wave functions are solved by iteration. The choice of pattern is made by selecting appropriately the initial values of the Fourier components of distortions. Once we obtain the information about the electronic states in the presence of the static distortions, it is straightforward to calculate the matrix elements $\mathcal{K}_{a, b}(q_{1}, q_{2} ; q')$ which are necessary to derive the phonon normal modes, as stated in the previous section.

In Fig. 2, we show as typical examples the temperature dependence of square frequencies for the normal modes within the group with $q'=0$ in the presence of multimode distortions with wave vectors (a) $\boldsymbol{Q}=(\pi, \pi)$ and $\boldsymbol{Q}/2=(\pi/2, \pi/2)$, and (b) $\boldsymbol{Q}=(\pi, \pi), \boldsymbol{Q}/4=(\pi/4, \pi/4)$ and $3 \boldsymbol{Q}/4=(3\pi/4, 3\pi/4)$, respectively. The system size is assumed to be $8 \times 8$ here for simplicity. The dimensionless coupling constant $\lambda \equiv \alpha^{2}/K t_{0}$ is fixed to be 0.65 here. The transition temperature for this value of $\lambda$ is given by $k_{\mathrm{B}} T_{\mathrm{c}} / t_{0}=0.362$. In Fig. 2, we have also plotted the square frequencies in the temperature region higher than $T_{\mathrm{c}}$ for reference.

The continuous curves in Fig. 2 are obtained by putting the eigenvalues $\omega^{2}$ in increasing order at each temperature. In general there is degeneracy; for example the horizontal straight line at $\omega^{2}=0$ includes two uniform modes ($q_{x}=q_{y}=0$). From the numerical data, we find that $10(=N+2)$ modes have zero value at $T=T_{\mathrm{c}}$. These modes are consisting of two uniform modes, two $\boldsymbol{Q}$-modes (transverse and longitudinal) and six other transverse modes, though the meaning of "transverse" and "longitudinal" is not quite clear in the temperature region below $T_{\mathrm{c}}$. Thus the multimode phonon softening is realized not only in the higher temperature region but also in the lower temperature region when $T$ approaches $T_{\mathrm{c}}$. These behaviors have also been confirmed for the system size $16 \times 16$ and for different possible patterns of distortions. We did not show the plot of the data for this larger system size in order to avoid figures with too many lines.

The examples shown in Fig. 2 indicate that the eigenfrequency spectrum depends on the distortion pattern. In order to see the pattern dependence of the phonon dispersion relations, we consider, as simplest examples, two distortion patterns whose Fourier components consist of wave vectors (a) $\boldsymbol{Q}$ and $\boldsymbol{Q}/2$ and (b) $\boldsymbol{Q}, \boldsymbol{Q}/4$ and $3 \boldsymbol{Q}/4$ as depicted in Fig. 3. Due to the presence of lattice distortions, the basic vectors in the reciprocal lattice space become $\boldsymbol{K}_{1}=(0,2\pi)$ and $\boldsymbol{K}_{2}=\boldsymbol{Q}/2=(\pi/2, \pi/2)$ in the case of (a), and $\boldsymbol{K}_{1}=(0,2\pi)$ and $\boldsymbol{K}_{2}=\boldsymbol{Q}/4=(\pi/4, \pi/4)$ in the case of (b), respectively. Generally, $\boldsymbol{K}_{1}$ can be chosen as one of the basic reciprocal lattice vectors for the original square lattice and $\boldsymbol{K}_{2}$ as the shortest wave vector for which the Fourier component of the distortions is finite. The primitive cell for the real space lattice can be constructed through the standard relations between the real and reciprocal lattice basic vectors. $^{14)}$ In the case of the pattern (a), there are four

![](./images/812304422443941889_3.jpg)

Fig. 3. The Fourier components of lattice distortions for different distortion patterns with wave vectors (a) $\boldsymbol{Q}$ and $\boldsymbol{Q}/2$ and (b) $\boldsymbol{Q}$, $\boldsymbol{Q}/4$ and $3\boldsymbol{Q}/4$, respectively. The arguments of the Fourier components of lattice distortions are also plotted. In both cases, the left hand side figures indicate the amplitudes and the right hand side the arguments of Fourier component $x_q$ (the symbol +) and $y_q$ (the symbol $\times$).

![](./images/812304422443941889_4.jpg)

Fig. 4. The primitive cells in the presence of multimode lattice distortions for the patterns (a) $\boldsymbol{Q}$ and $\boldsymbol{Q}/2$ and (b) $\boldsymbol{Q}$, $\boldsymbol{Q}/4$ and $3\boldsymbol{Q}/4$, respectively.

original lattice points within the primitive cell, and in the case of (b), there are eight original lattice points in the primitive cell as shown in Fig. 4. If we notice the modified periodicity in the presence of the distortions, the phonon eigenmodes are found to be specified by wave numbers $q$ ($|q| \leq |\boldsymbol{K}_2|/2$) and $q'$ (the group index), and expanded as

![](./images/812304422443941889_5.jpg)

Fig. 5. The phonon dispersion relations in the presence of different patterns of lattice distortions at $T=0$. The dimensionless electron-lattice coupling constant is $\lambda=0.65$ and the system size is $N \times N=64 \times 64$. Similarly as in Fig. 2 we take two different patterns of lattice distortions with wave vectors (a) $\boldsymbol{Q}$ and $\boldsymbol{Q}/2$ and (b)$\boldsymbol{Q}$, $\boldsymbol{Q}/4$ and $3\boldsymbol{Q}/4$, respectively. The horizontal axis is the wave number $q$ in the unit of $2\pi/N$ and the group index $q'$ is fixed to be 0. For both patterns (a) and (b), only the positive half of the first Brillouine zone, with the reduced zone scheme is shown.

$$
\begin{aligned}
\delta u_{a}(\boldsymbol{r}, q, q', \omega)= & \sum_{n=0}^{n_{\max }} v_{a}\left(n, q, q', \omega\right) \\
& \times \exp \left[\mathrm{i}\left(n \boldsymbol{K}_{2}+q \boldsymbol{e}_{x}+q \boldsymbol{e}_{y}+q' \boldsymbol{e}_{y}\right) \cdot \boldsymbol{r}\right], \\
& (a=x, y), \quad (3.1)
\end{aligned}
$$

where the integer $n_{\max }$ is chosen to satisfy $(n_{\max }+1)\boldsymbol{K}_{2}=2\boldsymbol{Q}$. For each $q$ value, there exist $2(n_{\max }+1)$ eigenfrequencies and corresponding eigenmodes. The eigenfrequencies can be plotted as functions of $q$ for each fixed value of $q'$ or as functions of $q'$ for each fixed value of $q$. In the case of patterns (a) and (b), the value of $n_{\max }$ is equal to 3 and 7, respectively. When we plot the phonon dispersion relations along the $\boldsymbol{K}_2$-axis in the first Brillouin zone the number of branches is $2(3+1)=8$ for the pattern (a) and $2(7+1)=16$ for the pattern (b), respectively.

In Fig. 5, we show examples of phonon dispersions for the cases (a) and (b), where the square frequencies are plotted as functions of $q$ by fixing $q'$ to be 0. The system size is chosen

to be $64 \times 64$ and the dimensionless electron-lattice coupling constant is set to be $\lambda = 0.65$. Because of the inversion symmetry, it suffices to show only the half of the first Brillouin zone. The number of branches within the first Brillouin zone is found to be 8 for the pattern (a) and 16 for the pattern (b) as discussed above.

Since different distortion patterns necessarily introduce different Brillouin zones, it is not easy to see the pattern dependence of the phonon dispersions from the data within the first Brillouin zone. Therefore we draw the dispersion of Fig. 5 in the extended zone scheme in Fig. 6, where the positive half of the first Brillouin zone of the original square lattice without distortion is shown for the wave vectors of the form $(q, q)$. The values of parameter are the same as in Fig. 5. Even in this extended zone scheme there are two branches corresponding to the "longitudinal" and "trans- verse" modes in the case without any distortion; they are expressed by the solid and broken lines, respectively, in Fig. 6. In the case of the pattern (a) we can see a phonon gap at the zone boundary $q = \pi/2$ ($qN/2\pi = 16$) for each branch and in the case of the pattern (b) three phonon gaps at zone boundaries $q = \pi/4$, $\pi/2$ and $3\pi/4$ ($qN/2\pi = 8, 16$ and 24) for each branch. Note that the gaps at $q = \pi/4$ in the case of the pattern (b) are so small that it is not easy to see them from Fig. 6(b) particularly for the lower branch. Nevertheless we can confirm them by numerical data. On the other hand, we find no gap at the zone boundaries at $q = \pi/4$ and $3\pi/4$ in the case of the pattern (a) and at $q = \pi/8, 5\pi/8$ and $7\pi/8$ in the case of (b). It will be clear that the phonon dispersion depends on the distortion pattern. This dependence is expected to be useful in determining experimentally which distortion pattern is realized in the lower temperature region.

There is also a possibility of lifting degeneracy of different patterns by taking account of the quantum correction for the ground state energy which is given by the sum of frequencies over all the modes multiplied by $\hbar/2$. This type of quantum correction was discussed in 1D systems in connection to the formation energy of a soliton or a polaron in polyacetylene. $^{15,16)}$ We have calculated this quantum correction for different system sizes and for different patterns. However, the system size dependence seems not simple. In some cases the simplest pattern of the distortions with the wave vectors $\boldsymbol{Q}$ and $\boldsymbol{Q}/2$ has the lowest quantum correction, but in other cases a more complicated pattern has the lowest. It would be necessary to study systematic dependence of the quantum correction on the system size and also on the coupling constant, before we can deduce a decisive conclusion on which pattern has the lowest ground state energy when the quantum correction is taken into account. This investigation is left for future works.

![](./images/812304422443941889_6.jpg)

Fig. 6. The phonon dispersion relations in the presence of different patterns of lattice distortions at $T = 0$ in the extended zone scheme. The solid line and broken lines represent two different branches corresponding to the "longitudinal" and "transverse" modes. The conditions of calculations are the same as in Fig. 5. Note that in (b) there is a small phonon gap at $q = \pi/4$ ($qN/2\pi = 8$) for each branch.

### 4. Summary and Discussion

The phonon dispersion relations in the 2D Peierls phase have been studied numerically. In this paper we focused on the 2D version of the SSH model with a half-filled electronic band, in which the lowest energy (or free energy) state at temperatures lower than a critical temperature of the Peierls transition is accompanied by multimode lattice distortions with the wave vector $\boldsymbol{Q} = (\pi, \pi)$, the nesting vector, and those parallel to $\boldsymbol{Q}$. When the temperature is raised from below the critical temperature $T_{\rm c}$, it has been confirmed the multimode phonon softening with the wave vectors of softening phonon modes being parallel to $\boldsymbol{Q}$ (including $\boldsymbol{Q}$ itself), which is consistent with our previous report $^{9)}$ having treated phonon dispersion relations in the temperature region higher than $T_{\rm c}$. As a supplement to the previous work, $^{9)}$ we

have presented the analytic expression concerning the $q$-dependence of the square eigenfrequencies for the transverse phonon modes with wave vectors $q_x = q_y = q$ at temperatures higher than $T_\text{c}$; it indicates that, as far as the $q$-dependence is concerned, the frequencies for these modes behaves similarly as in the case without the electron-lattice coupling. Namely the frequencies for those modes can be expressed as products of a temperature-dependent and $q$-independent prefactor and the frequencies of free phonons. This behavior certifies that the frequencies of all those modes vanish at the same critical temperature as concluded from the numerical data in the previous work.

It will be clear from those behaviors of the phonon frequencies that we have to consider multimode lattice distortions with the wave number $\boldsymbol{Q}$ and with those parallel to $\boldsymbol{Q}$ in the low temperature Peierls phase, as done in a series of previous works,${}^{8,10,12)}$ at least when we treat the 2D version of the SSH model.

Furthermore we have shown that there is the dependence of the phonon dispersion on the distortion pattern in the multimode Peierls phase, although the different multimode states have the same ground state energy and in addition the gap structure of the electronic energy spectrum is independent of the pattern of the lattice distortions.${}^{8,10)}$ The difference of dispersion relations appears in the size of the first Brillouin zone and in the number of branches, the latter reflecting the number of original lattice points in the primitive cell.

We have shown a part of phonon dispersions for two different distortion patterns in the reduced zone scheme and in the extended zone scheme. Particularly the dispersion curves in the extended zone scheme clearly indicate that the phonon dispersions depend on the distortion patterns.

This fact suggests that, if we take account of the quantum corrections for the ground state energy, there is a possibility to lift the degeneracy among the different distortion patterns in the multimode Peierls phase. Nevertheless, the present status of the data shows non-systematic system size dependence and in the present work we have not considered the coupling constant dependence of the phonon dispersions. Because of these ambiguities, we could not deduce any conclusion about whether the degeneracy might be lifted by the quantum corrections. A systematic research on this possibility is left for future works.

The present results for the phonon structure in the multimode Peierls phase will be useful when we consider in the future the dynamics of nonlinear localized excitations in 2D systems such as polarons in 1D electron-lattice systems.

### Acknowledgements

The authors are grateful to Professor A. Terai (Osaka City University) and H. Watanabe for useful comments and discussions. Present work is partially supported by Grants-in-Aid for Scientific Research (Nos. 14540365 and 16540329) from the Ministry of Education, Culture, Sports, Science and Technology.

1) W. P. Su, J. R. Schrieffer and A. J. Heeger: Phys. Rev. Lett. **42** (1979) 1698; W. P. Su, J. R. Schrieffer and A. J. Heeger: Phys. Rev. B **22** (1980) 2099.
2) S. Tang and J. E. Hirsh: Phys. Rev. B **37** (1987) 584.
3) S. Mazumdar: Phys. Rev. B **39** (1989) 12324.
4) S. Tang and J. E. Hirsh: Phys. Rev. B **39** (1989) 12327.
5) K. Yuan and T. Kopp: Phys. Rev. B **65** (2002) 85102.
6) T. Sasaki and N. Toyota: Synth. Met. **70** (1995) 849.
7) K. Miyagawa, A. Kawamoto and K. Kanoda: Phys. Rev. B **56** (1997) R8487.
8) Y. Ono and T. Hamano: J. Phys. Soc. Jpn. **69** (2000) 1769.
9) S. Chiba and Y. Ono: J. Phys. Soc. Jpn. **72** (2003) 1995.
10) T. Hamano and Y. Ono: J. Phys. Soc. Jpn. **70** (2001) 1849.
11) In ref. 10, there is a misprint; $_{N/2}\text{C}_{N/4} \simeq N^{N/4}$ should be replaced by $_{N/2}\text{C}_{N/4} \simeq 2^{N/2}$.
12) T. Hamano and Y. Ono: Physica E **22** (2004) 156.
13) S. Chiba and Y. Ono: Physica E **22** (2004) 152.
14) C. Kittel: *Introduction to Solid State Physics* (John Wiley & Sons, New York, 1996) 7th ed.
15) H. Takayama, Y. R. Lin-Liu and K. Maki: Phys. Rev. B **21** (1980) 2388.
16) A. Terai and Y. Ono: J. Phys. Soc. Jpn. **55** (1986) 213.