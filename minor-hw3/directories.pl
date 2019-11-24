use strict;
use warnings;

my $output = qx(echo \$PATH);
my @arr = $output =~ /[^\/]+/g;
foreach my $directory (@arr) {
   print "$directory\n";
}