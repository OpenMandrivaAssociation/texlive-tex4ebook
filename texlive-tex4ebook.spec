%global tl_name tex4ebook
%global tl_revision 78132

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4d
Release:	%{tl_revision}.1
Summary:	Converter from LaTeX to ebook formats
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/tex4ebook
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex4ebook.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex4ebook.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(make4ht)
Requires:	texlive(tex4ebook.bin)
Requires:	tex4ht
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a bundle of Lua scripts and LaTeX packages for conversion of
LaTeX files to ebook formats such as epub, mobi and epub3. tex4ht is
used as the conversion engine.

