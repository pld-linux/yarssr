Summary:	A RSS feed reader
Summary(pl):	Program do pobierania informacji w formacie RSS
Name:		yarssr
Version:	0.1.8
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/yarssr/yarssr-%{version}.tar.bz2
# Source0-md5:	d26420fe0b15156945a51ba4445e7823
Source1:	%{name}.desktop
URL:		http://yarssr.sourceforge.net/
Requires:	perl-Gtk2-GladeXML
Requires:	perl-Gtk2-TrayIcon
Requires:	perl-XML-RSS
Requires:	perl-Gnome2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YARSSR is a GTK+/GNOME RSS Reader nested in system tray.

%description -l pl
YARSSR to czytnik informacji RSS dla GTK+/GNOME dzia³aj±cy w
obszarze powiadamiania.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc ChangeLog TODO README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
