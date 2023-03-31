Name:		texlive-rtklage
Version:	15878
Release:	2
Summary:	A package for German lawyers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rtklage
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rtklage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rtklage.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
RATeX is a newly developed bundle of packages and classes
provided for German lawyers. Now in the early beginning it only
contains rtklage, a class to make lawsuits.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rtklage/rtklage.cls
%doc %{_texmfdistdir}/doc/latex/rtklage/README
%doc %{_texmfdistdir}/doc/latex/rtklage/bspklage.tex
%doc %{_texmfdistdir}/doc/latex/rtklage/rtklage.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
