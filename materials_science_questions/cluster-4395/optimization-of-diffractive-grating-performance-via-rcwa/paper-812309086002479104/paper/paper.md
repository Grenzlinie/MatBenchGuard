# USE OF PERIODIC STRUCTURES TO PRODUCE STANDARD MEASURES OF REFLECTION COEFFICIENT

O. A. D'yakonova, Yu. N. Kazantsev, A. N. Sivov,
and A. D. Chuprin

UDC 621.371:538.566

The possibility of designing standard measures of reflection coefficient in free space is analyzed. It is suggested that closely periodic gratings of metal wires of rectangular cross section should be used as standard measures.

One of the most pressing problems in measurement techniques is to design standard measures of reflection coefficient of electromagnetic waves in free space. The need to measure the characteristics of different kinds of materials and devices and also their standardization require the provision of units of measurement by which they can be compared with certain standard measures corresponding to different levels of reflection coefficient.

In existing methods of measuring reflection coefficient (see, for example, [1]) a plane-parallel metal plate is used to calibrate the measuring apparatus. One cannot use such a calibrated plate as a standard measure of reflection coefficient in open space because of a number of factors which considerably affect the accuracy of the measurements. These include rereflections between the plate and the components of the measuring apparatus, and the insufficient linearity of the receiving apparatus.

Sometimes one can use plane-parallel dielectric plates as standard measures of reflection coefficient. However, the use of dielectrics for standard measures encounters a number of problem that are difficult to solve. On the one hand, the good electrodynamic characteristics of such materials as polystyrene, polyethylene, teflon and plexiglass were seen, in principle, to make them suitable for producing standard measures. On the other hand, however, such characteristics as aging, the temperature dependence of the parameters, the degree of uniformity and the isotropy of these materials do not satisfy the requirements imposed on standard measures.

By analyzing the different approaches to the design of standard measures of reflection coefficient in free space, we decided to choose a periodic structure for investigation. In this paper we propose to use a set of closely periodic gratings of metal wires of rectangular cross section (Fig. 1) as standard measures of reflection coefficient. Theoretical and experimental investigations of the electrodynamic properties of periodic gratings of finite dimensions of this kind are always fairly complex and time consuming. Below we consider a theoretical method chosen for the calculation and we describe the results of experimental investigations on periodic gratings which we constructed.

The use of a set of such gratings enables a wide dynamic range of reflection coefficients to be covered. The most convenient from the point of view of ease of manufacture and of attaining the required accuracy is to use gratings of wires of rectangular transverse cross section. However, despite the simplicity of the geometry such arrays are a fairly complex electrodynamic system, particularly in the resonance region, i.e., when the wavelength $\lambda$ is comparable with the period p of the array. In this case one has to use fairly complex numerical methods which take up considerable time (see, for example, [2]).

Fairly accurate values of the reflection coefficient can be obtained by the methods developed in [3-5]. These methods can be used when the period of the array is 5-10 times less than the wavelength, depending on the filling factor of the array q = 2b/p (see Fig. 1) and on the required accuracy. The accuracy of the calculations is then proportional to $(p/\lambda)^2$. Below we describe an algorithm for calculating the reflection coefficient using the method proposed in [3]. The use of Floquet's theorem enables one to reduce the problem of the diffraction of an electromagnetic field by an infinite array to the corresponding problem for a single period of the array. The reflection and transmission coefficients can then be expressed solely in terms of the currents in the contour of the wire. The sole approximation is that these currents and fields in the immediate vicinity of

---
Translated from Izmeritel'naya Tekhnika, No. 6, pp. 48-49, June, 1994.
---

![](./images/812309086002479104_1.jpg)

Fig. 1. Grating of bars of rectangular
transverse cross section.

the wires are not found from Helmholtz's equation but from Laplace's equation. The latter is solved by the method of conformal transformations. In [3], in particular, explicit expressions were obtained for the reflection coefficient R and the transmission coefficient T of a plane wave incident at an arbitrary angle $\varphi$ on an infinite gratings of rectangular metal wires. For the case of H-polarization these formulas have the form (see Fig. 1):

$$
\begin{aligned}
& R=\frac{1}{2}\left\{\frac{\beta+i k\left(l+\alpha^{2} l_{2}\right)}{\beta-i k\left(l+\alpha^{2} l_{2}\right)}-\frac{1-i k \beta l_{1}}{1+i k \beta l_{1}}\right\} ; \\
& T=\frac{1}{2}\left\{\frac{\beta+i k\left(l+\alpha^{2} l_{2}\right)}{\beta-i k\left(l+\alpha^{2} l_{2}\right)}+\frac{1-i k \beta l_{1}}{1+i k \beta l_{1}}\right\},
\end{aligned} \tag{1}
$$

where

$$
\begin{gathered}
\beta=\cos \varphi ; \quad \alpha=\sin \varphi ; \quad k=2 \pi / \lambda ; \quad l=2 b h / p ; \\
l_{2}=l_{1}+p /(2 \pi) \ln [(\sigma-1) / \sigma] ; \\
l_{1}=\frac{t p}{2 \pi} \int_{0}^{1 / \sigma} \frac{d u}{\sqrt{(1-u)(1-\sigma u)}(\sqrt{1-t u}+1)}.
\end{gathered}
$$

