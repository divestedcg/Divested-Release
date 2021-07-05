Name: divested-release
Version: 20201204
Release: 1
Summary: The Divested RPM repository
License: GPLv3+
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%define _binary_payload w3T.xzdio
%define _sourcedir %(echo $PWD)
%define _rpmdir %(echo $PWD/build)

%description
- Installs the Divested RPM and GPG key

%install
install -Dm644 %{_sourcedir}/divested-release.repo %{buildroot}/etc/yum.repos.d/divested-release.repo
install -Dm644 %{_sourcedir}/RPM-GPG-KEY-divested %{buildroot}/etc/pki/rpm-gpg/RPM-GPG-KEY-divested

%files
/etc/yum.repos.d/divested-release.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-divested
