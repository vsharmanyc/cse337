use strict;
use warnings;

if($#ARGV == -1){ print "file not provided!\n"; }
else{
	if(open(my $file, '<:encoding(UTF-8)', $ARGV[0])){
		my @existing = ();
		my @readable = ();
		my @writable = ();
		my @executable = ();
		my @plain_text = ();

		foreach my $filePath (<$file>){ 
			$filePath =~ s/\s+\z//;
			if(-e $filePath){	push(@existing, $filePath);}
			if(-r $filePath){	push(@readable, $filePath);}
			if(-w $filePath){	push(@writable, $filePath);}
			if(-x $filePath){	push(@executable, $filePath);}
			if(-T $filePath){	push(@plain_text, $filePath);}
		}

		print 0+@existing." existing files: @existing\n";
		print 0+@readable." readable files: @readable\n";
		print 0+@writable." writable files: @writable\n";
		print 0+@executable." executable files: @executable\n";
		print 0+@plain_text." plain text files: @plain_text\n";
	}
	else{ print "Could not open file '$ARGV[0]'\n"; }
}