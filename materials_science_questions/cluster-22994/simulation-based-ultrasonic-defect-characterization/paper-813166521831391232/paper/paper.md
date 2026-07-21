# Defect Detection Of The Segmental Spherical Shell
Based On Ultrasonic Transducer Array

Xipeng Li¹,ᵃ, Chunguang Xu¹,²,ᵇ,⁎, Lijiu Wang¹,ᶜ and Wei Dai¹,ᵈ

¹ School of Mechanical Engineering, Beijing Institute of Technology, No.5 Zhongguancun South Street, Haidian District, Beijing, 100081,China
² Department of Mechanical Engineering, Northwestern University, 1801 Hinman Avenue, Evanston, Illinois, 60208, USA

ᵃ lixipeng2008@163.com, ᵇ xucg@bit.edu.cn, ᶜ wanglijiu@bit.edu.cn, ᵈ 0453115@163.com

Keywords: guided wave; dispersion; nondestructive; transducer array.

Abstract. It is of great significance to monitor and quantify the defects in the thin segmental spherical shell components. In the paper the guided wave's inspiring method has been obtained from the wave-mode conversion based on the theory of the guided wave propagating in the thin spherical shell. Using the wavelet to process the testing signal, and the ellipse localization imaging algorithm, the defect's localization and orientation can be detected accurately. Experimental results show the defect's direction and location can be detected effectively and clearly.

## Introduction

The curved plate components, such as containers used in the oil, gas, petrochemical industry, ships and aircraft, are easily affected by the adverse environment, resulting in different defects which undermine the components' safety and reliability, or even lead to greater security risks. However it is difficult to detect the defects in them by using the traditional methods due to the signal distortion phenomenon in the curved shells[1, 2, 3, 4].

Kargl and Marston researched on the lamb-like wave in isotropic spherical shells[5]. Wang studied the stress wave propagation in orthotropic laminated spherical shells[6]. Towfighi and Kundu studied the wave propagation in anisotropic spherical curved plates[7]. The previous researches are mainly focusing on the theoretical research and rarely used in the practical detecting.

In this article, we introduced a detecting method for defect's location and direction by combining the ellipse locating algorithm with wavelet transform. Taking the small curvature spherical shell as the specimen, we got the guided wave's excitation and receiving method by solving the elastic equilibrium equations in spherical coordinate system and analyzing the guided wave dispersion characteristics. Experimental results show the defect's location and geometric shape images were obtained effectively.

## Fundamental of curved shell

The spherical coordinate system and corresponding stress components are shown in Fig. 1. Considering the boundary conditions of the thin segmental spherical shell, the elastic constants dependent of the position are given by
$$
C(r)=C \pi(r), \quad \rho(r)=\rho \pi(r) \tag{1}
$$
where $C(r)$ are position-dependent elastic constants of the medium that constitutes the spherical shell plate and $\pi(r)$ is the rectangular window function defined by
$$
\pi(r)=
\begin{cases}
1, & a \leq r \leq b \\
0, & elsewhere
\end{cases} \tag{2}
$$
Given Eq. 2, the outside segmental spherical shell as a medium with zero acoustic impedance ensures that the stresses outside the specimen vanish regardless of the displacement [8].

![](./images/813166521831391232_1.jpg)

Fig.1 Spherical coordinate system and stress components

The wave front on the surface of the spherical shell is assumed to be toroidal. For detecting the defect in the thin spherical shell, considered the guided wave's propagating law at a specific direction is adequate. Therefore, it is sufficient to solve the governing equations for $\theta=\pi / 2$. Suppose the displacement components of the toroidal wave as:
$$
\begin{aligned}
& u_{r}=U_{r}(r) \exp [i(k b \phi-\omega t)] \\
& u_{\theta}=V_{\theta}(r) \exp [i(k b \phi-\omega t)] \\
& u_{\phi}=W_{\phi}(r) \exp [i(k b \phi-\omega t)]
\end{aligned}
\tag{3}
$$
where $U(r), V(r)$ and $W(r)$ are the amplitude in the radial and two tangential directions respectively, $k$ is the magnitude of the wave vector in the wave propagating direction, and $\omega$ is the angular frequency.

