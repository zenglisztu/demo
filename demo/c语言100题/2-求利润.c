/*题目：企业发放的奖金根据利润提成。

利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%；
高于100万元时，超过100万元的部分按1%提成。
从键盘输入当月利润I，求应发放奖金总数？

程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成双精度浮点(double)型*/ 

//#include <stdio.h>
//#define  tenThousand 100000
//
//int main()
//{
//	//定义profit变量接收输入利润的变量
//	double profit = 0;
//	printf("请输入利率：");
//	scanf("%lf",&profit);
//	double bonus = 0; //奖金 
//	
//	if(profit <= tenThousand) //利润(I)低于或等于10万元时，奖金可提10%； 
//	{
//		bonus = profit*0.1;
//	}
//	else if(profit < 2*tenThousand) //利润高于10万元，低于20万元时
//	{
//		bonus = tenThousand * 0.1 + (profit - tenThousand)*0.075;
//	}
//	else if(profit < 4*tenThousand) //利润高于20万元，低于40万元时
//	{
//		bonus = tenThousand * 0.1 + tenThousand*0.075 + (profit - 2*tenThousand)*0.05;
//	}
//	else if(profit < 6*tenThousand) //40万到60万之间时高于40万元的部分，可提成3%；
//	{
//		bonus = tenThousand * 0.1 + tenThousand*0.075 + 2*tenThousand*0.05 + (profit - 4*tenThousand)*0.03;
//	}
//	else if(profit < 6*tenThousand)  //60万到100万之间时，高于60万元的部分，可提成1.5%；
//	{
//		bonus = tenThousand * 0.1 + tenThousand*0.075 + 2*tenThousand*0.05 + 2*tenThousand*0.03 + (profit - 6*tenThousand)*0.015;
//	}
//	else //高于100万元时，超过100万元的部分按1%提成。
//	{
//		bonus = tenThousand * 0.1 + tenThousand*0.075 + 2*tenThousand*0.05 + 2*tenThousand*0.03 + 4*tenThousand*0.015 + (profit - 10*tenThousand)*0.01;
//	}
//	
//	
//	printf("应发放奖金总数：%.2lf",bonus);
//	return 0;
//}


