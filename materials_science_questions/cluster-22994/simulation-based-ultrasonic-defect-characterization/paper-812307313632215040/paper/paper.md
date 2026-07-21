## LITERATURE CITED

1.  Industry Standard RD 50-213-80: Rules for Measuring Gas and Liquid Flows with Standard Constricting Devices.
2.  ISO 5167: Measurement of Fluid by Means of Orifice Plates, Nozzles, and Venturi Tubes Inserted in Circular Cross Section Conduits Running Full, May, 1979 (E).
3.  P. P. Kremlevskii, Flow Meters and Quantity Gauges [in Russian], Mashinostroenie, Leningrad (1989).
4.  Industry Standard RD 50-411-83: Methodological Instructions for Flow Rates of Liquids and Gases: Methodology of Measurement with Special Constricting Devices.
5.  B. M. Levin and A. N. Lopatin, Gidrotekh. Stroit., No. 6, 24 (1982).
6.  B. M. Levin and A. N. Lopatin, in: Proc. Twentieth IAHR Congress, Moscow (1983).
7.  B. M. Levin, et al., Gidrotekh. Stroit., No. 6, 12 (1984).
8.  A. N. Lopatin, Tr. MIIT, Issue 793, 71 (1988).
9.  Official Manual MI 1948-88: Recommendation. Government System for Unified Measurement. Water Flows. Methodology for Measurement with Segmental Orifice Plates.
10. N. E. Zhukovskii, "A modification of the Kirchhoff method for determination of a liquid flow in two measurements at constant velocity on an unknown stream line," in: Collected Works [in Russian], Vol. 3, ONTI, Moscow (1936).
11. A. D. Al'tshul', Hydraulic Resistances [in Russian], Nedra, Moscow (1970).
12. ASME Fluid Meter Reports (1950).
13. V. Z. Volkov, B. M. Levin, and A. N. Lopatin, Vodosnabzh. Sanit. Tekh., No. 8, 18 (1985).

---

## REVERBERATION IN ULTRASOUND FLOW METERS

V. I. Filatov

UDC 681.121:534-8

Reverberation of ultrasound signals can modify the metrologic characteristics of flow meters. Frequency-pulse and phase flow meters are especially strongly affected by ultrasound signals multiply reflected from the receiver/emitter, especially doubly reflected signals. The influence of other types of reverberation, such as transmission of ultrasound signals through the converter pipe, signal reverberation in sound ducts, etc., can be eliminated or considerably attenuated by design and circuit concepts. In pulse-time ultrasound flow meters, the influence of multiply reflected ultrasound signals is eliminated by increasing the emission period.

We analyze the influence of signals multiply reflected from the surface of the piezo-elements or sound duct upon the characteristics of frequency-pulse ultrasound flow meters.

Figure 1 illustrates schematically a converter of an angle flow meter without refraction of ultrasound signals. The following notations are used: $P_d$, $P_u$ piezoelements emitting ultrasound signals, downstream and upstream, respectively; D is the diameter of nominal opening of flow meter converter; $\ell$ is the "pocket" depth; $\alpha$ is the ultrasound signal emission angle; and v is the flow velocity.

Time intervals $\Delta t_{2nd}$ and $\Delta t_{2nu}$ between 2n multiply reflected and basic signals emitted downstream and upstream, respectively, can be formulated as

$$\Delta t_{2 n d}=2 n t_{d}-n\left(t_{u}-\tau_{u}\right)-n\left(t_{d}-\tau_{d}\right)=n\left(t_{d}-t_{u}\right)+n\left(\tau_{d}+\tau_{u}\right), \tag{1}$$

$$\Delta t_{2 n u}=2 n t_{u}-n\left(t_{d}-\tau_{d}\right)-n\left(t_{u}-\tau_{u}\right)=-n\left(t_{d}-t_{u}\right)+n\left(\tau_{d}+\tau_{u}\right), \tag{2}$$

where $t_d$ and $t_u$ are the periods of signal self-circulation downstream and upstream; $\tau_d$ and $\tau_u$ are delays in the electronic circuit of the self-circulating signals downstream and upstream, respectively; $n = 0, 1, 2, 3, ....$

---

Translated from Izmeritel'naya Tekhnika, No. 3, pp. 39-40, March, 1993.

