# Nanophotonic Computational Design

Jesse Lu* and Jelena Vučković
Stanford University, Stanford, California, USA.
jesselu@stanford.edu

**Abstract:** In contrast to designing nanophotonic devices by tuning a handful of device parameters, we have developed a computational method which utilizes the full parameter space to design linear nanophotonic devices. We show that our method may indeed be capable of designing any linear nanophotonic device by demonstrating designed structures which are fully three-dimensional and multi-modal, exhibit novel functionality, have very compact footprints, exhibit high efficiency, and are manufacturable. In addition, we also demonstrate the ability to produce structures which are strongly robust to wavelength and temperature shift, as well as fabrication error. Critically, we show that our method does not require the user to be a nanophotonic expert or to perform any manual tuning. Instead, we are able to design devices solely based on the user's desired performance specification for the device.

© 2018 Optical Society of America

OCIS codes: 230.75370, 130.3990.

---

## References and links
1. J. Lu, J. Vuckovic, "Objective-first design of high-efficiency, small-footprint couplers between arbitrary nanophotonic waveguide modes," Opt. Express **20**, 7221-7236 (2012)
2. S. Boyd, N. Parikh, E. Chu, B. Peleato, and J. Eckstein, "Distributed Optimization and Statistical Learning via the Alternating Direction Method of Multipliers," Foundations and Trends in Machine Learning **3**, 1-122 (2011).
3. W. Shin and S. Fan, "Choice of the perfectly matched layer boundary condition for frequency-domain Maxwells equations solvers," J. of Comp. Phys **231**, 3406-3431 (2012).
4. S. Osher and R. Fedkiw, *Level Set Methods and Dynamic Implicit Surfaces: 1st Edition* (Springer, 2002).
5. Y. Jiao, S. Fan, and D. A. B. Miller, "Demonstrations of systematic photonic crystal design and optimization by low rank adjustment: an extremely compact mode separator", Opt. Lett. **30**, 140-142 (2005).
6. F. Van Laere, G. Roelkens, M. Ayre, J. Schrauwen, D. Taillaert, D. Van Thourhout, T. F. Krauss, and R. Baets, "Compact and highly efficient grating couplers between optical fiber and nanophotonic waveguides," J. of Lightwave Tech. **25**, 151-156 (2007).

---

## 1. Introduction
Currently, almost all nanophotonic components are designed by hand-tuning a small number of parameters (e.g. waveguide widths and gaps, hole and ring sizes). However, the realization of increasingly complex, dense, and robust on-chip optical networks will require utilizing increasing numbers of parameters when designing nanophotonic components.

Opening the design space to include many more parameters allows for smaller footprint, higher performance devices by definition, since original designs are still included in this parameter space. Unfortunately, the lack of intuition for what such designs might look like and the inability to manually search such a large parameter space have greatly hindered the ability to achieve this.

For this reason, we have developed and implemented a computational method which is able to use the full parameter space to design linear nanophotonic components in three dimensions. Critically, our method requires no user intervention or manual tuning. Instead, a design-by-specification scheme is used to produce designs based solely on a user's performance specification.

We show that our method can indeed produce designs which are extremely compact, and, at the same time, highly efficient. Furthermore, we demonstrate that devices with novel functionality are easily designed. We also show that our method can be used to produce designs with extreme robustness to wavelength and temperature shift, as well as fabrication error.

Lastly, all our results are produced by simply specifying the functionality and performance of the desired device, which suggests that our method may indeed by able to design all linear nanophotonic devices.

2. Problem formulation

In order to produce designs which utilize the full parameter space, and are based solely on the user's performance specification, we formulate the design problem in the following way:

$$
\operatorname{minimize} \quad \sum_{i}^{M}\left\|A_{i}(z) x_{i}-b_{i}\right\|^{2} \tag{1a}
$$

