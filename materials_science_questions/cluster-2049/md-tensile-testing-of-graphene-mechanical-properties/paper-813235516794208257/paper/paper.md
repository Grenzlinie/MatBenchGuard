# Improved beam theory for multilayer graphene nanoribbons with interlayer shear effect

D.Y. Liu $^{a}$, W.Q. Chen $^{b,c,*}$, Ch. Zhang $^{d}$

$^{a}$ Department of Civil Engineering, Zhejiang University, Hangzhou 310058, PR China
$^{b}$ State Key Lab of CAD \& CG, Zhejiang University, Hangzhou 310058, PR China
$^{c}$ Department of Engineering Mechanics, Zhejiang University, Hangzhou 310027, PR China
$^{d}$ Department of Civil Engineering, University of Siegen, Siegen 57068, Germany

---

## ARTICLE INFO

Article history:
Received 4 December 2012
Received in revised form 23 February 2013
Accepted 27 March 2013
Available online 29 March 2013
Communicated by R. Wu

Keywords:
Multilayer graphene
In-plane extension
Improved beam theory

## ABSTRACT

The bending of multilayer graphene nanoribbons incorporating the effect of interlayer shear is analyzed in this Letter. An improved beam theory is adopted and extended in which the in-plane extension of each layer is also taken into account. The governing equations for bilayer and trilayer graphene nanoribbons subjected to bending are presented as illustrative examples. Exact solutions for cantilever multilayer graphene nanoribbons are derived. Compared with the molecular dynamics (MD) simulations, the present beam model predicts much better results than the previous beam model in which the in-plane extension is ignored. The current study provides a strong evidence to include the in-plane extension effect in the continuum modeling of multilayer graphene structures.

© 2013 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Graphene, which is the thinnest known material and the strongest ever measured, has sparked much interest among worldwide research groups recently [1–4]. There have been great deals of investigations on the exceptional mechanical properties of graphene, such as the excellent extensibility up to 20% strain [5,6], the extremely large flexibility [7,8], and the super-high in-plane stiffness [9–12]. Many efforts have been made to determine the material constants of graphene, through the experiment, atomic simulation, and continuum mechanics modeling. Lee et al. measured the elastic constants of monolayer graphene membranes by nanoindentation [8]. Poot and van der Zant measured the mechanical properties of few-layer graphene with an atomic force microscope and obtained the bending rigidity of and the tension in ultrathin membranes [9]. The elastic deformation and failure strength of graphene have been studied using ab initio methods [10,11]. Zhao et al. investigated the mechanical strength and properties of graphene using molecular dynamics simulations [12]. Quasi-one-dimensional graphene nanoribbons can be achieved by patterning a two-dimensional graphene [13,14], and have been applied in a wide range of device applications in nanotechnology due to the outstanding mechanical, electronic transport and spin transport properties [15–18]. Recently, Liu et al. proposed a multi-beam shear model, which takes account of interlayer shear but neglects intralayer stretch, to study the dynamic response of multilayer graphene nanoribbons, under the assumption that each constituent layer has the same transverse displacement during deformation as clearly indicated by molecular dynamics simulations [19]. Using the multi-beam shear model, Shen and Wu recently investigated the interlayer shear effect on the bending behavior of multilayer graphene, with the Young's modulus and interlayer shear modulus calculated directly from the MD simulations; certain difference in bending response predictions between MD simulations and the multi-beam shear model is however observed, which becomes more prominent when the layer number is smaller than 5 [20]. It is noted that, the multi-beam shear model proposed and used in Refs. [19,20] is essentially a reduced version of Newmark's theory for composite beams with only two layers [21]. Newmark's beam theory includes both effects of in-plane extension and interlayer shear, and has found wide applications in the field of civil engineering [22,23].

In this Letter, we are interested in the effects of the in-plane extension (or intralayer stretch) on the bending response of multilayer graphene nanoribbons, which has been neglected in the previous studies in consideration of the super-high in-plane stiffness of graphene. However, since the relative stretch or contraction between longitudinal fibers is an important aspect even in the pure bending problem of a single-layer beam, the in-plane

