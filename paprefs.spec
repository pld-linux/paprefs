Summary:	PulseAudio Preferences - configuration dialog for PulseAudio sound server
Summary(pl.UTF-8):   PulseAudio Preferences - konfigurator serwera dźwięku PulseAudio
Name:		paprefs
Version:	0.9.5
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://0pointer.de/lennart/projects/paprefs/%{name}-%{version}.tar.gz
# Source0-md5:	3c7688657415618996344f475cde2442
Patch0:		%{name}-desktop.patch
URL:		http://0pointer.de/lennart/projects/paprefs/
BuildRequires:	gconfmm-devel >= 2.6
BuildRequires:	gtkmm-devel >= 2.4
BuildRequires:	libglademm-devel >= 2.4
BuildRequires:	libsigc++-devel >= 2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PulseAudio Preferences (paprefs) is a simple GTK+ based configuration
dialog for the PulseAudio sound server.

%description -l pl.UTF-8
PulseAudio Preferences (paprefs) to proste, oparte na GTK+ okno
dialogowe do konfiguracji serwera dźwięku PulseAudio.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-lynx
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/paprefs
%{_datadir}/paprefs
%{_desktopdir}/paprefs.desktop