$$
\text { subject to } \quad \alpha_{i j} \leq\left|c_{i j}^{\dagger} x_{i}\right| \leq \beta_{i j}, \quad \text { for } i=1, \ldots, M \text { and } j=1, \ldots, N_{i} \tag{1b}
$$

$$
z_{\min } \leq z \leq z_{\max } \tag{1c}
$$

The explanation for the various terms in eq. (1) follows:

1. $A_i(z)x_i - b_i$ is the physics residual for the $i$th mode. That is to say, $A_i(z)x_i - b_i$ represents the underlying physics of the problem; namely, the electromagnetic wave equation $(\nabla \times \mu_{0}^{-1} \nabla \times-\omega_{i}^{2} \varepsilon) E_{i}+i \omega_{i} J_{i}$.

The specific substitutions used in order to transform

$$
(\nabla \times \mu_{0}^{-1} \nabla \times-\omega_{i}^{2} \varepsilon) E_{i}+i \omega_{i} J_{i} \quad \longrightarrow \quad A_{i}(z) x_{i}-b_{i}
$$

are
- $E_i \to x_i$,
- $\varepsilon \to z$,
- $\nabla \times \mu_{0}^{-1} \nabla \times-\omega_{i}^{2} \varepsilon \to A_{i}(z)$, and
- $-i \omega_{i} J_{i} \to b_{i}$.

In contrast to typical schemes for optimizing physical structures, our formulation actually allows for non-zero physics residuals; which can be deduced since $A_i(z)x_i - b_i=0$ is not a hard constraint. Instead, this formulation is what we call an objective-first [1] formulation in that the design objective (explained below) is prioritized above satisfying physics.

2. The (field) design objective consist of the constraint $\alpha_{i j} \leq\left|c_{i j}^{\dagger} x_{i}\right| \leq \beta_{i j}$. Physically, this constraint describes the performance specification of the device via a series of field overlap integrals at various output ports of the device. Specifically, the $c_{i j}^{\dagger} x_{i}$ terms represents an overlap integral between the E-field of the $i$th mode $(x_i)$ with an E-field of the user's choice $(c_{i j})$, where the additional subscript $j$ allows the user to include multiple such fields. The amplitude of the overlap integral is then forced to reside between $\alpha_{i j}$ and $\beta_{i j}$.

This mechanism allows the user to express the desired performance of the device as a combination of field amplitudes in various output field patterns. These outputs would be in response to a predefined input excitation, which is determined by the current excitation $b_i(-i\omega_i J_i)$ in the physics residual of each mode.

As an example of a design objective for some mode 1 a user might choose to have the majority of the output power reside in some output pattern 1, while ensuring that only a small amount of power be transferred to some output pattern 2. In this case the user would use $0.9 \leq |c_{11}^{\dagger} x_1| \leq 1.0$ for the former. and then $0.0 \leq |c_{12}^{\dagger} x_1| \leq 0.01$ for the latter; where $c_{11}$ and $c_{12}$ are representative of output patterns 1 and 2 respectively.

Finally, we note again that the design objective in our formulation is actually a hard constraint. This means that it is always satisfied, even to the extent of allowing for an unphysical field (since the physics residual will not be exactly 0). It is for this reason that we call such a formulation "objective-first".

3. The final term in eq. (1), $z_{\text{min}} \leq z \leq z_{\text{max}}$, is the structure design objective. It is used as a relaxation of the binary constraint, $z \in \{z_{\text{min}}, z_{\text{max}}\}$, which would ensure that the final design be composed of two discrete materials.

### 3. Method of solution
We employed the alternating directions method of multipliers (ADMM) algorithm [2] in order to solve eq. (1). The ADMM algorithm solves eq. (1) by iteratively solving for $x_i$, $z$, and a dual variable $u_i$.

Since we are working in three dimensions, solving eq. (1) for $x_i$ is non-trivial in that it involves millions of variables and requires solving for the ill-conditioned $A_i(z)$ matrix. For this reason, we use a home-built finite-difference frequency-domain (FDFD) solver which implements a hardware-accelerated iterative solver[3] on Amazon's Elastic Compute Cloud. Critically, our cloud-based solver allows us to scale to solve problems with arbitrarily-large number of modes, with no significant penalty in runtime.

