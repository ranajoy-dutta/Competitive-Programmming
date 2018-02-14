t = int(input())                                #test cases
while t > 0:
     x1,y1,x2,y2 = map(int,input().split())     #input coordinates
     maxx=max(x1,x2)                           
     minx=min(x1,x2)
     maxy=max(y1,y2)
     miny=min(y1,y2)
     count=0
     cases = int(input())
     while cases > 0:
         a,b = map(int,input().split())
         if ((a>minx) and (a<maxx) and (b<maxy) and (b>miny)):
             count += 1
         cases -= 1
     print(count)
     t -= 1
