# Based on initial .spec file from upstream, link here https://github.com/netblue30/firejail/blob/master/platform/rpm/firejail.spec
# Originally created by Firejail authors

%define url https://github.com/netblue30/firejail

Name: firejail
Version: 0.9.56
Release: 1%{?dist}
Summary: Linux namespaces sandbox program

License: GPLv2+
Source0: %{url}/archive/%{version}.tar.gz
URL: %{url}

%description
Firejail is a SUID sandbox program that reduces the risk of security
breaches by restricting the running environment of untrusted applications
using Linux namespaces. It includes a sandbox profile for Mozilla Firefox.

%prep
%autosetup

%build
%configure --disable-userns --disable-contrib-install
make %{?_smp_mflags}

%install
%make_install
chmod 0755 %{buildroot}%{_libdir}/%{name}/lib*.so

%files
%doc README RELNOTES CONTRIBUTING.md
%license COPYING

%attr(0755, -, -) %{_bindir}/%{name}
%{_bindir}/firecfg
%{_bindir}/firemon
%{_libdir}/%{name}
%{_datarootdir}/bash-completion/completions/%{name}
%{_datarootdir}/bash-completion/completions/firecfg
%{_datarootdir}/bash-completion/completions/firemon
%{_docdir}/%{name}/COPYING
%{_mandir}/man5/%{name}-login.5.gz
%{_mandir}/man5/%{name}-profile.5.gz
%{_mandir}/man5/%{name}-users.5.gz
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/%{name}

%changelog
* Mon Oct 22 2018 Ondrej Dubaj <odubaj@redhat.com> 0.9.56-1
- First firejail RPM package for Fedora
