/* write a program to work like this
   Initially, RED LED (P1.0) is ON and GREEN LED (P1.6) is OFF. 	       When you press and release switch S2, RED goes OFF and GREEN comes ON.      Next time you press and release S2, RED comes ON and GREEN goes OFF ...     and so on ...*/

#include<msp430.h>
main()
{
	WDTCTL = WDTPW + WDTHOLD ;
	P1DIR = BIT6 | BIT0 ;
	while(1){
		if(P1IN & BIT3)
			P1OUT = BIT0 ;
		else
			P1OUT = BIT6;
	}
}
