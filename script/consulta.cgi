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

# Definir la ruta al archivo CSV
my $csv_file = 'C:/Program Files/xampp/htdocs/PW/archivos csv/Programas de Universidades.csv';