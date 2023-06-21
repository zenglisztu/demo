//#define _CRT_SECURE_NO_WARNINGS 1
//#pragma warning(disable:6031)
//#include <stdio.h>
//
//int main() {
//    int n1, n2;
//    scanf("%d", &n1); // 输入数组1的元素个数
//    int arr1[n1];
//    for (int i = 0; i < n1; i++) {
//        scanf("%d", &arr1[i]); // 输入数组1的元素
//    }
//    scanf("%d", &n2); // 输入数组2的元素个数
//    int arr2[n2];
//    for (int i = 0; i < n2; i++) {
//        scanf("%d", &arr2[i]); // 输入数组2的元素
//    }
//
//    int res[100]; // 定义一个数组res，用于存放两个数组不共有的元素
//    int count = 0; // 定义一个计数器count，用于统计res数组中存放的元素个数
//    for (int i = 0; i < n1; i++) {
//        int flag = 1; // 定义一个标记flag，表示当前元素是否为两个数组共有的元素。1表示是共有的，0表示不是共有的
//        for (int j = 0; j < n2; j++) {
//            if (arr1[i] == arr2[j]) { // 如果当前元素在数组2中也出现了，则表明不是不共有的元素
//                flag = 0;
//                break;
//            }
//        }
//        if (flag == 1) { // 如果当前元素是不共有的元素，则添加到res数组中
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
//    // 对res数组中的元素进行排序
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
//    // 输出res数组中的元素
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