In the spherical coordinate system, substituting Eq. 1, Eq. 2, and Eq. 3 into stress equilibrium equation, and based on the relationship between stress and displacement, the governing differential equations in terms of displacement components can be obtained as:
$$
\begin{aligned}
& {\left[r^{2} C_{11} U^{*}+2 r C_{11} U^{\prime}+i r k b\left(C_{12}+C_{11}\right) W^{\prime} / 2-\left(\left(2+k^{2} b^{2} / 2\right) C_{11}-k^{2} b^{2} C_{12} / 2\right) U\right.} \\
& \left.+i k b\left(-3 C_{11} / 2+C_{12} / 2\right) W\right] \pi(r)+(\delta(r-a)-\delta(r-b))\left[r^{2} C_{11} U^{\prime}+r\left((2+i k b / 2) C_{12}+i k b C_{15} / 2\right) U\right. \\
& \left.+i r k b C_{12} W\right]=-\rho r^{2} \omega^{2} U \pi(r)
\end{aligned}
\tag{4}
$$

$$
\begin{aligned}
& {\left[\left(r^{2}\left(C_{11}-C_{12}\right) / 2\right) V^{*}+r\left(C_{11}-C_{12}\right) V^{\prime}+i r k b\left(C_{14}+C_{56}\right) V^{\prime}-\left(C_{11}+k^{2} b^{2}\left(C_{11}-C_{12}\right) / 2\right) V\right] \pi(r)} \\
& \quad+(\delta(r-a)-\delta(r-b))\left[\left(r^{2}\left(C_{11}-C_{12}\right) / 2\right) V^{\prime}-\left(r\left(C_{11}-C_{12}\right) / 2\right) V\right]=-\rho r^{2} \omega^{2} V \pi(r)
\end{aligned}
\tag{5}
$$

$$
\begin{aligned}
& {\left[\left(r^{2}\left(C_{11}-C_{12}\right) / 2\right) W^{*}+\left(i r k b\left(C_{11}-C_{12}\right) / 2\right) U^{\prime}+r\left(C_{11}-C_{12}\right) W^{\prime}+2 i k b C_{11} U\right.} \\
& \left.+\left(\left(C_{12}-C_{11}\right) / 2-k^{2} b^{2} C_{11}\right) W\right] \pi(r)+(\delta(r-a)-\delta(r-b))\left[\left(i r k b\left(C_{11}-C_{12}\right) / 2\right) U\right. \\
& \left.+\left(r^{2}\left(C_{11}-C_{12}\right) / 2\right) W^{\prime}\right]=-\rho r^{2} \omega^{2} W \pi(r)
\end{aligned}
\tag{6}
$$

Enforcing the stress-free boundary conditions on inner and outer surfaces the following equations are obtained for $r=a, r=b$ and $\theta=\pi / 2$.
$$
\begin{aligned}
& i k b C_{12} W-2 C_{12} U+r C_{11} U^{\prime}=0 \\
& -\left(\left(C_{11}-C_{12}\right) / 2\right) V+\left(r\left(C_{11}-C_{12}\right) / 2\right) V^{\prime}=0 \\
& -\left(\left(C_{11}-C_{12}\right) / 2\right) W+\left(i k b\left(C_{11}-C_{12}\right) / 2\right) U+\left(r\left(C_{11}-C_{12}\right) / 2\right) W^{\prime}=0
\end{aligned}
\tag{7}
$$

The prime and double prime indicate the first and second derivatives with respect to the argument $r$ respectively in the above expressions.

By solving the equations using the Legendre orthogonal polynomial series, the corresponding phase velocity dispersion curves in the segmental spherical shell are obtained as shown in Fig. 2(the density is $2800 \mathrm{~kg} / \mathrm{m}^{3}$, the outer radius is $400 \mathrm{~mm}$, and the thickness is $1 \mathrm{~mm}$ ). From Fig. 2, we can see that the dispersion curves at low frequency has the characteristic that the wave travels fast, the

