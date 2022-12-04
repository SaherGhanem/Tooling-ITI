/****************************************************************************/
/****************************************************************************/
/**************************		Author: SAHER GHANEM 	*********************/
/**************************		   ITI-INTAKE43         *********************/
/**************************		DATE: 11/28/2022       	*********************/
/****************************************************************************/
/****************************************************************************/


#include <stdio.h>
#include "Std_types.h"

int main() {
	
    printf("Size of unsigned char:%d\n",sizeof(u8));
    printf("Size of pointer to unsigned char:%d\n",sizeof(pu8));
	printf("Size of unsigned short int:%d\n",sizeof(u16));
	printf("Size of pointer to unsigned short int:%d\n",sizeof(pu16));
	printf("Size of unsigned long  int:%d\n",sizeof(u32));
	printf("Size of pointer to unsigned long  int:%d\n",sizeof(pu32));
	printf("Size of unsigned long long int:%d\n",sizeof(u64));
	printf("Size of pointer to unsigned long long int:%d\n",sizeof(pu64));
	
	
	printf("Size of signed char	:%d\n",sizeof(s8));
	printf("Size of pointer to signed char:%d\n",sizeof(ps8));
	printf("Size of signed short int:%d\n",sizeof(s16));
	printf("Size of pointer to signed short int:%d\n",sizeof(ps16));
	printf("Size of signed long  int:%d\n",sizeof(s32));
	printf("Size of pointer to signed long int:%d\n",sizeof(ps32));
	printf("Size of signed long long int:%d\n",sizeof(s64));
	printf("Size of pointer to signed long long int:%d\n",sizeof(ps64));



	printf("Size of float:%d\n",sizeof(f32));
	printf("Size of pointer to float:%d\n",sizeof(pf32));
	printf("Size of double:%d\n",sizeof(f64));
	printf("Size of pointer to double:%d\n",sizeof(pf64));
	printf("Size of long double:%d\n",sizeof(f96));
	printf("Size of pointer to long double:%d\n",sizeof(pf96));


   // printf("Size of signed long double:%d\n",sizeof(long signed double));	




    return 0;
}