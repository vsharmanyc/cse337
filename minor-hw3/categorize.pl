#!/usr/bin/perl
#Vasu Sharma
#110493783
#vvsharma

use strict;
use warnings;

#check if file name provided as a command line argument
if($#ARGV == -1){ print "file not provided!\n"; }
else{
	#take file name from 1st command line argument, open file, it should contain file paths
	if(open(my $file, '<', $ARGV[0])){

		#arrays will store file paths with corresponding properties 
		my @existing = ();		#stores file paths that exist (-e)
		my @readable = ();		#stores file paths that are readable (-r)
		my @writable = ();		#stores file paths that are writable (-w)
		my @executable = ();	#stores file paths that are executable (-x)
		my @plain_text = ();	#stores file paths that are plain text (-T)

		#get file paths from file, check it has a property (-e, -r, -w, -x, -T), and push to corresponding array
		foreach my $filePath (<$file>){ 
			chomp $filePath;
			if(-e $filePath){	push(@existing, $filePath);
			if(-r $filePath){	push(@readable, $filePath);}
			if(-w $filePath){	push(@writable, $filePath);}
			if(-x $filePath){	push(@executable, $filePath);}
			if(-T $filePath){	push(@plain_text, $filePath);}	} #this closing brace belongs to if(-e $filePath){ 
		}

		#print summary to STDOUT 
		#<number of files> <property> files: <corresponding file paths>
		print 0+@existing." existing files: @existing\n";
		print 0+@readable." readable files: @readable\n";
		print 0+@writable." writable files: @writable\n";
		print 0+@executable." executable files: @executable\n";
		print 0+@plain_text." plain text files: @plain_text\n";

		close $file;

		#create text files where each line is a file path of corresponding property

		#creates efiles.txt and writes file paths of files that exist
		open($file, '>', 'efiles.txt');
		foreach my $filePath (@existing){print $file "$filePath\n";} 
		close $file;

		#creates rfiles.txt and writes file paths of files that are readable
		open($file, '>', 'rfiles.txt');
		foreach my $filePath (@readable){print $file "$filePath\n";}
		close $file;

		#creates wfiles.txt and writes file paths of files that are writable
		open($file, '>', 'wfiles.txt');
		foreach my $filePath (@writable){print $file "$filePath\n";}
		close $file;

		#creates xfiles.txt and writes file paths of files that are executable
		open($file, '>', 'xfiles.txt');
		foreach my $filePath (@executable){print $file "$filePath\n";}
		close $file;

		#creates tfiles.txt and writes file paths of files that are plain text
		open($file, '>', 'tfiles.txt');
		foreach my $filePath (@plain_text){print $file "$filePath\n";}
		close $file;
	}
	#if file name taken from command line is not openable then print could not open the file 
	else{ print "Could not open file '$ARGV[0]'\n"; }
}