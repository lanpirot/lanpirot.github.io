# Build the PDF CV from the website's own _data/*.yml files.
#
#   make cv      generate assets/cv/Alexander_Boll_CV.pdf
#   make cv-tex  render the LaTeX source only (cv/build/cv.tex), no compile
#   make clean   remove LaTeX build intermediates

.PHONY: cv cv-tex clean

cv:
	python3 cv/generate_cv.py

cv-tex:
	python3 cv/generate_cv.py --tex

clean:
	rm -rf cv/build
