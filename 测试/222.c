#include <stdio.h>

int main() {
    int s = 0; // 累加和
    int i = 1; // 计数器

    while (i <= 10) {
        s = s + i; // 累加
        i = i + 1; // 计数器递增
    }

    printf("累加和 s = %d\n", s); // 输出结果
    return 0;
}
