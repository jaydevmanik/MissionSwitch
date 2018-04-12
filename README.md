// wap to barrier point problem in os
#include<fcntl.h>
#include<stdlib.h>
#include<stdio.h>
#include<sys/types.h>
#include<semaphore.h>
#include<unistd.h>
#include<pthread.h>



sem_t a;
int f1=0,f2=0,const2=0,const1=0,value=0,stat=0,t=0,n=0;

int  BPoint(int x)
{
    if(x>=value)
    {
	return 0;
    }
    else
    {
    return -1;
    }
}
int starting(int n)
{
	if(n>0)
	{
	stat=2;
	value=n;
	return 0;
	}
	else
	{
	return -1;
	}

}

void* process1()
{
	do{
	if(f1==0)
	{
	sem_wait(&a);
	const2++;
    printf("execution of process 1\n");
	t=BPoint(const1);
	if(t==0)
	sem_post(&a);
		{
		stat-=1;f1=1;
		printf("barrier point is reached\n");
		}
	}
	else
	{
	printf("first process stopped\n");
	if(stat==0){printf("barrier point reached\n");f1=2;}
	}
	if(f1==2){printf("process are concurrent\n");break;}
	}while(const1<value);

}
void* process2()
{
	do
	{
	if(f2==0)
	{
	sem_wait(&a);
	printf("second process started\n");
	t=BPoint(const2);
	const2++;
	if(t==0){printf("barrier point reached\n");stat-=1;f2=1;}
	sem_post(&a);
	}
	else
	{
		printf("first process stopped");
		if(stat==0){printf("barrier save point reached\n");f2=2;}
	}
	if(f2==2){printf("two process are concurrent\n");break;}
	}while(const2<value);

}

int main()
{
    pthread_t t1,t2;
    
    pthread_create(&t1,NULL,process1,NULL);
    
	pthread_create(&t2,NULL,process2,NULL);
	
	pthread_join(t1,NULL);
	
	pthread_join(t2,NULL);
	
	printf("\n Enter the barrier point :");
	scanf("%d",&n);
	t=starting(n);
	sem_init(&a,0,2);
	if(t!=0)
	{
		printf("barrier point not possible\n");
	}
    return 0;

}
