//#define _CRT_SECURE_NO_WARNINGS 1
//#pragma warning(disable:6031)
//#include <stdio.h>
//
//int main() {
//    int n1, n2;
//    scanf("%d", &n1); // ��������1��Ԫ�ظ���
//    int arr1[n1];
//    for (int i = 0; i < n1; i++) {
//        scanf("%d", &arr1[i]); // ��������1��Ԫ��
//    }
//    scanf("%d", &n2); // ��������2��Ԫ�ظ���
//    int arr2[n2];
//    for (int i = 0; i < n2; i++) {
//        scanf("%d", &arr2[i]); // ��������2��Ԫ��
//    }
//
//    int res[100]; // ����һ������res�����ڴ���������鲻���е�Ԫ��
//    int count = 0; // ����һ��������count������ͳ��res�����д�ŵ�Ԫ�ظ���
//    for (int i = 0; i < n1; i++) {
//        int flag = 1; // ����һ�����flag����ʾ��ǰԪ���Ƿ�Ϊ�������鹲�е�Ԫ�ء�1��ʾ�ǹ��еģ�0��ʾ���ǹ��е�
//        for (int j = 0; j < n2; j++) {
//            if (arr1[i] == arr2[j]) { // �����ǰԪ��������2��Ҳ�����ˣ���������ǲ����е�Ԫ��
//                flag = 0;
//                break;
//            }
//        }
//        if (flag == 1) { // �����ǰԪ���ǲ����е�Ԫ�أ�����ӵ�res������
//            res[count] = arr1[i];
//            count++;
//        }
//    }
//    for (int i = 0; i < n2; i++) {
//        int flag = 1;
//        for (int j = 0; j < n1; j++) {
//            if (arr2[i] == arr1[j]) {
//                flag = 0;
//                break;
//            }
//        }
//        if (flag == 1) {
//            res[count] = arr2[i];
//            count++;
//        }
//    }
//
//    // ��res�����е�Ԫ�ؽ�������
//    for (int i = 0; i < count - 1; i++) {
//        for (int j = 0; j < count - 1 - i; j++) {
//            if (res[j] > res[j + 1]) {
//                int temp = res[j];
//                res[j] = res[j + 1];
//                res[j + 1] = temp;
//            }
//        }
//    }
//
//    // ���res�����е�Ԫ��
//    for (int i = 0; i < count; i++) {
//        printf("%d ", res[i]);
//    }
//    return 0;
//}

#include <stdio.h>

int main(int argc, char *argv[])
{
	printf("hello world\n");
	
	return 0;
}
