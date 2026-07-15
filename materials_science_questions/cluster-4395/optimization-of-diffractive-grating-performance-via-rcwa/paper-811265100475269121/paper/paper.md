# Bi-Directional Coupler as a Mode-Division Multiplexer/Demultiplexer

Hossam M. H. Shalaby, Senior Member, *IEEE*

Abstract—A bi-directional coupler supported with Bragg grat- ing is proposed as a mode-division multiplexer/demultiplexer. The structure can demultiplex 3 modes with only two waveguides and a Bragg grating. The input waveguide is multimode, while the output waveguide is single-mode. Both first- and second order modes of the input waveguide are coupled to the output waveguide, propagating at opposite directions, while the fun- damental mode is kept in the input waveguide. A theoretical analysis of the proposed demultiplexer is developed based on the perturbative mode-coupled theory. The insertion losses of both first- and second order modes are derived under suitable phase-matched conditions. Expressions of the insertion losses are obtained for simple slab-waveguides coupler. Numerical results of the proposed demultiplexer are presented for the slab- waveguides coupler under different design parameters. Further- more, the wavelength dependence of the device is addressed under mismatching conditions and a Lorentzian model of the Silicon material. In addition, FDTD simulation of proposed demultiplexer is performed to prove the validity of the proposed concept. Return loss due to reflection to the source is taken into consideration in the simulation in addition to the device wavelength dependence.

Index Terms—Bragg grating, coupled-mode equations, direc- tional coupler, integrated optics devices, mode chart, mode- division demultiplexer, mode-division multiplexer, optical inter- connects, space-division multiplexing.

## I. INTRODUCTION
PACE-DIVISION multiplexing increases the capacity of a single optical fiber, which would cope with current increase in the demand of high transmission rates [1]. Multiple modes can be used in a few-mode fiber in order to achieve space-division multiplexing (SDM) [2]. In addition, SDM technology is also becoming attractive for optical interconnects in data centers [3], [4].

Mode-division multiplexers (MDMs) are getting increasing interest in recent years in order to multiplex several modes in a single fiber [3], [5]–[20]. Ding *et al.* have demonstrated an on-chip two-mode division multiplexing circuit using a tapered directional coupler-based $TE_0$ and $TE_1$ mode multi- plexer and demultiplexer on the silicon-on-insulator platform [6]. In [7], Dai *et al.* have demonstrated experimentally a small silicon mode (de)multiplexer with cascaded asymmet- rical directional couplers. A simple and low-crosstalk silicon mode (de)multiplexer based on multimode grating-assisted- couplers has been proposed in [8]. Luo *et al.* have shown the first microring-based on-chip WDM-compatible mode-division multiplexing with low modal crosstalk and loss [11]. Dorin and Ye have presented a design and fabrication of a two-mode SOI ring resonator for MDM systems [13]. Gui *et al.* have fabricated an on-chip two-mode multiplexer/demultiplexer us- ing a tapered asymmetrical grating-assisted contra-directional coupler-based [18].

In this paper, we propose a simple mode-division multi- plexer/demultiplexer using a bi-directional coupler supported with a Bragg grating. We call it here bi-directional mode- division multiplexer (BMDM). The structure can demultiplex 3 modes with only two waveguides and a Bragg grating. The advantage of this device is that it has a simple structure and is compact in size, which is only several micrometers in length for silicon. The idea is that a single waveguide is used to carry two different modes in two opposite directions, rather than using a single waveguide for each mode. In addition, the device is expandable and forms a building block for higher order multiplexing. We develop a theoretical analy- sis of the proposed demultiplexer based on the perturbative mode-coupled theory. The insertion losses of both first- and second order modes are derived under suitable phase-matched conditions. Expressions of the insertion losses are obtained for simple slab-waveguides coupler. In addition, we present a simple design problem for the slab-waveguides coupler and evaluate numerically simultaneous insertion losses of both first- and second order modes. In our analysis, we neglect the effect of return loss (due to reflected waves in the main waveguide) in order to simplify the analysis and have more insight. Furthermore, the wavelength dependence of the device is addressed by considering mismatching conditions and a Lorentzian model of the Silicon material. In addition, FDTD simulation of proposed BMDM is performed to prove the validity of the proposed concept. Return loss due to reflection to the source is taken into consideration in the simulation. Two different examples are presented illustrating two differ- ent concepts in the design. The crosstalks and wavelength dependence of the device are addressed in the simulation as well. Although the focus in this paper is on the demultiplexer design, the structure also works as a multiplexer by inverting the inputs and outputs. Our results reveal that the proposed device can achieve acceptable values of both insertion losses and crosstalks, yet its size is very compact.

The remaining of this paper is organized as follows. The structure of the proposed demultiplexer is described in Section II. The theoretical analysis of the BMDM and derivation of

Manuscript received April 18, 2016; revised June 7, 2016; accepted June 8, 2016.

Hossam M. H. Shalaby is with the Department of Electronics and Com- munications Engineering, Egypt-Japan University of Science and Technology (E-JUST), Alexandria 21934, Egypt, on leave from the Electrical Engineering Department, Alexandria University, Alexandria 21544, Egypt (e-mail: shal- aby@ieee.org).

corresponding coupled-mode equations are given in Section III. Section IV is devoted for the solution of the coupled- mode equations and the derivation of the insertion losses for both first- and second-order modes. In Section V, we present some numerical results of the proposed BMDM with slab waveguides under different design parameters. FDTD simulations of proposed BMDM are performed in this section as well. Our concluding remarks are given in Section VI.

## II. BMDM STRUCTURE

Figure 1 shows the structure of proposed bi-directional coupler (BMDM) for use as a mode-division multiplexer in op- tical communications systems. The structure can demultiplex 3 modes with only two waveguides and a Bragg grating. The input waveguide is multimode, while the output waveguide is single-mode. Both first- and second order modes of the input waveguide are coupled to the output waveguide, propagating at opposite directions, while the fundamental mode is kept in the main input waveguide. Each waveguide sees perturbations in both $x$ and $z$ directions. The periodic dielectric perturbation of the Bragg grating can be created by surface corrugation using photolithographic techniques. The widths of the multimode and single-mode guiding layers are $w$ and $d$, respectively. The period of the Bragg grating is $\Lambda$ and the coupling length is $L$. The gap between the two guiding layers is $r$ and the depth of the grating teeth is $t \leq r$.

![](./images/811265100475269121_1.jpg)

Fig. 1: A bi-directional coupler used as a mode-division multiplexer.

A similar structure, that uses two single-mode waveguides, has been adopted in other applications [21], [22]. Shi et al. have demonstrated 4-port, electrically tunable photonic filters using silicon contra-directional couplers with uniform and phase-shifted waveguide Bragg gratings [21].

