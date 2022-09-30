# FingerPrint

DISCLAIMER: This project is still under development and will be updated as we move forward.

## Libraries used

1) OpenCV
2) Skimage
3) numpy
4) math
5) fingerprint_enhancer ([Utkarsh Deshmukh GitHub](https://github.com/Utkarsh-Deshmukh/Fingerprint-Enhancement-Python) [pip](https://pypi.org/project/fingerprint-enhancer/#description)) 

## References

1) Darrin. “The History & Evolution of Fingerprint Identification: NAI.” North American Investigations,  26 November, 2013, pvteyes.com/history-evolution-fingerprint-identification/.
2) Hsu, David S. “Fingerprint Sensor Technology And Security Requirements.” Semiconductor Engineering, 4 Nov. 2016, semiengineering.com/fingerprint-senor-technology-and-security-requirements/.
3) Peralta, Daniel, et al. “A Survey on Fingerprint Minutiae-Based Local Matching for Verification and Identification: Taxonomy and Experimental Evaluation.” Information Sciences, Elsevier, 16 Apr. 2015, www.sciencedirect.com/science/article/abs/pii/S0020025515002819.
4) Galar, Mikel, et al. “A Survey of Fingerprint Classification Part I: Taxonomies on Feature Extraction Methods and Learning Models.” Knowledge-Based Systems, Elsevier, 14 Feb. 2015, www.sciencedirect.com/science/article/abs/pii/S0950705115000519.
5) Deshmukh, Utkarsh. “Utkarsh-Deshmukh/Fingerprint-Enhancement-Python.” GitHub, github.com/Utkarsh-Deshmukh/Fingerprint-Enhancement-Python. 
6) Deshmukh, Utkarsh. “Utkarsh-Deshmukh/Fingerprint-Feature-Extraction.” GitHub, github.com/Utkarsh-Deshmukh/Fingerprint-Feature-Extraction.
7) Maponi, Pierluigi, et al. “Fingerprint Orientation Refinement Through Iterative Smoothing”, University of Camerino, October 2017
8) Patriciu, Victor-Valeriu & Spinu, Stelian. (2014). Fingerprint Ridge Frequency Estimation in the Fourier Domain. Advances in Electrical and Computer Engineering. 14. 95-98. 10.4316/AECE.2014.04014. 

## Project Slides

#### Presentation 1

[Project Review 1](https://docs.google.com/presentation/d/1JLqQ4dnO17-Fnf1hG567qRmSjrDhH3WsVML35hbRDLc/edit?usp=sharing)

#### Presentation 2

[Project Review 2](https://docs.google.com/presentation/d/1xDIpBhkaqAJBUuhaYUs8L2o7UGmb6AX_mjy7ydxyoSI/edit?usp=sharing)

## Getting started

Please make sure to do `pip install -r requirements.txt` to install all the required dependencies for the project to execute.

### Images Path

Make sure to store all UNENHANCED images in the directory `Unenhanced Images`. Enhanced Images will be stored in `Images` directory.

### Steps to get Enhanced Image

NOTE: Currently on jpg format is supported. Make sure the images stored in `Unenhanced Images` directory is in jpg format.

From your respective terminal run the command `python Enhance_image.py <image name>`. This should process your image and store it in the `Images` directory.