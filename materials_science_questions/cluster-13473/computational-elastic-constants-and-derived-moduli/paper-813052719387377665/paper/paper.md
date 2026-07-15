# Analysis of Gold Microbeams with Higher Order Continuum Theories

Murat Kandaz¹, Hüsnü Dal¹,*, and Mehmet Ünlü²

¹ Department of Mechanical Engineering, Middle East Technical University, Dumlupınar Bulvarı 1, 06800, Ankara, Turkey
² Department of Electrical and Electronics Engineering, Yıldırım Beyazıt University, 150. Sk. 7840, 06010, Ankara, Turkey

Microbeams are building blocks for many microstructures as well as microelectromechanical systems (MEMS) and cannot accurately be modelled by classical continuum theories due to size effects based on their micro-scale. These size effects can be taken into account by the so-called higher order continuum theories. *Modified Strain Gradient Theory* (MSGT) and *Modified Couple Stress Theory* (MCST) are two commonly used theories, which extend the classical local continuum theories of grade one with the introduction of additional length scale parameters. In this contribution, the variational problem governing the elasticity of higher order beam formulation and the finite element implementation based upon, are briefly introduced. To this end, well known Euler-Bernoulli beam formulation assumptions are used. The size effect for gold-micro beams is demonstrated and the length scale parameters of gold microbeams for MSGT and MCST are identified form the existing experimental data from literature for the first time. As a novel aspect, significant size effect is demonstrated for the length-scales associated with the state of the art gold microbeam structures developed for MEMS applications, which reveals the necessity of the use of higher order theories at these length scales. Advantages and drawbacks of these theories are also identified.

© 2017 Wiley-VCH Verlag GmbH & Co. KGaA, Weinheim

## 1 Higher Order Theories

MEMS structures incorporating gold microbeams are used vastly in many industries and improving steadily [1]. In order to incorporate size effects in these microbeams, *Modified Strain Gradient Theory* (MSGT) and *Modified Couple Stress Theory* (MCST) are used, which have been formulated by Lam et al. [2] and Yang et al. [3] respectively. In MSGT, the internal strain energy of a linear elastic solid is expressed as

$$
\Pi^{int} = \frac{1}{2} \int_{\Omega} \left( \boldsymbol{\sigma} : \delta \boldsymbol{\varepsilon} + \boldsymbol{p} \cdot \delta \nabla tr(\boldsymbol{\varepsilon}) + \boldsymbol{\tau}^{S(1)} : \delta \boldsymbol{\eta}^{S(1)} + \boldsymbol{m}^{S} : \delta \boldsymbol{\chi}^{S} \right) d\Omega
\tag{1}
$$

where the strain metrics are the normal strain tensor $\boldsymbol{\varepsilon}$, dilatation gradient vector $\nabla tr(\boldsymbol{\varepsilon})$, deviatoric stretch gradient vector $\boldsymbol{\eta}^{S(1)}$, and rotation gradient tensor $\boldsymbol{\chi}^{S}$. Their respective work conjugates are the stress metrics, which in turn are defined as Cauchy stress tensor $\boldsymbol{\sigma}$, pressure gradient vector $\boldsymbol{p}$, traceless part of the double stress tensor $\boldsymbol{\tau}^{S(1)}$, and couple stress tensor $\boldsymbol{m}^{S}$. The higher order stress-strain relationships are established via elastic constants $(\lambda, \mu)$ and length scale parameters $(l_0, l_1, l_2)$ as

$$
\boldsymbol{p} = 2\mu l_0^2 \nabla tr(\boldsymbol{\varepsilon}), \quad \boldsymbol{\tau}^{S(1)} = 2\mu l_1^2 \boldsymbol{\eta}^{S(1)}, \quad \boldsymbol{m}^{S} = 2\mu l_2^2 \delta \boldsymbol{\chi}^{S}
\tag{2}
$$

MCST is usually elaborated as the special case of MSGT in which $l_0 = l_1 = 0$, which further reduces the number of unknown length scale parameters in MSGT to one $(l_2)$. The length scale parameters for both MSGT $(l_0, l_1, l_2)$ and MCST $(l_2)$ are hereinafter referred to as $l$. For further sections it will be assumed that $l_0 = l_1 = l_2$, hence $l_0$ will be used to refer to the length scale parameter for MSGT, whereas $l_2$ will be used for MCST.

## 2 Quantification of Length Scale Parameters

