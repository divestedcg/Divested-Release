divested-release
================

Overview
--------
A RPM repository for Divested release packages.

Prebuilts
---------
- Fedora via CI: https://gitlab.com/divested/divested-release/-/jobs/artifacts/master/browse?job=build_rpm

Building
--------
- git clone [THIS REPO]
- CentOS: rpmbuild -ba divested-release.spec
- Fedora: rpmbuild -ba divested-release.spec