---

* Corresponding author at: Department of Engineering Mechanics, Zhejiang University, Hangzhou 310027, PR China. Tel./fax: +86 571 87951866.
E-mail address: chenwq@zju.edu.cn (W.Q. Chen)

0375-9601/$ – see front matter © 2013 Elsevier B.V. All rights reserved.
http://dx.doi.org/10.1016/j.physleta.2013.03.033

![](./images/813235516794208257_1.jpg)
![](./images/813235516794208257_2.jpg)
![](./images/813235516794208257_3.jpg)

![](./images/813235516794208257_4.jpg)

Fig. 1. Cantilever bilayer graphene nanoribbon subjected to a tip force.

![](./images/813235516794208257_5.jpg)

Fig. 2. Differential element in BGNR with interlayer shear effect.

extension may be somehow important in correctly understand- ing the response of multilayer graphene nanoribbons. With this in mind, Newmark's composite beam theory is employed and ex- tended to the multilayer case, along with a new presentation of the basic formulations. The deflection expressions of cantilever bi- layer and trilayer graphene nanoribbons subjected to a tip force are derived exactly. The procedure can be similarly applied to $n$-layer graphene nanoribbons. Our theoretical predictions are in excellent agreement with the MD simulations in Ref. [20], indicating the im- portance to include the in-plane extension.

## 2. Exact bending analysis of cantilever multilayer graphene

We define the size of the single-layer graphene nanoribbon by its length $l$, thickness $h$ and width $b$. First, let us consider a can- tilever bilayer graphene nanoribbon (BGNR). The coordinate system $xoy$ is introduced such that the $x$-axis is located at the interface, and the $y$-axis placed at the left-end of BGNR, as shown in Fig. 1. Using Newmark's beam theory, the normal stresses in the two constituent layers can be obtained as $\sigma_{1}=E\kappa(y+h/2)+E\varepsilon_{01}$, $\sigma_{2}=E\kappa(y-h/2)+E\varepsilon_{02}$, where $\varepsilon_{01}$ and $\varepsilon_{02}$ are the normal strains at the respective centroidal principal axes, $\kappa(x)$ is the common cur- vature, and $E$ is the elastic modulus. The equilibrium conditions lead to

$$
\begin{aligned}
& \int_{A_{1}} \sigma_{1} \mathrm{~d} A_{1}+\int_{A_{2}} \sigma_{2} \mathrm{~d} A_{2}=0, \\
& \int_{A_{1}} \sigma_{1} y \mathrm{~d} A_{1}+\int_{A_{2}} \sigma_{2} y \mathrm{~d} A_{2}=-P(l-x).
\end{aligned}
\tag{1}
$$

Substituting the normal stresses $\sigma_{1}$ and $\sigma_{2}$ into Eq. (1), we can express $\varepsilon_{01}$ and $\varepsilon_{02}$ in term of the curvature $\kappa(x)$ as

$$
\varepsilon_{01}=\frac{h}{6} \kappa-\frac{P(x-l)}{E b h^{2}}, \quad \varepsilon_{02}=\frac{P(x-l)}{E b h^{2}}-\frac{h}{6} \kappa.
\tag{2}
$$

Consider the free body of a differential element of BGNR, as shown in Fig. 2. The moment, shear force, longitudinal force, and slip force per unit length are denoted by $M$, $Q$, $N$, and $\tau$, respectively.

For equilibrium, the following well-known relationships should hold

$$
\frac{\mathrm{d} Q}{\mathrm{~d} x}=-q, \quad \frac{\mathrm{d} M}{\mathrm{~d} x}=Q.
\tag{3}
$$

In our analysis, there is no applied transverse force except at the cantilever tip so that $q=0$. Further, from the equivalence consider- ation, we have the following relations between the resultant forces applied on the whole section and those on the constituent layers as

