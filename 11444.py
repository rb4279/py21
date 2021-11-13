# https://www.acmicpc.net/problem/11444
import sys
input = sys.stdin.readline
n = int(input())
fi = [0] * (n+1)
fi[0] = 0
fi[1] = 1
fi[2] = 1
for i in range(3,n+1):
  fi[i] = fi[i-1] + fi[i-2]
print(fi[n]%1000000007)
