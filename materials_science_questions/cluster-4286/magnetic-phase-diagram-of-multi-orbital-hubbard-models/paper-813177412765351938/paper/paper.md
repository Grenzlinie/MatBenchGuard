# Superconductivity in an extended Hubbard model with attractive interaction

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2011 Supercond. Sci. Technol. 24 035004

(http://iopscience.iop.org/0953-2048/24/3/035004)

View [the table of contents for this issue](), or go to the [journal homepage]() for more

Download details:

IP Address: 137.99.31.134
This content was downloaded on 22/05/2015 at 02:08

Please note that [terms and conditions apply]().

# Superconductivity in an extended Hubbard model with attractive interaction

E J Calegari¹, S G Magalhães², C M Chaves³ and A Troper³

¹ Laboratório de Teoria da Matéria Condensada, Departamento de Física–UFSM, 97105-900, Santa Maria, RS, Brazil
² Instituto de Física, Universidade Federal Fluminense, Avenida Litorânea s/n, 24210-346 Niterói, Rio de Janeiro, Brazil
³ Centro Brasileiro de Pesquisas Físicas, Rua Xavier Sigaud 150, 22290-180, Rio de Janeiro, RJ, Brazil

E-mail: cmch@cbpf.br

Received 28 September 2010, in final form 25 November 2010
Published 23 December 2010
Online at stacks.iop.org/SUST/24/035004

## Abstract
In this work, a two-dimensional one-band Hubbard model is investigated within a two-pole approximation. The model presents a non-local attractive potential $U$ ($U < 0$) that allows the study of d-wave superconductivity and also includes hopping up to second-nearest neighbors. The two-pole scheme has been proposed to improve the Hubbard-I approximation. The analytical results show a more complex form for the gap $\Delta(T)$, when compared to the one obtained in the latter approximation. Indeed, new anomalous correlation functions associated with the superconductivity are involved in the calculation of $\Delta(T)$. Numerical results in a range of temperatures are presented. Moreover, the structure of the quasiparticle bands and the topology of the Fermi surface are studied in detail in the normal state. Connections with some experimental results are also included.

(Some figures in this article are in colour only in the electronic version)

---

## 1. Introduction
Superconductivity in strongly correlated systems is a field with plenty of challenging problems. Several non-usual properties of high temperature superconductors (HTSC) [1] still needed to be properly clarified. In particular, some experimental systems exhibit important deviations from the standard BCS theory. For instance, the superconductor gap behavior as a function of temperature in some borocarbides display a non-monotonic feature at lower temperatures. In fact, such a gap increases [2] in $\text{RNi}_2\text{B}_2\text{C}$ ($\text{R} = \text{Dy}, \text{Ho}, \text{Er}, \text{Tm}$) and $\text{ErNi}_2\text{B}_2\text{C}$ when the temperature decreases towards $T = 0$. This effect is ascribed to a competition between the superconductivity and weak antiferromagnetic correlations, which are absent in a weak coupling standard BCS superconductivity, appearing naturally from the formulation presented in this work. Another quite interesting feature of HTSC systems is the behavior found in some cuprates [3] in the low doping region, which gives rise to an anomalous Fermi surface leading to a pseudo-gap (pseudogap regime).

In this very complex problem, a number of theories have been proposed in order to explain the presence of a pseudo-gap region [1]. Here we claim that the appearance of a pseudo-gap can be ascribed to a more detailed many-body treatment in which superconductor and AF correlations compete.

Although a BCS-like approach [4] has been widely used to describe these physical systems, it is well recognized that superconductivity is a two-dimensional problem in which strong correlations play a fundamental role [5]. Thereby, we apply a two-pole approximation [6–8] to deal with the strong interaction coupling. Here we consider a d-wave symmetry gap and, therefore, a non-local attractive interaction is used [9, 10]. The net attractive interaction ($U < 0$) may result, for example, from the elimination of the electron–phonon-like coupling through a canonical transformation [11] or, alternatively, from an electronic mechanism proposed by Hirsch [12] which may produce, for a certain range of parameters, an effective attractive interaction.

In this work, we focused on the many-body renormalized normal state of these systems. Our Fermi surface obtained is consistent with recent claims in the literature [3, 13] about the presence of hole pockets due to antiferromagnetic correlations. Moreover, we discuss some thermodynamical properties of the superconducting regime, namely the critical temperature $T_\text{c}$,

the zero-temperature superconducting gap $\Delta_0$ and temperature dependence of the gap $\Delta(T)$ for various dopings $\delta \equiv 1 - n_T$ (with $n_T = n_\sigma + n_{-\sigma}$) and interaction $U$. The $n_\sigma$ represents the average occupation per site of electrons with spin $\sigma = \uparrow, \downarrow$.

This paper is organized as follows. In section 2, we present a general formulation describing the model as well as the ingredients of the normal state, e.g. the quasiparticle and the special characteristics of the Fermi surface (FS). In section 3, we present the equations describing the superconducting state which appears from the application of the two-pole approximation. In section 4, we exhibit self-consistent numerical results and conclusions for both the normal and the superconducting states. Appendix A briefly describes the main points involved in the two-pole approach whereas in appendix B the correlation functions involved in the Green's functions governing the superconducting and the normal states are displayed.

### 2. General formulation

The Hamiltonian studied here is, in standard notation:
$$
H = \sum_{\langle\langle ij \rangle\rangle \sigma} t_{ij} d_{i\sigma}^\dagger d_{j\sigma} + U \sum_{\langle ij \rangle \sigma} n_{i,\sigma}^d n_{j,-\sigma}^d - \mu \sum_{i\sigma} d_{i\sigma}^\dagger d_{i\sigma} \quad (1)
$$
where $\langle\langle \cdot \cdot \rangle\rangle$ indicates the sum over the first-and the second-nearest neighbors of $i$ and $\mu$ is the chemical potential. The two-dimensional dispersion relation is given by
$$
\varepsilon_{\vec{k}} = 2t(\cos(k_x a) + \cos(k_y a)) + 4t_2 \cos(k_x a) \cos(k_y a). \quad (2)
$$

In the present work, we adopted the two-pole approximation [6, 7] which consists in choosing a set of operators describing the most important excitations of the system. The details of the method are given in appendix A. The set of operators considered is $\{d_{i,\sigma}, n_{i,-\sigma}^d d_{i,\sigma}, d_{i,-\sigma}^\dagger, n_{i,\sigma}^d d_{i,-\sigma}^\dagger\}$. The first two are associated with the normal state whereas the last two are associated with the superconductivity [7, 8]. Following the method exhibited in appendix A, the one-particle Green's function for the normal state is
$$
G_{N\sigma}^{dd}(\vec{k}, \omega) = \frac{Z_{1\vec{k}\sigma}}{\omega - \omega_{1\vec{k}\sigma}} + \frac{Z_{2\vec{k}\sigma}}{\omega - \omega_{2\vec{k}\sigma}} \quad (3)
$$
with
$$
Z_{1\vec{k}\sigma} = \frac{1}{2} + \frac{\bar{U} - 2U_1 - \varepsilon_{\vec{k}} + W_{\vec{k}\sigma}}{2X_{\vec{k}\sigma}}, \quad (4)
$$
$$
Z_{2\vec{k}\sigma} = 1 - Z_{1\vec{k}\sigma} \quad (5)
$$
and
$$
\bar{U} = \frac{U_2 + n_{-\sigma}(U_1 - 2U_2)}{n_{-\sigma}(1 - n_{-\sigma})}. \quad (6)
$$

The quasiparticle bands are
$$
\omega_{1\vec{k}\sigma} = \frac{\bar{U} + \varepsilon_{\vec{k}} - 2\mu + W_{\vec{k}\sigma}}{2} - \frac{X_{\vec{k}\sigma}}{2}, \quad (7)
$$
$$
\omega_{2\vec{k}\sigma} = \omega_{1\vec{k}\sigma} + X_{\vec{k}\sigma} \quad (8)
$$
where
$$
X_{\vec{k}\sigma} = \sqrt{(\bar{U} - \varepsilon_{\vec{k}} + W_{\vec{k}\sigma})^2 + 4U_1(\varepsilon_{\vec{k}} - W_{\vec{k}\sigma}) + \tilde{U}} \quad (9)
$$
and
$$
\tilde{U} = \frac{4U_2(U_2 - U_1)}{n_{-\sigma}(1 - n_{-\sigma})}. \quad (10)
$$

The effective interactions $U_1, U_2$ and the band shift $W_{\vec{k}\sigma}$ are defined in appendix A (equations (A.5)–(A.7)). Here, as we are assuming a paramagnetic state of a translationally invariant system, $\langle n_{i,\sigma} \rangle = \langle n_{i,-\sigma} \rangle = \langle n_{-\sigma} \rangle$. It should be noticed that, due to many-body effects, in the pole structure of the Green's functions in the normal paramagnetic phase, there is a spin–spin correlation function which exhibits antiferromagnetic (AF) short range correlations but a global paramagnetic state holds. Moreover, in order to simplify the notation, we write $\langle n_{-\sigma} \rangle = n_{-\sigma}$. From the Green's function in equation (3), we find the spectral function
$$
A_\sigma(\vec{k}, \omega) = -\frac{1}{\pi} \text{Im}[G_{N\sigma}^{dd}(\vec{k}, \omega)]. \quad (11)
$$

The Fermi surface is obtained from $A_\sigma(\vec{k}, \omega = 0)$.

### 3. The superconducting state

In the superconducting state, the Green's function $G^{dd}$ is written as
$$
G_{S\sigma}^{dd}(\vec{k}, \omega) = \frac{A'(\omega) - (\omega + E_{11})(1 + n_{-\sigma}^2 \frac{U}{\theta})^2 \Delta_{\vec{k}}^2}{P(\omega)} \quad (12)
$$
where
$$
A'(\omega) = \alpha_0 + \alpha_1 \omega + \alpha_2 \omega^2 + \alpha_3 \omega^3 \quad (13)
$$
with
$$
\alpha_0 = (E_{12}^2 - E_{11}E_{22})(E_{22} - 2n_{-\sigma}E_{12} + n_{-\sigma}^2 E_{11}) \quad (14)
$$
$$
\begin{aligned}
\alpha_1 &= 2n_{-\sigma} \tilde{n} E_{11} E_{12} - (\tilde{n} + 2n_{-\sigma})n_{-\sigma} E_{12}^2 - n_{-\sigma}^3 E_{11}^2 \\
&- E_{22}[E_{22} + 2n_{-\sigma}(n_{-\sigma}E_{11} - 2E_{12})]
\end{aligned} \quad (15)
$$
$$
\alpha_2 = n_{-\sigma}^2 (1 - n_{-\sigma})^2 E_{11} \quad (16)
$$
$$
\alpha_3 = n_{-\sigma}^2 (1 - n_{-\sigma})^2 \quad (17)
$$
and $\tilde{n} = (1 + n_{-\sigma})$. The $E_{nm}$ are elements of the energy matrix (A.2) and the quantity $P(\omega)$, is defined as
$$
\begin{aligned}
P(\omega) &= [(\omega - E_{11})(n_{-\sigma}\omega - E_{22}) - (n_{-\sigma}\omega - E_{12})^2] \\
&\quad \times [(\omega + E_{11})(n_{-\sigma}\omega + E_{22}) - (n_{-\sigma}\omega + E_{12})^2] \\
&\quad + \Delta_{\vec{k}}^2(A_1 - A_2 \omega)
\end{aligned} \quad (18)
$$
with
$$
A_1 = a_0 + a_1 \frac{U}{\theta} + \left[ a_2 + \Delta_{\vec{k}}^2 \left(1 + n_{-\sigma}^2 \frac{U}{\theta}\right)^2 \right] \left( \frac{U}{\theta} \right)^2 \quad (19)
$$

![](./images/813177412765351938_1.jpg)

Figure 1. The spectral function $A(\vec{k}, \omega=0)$ representing the Fermi surface for different dopings $\delta=1-n_T$. The model parameters considered here are $U=8t$, $t=-1.0$ eV, $t_2=0.3|t|$ and $k_{\rm B}T=0.1|t|$ ($k_{\rm B}$ is the Boltzmann constant).

and
$$
A_{2}=\left(1+n_{-\sigma}^{2} \frac{U}{\theta}\right)^{2}+n_{-\sigma}^{2}\left(1-n_{-\sigma}\right)^{2}\left(\frac{U}{\theta}\right)^{2}. \tag{20}
$$

The quantities $a_0$, $a_1$, $a_2$ and $\theta$ are given by
$$
a_{0}=E_{11}^{2} \tag{21}
$$
$$
a_{1}=2 E_{12}\left(2 n_{-\sigma} E_{11}-E_{12}\right) \tag{22}
$$
$$
a_{2}=E_{22}^{2}-4 n_{-\sigma} E_{12} E_{22}+2 n_{-\sigma}^{2}\left(E_{12}^{2}+E_{11} E_{22}\right) \tag{23}
$$
and
$$
\theta=t n_{01 \sigma}-U\left(D_{01 \sigma}+2\left\langle S_{1}^{z} S_{0}^{z}\right\rangle\right) \tag{24}
$$
with the correlation functions $n_{01\sigma}$ and $D_{01\sigma} \langle S_1^z S_0^z \rangle$ defined in appendix B.

The main reason that we are adopting the d-wave symmetry is that we are following [7] where it is claimed that for a large number of HTSC materials d-wave gap symmetry is the most relevant. Moreover, the d-wave symmetry follows also from the fact that in our Hamiltonian we consider an attractive delocalized interaction term. Actually the extended s-wave symmetry is more favored for an attractive local interaction as discussed in [16].

For d-wave symmetry, the gap function is
$$
\Delta_{\vec{k}}=2 \Delta\left[\cos \left(k_{x}\right)-\cos \left(k_{y}\right)\right], \tag{25}
$$
where $\Delta$ is the gap function amplitude. Following the procedure described in [7, 8], the self-consistent gap function has been obtained from the Green's function:
$$
G_{\sigma}^{d d^{\dagger}}(\vec{k}, \omega)=-\frac{\Delta_{\vec{k}}\left(\beta_{0}+\beta_{1} \omega^{2}\right)}{P(\omega)} \tag{26}
$$
in which
$$
\Delta=-2 \theta \Delta \frac{1}{L} \sum_{\vec{q}}\left[\cos \left(q_{x}\right)-\cos \left(q_{y}\right)\right]^{2} F_{1 \vec{q} \sigma} \tag{27}
$$
and
$$
F_{1 \vec{q} \sigma}=\frac{1}{2 \pi \mathrm{i}} \oint f(\omega)\left[\frac{\beta_{0}+\beta_{1} \omega^{2}}{P(\omega)}\right] \mathrm{d} \omega. \tag{28}
$$

The $\beta_0$ and $\beta_1$ are
$$
\beta_{0}=n_{-\sigma}^{2}\left(1-n_{-\sigma}\right)^{2} \frac{U}{\theta} \tag{29}
$$
$$
\beta_{1}=E_{1}^{2}-\left[E_{2}^{2}-2 E_{1} E_{2}+\Delta_{\vec{q}}^{2}\left(1+n_{-\sigma}^{2} \frac{U}{\theta} 1\right)\right]^{2} \frac{U}{\theta} \tag{30}
$$
with $E_{1}=E_{12}-n_{-\sigma} E_{11}$ and $E_{2}=E_{22}-n_{-\sigma} E_{12}$.

### 4. Self-consistent results and conclusions

Firstly, we discuss the numerical results for the normal state ($T>T_c$). Figure 1 shows the FS for four different doping

![](./images/813177412765351938_2.jpg)

Figure 2. The quasiparticle bands intercepted by the chemical potential $(\mu=0)$. The model parameters and the temperature are the same as in figure 1.

values $\delta$. In (a), $\delta=0.30$, a well defined electron-like FS is found. However, in (b) when $\delta$ is decreased to $\delta=0.20$, the topology of the FS changes, with the emergence of a hole pocket enclosing the nodal point $(\frac{\pi}{2},\frac{\pi}{2})$. As a consequence, due to low spectral intensity, a pseudo-gap appears near the antinodal points $(\pi,0)$ and $(0,\pi)$. Further decrease in $\delta$ intensifies the presence of the pseudo-gap as shown in (c) and (d). This unusual behavior is due to the strong antiferromagnetic correlations coming from the band shift $W_{k\sigma}^{d}$ (see [7,14]) defined in equation (A.7).

The effects described above are corroborated by the quasiparticle band calculation exhibited in figure 2 which displays the quasiparticle band for distinct doping values $\delta$. In fact, while in the higher doping regime the quasiparticle bands cross the Fermi level near $(\frac{\pi}{2},\frac{\pi}{2})$ and near the antinodal point $(0,\pi)$, in the lower doping regime the quasiparticle band crosses the Fermi level only near the nodal point $(\frac{\pi}{2},\frac{\pi}{2})$. Such a behavior gives rise to a pocket around $(\frac{\pi}{2},\frac{\pi}{2})$. On the other hand, as the quasiparticle band does not touch the Fermi level near $(0,\pi)$, a pseudo-gap emerges in that region. As far as we know, the emergence of the pseudo-gap due to an attractive $U$ in a strong correlated regime is presented for the first time here. This is in accordance with experiments [13]. The kink observed near the $(\pi,\pi)$ point of the quasiparticle band is caused by the strong antiferromagnetic correlations associated with $\langle \vec{S}_j \cdot \vec{S}_i \rangle$, which are maximum in $\mathbf{Q}=(\pi,\pi)$. The $\mathbf{Q}$ is the antiferromagnetic wavevector.

Now we discuss some thermodynamical properties associated with the superconducting state. In figure 3 we describe the gap function amplitude $\Delta(T)$ for $U=8t$ and two different occupations $n_T$, in the lower doping regime. One sees that, for a given $U$ (in a characteristic strong coupling regime $|\frac{U}{t}| \gg 1$), the zero-temperature gap for $n_T=0.90$ is higher than the corresponding one for $n_T=0.80$. Furthermore, the temperature where a non-superconducting phase arises is higher for $n_T=0.90$, i.e. $T_{\rm c}(n_T=0.90) > T_{\rm c}(n_T=0.80)$. In both cases, in the region of low $T$, there is a increase in the value of the gap amplitude as compared to the zero-gap amplitude value. This unusual behavior is due to the effect of the strong correlations, since in the standard BCS weak correlated regime, $\Delta(0)$ is always greater than $\Delta(T)$. As mentioned in section 1 this behavior is observed experimentally in some HTSC materials [2].

We stress that in our case this non-monotonic behavior at low temperatures is mainly due to correlation functions in the pole structure of the superconducting Green's function (see equations (12) and (26)). To be more precise, we have found in our self-consistent calculation a complex interplay between the SC gap behavior and the AF-type short range correlations.

Figure 4 displays the value of the gap amplitude $\Delta(T)$ as a function of temperature for several values of $U$, in the strong correlation regime $(|\frac{U}{t}| \gg 1)$. In all cases, for $n_T=0.90$, we note that, when $U$ increases, $T_{\rm c}$ also increases, and the same unusual behavior for $\Delta(T)$ appears for very low $T$. We have calculated the gap function amplitude for several values

![](./images/813177412765351938_3.jpg)

Figure 3. The main figure shows the gap function amplitude versus the temperature for $U=8t, t=-1.0$ eV, $t_2=0.3|t|$ and two different occupations $n_T$. The small figures show the regions of low temperatures where the gap presents an unusual behavior.

![](./images/813177412765351938_4.jpg)

Figure 4. The main figure shows the gap function amplitude versus the temperature for $n_T = 0.90$ and different values of $U$. The remaining parameters are identical to figure 3. The small figures show the regions of low temperatures for two values of $U$. For low temperatures, the gap presents an unusual behavior.

![](./images/813177412765351938_5.jpg)

Figure 5. The difference between $\Delta_{\text{max}}$ and $\Delta_0$ as a function of $|\frac{U}{t}|$. The inset shows that $\Delta_{\text{max}}$ and $\Delta_0$ have been obtained.

of $U$ and $n_T$ ($n_T = 0.80$ and 0.70), and the same behavior is observed.

A very interesting result is shown in figure 5. Here we plot $\Delta_{\text{max}}-\Delta_0$ for several values of $|\frac{U}{t}|$. When $U$ increases $\Delta_{\text{max}}-\Delta_0$ increases also, until a special value (here $|\frac{U}{t}|8$) where $\Delta_{\text{max}}-\Delta_0$ is a maximum and then $\Delta_{\text{max}}-\Delta_0$ tends toward zero for very high values of $U$. When such behavior appears, one has attained the $|U| \to \infty$ limit. Moreover, it should be noted that this unusual behavior occurs for a critical low value of $|U|$, (in our calculation $|\frac{U}{t}| \simeq 4$), which is a signature of the onset of a characteristic $|\frac{U}{t}| \gg 1$, signaling the appearance of a strong correlation regime.

Our results are in qualitatively agreement concerning the Fermi surface in the underdoping region with other approaches using the $t$-$J$ model [17]. The reason for such agreement is that in both approaches the AF spin-spin correlation functions renormalize the band structure, giving rise to the appearance of hole pockets.

Finally, in order to complement our present calculations, we need to discuss the higher doping regime $n_T \lesssim 0.80$ as well as the behavior of $T_{\text{c}}$ as a function of doping. Moreover, a detailed discussion of the effect of external pressure, which affects mainly [15] the ratio $\frac{n}{t}$, is needed. These further calculations are now in progress.

### Appendix A. Two-pole approximation

In the present two-pole approximation [6, 7], the Green's functions are defined as
$$
\mathbf{G}(\omega)=\mathbf{N}(\omega \mathbf{N}-\mathbf{E})^{-1} \mathbf{N} \tag{A.1}
$$
where $\mathbf{E}$ and $\mathbf{N}$ are the energy and the normalization matrices given by
$$
E_{n m}=\langle\left[\left[A_{n}, H\right]_{-}, A_{m}^{\dagger}\right]_{(+)}\rangle \tag{A.2}
$$
and
$$
N_{n m}=\langle\left[A_{n}, A_{m}^{\dagger}\right]_{(+)}\rangle. \tag{A.3}
$$

In equations (A.2) and (A.3), $[\dots,\dots]_{(+)_{-}}$ denote the (anti)commutator and $\langle\cdots\rangle$ the thermal average. The set of operators $\{A_{n}\}$ must satisfy, within some approximation, the relation $[A_{n}, H]_{-}=\sum_{m} K_{n m} A_{m}$.

For the normal state of the model (1), the energy matrix is given by
$$
\mathbf{E}=\left[\begin{array}{cc}
\varepsilon_{\vec{k}}-\mu+U_{1} & \varepsilon_{\vec{k}}-\mu+U_{2} \\
\varepsilon_{\vec{k}}-\mu+U_{2} & \varepsilon_{\vec{k}} n_{\sigma}^{2}-\mu+U_{2}+\bar{n} W_{\vec{k} \sigma}
\end{array}\right] \tag{A.4}
$$
with
$$
U_{1}=2 U \sum_{l}\langle n_{l,-\sigma}\rangle, \tag{A.5}
$$

$$
U_{2}=2 U \sum_{l}\left\langle n_{l,-\sigma} n_{l,-\sigma}\right\rangle \tag{A.6}
$$

and $\bar{n}=n_{-\sigma}\left(1-n_{-\sigma}\right)$. The correlation function $D_{i l-\sigma}=$ $\left\langle n_{i-\sigma} n_{l-\sigma}\right\rangle$ is defined in equation (B.3). The band shift $W_{k \sigma}$ can be written as
$$
\bar{n} W_{k \sigma}^{d}=-\sum_{\langle\langle j \neq 0\rangle\rangle} t_{0 j}\left(n_{0 j \sigma}-2 m_{0 j \sigma}\right)+\sum_{\langle\langle j \neq 0\rangle\rangle} t_{0 j} \mathrm{e}^{\vec{i} \vec{k} \cdot \vec{R}_{j}} h_{j \sigma} \tag{A.7}
$$
with $n_{i j \sigma}, m_{i j \sigma}$ and $h_{j \sigma}$ defined below.

### Appendix B. Correlation functions

The correlation function $n_{i j \sigma}=\left\langle d_{i \sigma}^{\dagger} d_{j \sigma}\right\rangle$ is given by
$$
n_{i j \sigma}=\frac{1}{2 \pi \mathrm{i} L} \sum_{\vec{k}} \oint \mathrm{e}^{\mathrm{i} \vec{k} \cdot\left(\vec{R}_{j}-\vec{R}_{i}\right)} f(\omega) G_{S \sigma}^{d d}(\vec{k}, \omega) \mathrm{d} \omega \tag{B.1}
$$
with $G_{S \sigma}^{d d}$ defined in equation (12). Assuming $i=0$ and $t_{0 j}=t$ for the $z$ nearest neighbors, only one value of $n_{0 j \sigma}$, namely $n_{01 \sigma}$, is necessary. Considering the same for the second-nearest neighbors $t_{2}$, we have
$$
n_{01 \sigma}=\frac{1}{2 \pi \mathrm{i} L} \sum_{\vec{k}} \oint \frac{\epsilon_{\vec{k}}}{\left(t+t_{2}\right) z} f(\omega) \mathrm{d} \omega. \tag{B.2}
$$

By using the original Roth scheme [6], the correlation function $D_{i j \sigma}=\left\langle n_{i \sigma} n_{j \sigma}\right\rangle$ is calculated and written as
$$
D_{i j \sigma}=n_{\sigma}^{2}-\frac{\alpha_{i j \sigma} n_{i j \sigma}+\beta_{i j \sigma} m_{i j \sigma}}{1-\beta_{i i, \sigma} \beta_{i i,-\sigma}} \tag{B.3}
$$
with $m_{i j \sigma}=\left\langle d_{i \sigma}^{\dagger} n_{j-\sigma} d_{j \sigma}\right\rangle$ given by
$$
m_{i j \sigma}=\frac{1}{2 \pi \mathrm{i} L} \sum_{\vec{k}} \oint \mathrm{e}^{\mathrm{i} \vec{k} \cdot\left(\vec{R}_{j}-\vec{R}_{i}\right)} f(\omega) G_{S \sigma}^{n 2 d}(\vec{k}, \omega) \mathrm{d} \omega \tag{B.4}
$$
and
$$
\alpha_{i j \sigma}=\frac{n_{i j \sigma}-m_{i j \sigma}}{1-n_{-\sigma}} \tag{B.5}
$$
$$
\beta_{i j \sigma}=\frac{m_{i j \sigma} / n_{-\sigma}-n_{i j \sigma}}{1-n_{-\sigma}}. \tag{B.6}
$$

The $D_{01 \sigma}$ can be obtained assuming again $i=0$ and $t_{0 j}=t$ for the $z$ nearest neighbors, as has been done in $n_{01 \sigma}$.

The Green's function $G_{S \sigma}^{n 2 d}$ in (B.4) is
$$
G_{S \sigma}^{n 2 d}(\vec{k}, \omega)=\frac{n_{-\sigma}\left[A^{\prime \prime}(\omega)-A^{\prime \prime \prime}(\omega)\left(1+n_{-\sigma}^{2} \frac{U}{\theta}\right) \Delta_{k}^{2}\right]}{P(\omega)} \tag{B.7}
$$
where
$$
A^{\prime \prime}(\omega)=\gamma_{0}+\gamma_{1} \omega+\gamma_{2} \omega^{2}+\gamma_{3} \omega^{3} \tag{B.8}
$$
with
$$
\gamma_{0}=\left(E_{12}^{2}-E_{11} E_{22}\right)\left[E_{3}+n_{-\sigma}\left(E_{12}-E_{11}\right)\right] \tag{B.9}
$$
$$
\begin{aligned}
\gamma_{1}= & n_{-\sigma} E_{11}\left[E_{12}\left(1+3 n_{-\sigma}\right)-n_{-\sigma}\left(E_{11}+\tilde{n} E_{22}\right)\right] \\
& +E_{22} E_{3}+n_{-\sigma} E_{12}\left(3 E_{3}-n_{-\sigma} E_{12}\right)
\end{aligned} \tag{B.10}
$$
$$
\gamma_{2}=n_{-\sigma}\left(1-n_{-\sigma}\right)^{2} E_{12} \tag{B.11}
$$
$$
\gamma_{3}=n_{-\sigma}^{2}\left(1-n_{-\sigma}\right)^{2}. \tag{B.12}
$$

The quantities $E_{3}$ and $\tilde{n}$ are
$$
E_{3}=E_{22}-E_{12} \quad \text { and } \quad \tilde{n}=1+n_{-\sigma}. \tag{B.13}
$$

The term $A^{\prime \prime \prime}$ introduced in equation (B.7) is defined as
$$
A^{\prime \prime \prime}(\omega)=\omega\left(1+n_{-\sigma}^{2} \frac{U}{\theta}\right)+E_{11}+\frac{U}{\theta}\left[n_{-\sigma}\left(E_{12}+E_{11}\right)-E_{12}\right]. \tag{B.14}
$$

The denominator of the Green's function $G^{n 2 d}$ is given in equation (18).

The term $h_{j \sigma}$ presented in the band shift (A.7) is given by
$$
h_{j \sigma}=B_{j \sigma}+\left\langle\vec{S}_{j} \cdot \vec{S}_{0}\right\rangle \tag{B.15}
$$
with
$$
\begin{aligned}
B_{j \sigma} & =-\left\langle S_{j}^{z} S_{0}^{z}\right\rangle-\frac{\alpha_{j \sigma} n_{0 j \sigma}^{d}+\beta_{j \sigma} m_{j \sigma}}{1-\beta_{\sigma} \beta_{-\sigma}} \\
& -\frac{\alpha_{j \sigma} n_{0 j-\sigma}^{d}+\beta_{j \sigma}\left(n_{0 j-\sigma}^{d}-m_{j-\sigma}\right)}{1-\beta_{\sigma}}
\end{aligned} \tag{B.16}
$$
and
$$
\left\langle\vec{S}_{j} \cdot \vec{S}_{0}\right\rangle=\frac{1}{2}\left(\left\langle S_{j}^{+} S_{0}^{-}\right\rangle+\left\langle S_{j}^{-} S_{0}^{+}\right\rangle\right)+\left\langle S_{j}^{z} S_{0}^{z}\right\rangle. \tag{B.17}
$$

In particular, in the paramagnetic state, $\left\langle S_{j}^{+} S_{0}^{-}\right\rangle=\left\langle S_{j}^{-} S_{0}^{+}\right\rangle$, then $\left\langle\vec{S}_{j} \cdot \vec{S}_{0}\right\rangle$ can be written as
$$
\left\langle\vec{S}_{j} \cdot \vec{S}_{0}\right\rangle=\left\langle S_{j}^{+} S_{0}^{-}\right\rangle+\left\langle S_{j}^{z} S_{0}^{z}\right\rangle \tag{B.18}
$$
where
$$
\left\langle S_{j}^{+} S_{0}^{-}\right\rangle=\left\langle d_{j \sigma}^{\dagger} d_{j-\sigma} d_{0-\sigma}^{\dagger} d_{0 \sigma}\right\rangle=-\frac{\alpha_{j \sigma} n_{0 j,-\sigma}^{d}+\beta_{j, \sigma} m_{j,-\sigma}}{1+\beta_{\sigma}} \tag{B.19}
$$
and
$$
\begin{aligned}
\left\langle S_{j}^{z} S_{0}^{z}\right\rangle & =\frac{\left(1-\beta_{-\sigma}\right)}{2}\left[\left(n_{\sigma}^{d}\right)^{2}-\frac{\alpha_{j \sigma} n_{0 j \sigma}+\beta_{j \sigma} m_{j \sigma}}{1-\beta_{\sigma} \beta_{-\sigma}}\right] \\
& -\frac{\alpha_{-\sigma} n_{\sigma}^{d}}{2}.
\end{aligned} \tag{B.20}
$$

The correlation functions $n, m, \alpha$ and $\beta$ are defined in equations (B.1), (B.4), (B.5) and (B.6), respectively.

In order to calculate $n_{i j \sigma}$ and $m_{i j \sigma}$ in the normal state, it is necessary to consider $\Delta=0$ in the Green's functions $G_{S \sigma}^{d d}$ and $G_{S \sigma}^{n 2 d}$ defined in equations (12) and (B.7). In this case, $G_{S \sigma}^{d d} \rightarrow G_{N \sigma}^{d d}$ and $G_{S \sigma}^{n 2 d} \rightarrow G_{N \sigma}^{n 2 d}$.

### References

[1] Lee P A, Nagaosa N and Wen X-G 2006 Rev. Mod. Phys. 78 17

[2] Baba T et al 2008 Phys. Rev. Lett. 100 017003
Naidyuk Y G et al 2009 J. Phys.: Conf. Ser. 150 052178

[3] Kanigel A et al 2006 Nat. Phys. 2 447

[4] Japiassu G M, Continentino M A and Troper A 1992 Phys. Rev. B 45 2986

[5] Dagotto E 1994 Rev. Mod. Phys. 66 763

[6] Roth L M 1969 Phys. Rev. 184 451

[7] Beenen J and Edwards D M 1995 Phys. Rev. B 52 13636

[8] Calegari E J, Magalhaes S G and Gomes A A 2005 Eur. Phys. J. B 45 485

[9] Caixeiro E S and Troper A 2009 *J. Appl. Phys.* **105** 07E307

[10] Caixeiro E S and Troper A 2010 *Phys. Rev. B* **82** 014502

[11] Kittel C 1963 *Quantum Theory of Solids* (New York: Wiley) p 150

[12] Hirsch J E 1988 *Theories of High Temperature Superconductivity* ed J Woods Halley (Reading, MA: Addison-Wesley) p 241

[13] Harrison N, McDonald R D and Singleton J 2007 *Phys. Rev. Lett.* **99** 206406

Doiron-Leyraud N *et al* 2007 *Nature* **447** 565

[14] Calegari E J and Magalhaes S G 2010 *Int. J. Mod. Phys. B* at press

[15] Angilella G G N, Pucci R and Siringo F 1996 *Phys. Rev. B* **54** 15471

[16] Caixeiro E S and Troper A 2009 *Physica B* **404** 3102

[17] Korshunov M M and Ovchinnikov S G 2007 *Eur. Phys. J. B* **57** 271

Sakai S, Motome Y and Imada M 2009 *Phys. Rev. Lett.* **102** 056404

Sakai S, Motome Y and Imada M 2010 *Phys. Rev. B* **82** 134505