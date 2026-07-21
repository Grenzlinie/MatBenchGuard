Analytical and experimental investigation of the frequency ratio and switching law for piezoelectric switching techniques

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2008 Smart Mater. Struct. 17 035003

(http://iopscience.iop.org/0964-1726/17/3/035003)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 155.230.1.64
This content was downloaded on 23/08/2015 at 06:58

Please note that terms and conditions apply.

# Analytical and experimental investigation of the frequency ratio and switching law for piezoelectric switching techniques

M Neubauer and J Wallaschek

Institut für Dynamik und Schwingungen, Leibniz Universität Hannover, Appelstrasse 11, Hannover 30167, Germany

E-mail: neubauer@ids.uni-hannover.de

Received 3 December 2007, in final form 19 February 2008
Published 20 March 2008
Online at stacks.iop.org/SMS/17/035003

## Abstract
Piezoelectric shunt damping with mechanical structures has been an active research topic for several years. Standard passive techniques suffer from a very limited and frequency-dependent damping performance. Recently, semi-active switching techniques—namely SSDI (synchronized switch damping on inductor) and SSDV (synchronized switch damping on voltage source) techniques—have been proposed, which are capable of adapting to variations of the excitation frequency without reduction in performance. Crucial for the damping performance is the tuning of the shunt parameters and the precise switching sequence.

In this paper, an analytical analysis of the switching technique is presented, which includes the influence of all shunt parameters and the switching times. New results concerning the optimal tuning of the inductance and the switching sequence are obtained, and it is shown that the enhanced SSDV technique can be equated with the SSDI technique, albeit with an increased effective piezoelectric force factor. Measurements are conducted to validate the theoretical results.

(Some figures in this article are in colour only in the electronic version)

## 1. Introduction
Piezoceramics are widely used as actuators or sensors in technical systems. They offer very precise positioning and high dynamics, which makes them suitable for vibration damping especially in the high frequency range. An alternative to a fully active vibration control is piezoelectric shunt damping [1]. It features an electrical network that is connected to the electrodes of the piezoceramics, which is embedded into the mechanical structure and couples the mechanical and the electrical systems by the piezoelectric effect. This energy conversion can be optimized by the placement of the piezoceramics within the mechanical structure. It requires detailed knowledge of the vibration modes of the structure.

The task of the electrical network design is to influence the mechanical vibration in such a way that the mechanical vibration amplitudes are minimized and energy dissipation is maximized. The classical passive approach is to use an inductor–resistor network, which forms an electrical resonant circuit with the inherited capacitance of the piezoceramics [2, 3]. Tuning the electrical resonance frequency to the excitation frequency maximizes the voltage amplitudes and the dissipation within the resistance. These networks must be tuned to one specific frequency and they are only effective in a narrow frequency range around the tuned frequency. There exist techniques for damping multi-modes simultaneously, basically by adding additional inductor–resistor–branches [4–7].

Recently, various semi-active switching techniques have been studied in detail. In these techniques, a switching device connects the electrical network to the electrodes of the piezoceramics in a defined sequence. Typically, the switching is triggered by the mechanical vibration itself. This makes the shunt adaptive to the excitation frequency, and no precise tuning of the shunt parameters is necessary. Piezoelectric switching techniques are ideal for the damping of mechanical systems with tonal vibrations (however, they are also capable of damping multiple frequencies; see [8–10]). Because of

the adaption to the excitation frequency, they can be used in systems with time-varying vibration frequencies. In [11], a switching technique was used to suppress squealing on an automotive disc brake.

Two of the most important switching techniques are discussed in this paper: the SSDI [12] and the SSDV [13–15]. There exist other switching techniques like the 'state- switching' [16] or SSDS (synchronized switch damping with short circuit) [17], but their performance is lower than the performance of the techniques discussed here.

The SSDI technique, which is also called 'pulse- switching' or 'synchronized switching' [18], temporarily connects a passive inductance-resistance ($LR$) shunt to the piezoceramics. Timing the duration of connection precisely to half of the electrical periodic time results in an inversion of the applied charge at the electrodes of the piezoceramics. For the remaining approximately half of the excitation period, the switch is opened and the charge is kept constant. This switching sequence is repeated periodically and results in a nearly rectangular shaped voltage signal. Obviously the electrical resonance frequency must be higher than the excitation frequency in order that the system works properly. The SSDV technique is an extension of the SSDI technique, which adds a fixed voltage source with the same polarity as the voltage derivative during the voltage inversion. In fact, the SSDI technique can be treated as a special case of the SSDV technique with a zero amplitude of the voltage source [13].

Most publications that deal with switching techniques use heuristic switching laws. According to these laws, the switch should be connected at the time of maximum deformation of the piezoceramics, and closed exactly for one half of the electrical periodic time [17, 14, 19, 13, 20, 18]. In this case, the force generated by the piezoceramics acts against the deformation velocity, which results in high energy dissipation.

However, it is not proven that this heuristic switching law actually maximizes the damping performance. On the contrary, Niederberger observed in [21], by using a receding horizon optimal control approach, that the switch should be closed one quarter of the electrical periodic time before the maximum deformation of the piezoceramics (and connected for one half of the electrical periodic time). However, the improvement compared to the heuristic law and the influence of the shunt parameters were not quantified.

Similarly as for passive shunt damping, the parameters of the switching shunts must also be optimized. Corr and Clark mention in [18] that three parameters must be optimized for the SSDI technique: the resistance $R$, the inductance $L$ and the switching sequence. Interestingly, to our best knowledge, there is no precise information about the influence of different switching times, and how to tune the inductance. While it is obvious, and stated in many publications, that the resistance $R$ should be as small as possible (typically it represents only the losses of the electronic elements), it is not yet clear how to tune the inductance. In most publications, the dynamics of the switched piezoceramics are calculated only approximately, using various assumptions and simplifications. Typically, the time that is required to invert the charge (during connected shunt) is assumed to be very short compared to the periodic time of excitation. Therefore, this part is often neglected in the calculations. As a consequence, the influence of the inductance value, which is responsible for the required time of inversion, cannot be identified by these works. In [18] it is stated that the electrical resonant frequency should be 10–50 times higher than the excitation frequency, but this range is justified by practical reasons, only. Other authors mention the electrical resonant frequency should be 'very high' [17, 12] or about 1000 times higher [14] compared to the excitation frequency. Niederberger states [21, 22] that the optimal inductance value for the SSDV technique is 20 times smaller than for resonant $LR$ networks, which means that the optimal electrical resonant frequency is $\sqrt{20}$ times higher. Or—described in the periodic times—the electrical periodic time should be 'much smaller' [19, 20] than the excitation frequency.

The determination of the optimal switching sequence and the optimal frequency ratio between mechanical excitation and electrical resonance is addressed in this paper. The dynamics of SSDI switching are studied analytically. During all calculations, the influence of the shunt parameters and the switching sequence is highlighted. The calculations allow us to determine the effect of any possible periodic switching law as well as different inductance values. A precise solution as well as a reasonable approximation, which still includes the effect of the inductance upon the damping performance, is presented. The results obtained are supported by measurements.

## 2. Modeling

For the following calculations, the linear, one-dimensional model of a piezoceramics actuator with attached SSDV network is considered; see figure 1. It is described by the constitutive piezoelectric equations,

$$
\begin{aligned}
\sigma & =K_{\mathrm{E}} S-e E \\
D & =e S+\epsilon_{\mathrm{s}} E,
\end{aligned} \tag{1}
$$

where $\sigma$ is the mechanical stress, $K_{\mathrm{E}}$ the modulus of elasticity, $S$ the strain, $e$ the piezoelectric constant, $E$ the electrical field, $D$ the electrical displacement, and $\epsilon_{\mathrm{s}}$ the electrical permittivity. With the typical transformations, the force $F_{\mathrm{p}}$ generated by the piezoceramics and the current $i_{\mathrm{p}}$ flowing through the electrical network can be written as

$$
\begin{aligned}
F_{\mathrm{p}} & =c x_{\mathrm{p}}-\alpha u_{\mathrm{p}} \\
i_{\mathrm{p}} & =-\alpha \dot{x}_{\mathrm{p}}-C_{\mathrm{p}} \dot{u}_{\mathrm{p}},
\end{aligned} \tag{2}
$$

where $x_{\mathrm{p}}, u_{\mathrm{p}}, c, C_{\mathrm{p}}$ are the mechanical deformation of the piezoceramics, the applied voltage on the electrodes, the mechanical stiffness in the direction of the force, and the capacitance of the piezoceramics. $\alpha$ is the force factor of the piezoceramics, describing the amount of force $F_{\mathrm{p}}$ that is generated by an electrical voltage $u_{\mathrm{p}}$. With an attached SSDV network, the voltage with closed switch is obtained as

$$
u_{\mathrm{p}}=R i_{\mathrm{p}}+L \frac{\mathrm{d} i_{\mathrm{p}}}{\mathrm{d} t} \pm V_{\mathrm{s}}. \tag{3}
$$

![](./images/812112578590277634_1.jpg)

Figure 1. Piezoceramics with SSDV network.

Inserting this term into equation (2) results in

$$
L \underbrace{\left[C_{\mathrm{p}} \ddot{u}_{\mathrm{p}}(t)+\alpha \ddot{x}_{\mathrm{p}}(t)\right]}_{\ddot{Q}^{\mathrm{app}}}+R\left[C_{\mathrm{p}} \dot{u}_{\mathrm{p}}(t)+\alpha \dot{x}_{\mathrm{p}}(t)\right]+u_{\mathrm{p}}(t)= \pm V_{\mathrm{s}}.
\tag{4}
$$

Corr and Clark describe the dynamics in terms of the applied charge $Q^{\mathrm{app}}(t)=C_{\mathrm{p}} u_{\mathrm{p}}(t)+\alpha x_{\mathrm{p}}(t)$. An equivalent form of equation (4) for $V_{\mathrm{s}}=0$ reads

$$
\ddot{Q}^{\mathrm{app}}(t)+\frac{R}{L} \dot{Q}^{\mathrm{app}}(t)+\frac{1}{L C_{\mathrm{p}}} Q^{\mathrm{app}}(t)=\frac{\alpha}{L C_{\mathrm{p}}} x_{\mathrm{p}}(t),
\tag{5}
$$

which can be found in [18]. The response for the open switch is obtained by inserting $R \rightarrow \infty$,

$$
\dot{u}_{\mathrm{p}}(t)=-\frac{\alpha}{C_{\mathrm{p}}} \dot{x}_{\mathrm{p}}(t).
\tag{6}
$$

![](./images/812112578590277634_2.jpg)

Figure 2. Mechanical replacement model for the SSDV technique.

Figure 2 shows the mechanical replacement model of the piezoceramics with attached SSDV network. The piezoceramics is modeled as a lever with length $\alpha / C_{\mathrm{p}}$. This lever couples the mechanical and electrical subsystems and it is a dimensionfull quantity. Similar replacement models of piezoelectric transducers especially for energy harvesting systems can be found in [23, 24]. With the open switch the damping element $C_{\mathrm{p}} R$ is infinitely stiff, and the mass $C_{\mathrm{p}} L$ is held in its actual position. The applied charge $Q^{\text {app }}$ is constant during this time, while the voltage $u_{\mathrm{p}}$ is equal to the deformation of the spring with unity stiffness in the replacement model. It is time dependent, because of the deformation $x_{\mathrm{p}}(t)$. With the closed switch, the mass is free to oscillate at its damped eigenfrequency

$$
\omega_{\mathrm{res}, L R}=v / \sqrt{C_{\mathrm{p}} L}, \quad v=\sqrt{1-\left(\frac{1}{2 Q}\right)^{2}}.
\tag{7}
$$

$Q$ is the quality factor of the electrical network. The voltage source corresponds to a constant force $V_{\mathrm{s}}$ with alternating direction. In this study, the system is excited by a harmonic deformation $x_{\mathrm{p}}(t)$ of the piezoceramics. The reaction force from the piezoceramics upon the mechanical system is not considered. This is hardly met in reality, because the rectangular shaped force signal generated by the piezoceramics is highly nonlinear and may excite higher harmonics within the system [11], so that the assumption of a harmonic excitation is not fulfilled. In order to have the most general results, normalized parameters are introduced,

$$
\begin{gathered}
\eta=\frac{\omega}{\omega_{\mathrm{res}, L R}}=\omega \sqrt{C_{\mathrm{p}} L}, \quad Q=\frac{1}{R} \sqrt{\frac{L}{C_{\mathrm{p}}}}, \\
\tau=\omega_{\mathrm{res}, L R} t=\frac{t}{\sqrt{C_{\mathrm{p}} L}}.
\end{gathered}
\tag{8}
$$

The ratio of excitation frequency $\omega$ and resonant frequency $\omega_{\text {res }, L R}$ of the $L R-C_{\mathrm{p}}$ network is termed $\eta$, and $\tau$ is the associated eigentime. With these normalized parameters, equation (4) can be rewritten as

$$
\begin{aligned}
& u_{\mathrm{p}}^{\prime \prime}+\frac{1}{Q} u_{\mathrm{p}}^{\prime}+u_{\mathrm{p}}=-\alpha\left[L \ddot{x}_{\mathrm{p}}(\tau)+R \dot{x}_{\mathrm{p}}(\tau)\right] \pm V_{\mathrm{s}} \\
& \quad=-V_{\mathrm{pzt}}(\tau) \pm V_{\mathrm{s}}.
\end{aligned}
\tag{9}
$$

The right-hand side of the equation for the closed switch includes the voltage $V_{\mathrm{pzt}}(\tau)$ generated by the piezoelectric effect, which depends on the time derivatives of the deformation $x_{\mathrm{p}}$ of the piezoceramics and the $L R$ shunt as well

as a constant voltage $V_{\mathrm{s}}$ from the voltage source. The SSDI technique represents a special case of the SSDV technique with $V_{\mathrm{s}}=0$.

Two switching times must be determined: the time $\tau_{\text {closed }}$ at which the switch is closed, and the time $\tau_{\text {open }}$ when it is opened. All switching laws have in common that they repeat after every half of the excitation period. Two parameters are required to describe both switching times independently. In this paper the parameter $a$ determines the chronological mean value between $\tau_{\text {closed }}$ and $\tau_{\text {open }}$, and it counts from the time of maximum deformation of the piezoceramics. The parameter $b$ determines the length of time for which the switch is closed. Both values are normalized to the electrical periodic time.

According to these definitions, the heuristic switching law is described by $a=0.25, b=1 /(2 v) \approx 0.5$, because the chronological mean value with the closed switch is one quarter after maximum deformation of the piezoceramics (the switch is closed exactly during maximum deformation and opened one half of the electrical periodic time afterwards).

The switching law proposed by Niederberger [21] is described by $a=0, b=1 /(2 v) \approx 0.5$, because the switch is closed one quarter before maximum deformation and opened one quarter after maximum deformation of the piezoceramics.

## 3. Stationary voltage signal
Because of the periodicity it is sufficient to consider one half periodic time of excitation in order to obtain the stationary voltage signal. Every half of the periodic time consists of a period with the closed switch and with the open switch. These times are calculated separately, because within these times the system is linear.

Starting with an (originally unknown) initial voltage, the voltage signal during the time of the open switch is calculated. In particular, the change in voltage $\Delta u_{\mathrm{p}, \text { open }}$ during this time can be obtained. Similarly, the voltage signal with the closed switch is calculated and also the change in absolute voltage $\Delta u_{\mathrm{p}, \text { closed }}$ during that time. (Due to the oscillatory behavior, the voltage is inverted. Only the change in absolute value is considered.) Finally, the overall change $\Delta u_{\mathrm{p}}$ in voltage during this half periodic time of excitation reads

$$
\Delta u_{\mathrm{p}}=\Delta u_{\mathrm{p}, \text { open }}+\Delta u_{\mathrm{p}, \text { closed }} . \quad(10)
$$

The overall change $\Delta u_{\mathrm{p}}$ depends on the parameters of the electrical network $(L, R)$, of the piezoceramics $\left(\alpha, C_{\mathrm{p}}\right)$, the excitation $\left(\omega, \hat{x}_{\mathrm{p}}\right)$ as well as on the initial voltage $u_{0}$. In this case, we seek for the stationary oscillations, which are characterized by $\Delta u_{\mathrm{p}}\left(u_{0}=u_{\text {stat }}\right)=0$. Solving this equation results in the stationary voltage amplitude $u_{\text {stat }}$, which is a function of the parameters described above.

The difference $\Delta u_{\mathrm{p}, \text { open }}$ with open electrodes is proportional to the change in deformation $x_{\mathrm{p}}$ during this period,

$$
\begin{aligned}
\Delta u_{\mathrm{p}, \text { open }} & =-\frac{\alpha}{C_{\mathrm{p}}}\left[x_{\mathrm{p}}\left(\tau_{\text {closed }}\right)-x_{\mathrm{p}}\left(\tau_{\text {open }}\right)\right] \\
& =\frac{\alpha}{C_{\mathrm{p}}}[\cos [(2 a-b) \pi \eta]+\cos [(2 a+b) \pi \eta]] \hat{x}_{\mathrm{p}} .
\end{aligned}
$$

It depends on the switching times $a, b$ as well as the frequency ratio $\eta$ and the deformation amplitude $\hat{x}_{\mathrm{p}}$. The solution of equation (9) is the superposition of the general solution $u_{\mathrm{p}, \text { hom }}$ and the particular solution $u_{\mathrm{p}, \text { part }}, u_{\mathrm{p}}(t)=u_{\mathrm{p}, \text { hom }}+u_{\mathrm{p}, \text { part }}$. The general solution for a weakly damped network reads

$$
u_{\mathrm{p}, \text { hom }}(\tau)=\mathrm{e}^{-\frac{\tau}{2 v}}[A \cos (v \tau)+B \sin (v \tau)], \quad(12)
$$

where the constants $A, B$ are determined by the initial conditions. The particular solution $u_{\mathrm{p}, \text { part }}$ can be obtained with the Duhamel integral,

$$
u_{\mathrm{p}, \text { part }}(\tau)=\frac{1}{v} \int_{0}^{\tau} \mathrm{e}^{-\frac{\tau-\xi}{2 v}} \sin [v(\tau-\xi)]\left[V_{\mathrm{pzt}}(\xi)+V_{\mathrm{s}}\right] \mathrm{d} \xi .
$$

Because of the time-dependent excitation with $V_{\mathrm{pzt}}(\tau)$, this result is a very lengthy equation. The voltage response and the difference $\Delta u_{\mathrm{p}, \text { closed }}$ can be calculated afterwards. The stationary voltage amplitude is then obtained, which is precise regarding the model assumptions. In particular, this solution contains the influence of the frequency ratio $\eta$ (the inductance $L$ ) and the switching times $a, b$.

Maximizing the stationary voltage amplitude is not the primary aim in the network design. But the voltage amplitude is closely related to the dissipated energy, which is calculated by the integral

$$
E_{\text {diss }}=-\int_{T_{\text {mech }}} F_{\mathrm{p}}(t) \dot{x}_{\mathrm{p}}(t) \mathrm{d} t=-\alpha \int_{T_{\text {mech }}} u_{\mathrm{p}}(t) \dot{x}_{\mathrm{p}}(t) \mathrm{d} t .
$$

For the calculation of the dissipated energy it is sufficient to consider only the piezoforce generated by the voltage $u_{\mathrm{p}}$, because the reaction force caused by the mechanical stiffness $c$ is conservative. Higher voltages $u_{\mathrm{p}}$ result in more dissipated energy. However, the phase shift between the deformation velocity $\dot{x}_{\mathrm{p}}$ and the voltage also has an influence upon the dissipation.

In the following, the timeplots of the voltage $u_{\mathrm{p}}$ according to the above calculation are presented for the SSDV technique $\left(V_{\mathrm{s}}=0\right)$. Figure 3 shows the voltage signals for a variation of the frequency ratio $\eta$ and the quality factor $Q$. These timeplots are shown for the optimal switching times according to Niederberger [21]. The time axis is normalized to the periodic time $T_{\text {mech }}$ of the excitation. For low frequency ratios $\eta \ll 1$ the electrical resonant frequency is very high compared to the excitation frequency. Therefore, the inversion of the voltage during the closed switch occurs nearly instantly, and the voltage has a nearly rectangular shape. For frequency ratios close to 1 the voltage signal has a sinusoidal shape. Obviously, the proposed calculation is capable of demonstrating the influence of the frequency ratio. Beside the change in shape, it can be seen that the voltage amplitude slightly increases for smaller frequency ratios $\eta$.

The variation of the quality factor $Q$ shows that the voltage amplitudes grow nearly linearly with $Q$. A lower quality factor prevents the voltage from being inverted during the times with the closed switch and therefore drastically reduces the voltage amplitudes.

![](./images/812112578590277634_3.jpg)

Figure 3. Stationary voltage signals; variation of $\eta$ and $Q$.

![](./images/812112578590277634_4.jpg)

Figure 4. Stationary voltage signals; variation of switching times $a, b$.

It can be seen that the voltage (and therefore also the piezoforce) always acts against the deformation velocity, and therefore dissipates energy.

Figure 4 shows a variation of the switching times $a, b$. For clarity, the parameters $a$ and $b$ are varied separately. When parameter $a$ is varied, the parameter $b$ is set to $b = 1/(2\upsilon)$; when parameter $b$ is varied, parameter $a$ is set to $a = 0$. From the definition of the parameters, a change of $a$ shifts the time of the closed switch (negative values to the left, positive values to the right), and parameter $b$ changes the duration of connection. From the upper diagrams it is obvious that the voltage amplitudes are maximized for $a = 0$, which corresponds to the switching law proposed by Niederberger [21]. In this case, the voltage changes its sign exactly at the same time as the deformation velocity. In particular, the case $a = 0.25, b = 1/(2\upsilon)$ is worth mentioning: this is the heuristic switching law, which is the standard switching law for most previous publications. It can be seen that the switch is closed exactly at the time of zero velocity (which corresponds to maximum deformation), but it changes its sign one quarter of the electrical periodic time later than the deformation. Clearly, the voltage amplitude is reduced compared to the optimal parameters $a = 0, b = 1/(2\upsilon)$. Additionally, the signals $u_{\mathrm{p}}(t)$ and $\dot{x}_{\mathrm{p}}(t)$ have the same sign for one quarter of the electrical periodic time. For a high electrical resonant frequency, this has negligible influence upon the damping performance, but for a frequency ratio $\eta$ close to 1 the reduction is noticeable.

The lower diagrams clearly show that the switch must be closed exactly for one half of the electrical periodic time $(b = 1/(2\upsilon))$. This is in agreement with both switching laws. Opening the switch too early $(b = 1/(2\upsilon))$ means the voltage inversion cannot be fulfilled, and when opening the switch too late $(b = 1/(2\upsilon))$, the voltage oscillates back after inversion.

![](./images/812112578590277634_5.jpg)

Figure 5. Stationary voltage amplitude $u_{\text{stat}}$ versus switching times $a, b$.

In both cases, the stationary voltage amplitude is drastically reduced compared to the optimal value.

The influence of the times of closing and opening the switch is shown in figure 5. The stationary voltage amplitude $u_{\text{stat}}$ is given versus the normalized switching times $a, b$. It is normalized to the voltage amplitude of the voltage with open electrodes $\hat{u}_{\text{p,sensor}} = \alpha \hat{x}_{\text{p}}/C_{\text{p}}$. It can be seen that the voltage is maximized for the optimal switching law, $a = 0, b = 1/(2\nu)$. The voltage amplitude is very sensitive towards changes in length of connection $b$. Compared to the optimal switching, the heuristic switching law results in a slightly lower voltage amplitude, which is noticeable already in figure 4. However, for typical applications, the heuristic switching law offers nearly optimal damping performance and much easier implementation; therefore it is reasonable to use this switching.

### 3.1. Approximate solution
Although the solution presented above is precise and includes the influence of all parameters, the result is very lengthy. The influence of the parameters is not straightforward. Therefore, it is useful to develop an approximate solution, which shows the influence of the network parameters in a clear way while still having a high precision. The proposed approximation uses the following simplifications.

- The voltage $V_{\text{pzt}}(\tau)$ induced by the piezoceramics is approximated by the mean value $\bar{V}_{\text{pzt}}$ during the time with the closed switch. In this way, the particular solution according to equation (13) simplifies to a step response.
- Only optimal switching times according to the precise solution are considered, i.e. $a = 0, b = 1/(2\nu) \approx 0.5$. Therefore, the switch is closed for a duration $\tau^* = \pi/\nu$.

The change in voltage $\Delta u_{\text{p,open}}$ according to equation (11) with optimal switching times $a = 0, b = 1/(2\nu)$ reads
$$
\Delta u_{\text{p,open}} = 2 \frac{\alpha}{C_{\text{p}}} \cos\left(\frac{\pi \eta}{2}\right) \hat{x}_{\text{p}}, \tag{15}
$$
while the general solution with initial conditions $u_{\text{p}}(\tau = 0) = u_0, \dot{u}_{\text{p}}(\tau = 0) = 0$ is obtained as
$$
u_{\text{p,hom}}(\tau) = \text{e}^{-\frac{\tau}{2Q}} \left[ \cos(\nu \tau) + \frac{1}{2Q \nu} \sin(\nu \tau) \right] u_0. \tag{16}
$$

The particular solution is the step response,
$$
\begin{aligned}
u_{\text{p,part}}(\tau) &= - \left( \bar{V}_{\text{pzt}} + V_{\text{s}} \right) \\
&\quad \times \left[ 1 - \text{e}^{-\frac{\tau}{2Q}} \left[ \cos(\nu \tau) + \frac{1}{2Q \nu} \sin(\nu \tau) \right] \right],
\end{aligned} \tag{17}
$$
with the mean voltage $\bar{V}_{\text{pzt}}$ during the closed switch:
$$
\bar{V}_{\text{pzt}} = \frac{1}{T_{\text{close}} - T_{\text{open}}} \int_{T_{\text{open}}}^{T_{\text{close}}} V_{\text{pzt}}(\tau) \text{d}\tau = 2 \frac{\alpha \nu \eta}{\pi C_{\text{p}}} \sin\left( \frac{\pi \eta}{2\nu} \right) \hat{x}_{\text{p}}. \tag{18}
$$

The final voltage value with the closed switch can be obtained as
$$
\begin{aligned}
u_{\text{p}}(\tau^*) &= u_{\text{p,hom}}(\tau^*) + u_{\text{p,part}}(\tau^*) \\
&= - \text{e}^{-\frac{\pi}{2Q \nu}} u_0 - \left( \text{e}^{-\frac{\pi}{2Q \nu}} + 1 \right) \left( \bar{V}_{\text{pzt}} + V_{\text{s}} \right),
\end{aligned} \tag{19}
$$
and the difference $\Delta u_{\text{p,closed}}$ reads
$$
\begin{aligned}
\Delta u_{\text{p,closed}} &= |u_{\text{p}}(\tau^*)| - |u_0| \\
&= \left( \text{e}^{-\frac{\pi}{2Q \nu}} - 1 \right) u_0 + \left( 1 + \text{e}^{-\frac{\pi}{2Q \nu}} \right) V_{\text{s}} \\
&\quad + \left( 1 + \text{e}^{-\frac{\pi}{2Q \nu}} \right) \bar{V}_{\text{pzt}}.
\end{aligned} \tag{20}
$$

The stationary voltage amplitude $u_{\text{stat}}$ according to equation (10) reads
$$
\begin{aligned}
u_{\text{stat}} &= 2 \frac{\alpha}{C_{\text{p}}} \frac{\cos\left( \frac{\pi \eta}{2} \right) + \left( 1 + \text{e}^{-\frac{\pi}{2Q \nu}} \right) \sin\left( \frac{\pi \eta}{2\nu} \right) \frac{\nu \eta}{\pi}}{1 - \text{e}^{-\frac{\pi}{2Q \nu}}} \hat{x}_{\text{p}} \\
&\quad + \frac{1 + \text{e}^{-\frac{\pi}{2Q \nu}}}{1 - \text{e}^{-\frac{\pi}{2Q \nu}}} V_{\text{s}}.
\end{aligned} \tag{21}
$$

The standard SSDV technique with a constant amplitude $V_{\text{s}}$ may lead to instability for very small mechanical amplitudes $\hat{x}_{\text{p}}$, because the induced voltage due to $V_{\text{s}}$ is very high compared to the voltage induced by the piezoelectric effect. Therefore, the *enhanced* SSDV technique [19] has been developed, which adapts the amplitude of the voltage source proportionally to the deformation $\hat{x}_{\text{p}}$ of the piezoceramics, $V_{\text{s}} = \gamma \hat{x}_{\text{p}}$. In this case, the ratio of the voltage due to the piezoelectric effect and due to the external voltage source $V_{\text{s}}$ stays constant for any vibration amplitude $\hat{x}_{\text{p}}$,
$$
\begin{aligned}
u_{\text{stat}} &= \left( 2 \frac{\alpha}{C_{\text{p}}} \frac{\cos\left( \frac{\pi \eta}{2} \right) + \left( 1 + \text{e}^{-\frac{\pi}{2Q \nu}} \right) \sin\left( \frac{\pi \eta}{2\nu} \right) \frac{\nu \eta}{\pi}}{1 - \text{e}^{-\frac{\pi}{2Q \nu}}} \right. \\
&\quad \left. + \gamma \frac{1 + \text{e}^{-\frac{\pi}{2Q \nu}}}{1 - \text{e}^{-\frac{\pi}{2Q \nu}}} \right) \hat{x}_{\text{p}}.
\end{aligned} \tag{22}
$$

The approximate solutions according to equations (21) and (22) are valid only for optimal switching times, but they still include the effects of the frequency ratio $\eta$ and the quality factor $Q$ of the network. The voltage amplitude is composed of two terms: the first term is the voltage of the SSDI technique without voltage source ($V_{\text{s}} = 0$ or $\gamma = 0$), and the second term is the increase in voltage due to the voltage source in the SSDV technique.

#### 3.1.1. Comparison with standard approximation.
In most other publications, the calculation of the switching technique is further simplified with the following assumptions:

![](./images/812112578590277634_6.jpg)

Figure 6. Stationary voltage amplitude $u_{\text{stat}}$ versus quality factor $Q$ and frequency ratio $\eta$. Proposed solution according to equation (21) in solid lines, simplified approximation (equation (23)) in dashed lines.

- very high electrical frequency compared to the mechanical excitation frequency is considered: $\eta=0$;
- the damping of the network is assumed to be very small: $\nu\approx1$.

Inserting these terms into equation (21) simplifies the result to

$$
\begin{aligned}
u_{\text{stat}} &= 2 \frac{\alpha}{C_{\mathrm{p}}} \frac{1}{1-\mathrm{e}^{-\frac{\pi}{2 Q}}} \hat{x}_{\mathrm{p}}+\frac{1+\mathrm{e}^{-\frac{\pi}{2 Q}}}{1-\mathrm{e}^{-\frac{\pi}{2 Q}}} V_{\mathrm{s}} \\
&=\frac{2}{C_{\mathrm{p}}} \frac{1}{1-\mathrm{e}^{-\frac{\pi}{2 Q}}} \hat{x}_{\mathrm{p}}\left[\underbrace{\alpha+\frac{C_{\mathrm{p}}}{2} \gamma\left(1+\mathrm{e}^{-\frac{\pi}{2 Q}}\right)}_{\alpha^{*}}\right].
\end{aligned} \quad (23)
$$

A very similar result can be found in [17] for the SSDI technique ($V_{\mathrm{s}}=0$) and in [14] for the SSDV technique. Naturally, this equation does not include the influence of the frequency ratio any more. That means it cannot be used to determine the optimal value for inductance. Additionally, the error of this approximation increases with lower quality factor $Q$ of the network. However, the increase in voltage due to the source $V_{\mathrm{s}}$ is the same in both approximations.

Based on equation (23) the enhanced SSDV technique can be treated as a standard SSDI technique, but with enhanced piezoelectric force factor $\alpha^{*}$:

$$\alpha^{*} \approx \alpha+C_{\mathrm{p}} \gamma. \tag{24}$$

This means that the enhanced SSDV technique on a piezoceramics with a force factor $\alpha$ results in the same voltage amplitude as an SSDI technique on a piezoceramics with a (higher) force factor $\alpha^{*}$. The SSDV technique is therefore an active solution to effectively increase the force factor of a piezoceramics. From equation (24) it can be seen that the increase in voltage and energy dissipation depends on the ratio $\gamma$ between voltage source amplitude and deformation amplitude. By definition, $\alpha=\alpha^{*}$ for $\gamma=0$.

A comparison of the proposed solution according to equation (21) and the simplified solution is given in figure 6. Again the stationary voltage amplitude is normalized to the voltage amplitude with open electrodes. Both solutions agree very well for a frequency ratio close to zero, which means a high electrical resonant frequency. The proposed solution shows a slight decrease in the stationary voltage amplitude for higher frequency ratios. The border case is $\eta=1$, for which the electrical resonant frequency equals the excitation frequency, and the $LR$ shunt is always connected to the piezoceramics.

From these results it can be concluded that the electrical resonant frequency does not need to exceed the mechanical excitation frequency multiple times, like it is given in previous publications. An electrical frequency that is two times higher than the excitation frequency ($\eta=0.5$) reduces the voltage amplitudes by less than $5\%$ compared to $\eta=0$. It is desirable to have a smaller electrical resonant frequency because it does not excite high harmonics within the mechanical systems.

![](./images/812112578590277634_7.jpg)

Figure 7. Photograph of the mechanical test rig.

### 4. Measurements

Measurements are performed on a clamped beam; see figure 7. The beam has a first natural frequency of $f_{1}\approx100$ Hz. Three macro fiber composite (MFC) actuators are attached on it: two identical piezoceramics M-8528-P2 and one piezoceramics M-2814-P1 from company *Smart material*. The small M-2814-P1 is used as a sensor and triggers the switching times. One M-8528-P2 is shunted to the SSDI network, and the second M-8528-P2 (placed on the opposite side of the beam) is used as an actuator in order to generate stationary oscillations of the beam.

For the validation of the obtained results, a switching board is built up, which allows us to connect and disconnect the $LR$ shunt to the piezoceramics at precisely defined times;

![](./images/812112578590277634_8.jpg)
![](./images/812112578590277634_9.jpg)

Figure 8. Measured stationary voltage amplitude $u_{\text{stat}}$ versus switching times $a$, $b$ and network parameters $Q$, $\eta$.

see [25]. It is an electronic bilateral switch triggered by a digital circuitry. It requires a control signal to be supplied, providing the information about the vibration of the structure the piezoceramics is embedded in.

Measurements with different frequency ratios $\eta$, quality factors $Q$ and switching sequences $a, b$ have been done. Generally, the shapes of the time plots agree well with the analytical results in figures 3 and 4. The measured stationary voltage amplitudes are shown in figure 8 versus the switching times $a, b$ and network parameters $Q, \eta$. The voltage amplitudes in the left figure are normalized to the voltage for $a = 0, b = 1/(2v)$; in the right figures they are normalized to the sensor voltage. The measured influence of the switching times is very similar to the calculated result in figure 5. The maximum voltage occurs for the optimal switching times $a = 0, b = 1/(2v)$, being slightly higher than the voltages that occur for the heuristic switching law.

The second diagram proves that the quality factor $Q$ of the network mainly determines the stationary voltage amplitudes $u_{\text{stat}}$. The influence of the frequency ratio is qualitatively the same as the calculated one according to figure 6: a higher electrical resonant frequency (smaller $\eta$) leads to larger voltage amplitudes. For the measurements, the quality factor of the network is calculated according to equation (8), while the resistance $R$ is the sum of the external resistance and the internal resistance of the inductance. The voltage amplitudes of the measurements are smaller than predicted. This may be because of losses in the switching board, which are not considered in the quality factor.

## Conclusions
This paper discusses piezoelectric switching techniques for vibration damping. The SSDI and SSDV techniques are discussed analytically including all important system parameters and the switching sequence. A precise solution is presented as well as a reasonable approximation. The results obtained show the influence of the inductance value and the switching sequences upon the damping performance, which has not been obtained before. From these calculations, the switching law proposed by Niederberger proves to be optimal for maximizing the voltage amplitudes, while the heuristic switching law performs slightly more weakly. The difference in performance depends on the ratio of electrical resonant frequency and mechanical excitation frequency. The frequency ratio has little influence upon the damping performance. Therefore, the frequency ratios suggested in previous literature (ranging to ratios of $1/1000$) seem too extreme. It is instead recommended to use a rather moderate frequency ratio of $1/2$ or lower, if the required inductance value is not too high. In this way, the excitation of higher harmonics within the mechanical system is strongly reduced.

The SSDI and enhanced SSDV techniques are studied in a uniform approach. The results show that the enhanced SSDV technique performs similarly to the SSDI technique but with an actively increased force factor of the piezoceramics. The energy dissipation grows nearly linearly with the external voltage amplitude.

Measurements on a bending beam with attached piezoceramics validate the obtained results.

## References
[1] Moheimani S O R 2003 A survey of recent innovations in vibration damping and control using shunted piezoelectric transducer *IEEE Trans. Control Syst. Technol.* **11** 482–94

[2] Hagood N W and von Flotow A 1991 Damping of structural vibrations with piezoelectric materials and passive electrical networks *J. Sound Vib.* **146** 243–68

[3] Tang J and Wang K W 2001 Active–passive hybrid piezoelectric networks for vibration control: comparisons and improvement *Smart Mater. Struct.* **10** 794–806

[4] Fleming A J, Behrens S and Moheimani S O R 2003 Reducing the inductance requirements of piezoelectric shunt damping systems *Smart Mater. Struct.* **12** 57–64

[5] Hollkamp J J 1994 Multimodal passive vibration suppression with piezoelectric materials and resonant shunts *J. Intell. Mater. Syst. Struct.* **5** 49–57

[6] Wu S-Y 1998 Method for multiple-mode shunt damping of structural vibration using a single pzt transducer *Smart Structures and Materials 1998: Passive Damping and Isolation, Presented at the Society of Photo-Optical Instrumentation Engineers (SPIE) Conf.; Proc. SPIE* **3327** 159–68

[7] Behrens S and Moheimani S O R 2002 Current flowing multiple-mode piezoelectric shunt dampener *Smart Structures and Materials 2002: Damping and Isolation, Presented at the Society of Photo-Optical Instrumentation Engineers (SPIE) Conf.; Proc. SPIE* **4697** 217–226

[8] Corr L R and Clark W W 2003 A novel semi-active multi-modal vibration control law for a piezoceramic actuator *J. Vib. Acoust.* **125** 214–22

[9] Clark W W and Schoenly J 2005 Evaluation of performance indices for tuning the switch timing of pulse-switched piezoelectric shunts for vibration control *Smart Structures*

and Materials 2005: Damping and Isolation. Presented at the Society of Photo-Optical Instrumentation Engineers (SPIE) Conf.; Proc. SPIE **5760** 402–12

[10] Niederberger D, Fleming A, Moheimani S O R and Morari M 2004 Adaptive multi-mode resonant piezoelectric shunt damping *Smart Mater. Struct.* **13** 1025–35

[11] Neubauer M, Niederberger D and Morari M 2006 A novel approach for brake squeal control using shunted piezoceramics *Proc. 24th SAE Brake Colloquium*

[12] Corr L R and Clark W W 2001 Energy dissipation analysis of piezoceramic semi-active vibration control *J. Intell. Mater. Syst. Struct.* **12** 729–36

[13] Faiz A, Guyomar D, Petit L and Buttay C 2005 Semi-passive piezoelectric noise control in transmission by synchronized switching damping on voltage source *J. Physique IV* **128** 171–6

[14] Lefeuvre E, Badel A, Petit L, Richard C and Guyomar D 2006 Semi-passive piezoelectric structural damping by synchronized switching on voltage sources *J. Intell. Mater. Syst. Struct.* **17** 653–60

[15] Richard C, Guyomar D, Audigier D and Ching G 1999 Semi-passive damping using continuous switching of a piezoelectric device *Smart Structures and Materials 1999: Passive Damping and Isolation*, Presented at the Society of Photo-Optical Instrumentation Engineers (SPIE) Conf.; Proc. SPIE **3672** 104–11

[16] Clark W W 2000 Vibration control with state-switched piezoelectric materials *J. Intell. Mater. Syst. Struct.* **11** 263–71

[17] Richard C, Guyomar D, Audigier D and Bassaler H 2000 Enhanced semi-passive damping using continuous switching of a piezoelectric device on an inductor *Smart Structures and Materials 2000: Damping and Isolation*, Presented at the Society of Photo-Optical Instrumentation Engineers (SPIE) Conf.; Proc. SPIE **3989** 288–99

[18] Corr L R and Clark W W 2002 Comparison of low-frequency piezoelectric switching shunt techniques for structural damping *Smart Mater. Struct.* **11** 370–6

[19] Badel A, Sebald G, Guyomar D, Lallart M, Lefeuvre E, Richard C and Qiu J 2006 Piezoelectric vibration control by synchronized switching on adaptive voltage sources: towards wideband semi-active damping *J. Acoust. Soc. Am.* **119** 2815–25

[20] Anderson T, Manubarthi U, Corti G and Anderson M 2007 Response prediction of switched inductor/piezoelectric vibration suppression *Smart Mater. Struct.* **16** 135–9

[21] Niederberger D, Morari M and Pietrzko S 2004 A new control approach for switching shunt damping *Smart Structures and Materials 2004: Damping and Isolation*. Presented at the Society of Photo-Optical Instrumentation Engineers (SPIE) Conf.; Proc. SPIE **5386** 426–37

[22] Niederberger D and Morari M 2006 An autonomous shunt circuit for vibration damping *Smart Mater. Struct.* **15** 359–64

[23] Twiefel J, Richter B, Sattel T and Wallaschek J 2007 Power output estimation and experimental validation for piezoelectric energy harvesting systems *J. Electroceram.* doi:10.1007/s10832-007-9168-5

[24] Twiefel J, Richter B, Hemsel T and Wallaschek J 2006 Model-based design of piezoelectric energy harvesting systems *Proc. SPIE* **6169** 616909

[25] Neubauer M and Oleskiewicz R 2007 Optimal piezoelectric switching technique for vibration damping *Active and Passive Smart Structures and Integrated Systems 2007*. Presented at the Society of Photo-Optical Instrumentation Engineers (SPIE) Conf.; Proc. SPIE **6525** 652512