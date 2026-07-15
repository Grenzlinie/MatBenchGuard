# SS_MC: A Monte Carlo Program For Modeling X-ray Generation

P.R. Miller*, J. Sheffield-Parker**

* CSIRO Manufacturing and Infrastructure Technology, PB 33, Clayton South, VIC 3169, Australia
** XRT Limited, Suite A.3.1, 63 Turner Street, Port Melbourne, VIC 3207, Australia

The X-ray ultraMicroscope (XuM) is an SEM-based projection X-ray microscope that allows X-ray images to be recorded with resolution better than 100 nm [1-3]. The projection method for X-ray microscopy is very simple in principle: X-rays from the source pass through the sample to form a projected image at the detector and magnification is varied by moving the sample between the source and the detector. XuM images exploit both absorption contrast and phase contrast to reveal fine internal structure and edge detail.

A sub-micron X-ray source is obtained from the interaction of the electron beam with a metal target. The target is typically an inclined bulk target or a thin foil target viewed edge-on using a direct-detection CCD X-ray camera.

One factor limiting XuM resolution is the volume of X-ray generation within the target. The recorded X-ray image is equivalent to the image from an ideal point source convoluted with the X-ray source distribution as viewed from the detector (for magnification >>1) and taking into account X-ray absorption within the target and sample and detector efficiency. In principle, image resolution can be improved by deconvolution if the X-ray source distribution is known. With the imaging geometry used here the X-ray source distribution is asymmetric in shape and as a result image features may be distorted. Compare for example Fig. 1, which shows vias in an integrated circuit recorded using 30 keV electrons and a bulk Pt target inclined at $45^\circ$, with Fig. 3 where a 50 nm thick Pt foil target viewed edge-on was used. In Fig. 3 the bright fringe surrounding each via is due to Fresnel diffraction and resolution is not limited by the X-ray source size; fringe width is ~120 nm. In Fig. 1 a faint, dark horizontal band can be seen running through the top of each via and the Fresnel fringe is not visible there. Image degradation in Fig. 1 is due to the larger, asymmetric X-ray source distribution of the bulk target compared to that of the 50 nm thin foil target.

The Monte Carlo approach is a standard method for modeling the interaction of high energy electrons within a material and for simulating the production of various electron, X-ray and other signals. The program SS_MC uses the single-scattering Monte Carlo method [4] to model the production of characteristic and bremsstrahlung X-rays. Pre-calculated arrays are used to speed up the calculation; these arrays can be graphed. SS_MC allows for up to four target layers containing a total of four elements with arbitrary electron beam direction and position and arbitrary detector position. The calculation tracks K, L, M and bremsstrahlung (60 energies) X-ray generation and electron energy loss and accounts for absorption within the target and sample and for detector efficiency. These data are projected onto a plane normal to the beam origin/detector direction centered on the beam position (401x401 element arrays). Individual or combined arrays can be

graphed as a surface plot or as various line profiles with or without absorption corrections allowing the distribution of the various X-ray types within the target to be studied in detail. The modeled X-ray source distribution can be written to file for use in image deconvolution. X-ray generation data as a function of depth (100 slices) are also stored and can be used to simulate X-ray spectra.

The X-ray source distribution for the bulk Pt target was calculated using SS_MC assuming a point electron source and ideal detector point spread function, see inset in Fig. 1 (x8 scale compared to the images). Note that the X-ray source distribution is sharp at the bottom and sides but has a broad fan at the top (contrast has been adjusted significantly to show this broad fan). It is this broad fan that degrades the upper side of image features in Fig. 1. Fig. 2 shows the result of deconvolution using the model source distribution. It can be seen that deconvolution has removed the dark band and has restored the Fresnel fringe all the way around the vias; this significantly aides image interpretation. Image resolution after deconvolution is better than 200 nm. Deconvolution allows thicker targets to be used while maintaining resolution giving higher X-ray intensity which in turn allows shorter acquisition time. Deconvoluted images are subsequently processed using phase retrieval methods.

The Monte Carlo program SS_MC will be described and results of image deconvolution using model X-ray source distributions will be presented.

![](./images/812046614888710145_1.jpg)

Fig. 1: vias imaged using bulk Pt target and 30 keV electrons with inset showing model X-ray source distribution (x8 scale); Fig. 2: Fig. 1 after deconvolution; Fig. 3: vias using 50 nm thin foil Pt target and 30 keV electrons (different area to Fig. 1). Image width is 4 $\mu$m (10 nm/pixel).

References

[1] V.E. Cosslett and W.C. Nixon, J. App. Physics V24 Number 5, pp 616-623 (1953)
[2] S.C Mayo, P.R. Miller, S.W. Wilkins, T.J. Davis, D. Gao, T.E. Gureyev, D. Paganin, D., D.J. Parry, A. Pogany, and A.W. Stevenson, J. Micros., 207, pp 79-96 (2002).
[3] S.C. Mayo, T.J. Davis, T.E. Gureyev, P.R. Miller, D. Paganin, A. Pogany, A.W. Stevenson, S.W. Wilkins, Optics Express, 11, pp 2289-2302 (2003)
[4] D.C. Joy, Monte Carlo Modeling for Electron Microscopy and Microanalysis, Oxford University Press, Oxford, 1995