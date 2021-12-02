x=y=a=0
d=[[t,int(u)]for t,u in[v.split()for v in open('i')]]
for t,u in d:x+=u*(t=="forward");y+=a*u*(t=="forward");a+=u*(t=="down");a-=u*(t=="up")
print(x*y)
