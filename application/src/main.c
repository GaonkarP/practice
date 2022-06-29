#include "hello.h"
#include "armstrong.h"
#include <stdio.h>

int
main (void)
{
  int retvalue = 0;
  hello ("Aniketh");
  retvalue = armstrong();
  printf("\nReturn value, %d!\n", retvalue);
  return 0;
}