Using the perturbation approach, the refractive index of the BMDM (perturbed) structure can be written as:
$$
n^{2}(x, z)=n_{\text {multi }}^{2}(x)+\Delta n^{2}(x, z), \tag{1}
$$
where $n_{\text{multi}}(x)$ is the refractive index for the unperturbed multimode waveguide structure, Fig. 1:
$$
n_{\text {multi }}^{2}(x)= \begin{cases}n_{1}^{2} ; & |x| \leq w / 2, \\ n_{2}^{2} ; & \text { otherwise. }\end{cases} \tag{2}
$$

Here $n_1$ and $n_2$ are the refractive indices of the waveguide materials. From Fig. 1 and assuming that $L \gg \Lambda$, the periodic dielectric perturbation of the refractive index can be expanded using the Fourier series as:
$$
\Delta n_{\text {multi }}^{2}(x, z)=
\begin{cases}
\sum_{\nu=-\infty}^{\infty} b_{\nu} e^{-j \nu(2 \pi / \Lambda) z} ; & |x-w / 2-r / 2| \leq t / 2, \\
2 b_{0} ; & |x-w / 2-r-d / 2| \leq d / 2, \\
0 ; & \text { otherwise, }
\end{cases}
\tag{3}
$$
where
$$
b_{\nu}=\frac{n_{1}^{2}-n_{2}^{2}}{2} \operatorname{sinc}(\nu / 2), \quad \nu \in\{\ldots,-1,0,1, \ldots\}. \quad(4)
$$

Similarly, for the single-mode waveguide of the BMDM:
$$
n_{\text {single }}^{2}(x)= \begin{cases}n_{1}^{2} ; & |x-w / 2-r-d / 2| \leq d / 2, \\ n_{2}^{2} ; & \text { otherwise. }\end{cases} \tag{5}
$$

Using the Fourier series, we get:
$$
\Delta n_{\text {single }}^{2}(x, z)=
\begin{cases}
\sum_{\nu=-\infty}^{\infty} b_{\nu} e^{-j \nu(2 \pi / \Lambda) z} ; & |x-w / 2-r / 2| \leq t / 2, \\
2 b_{0} ; & |x| \leq w / 2, \\
0 ; & \text { otherwise. }
\end{cases}
\tag{6}
$$

## III. THEORETICAL ANALYSIS

In this section, we aim at obtaining analytical expressions for the insertion losses of the proposed device when exciting it with either the first- or second order mode. The analysis is developed based on the perturbative mode-coupled theory and the expressions of the insertion losses are obtained for simple slab-waveguides coupler. We neglect the effect of return loss in order to simplify the analysis and have more insight. The wavelength dependence of the device is addressed by considering mismatching conditions and a Lorentzian model of the Silicon material. In our analysis, we consider TE modes only. The input electric field to the multimode waveguide of the BMDM can be written as:
$$
E_{i}=\sum_{m=0}^{2} \mathcal{E}_{m}(x) e^{-j \beta_{m} z}, \tag{7}
$$
where for any $m \in\{0,1,2\}$, $\mathcal{E}_m(x)$ is the electric field profile of the $m$th TE mode ($\text{TE}_m$) and $\beta_m = 2\pi n_{\text{eff}_m}/\lambda_0$ is the corresponding propagation constant. Here, $\lambda_0$ is the operating wavelength and $n_{\text{eff}_m}$ is the effective index of $\text{TE}_m$ at input waveguide of width $w$. The field profiles are orthogonal and each mode field is normalized (corresponding to a power flow of one watt per unit width in $y$ direction). That is, for any $n,m \in\{0,1,2\}$:
$$
\int \mathcal{E}_{n}^{*}(x) \mathcal{E}_{m}(x) \mathrm{d} x=\frac{2 \omega \mu_{0}}{\beta_{m}} \delta_{n m}, \tag{8}
$$
where $\delta_{nm}$ is the Kronecker delta, $\mu_0=4\pi \times 10^{-7}\ \text{H/m}$ is the permeability of free space, and $\omega$ is the angular frequency.

Let $\mathscr{E}_{0}(x)$ denote electric field profile of the fundamental mode $\text{TE}_{0}^{\text{single}}$ of the single-mode waveguide of width $d$. The width $d$ can be selected so that the effective index of mode $\text{TE}_1$ of multimode waveguide equals that of the fundamental mode

$TE_0^{\text{single}}$ of single-mode waveguide. In this case, mode $\text{TE}_1$ will mostly couple to $TE_0^{\text{single}}$. In addition, a grating coupler of period $\Lambda$ is designed so that mode $\text{TE}_2$ would couple to the contra-directional mode of the single-mode waveguide. Here, we keep it general and assume that the propagation constant $\beta_{\text{single}} = 2\pi n_{\text{eff}}^{\text{single}}/\lambda_0$, where $n_{\text{eff}}^{\text{single}}$ is the effective index of the single-mode waveguide with width $d$.

The electric field in the coupling region ($L \geq z \geq 0$) of the BMDM can be written as:

$$
\begin{aligned}
E =& \sum_{m=0}^{2} \mathcal{A}_{m}(z) \mathcal{E}_{m}(x) e^{-j \beta_{m} z} \\
&+\mathcal{B}_{0}^{+}(z) \mathscr{E}_{0}(x) e^{-j \beta_{\text{single}} z}+\mathcal{B}_{0}^{-}(z) \mathscr{E}_{0}(x) e^{+j \beta_{\text{single}} z},
\end{aligned}
\tag{9}
$$

where $\mathcal{A}_{m}(z)$, $m \in \{0,1,2\}$, is a $z$-dependent complex amplitude of the electric field of mode $m$ of the multimode waveguide, and $\mathcal{B}_{0}^{+}(z)$ and $\mathcal{B}_{0}^{-}(z)$ are the complex amplitudes of the electric fields of both codirectional and contra-directional modes of the single-mode waveguide, respectively.

### A. Coupled-Mode Equations for $\mathcal{A}_n(z)$, $n \in \{1,2\}$

Using traditional analysis of periodic perturbations in waveguides [23]–[26], we can write the corresponding coupling differential equations of the BMDM as follows:

