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

# Abrir el archivo CSV
open my $archivo, '<', $csv_file or die "No se pudo abrir el archivo: $!";

# Crear objeto Text::CSV
my $csv = Text::CSV->new({ binary => 1 }) or die "No se pudo usar Text::CSV: " . Text::CSV->error_diag();

# Imprimir resultados en HTML como tabla
print <<HTML;
<!DOCTYPE html>
<html>
<head>
  <title>Resultados de la Consulta</title>
  <link rel='stylesheet' type='text/css' href='/PW/Lab_09/css/styles.css'>
</head>
<body>
  <h1>Resultados de la Consulta</h1>
  <div class="results">
    <table>
      <tr>
        <th>Nombre Universidad</th>
        <th>Periodo Licenciamiento</th>
        <th>Departamento Local</th>
        <th>Denominacion Programa</th>
      </tr>
HTML