In contrast to solving for $x_i$, solving for $z$ is much simpler since we only consider planar structures; thereby limiting $z$ to have only thousands of variables.

Lastly, in order to arrive at fully discrete, manufacturable structures, we convert $z$ to a boundary parameterization[4] and tune our structure using a steepest-descent method.

### 4. Results
We demonstrate the effectiveness of our design method by producing designs for a variety of nanophotonic devices.

All of our results are in three dimensions and are planar structures, consisting of a 250 nm etched silicon slab completely surrounded by silica. The permittivity values of silicon and silica used were $\varepsilon_{\text{Si}} = 12.25$ and $\varepsilon_{\text{SiO}_2} = 2.25$ respectively.

Many, if not all, of the produced designs exhibit novel functionality, high efficiency, and very compact footprints of only a few square vacuum wavelengths, while still remaining manufacturable. We also show that many devices can be designed to exhibit different functionality for different input excitations. Additionally, we show that devices can be designed with large tolerances for errors in wavelength, temperature and fabrication.

### 4.1. Mode converters
Our first devices consisted of waveguide mode converters. Such devices are simple in that they are single-input, single-output devices. At the same time, such a device is significant because

it demonstrates the feasibility of multi-mode on-chip optical networks by showing that high-efficiency mode conversion can readily be achieved in planar on-chip nanophotonic structures.

We show, through the design of mode converters for both the TE- and TM-polarized waveguide modes, that our method is indeed fully three-dimensional. Additionally, the devices also demonstrate very small device footprints (1.6 × 2.4 microns for this device in particular operating at 1550 nm wavelength).

#### 4.1.1. TE mode converter

Our first result is a mode conversion device operating in the TE polarization, where the primary E-field component of the waveguide mode is polarized in the plane of the structure.

Our performance specification (fig. 1) for the device was for $\geq 90\%$ of the input power to be transferred from the fundamental waveguide mode, to the second-order waveguide mode. At the same time, we specified that no more than 1% of the input power was to remain in the transmitted fundamental mode.

![](./images/867767938139030007_1.jpg)

Fig. 1. Perfomance specification of the TE mode converter. Input mode is the fundamental TE-polarized mode on the left. Primary output mode is the second-order mode on the right. Output power in the transmitted fundamental mode should be no more than 1%. The structure shown is the final three-dimensional design (the same holds for all the following figures in the article).

The performance of the device is shown in fig. 2. The conversion efficiency into the second-order mode is lower than desired (86.4%). Imperfect conversion may be due to evanescent modes "interfering" with the output field overlap calculation.

![](./images/867767938139030007_2.jpg)

Fig. 2. Structure and E-field at the central plane of the TE mode converter. The conversion efficiency into the second-order mode is 86.4%, while the power into the rejection mode (fundamental) is 0.7%. Device footprint is 1.6 × 2.4 microns. Operating wavelength is 1550 nm.

### 4.1.2. TM mode converter

In addition to mode conversion in the TE polarization (E-field in-plane), we show that TM po- larization (E-field out-of-plane) mode converters can be designed as well. This example shows that full three-dimensional structures truly are possible, and that no approximations are needed for our method.

Since our method is design-by-specification, the design of a TM mode converter requires only a small modification to the performance specification of the device; namely the polariza- tion of the input and output modes (fig. 3). Specifically, we still design for $\geq 90\%$ conversion into the second-order mode and a $\leq 1\%$ allowance for the fundamental mode to be transmitted.

![](./images/867767938139030007_3.jpg)

Fig. 3. Perfomance specification of the TM mode converter. Input mode is the fundamental TM-polarized mode on the left. Primary output mode is the second-order mode on the right. Output power in the transmitted fundamental mode on the right above $1\%$ is to be rejected. The structure shown is the final three-dimensional design.