dispersion effects is very weak and the wave is not disturbed easily. Thus, we should choose the low frequency to analyze the wave's propagation law for detecting the defect.

![](./images/813166521831391232_2.jpg)

Fig. 2 Phase velocity dispersion curves

Based on the phase velocity dispersion curves obtained above, the guided waves in the segmental spherical shell could be inspired and received by using the longitudinal wave's mode conversion method. The guided waves inspired and received configuration is shown in Fig. 3.

![](./images/813166521831391232_3.jpg)

Fig. 3 The guided wave's inspiring schematic diagram

According to the analysis of the guided wave's theory, the phase velocity dispersion curves, the guided wave's propagation properties, by choosing the proper inspired and received methods, the specific mode guided wave could be obtained for the detecting.

## Data Processing and Imaging Algorithm

Based on the guided wave's theory above, by using wavelet transformation and ellipse localization algorithm to process the signal, the defect's localization and direction can be imaged clearly. Using db2 wavelet transform, the flaw's edge location can be determined accurately[9, 10].

The testing signals obtained from the specimen were decomposed into 8 layers and filtered using the db2 wavelet. Then, the high frequency signal's envelop (d8) were extracted by using Hilbert envelope signal analyzing technique.

An 8mm×2mm×0.5mm artificial defect was located in front of the polymethyl methacrylate wedge (shown in Fig. 4), the distance (t3) is 100mm, and the total time (t1 plus t2) is$12.53\mu s$ . The signal reflected from the defect, is decomposed, filtered and extracted. The data processing and the results are shown in Fig. 5.

![](./images/813166521831391232_4.jpg)

Fig. 4 The transducers' configuration schematic diagram

![](./images/813166521831391232_5.jpg)

![](./images/813166521831391232_6.jpg)

(a)Defect's reflecting signal
(b)Low frequency approximation signal decomposed
(c)High frequency approximation signal decomposed
(d) Hilbert transformation extracting of the defect reflecting signal

Fig. 5 Defect reflecting signal's data processing and the results

Seen from the decomposed testing signal, we can get the conclusions that: (1) The high frequency signal's Hilbert envelope extracting (shown in Fig. 5(d)), the defect's max reflected amplitude is much higher than the clutter signal; (2) by calculating, the location of high frequency Hilbert envelope curve's maximum is corresponding to the defect's location. Thus, the db2 wavelet and the Hilbert transformation can completely meet the practical defect's locating characteristic parameters detecting demands.

Ellipse Imaging Algorithm. In order to locate and image the defect, the common ellipse algorithm would be used as the transducer array's algorithm. Taking 8 transducers' array as an example, one defect locates in the center of the circular transducers array configured by 8 transducers. The defect, the inspiring transducer (T1) and receiving transducer (T2) are supposed locating at $(x_{0},y_{0}),(x_{1},y_{1})$ and $(x_{2},y_{2})$ separately. The principle of the ellipse algorithm is shown in Fig. 6.

![](./images/813166521831391232_7.jpg)

Fig. 6 The principle of imaging

By making one transducer of the array as the exciting source and the rest transducers as the receiver and doing the same operation in turns, a series of ellipses can be obtained. Superposing all the ellipses in a fixed imaging and threshold filtering the small superposed gray values in a proper ratio, the defect's location and direction will be imaged clearly.

## Experiments

For detecting the defect in the thin segmental spherical shell, a multi-channel ultrasonic testing system has been established in the lab (as shown in Fig. 7). The multi-channel ultrasonic system mainly includes industrial computer, ultrasonic incentive & receiving card, multi-channel digital output card, multi-channel gating switch, and ultrasonic transducer array, protection circuit and so on.

![](./images/813166521831391232_8.jpg)

Fig. 7 The multi-channel ultrasonic testing system

