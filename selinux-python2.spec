# DEPRECATED (python2)
Summary:	SELinux Python 2 policy utilities
Summary(pl.UTF-8):	Narzędzia do polityk SELinuksa napisane w Pythonie 2
Name:		selinux-python2
Version:	2.9
Release:	0.1
License:	GPL v2 (sepolgen), GPL v2+ (sepolicy)
Group:		Applications/System
#Source0Download: https://github.com/SELinuxProject/selinux/wiki/Releases
Source0:	https://github.com/SELinuxProject/selinux/releases/download/20190315/selinux-python-%{version}.tar.gz
# Source0-md5:	e9dfedd1139dd9998f5a09abfb670454
URL:		https://github.com/SELinuxProject/selinux/wiki
BuildRequires:	libsepol-static >= 2.9
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	rpm-pythonprov
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Security-enhanced Linux is a patch of the Linux kernel and a number of
utilities with enhanced security functionality designed to add
mandatory access controls to Linux. The Security-enhanced Linux kernel
contains new architectural components originally developed to improve
the security of the Flask operating system. These architectural
components provide general support for the enforcement of many kinds
of mandatory access control policies, including those based on the
concepts of Type Enforcement, Role-based Access Control, and
Multi-level Security.

%description -l pl.UTF-8
Security-enhanced Linux jest prototypem jądra Linuksa i wielu
aplikacji użytkowych o funkcjach podwyższonego bezpieczeństwa.
Zaprojektowany jest tak, aby w prosty sposób ukazać znaczenie
obowiązkowej kontroli dostępu dla społeczności linuksowej. Ukazuje
również jak taką kontrolę można dodać do istniejącego systemu typu
Linux. Jądro SELinux zawiera nowe składniki architektury pierwotnie
opracowane w celu ulepszenia bezpieczeństwa systemu operacyjnego
Flask. Te elementy zapewniają ogólne wsparcie we wdrażaniu wielu typów
polityk obowiązkowej kontroli dostępu, włączając te wzorowane na: Type
Enforcement (TE), kontroli dostępu opartej na rolach (RBAC) i
zabezpieczeniach wielopoziomowych.

%package -n python-sepolgen
Summary:	sepolgen - Python 2 module for policy generation
Summary(pl.UTF-8):	Moduł Pythona 2 sepolgen do generowania polityki
License:	GPL v2
Group:		Libraries/Python
Requires:	python-selinux >= 2.9
Suggests:	python-setools
BuildArch:	noarch

%description -n python-sepolgen
Python sepolgen module for policy generation.

This package contains an old version of module, with Python 2 support.

%description -n python-sepolgen -l pl.UTF-8
Moduł Pythona sepolgen do generowania polityki.

Ten pakiet zawiera starą wersję modułu, obsługującą Pythona 2.

%package -n python-sepolicy
Summary:	Python modules for SELinux policy manipulation
Summary(pl.UTF-8):	Moduły Pythona do operowania na politykach SELinuksa
Group:		Libraries/Python
# seobject uses selinux,semanage,sepolicy,setools +IPy modules and "policycoreutils" translations domain
# seobject and sepolicy use translations from policycoreutils domain
Requires:	policycoreutils >= 2.9
Requires:	python-IPy
Requires:	python-dbus
Requires:	python-semanage >= 2.9
Requires:	python-sepolgen = %{version}-%{release}
Requires:	python-setools
Requires:	python-slip-dbus
# for sepolicy.gui additionally:
Requires:	gtk+3 >= 3
Requires:	python3-pygobject3 >= 3
Conflicts:	policycoreutils-sepolicy < 2.7

%description -n python-sepolicy
Python modules for SELinux policy manipulation.

This package contains an old version of modules, with Python 2
support.

%description -n python-sepolicy -l pl.UTF-8
Moduły Pythona do operowania na politykach SELinuksa.

Ten pakiet zawiera starą wersję modułów, obsługującą Pythona 2.

%prep
%setup -q -n selinux-python-%{version}

%build
%{__make} \
	PYTHON=%{__python} \
	SUBDIRS="sepolicy semanage sepolgen"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PYTHON=%{__python} \
	PYTHONLIBDIR=%{py_sitescriptdir} \
	LIBSEPOLA=%{_libdir}/libsepol.a

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%{__rm} -r $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_datadir}/bash-completion} \
	$RPM_BUILD_ROOT%{_mandir}/{man1,man8,ru/man1,ru/man8} \
	$RPM_BUILD_ROOT/var/lib/sepolgen

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python-sepolgen
%defattr(644,root,root,755)
%{py_sitescriptdir}/sepolgen

%files -n python-sepolicy
%defattr(644,root,root,755)
%{py_sitescriptdir}/seobject.py[co]
%dir %{py_sitedir}/sepolicy
%{py_sitedir}/sepolicy/*.py[co]
%{py_sitedir}/sepolicy/sepolicy.glade
%dir %{py_sitedir}/sepolicy/help
%{py_sitedir}/sepolicy/help/__init__.py[co]
%{py_sitedir}/sepolicy/help/*.png
%{py_sitedir}/sepolicy/help/*.txt
%dir %{py_sitedir}/sepolicy/templates
%{py_sitedir}/sepolicy/templates/*.py[co]
%{py_sitedir}/sepolicy-1.1-py*.egg-info