The performance of the device is shown in fig. 4. The lower conversion efficiency of $76.9\%$ in contrast to the TE mode converter may be attributed to the lower confinement of the TM waveguide modes in such thin slabs. However, good rejection of only $1\%$ is still achieved.

![](./images/867767938139030007_4.jpg)

Fig. 4. Structure and E-field at the central plane of the TM mode converter. The conversion efficiency into the second-order mode is $76.9\%$, while the power into the rejection mode (fundamental) is $1.0\%$. Device footprint is $1.6\times 2.4$ microns.

### 4.2. Mode splitters

Next, we demonstrate the design of nanophotonic waveguide mode splitters. Such devices can be used as multiplexers or demultiplexers and are the key component in utilizing a single waveg- uide to transmit multiple optical signals.

As a demonstration of the versatility of our method, we show that it is capable of designing mode splitting devices based on either the spatial profile, the polarization, or the wavelength of the input modes.

The performance specification for each device is simply to convert more than 90% of the input power in a particular input mode into either one of the output modes. At the same time, we specify that the transmission into the other output mode be kept below 1% of input power.

### 4.2.1. Spatial mode splitter
We demonstrate what is, to our knowledge, the first design for a three-dimensional nanophotonic spatial mode splitter (previous designs were restricted to two dimensions [5]). Such a device is the key enabler for multi-mode on-chip optical circuits, and we show here that they can be designed to be highly efficient while utilizing a very small device footprint (2.8 × 2.8 microns). The performance specification is shown in fig. 5, and the final results is shown in fig. 6.

![](./images/867767938139030007_5.jpg)

Fig. 5. Spatial mode splitter performance specification. Input mode is either the fundamental or second-order TE-polarized mode on the left. Output modes are the fundamental waveguide modes of either output waveguide on the right. Output power into the desired output arm is specified to be greater than 90%, while power into the opposing arm is set to below 1%.

### 4.2.2. TE/TM splitter
In addition to splitting different spatial modes, we show that different polarizations can also be split. Fig. 7 shows the performance specification of a device which is able to separate fundamental TE-polarized ($E_y$ dominant) and TM-polarized ($E_z$ dominant) waveguide modes into separate arms. The final, verified result is shown in fig. 8.

Not only is this result the first of its kind, it is the first in the device category where a single device is able to control both polarizations within the same device footprint. This shows the versatility and broad applicability of our method.

### 4.2.3. Wavelength splitter
Traditional wavelength splitting devices can also be designed using our method. Here, we show that the 1550 nm and 1310 nm wavelengths can be split in a very small device footprint (2.8 × 2.8 microns). The performance specification is shown in fig. 9, and the final result is shown in fig. 10.

![](./images/867767938139030007_6.jpg)

Fig. 6. Spatial mode splitter final result. The conversion efficiencies into the upper and lower output arms are 88.7% and 77.4% respectively, while the rejection powers for the same modes are 0.27% and 0.20%. Device footprint is $2.8 \times 2.8$ microns.

![](./images/867767938139030007_7.jpg)

Fig. 7. TE/TM splitter performance specification. Input mode is either the fundamental TE-polarized ($E_y$ dominant, top left) and TM-polarized ($E_z$ dominant, top right). Output power into the desired output arm is specified to be greater than 90%, while power into the opposing arm is set to below 1%.

### 4.3. Hubs
We continue to demonstrate the capabilities of our method by designing multi-input, multi-output devices which we call hubs. Such devices essentially re-arrange modes in the waveguides, and may be thought of as general cross-connect structures. Critically, the successful design of such structures shows that efficiently routing overlapping signals can be accomplished in a single layer for nanophotonic circuits.

#### 4.3.1. 3×3 hub
We first design a hub with three inputs and outputs. The performance specification is shown in fig. 11, and the final result is shown in fig. 12.

