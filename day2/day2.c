#include <stdio.h>
#include <string.h>

int partA();
int partB();

int main() {
	printf("%d\n",partA());
	printf("%d\n",partB());
}

int partA() {
	FILE *infile = fopen("input","r");
	char dir[32];
	int val,depth=0,pos=0;
	while(fscanf(infile,"%s %d",dir,&val)!=EOF) {
		if(!strcmp(dir,"forward")) {pos+=val;}
		else if(!strcmp(dir,"up")) {depth-=val;}
		else{depth+=val;}
	}
	fclose(infile);
	return pos*depth;	
}

int partB() {
	FILE *infile = fopen("input","r");
	char dir[32];
	int val,depth=0,pos=0,aim=0;
	while(fscanf(infile,"%s %d",dir,&val)!=EOF) {
		if(!strcmp(dir,"forward")) {pos+=val;depth+=aim*val;}
		else if(!strcmp(dir,"up")) {aim-=val;}
		else{aim+=val;}
	}
	fclose(infile);
	return pos*depth;	
}