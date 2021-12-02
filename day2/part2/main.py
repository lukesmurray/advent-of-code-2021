x,y,a,d=0,0,0,[[t,int(u)]for t,u in[v.split()for v in open('i')]]
for t,u in d:x+=u*(t=="forward");y+=a*u*(t=="forward");a+=u*(t=="down");a-=u*(t=="up")
print(x*y)
