//��Ŀ������ĳ��ĳ��ĳ�գ��ж���һ������һ��ĵڼ��죿 


//#include <stdio.h>
//
//int main()
//{
//	int year = 0, month = 0, day = 0;
//	printf("�������ꡢ�¡��գ���ʽΪ����,��,�գ�2015,12,10��\n");
//	scanf("%d,%d,%d",&year,&month,&day);
//	
//	int sum = 0;
//	switch(month)
//	{
//		case 1  : sum = 0  ; break;
//		case 2  : sum = 31 ; break;
//		case 3  : sum = 59 ; break;
//		case 4  : sum = 90; break;
//		case 5  : sum = 120; break;
//		case 6  : sum = 151; break;
//		case 7  : sum = 181; break;
//		case 8  : sum = 212; break;
//		case 9  : sum = 243; break;
//		case 10 : sum = 273; break;
//		case 11 : sum = 304; break;
//		case 12 : sum = 334; break;
//		default : printf("month error!\n"); return -1;
//	}
//	sum += day;
//	sum = (year%400 == 0 || year%4 ==0) ? (sum + 1) : sum;
//	
//	printf("\n%d,%d,%d��%d��ĵ�%d��\n",year,month,day,year,sum);
//	return 0;
//}
