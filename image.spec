#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : image
Version  : 1.5.28
Release  : 8
URL      : https://files.pythonhosted.org/packages/9d/a7/70108b13af991e49deb0cbfc717cae57614eae29ff2d3fa79532eead28cb/image-1.5.28.tar.gz
Source0  : https://files.pythonhosted.org/packages/9d/a7/70108b13af991e49deb0cbfc717cae57614eae29ff2d3fa79532eead28cb/image-1.5.28.tar.gz
Summary  : Django application that provides cropping, resizing, thumbnailing, overlays and masking for images and videos with the ability to set the center of attention,
Group    : Development/Tools
License  : BSD-3-Clause
Requires: image-license = %{version}-%{release}
Requires: image-python = %{version}-%{release}
Requires: image-python3 = %{version}-%{release}
Requires: Django
Requires: Pillow
BuildRequires : Django
BuildRequires : Pillow
BuildRequires : buildreq-distutils3

%description
Please visit https://github.com/francescortiz/image

%package license
Summary: license components for the image package.
Group: Default

%description license
license components for the image package.


%package python
Summary: python components for the image package.
Group: Default
Requires: image-python3 = %{version}-%{release}

%description python
python components for the image package.


%package python3
Summary: python3 components for the image package.
Group: Default
Requires: python3-core

%description python3
python3 components for the image package.


%prep
%setup -q -n image-1.5.28
cd %{_builddir}/image-1.5.28

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579798716
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/image
cp %{_builddir}/image-1.5.28/LICENSE %{buildroot}/usr/share/package-licenses/image/2ccbe68aaa162ca353516aa5bc84e95ac707a894
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/image/2ccbe68aaa162ca353516aa5bc84e95ac707a894

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
