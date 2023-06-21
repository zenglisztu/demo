
/*题目：有 1、2、3、4 四个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

程序分析：可填在百位、十位、个位的数字都是 1、2、3、4，组成所有的排列后再去掉不满足条件的排列。*/


//#include <stdio.h>
//
//int srouNum[4] = {1,2,3,4};
//int main()
//{	
//	int r = 0;
//	int n = 0;
//	
//	int i = 0;
//	for(i ; i < 4 ; i++)
//	{	
//		int b = srouNum[i];
//		int j = 0;
//		for(j ; j < 4 ; j++)
//		{	
//			
//			int s = srouNum[j];
//			int k = 0;
//			for(k ; k < 4 ; k++)
//			{
//				int g = srouNum[k];
//				if(b!=s&&b!=g&&s!=g)
//				{
//					r = b*100 + s*10 + g;
//					printf("%d\n",r);
//					n++;
//				}
//	
//			}
//		}	
//	}
//	printf("共有 %d 个互不相同且无重复数字的三位数\n",n);
//	return 0;
// } 



