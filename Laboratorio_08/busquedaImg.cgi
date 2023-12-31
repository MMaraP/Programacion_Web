#!/usr/bin/perl
use strict;
use warnings;

print "Content-type: text/html\n\n";
print "<!DOCTYPE html>\n";
print "<html lang='es'>\n";
print "<head>\n";
print "<meta charset='UTF-8'>\n";
print "<title>Resultado de la búsqueda de imágenes</title>\n";
print "</head>\n";
print "<body>\n";

my $query = $ENV{'QUERY_STRING'};
$query =~ s/%20/+/g;
$query =~ s/q=//;

print "<h2>Resultado de la búsqueda de imágenes para: $query</h2>\n";

# Aquí podrías realizar acciones adicionales, como consultar una base de datos o un servicio externo para obtener resultados de imágenes.

print "</body>\n";
print "</html>\n";
