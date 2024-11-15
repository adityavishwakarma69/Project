#include<stdio.h>
#include<string.h>

typedef struct{
  int x;
  int y;
}intvec2;

int isPalindrome(char* str, int start, int end)
{
  int len = end - start + 1;
  for (size_t i = 0; i < len/2; i++)
  {
    if (str[start + i] != str[end - i])
    {
      return 0;
    };
  }
  return 1;
}

intvec2 longestPalindrome(char* str, int start, int end){
  int arr[2] = {start, start};
  for(size_t i = start; i < end + 1; i++){
    for(size_t j = i; j < end + 1; j++){
      if (isPalindrome(str, i, j)){
        if ((j - i + 1) > (arr[1] - arr[0] + 1)){
          arr[0] = i;
          arr[1] = j;
        }
      /*printf("%d, %d : ", i, j);
        for (size_t k = i; k < j + 1; k++){
          printf("%c", str[k]);
        }
        printf("\n");*/
      }
    }
  }
  intvec2 vec;
  vec.x = arr[0];
  vec.y = arr[1];
  return vec;
}

int main(int argc, char *argv[])
{
  char str[1024];
  printf("enter a string : ");
  fgets(str, sizeof(str), stdin);
  int len;
  for (size_t i = 0; i < sizeof(str); i++){
    if (str[i] == 10){
      len = i;
      break;
    };
  } 

  intvec2 vec = longestPalindrome(str, 0, len - 1);

  //printf("%d, %d\n", vec.x, vec.y);

  for (size_t i = vec.x; i < vec.y + 1; i++){
    printf("%c", str[i]);
  }
  printf("\n");

  return 0;
}
