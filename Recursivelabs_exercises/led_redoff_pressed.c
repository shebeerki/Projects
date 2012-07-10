/* write a program to switch off RED led when push button is pressed */

#include<msp430.h>
main()
{
	WDTCTL = WDTPW + WDTHOLD ;
	P1DIR = BIT0 ;
	while(1){
		if(P1IN & BIT3)
			P1OUT = BIT0 ;
		else 
			P1OUT = 0 ;
	}
}

