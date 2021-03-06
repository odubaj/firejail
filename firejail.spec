# Based on initial .spec file from upstream, link here 
# https://github.com/netblue30/firejail/blob/master/platform/rpm/firejail.spec
# Originally created by Firejail authors

Name: firejail
Version: 0.9.56
Release: 6%{?dist}
Summary: Linux namespaces sandbox program
BuildRequires: gcc make python3-devel

# spec released under GPLv2+, contacted upstream whether it can be 
# released under MIT
License: GPLv2+
URL: https://github.com/netblue30/firejail
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

%description
Firejail is a SUID sandbox program that reduces the risk of security
breaches by restricting the running environment of untrusted applications
using Linux namespaces. It includes a sandbox profile for Mozilla Firefox.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install
chmod 0755 %{buildroot}%{_libdir}/%{name}/lib*.so
for f in \
%{buildroot}%{_libdir}/%{name}/fj-mkdeb.py \
%{buildroot}%{_libdir}/%{name}/fjclip.py \
%{buildroot}%{_libdir}/%{name}/fjdisplay.py \
%{buildroot}%{_libdir}/%{name}/fjresize.py
do
    sed -i "1 s/^.*$/\#\!\/usr\/bin\/python3/" "$f";
done

%files
%doc README RELNOTES CONTRIBUTING.md
%license COPYING

%{_bindir}/firecfg
%{_bindir}/firemon
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datarootdir}/bash-completion/completions/
%{_docdir}/%{name}/COPYING
%{_mandir}/man5/%{name}-login.5.*
%{_mandir}/man5/%{name}-profile.5.*
%{_mandir}/man5/%{name}-users.5.*
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/%{name}

%changelog
* Thu Nov 22 2018 Ondrej Dubaj <odubaj@redhat.com> 0.9.56-6
- Added python3-devel to BuildRequires, modified python shebangs

* Wed Nov 21 2018 Ondrej Dubaj <odubaj@redhat.com> 0.9.56-5
- Modified path to bash completion scripts

* Mon Nov 19 2018 Ondrej Dubaj <odubaj@redhat.com> 0.9.56-4
- Fixed problem with bash completion scripts

* Thu Nov 15 2018 Ondrej Dubaj <odubaj@redhat.com> 0.9.56-3
- Fixed .spec file according to review request comments (#1645172)

* Thu Nov 8 2018 Ondrej Dubaj <odubaj@redhat.com> 0.9.56-2
- Fixed .spec file according to review request comments (#1645172)

* Mon Oct 22 2018 Ondrej Dubaj <odubaj@redhat.com> 0.9.56-1
- First firejail RPM package for Fedora