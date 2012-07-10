/* write a program to blink the red or green LED on the launchpad board using msp430g2231 */

#include<msp430.h>
main()
{
	WDTCTL = WDTPW + WDTHOLD;
	P1DIR=BIT0 ;
	int n;
	while(1){
		for(n=0;n<10000;++n)
			P1OUT=BIT0;
		for(;n<20000;++n)
			P1OUT&=0;
	}
}