#### 4.3.2. 4×4 hub
We extend our previous result to design a hub with four inputs and outputs. The performance specification is shown in fig. 13, and the final result is shown in fig. 14.

![](./images/867767938139030007_8.jpg)

Fig. 8. TE/TM splitter final result. The conversion efficiencies into the upper and lower output arms are 87.6% and 88.8% respectively, while the rejection powers for the same modes are 1.06% and 0.58%. Device footprint is 2.8 × 2.8 microns.

![](./images/867767938139030007_9.jpg)

Fig. 9. Wavelength splitter performance specification. Input mode is the fundamental TE-polarized mode on the left at a wavelength of either 1550 nm or 1330 nm. Output modes are the fundamental waveguide modes of either output waveguide on the right; however, the 1550 nm wavelength is directed into the top output, while the 1310 nm wavelength is directed into the bottom output. Output power into the desired output arm is specified to be greater than 90%, while power into the opposing arm is set to below 1%.

### 4.3.3. 2×2×2 hub
We can now design a hub that performs different switching functions for different wavelengths. Specifically, we use two input waveguides, two output waveguides, and two wavelengths (hence the name 2×2×2).

Our performance specification (fig. 15) is to cross-couple the waveguides at the 1310 nm wavelength, but to uncouple the waveguides at the 1550 nm wavelength. The final result is shown in fig. 16.

### 4.4. Fiber couplers
The capabilities of our method are further demonstrated in the design of nanophotonic fiber couplers, which couple light from an optical fiber at normal incidence into an in-plane waveguide[6].

The structure of the optical fibers used was a 2 micron diameter core with refractive index $n_{\text{core}} = 1.6$, surrounded by a cladding with refractive index $n_{\text{cladding}} = 1.5$. The reduced size

![](./images/867767938139030007_10.jpg)

Fig. 10. Wavelength splitter final result. The conversion efficiencies into the upper and lower output arms are 83.2% and 78.7% respectively, while the rejection powers for the same modes are 0.49% and 1.66%. Device footprint is 2.8 × 2.8 microns.

![](./images/867767938139030007_11.jpg)

Fig. 11. 3×3 hub performance specification. Input and output modes all consist of the fundamental TE-polarized mode. Output power into the desired output arm is specified to be greater than 90%, no rejection modes are used for computational efficiency. This hub directs input power from input ports 1, 2, and 3 (from top to bottom) into output ports 2, 3, and 1 respectively.

of the fiber core was employed in order to keep the device footprint small. Additionally, the fiber coupler devices were only etched to half the membrane depth, in order to increase the asymmetry in the device structure.

### 4.4.1. Compact fiber coupler

We first present the design of a compact fiber coupler. Such a device is said to be compact in that the functions of coupling into the plane, and focusing into a narrow waveguide are overlapped in the same device footprint.

Although the performance specification (fig. 17) desired a coupling efficiency above 90%, only 51.5% efficiency was achieved (fig. 18); however, this likely remains the highest efficiency demonstrated in a compact fiber coupler.

### 4.4.2. Mode-splitting fiber coupler

We now continue to show how different functionalities can be incorporated into a single device, by virtue of our design-by-specification scheme.

Here, we show how the functionality of a fiber coupler can be combined with that of a spatial

![](./images/867767938139030007_12.jpg)

Fig. 12. 3×3 hub final result. The conversion efficiencies into the selected output arms are 88.6%, 90.6%, and 87.3% for input arms 1, 2, and 3 respectively (top to bottom).

![](./images/867767938139030007_13.jpg)

Fig. 13. 4×4 hub performance specification. Input and output modes all consist of the fundamental TE-polarized mode. Output power into the desired output arm is specified to be greater than 90%, no rejection modes are used for computational efficiency. This hub directs input power from input ports 1, 2, 3, and 4 into output ports 3, 2, 4, and 1 respectively.

