Summary:	PulseAudio Preferences - configuration dialog for PulseAudio sound server
Summary(pl.UTF-8):	PulseAudio Preferences - konfigurator serwera dźwięku PulseAudio
Name:		paprefs
Version:	0.9.10
Release:	11
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://freedesktop.org/software/pulseaudio/paprefs/%{name}-%{version}.tar.xz
# Source0-md5:	e9130fb1ab5211a50b16f6b63bb6fd49
URL:		http://freedesktop.org/software/pulseaudio/paprefs/
BuildRequires:	dbus-glib-devel
BuildRequires:	gconfmm-devel >= 2.6
BuildRequires:	gettext-tools
BuildRequires:	gtkmm-devel >= 2.4
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libglademm-devel >= 2.4
BuildRequires:	libsigc++-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 1.1
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%requires_eq_to	pulseaudio pulseaudio-libs
Requires:	pulseaudio-gconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PulseAudio Preferences (paprefs) is a simple GTK+ based configuration
dialog for the PulseAudio sound server.

%description -l pl.UTF-8
PulseAudio Preferences (paprefs) to proste, oparte na GTK+ okno
dialogowe do konfiguracji serwera dźwięku PulseAudio.

%prep
%setup -q

%build
%configure \
	--disable-lynx
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/paprefs
%{_datadir}/paprefs
%{_desktopdir}/paprefs.desktop
