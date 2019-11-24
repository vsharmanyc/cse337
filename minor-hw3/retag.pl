use strict;
use warnings;

if($#ARGV == -1){ print "file not provided!\n"; }
#elsif($ARGV[0] !~ /[^\.]+\.{1}[^\.]+/){ print "Invalid file argument! File argument must be file_name.file_type\n"}
else{
	if(open(my $file, '<:encoding(UTF-8)', $ARGV[0])){
		while(my $line = <$file>){ 
			if($line =~ /<p>/){
				$line =~ s/<p>//g;
				$line =~ s/<\/p>//g;
				$line =~ s/\n//;
				$line .= "<br><br>\n"
			}
			$line =~ s/<span>//g;
			$line =~ s/<\/span>//g;
			print "$line";
		}
	}
	else{ print "Could not open file '$ARGV[0]'\n"; }
}