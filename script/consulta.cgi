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

# Procesar el archivo CSV línea por línea
while (my $row = $csv->getline($archivo)) {
    my $line = join('|', @$row);  # Unir los campos en una línea con '|'
    my @fields = split('\|', $line);  # Separar la línea en campos

    my $nombre = $fields[1];  # El segundo campo es el nombre de la universidad
    my $periodo = $fields[4];  # Campo del periodo de licenciamiento
    my $departamento = $fields[10];  # Campo del departamento local
    my $denominacion = $fields[16];  # Campo de la denominación del programa

    # Realizar la búsqueda según los parámetros del formulario
	if (($nombre_universidad eq '' || lc $nombre =~ /\Q$nombre_universidad\E/i)) {
		# Imprimir resultados en filas de tabla
		print "<tr>";
		print "<td>$nombre</td>";
		print "<td>$periodo</td>";
		print "<td>$departamento</td>";
		print "<td>$denominacion</td>";
		print "</tr>";
	}
}

# Cerrar etiquetas HTML
print <<HTML;
    </table>
  </div>
</body>
</html>
HTML

# Cerrar el archivo CSV
close $archivo;