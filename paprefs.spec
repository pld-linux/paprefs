Summary:	PulseAudio Preferences - configuration dialog for PulseAudio sound server
Summary(pl.UTF-8):	PulseAudio Preferences - konfigurator serwera dźwięku PulseAudio
Name:		paprefs
Version:	1.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	https://freedesktop.org/software/pulseaudio/paprefs/%{name}-%{version}.tar.xz
# Source0-md5:	ae3261ccff40060ba39e6d3325e66c96
URL:		https://freedesktop.org/software/pulseaudio/paprefs/
BuildRequires:	gettext-tools
BuildRequires:	glibmm-devel >= 2.26
BuildRequires:	gtkmm3-devel >= 3.0
BuildRequires:	libsigc++-devel >= 2.0
BuildRequires:	meson >= 0.40.1
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 1.1
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glibmm >= 2.26
Requires:	pulseaudio
Requires:	pulseaudio-gsettings
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
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/paprefs
%{_datadir}/paprefs
%{_desktopdir}/paprefs.desktop
