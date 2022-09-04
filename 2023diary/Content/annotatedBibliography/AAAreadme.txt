Remember to add reference to the global bib file in alphabetical order.

~/Manuscripts/BibtexLibraries/global.bib

I wonder if there is a tool to merge bib files with references in cite keys in alphabetical order.

"bibtool -s bibliography1.bib bibliography2.bib # will merge two bib files, keeping duplicate entries.

bibtool -s -d bibliography1.bib bibliography2.bib # will merge two bib files, commenting out one of the duplicated entries."

printf "Script to make an annotated bibliography from global.bib.\n" && 
printf "It uses the annote field in the bibtex entry and the plain-annote.bst file." &&
printf "Use two pairs of backslashes to separate paragraphs with a blank line. \n"&&
printf "Use the \cite{} command to specify entries. Use the \cite{*} to print everything.\n" &&
printf
printf "To write out the cited bib entries from global.bib, use bibtool with the tex file's corresponding *.aux file.\n" &&
printf "bibtool -x annotatedbibglobal.aux -o annotatedbibglobal.bib\n" &&


JabRef and BibDesk can merge and identify duplicates. See {http://tex.stackexchange.com/questions/20027/merge-two-bibtex-files}