In the case of normal incidence of a plane wave we must put $\beta=1$, $\alpha=0$ in (1). The parameters $\sigma$ and t, which depend on the relative dimensions of the wires of the array, are found by solving the following system of equations:

$$
\left.\begin{array}{l}
\pi q=I_{1}(\sigma, t) ; \\
2 \pi h / p=I_{2}(\sigma, t),
\end{array}\right\} \tag{2}
$$

where

$$
\begin{aligned}
I_{1}(\sigma, t)=\int_{0}^{t} & \sqrt{\frac{t-u}{u(1-u)(\sigma-u)}} d u ; I_{2}(\sigma, t)= \\
& =\int_{t}^{1} \sqrt{\frac{u-t}{u(1-u)(\sigma-u)}} d u.
\end{aligned}
$$

A numerical solution of the system of nonlinear equations (2) can be obtained, for example, by minimizing the function

$$
F(\sigma, t)=\left[\pi q-I_{1}(\sigma, t)\right]^{2}+\left[\frac{2 \pi h}{p}-I_{2}(\sigma, t)\right]^{2}.
$$

We used this simple method. Here, depending on q, the time taken to solve system (2) using a PC XT computer was from several seconds up to several tens of seconds, and the discrepancy in $F(\sigma, t)$ was of the order $10^{-8}-10^{-10}$. The greatest number of computing time is required when $q \to 1$, i.e. when the array approximates to a metal plane in its reflecting properties. It should be noted that the solution of system (2) does not just define a single point of the frequency characteristic of the array but the whole curve within the frequency band where the above approximation is applicable. This considerably reduces the amount of computing time required compared with other methods.

Note that the region in which the above numerical-analytical solution can be used is determined by the frequency band for which the equivalent conjugate boundary conditions of the corresponding electrodynamic problem hold [3]:

![](./images/812309086002479104_2.jpg)

Fig. 2. Reflection coefficient R as a function of the wave
length $\lambda$ and the slot width $\delta$.

$$
H_{z}^{-}-H_{z}^{+}=i k l_{1}\left(E_{x}^{+}+E_{x}^{-}\right) ;
$$

$$
E_{x}^{-}-E_{x}^{+}=i k\left[\left(H_{z}^{+}+H_{z}^{-}\right) l-i \frac{l_{2}}{k} \frac{\partial}{\partial x}\left(E_{y}^{+}+E_{y}^{-}\right)\right].
$$

After optimizing the parameters of the theoretically calculated closely periodic gratings we chose the geometrical dimensions for the assumed set of standard measures. This choice consists of six slotted arrays with a period p = 8 mm for each. The slots are cut in metal plates with overall dimensions of 440 × 340 mm made of dural with a thickness 2h = 2 mm. The width of a slot $\delta$ lies in the range 1-6 mm with a step of 1 mm.

The reflection coefficients were measured for three identical sets in the wavelength range from 8 mm to 150 mm using the methods described in [6,7]. The measurements were made for a working version when a plane H-polarized electromagnetic wave was incident normally (normal to the plane of the array) on the periodic grating.

An analysis of the measured dependences of the reflection coefficient R on the wavelength $\lambda$ enables us to draw the following conclusions:

the spread in the reflection coefficients due to manufacturing inaccuracies is considerably less than the measurement errors;

the reflection coefficient for all the gratings increases monotonically as the wavelength decreases, which can be clearly seen in Fig. 2.

The graphs in Fig. 2 show the experimentally measured reflection coefficient R as a function of the wavelength $\lambda$. The curves were obtained for the wavelength range in which calculation does not give the required accuracy. The error in measuring R is $5 \%$. At wavelengths above 40 mm the error in the calculation also does not exceed $5 \%$. Hence, in the wavelength range $\lambda<40 \mathrm{~mm}$ one can use the results of measurements, whereas in the region $\lambda>40 \mathrm{~mm}$ one must use the results of calculation.

These investigations of a periodic structure, which are accessible to both theoretical and experimental methods, enabled us to develop and put into practical use a set of standard measures of reflection coefficient in free space.

REFERENCES

1. V. N. Apletalin, O. A. D'yakonova, Yu. N. Kazantsev, and V. S. Solosin, Izmer. Tekh., No. 7, 40 (1991).
2. V. P. Shestopalov, L. N. Litvinenko, S. A. Masalov, and V. G. Sologub, Diffraction of Waves by Gratings [in Russian], Izd. Khar'k. Univ., Khar'kov (1973), p. 288.
3. E. I. Nefedov and A. N. Sivov, Electrodynamics of Periodic Structures [in Russian], Nauka, Moscow (1977), p. 209.
4. L. A. Vainshtein, The Electrodynamic Theory of Gratings, in 4 volumes: High-Power Electronics [in Russian], Nauka, Moscow (1963), No. 2, pt. 1, p. 26.
5. N. Marcuvitz, Waveguide Handbook (M.I.T. Radio Lab. Series Vol. 10), McGraw-Hill, New York (1951).

6.  V. N. Apletalin, O. A. Dyakonova, Y. N. Kazantsev, et al., Proc. Joint 3rd Intern. Conf. on Electromagnetics in Aerospace Applications and 7th Europ. Electromagnetic Structures Conf., Torino, Italy (1993), p. 253.

7.  V. N. Apletalin, O. A. Dyakonova, Y. N. Kazantsev, et al, Proc. Joint 23rd Europ. Microwave Conf., Madrid, Spain (1993), p. 308.