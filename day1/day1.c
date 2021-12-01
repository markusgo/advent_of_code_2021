#include <stdio.h>
//	1607429-20211201-a1c1781e
int partA() {
	FILE *infile = fopen("input","r");
	int n1,n2,res;
	res = 0;
	fscanf(infile,"%d",&n1);
	while(fscanf(infile,"%d",&n2)!=EOF) {
		res += (n2>n1)?1:0;
		n1=n2;
	}
	return res;
}

int partB() {
	FILE *infile = fopen("input","r");
	int n1,n2,n3,n4,res;
	res = 0;
	fscanf(infile,"%d",&n1);
	fscanf(infile,"%d",&n2);
	fscanf(infile,"%d",&n3);
	while(fscanf(infile,"%d",&n4)!=EOF) {
		res+=n4>n1?1:0;
		n1=n2;n2=n3;n3=n4;
	}
	return res;
}

int main() {
	printf("%d\n",partA());
	printf("%d\n",partB());
}