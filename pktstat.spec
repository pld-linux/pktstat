Summary:	Real-time packet viewer
Summary(pl):	Przegl±darka pakietów trybu rzeczywistego
Name:		pktstat
Version:	1.7.5
Release:	1
License:	BSD
Group:		Applications/Networking
Source0:	http://www.adaptive-enterprises.com.au/~d/software/pktstat/%{name}-%{version}.tar.gz
# Source0-md5:	8ce237a23f7598c06d7996d15b7cd2fb
URL:		http://www.adaptive-enterprises.com.au/~d/software/pktstat/
BuildRequires:	libpcap-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Display a real-time list of active connections seen on a network
interface, and how much bandwidth is being used by what. Partially decodes
HTTP and FTP protocols to show what filename is being transferred. X11
application names are also shown. Entries hang around on the screen for
a few seconds so you can see what just happened. Also accepts filter
expressions a'la tcpdump.

%description -l pl
Wy¶wietla na ¿ywo listê po³±czeñ widocznych na interfejsie sieciowym,
wraz z informacj± co zajmuje pasmo. W szczególno¶ci dekoduje protoko³y
HTTP oraz FTP, pokazuj±c nazwê przesy³anego pliku. Nazwy aplikacji X11
równie¿ s± pokazywane. Pozycje wy¶wietlane s± przez kilka sekund, aby
mo¿na by³o zobaczyæ co siê dzieje. Przyjmuje filtry w sk³adni podobnej
do tcpdumpa.

%prep
%setup -q

%build
%{__make} %{name} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	CPPFLAGS=-I/usr/include/ncurses

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \

install pktstat $RPM_BUILD_ROOT%{_bindir}
install pktstat.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/pktstat
%{_mandir}/man1/*