$$
\begin{aligned}
\frac{\mathrm{d} \mathcal{A}_{n}}{\mathrm{~d} z}=&-j \frac{\omega \epsilon_{0}}{4}\left[\sum_{\nu=-\infty}^{\infty} b_{\nu}\left(\sum_{m=0}^{2} \mathcal{A}_{m}(z) \int_{|x-w / 2-r / 2| \leq t / 2}\right.\right. \\
& \left.\times \mathcal{E}_{n}^{*}(x) \mathcal{E}_{m}(x) \mathrm{d} x \cdot e^{j\left(\beta_{n}-\beta_{m}-2 \pi \nu / \Lambda\right) z}\right. \\
&+\mathcal{B}_{0}^{+}(z) \int_{|x-w / 2-r / 2| \leq t / 2} \mathcal{E}_{n}^{*}(x) \mathscr{E}_{0}(x) \mathrm{d} x \\
& \times e^{j\left(\beta_{n}-\beta_{\text{single}}-2 \pi \nu / \Lambda\right) z} \\
&+\mathcal{B}_{0}^{-}(z) \int_{|x-w / 2-r / 2| \leq t / 2} \mathcal{E}_{n}^{*}(x) \mathscr{E}_{0}(x) \mathrm{d} x \\
&\left.\times e^{j\left(\beta_{n}+\beta_{\text{single}}-2 \pi \nu / \Lambda\right) z}\right) \\
&+2 b_{0} \mathcal{B}_{0}^{+}(z) \int_{|x| \leq w / 2} \mathcal{E}_{n}^{*}(x) \mathscr{E}_{0}(x) \mathrm{d} x \cdot e^{j\left(\beta_{n}-\beta_{\text{single}}\right) z}
\end{aligned}
\tag{10}
$$

It should be noticed that the last term of the last equation cannot be neglected in general as one of the fields inside the integration is not evanescent and phase matched condition could be satisfied if $\beta_n = \beta_{\text{single}}$.

Next, we consider the last equation for two specific cases when $n \in \{1,2\}$. Here we assume the following design conditions:

$$
\begin{aligned}
\beta_{1}-\beta_{\text{single}} &=\frac{2 \pi \ell_{1}}{\Lambda} \\
\beta_{2}+\beta_{\text{single}} &=\frac{2 \pi \ell_{2}}{\Lambda},
\end{aligned}
\tag{11}
$$

for some integers $\ell_2 > \ell_1 \geq 0$.

1) Case 1: Coupled-Mode Equations for $\mathcal{A}_2(z)$: Applying conditions (11) to (10) with $n=2$ and ignoring phase unmatched terms, we get:

$$
\frac{\mathrm{d} \mathcal{A}_{2}}{\mathrm{~d} z}=-j\left[\zeta_{2}^{0} \mathcal{A}_{2}(z)+\kappa_{2}^{\ell_{2}} \mathcal{B}_{0}^{-}(z)\right],
\tag{12}
$$

where for the slab-waveguides coupler,

$$
\begin{aligned}
\zeta_{m}^{\nu} & \stackrel{\text { def }}{=} \frac{\omega \epsilon_{0}}{4} \cdot b_{\nu} \int_{|x-w / 2-r / 2| \leq t / 2}\left|\mathcal{E}_{m}(x)\right|^{2} \mathrm{~d} x \\
&=\frac{\varrho_{m}^{2} \operatorname{sinc}(\nu / 2)}{2 \beta_{m}\left(w+\frac{2}{\gamma_{m}}\right)} \cdot \frac{\sinh \left(\gamma_{m} t\right)}{\gamma_{m}} \cdot e^{-\gamma_{m} r}
\end{aligned}
\tag{13}
$$

and

$$
\begin{aligned}
\kappa_{m}^{\nu} & \stackrel{\text { def }}{=} \frac{\omega \epsilon_{0}}{4} \cdot b_{\nu} \int_{|x-w / 2-r / 2| \leq t / 2} \mathcal{E}_{m}^{*}(x) \mathscr{E}_{0}(x) \mathrm{d} x \\
&=\frac{\varrho_{m} \varrho_{\text{single}} \operatorname{sinc}(\nu / 2)}{\sqrt{\beta_{m} \beta_{\text{single}}\left(w+\frac{2}{\gamma_{m}}\right)\left(d+\frac{2}{\gamma_{\text{single}}}\right)}} \\
& \times \frac{\sinh \left[\left(\gamma_{\text{single}}-\gamma_{m}\right) t / 2\right]}{\gamma_{\text{single}}-\gamma_{m}} \cdot e^{-\left(\gamma_{\text{single}}+\gamma_{m}\right) r / 2}
\end{aligned}
\tag{14}
$$

for any $m \in \{0,1,2\}$ and any integer $\nu$. Here we have:

$$
\begin{aligned}
\varrho_{m} &=\sqrt{k_{0}^{2} n_{1}^{2}-\beta_{m}^{2}}=\frac{2 \pi}{\lambda_{0}} \sqrt{n_{1}^{2}-n_{\text{eff} m}^{2}} \\
\gamma_{m} &=\sqrt{\beta_{m}^{2}-k_{0}^{2} n_{2}^{2}}=\frac{2 \pi}{\lambda_{0}} \sqrt{n_{\text{eff} m}^{2}-n_{2}^{2}} \\
\varrho_{\text{single}} &=\sqrt{k_{0}^{2} n_{1}^{2}-\beta_{\text{single}}^{2}}=\frac{2 \pi}{\lambda_{0}} \sqrt{n_{1}^{2}-\left(n_{\text{eff}}^{\text{single}}\right)^{2}} \\
\gamma_{\text{single}} &=\sqrt{\beta_{\text{single}}^{2}-k_{0}^{2} n_{2}^{2}}=\frac{2 \pi}{\lambda_{0}} \sqrt{\left(n_{\text{eff}}^{\text{single}}\right)^{2}-n_{2}^{2}},
\end{aligned}
\tag{15}
$$

where $k_0=2\pi/\lambda_0$.

2) Case 2: Coupled-Mode Equations for $\mathcal{A}_1(z)$: Similarly, applying conditions (11) to (10) with $n=1$ and ignoring phase unmatched terms, we get:

$$
\frac{\mathrm{d} \mathcal{A}_{1}}{\mathrm{~d} z}=-j\left[\zeta_{1}^{0} \mathcal{A}_{1}(z)+\left(\kappa_{1}^{\ell_{1}}+\varsigma_{1} e^{j\left(2 \pi \ell_{1} / \Lambda\right) z}\right) \mathcal{B}_{0}^{+}(z)\right],
\tag{16}
$$

where for any $m \in \{0,1,2\}$,

$$
\begin{aligned}
\varsigma_{m} & \stackrel{\text { def }}{=} \frac{\omega \epsilon_{0}}{4} \cdot 2 b_{0} \int_{|x| \leq w / 2} \mathcal{E}_{m}^{*}(x) \mathscr{E}_{0}(x) \mathrm{d} x \\
&=\frac{\varrho_{m} \varrho_{\text{single}}\left(\gamma_{m}+\gamma_{\text{single}}\right) \cdot e^{-\gamma_{\text{single}} r}}{\left(\varrho_{m}^{2}+\gamma_{\text{single}}^{2}\right) \sqrt{\beta_{m} \beta_{\text{single}}\left(w+\frac{2}{\gamma_{m}}\right)\left(d+\frac{2}{\gamma_{\text{single}}}\right)}}.
\end{aligned}
\tag{17}
$$

Unlike most traditional assumptions in perturbative mode-coupled theory, the last term of (16) is not negligible as phase matched condition would be satisfied in the case of $\ell_1=0$.

### B. Coupled-Mode Equations for $\mathcal{B}_0^+(z)$ and $\mathcal{B}_0^-(z)$

Here we obtain the corresponding coupled-mode equations for $\mathcal{B}_0^+(z)$ and $\mathcal{B}_0^-(z)$ as we did in the last part.

### 1) Case 1: Coupled-Mode Equations for $B_0^+$:

