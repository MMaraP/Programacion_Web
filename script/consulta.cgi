#!C:\Program Files\xampp\perl\bin\perl.exe
use strict;
use warnings;
use CGI;
use Text::CSV;

# Crear objeto CGI
my $cgi = CGI->new;

# Imprimir encabezado HTTP
print $cgi->header(-type => 'text/html');

# Obtener parámetros del formulario HTML
my $nombre_universidad = $cgi->param('nombre_universidad') || '';