#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	6.3.3
%define		qtver		5.15.2
%define		kpname		kinfocenter
Summary:	kinfocenter
Name:		kp6-%{kpname}
Version:	6.3.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	27818b89503b78803aa7ac039e5592b7
URL:		http://www.kde.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= 1.4.0
BuildRequires:	kf6-kcmutils-devel
BuildRequires:	kf6-kdeclarative-devel
BuildRequires:	kf6-kdoctools-devel
BuildRequires:	libusb-devel
BuildRequires:	ninja
BuildRequires:	pciutils-devel
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Obsoletes:	kp5-%{kpname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility that provides information about a computer system.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build
rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{sr,sr@latin}

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kinfocenter
%{_desktopdir}/org.kde.kinfocenter.desktop
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kinfocenter/kcm_edid.so
%attr(755,root,root) %{_prefix}/libexec/kinfocenter-opengl-helper
%attr(755,root,root) %{_libdir}/libKInfoCenterInternal.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kcm_about-distro.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kcm_energyinfo.so
%dir %{_libdir}/qt6/plugins/plasma/kcms/kinfocenter
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kinfocenter/kcm_cpu.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kinfocenter/kcm_egl.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kinfocenter/kcm_firmware_security.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kinfocenter/kcm_glx.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kinfocenter/kcm_interrupts.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kinfocenter/kcm_kwinsupportinfo.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kinfocenter/kcm_opencl.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kinfocenter/kcm_pci.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kinfocenter/kcm_samba.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kinfocenter/kcm_usb.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kinfocenter/kcm_vulkan.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kinfocenter/kcm_wayland.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kinfocenter/kcm_xserver.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kinfocenter/kcm_audio_information.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kinfocenter/kcm_block_devices.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kinfocenter/kcm_network.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/kinfocenter/kcm_memory.so
%dir %{_libdir}/qt6/qml/org/kde/kinfocenter
%dir %{_libdir}/qt6/qml/org/kde/kinfocenter/private
%{_libdir}/qt6/qml/org/kde/kinfocenter/private/CommandOutputKCM.qml
%{_libdir}/qt6/qml/org/kde/kinfocenter/private/qmldir
%attr(755,root,root) %{_prefix}/libexec/kf6/kauth/kinfocenter-dmidecode-helper
%{_desktopdir}/kcm_about-distro.desktop
%{_desktopdir}/kcm_energyinfo.desktop
%{_datadir}/dbus-1/system-services/org.kde.kinfocenter.dmidecode.service
%{_datadir}/dbus-1/system.d/org.kde.kinfocenter.dmidecode.conf
%dir %{_datadir}/kinfocenter
%dir %{_datadir}/kinfocenter/categories
%{_datadir}/kinfocenter/categories/basicinformation.desktop
%{_datadir}/kinfocenter/categories/deviceinfocategory.desktop
%{_datadir}/kinfocenter/categories/graphicalinfocategory.desktop
%{_datadir}/kinfocenter/categories/lostfoundcategory.desktop
%{_datadir}/kinfocenter/categories/networkinfocategory.desktop
%dir %{_datadir}/kinfocenter/edid
%attr(755,root,root) %{_datadir}/kinfocenter/edid/edid.sh
%dir %{_datadir}/kinfocenter/firmware_security
%attr(755,root,root) %{_datadir}/kinfocenter/firmware_security/fwupdmgr.sh
%{_datadir}/metainfo/org.kde.kinfocenter.appdata.xml
%{_datadir}/polkit-1/actions/org.kde.kinfocenter.dmidecode.policy
