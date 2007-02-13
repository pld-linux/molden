Summary:	A pre- and post processing program of molecular and electronic structure
Summary(pl.UTF-8):	Program do pre- i postprocessingu struktur molekularnych i elektronicznych
Name:		molden
Version:	4.3
Release:	1
License:	Free for non-commercial use
Group:		X11/Applications
Source0:	ftp://ftp.cmbi.ru.nl/pub/molgraph/molden/%{name}%{version}.tar.Z
# Source0-md5:	782101e33b837733bffc3265bb2a0292
Patch0:		%{name}-make.patch
URL:		http://www.cmbi.ru.nl/molden/molden.html
BuildRequires:	XFree86-devel
BuildRequires:	gcc-g77
BuildRequires:	glut-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Molden is a package for displaying Molecular Density from the Ab
Initio packages GAMESS-UK, GAMESS-US and GAUSSIAN and the
Semi-Empirical packages Mopac/Ampac.

%description -l pl.UTF-8
Molden to pakiet do wyświetlania gęstości cząsteczkowej z pakietów
Ab Initio GAMESS-UK, GAMESS-US i GAUSSIAN oraz pakietów Semi-Empirical
Mopac/Ampac.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1

%build
%{__make} CC="%{__cc}" OPT="%{rpmcflags}"
%{__make} CC="%{__cc}" OPT="%{rpmcflags}" moldenogl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install molden moldenogl $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.ps* COMMERCIAL_LICENSE CopyRight HISTORY README REGISTER
%attr(755,root,root) %{_bindir}/*
