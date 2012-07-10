/* write a program to light up RED led on the launchpad if push button s2 is pressed */

#include<msp430.h>
main()
{
	WDTCTL = WDTPW + WDTHOLD;
	P1DIR = BIT0;
	while(1){
		if(P1IN & BIT3)
			P1OUT=0;
		else
			P1OUT=BIT0;
	}
}