$$
\begin{aligned}
\frac{\mathrm{d} B_0^{+}}{\mathrm{d} z}= & -j\left[\iota^{0} B_0^{+}(z)\right. \\
& \left.+\left(\left(\kappa_{1}^{\ell_{1}}\right)^{*}+\varpi_{1} e^{-j\left(2 \pi \ell_{1} / \Lambda\right) z}\right) \mathcal{A}_{1}(z)\right],
\end{aligned}
\tag{18}
$$

where for any integer $\nu$,
$$
\begin{aligned}
\iota^{\nu} & \stackrel{\text { def }}{=} \frac{\omega \epsilon_{0}}{4} \cdot b_{\nu} \int_{|x-w / 2-r / 2| \leq t / 2}\left|\mathscr{E}_{0}(x)\right|^{2} \mathrm{~d} x \\
& =\frac{\varrho_{\text {single }}^{2} \operatorname{sinc}(\nu / 2)}{2 \beta_{\text {single }}\left(d+\frac{2}{\gamma_{\text {single }}}\right)} \cdot \frac{\sinh \left(\gamma_{\text {single }} t\right)}{\gamma_{\text {single }}} \cdot e^{-\gamma_{\text {single }} r}
\end{aligned}
\tag{19}
$$

and for any $m \in \{0,1,2\}$,
$$
\begin{aligned}
\varpi_{m} & \stackrel{\text { def }}{=} \frac{\omega \epsilon_{0}}{4} \cdot 2 b_{0} \int_{|x-w / 2-r-d / 2| \leq d / 2} \mathscr{E}_{0}^{*}(x) \mathcal{E}_{m}(x) \mathrm{d} x \\
& =\frac{\varrho_{m} \varrho_{\text {single }}\left(\gamma_{m}+\gamma_{\text {single }}\right) \cdot e^{-\gamma_{m} r}}{\left(\varrho_{\text {single }}^{2}+\gamma_{m}^{2}\right) \sqrt{\beta_{m} \beta_{\text {single }}\left(w+\frac{2}{\gamma_{m}}\right)\left(d+\frac{2}{\gamma_{\text {single }}}\right)}}.
\end{aligned}
\tag{20}
$$

### 2) Case 2: Coupled-Mode Equations for $B_0^-$:

$$
\frac{\mathrm{d} B_0^{-}}{\mathrm{d} z}=j\left[\iota^{0} B_0^{-}(z)+\left(\kappa_{2}^{\ell_{2}}\right)^{*} \mathcal{A}_{2}(z)\right].
\tag{21}
$$

---

## IV. SOLUTION OF THE COUPLED-MODE EQUATIONS

From the last section, we have four coupled-mode equations as given in (12), (16), (18), and (21). The coupling coefficients $\zeta_{m}^{\nu}$, $\kappa_{m}^{\nu}$, $\varsigma_{m}$, $\iota^{\nu}$, and $\varpi_{m}$ are given in (13), (14), (17), (19), and (20), respectively.

---

### A. Solutions of $\mathcal{A}_2(z)$ and $B_0^-(z)$

#### 1) Correction to the Phase Matching Condition:
The set of equations (12), (16), (18), and (21) suggests the following corrections to the phase matching conditions:
$$
\begin{aligned}
& \beta_{1}+\zeta_{1}^{0}-\beta_{\text {single }}-\iota^{0}=\frac{2 \pi \ell_{1}}{\Lambda} \\
& \beta_{2}+\zeta_{2}^{0}+\beta_{\text {single }}+\iota^{0}=\frac{2 \pi \ell_{2}}{\Lambda}.
\end{aligned}
\tag{22}
$$

#### 2) Phase Mismatching Effect:
If further the operating wavelength is shifted from $\lambda_0$ to $\lambda$, we have the following phase mismatching effect on (12) and (21):
$$
\begin{aligned}
\frac{\mathrm{d} \mathcal{A}_{2}}{\mathrm{~d} z} & =-j \zeta_{2}^{0} \mathcal{A}_{2}(z)-j \kappa_{2}^{\ell_{2}} B_0^{-}(z) e^{j \delta_{2}(\lambda) z} \\
\frac{\mathrm{d} B_0^{-}}{\mathrm{d} z} & =j \iota^{0} B_0^{-}(z)+j\left(\kappa_{2}^{\ell_{2}}\right)^{*} \mathcal{A}_{2}(z) e^{-j \delta_{2}(\lambda) z},
\end{aligned}
\tag{23}
$$

where
$$
\begin{aligned}
\delta_{2}(\lambda) & \stackrel{\text { def }}{=} \Delta \beta_{2}-\left(\zeta_{2}^{0}+\iota^{0}\right) \\
\Delta \beta_{2} & \stackrel{\text { def }}{=} \beta_{2}^{\lambda}+\beta_{\text {single }}^{\lambda}-\left(\beta_{2}+\beta_{\text {single }}\right).
\end{aligned}
\tag{24}
$$

Here, $\beta_{2}^{\lambda}$ and $\beta_{\text{single}}^{\lambda}$ are the propagation constants of $\text{TE}_2$ mode and fundamental mode in both the multimode and single-mode waveguides, respectively, evaluated at wavelength $\lambda$. The solutions of the two coupled equations (23) are given by:

$$
\begin{aligned}
\mathcal{A}_{2}(z)= & e^{j\left(\Delta \beta_{2} / 2-\zeta_{2}^{0}\right) z} \\
& \times \frac{s_{2} \cosh s_{2}(L-z)+j \frac{\Delta \beta_{2}}{2} \sinh s_{2}(L-z)}{s_{2} \cosh s_{2} L+j \frac{\Delta \beta_{2}}{2} \sinh s_{2} L} \mathcal{A}_{2}(0)
\end{aligned}
$$

$$
B_0^{-}(z)=e^{-j\left(\Delta \beta_{2} / 2-\iota^{0}\right) z} \frac{-j\left(\kappa_{2}^{\ell_{2}}\right)^{*} \sinh s_{2}(L-z)}{s_{2} \cosh s_{2} L+j \frac{\Delta \beta_{2}}{2} \sinh s_{2} L} \mathcal{A}_{2}(0) ;
\tag{25}
$$

where
$$
s_{2} \stackrel{\text { def }}{=} \sqrt{\left|\kappa_{2}^{\ell_{2}}\right|^{2}-\left(\frac{\Delta \beta_{2}}{2}\right)^{2}}.
\tag{26}
$$

#### 3) Coupling Efficiency and Insertion Loss:
The coupling efficiency and insertion loss are defined as:
$$
\eta_{2} \stackrel{\text { def }}{=}\left|\frac{B_0^{-}(0)}{\mathcal{A}_{2}(0)}\right|^{2}=\frac{\left|\kappa_{2}^{\ell_{2}}\right|^{2} \sinh ^{2} s_{2} L}{s_{2}^{2} \cosh ^{2} s_{2} L+\left(\Delta \beta_{2} / 2\right)^{2} \sinh ^{2} s_{2} L}
$$

$$
IL_{2} \stackrel{\text { def }}{=} 10 \log \eta_{2},
\tag{27}
$$

