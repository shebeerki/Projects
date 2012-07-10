/* write a program to blink p1.6 randomly on launchpad making it as bit number 6 , according to a linear feedback shift register algorithm*/
#include<msp430.h>
#include<stdint.h>
void delay(void);
main()
{
	P1DIR = BIT6 ;
	uint16_t lfsr = 0xACE1u;
	unsigned bit;
	unsigned period = 0;
	do {
  /* taps: 16 14 13 11; characteristic polynomial: x^16 + x^14 + x^13 + x^11 + 1 */
  		bit  = ((lfsr >> 0) ^ (lfsr >> 2) ^ (lfsr >> 3) ^ (lfsr >> 5) ) & 1;
  		lfsr =  ( lfsr >> 1 ) | ( bit << 15) ;
  		P1OUT = lfsr & BIT6 ;
  		delay() ;
		P1OUT ^= BIT6 ; //toggling the led to know the change of its value
  		++period ;
	} while( lfsr != 0xACE1u ) ;
}
void delay(void)
{
	int n = 0 ;
	while( n++ < 32000 ) ;
}
