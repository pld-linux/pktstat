Summary:	Real-time packet viewer
Summary(pl.UTF-8):	Przeglądarka pakietów trybu rzeczywistego
Name:		pktstat
Version:	1.8.5
Release:	2
License:	BSD
Group:		Applications/Networking
Source0:	http://www.adaptive-enterprises.com.au/~d/software/pktstat/%{name}-%{version}.tar.gz
# Source0-md5:	0f387f86567eb3da1c329f7b182c3355
URL:		http://www.adaptive-enterprises.com.au/~d/software/pktstat/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Display a real-time list of active connections seen on a network
interface, and how much bandwidth is being used by what. Partially
decodes HTTP and FTP protocols to show what filename is being
transferred. X11 application names are also shown. Entries hang around
on the screen for a few seconds so you can see what just happened.
Also accepts filter expressions a'la tcpdump.

%description -l pl.UTF-8
Ten program yświetla na żywo listę połączeń widocznych na interfejsie
sieciowym, wraz z informacją, co zajmuje pasmo. W szczególności
dekoduje protokoły HTTP oraz FTP, pokazując nazwę przesyłanego pliku.
Nazwy aplikacji X11 również są pokazywane. Pozycje wyświetlane są
przez kilka sekund, aby można było zobaczyć co się dzieje. Przyjmuje
filtry w składni podobnej do tcpdumpa.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses"

%{__make} %{name} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses" \
	CPPFLAGS=-I/usr/include/ncurses

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/pktstat
%{_mandir}/man1/pktstat.1*