0543-1972/93/3603-0301$12.50

© 1993 Plenum Publishing Corporation

![](./images/812307313632215040_1.jpg)

Fig. 1

Self-circulating periods of signals downstream $(t_{d})$ and upstream $(t_{u})$ consist of the time of travel of an ultrasound signal in the converter (see Fig. 1) and delay times of the signals $\tau_{d}$ and $\tau_{u}$ in the electronic circuit, i.e.,

$$
t_{d}=\frac{D}{\sin \alpha(c+v \cos \alpha)}+\frac{l}{c}+\tau_{d} ; \tag{3}
$$

$$
t_{u}=\frac{D}{\sin \alpha(c-v \cos \alpha)}+\frac{l}{c}+\tau_{u}, \tag{4}
$$

whence

$$
t_{d}-t_{u}=-\frac{2 D v c \operatorname{tg} \alpha}{c^{2}-v^{2} \cos ^{2} \alpha}+\left(\tau_{d}-\tau_{u}\right),
$$

where c is the ultrasound velocity in the flow.

Substituting the last expression into (1) and (2), we obtain:

$$
\Delta t_{2 n d}=-\frac{2 n D v c \operatorname{tg} \alpha}{c^{2}-v^{2} \cos ^{2} \alpha}+2 n \tau_{d},
$$

$$
\Delta t_{2 n u}=\frac{2 n D v c \operatorname{tg} \alpha}{c^{2}-v^{2} \cos ^{2} \alpha}+2 n \tau_{u}.
$$

Neglecting in the denominators the terms $v^{2} \cos ^{2} \alpha$, because $c^{2} \gg v^{2} \cos ^{2} \alpha$, and considering that when the zero of the flow meter is set $\tau_{d}=\tau_{u}=\tau$, we rewrite the last two expressions:

$$
\Delta t_{2 n d}=-\frac{2 n D v c \operatorname{tg} \alpha}{c^{2}}+2 n \tau, \tag{5}
$$

$$
\Delta t_{2 n u}=\frac{2 n D v c \operatorname{tg} \alpha}{c^{2}}+2 n \tau. \tag{6}
$$

We see from (5) and (6) that multiply reflected signals lag behind the main signal periodically with period $2 \tau$. When the flow velocity is increased, multiply reflected signals approach the basic signal directed downstream and move away from the basic signal directed upstream.

Assuming that the form of multiply reflected signals coincides with that of the basic signal, we can express for a signal length $\tau_{c}$ on the basis of (5) the condition ensuring the absence of superposition of doubly reflected signals, and therefore of all multiply reflected signals, upon the basic signal:

$$
\tau_{c}<2 \tau-\frac{2 D v_{\max } \operatorname{ctg} \alpha}{c^{2}}, \tag{7}
$$

where $v_{max}$ is the maximum flow of velocity.

We see that in frequency-pulse ultrasound flow meters inequality (7) can be ensured by reducing $\tau_{c}$: emitting short ultrasound signals at a possibly high frequency or by increas- ing the delay of the signals $(\tau)$ in the electronic circuit. A significant increase of delay

τ deteriorates an important feature of a frequency-pulse ultrasound velocity. We examine this aspect in some detail.

The output signal of a frequency-pulse ultrasound flow meter is expressed as
$$\Delta f=f_{u}-f_{d}=\frac{1}{t_{u}}-\frac{1}{t_{d}}. \tag{8}$$

Substituting into this expression $t_{u}$ and $t_{d}$ from (3) and (4) solving the equation and omitting small terms, we obtain:
$$\Delta f=\frac{2 D v c \operatorname{tg} \alpha}{(D / \sin \alpha+l)^{2}+2 c(D / \sin \alpha+l)+\tau^{2} c^{2}}.$$

We see from this expression that the dependence of the output signal upon ultrasound velocity c is caused by last two terms in the denominator, which, when $\tau$ is large, have substantially high values.

When inequality (7) is not satisfied, or when a long harmonic signal is emitted, multiply reflected signals become superimposed upon the basic signals, which results in a modulation of the graduation characteristic of the frequency-pulse ultrasound flow meter by multiply reflected signals, introducing a systematic error. Such a modulated graduation characteristic has been observed in studies with UZRF2-150 flow meter [1].

