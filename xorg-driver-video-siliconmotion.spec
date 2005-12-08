Summary:	X.org video driver for Silicon Motion video chips
Summary(pl):	Sterownik obrazu X.org dla uk³adów graficznych Silicon Motion
Name:		xorg-driver-video-siliconmotion
Version:	1.3.1.3
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/driver/xf86-video-siliconmotion-%{version}.tar.bz2
# Source0-md5:	9c6edb02ae464f67f0e71b09b8d8e9a2
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 0.99.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Silicon Motion video chips. It supports PCI
and AGP video cards based on the following chips: Lynx (SM910), LynxE
(SM810), Lynx3D (SM820), LynxEM (SM710), LynxEM+ (SM712), Lynx3DM
(SM720), Cougar3DR (SM730).

%description -l pl
Sterownik obrazu X.org dla uk³adów graficznych Silicon Motion.
Obs³uguje karty PCI i AGP oparte na nastêpuj±cych uk³adach: Lynx
(SM910), LynxE (SM810), Lynx3D (SM820), LynxEM (SM710), LynxEM+
(SM712), Lynx3DM (SM720), Cougar3DR (SM730).

%prep
%setup -q -n xf86-video-siliconmotion-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README Release.txt
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/siliconmotion_drv.so
%{_mandir}/man4/siliconmotion.4*
