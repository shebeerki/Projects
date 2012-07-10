/* Write a program to put ON the green LED P1.6 of launchpad using msp430g2231 */

#include<msp430.h>
void main()
{
 	WDTCTL = WDTPW + WDTHOLD;
	P1DIR = BIT6;
	P1OUT = BIT6;
	for(;;);
}