When harmonic oscillations are combined $F_{O}(t)=A_{O} \sin (\omega t+\varphi_{O})$ we obtain the resulting signal
$$\sum_{0=0}^{n} A_{0} \sin \left(\omega t+\varphi_{0}\right)=A \sin (\omega t+\varphi),$$
where $A_{O}$ is the oscillation amplitude and $\varphi_{O}$ is the oscillation phase.

When basic signal $A_{c} \sin (\omega t+\varphi_{c})$ is combined with the doubly reflected signal $A_{1} \sin (\omega t+$ $\varphi_{1}$ ), the signal amplitude and the signal phase can be written as
$$A=\sqrt{A_{c}^{2}+A_{1}^{2}+2 A_{c} A_{1} \cos \left(\varphi_{c}-\varphi_{1}\right)}, \tag{9}$$

$$\operatorname{tg} \varphi=\frac{A_{c} \sin \varphi_{c}+A_{1} \sin \varphi_{1}}{A_{c} \cos \varphi_{c}+A_{1} \cos \varphi_{1}}. \tag{10}$$

Solving Eq. (10), we see that only when $\varphi_{c}=\varphi_{1}, \varphi=\varphi_{c}$, while in all the other cases $\varphi \neq \varphi_{c}$. This is responsible for the large systematic error $\delta_{\varphi}=(\varphi-\varphi_{c}) / \varphi_{c}$ of phase ultrasound flow meters, which is an unavoidable shortcoming of these devices.

In frequency-pulse ultrasound flow meters the composite signal
$$A_{c} \sin \left(\omega t+\varphi_{c}\right)+A_{1} \sin \left(\omega t+\varphi_{1}\right)=A \sin \left[\omega\left(t+\frac{\varphi-\varphi_{c}}{\omega}\right)+\varphi_{c}\right]$$
includes, because of the phase change, a time shift relative to the basic signal $t_{d}'=$ $(\varphi-\varphi_{c}) /(\omega)=(\varphi-\varphi_{c}) /(2 \pi f)$, where f is the emitted signal frequency. The output signal then appears as
$$\Delta f^{\prime}=\frac{1}{t_{u}}-\frac{1}{t_{d}+t_{d}^{\prime}}.$$

The value of $t_{d}'$ determines the systematic error $\delta'$ of measurement because of the phase shift, which is equal to $\delta'=(\Delta f-\Delta f') /(\Delta f)$.

The change of the signal amplitude because of combination with doubly reflected signal is also a source of error of frequency-pulse ultrasound flow meters. In a flow meter, the signal generator has a triggering threshold $u_{c}$, which is a component of signal amplitude $A_{c}$, i.e., $m_{c}=u_{c} / A_{c}$. When the basic signal is combined with a doubly reflected signal, the amplitude is changed, and the trigger ranger threshold now corresponds to a different portion of the composite signal $m=u_{c} / A=m_{c} A_{c} / A$.

Because of the difference in the slope of the basic signal and the composite signal, a time shift $t_{d}^{\prime \prime}$ is formed at the triggering threshold valve, which can be expressed

$$t_{d}''=\frac {1}{2\pi f}\ (\arcsin  m_{c}-\arcsin  m).$$

This time shift $t_{d}^{\prime \prime}$ changes the output signal frequency

$$\Delta f''=\frac {1}{t_{u}}-\frac {1}{t_{d}+t_{d}''},$$

which produces a measurement error $\delta^{\prime \prime}=(\Delta f-\Delta f^{\prime \prime}) /(\Delta f)$.

We see that with increasing frequency of emitted signal f the absence of superposition of a doubly reflected signal upon basic signal (7) is attained more easily and measurement errors $\delta'$ and $\delta''$ are reduced. Usually, in ultrasound flow meters, piezoelement assemblies with ceramics protected by fluoroplastic from the flow have $A_{1}/A_{C} \approx 0.08-0.1$, while whole metal assemblies have $A_{1}/A_{C} \approx 0.2-0.25$.

## LITERATURE CITED
1. V. I. Filatov, Ultrasound Flow Meter for Petroleum Products [in Russian], NTRS TsNIITENeftekhim, Moscow (1983), No. 1, p. 26.
