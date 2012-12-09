# revision 27025
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-binextra
Epoch:		1
Version:	20120810
Release:	1
Summary:	TeX auxiliary programs
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-binextra.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-a2ping
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
Requires:	texlive-latex2man
Requires:	texlive-latexdiff
Requires:	texlive-latexfileversion
Requires:	texlive-latexmk
Requires:	texlive-latexpand
Requires:	texlive-listings-ext
Requires:	texlive-match_parens
Requires:	texlive-mkjobtexmf
Requires:	texlive-patgen
Requires:	texlive-pdfcrop
Requires:	texlive-pdfjam
Requires:	texlive-pdftools
Requires:	texlive-pkfix
Requires:	texlive-pkfix-helper
Requires:	texlive-purifyeps
Requires:	texlive-seetexk
Requires:	texlive-sty2dtx
Requires:	texlive-synctex
Requires:	texlive-texcount
Requires:	texlive-texdef
Requires:	texlive-texdiff
Requires:	texlive-texdirflatten
Requires:	texlive-texdoc
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
%setup -c -a0

%build

%install


%changelog
* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120810-1
+ Revision: 813900
- Update to latest release.

* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120327-1
+ Revision: 787846
- Update to latest release.

* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780192
- Update to latest release.
- Import texlive-collection-binextra
- Import texlive-collection-binextra

