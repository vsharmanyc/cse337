#!/usr/bin/perl
#Vasu Sharma
#110493783
#vvsharma

use strict;
use warnings;

#check if file name provided as a command line argument
if($#ARGV == -1){ print "file not provided!\n"; }
else{
	
	#take file name from 1st command line argument, open file, it should be a html file
	if(open(my $file, '<', $ARGV[0])){
		
		#get each line from file
		while(my $line = <$file>){

			#check if there are '<p>' to find and then delete all instances
			if($line =~ s/<p>//g){
				$line =~ s/<\/p>//g;	#delete all </p>
				chomp $line;
				$line .= "<br><br>\n"	#add <br><br> to end of the line
			}

			##check if there are '<span>' to find and then delete all instances
			if($line =~ s/<span>//g){
				$line =~ s/<\/span>//g;	 #delete all </span>
			}

			#print the processed line to STDOUT
			print "$line";
		}
	}
	#if file name taken from command line is not openable then print could not open the file 
	else{ print "Could not open file '$ARGV[0]'\n"; }
}