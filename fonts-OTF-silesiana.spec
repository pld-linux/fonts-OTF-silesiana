# TODO:
# - beautify en description
%define		_name	silesiana
Summary:	Silesian typeface
Summary(pl.UTF-8):	Śląski krój pisma
Name:		fonts-OTF-silesiana
Version:	2006
Release:	1
License:	CC BY-NC-ND 2.0
Group:		Fonts
Source0:	http://www.silesia-region.pl/silesiana/%{_name}_otf.zip
# Source0-md5:	9bddfa4e70dacf078111e87f2fc767f6
URL:		http://www.silesia-region.pl/silesiana/
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/OTF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_otffontsdir	%{_fontsdir}/OTF

%description
Silesiana is a typeface created for silesian local authorities, who
held all rights to this font. Silesiana will be used in all official
letters and documents.

Font was first introduced on 17 October, 2006. It was created after
research of typefaces of the past centuries collections of letters
from Silesian Library and Ksiaznica Cieszynska.

Henryk Sakwerda (Silesian master of caligraphy) and Artur Frankowski
(typograph) decided that the typeface should be made in italics and
based on traditional calligraphy. Silesian typeface refers to the
activity of Heronim Wietora, a 16th century publisher and typograph as
well as to the silesian currenta, a handwritten typeface derived from
gothic.

%description -l pl.UTF-8
Silesiana (nazywana również Pismem Śląskim) - krój pisma powstały na
zamówienie władz województwa śląskiego, które są właścicielem
wszystkich praw autorskich tego fontu. Silesiana będzie używana w
oficjalnych pismach i dokumentach urzędowych.

Czcionka została oficjalnie zaprezentowana 17 października 2006 roku.
Powstała w wyniku badań nad krojami pisma z minionych stuleci,
prowadzonych na podstawie zbiorów z Biblioteki Śląskiej i Książnicy
Cieszyńskiej.

Śląski mistrz kaligrafii Henryk Sakwerda oraz typograf Artur
Frankowski, którzy pracowali nad projektem zadecydowali, że pismo
powinno być pochyłe i wywodzić się z tradycyjnej kaligrafii. Krój
Silesiany nawiązuje do działalności literniczej Hieronima Wietora,
XVI?wiecznego śląskiego wydawcy i typografa oraz do śląskiej kurrenty,
odręcznego pisma wywodzącego się z gotyku.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_otffontsdir}

install *.otf $RPM_BUILD_ROOT%{_otffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst OTF

%postun
fontpostinst OTF

%files
%defattr(644,root,root,755)
%{_otffontsdir}/*
