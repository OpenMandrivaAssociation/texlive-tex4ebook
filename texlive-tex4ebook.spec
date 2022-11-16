Name:		texlive-tex4ebook
Version:	62076
Release:	1
Summary:	Converter from LaTeX to ebook formats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tex4ebook
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex4ebook.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex4ebook.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a bundle of Lua scripts and LaTeX packages for
conversion of LaTeX files to ebook formats such as epub, mobi
and epub3. tex4ht is used as the conversion engine.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/tex/latex/tex4ebook
%{_texmfdistdir}/texmf-dist/scripts/tex4ebook
%doc %{_texmfdistdir}/texmf-dist/doc/support/tex4ebook

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
