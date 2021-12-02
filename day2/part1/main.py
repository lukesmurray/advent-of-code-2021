x,y,d=0,0,[[t,int(u)]for t,u in[v.split()for v in open('i')]]
for t,u in d:x+=u*(t=="forward");y+=u*(t=="down");y-=u*(t=="up")
print(x*y)