$$
\begin{aligned}
& F=N_{1}+N_{2}=0, \\
& Q=Q_{1}+Q_{2}, \\
& M=M_{1}+M_{2}-N_{1} h.
\end{aligned}
\tag{4}
$$

The moment equilibrium of each layer yields

$$
Q_{1}=\frac{\mathrm{d} M_{1}}{\mathrm{~d} x}+\tau \frac{h}{2}, \quad Q_{2}=\frac{\mathrm{d} M_{2}}{\mathrm{~d} x}+\tau \frac{h}{2}.
\tag{5}
$$

Substituting into the second equation of Eq. (4), and then differen- tiating with respect to $x$, we obtain

$$
\frac{\mathrm{d} Q}{\mathrm{~d} x}=\frac{\mathrm{d}^{2} M_{1}}{\mathrm{~d} x^{2}}+\frac{\mathrm{d}^{2} M_{2}}{\mathrm{~d} x^{2}}+h \frac{\mathrm{d} \tau}{\mathrm{d} x}.
\tag{6}
$$

The slip force $\tau$ due to the interlayer shear is assumed to be pro- portional to the displacement jump, i.e. $\tau=K(u_{2}-u_{1}+h \mathrm{~d} w / \mathrm{d} x)$, where $u_{1}$ and $u_{2}$ are the axial displacements at the respec- tive centroidal principal axes, $w$ is the deflection, and $K=G b / h$ is the interface slip stiffness [24], with $G$ being the interlayer shear modulus. Since $M_{1}=M_{2}=E I \kappa$, Eq. (6) can be rewritten as

$$
\frac{\mathrm{d} Q}{\mathrm{~d} x}=2 E I \frac{\mathrm{d}^{2} \kappa}{\mathrm{d} x^{2}}+K h\left(\varepsilon_{02}-\varepsilon_{01}-h \kappa\right)=0.
\tag{7}
$$

From Eqs. (2) and (7), we can obtain a second-order ordinary dif- ferential equation in terms of the curvature $\kappa$,

$$
\frac{\mathrm{d}^{2} \kappa}{\mathrm{d} x^{2}}-\frac{8 K}{E b h} \kappa-\frac{12 K P(l-x)}{E^{2} b^{2} h^{4}}=0.
\tag{8}
$$

With $\kappa = -d^2w/dx^2$, Eq. (8) becomes
$$
\frac{\mathrm{d}^{4} w}{\mathrm{~d} x^{4}}-\frac{8 G}{E h^{2}} \frac{\mathrm{d}^{2} w}{\mathrm{~d} x^{2}}+\frac{12 G(l-x) P}{E^{2} b h^{5}}=0.
\tag{9}
$$

The solution to this equation satisfying the boundary conditions at the two ends of a cantilever beam can be found as
$$
\begin{aligned}
w(x)= & \frac{9 P}{16 \lambda\left(1+e^{2 \lambda l}\right) G b h}\left(1-e^{2 \lambda l}-e^{\lambda x}+e^{2 \lambda l-\lambda x}\right) \\
& +\frac{9 P}{16 G b h} x-\frac{P\left(x^{3}-3 l x^{2}\right)}{4 E b h^{3}}
\end{aligned}
\tag{10}
$$
where $\lambda^{2}=\frac{8 G}{E h^{2}}$. The transverse displacement at $x=l$ is
$$
w_{l}=w(l)=\frac{9 P\left(1-e^{2 \lambda l}\right)}{16 \lambda\left(1+e^{2 \lambda l}\right) G b h}+\frac{9 P l}{16 G b h}+\frac{P l^{3}}{2 E b h^{3}}.
\tag{11}
$$

If the two layers are perfectly bonded, the interlayer shear stiffness becomes infinite $(G \rightarrow \infty)$, then Eq. (11) gives $w_{l}=\frac{P l^{3}}{2 E b h^{3}}$, which is the classical solution of a cantilever beam (of thickness $2 h$) subjected to a tip force.