mode splitter. Specifically, the performance specification (fig. 19) determines that different fiber spatial modes by split into different in-plane nanophotonic waveguides.

The final result (fig. 20) has lower efficiencies; however, the result is still useful in that no device with such a functionality has previously been demonstrated.

### 4.4.3. Wavelength-splitting fiber coupler
Another example of a functionality-combining device is the wavelength-splitting fiber coupler. Here, fiber modes of different wavelengths are coupled in-plane and then split into different nanophotonic waveguides (fig. 21). Once again, efficiencies are low (fig. 22), but no such device has previously been demonstrated.

### 4.5. Broadband wavelength splitter
We continue to investigate the capabilites of our method by attempting the design of a broadband wavelength splitter.

![](./images/867767938139030007_14.jpg)

Fig. 14. 4×4 hub final result. The conversion efficiencies into the selected output arms are 85.9%, 88.1%, 85.4%, and 84.3% for input arms 1, 2, 3, and 4 respectively (top to bottom).

First, we revisit our wavelength splitter result (fig. 10) and perform a broadband analysis, the results of which are shown in fig. 23. This analysis reveals that device performance quickly drops off as one moves away from the target wavelengths.

In order to design a broadband wavelength splitter, we modify our performance specification to include multiple target wavelengths (with identical desired performance) around the original target wavelengths, as seen in fig. 24 which reveals that broadband operation has been achieved. The final result for the broadband wavelength splitter is shown in fig. 25.

#### 4.5.1. Temperature-robustness of broadband wavelength splitter

We can now perform a temperature analysis of our broadband wavelength splitter, using $\Delta n_{\text{Si}}/\Delta T = 1.85 \cdot 10^{-4} K^{-1}$ and $\Delta n_{\text{SiO}_2}/\Delta T = 0$ (no refractive index shift for silica). This analysis, shown in fig. 26, reveals that stable operating points exist over a temperature range of

![](./images/867767938139030007_15.jpg)

Fig. 15. 2×2×2 hub performance specification. Input and output modes all consist of the fundamental TE-polarized mode at either 1550 nm or 1310 nm wavelengths. Output power into the desired output arm is specified to be greater than 80%, no rejection modes are used for computational efficiency. This hub directs input arms 1 and 2 into output arms 1 and 2 at 1550 nm, but swaps them at 1310 nm.

![](./images/867767938139030007_16.jpg)

Fig. 16. 2×2×2 hub final result. The conversion efficiencies at the 1550 nm wavelength are 77.6% and 73.7% respectively for the top and bottom inputs. At 1310 nm, the respective efficiencies are 75.7% and 75.2%.

![](./images/867767938139030007_17.jpg)

Fig. 17. Compact fiber coupler performance specification. Input mode consists of the $E_y$-polarized fundamental fiber mode. Output mode is the fundamental TE-polarized mode of the in-plane waveguide. Output power into the desired output arm is specified to be greater than 90%.

nearly 1000 K. Such a result is telling in that it demonstrates that on-chip optical devices can be designed to be passively stable to temperature shifts which would typically be present in CPUs, since these are much less than 1000 K.

![](./images/867767938139030007_18.jpg)

Fig. 18. Compact fiber coupler final result. The conversion efficiency into the in-plane waveguide mode is 51.5%.

![](./images/867767938139030007_19.jpg)

Fig. 19. Mode-splitting fiber coupler performance specification. Input mode consists of the fundamental fiber mode or the third-order, circularly polarized fiber mode. Output mode is the fundamental TE-polarized mode of either in-plane waveguide. The device is designed to couple the fundamental fiber mode into the upper output arm, while the third-order fiber mode is coupled into the lower output arm. Output power into the desired output arm is specified to be greater than 90%.

### 4.5.2. Fabrication-robustness of broadband wavelength splitter

A analysis with regard to fabrication-error was also performed on the broadband wavelength splitter. The specific fabrication error was a general over- or under-etch of the device (input and output waveguides unaffected). Fig. 27 reveals that up to 8 nm of over- or under-etching can be sustained before performance falls below 70%, at the central operating wavelengths. The structural variations at 8 nm of etch error are shown in fig. 28.