Finite element codes are developed using variational principles. Then, experiments of Espinosa et al. [4] are simulated with these codes in order to come up with unknown length scale parameters for gold. An error parameter as the L2-norm of the residual vector is defined and sequential runs are performed for various values elastic moduli $E$ and corresponding values of $l$ that minimize the error function are determined. The minimum and maximum values of $E$ are chosen according to the upper and lower limits reported in literature, i.e. 140 GPa and 20 GPa respectively. The length scale parameters yielding the minimum error for macroscopic elastic modulus of gold i.e. $E$=80 GPa are found as $l_0$=3.60 $\mu$m for MSGT and $l_2$=6.75 $\mu$m for MCST [5,6]. As the increment of length scale parameter variation is 0.05 $\mu$m in the analysis, the results are correct with an accuracy of $\pm$ 0.025 $\mu$m. Further sequential runs with smaller intervals in length scale parameter variation yield that the values upto 6 significant figures are $l_0$=3.76862 $\mu$m for MSGT and $l_2$=6.74013 $\mu$m for MCST. For lower and upper bounds of $E = 20$ GPa and $E = 140$ GPa, length scale parameters are also found as $l_{0,20} = 7.15$ $\mu$m, $l_{0,140} = 2.70$ $\mu$m for MSGT, $l_{2,20} = 13.50$ $\mu$m, $l_{2,140} = 5.10$ $\mu$m for MCST.

* Corresponding author: e-mail dal@metu.edu.tr, phone +90 312 210 2584, fax +90 312 210 2536

© 2017 Wiley-VCH Verlag GmbH & Co. KGaA, Weinheim

## 3 Size Effects

Using these values of length scale parameters, a comparison is made between the beam deflection predictions of classical theory and higher order theories as given in Figure 1.

![](./images/813052719387377665_1.jpg)
![](./images/813052719387377665_2.jpg)

Fig. 1: Ratio of midpoint deflection with higher order theories ($w^m$) to those predicted with classical theories ($w_0^m$) for double-cantilevered beams for (a) MSGT and (b) MCST. The beam is under external point load applied at the midpoint. The length scale parameters are taken as given in Section 2, and the aspect ratio (thickness:width:length) is 1:5:20.

It is seen that the error of using classical theory with macroscopic material parameters in predicting beam deflections is more than 10% if thickness is reduced below 30 $\mu$m. The same error becomes more than 25% if the relevant beam thickness is taken smaller than 15 $\mu$m. The changes in beam aspect ratio almost do not affect these values.

## 4 Conclusion

It is proposed to the MEMS community that using the classical beam theory results in errors in predicting microbeam behavior under external forces. It is concluded that higher-order theories should be employed for gold beams with thickness smaller than 30 $\mu$m. Unfortunately, due to lack of adequate number of experimental data performed on varying beam thickness, a unique set of parameters could not be obtained for gold. For this purpose, the length scale parameter according to the selected modulus of elasticity parameters are identified. A length scale parameter of 3.60 $\mu$m for MSGT (in the case of $l_0 = l_1 = l_2$) and 6.75 $\mu$m for MCST are found for bulk elastic parameters. Several aspects such as correlation between length scale parameters, shape functions, and convergence characteristics are also elaborated. It is shown that both MSGT and MCST provide accurate estimates for microbeam behavior. MCST is demonstrated to be as powerful as MSGT even with minimum number of finite elements and reduced number of length scale parameters. It is also much easier to be implemented based on its finite element formulation.

### Acknowledgements
The financial support from Tubitak under grant number 116M258 is gratefully acknowledged.

### References

[1] C.W. Berry, N. Wang, M.R. Hashemi, M. Ünlü, and M. Jarrahi. Significant performance enhancement in photoconductive terahertz optoelectronics by incorporating plasmonic contact electrodes. Nature Comms. **4**, 1622 (2013).

[2] D.C.C. Lam, F. Yang, A.C.M. Chong, J. Wang and P. Tong. Experiments and theory in strain gradient elasticity. Int. J. Solids Struct. **51**, 1477 (2003).

[3] F. Yang, A.C.M. Chong, D.C.C. Lam, and P. Tong. Couple stress based strain gradient theory for elasticity. Int. J. Solids Struct. **39**, 2731 (2002).

[4] H.D. Espinosa, B.C. Prorok, and M. Fischer. A methodology for determining mechanical properties of freestanding thin films and MEMS materials. J. Mech. Phys. Solids **51**, 47 (2003).

[5] H. Dal. Analysis of gold microbeams with modified strain gradient theory. AUJST-A. Manuscript submitted for publication (2017).

[6] M. Kandaz, H. Dal, and M. Ünlü. A comparative study of modified strain gradient theory and modified couple stress theory for gold microbeams. Int. J. Non. Mech. Manuscript under review (2017).