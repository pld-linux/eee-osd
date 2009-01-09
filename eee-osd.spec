#
%define	_rev	r19
Summary:	Scriptpack for enabling OSD-display for EeePC hotkeys
Name:		eee-osd
Version:	2.0
Release:	0.2
License:	MIT
Group:		Base
Source0:	%{name}-%{version}-%{_rev}.tar.bz2
# Source0-md5:	359a69f7893b107e774a881edc3cb869
URL:		http://code.google.com/p/eee-osd/
Requires:	acpid
Requires:	gnome-system-monitor
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This scriptpack aims at enabling the osd-display that one has with the
standard xandros os on the eee-pc on other distributions.

Furthermore it offers support for the fn-fx hotkeys for brightness,
volume control and so on.

%prep
%setup -q -n %{name}-%{version}-%{_rev}
sed -i -e 's#/usr/local/share/asus_osd#/usr/share/asus_osd#' asus_osd/asusosd.c

%build
%{__make} -C asus_osd

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/asus_osd
install -d $RPM_BUILD_ROOT%{_sysconfdir}/acpi{,/events}

install asus_osd/asusosd $RPM_BUILD_ROOT%{_bindir}/
install autostart/asusosd.desktop $RPM_BUILD_ROOT%{_datadir}/asus_osd/
install ressources/* $RPM_BUILD_ROOT%{_datadir}/asus_osd/
install events/* $RPM_BUILD_ROOT%{_sysconfdir}/acpi/events/
install scripts/{eee-wifi-on-off.sh,queryvolume.sh} $RPM_BUILD_ROOT%{_sysconfdir}/acpi/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/asusosd
%attr(755,root,root) %{_sysconfdir}/acpi/*.sh
%{_sysconfdir}/acpi/events/eee-*
%dir %{_datadir}/asus_osd
%{_datadir}/asus_osd/*