respectively.

---

### B. Solutions of $\mathcal{A}_1(z)$ and $B_0^+(z)$

Noticing that $\varpi_{1} \approx \varsigma_{1}^{*}$ and following a similar argument to what we did in the last subsection, it can be checked that the solutions of the two equations (16) and (18) can be written as:

$$
\mathcal{A}_{1}(z)=e^{j\left(\frac{\Delta \beta_{1}}{2}-\zeta_{1}^{0}\right) z}\left(\cos s_{1} z-j \frac{\Delta \beta_{1}}{2} \frac{\sin s_{1} z}{s_{1}}\right) \mathcal{A}_{1}(0)
$$

$$
B_0^{+}(z)=-j e^{-j\left(\frac{\Delta \beta_{1}}{2}+\iota^{0}\right) z}\left(\kappa_{1}^{\prime}\right)^{*} \frac{\sin s_{1} z}{s_{1}} \mathcal{A}_{1}(0),
\tag{28}
$$

where
$$
\begin{aligned}
\Delta \beta_{1} & \stackrel{\text { def }}{=} \beta_{1}^{\lambda}-\beta_{\text {single }}^{\lambda}-\left(\beta_{1}-\beta_{\text {single }}\right) \\
s_{1} & \stackrel{\text { def }}{=} \sqrt{\left|\kappa_{1}^{\prime}\right|^{2}+\left(\frac{\Delta \beta_{1}}{2}\right)^{2}},
\end{aligned}
\tag{29}
$$

and
$$
\kappa_{1}^{\prime} \stackrel{\text { def }}{=} \begin{cases}\kappa_{1}^{0}+\varsigma_{1} ; & \text { if } \ell_{1}=0, \\ \kappa_{1}^{\ell_{1}} ; & \text { else. }\end{cases}
\tag{30}
$$

Here $\beta_{1}^{\lambda}$ is the propagation constant of $\text{TE}_1$ mode, evaluated at wavelength $\lambda$.

#### 1) Coupling Efficiency and Insertion Loss:
The corresponding coupling efficiency and insertion loss are defined as:
$$
\eta_{1} \stackrel{\text { def }}{=}\left|\frac{B_0^{+}(L)}{\mathcal{A}_{1}(0)}\right|^{2}=\frac{\left|\kappa_{1}^{\prime}\right|^{2}}{\left|s_{1}\right|^{2}} \cdot \sin ^{2} s_{1} L
\tag{31}
$$

$$
IL_{1} \stackrel{\text { def }}{=} 10 \log \eta_{1},
$$

respectively.

### V. NUMERICAL RESULTS AND FDTD SIMULATIONS

In this section, we study the performance of proposed BMDM for the case of a directional coupler with simple slab waveguides. We start by designing the device using the equations derived in the preceding sections. Next, we simulate the device based on FDTD Solutions in order to prove the validity of the proposed concept. In our results, we present two different examples illustrating two different concepts in the design. Although we only focus on a 2D design, our aim here is simply to prove the validity of the proposed concept rather than providing rigorous 3D design. In addition, since the waveguide thickness is fixed by the foundry, e.g., 220 nm, the design parameters are essentially 2D. Indeed, following the effective-index method of analysis [27], the vertical dimension ensures a single-mode operation everywhere in vertical decomposition, while the horizontal dimension determines the higher-order modes in horizontal decomposition. This renders that the 2D performance measures are good estimates to that of 3D for our device.

### A. Mode Chart of a Slab Waveguide

Figure 2 shows the mode chart for a dielectric slab waveguide with refractive indices $n_1 = 3.473$ and $n_2 = 1.444$. These are typical values of silicon and $\text{SiO}_2$ materials, respectively.

![](./images/811265100475269121_2.jpg)

Fig. 2: Mode chart for a dielectric slab with $n_1 = 3.473$ and $n_2 = 1.444$.

### B. Example 1: Slab Waveguide with three TE Modes

Here, the multimode slab waveguide is assumed to have a width of $w = 600$ nm and carries TE modes only, specifically, $\text{TE}_0$, $\text{TE}_1$, and $\text{TE}_2$. The fundamental mode $\text{TE}_0$ is kept through the waveguide, while the other two modes are coupled to a single-mode waveguide, which width $d$ is to be determined. The operating wavelength is 1550 nm. The corresponding coupling coefficients are evaluated from (13), (14), (17), (19), and (20).

### C. Effective Indices

The effective indices of the three modes of the multimode waveguide can be determined from the chart as: $n_{\text{eff}0} = 3.32$, $n_{\text{eff}1} = 2.83$, and $n_{\text{eff}2} = 1.9$.

### D. Width of Single-Mode Waveguide

In this example, we select $\ell_1 = 0$ and $\ell_2 = 1$ in (22). Accordingly, we can determine the effective index and width of the single-mode waveguide as $n_{\text{eff}}^{\text{single}} = 2.93$ and $d = 250$ nm, respectively.

### E. Grating Period

From (22), we can determine the grating period as follows:

$$
\begin{align*}
\Lambda &= \frac{2\pi}{\beta_2 + \beta_{\text{single}} + \zeta_2^0 + \iota^0} = \left[ \frac{n_{\text{eff}2} + n_{\text{eff}}^{\text{single}}}{\lambda_0} + \frac{\zeta_2^0 + \iota^0}{2\pi} \right]^{-1} \\
&= \left[ \frac{1}{328\ \text{nm}} + \frac{\zeta_2^0 + \iota^0}{2\pi} \right]^{-1}.
\end{align*}
\tag{32}
$$

The grating period is plotted in Fig. 3 versus coupler gap $r$ at different values of grating teeth depth $t$. It is clear that the grating period is a convex function of $r$. For any given value of $r$, it is a decreasing function of $t$. It is easy to check that if $t = r$, then both $\zeta_2^0$ and $\iota^0$ are increasing functions in the coupler gap $r$ and in turn $\Lambda$ is a decreasing function in $r$ as shown in Fig. 3. Its maximum value is 328 nm and its global minimum value is:

$$
\begin{align*}
\Lambda_{\text{min}} = \Bigg[ &\frac{1}{328\ \text{nm}} + \frac{1}{2\pi} \cdot \frac{\varrho_2^2}{4\beta_2\gamma_2 \left( w + \frac{2}{\gamma_2} \right)} \\
&\times \frac{\varrho_{\text{single}}^2}{4\beta_{\text{single}}\gamma_{\text{single}} \left( d + \frac{2}{\gamma_{\text{single}}} \right)} \Bigg]^{-1} = 309.18\ \text{nm}.
\end{align*}
\tag{33}
$$

![](./images/811265100475269121_3.jpg)

Fig. 3: Grating period of proposed BMDM versus coupler gap at different values of grating teeth depth $t$.

![](./images/811265100475269121_4.jpg)