For a cantilever trilayer graphene nanoribbon (TGNR), the $x$-axis of the coordinate system $x o y$ is taken to coincide with the centroidal principal axis of the second layer. Similar to the analysis of BGNR, the normal stresses in the three layers are $\sigma_{1}=$ $E \kappa(y+h)+E \varepsilon_{01}, \sigma_{2}=E \kappa y+E \varepsilon_{02}$, and $\sigma_{3}=E \kappa(y-h)+E \varepsilon_{03}$, respectively. The equilibrium conditions of TGRN are characterized by
$$
\begin{aligned}
& \int_{A_{1}} \sigma_{1} \mathrm{~d} A_{1}+\int_{A_{2}} \sigma_{2} \mathrm{~d} A_{2}+\int_{A_{3}} \sigma_{3} \mathrm{~d} A_{3}=0, \\
& \int_{A_{1}} \sigma_{1} y \mathrm{~d} A_{1}+\int_{A_{2}} \sigma_{2} y \mathrm{~d} A_{2}+\int_{A_{3}} \sigma_{3} y \mathrm{~d} A_{3}=-P(l-x).
\end{aligned}
\tag{12}
$$

The relations between the resultant forces applied on the whole section and those on the constituents are
$$
\begin{aligned}
& F=N_{1}+N_{2}+N_{3}=0, \\
& Q=Q_{1}+Q_{2}+Q_{3}, \\
& M=M_{1}+M_{2}+M_{3}-N_{1} h+N_{3} h.
\end{aligned}
\tag{13}
$$

The moment equilibrium of each layer yields
$$
\begin{aligned}
& Q_{1}=\frac{\mathrm{d} M_{1}}{\mathrm{~d} x}+\frac{1}{2} h \tau_{1}, \\
& Q_{2}=\frac{\mathrm{d} M_{2}}{\mathrm{~d} x}+\frac{1}{2} h\left(\tau_{1}+\tau_{2}\right), \\
& Q_{3}=\frac{\mathrm{d} M_{3}}{\mathrm{~d} x}+\frac{1}{2} h \tau_{2}.
\end{aligned}
\tag{14}
$$

The slip forces $\tau_{1}$ and $\tau_{2}$ between respective layers are given by $\tau_{1}=K\left(u_{2}-u_{1}+h \mathrm{~d} w / \mathrm{d} x\right)$ and $\tau_{2}=K\left(u_{3}-u_{2}+h \mathrm{~d} w / \mathrm{d} x\right)$. Combining them with the second equation of Eq. (13) as well as Eq. (14), we obtain
$$
3 E I \frac{\mathrm{d}^{2} \kappa}{\mathrm{d} x^{2}}+K h\left(\varepsilon_{03}-\varepsilon_{01}-2 h \kappa\right)=0.
\tag{15}
$$

The force equilibrium in the longitudinal direction in each layer requires that
$$
\frac{\mathrm{d} N_{1}}{\mathrm{~d} x}=-\tau_{1}, \quad \frac{\mathrm{d} N_{2}}{\mathrm{~d} x}=\tau_{1}-\tau_{2}, \quad \frac{\mathrm{d} N_{3}}{\mathrm{~d} x}=\tau_{2},
\tag{16}
$$
where $N_{1}=E A \varepsilon_{01}, N_{2}=E A \varepsilon_{02}, N_{3}=E A \varepsilon_{03}$ are the axial forces in the three layers. From Eqs. (12), (15) and (16), we can obtain a differential equation for TGNR in terms of the deflection $w$ as
$$
\frac{\mathrm{d}^{4} w}{\mathrm{~d} x^{4}}-\frac{9 G}{E h^{2}} \frac{\mathrm{d}^{2} w}{\mathrm{~d} x^{2}}+\frac{4 G(l-x) P}{E^{2} b h^{5}}=0.
\tag{17}
$$

![](./images/813235516794208257_6.jpg)

Fig. 3. Comparison between the results predicted by Newmark's beam theory and the MD simulations.

