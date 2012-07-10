/* LCD Interfacing in 4 bit mode*/

#include<msp430g2231.h>

#define RS(X) 	P1OUT = ((P1OUT & ~BIT7) | (X<<7))
#define EN(X)   P1OUT = ((P1IN & ~BIT6) | (X<<6))
#define databits P1OUT  //lower nibble
#define LINE1 cmd(0x80)
#define LINE2 cmd(0xc0)

void lcd_init(void);
void port_init(void);
void LCD_STROBE(void);
void data(unsigned char c);
void cmd(unsigned char c); 
void clear(void);
void string(char *p);
void waitlcd(volatile unsigned int x);

void port_init(void)
{
    	P1OUT = 0 ;
    	P1DIR = 0xff;
}

void LCD_STROBE(void)
{   	EN(0);
    	EN(1);
    	EN(0);
}

void data(unsigned char c)
{
    	RS(1);
    	waitlcd(2);	
    	unsigned char msb , lsb;
    	msb = c >>4 ;
   	lsb = c & 0x0f;
    	databits = (databits & 0xf0) | msb;
    	LCD_STROBE();
    	databits = lsb | (databits & 0xf0);
    	LCD_STROBE();
}


void waitlcd(volatile unsigned int x)
{
	volatile unsigned int i;
	for (x ; x>1 ; x--)
	{
		for (i = 0; i <= 110; i++);
	}
}
 
void cmd(unsigned char c)
{
    	RS(0);
    	waitlcd(2);	
    	unsigned char msb , lsb ;
    	msb = c >>4 ;
    	lsb = c & 0x0f;
    	databits = (databits & 0xf0) | msb;
    	LCD_STROBE();
    	databits = lsb | (databits & 0xf0) ;
    	LCD_STROBE();
}
 
void clear(void)
{
    	cmd(0x01);
    	waitlcd(250);	
}
 
void lcd_init()
{
    	waitlcd(250);	
    	cmd(0x30);
    	waitlcd(250);	
    	cmd(0x28);            // Function set (4-bit interface, 2 lines, 5*7Pixels)
    	waitlcd(250);	
    	cmd(0x0c);            // Make cursorinvisible
    	waitlcd(250);	
    	clear();              // Clear screen
    	cmd(0x6);             // Set entry Mode(auto increment of cursor)
    	waitlcd(250);	
    	waitlcd(250);	
}
 
void string(char *p)
{
    	while(*p) 
	    	data(*p++);
}
 
int main()
{
    	port_init();
    	lcd_init();
    	LINE1;
    	string("MSP430 LCD");
    	LINE2;
    	string("INTERFACING");
    	while(1);
  
}
