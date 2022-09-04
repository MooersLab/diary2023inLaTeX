# Makefile for NAR formatted annotated bibliography.
#
# Author: Titus Barik (titus@barik.net)
#
# Modified by Blaine Mooers
#
# Has to be run in the main directory with the main.aux generated after the full running of the compile.sh script.
# bibtool -x main.aux -o ./AnnotatedBibliography/AnnoBibMyBDA.bib
cd ../
bibtool -x main.aux -o ./annotatedBibliography/AnnoBibMain.bib
cd ./annotatedBibliography
pdflatex AnnoBibMain
bibtex AnnoBibMain
pdflatex AnnoBibMain
pdflatex AnnoBibMain
open -a "Preview.app" AnnoBibMain.pdf
echo "================================================"
echo "All done! AnnoBibMyBDA.pdf has been created. - Blaine"
echo "================================================"

# clean:
rm -rf AnnoBibMain.log AnnoBibMain.blg AnnoBibMain.bbl AnnoBibMain.aux
