#include <stdio.h>
#include <string.h>
void main()
{
    printf("hola");
    char *zita="hard luck";
    char z[]="hard luck",space[]=" ";
    printf("This is %s\n",zita);
    int k=strlen(zita),i=0,zn=8;
    for(k; k>=0; k--)
    {
        printf("%c",*(zita+k));
        if(zita[k]==' ')
        {
            printf("Bonner");
        }
    }

}