Fig. 4: (a) Insertion loss of second-order mode of BMDM versus coupler gap at different values of coupling length $L$. (b) Insertion losses of both first- and second-order modes of BMDM versus coupling length $L$ at optimum coupler gap $r_{opt}=136.13$ nm. (c) Insertion losses of both first- and second-order modes of BMDM versus wavelength $\lambda$ at optimum coupler gap $r_{opt}=136.13$ nm.

## F. Insertion Losses

In this subsection we evaluate the insertion losses for $t=r$ in order to get lowest values of grating periods, which reduces the size of the demultiplexer. Figure 4(a) shows the insertion loss $IL_2$ of the second-order mode as given from (27) (with phase matching condition $\Delta\beta_2=0$) versus the coupler gap $r$ at three different values of coupling length $L\in\{5\Lambda_{\text{min}},10\Lambda_{\text{min}},20\Lambda_{\text{min}}\}$. It can be seen from the figure that the magnitude of insertion loss $IL_2$ decreases as the coupler gap $r$ increases until it reaches a minimum value and then start increasing. This can be explained as follows. For small values of $r$, the size of the grating is small and many rays would miss the regions of refractive index change. As $r$ increases, most of the rays would not miss and the coupling increases. Increasing $r$ even more would make the single-mode waveguide far from the multimode waveguide and coupling would start to decrease back. In addition, one can notice that the coupling increases with increasing the coupling length $L$ as expected. It is interesting to notice that the optimum value of the gap $r_{opt}$ that minimizes the magnitude of the insertion losses is independent of the coupling length and can be obtained by differentiating (14) with respect to $r$:

$$
r_{opt}=\frac{\log\left(\gamma_{\text{single}}/\gamma_m\right)}{\gamma_{\text{single}}-\gamma_m}.\tag{34}
$$

For our example, $r_{opt}=136.13$ nm and the corresponding grating period $\Lambda=313.02$ nm.

In Fig. 4(b) we plot the insertion losses $IL_1$ and $IL_2$ of both first- and second-order modes as given in (31) and (27), respectively (with phase matching), versus the coupling length $L$ for the optimum coupler gap $r_{opt}=136.13$ nm. As expected the insertion loss of the first-order mode is periodic with period:

$$
L_x^{opt}=\frac{\pi}{s_1|_{\Delta\beta_1=0}}=\frac{\pi}{|\kappa_1^0+\varsigma_1|}=22.29\Lambda_{\text{min}}.\tag{35}
$$

In order to have suitable values of both $IL_1$ and $IL_2$ simultaneously, we choose a coupling length that satisfies the condition $IL_1=IL_2$. This can be achieved, for example, at $L=34\Lambda_{\text{min}}$.

1) Wavelength Dependence of BMDM: In order to measure the wavelength dependence of the device, we study (27) and (31) with same aforementioned parameters but under mismatching conditions. In addition, a dispersive and lossless Silicon material is assumed with refractive index following a Lorentzian model:

$$
n_1^2(\lambda)=\epsilon+\frac{\epsilon_{Lorentz}\omega_0^2}{\omega_0^2-2j\delta_0\left(\frac{2\pi c}{\lambda}\right)-\left(\frac{2\pi c}{\lambda}\right)^2},\tag{36}
$$

where the permittivity $\epsilon=7.9874$, Lorentz permit- tivity $\epsilon_{Lorentz}=3.6880$, Lorentz resonance $\omega_0=3.9328\times10^{15}$ rad/s, and damping rate $\delta_0=0$. The results are plotted in Fig. 4(c) for the insertion losses versus wavelength $\lambda$. It can be seen that the bandwidth is about 30 nm. It should be noticed that in MDMs, multiplexing is based on several modes at same wavelength.

## G. FDTD Simulation of BMDM for Example 1

In this subsection, we use FDTD Solutions to simulate the performance of the proposed BMDM with the following parameters: A coupler gap $r=136$ nm, a grating period $\Lambda=312$ nm, a grating teeth depth $t=0.7r$, and a coupling length $L=34\Lambda_{\text{min}}$. A Palik Silicon material is used in our simulation in order to have the results as close to experimental ones as possible [28]. The resulting crosstalks and insertion losses versus wavelength are shown in Figs. 5(a), 5(b), and 5(c), when exciting the demultiplexer by $\text{TE}_0$, $\text{TE}_1$, and $\text{TE}_2$, respectively. It is clear from the figure that the three modes are separated at the three ports with suitable values of crosstalks among different modes. For example, at a wavelength of 1550 nm, the crosstalk is below $-19.6$ dB, $-19.3$ dB, and $-24.2$ dB, when exciting the BMDM by $\text{TE}_0$, $\text{TE}_1$, and $\text{TE}_2$, respectively. The insertion loss is about $-0.2$ dB for the $\text{TE}_0$ mode, while it is too high for both $\text{TE}_1$ and $\text{TE}_2$. Specifically, at 1550 nm, the insertion loss is about $-3$ dB and $-6.6$ dB for the cases of $\text{TE}_2$ and $\text{TE}_1$ modes, respectively. The reason is

![](./images/811265100475269121_5.jpg)

Fig. 5: FDTD simulation of crosstalk and insertion loss versus wavelength of proposed BMDM with a coupler gap $r = 136$ nm, a grating period $\Lambda = 312$ nm, a grating teeth depth $t = 0.7r$, and a coupling length $L = 34\Lambda_{\text{min}}$, when excited by: (a) $\text{TE}_0$, (b) $\text{TE}_1$, and (c) $\text{TE}_2$ modes. Insets: (b) Crosstalk to mode $\text{TE}_1$, port 2. (c) Return loss to mode $\text{TE}_1$, port 1.

![](./images/811265100475269121_6.jpg)

Fig. 6: FDTD simulation of crosstalk and insertion loss versus wavelength of proposed BMDM with a coupler gap $r = 140$ nm, a grating period $\Lambda = 285$ nm, a grating teeth depth $t = r$, and a coupling length $L = 55\Lambda_{\text{min}}$, when excited by: (a) $\text{TE}_0$, (b) $\text{TM}_1$, and (c) $\text{TE}_2$ modes. Here, the widths of waveguides are $w = 650$ nm and $d = 287$ nm.

that the selected value of $\ell_1 = 0$ would lead to a grating period that causes other mode coupling. That is, some of the power of $\text{TE}_2$ mode is reflected back to source (at port one) and excites a $\text{TE}_1$ mode. This return loss is shown in the inset of Fig. 5(c), which is about $-7.8$ dB at 1550 nm. On the other hand, the power of $\text{TE}_1$ is divided between the fundamental mode at port 3 and $\text{TE}_1$ mode at port 1; this is shown in the inset of Fig. 5(b). In fact, the high insertion losses of both $\text{TE}_1$ and $\text{TE}_2$ modes are due to the contra-directional coupling between them in the input waveguide. As the effective indices of $\text{TE}_1$ and $\text{TE}_0^{\text{single}}$ modes are approximately the same, these insertion losses cannot be avoided. However, if there exist other suitable choices of $\ell_1 \neq 0$ and $\ell_2$ that satisfy (22), these losses could be reduced. Another solution is to use $\text{TM}_1$ instead of $\text{TE}_1$ as illustrated in Example 2 below.

