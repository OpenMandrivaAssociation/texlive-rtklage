# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/rtklage
# catalog-date 2006-02-07 18:31:12 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-rtklage
Version:	20060207
Release:	9
Summary:	A package for German lawyers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rtklage
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rtklage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rtklage.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20060207-2
+ Revision: 755779
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20060207-1
+ Revision: 719470
- texlive-rtklage
- texlive-rtklage
- texlive-rtklage
- texlive-rtklage

