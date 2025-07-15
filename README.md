divested-release
================

Overview
--------
A RPM repository for Divested release packages.

Prebuilts
---------
- official release: sudo dnf install https://divested.dev/rpm/fedora/divested-release-20250714-1.noarch.rpm
- Fedora via CI: https://gitlab.com/divested/divested-release/-/jobs/artifacts/master/browse?job=build_rpm

Building
--------
- git clone [THIS REPO]
- CentOS: rpmbuild -ba divested-release.spec
- Fedora: rpmbuild -ba divested-release.spec