By incorporating the boundary conditions, the deflection of the cantilever TGNR is obtained as
$$
\begin{aligned}
w(x)= & \frac{32 P}{81 \lambda\left(1+e^{2 \lambda l}\right) G b h}\left(e^{2 \lambda l-\lambda x}-e^{\lambda x}+1-e^{2 \lambda l}\right) \\
& -\frac{2 P\left(x^{3}-3 l x^{2}\right)}{27 E b h^{3}}+\frac{32 P x}{81 G b h}
\end{aligned}
\tag{18}
$$
where $\lambda^{2}=\frac{9 G}{E h^{2}}$. The deflection of TGNR at $x=l$ is
$$
w_{l}=\frac{32 P\left(1-e^{2 \lambda l}\right)}{81 \lambda\left(1+e^{2 \lambda l}\right) G b h}+\frac{4 P l^{3}}{27 E b h^{3}}+\frac{32 P l}{81 G b h}.
\tag{19}
$$

For $G \rightarrow \infty$, we again get the classical solution for a cantilever TGNR of thickness $3 h$. The same procedure can be applied to a cantilever multilayer graphene nanoribbon (MGNR) as well, and is not repeated here for simplicity.

## 3. Numerical results and comparison

The variation of $\mathrm{Pl} /\left(w_{l} b h\right)$ with the layer number $n$, which is predicted from the above beam theory, is depicted in Fig. 3. The Young's modulus of graphene and the interlayer shear modulus are taken to be the same as those obtained in Ref. [20], e.g. $E=1.0$ TPa and $G=4.6$ GPa. The corresponding results calculated using MD simulations are also given in the same figure [25]. As can be seen, the two predictions agree quite well. In particular, as pointed out in Ref. [20], the results of the MD simulations for layer number $n \geqslant 5$ can be linearly fitted as $\mathrm{Pl} /\left(w_{l} b h\right)=$ $4.05(n-3.35)$ (GPa), differing significantly from $\mathrm{Pl} /\left(w_{l} b h\right)=$ $4.9546(n-0.9651)$ obtained by the multi-beam model, in which the in-plane extension is neglected. The fitting line of our results for $n \geqslant 5$, which take account of the in-plane extension, is obtained as $\mathrm{Pl} /\left(w_{l} b h\right)=4.18(n-3.72)$ and is shown in Fig. 4. Apparently, our results are much better than those obtained from the multi-beam model and are much closer to the MD simulation results. Furthermore, the variation of $\mathrm{Pl} /\left(w_{l} b h\right)$ with $n$ is no longer linear for layer number $n<5$, as indicated by MD simulations. While the prediction based on the multi-beam model is still linear and becomes obviously inaccurate, our prediction can capture this non-linear feature and matches the MD simulations very well, as shown in Fig. 3. Thus, all the above observations indicate that the in-plane extension of multilayer graphene nanoribbons plays a significant role in their bending response, and should be taken into consideration when setting up the continuum beam model.

![](./images/813235516794208257_7.jpg)

Fig. 4. Comparison of various fitting lines for $n \geqslant 5$.

## 4. Conclusions

In this Letter, we investigated the effect of interlayer shear on the bending behavior of cantilever multilayer graphene nanoribbons using Newmark's beam theory, which includes both the interlayer shear and the in-plane extension (or intralayer stretch). The results we obtained coincide with the MD simulation results very well, not only for the linear part when the layer number $n \geqslant 5$, but also for the nonlinear part when $n < 5$. By comparison with the results based on the multi-beam model, we conclude that the in-plane extension should be considered to correctly predict the bending response of multilayer graphene structures.

It is worth pointing out that, although the comparison of the multi-beam model with MD simulation in Ref. [19] also shows good agreement, the Young's modulus and interlayer shear modulus adopted by these authors ($E = 0.11$ TPa, $G = 0.25$ GPa) are quite different from those obtained by others ($E \sim 1.0$ TPa, $G \sim$ 5 GPa, see Table 1 of Ref. [20]). When more reasonable elastic properties are adopted as done in Ref. [20], the multi-beam model predicts quantitatively different results from the MD simulation due to the neglect of in-plane extension, as clearly revealed by our study.

