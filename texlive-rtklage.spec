%global tl_name rtklage
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A package for German lawyers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rtklage
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rtklage.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rtklage.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
RATeX is a newly developed bundle of packages and classes provided for
German lawyers. Now in the early beginning it only contains rtklage, a
class to make lawsuits.