This result is significant in that it demonstrates that the design of broadband devices seems to be a valid heuristic in the search for devices which are tolerant to temperature shifts and fabrication error. Note, however, that our method, as formulated, is also able to deal with temperature and fabrication shifts explicitly as well, although such results are not demonstrated here.

## 5. Conclusion

We have developed and implemented a method to design linear nanophotonic structures which are fully three-dimensional and multi-modal, have very compact footprints, exhibit high efficiency, and are manufacturable. We demonstrate this capability by designing various nanophoto-

![](./images/867767938139030007_20.jpg)

Fig. 20. Mode-splitting fiber coupler final result. The conversion efficiency for the fundamental fiber mode input is 32.6% (top plot). The conversion efficiency for the third-order fiber mode input is 22.7% (bottom plot).

![](./images/867767938139030007_21.jpg)

Fig. 21. Wavelength-splitting fiber coupler performance specification. Input mode consists of the $E_y$-polarized fundamental fiber mode at either the 1310 nm or 1550 nm wavelengths. Output mode is the fundamental TE-polarized mode of either in-plane waveguide. The structure is designed to guide light at the 1550 nm wavelength into the upper output arm, while 1310 nm light is guided into the lower output arm. Output power into the desired output arm is specified to be greater than 90%.

tonic mode converters, splitters, hubs, and fiber couplers. Critically, many, if not all, of these devices have never been demonstrated before and cannot be designed by hand. In contrast, our method allows user to easily design such devices by virtue of our design-by-specification scheme.

In addition, we demonstrate the design of a broadband device which is strongly robust to wavelength and temperature shift, as well as fabrication error. We show that such a device has stable operating wavelengths over temperature shifts as large as 905 K, or over-/under-etching error of up to 8 nm. We suggest, based on this design, that wavelength tolerance may be a good heuristic to the design of temperature and fabrication-error tolerant nanophotonic devices.

This work has been supported by the AFOSR MURI for Complex and Robust On-chip Nanophotonics (Dr. Gernot Pomrenke), grant number FA9550-09-1-0704.

![](./images/867767938139030007_22.jpg)

Fig. 22. Wavelength-splitting fiber coupler final result. The conversion efficiency into the in-plane waveguide mode at 1550 nm is 31.6%. The conversion efficiency into the in-plane waveguide mode at 1310 nm is 28.6%.

![](./images/867767938139030007_23.jpg)

Fig. 23. Broadband analysis of previously design wavelength splitter (fig. 10). Although high-efficiency operation is achieved, the performance quickly drops off away from the target wavelengths (denoted by arrows).

![](./images/867767938139030007_24.jpg)

Fig. 24. Broadband analysis of broadband wavelength splitter (final design shown in fig. 25. The addition of multiple target wavelengths (vertical arrows) allows for high-efficiency operation is achieved across a wide bandwidth.

![](./images/867767938139030007_25.jpg)

Fig. 25. Broadband wavelength splitter final result. The efficiencies at the central target wavelengths of 1550 nm and 1310 nm exceed those of its narrowband counterpart (fig. 10).

![](./images/867767938139030007_26.jpg)

Fig. 26. Temperature analysis of the broadband wavelength splitter. Stable operating points (defined as efficiency $\geq 80\%$) exist over a temperature shift of 905K.

![](./images/867767938139030007_27.jpg)

Fig. 27. Analysis of fabrication-error on the performance of the broadband wavelength splitter. Original central wavelengths are shown to hold greater than 70% efficiency, in spite of up to 8 nm of over- or under-etch error.

![](./images/867767938139030007_28.jpg)

Fig. 28. Comparison of under-etched, as-designed, and over-etched structures. Differences are subtle since the pixel size is 40 nm and the fabrication error is 8 nm.