# ln -s ../../BibtexLibraries/global.bib main.bib
#!/bin/bash
rm *.ind *.ilg *.acn *.ain *.aux *.bbl *.blg *.glo *.idx *.ilg *.ind *.ist *.lof *.log *.lol *.lot *.syg *.out *.toc
pdflatex -shell-escape main.tex 
open -a "Preview" main.pdf