Size effect may present for structures at nanoscale, which has not been considered in our model. Once it is necessary, we can construct new beam models with size effect based on high-order continuum mechanics theories such as the nonlocal elasticity, surface elasticity, gradient elasticity, etc.

## Acknowledgements

This work was supported by the National Natural Science Foundation of China (Grant Nos. 11090333, 10832009 and 11272281) and the German Research Foundation (DFG, Project No. ZH 15/20-1).

## References

[1] A.K. Geim, K.S. Novoselov, Nature Mater. 6 (2007) 183.
[2] J.C. Meyer, A.K. Geim, M.I. Katsnelson, K.S. Novoselov, T.J. Booth, S. Roth, Nature 446 (2007) 60.
[3] S.C. Pradhan, Phys. Lett. A 373 (2009) 4182.
[4] F. Scarpa, S. Adhikari, R. Chowdhury, Phys. Lett. A 374 (2010) 2053.
[5] Z.P. Xu, J. Comput. Theor. Nanosci. 6 (2009) 625.
[6] Z.P. Xu, M.J. Buehler, ACS-Nano 4 (2010) 3869.
[7] A.K. Geim, Science 324 (2009) 1530.
[8] Q. Wang, Phys. Lett. A 374 (2010) 1180.
[9] C. Lee, X. Wei, J.W. Kysar, J. Hone, Science 321 (2008) 385.
[10] M. Poot, H.S.J. van der Zant, Appl. Phys. Lett. 92 (2008) 063111.
[11] F. Liu, P. Ming, J. Li, Phys. Rev. B 76 (2007) 064120.
[12] H. Zhao, K. Min, N.R. Aluru, Nano Lett. 9 (2009) 3012.
[13] B. Obradovic, R. Kotlyar, F. Heinz, P. Matagne, T. Rakshit, M.D. Giles, M.A. Stet-tler, D.E. Nikonov, Appl. Phys. Lett. 88 (2006) 142102.
[14] F. Yu, H.Q. Zhou, Z.X. Zhang, D.S. Tang, M.J. Chen, H.C. Yang, G. Wang, H.F. Yang, C.Z. Gu, L.F. Sun, Appl. Phys. Lett. 100 (2012) 101904.
[15] M.A. Rafiee, W. Lu, A.V. Thomas, A. Zandiatashbar, J. Rafiee, J.M. Tour, N.A. Koratkar, ACS-Nano 4 (2010) 7415.
[16] L.Y. Jiao, L. Zhang, X.R. Wang, G. Diankov, H.J. Dai, Nature 458 (2009) 877.
[17] D.V. Kosynkin, A.L. Higginbotham, A. Sinitskii, J.R. Lomeda, A. Dimiev, B.K. Price, J.M. Tour, Nature 458 (2009) 872.
[18] H. Ren, Q.X. Li, Y. Luo, J.L. Yang, Appl. Phys. Lett. 94 (2009) 173110.
[19] Y. Liu, Z.P. Xu, Q.S. Zheng, J. Mech. Phys. Solids 59 (2011) 1613.
[20] Y.K. Shen, H.A. Wu, Appl. Phys. Lett. 100 (2012) 101909.
[21] N.M. Newmark, C.P. Siest, I.M. Viest, Proc. Soc. Exper. Stress Anal. 9 (1952) 75.
[22] W.Q. Chen, Y.F. Wu, R.Q. Xu, Compos. Sci. Technol. 67 (2007) 2500.
[23] X.D. Shen, W.Q. Chen, Y.F. Wu, R.Q. Xu, Compos. Sci. Technol. 71 (2011) 1286.
[24] The interface slip stiffness equals the interlayer shear modulus multiplied by the beam width and divided by the interlayer spacing. The interlayer spacing is approximately the same as the layer thickness, see Ref. [20].
[25] The ordinate values in Fig. 2 of Ref. [20] should be multiplied by $L/bh$, and the unit should be $10^{-2}$ eV/Å², according to our private communication with the authors of Ref. [20].