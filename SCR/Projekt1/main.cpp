#include <iostream>
#include <bitset>

using namespace std;

int licznik = 0;
unsigned char p[16];
void Sprawdzanie(int ktory_wyraz);

unsigned short CRC(unsigned char *pMessage, unsigned int NumberOfBytes)
{
register unsigned short reg16 = 0xFFFF;
unsigned char reg8;
unsigned char i;

    while (NumberOfBytes--)
    {
        reg16 ^= *pMessage++;
        i = 8;

        while(i--)
        {
            if (reg16 & 0x0001)
            {
                reg16 >>= 1;
                reg16 ^= 0xA001;
            }
            else
                reg16 >>= 1;
            }
    };

    reg8 = reg16 >> 8;

    return (reg16);
}

void Sprawdzanie(int ktory_wyraz)
{
    int wyraz_nastepny = ktory_wyraz+1;

    for(int i = 0; i<256; i++)
    {
        p[ktory_wyraz] = {i};

        if(ktory_wyraz<15)
        {
            Sprawdzanie(wyraz_nastepny);

        }
        else if (ktory_wyraz==15)
        {
            unsigned short wartosc = CRC(p,16);

            bitset<16> bitset1(wartosc);

            bitset<16> bitset2({0x7CA7});

            if(bitset1==bitset2)
            {
                licznik++;
                cout<<licznik<<endl;
            }
        }
    }
}

int main()
{
    for(int i = 0; i<16;i++)
    {
        p[i]={0x11};
    }

//    Sprawdzanie(0); // Funkcja służąca do sprawdzenia liczby rozwiązań

//    cout<<licznik;

    p[6]={0x25};
    p[7]={0x05};
    p[8]={0x19};
    p[9]={0x99};

    p[14] = {0x00};
    p[15] = {0x00};

    bool czy_odkryl = false;

    int licznik = 0;

    for(int i = 0; i<256;i++)
    {
        p[14]={i};

        licznik = 0;

            do{

                unsigned short wartosc = CRC(p,16);

                bitset<16> bitset1(wartosc);

                bitset<16> bitset2({0x7CA7});

                if(bitset1==bitset2)
                {
                    czy_odkryl = true;

                    cout<<bitset1<<endl;
                    cout<<bitset2<<endl;

                    bitset<8>bitset3(p[15]);

                    cout<<"Ostatni:"<<endl;
                    cout<<bitset3<<endl;
                }

                p[15]++;

                licznik++;

            }while(!czy_odkryl&&licznik<256);

        if(czy_odkryl)
        {
            break;
        }
    }

    bitset<8>bitset3(p[14]);

    cout<<bitset3<<endl;

    return 0;
}
