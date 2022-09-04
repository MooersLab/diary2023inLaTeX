# Diary for 2023 in LaTeX

## What is this?

This repo contains a template book with 365 blank tex files, one for each day of the year.
It is set up for 2023.
It is configured to automatically generate the following:

- Chapter headings and section headings (add subsections and lower in your daily writing).
- Chapters and sections are automatically numbered.
- Table of Contents, hyperlinked
- References Cited, hyperlinked
- Index, hyperlinked
- Lists of code listings, hyperlinked
- List of Figures, hyperlinked
- List of Tables, hyperlinked
- An appendix section uses chapters that are arranged in alphabetical order by letters instead of numbers.
- Automated page numbering
- Epigraphs for Chapter header pages
- Urls in footnotes to prevent them from running into the right margin.
- Uses the minted package for syntax highlighting of code
- Supports the use of equations with captions (it is possible generate lists of equations).


The document is based on the Springer book format, but it has a 7 by 9 inch area for writing with conservative margins to save paper.


## What is this good for?

This can be used for the following purposes:

- diary
- laboratory notebook
- log book
- managing todo lists and plans
- provide material for an autobiography, biography, or to stimulate nonfiction and fiction books.
- to document one's life to inspire your descendents
- storage site for daily writing

This document's design was stimulated by the last use.
I wanted an independent place to store my daily writing on \url{750words.com} where is it stored in markdown files that are hard to search.
I wanted that writing to be indexable and searchable.
This documet has been very useful for finding information, including computer code, that I used in the past.
If it is used as a "Captian's log" of ones own "Enterprise", it can be used to gather information for annual reports.
Lists of accomplishments can be stored in the Appendix.

## Prior Experience

I have been using something like this since 2012 and this document in its current format since 2015.
Each year's document has run about 1000-1200 pages in length.
It is part of my daily routine to paste the day's writing into this document before retiring for the day or first thing in the following morning.

## Limitations

Writing in LaTeX has some limitations:

- The document is limited by computer RAM to one year. 
- The document is limited by RAM in terms of the number of lists and indices that can be generated at a time.
- Debugging can involve commenting out chapters in the 0AAAContent document to isolate the error.

I generally fall behind on my debugging and will comment out earlier chapters to prevent their errors from stopping compiling.
I debug the old writing occassionally during the year and during winter break before the start of the new year.

## Compiling

Compile with lualatex and the -escape-shell key.
The compile.sh script is run in the top level of the folder `2023diary`, which you can rename.
The document is easy to compile with the click of a button using the Overleaf website.
The empty shell document takes several seconds to compile.
A 1000 page document will compile in 30 - 60 seconds.

## Configuration

- Edit the title and author at the top of the A000Contents.tex file in the Content subfolder.
- Change the cover figure to suit by loading a new image into the Figures subfolder and by editing the path to the image to specify this new figure.
- Comment out the lists that you do not intend to use. For example, if you do not save computer code, the list of listings will not be used.

## Daily use

The documents to be edited are in chapter subfolders in the Content subfolders.
Each day's entry is in a separate tex file.
Navigate to the file corresponding to the current date and start writing on line two.
The code on the first line must remain in place for the document to compile.

Each file forms a section of a chapter.
This book has one chapter per month.
All sections for a month are in a chapter subfolder.

## On-line editor

I recommend using the on-line editor Overleaf for the smoothest operation.
I have been editing this document on Overleaf for six years.
You do NOT have to run each of the steps of compiling separately.
You just click a button and the latex and bibtex compilers are run seemlessly.
I store the URL for a specific project in my bookmarks or on my private home page for rapid access.

## Local editors

In terms of local editing, there are many text editors (>20) that are freely available and have great support for editing documents in LaTeX.
The following are perhaps the most popular editors:

- TextMate for the Mac (very easy to compile with `cmd-R`)
- Sublime Text
- VSC
- Vim
- Emacs

TextMate for the Mac does not get enough love these days.
It starts lightning fast.
It is still the editor that I open most frequently, although I am trying to migrate to Emacs.

Emacs is the most configurable editors, thanks to elisp and a dedicated developer community.

### Emacs

Must be configured to use laulatex and -escape-shell. 
It might be easiest to call the shell with `M-!` and enter `compile.sh main.tex` to compile and open in you default PDF viewer.
Or just run the compile.sh script externally to Emacs.

See the `latex-emacs` repo for a sample configuration.
If you have citations, you will have to run bibtex on main.tex.

## Best of both worlds: use local editor to edit pages on Overleaf

The Google Chrome extension supports the use of local editors to edit text areas in web browsers.
The daily.tex file is a text area when open in Overleaf.
You can bring you favorite LaTeX snippets to Overleaf.
See the end of this [slideshow]().

For the Jupyter users, you can likewise use GhostText to edit code and markdown cells with your favorite editor.
See [slideshow](https://github.com/MooersLab/DSW22ghosttext) about this exciting topic.
See corresponding [video](https://mediasite.ouhsc.edu/Mediasite/Channel/python/watch/4da0872f028c4255ae12935655e911321d).



