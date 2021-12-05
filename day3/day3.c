#include <stdio.h>
#include <string.h>
#include <math.h>

int bin2dec(char *bin);

int main() {
	FILE *infile = fopen("input","r");
	char inbin[64];
	int numbers[1000][12];
	int n=0;
	while(fscanf(infile,"%s",inbin)!=EOF) {
		for(int i=0;i<strlen(inbin);i++) {
			numbers[n][i]=(inbin[i]=='1');
			printf("%d ",numbers[n][i]);
		}
		printf("\n");
		n++;
	}
	fclose(infile);

	for(int i=0;i<)
	return 0;
}

int count_lines(FILE *file) {
	char readline[128];
	int nlines=0;
	while(fscanf(file,"%s",readline)!=EOF) {nlines++;}
}

int bin2dec(char *bin) {
	int nbits = strlen(bin),dec = 0;
	for(int i=0;i<nbits;i++) {
		dec += (bin[i]=='1')*pow(2,nbits-i-1); 
	}
	return dec;
} 