### H. Example 2: Slab Waveguide with Two TE Modes and One TM Mode

In this example, we assume that the multimode slab waveguide has a width of $w = 650$ nm and is excited by two TE modes and one TM mode, specifically, $\text{TE}_0$, $\text{TM}_1$, and $\text{TE}_2$. The fundamental mode $\text{TE}_0$ is kept through the waveguide, while the other two modes are coupled to a single-mode waveguide. The $\text{TM}_1$ mode is coupled into the fundamental TM mode in the codirection of the single-mode waveguide, while the $\text{TE}_2$ mode is coupled into the fundamental TE mode in the contra-direction of the single-mode waveguide. In this way, we reduce much the crosstalks between TE and TM modes. The analysis in this example is pretty much similar to that of previous example and is omitted here. We use FDTD Solutions to simulate the performance of this device with same Palik Silicon material as that used in example 1. Accordingly the width of the single-mode waveguide, the grating period, and the coupling length are determined to be $d = 287$ nm, $t = r = 140$ nm, $\Lambda = 285$ nm, and $L = 55\Lambda_{\text{min}}$, respectively. The resulting crosstalks and insertion losses versus wavelength are shown in Figs. 6(a), 6(b), and 6(c), when exciting the demultiplexer by $\text{TE}_0$, $\text{TM}_1$, and $\text{TE}_2$, respectively. It is clear from the figure that that return loss (when exciting the device with $\text{TE}_2$) is reduced. In addition, the crosstalks between TE and TM modes is too small to appear in the figures. The device has a good performance with suitable values of crosstalks and insertion losses. For example, at a wavelength of 1550 nm, the crosstalk is below $-35.7$ dB and $-23.5$ dB, when exciting the

$BMDM$ by $TE_0$ and $TE_2$, respectively. The insertion loss is about $-0.57$ dB for the $TE_0$ mode, while it is about $-2.85$ dB and $-3.8$ dB for the $TM_1$ and $TE_2$ modes, respectively. Notice that for the case of $TE_2$, the insertion loss starts from about $-1.5$ dB at a wavelength of 1525 nm. The loss in the $TM_1$ mode is due to some back reflection in the main waveguide. One can estimate the bandwidth limitation from the figure, which is about 20 nm in this example. Anti-reflection design can be used in the waveguides in order to eliminate the conventional Bragg reflection. This is accomplished by placing two different gratings on each side of the waveguide. If the gratings are phase shifted by $180^\circ$, complete cancellation of Bragg back-reflections is achieved [29].

It should be remarked that although the insertion losses of the second-example device are somewhat high, they are acceptable in view of its very compact size of about $L = 55\Lambda_{\text{min}} = 17\,\mu\text{m}$, which is almost an order of magnitude smaller than that of traditional demultiplexers [3], [13]. The design of this example seems to be more practical than that of three TE modes, given in Example 1.

### VI. CONCLUSIONS

A bi-directional coupler supported with Bragg grating has been proposed as a mode-division multiplexer/demultiplexer (BMDM). The device length is very compact, about $17\,\mu\text{m}$, and can demultiplex 3 modes with only two waveguides and a Bragg grating. The input waveguide is multimode, while the output waveguide is single-mode. Both first- and second order modes of the input waveguide are coupled to the output waveguide, propagating at opposite directions. The fundamental mode is kept in the main waveguide. A theoretical analysis of the proposed demultiplexer has been developed based on the perturbative mode-coupled theory. Insertion losses of both first- and second order modes have been derived and wavelength dependence of the device has been addressed by considering mismatching conditions and a Lorentzian model of the Silicon material. Mathematical expressions of the insertion losses have been obtained for simple slab waveguides. Numerical results of the proposed BMDM have been demonstrated for the slab waveguides under different design parameters. In addition, FDTD simulation of proposed BMDM has been performed to prove the validity of the proposed concept. Return loss due to reflection to the source has been taken into consideration in the simulation. Our results reveal that by proper selection of the design parameters, suitable values of both insertion losses and crosstalks are achievable by the proposed demultiplexer. Specifically, at a wavelength of 1550 nm, crosstalks lower than $-23.5$ dB are achievable.

### REFERENCES

[1] D. J. Richardson, J. M. Fini, and L. E. Nelson, "Space-division multiplexing in optical fibres," *Nat Photon*, vol. 7, pp. 354–362, May 2013.

[2] S. Berdagué and P. Facq, "Mode division multiplexing in optical fibers," *Appl. Opt.*, vol. 21, no. 11, pp. 1950–1955, Jun. 1982.

[3] J. Wang, P. Chen, S. Chen, Y. Shi, and D. Dai, "Improved 8-channel silicon mode demultiplexer with grating polarizers," *Opt. Express*, vol. 22, no. 11, pp. 12799–12807, Jun. 2014.

[4] A. Grieco, G. Porter, and Y. Fainman, "Integrated space-division multiplexer for application to data center networks," *IEEE Journal of Selected Topics in Quantum Electronics*, vol. 22, no. 6, pp. 1–6, Nov. 2016.

[5] T. Uematsu, Y. Ishizaka, Y. Kawaguchi, K. Saitoh, and M. Koshiba, "Design of a compact two-mode multi/demultiplexer consisting of multi-mode interference waveguides and a wavelength-insensitive phase shifter for mode-division multiplexing transmission," *J. Lightwave Technol.*, vol. 30, no. 15, pp. 2421–2426, Aug. 2012.

[6] Y. Ding, J. Xu, F. D. Ros, B. Huang, H. Ou, and C. Peucheret, "On-chip two-mode division multiplexing using tapered directional coupler-based mode multiplexer and demultiplexer," *Opt. Express*, vol. 21, no. 8, pp. 10376–10382, Apr. 2013.

[7] D. Dai, J. Wang, and Y. Shi, "Silicon mode (de)multiplexer enabling high capacity photonic networks-on-chip with a single-wavelength-carrier light," *Opt. Lett.*, vol. 38, no. 9, pp. 1422–1424, May 2013.

[8] H. Qiu, H. Yu, T. Hu, G. Jiang, H. Shao, P. Yu, J. Yang, and X. Jiang, "Silicon mode multi/demultiplexer based on multimode grating-assisted couplers," *Opt. Express*, vol. 21, no. 15, pp. 17904–17911, Jul. 2013.

[9] W. Chen, P. Wang, and J. Yang, "Mode multi/demultiplexer based on cascaded asymmetric Y-junctions," *Opt. Express*, vol. 21, no. 21, pp. 25113–25119, Oct. 2013.

[10] J. B. Driscoll, R. R. Grote, B. Souhan, J. I. Dadap, M. Lu, and R. M. Osgood, "Asymmetric Y junctions in silicon waveguides for on-chip mode-division multiplexing," *Opt. Lett.*, vol. 38, no. 11, pp. 1854–1856, Jun. 2013.

