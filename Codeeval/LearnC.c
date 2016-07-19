#include <stdio.h>
#include <string.h>
void main()
{
    int i=2;
    printf("%old %old %old %old ",i, i++,i--,i++);
    //printf("hola");
    char *zita="hard luck";
    char z[]="hard luck",space[]=" ";
    //printf("This is %s\n",zita);
    int k=strlen(zita),zn=8;
    for(k; k>=0; k--)
    {
        //printf("%c",*(zita+k));
        if(zita[k]==' ')
        {
            printf("Bonner \o");
        }
    }

}
