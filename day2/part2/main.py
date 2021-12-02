x=y=a=0
f="forward"
d=[[t,int(u)]for t,u in[v.split()for v in open('i')]]
for t,u in d:x+=u*(t==f);y+=a*u*(t==f);a+=u*(t=="down");a-=u*(t=="up")
print(x*y)