[11] L.-W. Luo, N. Ophir, C. P. Chen, L. H. Gabrielli, C. B. Poitras, K. Bergmen, and M. Lipson, "WDM-compatible mode-division multiplexing on a silicon chip," *Nat Commun*, vol. 5, Jan. 15, 2014.

[12] J. Wang, S. He, and D. Dai, "On-chip silicon 8-channel hybrid (de)multiplexer enabling simultaneous mode- and polarization-division-multiplexing," *Laser & Photon. Rev.*, vol. 8, no. 2, p. L18L22, Feb. 2014.

[13] B. A. Dorin and W. N. Ye, "Two-mode division multiplexing in a silicon-on-insulator ring resonator," *Opt. Express*, vol. 22, no. 4, pp. 4547–4558, Feb. 2014.

[14] D. Dai, "Multimode optical waveguide enabling microbends with low inter-mode crosstalk for mode-multiplexed optical interconnects," *Opt. Express*, vol. 22, no. 22, pp. 27524–27534, Nov. 2014.

[15] N. Hanzawa, K. Saitoh, T. Sakamoto, T. Matsui, K. Tsujikawa, M. Koshiba, and F. Yamamoto, "Mode multi/demultiplexing with parallel waveguide for mode division multiplexed transmission," *Opt. Express*, vol. 22, no. 24, pp. 29321–29330, Dec. 2014.

[16] H. Chen, R. van Uden, C. Okonkwo, and T. Koonen, "Compact spatial multiplexers for mode division multiplexing," *Opt. Express*, vol. 22, no. 26, pp. 31582–31594, Dec. 2014.

[17] M. Yin, Q. Deng, Y. Li, X. Wang, and H. Li, "Compact and broadband mode multiplexer and demultiplexer based on asymmetric plasmonic-dielectric coupling," *Appl. Opt.*, vol. 53, no. 27, pp. 6175–6180, Sept. 2014.

[18] C. Gui, Y. Gao, Z. Zhang, and J. Wang, "On-chip silicon two-mode (de)multiplexer for OFDM/OQAM data transmission based on grating-assisted coupler," *IEEE Photonics Journal*, vol. 7, no. 6, pp. 1–7, Dec. 2015.

[19] C. Williams, B. Banan, G. Cowan, and O. Liboiron-Ladouceur, "Source-synchronous optical link using mode-division multiplexing," in *IEEE 12th International Conference on Group IV Photonics (GFP)*, Aug. 2015, pp. 110–111.

[20] B. Stern, X. Zhu, C. P. Chen, L. D. Tzuang, J. Cardenas, K. Bergman, and M. Lipson, "On-chip mode-division multiplexing switch," *Optica*, vol. 2, no. 6, pp. 530–535, Jun. 2015.

[21] W. Shi, X. Wang, C. Lin, H. Yun, Y. Liu, T. Baehr-Jones, M. Hochberg, N. A. F. Jaeger, and L. Chrostowski, "Silicon photonic grating-assisted, contra-directional couplers," *Opt. Express*, vol. 21, no. 3, pp. 3633–3650, Feb. 2013.

[22] W. Shi, V. Veerasubramanian, D. V. Plant, N. A. F. Jaeger, and L. Chrostowski, "Silicon photonic Bragg-grating couplers for optical communications," in *Proc. of SPIE*, vol. 9010, 2014, pp. 90100F(1–13).

[23] A. Yariv, "Coupled-mode theory for guided-wave optics," *Quantum Electronics, IEEE Journal of*, vol. 9, no. 9, pp. 919–933, Sep. 1973.

[24] T. Erdogan, "Optical add-drop multiplexer based on an asymmetric bragg couple," *Optics Communications*, vol. 157, no. 1–6, pp. 249–264, Dec. 1998.

[25] E. Peral and A. Yariv, "Supermodes of grating-coupled multimode waveguides and application to mode conversion between copropagating modes mediated by backward bragg scattering," *Lightwave Technology, Journal of*, vol. 17, no. 5, pp. 942–947, May 1999.

[26] A. Milton and W. Burns, "Mode coupling in tapered optical waveguide structures and electro-optic switches," *IEEE Trans. Circuits and Systems*, vol. 26, no. 12, pp. 1020–1028, Dec. 1979.

[27] M. J. Deen and P. K. Basu, *Silicon Photonics: Fundamentals and Devices*. New York: John Wiley & Sons, 2012.

[28] E. Palik, *Handbook of Optical Constants of Solids*. CA, USA: Academic Press, 1998.

[29] W. Shi, H. Yun, C. Lin, M. Greenberg, X. Wang, Y. Wang, S. T. Fard, J. Flueckiger, N. A. F. Jaeger, and L. Chrostowski, "Ultra-compact, flat-top demultiplexer using anti-reflection contra-directional couplers for CWDM networks on silicon," *Opt. Express*, vol. 21, no. 6, pp. 6733–6738, Mar. 2013.

Hossam M. H. Shalaby (S'83–M'91–SM'99) was born in Giza, Egypt, in 1961. He received the B.S. and M.S. degrees from Alexandria University, Alexandria, Egypt, in 1983 and 1986, respectively, and the Ph.D. degree from the University of Maryland at College Park in 1991, all in electrical engineering.

In 1991, he joined the Electrical Engineering Department, Alexandria University, and was promoted to Professor in 2001. Currently he is on leave from Alexandria University, where he is the chair of the Department of Electronics and Communications Engineering, School of Electronics, Communications, and Computer Engineering, Egypt-Japan University of Science and Technology (E-JUST), New Borg EL-Arab City, Alexandria, Egypt. From December 2000 to 2004, he was an Adjunct Professor with the Faculty of Engineering and Engineering, Department of Electrical and Information Engineering, Laval University, Quebec, QC, Canada. From September 1996 to February 2001, he was on leave from the Alexandria University. From September 1996 to January 1998, he was with the Electrical and Computer Engineering Department, International Islamic University Malaysia, and from February 1998 to February 2001, he was with the School of Electrical and Electronic Engineering, Nanyang Technological University, Singapore. He has been working as a Consultant at SysDSoft company, Alexandria, Egypt, from 2007-2010. His research interests include optical communications, silicon photonics, optical space-division multiplexing, optical CDMA, optical OFDM technology, and information theory.

Prof. Shalaby has served as a student branch counselor at Alexandria University, IEEE Alexandria and North Delta Subsection, from 2002 to 2006, and served as a chairman of the student activities committee of IEEE Alexandria Subsection from 1995 to 1996. He received an SRC fellowship from 1987 to 1991 from Systems Research Center, Maryland; State Excellence Award in Engineering Sciences in 2007 from Academy of Scientific Research and Technology, Egypt; Shoman Prize for Young Arab Researchers in 2002 from Abdul Hameed Shoman Foundation, Amman, Jordan; State Incentive Award in Engineering Sciences in 1995 and 2001 from Academy of Scientific Research and Technology, Egypt; University Excellence Award in 2009 from Alexandria University; and University Incentive Award in 1996 from Alexandria University. He is a Senior member of the IEEE Photonics Society and The Optical Society (OSA).