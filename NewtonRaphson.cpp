#include<iostream>
#include<cmath>
#include <stdlib.h>

using namespace std;
float J[2][3];
float J1[2][3];
float F1(float x, float y)
{return x*x+y*y-4;
}

float F2(float x, float y) 
{return x*x-y+1;
}

void Jacobian(float x, float y)
{
float v1 = (rand() % 100 + 1)/100.0;
float v2 = (rand() % 100 + 1)/100.0;
float v3 = (rand() % 100 + 1)/100.0;
float v4 = (rand() % 100 + 1)/100.0;
J[0][0]=1*(2*x);//+v1;
J[0][1]=1*(2*y);//+v2;
J[0][2]=F1(x,y);
J[1][0]=1*(2*x);//+v3;
J[1][1]=1*(-1);//+v4;
J[1][2]=F2(x,y);
//cout<<v1<<'\t'<<v2<<'\t'<<v3<<'\t'<<v4<<endl;
}

void diagonal_matrix(float A[2][3])
{
int n=2;
float k;
for(int i=0;i<n;i++)
{
    for(int j=0;j<n;j++)
    {
        if(i!=j)
        {
            k=A[j][i]/A[i][i];
            
            for(int l=0;l<=n;l++)
            {
                A[j][l]=A[j][l]-k*A[i][l];
            }
        }
    }
}
}

int main()
{
float x=0.2;
float y=0.1;
float Dx=1000.0;
float Dy=1000.0;
float f1,f2;
int count=0;
float errorx, errory;
while(abs(Dx)>0.001 || abs(Dy)>0.001)
{
Jacobian(x,y);
diagonal_matrix(J);

f1=J[0][2];
f2=J[1][2];
//cout<<f1<<'\t'<<f2<<endl;
//cout<<J[0][0]<<'\t'<<J[1][1];
Dx=-f1/J[0][0];
Dy=-f2/J[1][1];
errorx=Dx/x;
errory=Dy/y;
x=x+Dx;
y=y+Dy;
count=count+1;
cout<<"Errorx:"<<errorx<<'\t'<<"Errory:"<<errory<<endl;
}

cout<<"x: "<<x<<'\t'<<"y: "<<y<<endl<<"f1: "<<'\t'<<F1(x,y)<<'\t'<<"f2: "<<F2(x,y)<<'\t'<<"count: "<<count<<endl;
return 0;
}

