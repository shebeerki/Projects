/*write a program to implement galois linear feeedback shift register  using P1.6 and P1.0 of launchpad */

#include<msp430.h>
#include<stdint.h>
void delay(void);
main()
{
	uint32_t lfsr = 1;
	unsigned period = 0;
	P1DIR = ( BIT6 | BIT0 ) ;
	do {
  /* taps: 32 31 29 1; characteristic polynomial: x^32 + x^31 + x^29 + x + 1 */
  		lfsr = (lfsr >> 1) ^ (-(lfsr & 1u) & 0xD0000001u); 
		P1OUT = ( BIT6 | BIT0 ) & lfsr;
		delay();
		++period;
	} while(lfsr != 1u);
}
void delay(void)
{
	int n=0 ;
	while( n++ < 10000)
		;
}
