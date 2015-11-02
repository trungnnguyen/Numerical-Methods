#include<iostream>
#include<math.h>

using namespace std;

float f(float x,float y)
{
//return 1+x+y;
return pow((1+x*x+y*y),-1.5);
}
float X(float t,float ax, float bx)
{
float x;
x=((bx-ax)*(t+1)/2.0)+ax;
return x;

}

float Y(float t, float ay, float by)
{
float y;
y=((by-ay)*(t+1)/2.0)+ay;
return y;

}

int main()
{
float ax=-1;
float ay=-1;
float bx=1;
float by=1;

float Ans;

float tax=-1;
float tay=-1;
float tbx=1;
float tby=1;

float Ax[]={1,1};
int nx=sizeof(Ax)/sizeof(Ax[0]);
float Ay[]={1,1};
int ny=sizeof(Ay)/sizeof(Ay[0]);
float T[]={-1.0/sqrt(3),1.0/sqrt(3)};

float integ=0;
float x,y;

for(int i=1; i<=nx;i++)
{
    float integx=0;
    for(int j=1; j<=ny;j++)
    {
        x=X(T[j-1],ax,bx);
        y=Y(T[j-1],ay,by);
        integx+=Ax[j-1]*f(x,y);
    }
    integx=(bx-ax)*integx*0.5;
    integ+=Ay[i-1]*integx;
}
integ=(by-ay)*integ*0.5;
Ans=integ;
cout<<Ans<<endl;
return 0;
}

