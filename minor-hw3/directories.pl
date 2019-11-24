#!/usr/bin/perl
#Vasu Sharma
#110493783
#vvsharma

use strict;
use warnings;

#get result of calling echo $PATH in terminal (should be a list of directories)
my $output = qx(echo \$PATH);
chomp $output;

#store each directory name using regex to parse out forward slashes in an array
my @arr = $output =~ m/[^\/]+/g;

#print every directory name in the array on a new line
foreach my $directory (@arr) {
   print "$directory\n";
}