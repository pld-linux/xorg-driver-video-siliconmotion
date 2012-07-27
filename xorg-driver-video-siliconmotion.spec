Summary:	X.org video driver for Silicon Motion video chips
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów graficznych Silicon Motion
Name:		xorg-driver-video-siliconmotion
Version:	1.7.7
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-siliconmotion-%{version}.tar.bz2
# Source0-md5:	dc139f8ea17c40fb7bcc89181e9dbfb3
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-server >= 1.0.99.901
Provides:	xorg-driver-video
Obsoletes:	X11-driver-siliconmotion < 1:7.0.0
Obsoletes:	XFree86-driver-siliconmotion < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Silicon Motion video chips. It supports PCI and
AGP video cards based on the following chips:
- Lynx (SM910),
- LynxE (SM810),
- Lynx3D (SM820),
- LynxEM (SM710),
- LynxEM+ (SM712),
- Lynx3DM (SM720),
- Cougar3DR (SM730),
- MSOC (SM501, SM502).

%description -l pl.UTF-8
Sterownik obrazu X.org dla układów graficznych Silicon Motion.
Obsługuje karty PCI i AGP oparte na następujących układach:
- Lynx (SM910),
- LynxE (SM810),
- Lynx3D (SM820),
- LynxEM (SM710),
- LynxEM+ (SM712),
- Lynx3DM (SM720),
- Cougar3DR (SM730),
- MSOC (SM501, SM502).

%prep
%setup -q -n xf86-video-siliconmotion-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README Release.txt
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/siliconmotion_drv.so
%{_mandir}/man4/siliconmotion.4*