An thin segmental spherical shell specimen(radius radius of curvature is 400mm, thickness is 1mm) and an array of 8 guided wave transducers (center frequency is 1MHz) with wedges are introduced. These transducers are arranged in a circle with the diameter of 400mm and mounted on the specimen. The experimental transducer array's configuration is shown in Fig. 8.

The 10mm×0.5mm×0.5mm defect's detecting images at different threshold is shown in fig. 9. The $\phi2mm$ circular aperture's detecting images at different threshold is shown in Fig. 10.

![](./images/813166521831391232_9.jpg)

Fig. 8 The experimental transducer array's configuration

![](./images/813166521831391232_10.jpg)

(a)threshold 0 (b) threshold 40

Fig. 9 10mm×0.5mm×0.5mm flaw's images

![](./images/813166521831391232_11.jpg)

(a) threshold 0 (b) threshold 40

Fig. 10 $\phi2mm$ circular aperture's images

## Conclusion

By analyzing the experimental results, we concluded that: (1) the multi-channel ultrasonic testing system has a high detecting precision in localization and direction identification, but has a large detection error in size detecting; (2) Due to the circular aperture's reflecting energy which is caused by the small reflecting surface is relatively low, the detection precision becomes low; (3) a further study is needed to improve the small defects detecting ability.

However there was only one artificial defect in the specimen, and further experiments are needed to research a specimen with two or more defects.

## Acknowledgment

This work is supported by the National Pre-research Foundation. The corresponding author is Prof. Chunguang Xu.

## References

[1] Chunguang Xu, Joseph L Rose, Xiang Zhao. Detection Principle of Shape and Orientation of Corrosive Defects Using Lamb Waves[J].Journal of Robotics and Mechatronica, Vol.21, No.5,2008:568-573.

[2] R.Raisutis, R.Kazys, L.Mazeika, R.Sliteris. Application of the ultrasonic transmission tomography for inspection of the petroleum tank floor. Ultragarsas, Vol.62, No.3, 2007:26-31.

[3] Xiang Zhao, Roger L Royer, Steven E Owens and Joseph L rose. Ultrasonic lamb wave tomography in structural health monitoring. Smart Materials and Structures,20(2011) 105002.

[4] K. Edalati, A. Kermani, B. Naderi and B. Panahi,"Defects Evaluation in Lamb Wave Testing of Thin Plates" www.ndt.net-3rd MENDT-Middle East Nondestructive Testing Conference & Exhibition , 27-30 Nov., 2005 Bahrain, Manama.

[5] Kargl, S.G., Marston, P.L., 1990. Ray synthesis of lamb wave contributions to the total scattering cross section for an elastic spherical shell. Journal of the Acoustical Society of America 88, 1103-1113.

[6] Wang, X., Lu, G., Guillow, S.R., 2002. Stress wave propagation in orthotropic laminated thick-walled spherical shells. International Journal of Solids and Structures 39, 4027-4037.

[7] Towfighi, S., Kundu, T., 2003. Elastic wave propagation in anisotropic spherical curved plates. International Journal of Solids and Structures 40, 5495-5510.

[8] Xianfeng Fan, Ming J. Zuo, Xiaodong Wang. Identification of weak ultrasonic signals in testing of metallic materials using wavelet transform. Smart Mater. Struct., 15 (6) (2006), pp. 1531-1539

[9] Elisabetta Pistone, Abdollah Bagheri, Kaiyuan Li. Piervincenzo Rizzo. Signal processing for the inspection of immersed structures. Health Monitoring of Structural and Biological Systems 2013, Proc. SPIE 8695, 86951A .

[10] Abdollah Bagheri, Kaiyuan Li, Piervincenzo Rizzo. Reference-free damage detection by means of wavelet transform and empirical mode decomposition applied to Lamb waves. Journal of Intelligent Material Systems and Structures, January 2013, vol. 24 (2). pp:194-208.

Frontiers of Manufacturing and Design Science IV
10.4028/www.scientific.net/AMM.496-500

Defect Detection of the Segmental Spherical Shell Based on Ultrasonic Transducer Array
10.4028/www.scientific.net/AMM.496-500.1298