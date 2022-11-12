Name:		texlive-collection-binextra
Epoch:		1
Version:	64447
Release:	1
Summary:	TeX auxiliary programs
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-binextra.r64447.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-a2ping
Requires:	texlive-adhocfilelist
Requires:	texlive-arara
Requires:	texlive-bibtex8
Requires:	texlive-bibtexu
Requires:	texlive-bundledoc
Requires:	texlive-chktex
Requires:	texlive-ctanify
Requires:	texlive-ctanupload
Requires:	texlive-ctie
Requires:	texlive-cweb
Requires:	texlive-de-macro
Requires:	texlive-detex
Requires:	texlive-dtl
Requires:	texlive-dtxgen
Requires:	texlive-dvi2tty
Requires:	texlive-dviasm
Requires:	texlive-dvicopy
Requires:	texlive-dvidvi
Requires:	texlive-dviljk
Requires:	texlive-dvipng
Requires:	texlive-dvipos
Requires:	texlive-dvisvgm
Requires:	texlive-findhyph
Requires:	texlive-fragmaster
Requires:	texlive-hyphenex
Requires:	texlive-installfont
Requires:	texlive-lacheck
Requires:	texlive-latex-git-log
Requires:	texlive-latex2man
Requires:	texlive-latexdiff
Requires:	texlive-latexfileversion
Requires:	texlive-latexmk
Requires:	texlive-latexpand
Requires:	texlive-latexindent
Requires:	texlive-ltxfileinfo
Requires:	texlive-ltximg
Requires:	texlive-listings-ext
Requires:	texlive-match_parens
Requires:	texlive-mkjobtexmf
Requires:	texlive-patgen
Requires:	texlive-pdfcrop
Requires:	texlive-pdfjam
Requires:	texlive-pdftools
Requires:	texlive-pfarrei
Requires:	texlive-pkfix
Requires:	texlive-pkfix-helper
Requires:	texlive-purifyeps
Requires:	texlive-pythontex
Requires:	texlive-seetexk
Requires:	texlive-sty2dtx
Requires:	texlive-synctex
Requires:	texlive-texcount
Requires:	texlive-texdef
Requires:	texlive-texdiff
Requires:	texlive-texdirflatten
Requires:	texlive-texdoc
Requires:	texlive-texfot
Requires:	texlive-texliveonfly
Requires:	texlive-texloganalyser
Requires:	texlive-texware
Requires:	texlive-tie
Requires:	texlive-tpic2pdftex
Requires:	texlive-typeoutfileinfo
Requires:	texlive-web

%description
Various useful, but non-essential, support programs. Includes
programs and macros for DVI file manipulation, literate
programming, patgen, and the TeX Works Editor.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
