Summary:	A pre- and post processing program of molecular and electronic structure
Summary(pl):	Program do pre- i postprocessingu struktur molekularnych i elektronicznych
Name:		molden
Version:	3.7
Release:	1
License:	Free for non-commercial use
Group:		X11/Applications
Source0:	ftp://ftp.cmbi.kun.nl/pub/molgraph/molden/%{name}%{version}.tar.Z
Patch0:		%{name}-make.patch
URL:		http://www.caos.kun.nl/~schaft/molden/molden.html
BuildRequires:	XFree86-devel
BuildRequires:	gcc-g77
BuildRequires:	glut-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Molden is a package for displaying Molecular Density from the Ab
Initio packages GAMESS-UK, GAMESS-US and GAUSSIAN and the
Semi-Empirical packages Mopac/Ampac.

%description -l pl
Molden to pakiet do wy¶wietlania gêsto¶ci cz±steczkowej z pakietów
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
