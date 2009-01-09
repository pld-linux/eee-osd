Summary:	Scriptpack for enabling OSD-display for EeePC hotkeys
Name:		eee-osd
Version:	2.0
Release:	0.1
License:	MIT
Group:		Base
Source0:	http://eee-osd.googlecode.com/files/%{name}-%{version}-eeexubuntu.tar.gz
# Source0-md5:	cc0c59ad054aacac47ac8003be61c756
URL:		http://code.google.com/p/eee-osd/
Requires:	acpid
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This scriptpack aims at enabling the osd-display that one has with the
standard xandros os on the eee-pc on other distributions.

Furthermore it offers support for the fn-fx hotkeys for brightness,
volume control and so on.

%prep
%setup -q -n eeexubuntu-osd

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/asus_osd
install -d $RPM_BUILD_ROOT%{_sysconfdir}/acpi{,/events}

install autostart/ASUS-OSD.desktop $RPM_BUILD_ROOT%{_datadir}/asus_osd/
install ressources/* $RPM_BUILD_ROOT%{_datadir}/asus_osd/
install binaries/asusosd $RPM_BUILD_ROOT%{_bindir}/asusosd
install events/* $RPM_BUILD_ROOT%{_sysconfdir}/acpi/events/
install scripts/{asus-brn-down.sh,asus-brn-up.sh,eee-wifi-on-off.sh,queryvolume.sh} $RPM_BUILD_ROOT%{_sysconfdir}/acpi/

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
