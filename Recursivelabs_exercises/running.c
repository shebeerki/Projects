/* program to run light led through P1.0 to P1.3 with one led lit at a time */

#include<msp430.h>
main()
{
	P1OUT=0x00 ;
	P1DIR=0x0f ;
	unsigned int i;
	for(i=1;i<10 ? (i=i<<1):(i=1);){
		P1OUT=i;
		__delay_cycles(50000);
		__delay_cycles(50000);
	}	
}
